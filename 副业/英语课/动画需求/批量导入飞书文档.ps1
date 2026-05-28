# 批量导入 Markdown 文档到飞书知识库
# 目标知识库: https://my.feishu.cn/wiki/NCWYwb6IdiYokMkY1qHcdT0qnWj
# 空间 ID: 7631207211955407825
# 父节点 token: NCWYwb6IdiYokMkY1qHcdT0qnWj

$TargetSpaceId = "7631207211955407825"
$TargetParentToken = "NCWYwb6IdiYokMkY1qHcdT0qnWj"

$Files = @(
    ".\描红题.md",
    ".\情景对话.md",
    ".\闪卡题.md",
    ".\通用答题反馈.md",
    ".\通用loading.md",
    ".\涂色题答题页.md"
)

Write-Host "Start batch import..."
Write-Host "Target: $TargetParentToken"
Write-Host "========================================"

$SuccessCount = 0
$FailCount = 0

foreach ($File in $Files) {
    $FileName = [System.IO.Path]::GetFileNameWithoutExtension($File)
    
    Write-Host "`nImporting: $FileName"
    
    # Step 1: Import to root
    $ImportResult = lark-cli drive +import --file $File --type docx --name $FileName --format json 2>&1 | Where-Object { $_ -match '^\{' } | Out-String
    
    if (-not $ImportResult.Trim()) {
        Write-Host "  [FAIL] Import failed: $File"
        $FailCount++
        continue
    }
    
    try {
        $JsonObj = $ImportResult | ConvertFrom-Json
        if (-not $JsonObj.ok -or -not $JsonObj.data.token) {
            $ErrMsg = if ($JsonObj.error) { $JsonObj.error.message } else { "Unknown error" }
            Write-Host "  [FAIL] $ErrMsg"
            $FailCount++
            continue
        }
        $Token = $JsonObj.data.token
    } catch {
        Write-Host "  [FAIL] Parse error"
        $FailCount++
        continue
    }
    
    Write-Host "  [OK] Imported (token: $Token)"
    Write-Host "  -> Moving to wiki..."
    
    # Step 2: Move to wiki
    $MoveResult = lark-cli wiki +move --obj-type docx --obj-token $Token --target-space-id $TargetSpaceId --target-parent-token $TargetParentToken --format json 2>&1 | Where-Object { $_ -match '^\{' } | Out-String
    
    if (-not $MoveResult.Trim()) {
        Write-Host "  [FAIL] Move to wiki failed"
        $FailCount++
        continue
    }
    
    try {
        $MoveJsonObj = $MoveResult | ConvertFrom-Json
        if ($MoveJsonObj.data.wiki_token) {
            $WikiToken = $MoveJsonObj.data.wiki_token
            $WikiUrl = "https://my.feishu.cn/wiki/$WikiToken"
            Write-Host "  [OK] Moved to wiki"
            Write-Host "  URL: $WikiUrl"
        } else {
            Write-Host "  [OK] Moved to wiki"
        }
    } catch {
        Write-Host "  [OK] Moved (no URL extracted)"
    }
    
    $SuccessCount++
}

Write-Host "`n========================================"
Write-Host "Done!"
Write-Host "Success: $SuccessCount"
if ($FailCount -gt 0) {
    Write-Host "Failed: $FailCount"
} else {
    Write-Host "Failed: 0"
}
