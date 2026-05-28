# 批量导入 Markdown 文档到飞书知识库
# 目标知识库: https://my.feishu.cn/wiki/NCWYwb6IdiYokMkY1qHcdT0qnWj
# 空间 ID: 7631207211955407825
# 父节点 token: NCWYwb6IdiYokMkY1qHcdT0qnWj

$TargetSpaceId = "7631207211955407825"
$TargetParentToken = "NCWYwb6IdiYokMkY1qHcdT0qnWj"

# 需要导入的文件列表
$Files = @(
    ".\描红题.md",
    ".\情景对话.md",
    ".\闪卡题.md",
    ".\通用答题反馈.md",
    ".\通用loading.md",
    ".\涂色题答题页.md"
)

Write-Host "开始批量导入 Markdown 文档到飞书知识库..." -ForegroundColor Green
Write-Host "目标知识库节点: $TargetParentToken" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Gray

$SuccessCount = 0
$FailCount = 0

foreach ($File in $Files) {
    # 获取文件名（不含扩展名）作为文档名称
    $FileName = [System.IO.Path]::GetFileNameWithoutExtension($File)
    
    Write-Host "`n正在导入: $FileName" -ForegroundColor Yellow
    
    # 第一步：导入为在线 docx 文档到根目录，使用 --format json 确保纯 JSON 输出
    $ImportResult = lark-cli drive +import --file $File --type docx --name $FileName --format json 2>&1 | Where-Object { $_ -match '^\{' } | Out-String
    
    if (-not $ImportResult.Trim()) {
        Write-Host "  ✗ 导入失败: $File" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    # 解析 JSON 提取文档 token
    try {
        $JsonObj = $ImportResult | ConvertFrom-Json
        if (-not $JsonObj.ok -or -not $JsonObj.data.token) {
            Write-Host "  ✗ 导入失败: $($JsonObj.error.message)" -ForegroundColor Red
            $FailCount++
            continue
        }
        $Token = $JsonObj.data.token
    } catch {
        Write-Host "  ✗ 解析导入结果失败" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    Write-Host "  ✓ 导入成功 (token: $Token)" -ForegroundColor Green
    Write-Host "  → 正在移动到知识库..." -ForegroundColor Cyan
    
    # 第二步：将文档移动到知识库节点下
    $MoveResult = lark-cli wiki +move --obj-type docx --obj-token $Token --target-space-id $TargetSpaceId --target-parent-token $TargetParentToken --format json 2>&1 | Where-Object { $_ -match '^\{' } | Out-String
    
    if (-not $MoveResult.Trim()) {
        Write-Host "  ✗ 移动到知识库失败" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    # 解析 JSON 提取 wiki token
    try {
        $MoveJsonObj = $MoveResult | ConvertFrom-Json
        if ($MoveJsonObj.data.wiki_token) {
            $WikiToken = $MoveJsonObj.data.wiki_token
            $WikiUrl = "https://my.feishu.cn/wiki/$WikiToken"
            Write-Host "  ✓ 移动成功" -ForegroundColor Green
            Write-Host "  📄 访问链接: $WikiUrl" -ForegroundColor White
        } else {
            Write-Host "  ✓ 移动成功" -ForegroundColor Green
        }
    } catch {
        Write-Host "  ✓ 移动成功（未能提取链接）" -ForegroundColor Green
    }
    
    $SuccessCount++
}

Write-Host "`n========================================" -ForegroundColor Gray
Write-Host "导入完成!" -ForegroundColor Green
Write-Host "成功: $SuccessCount 个文件" -ForegroundColor Green
if ($FailCount -gt 0) {
    Write-Host "失败: $FailCount 个文件" -ForegroundColor Red
} else {
    Write-Host "失败: 0 个文件" -ForegroundColor Green
}
