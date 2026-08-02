#!/bin/zsh
set -euo pipefail

script_dir=${0:A:h}
repo_dir=${script_dir:h}
source_dir="$repo_dir/docs"
output_dir="$repo_dir/exports/docx"
temp_dir=$(mktemp -d)

trap 'rm -rf "$temp_dir"' EXIT

mkdir -p "$output_dir"

pages=(
  privacy-policy
  coppa-direct-notice
  school-services-agreement
  data-privacy-addendum
  parent-guardian-notice
  data-retention-deletion
  security-overview
  subprocessors
  data-requests
  secure-export-delivery
)

titles=(
  Brainy-Bee-Schools-Privacy-Policy
  Brainy-Bee-Schools-COPPA-Direct-Notice
  Brainy-Bee-Schools-Services-Agreement
  Brainy-Bee-Schools-Data-Privacy-Addendum
  Brainy-Bee-Schools-Parent-Guardian-Notice
  Brainy-Bee-Schools-Data-Retention-and-Deletion-Policy
  Brainy-Bee-Schools-Security-Overview
  Brainy-Bee-Schools-Subprocessor-List
  Brainy-Bee-Schools-Data-Request-Procedure
  Brainy-Bee-Schools-Secure-Export-Delivery-Procedure
)

outputs=()
for index in {1..${#pages}}; do
  source_file="$source_dir/${pages[$index]}.html"
  docx_source="$temp_dir/${pages[$index]}.html"
  output_file="$output_dir/${titles[$index]}.docx"
  perl -0pe 's{<header\b.*?</header>}{}si; s{<footer\b.*?</footer>}{}si' "$source_file" > "$docx_source"
  textutil -convert docx -format html -baseurl "file://$source_dir/" -output "$output_file" "$docx_source" >/dev/null
  outputs+=("$output_file")
done

legal_outputs=("${outputs[@]:0:9}")
textutil -cat docx -output "$output_dir/Brainy-Bee-Schools-Legal-Documentation-Packet.docx" "${legal_outputs[@]}" >/dev/null

print "Generated ${#outputs} individual Word documents and one combined packet in $output_dir"
