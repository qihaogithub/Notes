# Batch Import Markdown to Feishu Wiki
# Target: https://my.feishu.cn/wiki/NCWYwb6IdiYokMkY1qHcdT0qnWj
# Space ID: 7631207211955407825
# Parent token: NCWYwb6IdiYokMkY1qHcdT0qnWj

$SpaceId = "7631207211955407825"
$ParentToken = "NCWYwb6IdiYokMkY1qHcdT0qnWj"

$Files = @(
    ".\描红题.md",
    ".\情景对话.md",
    ".\闪卡题.md",
    ".\通用答题反馈.md",
    ".\通用loading.md",
    ".\涂色题答题页.md"
)

Write-Host "Start batch import..."
Write-Host "========================================"

$SuccessCount = 0
$FailCount = 0

foreach ($File in $Files) {
    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($File)
    
    Write-Host "`nImporting: $BaseName"
    
    # Step 1: Import
    $Output1 = lark-cli drive +import --file $File --type docx --name $BaseName 2>&1 | Out-String
    $Json1 = $Output1 -replace '[\s\S]*?(\{[\s\S]*\})[\s\S]*?', '$1'
    
    try {
        $Obj1 = $Json1 | ConvertFrom-Json
        if (-not $Obj1.ok) {
            Write-Host "  FAIL: $($Obj1.error.message)"
            $FailCount++
            continue
        }
        $Token = $Obj1.data.token
    } catch {
        Write-Host "  FAIL: Parse error"
        $FailCount++
        continue
    }
    
    Write-Host "  OK: token=$Token"
    
    # Step 2: Move to wiki
    $Output2 = lark-cli wiki +move --obj-type docx --obj-token $Token --target-space-id $SpaceId --target-parent-token $ParentToken 2>&1 | Out-String
    $Json2 = $Output2 -replace '[\s\S]*?(\{[\s\S]*\})[\s\S]*?', '$1'
    
    try {
        $Obj2 = $Json2 | ConvertFrom-Json
        if ($Obj2.ok -and $Obj2.data.wiki_token) {
            Write-Host "  OK: https://my.feishu.cn/wiki/$($Obj2.data.wiki_token)"
        } elseif ($Obj2.ok) {
            Write-Host "  OK: moved"
        } else {
            Write-Host "  FAIL: $($Obj2.error.message)"
            $FailCount++
            continue
        }
    } catch {
        Write-Host "  FAIL: Parse error"
        $FailCount++
        continue
    }
    
    $SuccessCount++
}

Write-Host "`n========================================"
Write-Host "Done! Success=$SuccessCount Failed=$FailCount"
