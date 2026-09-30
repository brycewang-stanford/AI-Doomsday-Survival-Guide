#!/usr/bin/env python3
"""Render the "news wall" headline collages used in the READMEs.

Headlines are quoted verbatim from the linked articles and set in our own
layout (no screenshots, logos or photos from the publishers).

Requires: Google Chrome / Chromium, Pillow.
Usage:    python3 scripts/build_news_wall.py
Output:   assets/news/*.png
"""
import html
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

from build_pdf import chrome

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "news"

# (outlet, date, headline, gist_en, gist_zh, headline_zh)
BUNKERS = [
    ("WIRED", "Dec 14, 2023", "Inside Mark Zuckerberg's Top-Secret Hawaii Compound",
     "1,400 acres on Kauai, ~$270M, and a 5,000 sq ft underground shelter with an escape hatch.",
     "考艾岛 1,400 英亩、约 2.7 亿美元，另有一个带逃生舱口的 5,000 平方英尺地下掩体。",
     "揭秘扎克伯格的夏威夷绝密庄园"),
    ("The Hollywood Reporter", "Dec 2024", "Mark Zuckerberg Calls Massive Bunker in Hawaii 'a Little Shelter'",
     "\"Whatever you want to call it, hurricane shelter whatever.\"",
     "\"随便你怎么叫，防飓风避难所什么的。\"",
     "扎克伯格称夏威夷巨型地堡只是\"一个小避难所\""),
    ("The New Yorker", "Jan 2017", "Doomsday Prep for the Super-Rich",
     "Reid Hoffman guesses more than half of Silicon Valley billionaires have \"apocalypse insurance.\"",
     "里德·霍夫曼估计，超过一半的硅谷亿万富翁都买了\"末日保险\"。",
     "超级富豪的末日准备"),
    ("Futurism", "May 2025", "OpenAI's Top Scientist Wanted to \"Build a Bunker Before We Release AGI\"",
     "From Karen Hao's book Empire of AI: entry to the bunker would be \"optional.\"",
     "出自 Karen Hao 的《Empire of AI》：进不进地堡\"是自愿的\"。",
     "OpenAI 首席科学家曾想\"在发布 AGI 之前先建一个地堡\""),
    ("Forbes", "Jan 13, 2025", "Inside The $300 Million Doomsday Bunker With Opulent Medical Suites And Robotic Staff",
     "SAFE's \"Aerie\": a members-only underground club for 625 people in Virginia.",
     "SAFE 公司的 \"Aerie\"：弗吉尼亚州一个可容纳 625 人的会员制地下俱乐部。",
     "探访 3 亿美元末日地堡：奢华医疗套房与机器人员工"),
    ("The Washington Post", "May 31, 1992", "The Ultimate Congressional Hideaway",
     "Exposed: a secret bunker for the US Congress, hidden for 30 years under the Greenbrier resort.",
     "曝光：美国国会的秘密地堡，藏在 Greenbrier 度假酒店地下长达 30 年。",
     "终极国会藏身所"),
    ("U.S. News / AP", "Oct 23, 2025", "Survival Bunker Renters Sue Owner of Former South Dakota Munitions Bunkers Over Lease, Amenities",
     "Vivos xPoint residents file a class action over their 99-year leases.",
     "Vivos xPoint 住户就 99 年期租约提起集体诉讼。",
     "生存地堡租户起诉南达科他州前弹药掩体业主"),
    ("RNZ", "2024", "US billionaire Peter Thiel 'abandons' Lake Wānaka lodge build",
     "After a council refusal and a failed appeal, the New Zealand refuge is off.",
     "在被议会否决、上诉失败后，这个新西兰避难所计划告吹。",
     "美国亿万富翁彼得·蒂尔\"放弃\"瓦纳卡湖度假屋"),
]

WORLD = [
    ("CNN", "Mar 26, 2025", "EU urges citizens to stockpile 72 hours' worth of supplies amid war risk",
     "The Preparedness Union Strategy asks every household to be ready for 72 hours.",
     "《备灾联盟战略》要求每个家庭做好独立支撑 72 小时的准备。",
     "欧盟敦促公民储备 72 小时物资以应对战争风险"),
    ("The Register", "Nov 18, 2024", "Sweden dishes out updated crisis and war-survival guide",
     "Mailed to ~5 million homes; first edition to cover disinformation and digital attacks.",
     "寄送约 500 万户；首次涵盖虚假信息和数字攻击。",
     "瑞典发放新版危机与战争生存指南"),
    ("Taiwan News", "Sep 17, 2025", "Taiwan unveils new civil defense handbook",
     "Warns about deepfake videos; self-sufficiency raised from 3 days to 1 week.",
     "警示深度伪造视频；自给时间从 3 天提高到 1 周。",
     "台湾发布新版民防手册"),
    ("CNN", "May 16, 2024", "Arup revealed as victim of $25 million deepfake scam involving Hong Kong employee",
     "Every other face on the video call was AI-generated.",
     "视频会议上除他之外的每一张脸都是 AI 生成的。",
     "奥雅纳被曝遭 2,500 万美元深度伪造诈骗，涉及香港员工"),
]

TITLES = {
    ("bunkers", "en"): ("THE BUNKER FILES", "What the press has reported about elite doomsday shelters"),
    ("bunkers", "zh"): ("地堡档案", "媒体报道中的精英末日避难所"),
    ("world", "en"): ("MEANWHILE, FOR EVERYONE ELSE", "Governments tell households to prepare, and AI fakes a CFO"),
    ("world", "zh"): ("与此同时，普通人这边", "各国政府提醒家庭做准备，AI 伪造了一位首席财务官"),
}
FOOTER = {
    "en": "Headlines quoted verbatim from the original articles and set in our own layout. These are not screenshots. Links in the README.",
    "zh": "标题逐字引自原文，由本项目重新排版，并非网页截图。原文链接见 README。",
}

CSS = """
* { box-sizing: border-box; margin: 0; }
body { width: 1200px; background: #efe8da; font-family: "Helvetica Neue", Arial, "PingFang SC", "Noto Sans SC", sans-serif;
       padding: 40px 44px 30px; color: #1b1b1b; }
header { text-align: center; border-top: 4px double #1b1b1b; border-bottom: 4px double #1b1b1b; padding: 14px 0 12px; margin-bottom: 30px; }
header h1 { font-family: Georgia, "Times New Roman", "Songti SC", serif; font-size: 46px; letter-spacing: 3px; }
header p { font-family: Georgia, "Songti SC", serif; font-style: italic; font-size: 19px; color: #444; margin-top: 4px; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px 30px; }
.card { background: #fffdf8; padding: 20px 22px 18px; box-shadow: 0 3px 10px rgba(0,0,0,.18); position: relative; }
.card:nth-child(4n+1) { transform: rotate(-.7deg); } .card:nth-child(4n+2) { transform: rotate(.6deg); }
.card:nth-child(4n+3) { transform: rotate(.4deg); } .card:nth-child(4n) { transform: rotate(-.5deg); }
.card::before { content: ""; position: absolute; top: -9px; left: 50%; width: 90px; height: 20px; margin-left: -45px;
                background: rgba(214,196,150,.75); transform: rotate(-2deg); }
.meta { display: flex; justify-content: space-between; font-size: 13px; text-transform: uppercase; letter-spacing: 1.4px;
        color: #8a1c14; font-weight: 700; border-bottom: 1px solid #d8d0c0; padding-bottom: 7px; margin-bottom: 10px; }
.meta span:last-child { color: #666; }
h2 { font-family: Georgia, "Times New Roman", serif; font-size: 25px; line-height: 1.18; font-weight: 700; }
.zh-head { font-family: "Songti SC", "Noto Serif SC", serif; font-size: 20px; font-weight: 700; margin-top: 7px; color: #333; }
.gist { font-size: 15.5px; line-height: 1.45; color: #444; margin-top: 10px; }
footer { text-align: center; font-size: 13px; color: #6b6355; margin-top: 30px; }
"""


def render(kind, items, lang):
    title, sub = TITLES[(kind, lang)]
    cards = []
    for outlet, date, head, gist_en, gist_zh, head_zh in items:
        zh = f'<div class="zh-head">{html.escape(head_zh)}</div>' if lang == "zh" else ""
        gist = gist_zh if lang == "zh" else gist_en
        cards.append(
            f'<div class="card"><div class="meta"><span>{html.escape(outlet)}</span><span>{html.escape(date)}</span></div>'
            f"<h2>“{html.escape(head)}”</h2>{zh}<p class=\"gist\">{html.escape(gist)}</p></div>"
        )
    page = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f"<header><h1>{html.escape(title)}</h1><p>{html.escape(sub)}</p></header>"
            f'<div class="grid">{"".join(cards)}</div><footer>{html.escape(FOOTER[lang])}</footer></body></html>')
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "wall.html"
        src.write_text(page, encoding="utf-8")
        shot = Path(tmp) / "shot.png"
        subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1200,3200",
                        f"--screenshot={shot}", src.as_uri()], check=True, capture_output=True)
        im = Image.open(shot).convert("RGB")
        bg = Image.new("RGB", im.size, im.getpixel((5, im.height - 5)))
        bbox = ImageChops.difference(im, bg).getbbox()
        im = im.crop((0, 0, im.width, min(im.height, bbox[3] + 60)))
        out = OUT / f"{kind}-{lang}.png"
        im.save(out, optimize=True)
    print("built", out.relative_to(ROOT), im.size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lang in ("en", "zh"):
        render("bunkers", BUNKERS, lang)
        render("world", WORLD, lang)


if __name__ == "__main__":
    main()
