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
    
    # 第一步：导入为在线 docx 文档到根目录
    $ImportResult = lark-cli drive +import --file $File --type docx --name $FileName 2>&1
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ✗ 导入失败: $File" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    # 从 JSON 输出中提取文档 token
    $Token = ($ImportResult | ConvertFrom-Json).data.token
    
    if (-not $Token) {
        Write-Host "  ✗ 未能获取文档 token" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    Write-Host "  ✓ 导入成功 (token: $Token)" -ForegroundColor Green
    Write-Host "  → 正在移动到知识库..." -ForegroundColor Cyan
    
    # 第二步：将文档移动到知识库节点下
    $MoveResult = lark-cli wiki +move --obj-type docx --obj-token $Token --target-space-id $TargetSpaceId --target-parent-token $TargetParentToken 2>&1
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ✗ 移动到知识库失败" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    # 从 JSON 输出中提取 wiki token
    $WikiToken = ($MoveResult | ConvertFrom-Json).data.wiki_token
    
    if ($WikiToken) {
        $WikiUrl = "https://my.feishu.cn/wiki/$WikiToken"
        Write-Host "  ✓ 移动成功" -ForegroundColor Green
        Write-Host "  📄 访问链接: $WikiUrl" -ForegroundColor White
    } else {
        Write-Host "  ✓ 移动成功" -ForegroundColor Green
    }
    
    $SuccessCount++
}

Write-Host "`n========================================" -ForegroundColor Gray
Write-Host "导入完成!" -ForegroundColor Green
Write-Host "成功: $SuccessCount 个文件" -ForegroundColor Green
Write-Host "失败: $FailCount 个文件" -ForegroundColor $(if ($FailCount -gt 0) { "Red" } else { "Green" })
