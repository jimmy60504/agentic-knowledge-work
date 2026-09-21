#!/usr/bin/env python3
"""第四週投影片建置：把三份逐頁稿（drafts/09、10、11）各產成一份素版 PPTX。

用法：python3 slides/build-week4.py            → slides/week4-1-plain.pptx、week4-2.pptx、week4-3.pptx（week4-1.pptx 由使用者外掛維護，不覆寫）
      python3 slides/build-week4.py 09         → 只建其中一份

逐頁稿格式（drafts/09-week4-1-slides.md 等）：
- 「## 逐頁」之後，每頁以「### N｜標題」開頭；頁內可用「**畫面**」「**筆記**」「**原話與來源**」「**圖規格**」分區，畫面區上投影片，其餘進備註。舊格式（無分區，以「- 原話：」等前綴區分）仍支援。
- 內文：一般條列「- 」、編號「1. 」、Markdown 表格、```text 程式區塊，依序放到畫面。
- 「- 原話：」「- 口述：」「- 【無原話】」「- 案例：」「- 圖：」「- 來源：」不上畫面，進備註。
- 「- 引文頁內文：『…』」以引文方塊放到畫面。
- 「- 主訊息：…」以粗體大字放在條列之前，一頁一句。
- 圖：加 `--figures` 才套用 week4_figures.py 的原生圖形（依頁標題），預設不畫。
- 圖片：筆記裡以反引號寫出的 `slides/story/*.svg` 會置入畫面（先以 rsvg-convert 轉成 slides/story/png/*.png）；一張放文字下方，文字太長時改為左文右圖；多張並排。原圖寬度超過 1400 px 的大圖（整張研究流程圖）另立一頁全幅放，頁碼與文字頁相同。畫面裡「- 圖下：」之後的編號清單是圖下句子，放在圖頁的圖下方（編號寫活動編號），不放在文字頁。
- 第 1 頁視為封面。
- 「### 段｜標題」為段落標題頁，不佔頁碼；畫面只有標題，不放副標，筆記照常進備註。

素版原則：白底、標題一句、內文條列或表格、備註放原話與口述；不做視覺設計，供使用者先有東西改。
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from week4_figures import FIGURES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DECKS = {
    "09": ("drafts/09-week4-1-slides.md", "week4-1-plain.pptx"),  # week4-1.pptx 已由使用者外掛接手，不覆寫
    "10": ("drafts/10-week4-2-slides.md", "week4-2.pptx"),
    "11": ("drafts/11-week4-3-slides.md", "week4-3.pptx"),
}

DARK = RGBColor(0x2A, 0x26, 0x23)
MUTED = RGBColor(0x6B, 0x65, 0x60)
ACCENT = RGBColor(0xB8, 0x50, 0x42)
TINT = RGBColor(0xEE, 0xF2, 0xEF)
LINE = RGBColor(0xD9, 0xD4, 0xCE)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "PingFang TC"
W, H, M = 13.333, 7.5, 0.7

NOTE_PREFIXES = ("原話：", "口述：", "【無原話】", "案例：", "備註用：", "圖：", "來源：", "圖格：")


# ---------- 解析 ----------
def parse(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    text = text[text.index("## 逐頁"):]
    pages = []
    cur = None
    in_code = False
    section = "畫面"
    for line in text.split("\n"):
        m = re.match(r"^### (\d+|段)｜(.+)$", line)
        if m:
            n = m.group(1)
            cur = {"n": None if n == "段" else int(n), "title": m.group(2).strip(),
                   "blocks": [], "notes": [], "divider": n == "段"}
            pages.append(cur)
            section = "畫面"
            continue
        if cur is None:
            continue
        m = re.match(r"^\*\*(畫面|筆記|原話與來源|圖規格)\*\*$", line.strip())
        if m:
            section = m.group(1)
            if section != "畫面":
                cur["notes"].append(f"【{section}】")
            continue
        if section != "畫面":
            t = line.strip()
            if t and t != "無。":
                cur["notes"].append(re.sub(r"^- ", "", t))
            continue
        if line.startswith("```"):
            if in_code:
                in_code = False
            else:
                in_code = True
                cur["blocks"].append(("code", []))
            continue
        if in_code:
            cur["blocks"][-1][1].append(line)
            continue
        s = line.strip()
        if not s:
            continue
        if s.startswith("|"):
            if s.startswith("|---") or set(s.replace("|", "").strip()) <= set("-: "):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cur["blocks"] and cur["blocks"][-1][0] == "table":
                cur["blocks"][-1][1].append(cells)
            else:
                cur["blocks"].append(("table", [cells]))
            continue
        m = re.match(r"^- (.*)$", s)
        if m:
            body = m.group(1).strip()
            if body.startswith("引文頁內文："):
                q = body[len("引文頁內文："):].strip()
                q = re.sub(r"（[^）]*）$", "", q).strip().strip("「」")
                cur["blocks"].append(("quote", q))
                continue
            if body.startswith("主訊息："):
                cur["blocks"].append(("lead", body[len("主訊息："):].strip()))
                continue
            if body.startswith(NOTE_PREFIXES):
                cur["notes"].append(body)
                continue
            cur["blocks"].append(("bullet", body))
            continue
        m = re.match(r"^(\d+)\. (.*)$", s)
        if m:
            cur["blocks"].append(("num", f"{m.group(1)}. {m.group(2).strip()}"))
            continue
        cur["blocks"].append(("bullet", s))
    return pages


# ---------- 元件 ----------
def _run(run, size, bold=False, color=DARK):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def textbox(slide, x, y, w, h, lines, size=18, bold=False, color=DARK,
            align="l", anchor="t", spacing=6, bullet=False):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE}[anchor]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER}[align]
        p.space_after = Pt(spacing)
        txt = ("•  " + ln) if bullet and not re.match(r"^\d+\. ", ln) else ln
        r = p.add_run()
        r.text = txt
        _run(r, size, bold, color)
    return box


def rect(slide, x, y, w, h, fill=TINT, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.75)
    shp.shadow.inherit = False
    return shp


def table_layout(w, rows, size=13, row_h=0.42):
    """欄寬與每列高度的估算，畫表與量高共用。"""
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    lens = [max(len(r[c]) for r in rows) for c in range(ncol)]
    lens = [max(l, 4) for l in lens]
    total = sum(lens)
    col_w = [w * l / total for l in lens]
    heights = []
    for r in rows:
        mx = 1
        for c, cell in enumerate(r):
            per_line = max(int(col_w[c] * 72 / (size * 1.05)), 1)
            mx = max(mx, -(-len(cell) // per_line))
        heights.append(row_h * (0.55 + 0.45 * mx))
    return rows, col_w, heights


def table(slide, x, y, w, rows, size=13, row_h=0.42):
    rows, col_w, heights = table_layout(w, rows, size, row_h)
    ncol = len(col_w)
    shp = slide.shapes.add_table(len(rows), ncol, Inches(x), Inches(y), Inches(w), Inches(sum(heights)))
    tbl = shp.table
    for c in range(ncol):
        tbl.columns[c].width = Inches(col_w[c])
    for i, r in enumerate(rows):
        tbl.rows[i].height = Inches(heights[i])
        for c, cell in enumerate(r):
            tc = tbl.cell(i, c)
            tc.margin_left = tc.margin_right = Inches(0.06)
            tc.margin_top = tc.margin_bottom = Inches(0.03)
            tc.fill.solid()
            tc.fill.fore_color.rgb = TINT if i == 0 else WHITE
            tf = tc.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = cell.replace("**", "")
            _run(run, size, bold=(i == 0 or c == 0), color=DARK)
    return sum(heights)


# ---------- 圖片 ----------
IMG_RE = re.compile(r"`(slides/story/[^`]+\.svg)`")


def page_images(page):
    """筆記裡以反引號標出的 story 圖 SVG，依出現順序、不重複。"""
    seen = []
    for line in page["notes"]:
        for m in IMG_RE.findall(line):
            if m not in seen and (ROOT / m).exists():
                seen.append(m)
    return seen


def svg_png(rel):
    """SVG → PNG（slides/story/png/，git 忽略）。需要 rsvg-convert（brew install librsvg）。"""
    src = ROOT / rel
    out = src.parent / "png" / (src.stem + ".png")
    out.parent.mkdir(exist_ok=True)
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        if not shutil.which("rsvg-convert"):
            sys.exit("找不到 rsvg-convert：brew install librsvg")
        subprocess.run(["rsvg-convert", "-z", "3", str(src), "-o", str(out)], check=True)
    return out


BIG_PX = 1400


def is_big(rel):
    iw, _ = Image.open(svg_png(rel)).size
    return iw / 3 > BIG_PX  # svg_png 以 3 倍縮放


def split_captions(page):
    """把「- 圖下：」之後連續的編號項抽出，回傳 (其餘 blocks, captions)。"""
    blocks, caps, grab = [], [], False
    for kind, val in page["blocks"]:
        if kind == "bullet" and val.strip() == "圖下：":
            grab = True
            continue
        if grab and kind == "num":
            caps.append(val)
            continue
        grab = False
        blocks.append((kind, val))
    return blocks, caps


def figure_slide(prs, page, images, total, captions=()):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    textbox(s, M, 0.45, W - 2 * M, 0.9, [page["title"]], size=28, bold=True)
    ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(M), Inches(1.32), Inches(W - 2 * M), Inches(0.03))
    ln.fill.solid(); ln.fill.fore_color.rgb = ACCENT; ln.line.fill.background()
    avail_w = W - 2 * M
    cap_h = 0.0
    if captions:
        n = len(captions)
        cols = 2 if n > 5 else 1
        per = -(-n // cols)
        cap_h = per * 0.3 + 0.15
        cy = H - 0.65 - cap_h
        cw = (avail_w - 0.3 * (cols - 1)) / cols
        for c in range(cols):
            chunk = captions[c * per:(c + 1) * per]
            if chunk:
                textbox(s, M + c * (cw + 0.3), cy, cw, cap_h, chunk, size=12, spacing=2)
    place_images(s, images, M, 1.5, avail_w, H - 1.5 - 0.65 - cap_h - (0.15 if captions else 0))
    textbox(s, W - M - 1.2, H - 0.55, 1.2, 0.35, [f"{page['n']} / {total}"], size=11, color=MUTED, align="c")
    notes(s, ["圖頁：與前一頁同一頁碼，圖全幅。"] + page["notes"][:2])
    return s


def place_images(slide, paths, x, y, w, h):
    """把幾張圖等寬並排放進 (x, y, w, h)，各自保持比例、置中。"""
    n = len(paths)
    gap = 0.2
    cell_w = (w - gap * (n - 1)) / n
    for i, rel in enumerate(paths):
        png = svg_png(rel)
        iw, ih = Image.open(png).size
        scale = min(cell_w / iw, h / ih)
        pw, ph = iw * scale, ih * scale
        cx = x + i * (cell_w + gap) + (cell_w - pw) / 2
        cy = y + (h - ph) / 2
        slide.shapes.add_picture(str(png), Inches(cx), Inches(cy), Inches(pw), Inches(ph))


def notes(slide, lines):
    if not lines:
        return
    slide.notes_slide.notes_text_frame.text = "\n".join(lines)


# ---------- 版面 ----------
def cover(prs, page, deck_label):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    lines = [b[1] for b in page["blocks"] if b[0] == "bullet"]
    title = lines[0] if lines else page["title"]
    sub = lines[1:] if len(lines) > 1 else [deck_label]
    rect(s, 0, 0, 0.35, H, fill=ACCENT)
    textbox(s, M + 0.4, 2.3, W - 2 * M - 0.4, 1.6, [title], size=36, bold=True)
    textbox(s, M + 0.4, 4.0, W - 2 * M - 0.4, 1.2, sub, size=18, color=MUTED)
    notes(s, page["notes"])
    return s


def divider(prs, page):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=TINT)
    rect(s, 0, 0, 0.35, H, fill=ACCENT)
    textbox(s, M + 0.4, 2.9, W - 2 * M - 0.4, 1.4, [page["title"]], size=34, bold=True)
    notes(s, page["notes"])
    return s


def measure(page, avail_w):
    """不畫，只估文字區排完後的 y，與 content() 的算法一致。"""
    y = 1.6
    bullets = []

    def flush():
        nonlocal y, bullets
        if not bullets:
            return
        n = len(bullets)
        size = 18 if n <= 5 else 16 if n <= 7 else 14
        est = 0.0
        for b in bullets:
            per_line = max(int(avail_w * 72 / (size * 1.05)), 1)
            est += (size / 72) * 1.5 * -(-len(b) // per_line) + 0.08
        y += est + 0.25
        bullets = []

    for kind, val in page["blocks"]:
        if kind in ("bullet", "num"):
            bullets.append(val)
            continue
        flush()
        if kind == "lead":
            per_line = max(int(avail_w * 72 / (22 * 1.05)), 1)
            y += (22 / 72) * 1.5 * -(-len(val) // per_line) + 0.1 + 0.2
        elif kind == "table":
            nrow = len(val)
            size = 13 if nrow <= 7 else 12 if nrow <= 9 else 11
            row_h = 0.42 if nrow <= 7 else 0.36 if nrow <= 9 else 0.31
            y += sum(table_layout(avail_w, val, size, row_h)[2]) + 0.25
        elif kind == "code":
            y += 0.32 * len(val) + 0.3 + 0.25
        elif kind == "quote":
            y += 1.5 + 0.25
    flush()
    return y


def content(prs, page, total):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    textbox(s, M, 0.45, W - 2 * M, 0.9, [page["title"]], size=28, bold=True)
    ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(M), Inches(1.32), Inches(W - 2 * M), Inches(0.03))
    ln.fill.solid(); ln.fill.fore_color.rgb = ACCENT; ln.line.fill.background()
    y = 1.6
    avail_w = W - 2 * M
    images = page_images(page)
    page["figure_slide"] = bool(images) and any(is_big(i) for i in images)
    if page["figure_slide"]:
        images = []  # 大圖另立一頁
        page["blocks"], page["captions"] = split_captions(page)
    img_box = None  # (x, y, w, h)
    compact = False
    if images:
        full_w = avail_w
        rest = H - 0.75 - measure(page, full_w)
        iw, ih = Image.open(svg_png(images[0])).size
        if rest >= 2.2 and iw / ih >= 2.0:  # 扁圖放下方，方圖放右欄
            img_box = ("below", rest)
        else:  # 左文右圖
            col = full_w * 0.5 - 0.15
            avail_w = col
            compact = True
            img_box = ("right", (M + full_w * 0.5 + 0.15, 1.6, col, H - 1.6 - 0.7))
    bullets = []

    def flush_bullets():
        nonlocal y, bullets
        if not bullets:
            return
        n = len(bullets)
        size = 18 if n <= 5 else 16 if n <= 7 else 14
        if compact:
            size = 14
        est = 0.0
        for b in bullets:
            per_line = max(int(avail_w * 72 / (size * 1.05)), 1)
            est += (size / 72) * 1.5 * -(-len(b) // per_line) + 0.08
        textbox(s, M, y, avail_w, est + 0.2, bullets, size=size, bullet=True)
        y += est + 0.25
        bullets = []

    for kind, val in page["blocks"]:
        if kind in ("bullet", "num"):
            bullets.append(val)
            continue
        flush_bullets()
        if kind == "lead":
            ls = 18 if compact else 22
            per_line = max(int(avail_w * 72 / (ls * 1.05)), 1)
            est = (ls / 72) * 1.5 * -(-len(val) // per_line) + 0.1
            textbox(s, M, y, avail_w, est, [val], size=ls, bold=True)
            y += est + 0.2
        elif kind == "table":
            nrow = len(val)
            size = 13 if nrow <= 7 else 12 if nrow <= 9 else 11
            row_h = 0.42 if nrow <= 7 else 0.36 if nrow <= 9 else 0.31
            if compact:
                size, row_h = 11, 0.3
            h = table(s, M, y, avail_w, val, size=size, row_h=row_h)
            y += h + 0.25
        elif kind == "code":
            lines = [l for l in val]
            cs = 11 if compact else 14
            h = (0.26 if compact else 0.32) * len(lines) + 0.3
            rect(s, M, y, avail_w, h, fill=TINT)
            box = textbox(s, M + 0.2, y + 0.15, avail_w - 0.4, h - 0.3, lines, size=cs)
            for p in box.text_frame.paragraphs:
                for r in p.runs:
                    r.font.name = "Menlo"
            y += h + 0.25
        elif kind == "quote":
            h = 1.5
            rect(s, M, y, avail_w, h, fill=TINT)
            rect(s, M, y, 0.12, h, fill=ACCENT)
            textbox(s, M + 0.4, y + 0.2, avail_w - 0.8, h - 0.4, [val], size=18, anchor="m")
            y += h + 0.25
    flush_bullets()
    if img_box:
        if img_box[0] == "below":
            place_images(s, images, M, y + 0.05, avail_w, H - 0.75 - (y + 0.05))
            y = H - 0.6
        else:
            place_images(s, images, *img_box[1])
    fig = FIGURES.get(page["title"]) if USE_FIGURES else None
    if fig:
        fig(s, M, y + 0.1, avail_w, H - 0.7 - (y + 0.1))
        y = H - 0.6
    textbox(s, W - M - 1.2, H - 0.55, 1.2, 0.35, [f"{page['n']} / {total}"], size=11, color=MUTED, align="c")
    if y > H - 0.4:
        print(f"  [溢出警告] 第 {page['n']} 頁「{page['title']}」內容估計高度到 {y:.1f} in")
    notes(s, page["notes"])
    return s


def build(key):
    md, out = DECKS[key]
    pages = parse(ROOT / md)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    label = {"09": "第四週 4-1", "10": "第四週 4-2", "11": "第四週 4-3"}[key]
    total = sum(1 for p in pages if not p.get("divider"))
    for p in pages:
        if p.get("divider"):
            divider(prs, p)
        elif p["n"] == 1:
            cover(prs, p, label)
        else:
            content(prs, p, total)
            if p.get("figure_slide"):
                figure_slide(prs, p, page_images(p), total, p.get("captions", ()))
    out_path = ROOT / "slides" / out
    prs.save(out_path)
    print(f"{out}: {len(pages)} 頁（含 {len(pages) - total} 頁段落標題）← {md}")


USE_FIGURES = False

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--figures"]
    USE_FIGURES = "--figures" in sys.argv[1:]
    keys = args or list(DECKS)
    for k in keys:
        build(k)
