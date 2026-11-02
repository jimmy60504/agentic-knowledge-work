#!/usr/bin/env python3
"""把 build.py 輸出的圖片組成只有圖片的 PPTX（slides/week8.pptx），備註取自逐頁稿的筆記與原話。

用法：python3 assets/week8-diagrams/slides/deck.py（需要 python-pptx）
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu, Inches

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SRC = ROOT / "drafts/25-week8-slides.md"
OUT = ROOT / "slides/week8.pptx"


def parse():
    """依序回傳 (圖片, 備註)；段落頁沒有備註。"""
    text = SRC.read_text(encoding="utf-8")
    pages, sec = [], 0
    for head, body in re.findall(r"^### (.+?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        if head.startswith("段｜"):
            sec += 1
            pages.append((HERE / f"w8-sec{sec}.png", ""))
            continue
        no = int(head.split("｜")[0])
        img = next(HERE.glob(f"w8-{no:02d}-*.png"))
        note = body.split("**筆記**", 1)[1] if "**筆記**" in body else ""
        lines = [l[2:].strip() for l in note.splitlines() if l.startswith("- ")]
        pages.append((img, "\n".join(lines)))
    return pages


def main():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank = prs.slide_layouts[6]
    pages = parse()
    for img, note in pages:
        s = prs.slides.add_slide(blank)
        s.shapes.add_picture(str(img), Emu(0), Emu(0), prs.slide_width, prs.slide_height)
        if note:
            s.notes_slide.notes_text_frame.text = note
    prs.save(OUT)
    print(f"{OUT.name}: {len(pages)} 頁")


if __name__ == "__main__":
    main()
