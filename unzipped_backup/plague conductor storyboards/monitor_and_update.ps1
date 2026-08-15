#!/usr/bin/env pwsh
<#
PLAGUE CONDUCTOR - Monitor & Auto-Update Video
Watches for new images and regenerates video when count changes
#>

param(
    [int]$CheckInterval = 10  # seconds between checks
)

$ProductionFolder = "d:\plague conductor storyboards\00_PRODUCTION"
$VideoScript = "d:\plague conductor storyboards\create_video_smart.py"
$TargetCount = 21  # 15 current + 6 new Bridge images

function Get-ImageCount {
    $images = Get-ChildItem -Path $ProductionFolder -Recurse -Include "*.jpg","*.png" 2>$null
    return $images.Count
}

function Update-Video {
    Write-Host "`n" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "  🎬 REGENERATING VIDEO" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    
    cd "d:\plague conductor storyboards"
    python $VideoScript
}

function Show-Status {
    param([int]$Current, [int]$Target, [int]$Elapsed)
    
    $percent = [math]::Min(($Current / $Target) * 100, 100)
    $bar = "█" * [int]($percent / 5) + "░" * (20 - [int]($percent / 5))
    
    Write-Host "`r[$bar] $Current/$Target images ($([int]$percent)%) | Elapsed: ${Elapsed}s" -NoNewline -ForegroundColor Green
}

# Main loop
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
Write-Host "  📊 MONITORING IMAGE GENERATION" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
Write-Host "Checking every ${CheckInterval}s for new images..."
Write-Host "Target: $TargetCount images"
Write-Host ""

$startTime = Get-Date
$lastCount = Get-ImageCount
$startCount = $lastCount

while ($true) {
    $currentCount = Get-ImageCount
    $elapsed = [int]((Get-Date) - $startTime).TotalSeconds
    
    Show-Status $currentCount $TargetCount $elapsed
    
    if ($currentCount -gt $lastCount) {
        Write-Host ""
        Write-Host "`n✓ New images detected! ($lastCount → $currentCount)" -ForegroundColor Green
        $lastCount = $currentCount
    }
    
    if ($currentCount -ge $TargetCount) {
        Write-Host ""
        Write-Host "`n✓ Target reached! Waiting 5 seconds before video update..." -ForegroundColor Green
        Start-Sleep 5
        Update-Video
        
        Write-Host ""
        Write-Host "✓ Video updated! Location:" -ForegroundColor Green
        Write-Host "  d:\plague conductor storyboards\plague_conductor_rough_cut.mp4" -ForegroundColor Cyan
        
        # Offer to commit
        Write-Host ""
        $response = Read-Host "Commit to GitHub? (y/n)"
        if ($response -eq 'y') {
            cd "d:\plague conductor storyboards"
            git add .
            git commit -m "Add Bridge batch images (Batch 2 - 6 scenes)"
            git push
            Write-Host "✓ Pushed to GitHub!" -ForegroundColor Green
        }
        
        break
    }
    
    Start-Sleep $CheckInterval
}
