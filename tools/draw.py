#!/usr/bin/env python3
"""Draw the news-image-20261127 entry: one 1024x1024 image summing up
Friday 27 November 2026 world news. All artwork is drawn programmatically
with PIL (no downloaded photos or artwork). Run: python3 tools/draw.py
Writes entry.png next to the repo root (and a preview copy to out/)."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "entry.png")

BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"

NAVY = (14, 27, 46)
NAVY2 = (19, 35, 58)
GOLD = (242, 183, 5)
PAPER = (247, 243, 234)
INK = (20, 33, 61)
MUTED = (90, 100, 114)
WHITE = (255, 255, 255)

STORIES = [
    {
        "tag": "UKRAINE", "color": (43, 94, 167),
        "head": "Russia pounds Kyiv and Kharkiv",
        "cap": "Zelenskyy warns of mass strikes on the power grid",
        "glyph": "bolt",
    },
    {
        "tag": "GAZA", "color": (14, 124, 107),
        "head": "Strikes kill 10 as ceasefire strains",
        "cap": "Hamas weighs its reply after the latest deaths",
        "glyph": "shield",
    },
    {
        "tag": "RED SEA", "color": (179, 39, 30),
        "head": "Houthi missiles hit Saudi oil sites",
        "cap": "One killed at Jazan refinery; Riyadh intercepts more",
        "glyph": "rocket",
    },
    {
        "tag": "TAIWAN", "color": (30, 122, 52),
        "head": "Taiwan heads to the polls",
        "cap": "Local elections and a nuclear referendum",
        "glyph": "ballot",
    },
    {
        "tag": "INDONESIA", "color": (154, 107, 0),
        "head": "Mine flood kills 13 in Indonesia",
        "cap": "Rescuers race to reach miners still trapped",
        "glyph": "mountain",
    },
    {
        "tag": "USA", "color": (62, 92, 118),
        "head": "Thanksgiving storm lashes the East",
        "cap": "Power out and flights delayed on the East Coast",
        "glyph": "storm",
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_glyph(d, kind, cx, cy, r, color):
    """White pictogram centred at (cx, cy) inside a coloured circle."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    w = WHITE
    if kind == "bolt":
        d.polygon([(cx + 8, cy - r + 12), (cx - 14, cy + 6), (cx - 2, cy + 6),
                   (cx - 8, cy + r - 12), (cx + 14, cy - 6), (cx + 2, cy - 6)], fill=w)
    elif kind == "shield":
        d.polygon([(cx - 22, cy - 20), (cx + 22, cy - 20), (cx + 22, cy + 2),
                   (cx, cy + 24), (cx - 22, cy + 2)], fill=w)
        d.line([(cx + 4, cy - 20), (cx - 4, cy - 8), (cx + 6, cy + 2),
                (cx - 4, cy + 14)], fill=color, width=4)
    elif kind == "rocket":
        d.polygon([(cx, cy - 26), (cx + 12, cy - 2), (cx + 12, cy + 12),
                   (cx, cy + 6), (cx - 12, cy + 12), (cx - 12, cy - 2)], fill=w)
        d.polygon([(cx - 12, cy + 10), (cx - 20, cy + 22), (cx - 6, cy + 16)], fill=w)
        d.polygon([(cx + 12, cy + 10), (cx + 20, cy + 22), (cx + 6, cy + 16)], fill=w)
        d.polygon([(cx - 4, cy + 22), (cx + 4, cy + 22), (cx, cy + 30)], fill=(242, 183, 5))
    elif kind == "ballot":
        d.rectangle([cx - 22, cy - 6, cx + 22, cy + 22], fill=w)
        d.rectangle([cx - 8, cy - 6, cx + 8, cy - 2], fill=color)
        # gold check mark drawn ON the white ballot box so it stays visible
        d.line([(cx - 12, cy + 2), (cx - 3, cy + 12), (cx + 14, cy - 8)],
               fill=(242, 183, 5), width=7)
    elif kind == "mountain":
        d.polygon([(cx - 26, cy + 22), (cx, cy - 22), (cx + 26, cy + 22)], fill=w)
        d.arc([cx - 10, cy + 8, cx + 10, cy + 28], 180, 360, fill=color, width=5)
    elif kind == "storm":
        d.ellipse([cx - 24, cy - 14, cx - 2, cy + 6], fill=w)
        d.ellipse([cx - 10, cy - 20, cx + 14, cy + 6], fill=w)
        d.ellipse([cx + 2, cy - 12, cx + 24, cy + 6], fill=w)
        d.rectangle([cx - 24, cy - 2, cx + 24, cy + 6], fill=w)
        d.polygon([(cx + 4, cy + 6), (cx - 6, cy + 20), (cx + 2, cy + 20),
                   (cx - 2, cy + 30), (cx + 10, cy + 12)], fill=(242, 183, 5))


def main():
    W, H = 1024, 1024
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY2)
    f_title = font(SERIF_BOLD, 46)
    f_date = font(BOLD, 58)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 14), title, font=f_title, fill=WHITE)
    date = "FRIDAY · 27 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 66), date, font=f_date, fill=GOLD)
    d.rectangle([24, 146, W - 24, 148], fill=GOLD)

    # ---- story grid: 2 cols x 3 rows ----
    margin, gap = 24, 12
    pw = (W - 2 * margin - gap) // 2
    ph = 248
    top = 164
    f_tag = font(BOLD, 26)
    f_head = font(BOLD, 35)
    f_cap = font(REG, 24)
    for i, s in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = margin + col * (pw + gap)
        y0 = top + row * (ph + gap)
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=10, fill=PAPER)
        # tag band
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + 42], radius=10, fill=s["color"])
        d.rectangle([x0, y0 + 21, x0 + pw, y0 + 42], fill=s["color"])
        d.rectangle([x0, y0, x0 + 10, y0 + 42], fill=s["color"])
        d.rectangle([x0 + pw - 10, y0, x0 + pw, y0 + 42], fill=s["color"])
        d.text((x0 + 16, y0 + 7), s["tag"], font=f_tag, fill=WHITE)
        # headline, full panel width
        lines = wrap(d, s["head"], f_head, pw - 32)
        y = y0 + 54
        for ln in lines[:2]:
            d.text((x0 + 16, y), ln, font=f_head, fill=INK)
            y += 42
        # pictogram + caption row
        gy = y0 + ph - 62
        draw_glyph(d, s["glyph"], x0 + 62, gy, 42, s["color"])
        cap_lines = wrap(d, s["cap"], f_cap, pw - 130)
        cy = gy - 24
        for ln in cap_lines[:2]:
            d.text((x0 + 118, cy), ln, font=f_cap, fill=MUTED)
            cy += 30

    # ---- footer ----
    f_foot = font(REG, 22)
    foot = "Six stories that defined Friday 27 November 2026"
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, H - 44), foot, font=f_foot, fill=(160, 175, 195))

    img.save(OUT, optimize=True)
    print(f"wrote {OUT} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
