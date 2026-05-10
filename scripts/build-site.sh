#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docs="$root/docs"

mkdir -p "$docs/social"

"$root/scripts/build-pdf.sh" >/dev/null
"$root/scripts/generate-social-assets.py" >/dev/null

cp "$root/dist/whitepaper.pdf" "$docs/whitepaper.pdf"
cp "$root/dist/whitepaper.html" "$docs/whitepaper.html"
cp "$root"/social/*.png "$docs/social/"
cp "$root"/social/*.svg "$docs/social/"

echo "$docs/index.html"
