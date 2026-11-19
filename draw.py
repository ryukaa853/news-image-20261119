#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Vector-style editorial infographic, drawn with PIL only. No network, no
randomness: the same script always writes the same bytes.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)      # warm newsprint
INK = (20, 33, 61)           # deep navy
NAVY = (20, 33, 61)
RED = (178, 34, 34)
GOLD = (184, 134, 11)
TEAL = (15, 118, 110)
GREEN = (22, 101, 52)
PURPLE = (88, 28, 135)
GREY = (90, 90, 90)
PANEL = (255, 255, 255)
BORDER = (20, 33, 61)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F + "DejaVuSerif-Bold.ttf"
SANS_B = F + "DejaVuSans-Bold.ttf"
SANS = F + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap using real pixel widths."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_panel(d, x, y, w, h, kicker, kicker_color, headline, body,
               hl_size=30, body_size=19, illo=None):
    """One news panel: white card, kicker chip, headline, body, illustration.

    The illustration is drawn in whatever space is left below the text, so
    text and art can never overlap.
    """
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=PANEL, outline=BORDER, width=2)
    pad = 18
    cx = x + pad
    cy = y + 14
    # kicker chip
    kf = font(SANS_B, 17)
    kw = d.textlength(kicker, font=kf) + 20
    d.rounded_rectangle([cx, cy, cx + kw, cy + 26], radius=4, fill=kicker_color)
    d.text((cx + 10, cy + 4), kicker, font=kf, fill=(255, 255, 255))
    cy += 36
    # headline
    hf = font(SANS_B, hl_size)
    for line in wrap(d, headline, hf, w - 2 * pad):
        d.text((cx, cy), line, font=hf, fill=INK)
        cy += hl_size + 6
    cy += 4
    # body
    bf = font(SANS, body_size)
    for line in wrap(d, body, bf, w - 2 * pad):
        d.text((cx, cy), line, font=bf, fill=(40, 40, 40))
        cy += body_size + 5
    # illustration strip in the remaining space
    if illo is not None:
        iy = cy + 6
        ih = (y + h - 10) - iy
        if ih >= 30:
            illo(d, x + pad, iy, w - 2 * pad, ih)


def flag_us(d, x, y, w, h):
    stripe = h / 13.0
    for i in range(13):
        if i % 2 == 0:
            d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe],
                        fill=(178, 34, 34))
    cw, ch = w * 0.4, stripe * 7
    d.rectangle([x, y, x + cw, y + ch], fill=(20, 33, 61))
    for r in range(4):
        for c in range(5):
            sx = x + 6 + c * (cw - 12) / 4
            sy = y + 5 + r * (ch - 10) / 3
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.ellipse([x + 10, y + 10, x + 34, y + 34], fill=(255, 222, 0))
    for sx, sy in [(52, 14), (62, 26), (60, 42), (46, 48)]:
        d.ellipse([x + sx, y + sy, x + sx + 9, y + sy + 9], fill=(255, 222, 0))


def flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 50))
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=(120, 120, 120), width=1)


def illo_summit(d, x, y, w, h):
    fh = min(72, h - 18)
    fw = (w - 32) // 3
    flag_us(d, x, y, fw, fh)
    flag_cn(d, x + fw + 16, y, fw, fh)
    flag_ru(d, x + 2 * fw + 32, y, fw, fh)
    d.text((x + w // 2, y + fh + 3), "SHENZHEN, CHINA",
           font=font(SANS_B, 13), fill=TEAL, anchor="ma")


def illo_scales(d, x, y, w, h):
    cx = x + w // 2
    top, bot = y + 2, y + h - 6
    mid = top + int((bot - top) * 0.22)
    pan_y = top + int((bot - top) * 0.72)
    d.line([cx, top, cx, bot], fill=INK, width=4)
    d.line([cx - 68, mid, cx + 68, mid], fill=INK, width=4)
    d.line([cx, bot, cx - 24, bot + 2], fill=INK, width=4)
    d.line([cx, bot, cx + 24, bot + 2], fill=INK, width=4)
    for px in (cx - 68, cx + 68):
        d.line([px, mid, px - 19, pan_y], fill=INK, width=3)
        d.line([px, mid, px + 19, pan_y], fill=INK, width=3)
        d.arc([px - 19, pan_y - 6, px + 19, pan_y + 16], start=0, end=180,
              fill=INK, width=3)
    d.ellipse([cx - 5, top - 2, cx + 5, top + 8], fill=GOLD)


def illo_gta(d, x, y, w, h):
    # sunset gradient
    top, mid, bot = (255, 154, 61), (232, 74, 122), (107, 63, 160)
    for i in range(h):
        t = i / max(h - 1, 1)
        if t < 0.5:
            c = tuple(int(top[j] + (mid[j] - top[j]) * t * 2) for j in range(3))
        else:
            c = tuple(int(mid[j] + (bot[j] - mid[j]) * (t - 0.5) * 2)
                        for j in range(3))
        d.line([x, y + i, x + w, y + i], fill=c)
    # skyline
    for bx, bw_, bh in [(0, 30, int(h * 0.3)), (36, 26, int(h * 0.45)),
                        (68, 30, int(h * 0.32)), (104, 26, int(h * 0.5))]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw_, y + h], fill=(40, 20, 60))
    # palm silhouette (right side): trunk + drooping fronds
    px, py = x + w - 64, y + 10
    d.line([px, y + h, px + 10, py], fill=(40, 20, 60), width=5)
    for ex, ey in [(-42, -6), (-34, 14), (-16, -18), (16, -18),
                   (34, 14), (42, -6)]:
        mx, my = px + 10 + ex // 2, py + ey // 2 - 6
        d.line([px + 10, py, mx, my, px + 10 + ex, py + ey],
               fill=(40, 20, 60), width=3, joint="curve")
    # big VI
    vf = font(SANS_B, max(28, int(h * 0.85)))
    d.text((x + 12, y - 2), "VI", font=vf, fill=(255, 255, 255),
           stroke_width=2, stroke_fill=(40, 20, 60))


def illo_ipo(d, x, y, w, h):
    label_h = min(28, h // 3)
    d.text((x + 4, y), "$81BN", font=font(SANS_B, label_h), fill=INK)
    bars = [0.42, 0.55, 0.50, 0.68, 0.82, 1.0]
    bw = (w - 40) // len(bars)
    base = y + h
    for i, frac in enumerate(bars):
        bh = int((h - label_h - 6) * frac)
        bx = x + 6 + i * bw
        d.rectangle([bx, base - bh, bx + bw - 8, base],
                    fill=(22, 101, 52) if i < 5 else TEAL)
    # rising arrow above the bars
    d.line([x + 4, base - int((h - label_h) * 0.42),
            x + w - 6, y + label_h + 2], fill=RED, width=4)
    d.polygon([(x + w - 6, y + label_h + 2), (x + w - 22, y + label_h + 2),
               (x + w - 6, y + label_h + 16)], fill=RED)


def illo_riyadh(d, x, y, w, h):
    # night sky
    d.rectangle([x, y, x + w, y + h], fill=(20, 33, 61))
    # buildings
    for bx, bw_, bh in [(0, 46, int(h * 0.55)), (56, 40, int(h * 0.72)),
                        (106, 52, int(h * 0.48))]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw_, y + h],
                    fill=(60, 80, 120))
    # twisted PIF tower
    tx = x + w - 92
    d.polygon([(tx, y + h), (tx + 10, y + 4), (tx + 44, y + 4), (tx + 54, y + h)],
              fill=(150, 180, 220))
    for i in range(5):
        yy = y + 12 + i * max(8, (h - 20) // 5)
        d.line([tx + 8 + i, yy, tx + 46 - i, yy], fill=(20, 33, 61), width=2)
    # missile streak
    d.line([x + 8, y + 8, x + w - 112, y + h // 2], fill=(255, 200, 60), width=4)
    d.ellipse([x + w - 120, y + h // 2 - 8, x + w - 104, y + h // 2 + 8],
              fill=(255, 120, 40))
    d.text((x + 8, y + h - 22), "RIYADH", font=font(SANS_B, 14),
           fill=(255, 255, 255))


def illo_wars(d, x, y, w, h):
    # bridge deck with a gap in the middle, over water
    deck_y = y + int(h * 0.42)
    d.rectangle([x, deck_y + 10, x + w, y + h], fill=(30, 90, 140))
    d.line([x, deck_y, x + w // 2 - 24, deck_y], fill=INK, width=7)
    d.line([x + w // 2 + 24, deck_y, x + w, deck_y], fill=INK, width=7)
    for bx in range(x + 8, x + w, 26):
        if abs(bx + 10 - (x + w // 2)) > 32:
            d.line([bx, deck_y, bx, deck_y + 10], fill=INK, width=4)
    # explosion starburst in the gap
    cx, cy = x + w // 2, deck_y - 6
    for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 14),
                   (-12, -12), (12, -12), (-12, 12), (12, 12)]:
        d.line([cx, cy, cx + dx, cy + dy], fill=(255, 140, 0), width=4)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(255, 200, 60))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 116], fill=NAVY)
    d.text((W // 2, 12), "THE WORLD IN ONE DAY", font=font(SERIF_B, 52),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 74), "THURSDAY  •  19 NOVEMBER 2026",
           font=font(SANS_B, 30), fill=(255, 200, 60), anchor="ma")
    d.rectangle([0, 116, W, 120], fill=RED)

    # ---- row A: summit (lead) + ICJ ----
    draw_panel(d, 24, 134, 600, 316, "SHENZHEN SUMMIT", RED,
               "TRUMP, XI AND PUTIN HOLD FIRST TRILATERAL TALKS",
               "The three leaders met in Shenzhen and signed a joint "
               "\u201cpeace declaration\u201d on UN reform, nuclear arms "
               "and oil output. Trump flew home straight after the "
               "hour-long talks.",
               hl_size=34, body_size=20, illo=illo_summit)
    draw_panel(d, 640, 134, 360, 316, "THE HAGUE", NAVY,
               "MYANMAR GUILTY OF GENOCIDE",
               "The UN\u2019s top court ruled Myanmar committed genocide "
               "against the Rohingya in 2017 \u2014 a first against a "
               "state.",
               hl_size=30, body_size=19, illo=illo_scales)

    # ---- row B: GTA VI + Anthropic IPO ----
    draw_panel(d, 24, 466, 488, 272, "ENTERTAINMENT", PURPLE,
               "GTA VI IS OUT \u2014 AND ALREADY A RECORD",
               "Rockstar\u2019s Vice City epic launched at midnight "
               "worldwide after $1bn in pre-orders: 10.3m copies "
               "sold before release day.",
               hl_size=28, body_size=19, illo=illo_gta)
    draw_panel(d, 528, 466, 472, 272, "WALL STREET", GREEN,
               "ANTHROPIC\u2019S $81BN IPO IS THE BIGGEST EVER",
               "The Claude maker\u2019s shares debuted on Nasdaq as "
               "\u201cANT\u201d at $83, valuing the AI lab at about "
               "$1.5 trillion.",
               hl_size=28, body_size=19, illo=illo_ipo)

    # ---- row C: Iran war + Gaza/Ukraine ----
    draw_panel(d, 24, 754, 488, 238, "MIDDLE EAST", RED,
               "MISSILE HITS RIYADH AS IRAN WAR GRINDS ON",
               "A Houthi missile damaged the PIF Tower in Riyadh. "
               "Trump: the US will \u201csee what happens\u201d after "
               "Jan. 1.",
               hl_size=26, body_size=18, illo=illo_riyadh)
    draw_panel(d, 528, 754, 472, 238, "WAR UPDATES", NAVY,
               "ISRAEL PUSHES INTO CENTRAL GAZA",
               "Israeli tanks crossed the \u201cyellow line\u201d in "
               "central Gaza. Ukraine struck the Crimean Bridge for "
               "a third time this week.",
               hl_size=26, body_size=18, illo=illo_wars)

    # ---- footer: sources ----
    d.text((W // 2, 1000),
           "Sources: The Times  •  UN News  •  Reuters  •  WSJ  •  "
           "Rockstar Games  •  Just Security  —  19 November 2026",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
