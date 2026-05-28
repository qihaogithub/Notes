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
    $RawOutput = lark-cli drive +import --file $File --type docx --name $FileName 2>&1 | Out-String
    
    # Extract JSON from output (find the first { and last })
    $JsonStart = $RawOutput.IndexOf("{")
    $JsonEnd = $RawOutput.LastIndexOf("}") + 1
    
    if ($JsonStart -lt 0 -or $JsonEnd -le $JsonStart) {
        Write-Host "  [FAIL] No valid output"
        $FailCount++
        continue
    }
    
    $JsonString = $RawOutput.Substring($JsonStart, $JsonEnd - $JsonStart)
    
    try {
        $JsonObj = $JsonString | ConvertFrom-Json
        if (-not $JsonObj.ok -or -not $JsonObj.data.token) {
            $ErrMsg = if ($JsonObj.error) { $JsonObj.error.message } else { "Unknown error" }
            Write-Host "  [FAIL] $ErrMsg"
            $FailCount++
            continue
        }
        $Token = $JsonObj.data.token
    } catch {
        Write-Host "  [FAIL] Parse error: $_"
        $FailCount++
        continue
    }
    
    Write-Host "  [OK] Imported (token: $Token)"
    Write-Host "  -> Moving to wiki..."
    
    # Step 2: Move to wiki
    $MoveRawOutput = lark-cli wiki +move --obj-type docx --obj-token $Token --target-space-id $TargetSpaceId --target-parent-token $TargetParentToken 2>&1 | Out-String
    
    $MoveJsonStart = $MoveRawOutput.IndexOf("{")
    $MoveJsonEnd = $MoveRawOutput.LastIndexOf("}") + 1
    
    if ($MoveJsonStart -lt 0 -or $MoveJsonEnd -le $MoveJsonStart) {
        Write-Host "  [FAIL] Move to wiki failed"
        $FailCount++
        continue
    }
    
    $MoveJsonString = $MoveRawOutput.Substring($MoveJsonStart, $MoveJsonEnd - $MoveJsonStart)
    
    try {
        $MoveJsonObj = $MoveJsonString | ConvertFrom-Json
        if ($MoveJsonObj.ok -and $MoveJsonObj.data.wiki_token) {
            $WikiToken = $MoveJsonObj.data.wiki_token
            $WikiUrl = "https://my.feishu.cn/wiki/$WikiToken"
            Write-Host "  [OK] Moved to wiki"
            Write-Host "  URL: $WikiUrl"
        } elseif ($MoveJsonObj.ok) {
            Write-Host "  [OK] Moved to wiki"
        } else {
            $MoveErrMsg = if ($MoveJsonObj.error) { $MoveJsonObj.error.message } else { "Unknown error" }
            Write-Host "  [FAIL] $MoveErrMsg"
            $FailCount++
            continue
        }
    } catch {
        Write-Host "  [FAIL] Parse error: $_"
        $FailCount++
        continue
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
