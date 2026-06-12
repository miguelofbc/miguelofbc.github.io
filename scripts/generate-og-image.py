#!/usr/bin/env python3
"""Generate assets/og.png — the 1200x630 Open Graph card for the site.

Only scrapers (LinkedIn, Slack, X, ...) fetch this image; it never loads on a
normal page view, so the page itself stays free of extra requests.

Requires Pillow (`pip install pillow`) and the Liberation fonts, which match
the site's Helvetica-style system font stack:

    python3 scripts/generate-og-image.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MARGIN = 96

# Same palette as the :root tokens in index.html (light theme)
BG = "#fafafa"
FG = "#1a1a1a"
FG_MUTED = "#4a4a4a"
FG_FAINT = "#6b6b6b"
ACCENT = "#0a66c2"
BORDER = "#e3e3e1"

FONTS = Path("/usr/share/fonts/truetype/liberation")
SANS_BOLD = FONTS / "LiberationSans-Bold.ttf"
SANS = FONTS / "LiberationSans-Regular.ttf"
MONO = FONTS / "LiberationMono-Regular.ttf"


def fit_font(path: Path, text: str, max_width: int, start_size: int) -> ImageFont.FreeTypeFont:
    size = start_size
    while size > 12:
        font = ImageFont.truetype(str(path), size)
        if font.getlength(text) <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(str(path), size)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    max_width = W - 2 * MARGIN

    # "MO" badge, mirroring the favicon
    badge = 88
    d.rounded_rectangle((MARGIN, 92, MARGIN + badge, 92 + badge), radius=18, fill=ACCENT)
    badge_font = ImageFont.truetype(str(SANS_BOLD), 40)
    d.text((MARGIN + badge / 2, 92 + badge / 2 - 2), "MO", font=badge_font,
           fill="#ffffff", anchor="mm")

    # Name + role
    name_font = fit_font(SANS_BOLD, "Miguel Oliveira", max_width, 92)
    d.text((MARGIN, 268), "Miguel Oliveira", font=name_font, fill=FG, anchor="lm")

    role = "Engineering Manager · AI-SDLC & agentic test automation"
    role_font = fit_font(SANS, role, max_width, 40)
    d.text((MARGIN, 352), role, font=role_font, fill=FG_MUTED, anchor="lm")

    # Footer rule + url/location line, echoing the h2 treatment on the page
    d.line((MARGIN, 506, W - MARGIN, 506), fill=BORDER, width=2)
    mono_font = ImageFont.truetype(str(MONO), 26)
    d.text((MARGIN, 546), "miguelofbc.github.io", font=mono_font, fill=ACCENT, anchor="lm")
    loc = "Aveiro · Portugal"
    d.text((W - MARGIN, 546), loc, font=mono_font, fill=FG_FAINT, anchor="rm")

    out = Path(__file__).resolve().parent.parent / "assets" / "og.png"
    out.parent.mkdir(exist_ok=True)
    img.save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
