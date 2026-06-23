# Simple checklist checker for required attachments
# Usage: powershell -ExecutionPolicy Bypass -File .\scripts\check_mellekletek.ps1

$repoRoot = Resolve-Path -Path "." | Select-Object -ExpandProperty Path

$required = @(
    "KOMA.pdf",
    "IPA_igazolas.pdf",
    "DFK.pdf",
    "arajanlat_GPU.pdf",
    "arajanlat_NAS.pdf",
    "arajanlat_software.pdf",
    "arajanlat_integracio.pdf",
    "cegkivonat.pdf",
    "mesterdoc.md",
    "Palyazatok\\DIMOP_1_2_6\\dimop_126b_koltsegvetes_es_indikatorok.md"
)

$found = @()
$missing = @()

Write-Output "Repository root: $repoRoot"

foreach ($r in $required) {
    # Try exact name first
    $matches = Get-ChildItem -Path $repoRoot -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.Name -ieq $r -or $_.FullName -like "*$r*" }
    if ($matches) {
        foreach ($m in $matches) { $found += $m.FullName }
    } else {
        $missing += $r
    }
}

Write-Output "`nFound files:`n"
if ($found.Count -gt 0) { $found | ForEach-Object { Write-Output "- $_" } } else { Write-Output "(none)" }

Write-Output "`nMissing required files (upload these to EPTK as melléklet):`n"
if ($missing.Count -gt 0) { $missing | ForEach-Object { Write-Output "- $_" } } else { Write-Output "(none)" }

Write-Output "`nNote: the script looks for filenames or substrings; modify the \$required array in the script to match your actual file naming convention."