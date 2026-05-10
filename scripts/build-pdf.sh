#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dist="$root/dist"
mkdir -p "$dist"
cd "$root"

pandoc "paper/manuscript.md" \
  --quiet \
  --from markdown+tex_math_dollars+tex_math_single_backslash \
  --to html5 \
  --standalone \
  --metadata title="Agent Harnesses as Operational Control Systems" \
  --output "$dist/whitepaper.html"

python3 - "$dist/whitepaper.html" "$root/styles/paper.css" <<'PY'
from pathlib import Path
import sys

html_path = Path(sys.argv[1])
css_path = Path(sys.argv[2])
html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
html = html.replace("</head>", f"<style>\n{css}\n</style>\n</head>")
html_path.write_text(html, encoding="utf-8")
PY

weasyprint --quiet "$dist/whitepaper.html" "$dist/whitepaper.pdf"

echo "$dist/whitepaper.pdf"
