#!/usr/bin/env python3
"""Generate deterministic social launch assets for the white paper."""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOCIAL = ROOT / "social"

BG = "#0B1020"
SURFACE = "#111827"
TEXT = "#F8FAFC"
SECONDARY = "#CBD5E1"
MUTED = "#94A3B8"
CYAN = "#38BDF8"
GREEN = "#34D399"
AMBER = "#FBBF24"
BORDER = "#263244"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    base = "/usr/share/fonts/truetype/dejavu"
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"{base}/{name}", size)


def draw_grid(draw: ImageDraw.ImageDraw, width: int, height: int, step: int = 32) -> None:
    for x in range(0, width, step):
        draw.line([(x, 0), (x, height)], fill="#111A2E", width=1)
    for y in range(0, height, step):
        draw.line([(0, y), (width, y)], fill="#111A2E", width=1)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        test = " ".join(current + [word])
        if draw.textlength(test, font=fnt) <= width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, width: int, fill: str, leading: int = 8) -> int:
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str = BORDER, width: int = 2, radius: int = 18) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def centered_label(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], label: str, size: int, fill: str = TEXT) -> None:
    x1, y1, x2, y2 = box
    fnt = font(size, True)
    words = label.split()
    lines = [label]
    if draw.textlength(label, font=fnt) > (x2 - x1 - 28) and len(words) > 1:
        mid = len(words) // 2
        lines = [" ".join(words[:mid]), " ".join(words[mid:])]
    total_h = len(lines) * size + (len(lines) - 1) * 4
    y = y1 + ((y2 - y1) - total_h) / 2 - 2
    for line in lines:
        draw.text((x1 + ((x2 - x1) - draw.textlength(line, font=fnt)) / 2, y), line, font=fnt, fill=fill)
        y += size + 4


def card_base(size: tuple[int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(image)
    draw_grid(draw, *size)
    return image, draw


def lane_diagram(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int) -> None:
    lane_w = (w - 60) // 2
    labels = ["Plan", "Act", "Verify", "Handoff"]
    for i, title in enumerate(["Hermes", "Codex"]):
        lx = x + i * (lane_w + 60)
        rounded(draw, (lx, y, lx + lane_w, y + h), "#0F172A", CYAN if i == 0 else GREEN)
        draw.text((lx + 28, y + 24), title, font=font(32, True), fill=TEXT)
        node_y = y + 88
        for n, label in enumerate(labels):
            color = [CYAN, SECONDARY, GREEN, AMBER][n]
            node_box = (lx + 28, node_y, lx + lane_w - 28, node_y + 54)
            rounded(draw, node_box, "#111827", color, radius=14)
            centered_label(draw, node_box, label, 23)
            node_y += 76
    center_x = x + lane_w + 30
    draw.line([(center_x, y + 50), (center_x, y + h - 50)], fill=BORDER, width=3)
    draw.text((center_x - 110, y + h - 38), "Harness Evaluation", font=font(18), fill=MUTED)


def generate_og() -> None:
    image, draw = card_base((1200, 630))
    draw.text((72, 84), "Hermes vs Codex", font=font(64, True), fill=TEXT)
    draw.text((72, 158), "Agent Harnesses", font=font(58, True), fill=TEXT)
    subtitle = "A practical comparison of agent execution, memory, tooling, and verification workflows"
    text_block(draw, (76, 252), subtitle, font(30), 520, SECONDARY, 10)
    draw.text((76, 540), "Case-study findings", font=font(22, True), fill=AMBER)
    lane_diagram(draw, 690, 96, 420, 420)
    image.save(SOCIAL / "og-card.png", quality=95)


def generate_linkedin() -> None:
    image, draw = card_base((1200, 627))
    draw.text((72, 80), "Hermes vs Codex", font=font(62, True), fill=TEXT)
    draw.text((72, 154), "Agent Harnesses", font=font(62, True), fill=TEXT)
    draw.text((76, 252), "What changes when agents get stronger execution loops?", font=font(30), fill=SECONDARY)
    chips = [("Tooling", CYAN), ("Memory", GREEN), ("Verification", AMBER), ("Handoffs", SECONDARY)]
    x = 80
    y = 454
    draw.line([(110, y + 34), (1030, y + 34)], fill=BORDER, width=3)
    for label, color in chips:
        rounded(draw, (x, y, x + 220, y + 68), SURFACE, color, radius=16)
        draw.text((x + 28, y + 18), label, font=font(25, True), fill=TEXT)
        x += 260
    image.save(SOCIAL / "linkedin-1200x627.png", quality=95)


def generate_x() -> None:
    image, draw = card_base((1600, 900))
    draw.text((96, 190), "Hermes vs Codex", font=font(92, True), fill=TEXT)
    draw.text((104, 310), "Agent harnesses compared", font=font(48, True), fill=SECONDARY)
    draw.text((108, 374), "with synthetic workflows", font=font(48, True), fill=SECONDARY)
    draw.text((108, 730), "Execution | Memory | Verification | Handoff", font=font(30), fill=AMBER)
    start_x, start_y = 970, 200
    colors = [CYAN, GREEN, AMBER, CYAN, GREEN, SECONDARY]
    for i in range(6):
        x = start_x + (i % 2) * 220
        y = start_y + i * 82
        rounded(draw, (x, y, x + 178, y + 62), "#0F172A", colors[i], radius=14)
        draw.text((x + 32, y + 16), f"Stage {i + 1}", font=font(24, True), fill=TEXT)
        if i < 5:
            x2 = start_x + ((i + 1) % 2) * 220
            y2 = start_y + (i + 1) * 82
            draw.line([(x + 178, y + 31), (x2, y2 + 31)], fill=BORDER, width=4)
    image.save(SOCIAL / "x-1600x900.png", quality=95)


def generate_square() -> None:
    image, draw = card_base((1080, 1080))
    draw.text((148, 140), "Hermes vs Codex", font=font(72, True), fill=TEXT)
    draw.text((236, 230), "Agent harness comparison", font=font(34), fill=SECONDARY)
    rounded(draw, (140, 374, 500, 578), "#0F172A", CYAN, radius=24)
    rounded(draw, (580, 374, 940, 578), "#0F172A", GREEN, radius=24)
    draw.text((232, 448), "Hermes", font=font(44, True), fill=TEXT)
    draw.text((704, 448), "Codex", font=font(44, True), fill=TEXT)
    for x, label, color in [(172, "Run", CYAN), (444, "Check", GREEN), (734, "Remember", AMBER)]:
        rounded(draw, (x, 728, x + 190, 812), SURFACE, color, radius=18)
        draw.text((x + 38, 752), label, font=font(30, True), fill=TEXT)
    draw.text((448, 936), "Launch notes", font=font(26, True), fill=MUTED)
    image.save(SOCIAL / "square-1080x1080.png", quality=95)


def box_svg(x: int, y: int, w: int, h: int, label: str, stroke: str = CYAN) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{SURFACE}" stroke="{stroke}" stroke-width="3"/>'
        f'<text x="{x + w / 2}" y="{y + h / 2 + 9}" text-anchor="middle" font-size="30" font-weight="700" fill="{TEXT}">{label}</text>'
    )


def arrow_svg(x1: int, y1: int, x2: int, y2: int) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{BORDER}" stroke-width="5" marker-end="url(#arrow)"/>'


def svg_shell(width: int, height: int, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
<title>Agent harness diagram</title>
<rect width="100%" height="100%" fill="{BG}"/>
<defs>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#111A2E" stroke-width="1"/></pattern>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{BORDER}"/></marker>
</defs>
<rect width="100%" height="100%" fill="url(#grid)"/>
<style>text {{ font-family: Inter, Geist, Arial, sans-serif; }}</style>
{body}
</svg>
'''


def svg_to_png(svg_path: Path, png_path: Path) -> None:
    # PIL cannot render SVG directly, so draw matching PNG diagrams in Python.
    if "architecture" in svg_path.name:
        draw_architecture_png(png_path)
    else:
        draw_benchmark_png(png_path)


def generate_architecture_svg() -> None:
    labels = ["User Goal", "Agent Harness", "Planning Loop", "Tool Execution", "Verification", "Result"]
    xs = [70, 320, 590, 860, 1130, 1380]
    body = ['<text x="80" y="86" font-size="44" font-weight="700" fill="#F8FAFC">Agent Harness Architecture</text>']
    for x, label in zip(xs, labels):
        body.append(box_svg(x, 260, 190, 92, label, CYAN if label != "Result" else GREEN))
    for i in range(len(xs) - 1):
        body.append(arrow_svg(xs[i] + 190, 306, xs[i + 1], 306))
    body.append(box_svg(846, 520, 220, 92, "Workspace", AMBER))
    body.append(box_svg(1106, 520, 260, 92, "Memory / Handoff", GREEN))
    body.append(arrow_svg(960, 352, 956, 520))
    body.append(arrow_svg(1230, 352, 1236, 520))
    svg = svg_shell(1600, 1000, "\n".join(body))
    path = SOCIAL / "architecture-diagram.svg"
    path.write_text(svg, encoding="utf-8")
    svg_to_png(path, SOCIAL / "architecture-diagram.png")


def generate_benchmark_svg() -> None:
    labels = ["Task Set", "Harness Run", "Tool Trace", "Outcome Check", "Quality Review", "Metrics Summary"]
    xs = [70, 310, 550, 790, 1030, 1270]
    body = ['<text x="80" y="86" font-size="44" font-weight="700" fill="#F8FAFC">Benchmark Pipeline</text>']
    for x, label in zip(xs, labels):
        body.append(box_svg(x, 290, 190, 92, label, CYAN))
    for i in range(len(xs) - 1):
        body.append(arrow_svg(xs[i] + 190, 336, xs[i + 1], 336))
    chips = ["Completion", "Correctness", "Latency", "Recovery", "Handoff Quality"]
    x = 150
    for chip in chips:
        body.append(f'<rect x="{x}" y="580" width="230" height="66" rx="22" fill="{SURFACE}" stroke="{GREEN}" stroke-width="3"/>')
        body.append(f'<text x="{x + 115}" y="623" text-anchor="middle" font-size="25" font-weight="700" fill="{TEXT}">{chip}</text>')
        x += 260
    body.append(f'<text x="80" y="806" font-size="28" fill="{MUTED}">No private data. Public-safe examples only.</text>')
    svg = svg_shell(1600, 1000, "\n".join(body))
    path = SOCIAL / "benchmark-pipeline.svg"
    path.write_text(svg, encoding="utf-8")
    svg_to_png(path, SOCIAL / "benchmark-pipeline.png")


def draw_architecture_png(path: Path) -> None:
    image, draw = card_base((1600, 1000))
    draw.text((80, 60), "Agent Harness Architecture", font=font(48, True), fill=TEXT)
    labels = ["User Goal", "Agent Harness", "Planning Loop", "Tool Execution", "Verification", "Result"]
    xs = [60, 310, 565, 820, 1085, 1350]
    for x, label in zip(xs, labels):
        width = 220 if label != "Result" else 190
        box = (x, 260, x + width, 352)
        rounded(draw, box, SURFACE, CYAN if label != "Result" else GREEN, radius=18)
        centered_label(draw, box, label, 24)
    for i in range(len(xs) - 1):
        current_w = 220 if labels[i] != "Result" else 190
        draw.line([(xs[i] + current_w, 306), (xs[i + 1], 306)], fill=BORDER, width=5)
    rounded(draw, (846, 520, 1066, 612), SURFACE, AMBER, radius=18)
    draw.text((880, 552), "Workspace", font=font(28, True), fill=TEXT)
    rounded(draw, (1106, 520, 1366, 612), SURFACE, GREEN, radius=18)
    draw.text((1138, 552), "Memory / Handoff", font=font(28, True), fill=TEXT)
    draw.line([(960, 352), (956, 520)], fill=BORDER, width=5)
    draw.line([(1230, 352), (1236, 520)], fill=BORDER, width=5)
    image.save(path, quality=95)


def draw_benchmark_png(path: Path) -> None:
    image, draw = card_base((1600, 1000))
    draw.text((80, 60), "Benchmark Pipeline", font=font(48, True), fill=TEXT)
    labels = ["Task Set", "Harness Run", "Tool Trace", "Outcome Check", "Quality Review", "Metrics Summary"]
    xs = [70, 310, 550, 790, 1030, 1270]
    for x, label in zip(xs, labels):
        rounded(draw, (x, 290, x + 190, 382), SURFACE, CYAN, radius=18)
        lines = textwrap.wrap(label, width=13)
        yy = 312 if len(lines) == 1 else 300
        for line in lines:
            draw.text((x + 95 - draw.textlength(line, font=font(24, True)) / 2, yy), line, font=font(24, True), fill=TEXT)
            yy += 31
    for i in range(len(xs) - 1):
        draw.line([(xs[i] + 190, 336), (xs[i + 1], 336)], fill=BORDER, width=5)
    chips = ["Completion", "Correctness", "Latency", "Recovery", "Handoff Quality"]
    x = 150
    for chip in chips:
        rounded(draw, (x, 580, x + 230, 646), SURFACE, GREEN, radius=22)
        draw.text((x + 115 - draw.textlength(chip, font=font(25, True)) / 2, 600), chip, font=font(25, True), fill=TEXT)
        x += 260
    draw.text((80, 806), "No private data. Public-safe examples only.", font=font(28), fill=MUTED)
    image.save(path, quality=95)


def main() -> int:
    SOCIAL.mkdir(parents=True, exist_ok=True)
    generate_og()
    generate_linkedin()
    generate_x()
    generate_square()
    generate_architecture_svg()
    generate_benchmark_svg()
    print(f"generated {SOCIAL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
