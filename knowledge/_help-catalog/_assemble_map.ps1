# One-off: raw/all-rows.json -> sprinklr-map.json (JSONL) + per-area raw .jsonl, joining local_kb.
$ErrorActionPreference = 'Stop'
$HC = Split-Path -Parent $PSCommandPath          # knowledge/_help-catalog
$KN = Split-Path -Parent $HC                     # knowledge/
$rows = Get-Content (Join-Path $HC 'raw/all-rows.json') -Raw -Encoding UTF8 | ConvertFrom-Json

# local_kb index: conversationId -> distilled file path relative to knowledge/
$idx = @{}
$rx = [regex]'sprinklr\.com/help/articles/\S*?/([0-9a-f]{16,})'
Get-ChildItem -Path $KN -Recurse -Filter *.md | Where-Object { $_.FullName -notmatch '_help-catalog' } | ForEach-Object {
  $rel = $_.FullName.Substring($KN.Length + 1).Replace('\','/')
  $txt = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
  if ($txt) { foreach ($m in $rx.Matches($txt)) { $cid = $m.Groups[1].Value; if (-not $idx.ContainsKey($cid)) { $idx[$cid] = $rel } } }
}

$areaSlug = @{ 'Sprinklr Service'='service'; 'Sprinklr Insights'='insights'; 'Sprinklr Social'='social'; 'Sprinklr Marketing'='marketing'; 'Sprinklr AI'='ai'; 'Platform'='platform' }
$mapLines = [System.Collections.Generic.List[string]]::new()
$byArea = @{}
$linked = 0
foreach ($r in $rows) {
  $cid = if ($r._cid) { $r._cid } else { ($r.url -split '/')[-1] }
  $lk = $null; if ($idx.ContainsKey($cid)) { $lk = $idx[$cid]; $linked++ }
  $obj = [ordered]@{ area=$r.area; category=$r.category; topic=$r.topic; url=$r.url; keywords=$r.keywords; local_kb=$lk }
  $line = ($obj | ConvertTo-Json -Compress -Depth 5)
  $mapLines.Add($line)
  $a = $r.area; if (-not $byArea.ContainsKey($a)) { $byArea[$a] = [System.Collections.Generic.List[string]]::new() }
  $byArea[$a].Add($line)
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllLines((Join-Path $KN 'sprinklr-map.json'), $mapLines, $utf8)
foreach ($a in $byArea.Keys) {
  $slug = $areaSlug[$a]; if ($slug) { [System.IO.File]::WriteAllLines((Join-Path $HC "raw/$slug.jsonl"), $byArea[$a], $utf8) }
}

Write-Output ("total={0} linked_local_kb={1} distilled_urls_indexed={2}" -f $rows.Count, $linked, $idx.Count)
$byArea.GetEnumerator() | Sort-Object { $_.Value.Count } -Descending | ForEach-Object { Write-Output ("  {0}: {1}" -f $_.Key, $_.Value.Count) }
