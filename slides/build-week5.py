#!/usr/bin/env python3
"""第五週投影片建置：把 drafts/15-week5-slides.md 產成素版 PPTX（slides/week5.pptx）。

用法：python3 slides/build-week5.py

沿用 build-week4.py 的逐頁稿解析與文字元件，另加：
- 圖片：畫面中「- 圖：`路徑`」（PNG、JPG）依序置入；路徑不存在時以灰框標示預留位置與檔名，供使用者之後替換。
- 版面：標題、主訊息、條列在上，圖片並排在下；文字較多時改為左文右圖。
- 封面：若有圖，滿版鋪底，標題疊在左側留白處。
- 配色：沿用 assets/week5-visuals/README.md 的封面規格（象牙米白、暖灰、陶土紅、灰藍）。

素版原則：只做文字階層與圖片位置，不做視覺設計，供使用者套用素材。
"""
import importlib.util
import re
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("bw4", HERE / "build-week4.py")
bw4 = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(HERE))
spec.loader.exec_module(bw4)

SRC = ROOT / "drafts/15-week5-slides.md"
OUT = HERE / "week5.pptx"

DARK = RGBColor(0x2A, 0x26, 0x23)
MUTED = RGBColor(0x6B, 0x65, 0x60)
ACCENT = RGBColor(0xBE, 0x89, 0x79)   # 陶土紅
BLUE = RGBColor(0xA6, 0xB7, 0xBA)     # 灰藍
IVORY = RGBColor(0xF5, 0xF2, 0xEC)    # 象牙米白
GREY = RGBColor(0xD8, 0xD2, 0xC9)     # 暖灰
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
W, H, M = bw4.W, bw4.H, bw4.M

textbox = bw4.textbox
notes = bw4.notes


def rect(slide, x, y, w, h, fill, line=None):
    return bw4.rect(slide, x, y, w, h, fill=fill, line=line)


def images_of(page):
    """畫面中「圖：`路徑`｜圖說」進了備註；依序取出 (路徑, 圖說)，保留不存在者作為預留位置。"""
    out = []
    for line in page["notes"]:
        if line.startswith("圖："):
            body = line[len("圖："):].strip()
            rel, _, cap = body.partition("｜")
            rel = rel.strip().strip("`")
            if rel and rel not in [r for r, _ in out]:
                out.append((rel, cap.strip()))
    page["notes"] = [l for l in page["notes"] if not l.startswith("圖：")]
    return out


def placeholder(slide, x, y, w, h, rel):
    rect(slide, x, y, w, h, fill=IVORY, line=GREY)
    textbox(slide, x + 0.1, y + h / 2 - 0.3, w - 0.2, 0.6, ["圖片預留", Path(rel).name],
            size=11, color=MUTED, align="c", anchor="m", spacing=2)


def place(slide, rels, x, y, w, h):
    n = len(rels)
    gap = 0.2
    cell_w = (w - gap * (n - 1)) / n
    for i, rel in enumerate(rels):
        cx0 = x + i * (cell_w + gap)
        path = ROOT / rel
        if not path.exists():
            placeholder(slide, cx0, y, cell_w, h, rel)
            continue
        iw, ih = Image.open(path).size
        scale = min(cell_w / iw, h / ih)
        pw, ph = iw * scale, ih * scale
        pic = slide.shapes.add_picture(str(path), Inches(cx0 + (cell_w - pw) / 2),
                                       Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))
        if "week5-diagrams" not in rel:  # 截圖加細框，自繪圖不加
            pic.line.color.rgb = GREY
            pic.line.width = Pt(0.75)


def text_height(lines, size, w):
    est = 0.0
    for b in lines:
        per_line = max(int(w * 72 / (size * 1.05)), 1)
        est += (size / 72) * 1.5 * -(-len(b) // per_line) + 0.08
    return est


def header(slide, title):
    textbox(slide, M, 0.4, W - 2 * M, 0.8, [title], size=26, bold=True, color=DARK)
    rect(slide, M, 1.18, 1.2, 0.05, fill=ACCENT)


def fit_box(rel, x, y, w, h):
    """回傳圖片等比縮放後的實際位置 (x, y, w, h)，靠右、垂直置中；檔案不存在時回傳整個框。"""
    path = ROOT / rel
    if not path.exists():
        return x, y, w, h
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    return x + (w - pw), y + (h - ph) / 2, pw, ph


def pic_at(slide, rel, box):
    x, y, w, h = box
    path = ROOT / rel
    if not path.exists():
        placeholder(slide, x, y, w, h, rel)
        return
    pic = slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(w), Inches(h))
    if "week5-diagrams" not in rel:
        pic.line.color.rgb = GREY
        pic.line.width = Pt(0.75)


CAP_H = 0.42  # 圖說保留高度


def visual_boxes(imgs, x, y, w, h):
    """右側視覺區：一張靠右；兩張並排；三張以上為上方一張大圖、其餘排成下方一列。回傳 [(rel, cap, box)] 與最左緣。"""
    gap = 0.25
    has_cap = any(c for _, c in imgs)
    ch = CAP_H if has_cap else 0
    out = []

    def cell(r, c, cx, cy, cw, chh, center):
        bx, by, bw, bh = fit_box(r, cx, cy, cw, chh - ch)
        if center:
            bx = cx + (cw - bw) / 2
        out.append((r, c, (bx, by, bw, bh)))

    if len(imgs) == 1:
        cell(*imgs[0], x, y, w, h, False)
    elif len(imgs) == 2:
        cw = (w - gap) / 2
        for i, (r, c) in enumerate(imgs):
            cell(r, c, x + i * (cw + gap), y, cw, h, True)
    else:
        # 三張以上：上方一張大圖，其餘排成下方一列（素材先全部放上，版面之後再調）
        rest = imgs[1:]
        top_h = h * (0.56 if len(rest) <= 2 else 0.5)
        cell(*imgs[0], x, y, w, top_h, False)
        cw = (w - gap * (len(rest) - 1)) / len(rest)
        for i, (r, c) in enumerate(rest):
            cell(r, c, x + i * (cw + gap), y + top_h + gap, cw, h - top_h - gap, True)
    left = min(b[0] for _, _, b in out)
    return out, left


def rich_bullets(slide, x, y, w, items, key_size, body_size, plain_size):
    """條列：「**關鍵詞**：說明」排成粗體關鍵詞加灰色說明兩層；其餘為一般條列。回傳高度。"""
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(1))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    total = 0.0
    first = True
    for it in items:
        m = re.match(r"^\*\*(.+?)\*\*[：:]\s*(.*)$", it)
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        if m:
            key, body = m.group(1), m.group(2)
            p.space_before = Pt(10)
            r = p.add_run(); r.text = key
            bw4._run(r, key_size, True, DARK)
            total += text_height([key], key_size, w) + 0.14
            if body:
                q = tf.add_paragraph()
                q.space_after = Pt(4)
                r2 = q.add_run(); r2.text = body
                bw4._run(r2, body_size, False, MUTED)
                total += text_height([body], body_size, w)
        else:
            p.space_after = Pt(8)
            r = p.add_run(); r.text = "•  " + it
            bw4._run(r, plain_size, False, DARK)
            total += text_height([it], plain_size, w) + 0.1
    box.height = Inches(total + 0.2)
    return total


def content(prs, page, total, section=""):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=WHITE)
    imgs = images_of(page)
    lead = [v for k, v in page["blocks"] if k == "lead"]
    bullets = [v for k, v in page["blocks"] if k in ("bullet", "num")]
    sources = [l[len("來源："):].strip() for l in page["notes"] if l.startswith("來源：")]
    full = W - 2 * M
    # 第一層：小標（段落｜頁名）
    kicker = section
    if kicker:
        textbox(s, M, 0.38, full, 0.35, [kicker], size=12, color=MUTED)
    # 第二層：主張
    y = 0.78
    claim = page["title"]  # 大標題用書面的名詞短語；主訊息移到內文第一行
    ch = text_height([claim], 30, full)
    textbox(s, M, y, full, ch, [claim], size=30, bold=True, color=DARK)
    y += ch + 0.12
    rect(s, M, y, 0.9, 0.05, fill=ACCENT)
    y += 0.4
    foot_h = 0.45 if sources else 0.0
    bottom = H - 0.45 - foot_h
    col = full
    if imgs:
        vx = W * 0.46
        boxes, left = visual_boxes(imgs, vx, y, W - M - vx, bottom - y)
        for rel, cap, box in boxes:
            pic_at(s, rel, box)
            if cap:
                bx, by, bw, bh = box
                textbox(s, bx, by + bh + 0.05, max(bw, 2.2), CAP_H - 0.05, [cap], size=10.5, color=MUTED, spacing=0)
        col = left - 0.4 - M
    # 主訊息：內文第一行
    if lead:
        lh = text_height(lead, 19, col)
        textbox(s, M, y, col, lh + 0.1, lead, size=19, bold=True, color=DARK)
        y += lh + 0.25
    # 第三層：要點
    if bullets:
        dense = any(re.match(r"^\*\*.+?\*\*[：:]", b) for b in bullets)
        if dense:
            h = rich_bullets(s, M, y, col, bullets, 18, 14.5, 16)
        else:
            h = rich_bullets(s, M, y, col, bullets, 18, 14.5, 17 if imgs else 19)
        y += h
    if y > bottom + 0.1:
        print(f"  [溢出警告] 第 {page['n']} 頁「{page['title']}」文字估計高度到 {y:.1f} in")
    # 第四層：來源
    if sources:
        textbox(s, M, H - 0.45 - foot_h + 0.05, full - 1.0, foot_h, ["來源：" + "；".join(sources)],
                size=9.5, color=MUTED, spacing=0)
    textbox(s, W - M - 0.8, H - 0.45, 0.8, 0.3, [f"{page['n']} / {total}"], size=10, color=MUTED, align="c")
    notes(s, page["notes"])


def cover(prs, page):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    imgs = images_of(page)
    rect(s, 0, 0, W, H, fill=IVORY)
    if imgs and (ROOT / imgs[0][0]).exists():
        s.shapes.add_picture(str(ROOT / imgs[0][0]), 0, 0, Inches(W), Inches(H))
    lines = [v for k, v in page["blocks"] if k == "bullet"]
    title = lines[0] if lines else page["title"]
    sub = lines[1:]
    textbox(s, M + 0.2, 2.5, 6.4, 1.8, [title], size=38, bold=True, color=DARK)
    if sub:
        textbox(s, M + 0.2, 4.4, 6.4, 1.0, sub, size=18, color=MUTED)
    notes(s, page["notes"])


def divider(prs, page):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=IVORY)
    rect(s, M, 3.0, 1.2, 0.06, fill=ACCENT)
    textbox(s, M, 3.2, W - 2 * M, 1.2, [page["title"]], size=34, bold=True, color=DARK)
    notes(s, page["notes"])


def main():
    pages = bw4.parse(SRC)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    total = sum(1 for p in pages if not p.get("divider"))
    missing = []
    section = ""
    for p in pages:
        if p.get("divider"):
            divider(prs, p)
            section = p["title"]
            continue
        for line in p["notes"]:
            if line.startswith("圖："):
                rel = line[3:].strip().partition("｜")[0].strip().strip("`")
                if not (ROOT / rel).exists():
                    missing.append(rel)
        if p["n"] == 1:
            cover(prs, p)
        else:
            content(prs, p, total, section)
    prs.save(OUT)
    print(f"{OUT.name}: {len(pages)} 頁（含 {len(pages) - total} 頁段落標題）← {SRC.relative_to(ROOT)}")
    for m in missing:
        print(f"  預留圖片（檔案不存在）：{m}")


if __name__ == "__main__":
    main()
