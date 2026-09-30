#!/usr/bin/env python3
"""Build printable PDFs of the guide (EN + ZH) and the one-page quick cards.

Requires: pandoc, and Google Chrome / Chromium (headless printing).
Usage:    python3 scripts/build_pdf.py
Output:   print/*.pdf
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "print"
CSS = ROOT / "scripts" / "print.css"

CHAPTERS = [
    "00-threat-model.md", "01-billionaire-bunkers.md", "02-low-cost-shelter.md",
    "03-water-food.md", "04-power.md", "05-comms.md", "06-information.md",
    "07-privacy.md", "08-medical.md", "09-community.md", "10-human-zoo.md",
    "11-real-world-rehearsals.md", "checklists.md", "regions/china.md", "regions/typhoon.md", "regions/earthquake.md",
    "resources.md", "quick-card.md",
]

COVER = {
    "en": ("AI Doomsday Survival Guide",
           "A field manual for ordinary people, for the day a superintelligent AI runs "
           "the power grid, the internet, the phone network and the news."),
    "zh": ("AI 末日求生指南",
           "一本写给普通人的野外手册：假如有一天，超级 AI 接管了电网、互联网、通信网络和新闻舆论。"),
}
FOOTER = "github.com/brycewang-stanford/AI-Doomsday-Survival-Guide · CC BY-SA 4.0"

# Navigation lines only make sense on GitHub; drop them from print.
NAV = re.compile(r"^(\[← .*|Next: .*|下一章：.*|See also: .*|另见：.*)$")
# Turn internal .md links into plain text; keep external links.
MDLINK = re.compile(r"\[([^\]]+)\]\((?!https?://)[^)]*\)")


def chrome() -> str:
    for c in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome") or "", shutil.which("chromium") or "",
        shutil.which("chromium-browser") or "",
    ]:
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome/Chromium not found")


def clean(md: str) -> str:
    lines = [l for l in md.splitlines() if not NAV.match(l.strip())]
    return MDLINK.sub(r"\1", "\n".join(lines))


def to_pdf(md_text: str, pdf: Path, lang: str, title: str, body_class: str = "", cover: str = ""):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "in.md"
        src.write_text(md_text, encoding="utf-8")
        frag = subprocess.run(
            ["pandoc", str(src), "-f", "gfm", "-t", "html5"],
            check=True, capture_output=True, text=True,
        ).stdout
        html = Path(tmp) / "out.html"
        html.write_text(
            f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
            f"<title>{title}</title><style>{CSS.read_text()}</style></head>"
            f'<body class="{body_class}">{cover}{frag}</body></html>',
            encoding="utf-8",
        )
        subprocess.run(
            [chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdf}", html.as_uri()],
            check=True, capture_output=True,
        )
    print("built", pdf.relative_to(ROOT))


def main():
    OUT.mkdir(exist_ok=True)
    for lang in ("en", "zh"):
        title, sub = COVER[lang]
        cover = (f'<section class="cover"><h1>{title}</h1><p>{sub}</p>'
                 f'<p class="small">{FOOTER}</p></section>')
        body = "\n\n".join(clean((ROOT / lang / c).read_text(encoding="utf-8")) for c in CHAPTERS)
        to_pdf(body, OUT / f"AI-Doomsday-Survival-Guide-{lang}.pdf", lang, title, cover=cover)
        card = clean((ROOT / lang / "quick-card.md").read_text(encoding="utf-8"))
        to_pdf(card, OUT / f"quick-card-{lang}.pdf", lang, title, body_class="card")


if __name__ == "__main__":
    main()
