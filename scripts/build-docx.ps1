#Requires -Version 5.1
param([string]$OutputDirectory, [string]$SourceDirectory, [string]$EvidencePath)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$arguments = @((Join-Path $PSScriptRoot 'build-docx.py'))
if ($OutputDirectory) { $arguments += @('--output-directory', $OutputDirectory) }
if ($SourceDirectory) { $arguments += @('--source-directory', $SourceDirectory) }
if ($EvidencePath) { $arguments += @('--evidence', $EvidencePath) }
& python @arguments
if ($LASTEXITCODE -ne 0) { throw "Word generation failed (exit $LASTEXITCODE)." }
