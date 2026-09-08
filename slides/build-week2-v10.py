#!/usr/bin/env python3
"""第二週講師版投影片 v10：有排版的版本，依 drafts/08-week2-slide-copy.md 第十七版（28 頁）建置。

用法：python3 slides/build-week2-v8.py  → slides/week2-agent-knowledge-work-v10.pptx
原則：標題是一句主張、畫面是證據、解釋放備註（kb/slide-design-principles-argument-to-slides.md）。
版面依 drafts/07-visual-design-rules.md；配色暖炭灰、陶土紅、鼠尾草綠；圖示 assets/week2-icons（Tabler，MIT）。
"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from PIL import Image
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "assets"
IC = A / "week2-icons"
OUT = ROOT / "slides" / "week2-agent-knowledge-work-v10.pptx"

DARK = RGBColor(0x2A, 0x26, 0x23)
DARK2 = RGBColor(0x3A, 0x35, 0x31)
ACCENT = RGBColor(0xB8, 0x50, 0x42)
SAGE = RGBColor(0xA7, 0xBE, 0xAE)
TINT = RGBColor(0xEE, 0xF2, 0xEF)
MUTED = RGBColor(0x6B, 0x65, 0x60)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LINE = RGBColor(0xD9, 0xD4, 0xCE)
FONT = "PingFang TC"
W, H, M = 13.333, 7.5, 0.6

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(W), Inches(H)
BLANK = prs.slide_layouts[6]


# ---------- 元件 ----------
def _font(run, size, bold=False, color=DARK):
    f = run.font
    f.name, f.size, f.bold = FONT, Pt(size), bold
    f.color.rgb = color
    rpr = run._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        el = rpr.find(qn(tag))
        if el is None:
            el = etree.SubElement(rpr, qn(tag))
        el.set("typeface", FONT)


def tb(s, x, y, w, h, lines, size=15, bold=False, color=DARK, align="l", anchor="t", spacing=5):
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(lines, str):
        lines = [lines]
    for i, ln in enumerate(lines):
        d = ln if isinstance(ln, dict) else {"text": ln}
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[d.get("align", align)]
        p.space_after = Pt(d.get("after", spacing))
        if d.get("bullet"):
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(Inches(0.2))))
            pPr.set("indent", str(-int(Inches(0.2))))
            etree.SubElement(pPr, qn("a:buChar")).set("char", "•")
        r = p.add_run()
        r.text = d["text"]
        _font(r, d.get("size", size), d.get("bold", bold), d.get("color", color))
    return box


def rect(s, x, y, w, h, fill=TINT, line=None, radius=0.08):
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = radius
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp


def oval(s, x, y, d, fill):
    c = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    c.fill.solid()
    c.fill.fore_color.rgb = fill
    c.line.fill.background()
    c.shadow.inherit = False
    return c


def num(s, x, y, n, d=0.42, fill=ACCENT, color=WHITE, size=14):
    c = oval(s, x, y, d, fill)
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(n)
    _font(r, size, True, color)
    return c


def icon(s, name, x, y, d=0.6, variant="accent", circle=None):
    """單色圖示；circle 給底色時，圖示置於圓內。"""
    if circle is not None:
        oval(s, x, y, d, circle)
        pad = d * 0.22
        s.shapes.add_picture(str(IC / f"{name}-{variant}.png"), Inches(x + pad), Inches(y + pad), Inches(d - 2 * pad), Inches(d - 2 * pad))
    else:
        s.shapes.add_picture(str(IC / f"{name}-{variant}.png"), Inches(x), Inches(y), Inches(d), Inches(d))


def picture(s, path, x, y, w, h, align="l"):
    with Image.open(path) as im:
        iw, ih = im.size
    ar = iw / ih
    pw, ph = (h * ar, h) if w / h > ar else (w, w / ar)
    px = x + (w - pw) / 2 if align == "c" else x
    py = y + (h - ph) / 2 if align == "c" else y
    pic = s.shapes.add_picture(str(path), Inches(px), Inches(py), Inches(pw), Inches(ph))
    pic.line.color.rgb = LINE
    pic.line.width = Pt(0.75)
    return px, py, pw, ph


def arrow(s, x1, y1, x2, y2, color=MUTED, dashed=False, width=1.5, head=True):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    if dashed:
        etree.SubElement(ln, qn("a:prstDash")).set("val", "dash")
    if head:
        t = etree.SubElement(ln, qn("a:tailEnd"))
        t.set("type", "triangle"); t.set("w", "med"); t.set("h", "med")
    return c


def table(s, x, y, w, rows, col_w, size=14, row_h=0.5, first_col_bold=True):
    gt = s.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(row_h * len(rows)))
    t = gt.table
    tblPr = t._tbl.tblPr
    tblPr.set("bandRow", "0"); tblPr.set("firstRow", "0")
    for el in tblPr.findall(qn("a:tableStyleId")):
        tblPr.remove(el)
    for i, cw in enumerate(col_w):
        t.columns[i].width = Inches(cw)
    for ri, row in enumerate(rows):
        t.rows[ri].height = Inches(row_h)
        for ci, val in enumerate(row):
            cell = t.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.1)
            cell.margin_top = cell.margin_bottom = Inches(0.05)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            head = ri == 0
            cell.fill.fore_color.rgb = DARK if head else (WHITE if ri % 2 else TINT)
            p = cell.text_frame.paragraphs[0]
            cell.text_frame.word_wrap = True
            r = p.add_run(); r.text = str(val)
            _font(r, size, head or (first_col_bold and ci == 0), WHITE if head else DARK)
    return gt


def notes(s, text):
    s.notes_slide.notes_text_frame.text = text


def bg(s, color):
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = color


def assert_slide(title, seg, right=None):
    """白底主張頁：左上段落標，標題句 30pt 兩行內，右上可放時間。"""
    s = prs.slides.add_slide(BLANK)
    bg(s, WHITE)
    tb(s, M, 0.45, 6, 0.3, seg, size=11, color=MUTED)
    if right:
        tb(s, W - M - 4, 0.45, 4, 0.3, right, size=11, color=MUTED, align="r")
    tb(s, M, 0.85, W - 2 * M, 1.2, title, size=30, bold=True)
    return s


def card(s, x, y, w, h, head, body, ic=None, head_size=17, body_size=14, n=None):
    rect(s, x, y, w, h)
    hx = x + 0.25
    if ic:
        icon(s, ic, x + 0.25, y + 0.25, 0.6, circle=WHITE)
        hx = x + 1.0
    elif n is not None:
        num(s, x + 0.25, y + 0.3, n)
        hx = x + 0.8
    tb(s, hx, y + 0.3, w - (hx - x) - 0.2, 0.5, head, size=head_size, bold=True, anchor="m")
    tb(s, x + 0.25, y + 1.0, w - 0.5, h - 1.15, body, size=body_size)


BODY_Y = 2.25  # 主張頁內容起始


def section_slide(name, sub=None, note=""):
    s = prs.slides.add_slide(BLANK); bg(s, DARK)
    tb(s, M, 2.9, 11, 1.2, name, size=44, bold=True, color=WHITE)
    if sub:
        tb(s, W - M - 4, 6.6, 4, 0.4, sub, size=14, color=SAGE, align="r")
    notes(s, note)
    return s

def loop_crop(img, frac):
    """把直式全圖裁出某一圈的區域，回傳裁好的檔案路徑。frac 為上下比例。"""
    src = A / "week2-diagrams" / img
    dst = A / "week2-diagrams" / (img.replace(".png", f"-crop.png"))
    with Image.open(src) as im:
        h = im.height
        im.crop((0, int(h * frac[0]), im.width, int(h * frac[1]))).save(dst)
    return dst


CROPS = {"three-loops-mermaid-h1.png": (0.0, 0.29), "three-loops-mermaid-h2.png": (0.30, 0.60), "three-loops-mermaid-h3.png": (0.61, 0.905)}


def loop_slide(title, img, caption, note, seg="三個迴圈"):
    s = assert_slide(title, seg)
    if img in CROPS:
        path = loop_crop(img, CROPS[img])
        px, py, pw, ph = picture(s, path, M, BODY_Y, 7.4, 4.3, align="l")
        tx = px + pw + 0.5
    else:
        px, py, pw, ph = picture(s, A / "week2-diagrams" / img, M, BODY_Y - 0.15, 3.6, 5.5, align="l")
        tx = px + pw + 0.6
    tb(s, tx, BODY_Y + 0.4, W - M - tx, 4.5, caption, size=16, spacing=10)
    notes(s, note)
    return s


def mini_loop(s, img):
    path = loop_crop(img, CROPS[img])
    picture(s, path, W - M - 2.2, 0.4, 2.2, 1.3, align="l")


# ============ 內容 ============
def mini_tag(s, x, y, text, fill=ACCENT, color=WHITE, w=None, size=11):
    w = w or (0.32 * len(text) + 0.3)
    r = rect(s, x, y, w, 0.32, fill=fill, radius=0.5)
    tf = r.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    run = p.add_run(); run.text = text; _font(run, size, True, color)
    return w

def quote_box(s, x, y, w, h, text, size=14):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    rect(s, x, y, 0.08, h, fill=ACCENT, radius=0)
    tb(s, x + 0.3, y + 0.15, w - 0.5, h - 0.3, text, size=size, anchor="m")

# 01 封面
s = prs.slides.add_slide(BLANK); bg(s, DARK)
tb(s, M, 2.0, 11, 1.3, "先玩玩看 agent 吧", size=54, bold=True, color=WHITE)
tb(s, M, 3.4, 11, 0.5, "Agent 時代的知識工作｜第二週", size=20, color=SAGE)
for i, (ic, name) in enumerate([("compass", "確認方向"), ("route", "建立架構"), ("ruler-2", "調整風格")]):
    x = M + i * 2.6
    icon(s, ic, x, 5.2, 0.8, variant="light", circle=DARK2)
    tb(s, x + 1.0, 5.2, 1.6, 0.8, name, size=16, color=WHITE, anchor="m")
notes(s, "上次介紹了 agent 是什麼，這次讓大家有個方向怎麼學。前半段 30 分講怎麼合作，示範 30 分看一遍，練習 120 分自己做一份。")

# 02 放大器
s = assert_slide("AI 是放大器：領域知識 × agent 能力", "怎麼學 agent")
px, py, pw, ph = picture(s, A / "week2-evidence-pilot/magnifying-glass-book.jpg", M, BODY_Y + 0.1, 5.4, 3.6)
tb(s, M, py + ph + 0.1, 5.4, 0.35, "圖片：Julo，Wikimedia Commons，公有領域，未修改。", size=10, color=MUTED)
x = 6.6; w = W - M - x
card(s, x, BODY_Y + 0.1, w, 1.7, "領域知識", "知道方法的因果關係，知道現在缺什麼、該怎麼跟 agent 講才會得到預期的結果。", ic="book", body_size=14)
num(s, x + w / 2 - 0.25, BODY_Y + 1.9, "×", d=0.5, fill=DARK, size=18)
card(s, x, BODY_Y + 2.5, w, 1.7, "駕馭 agent 的能力", "知道不同模型擅長什麼、能做到什麼程度，偏工具的熟悉度。", ic="tool", body_size=14)
tb(s, x, BODY_Y + 4.35, w, 0.4, "兩邊都要有，才發揮得出來。", size=15, bold=True, color=ACCENT)
notes(s, "兩個族群。學得快沒有包袱的，缺的是領域知識；經驗老到的，不用把原本工作流程打掉換新的，分析自己工作流裡重複機械式或目標明確的部分，用 agent 試試看，也可以去補過去一直想補但沒時間補的短板。")

# 03 當同事
s = assert_slide("把 AI 當同事", "怎麼學 agent")
cw = (W - 2 * M - 0.4) / 2
for i, (ic, h1, body, ex) in enumerate([
    ("message-circle", "請教", "像請教不同領域的同事。先以自己的想法為主，不被牽著走。", "「GDMS 的新進同仁最常卡在哪裡？有什麼介紹方式？」"),
    ("list-check", "交辦", "講明確的方向跟重要的限制：格式、範圍、長度。具體怎麼做留給它。", "「只用 GDMS 公開頁面，做 10 到 12 頁，先給我逐頁稿。」")]):
    x = M + i * (cw + 0.4)
    rect(s, x, BODY_Y, cw, 3.6)
    icon(s, ic, x + 0.3, BODY_Y + 0.3, 0.7, circle=WHITE)
    tb(s, x + 1.15, BODY_Y + 0.35, cw - 1.4, 0.6, h1, size=22, bold=True, anchor="m")
    tb(s, x + 0.3, BODY_Y + 1.2, cw - 0.6, 1.0, body, size=15)
    quote_box(s, x + 0.3, BODY_Y + 2.35, cw - 0.6, 0.95, ex, size=14)
rect(s, M, BODY_Y + 3.85, W - 2 * M, 0.7, fill=WHITE, line=LINE)
tb(s, M + 0.3, BODY_Y + 3.85, W - 2 * M - 0.6, 0.7, [{"text": "最省事的交辦：只給一句話、不給材料、不請教。示範開頭會先做一次這種版本。", "size": 14}], anchor="m", color=MUTED)
notes(s, "太籠統會沒跟自己對齊，太細節可能會錯過更好的方法。已有自己累積的工作流程，不用急著全部切換。")

# 04 補足
s = assert_slide("從自己需要補足的地方開始", "怎麼學 agent")
rows = [("search", "缺知識與方向", "請它拓展材料"), ("tool", "有想法但不熟工具", "請它實作"), ("refresh", "簡單重複的雜工", "交給它整理與排版"), ("eye", "需要人抓盲點", "讓它當審查者")]
for i, (ic, need, act) in enumerate(rows):
    y = BODY_Y + i * 1.05
    rect(s, M, y, 5.4, 0.85, fill=TINT)
    icon(s, ic, M + 0.2, y + 0.12, 0.6, circle=WHITE)
    tb(s, M + 1.0, y, 4.2, 0.85, need, size=17, bold=True, anchor="m")
    arrow(s, M + 5.6, y + 0.42, M + 6.6, y + 0.42, color=ACCENT, width=2)
    rect(s, M + 6.8, y, 5.3, 0.85, fill=WHITE, line=LINE)
    tb(s, M + 7.1, y, 5.0, 0.85, act, size=17, anchor="m")
tb(s, M, BODY_Y + 4.3, 12, 0.4, "同一件事可能同時需要幾種。選定之後，下一步是把需要向 agent 說清楚。", size=13, color=MUTED)
notes(s, "同一件事可能同時需要幾種。選定之後，下一步是把需要向 agent 說清楚。")

# 05 交付物代表自己
s = assert_slide("交付物代表自己", "怎麼學 agent")
px, py, pw, ph = picture(s, A / "week2-baseline/baseline-method-card.png", M, BODY_Y, 7.2, 4.4)
mini_tag(s, px, py - 0.05, "一句話生成的對照組", fill=DARK)
x = px + pw + 0.5; w = W - M - x
for i, t in enumerate(["用幾句話完成什麼東西看起來很厲害，但那不是你要的東西。", "與其 AI 一次吐一堆看不完的東西，不如一點一點的把工作流程替換。"]):
    quote_box(s, x, BODY_Y + i * 1.5, w, 1.3, t, size=14)
rect(s, x, BODY_Y + 3.1, w, 1.3, fill=ACCENT)
tb(s, x + 0.3, BODY_Y + 3.1, w - 0.6, 1.3, [{"text": "看的人的反應", "size": 12, "color": WHITE}, {"text": "做得不錯，拿去報就會卡，被問就答不出來。", "size": 15, "bold": True, "color": WHITE}], anchor="m")
notes(s, "對照組的反應：做得不錯，但拿去報就會卡，被問就答不出來。漂亮這點可以吸收，後面第三圈會用到。")

# 06 外部化
s = assert_slide("東西都要外部化存起來", "怎麼學 agent")
tree = [("AGENTS.md", "給 agent 的工作規則", 0), ("工作紀錄.md", "每次的決定與待辦", 0), ("kb/", "材料與筆記，分 arguments 與 tools", 0), ("drafts/", "文稿、逐頁稿與棄案", 0), ("skills/", "用過有效的標準", 0), ("assets/", "圖與素材", 0), ("slides/", "成品", 0), ("lessons/", "公開教材", 0), ("tmp/", "不進 git", 0)]
rect(s, M, BODY_Y, 6.6, 4.6, fill=WHITE, line=LINE)
tb(s, M + 0.3, BODY_Y + 0.2, 6, 0.35, "這門課的專案資料夾", size=12, bold=True, color=ACCENT)
for i, (name, desc, _) in enumerate(tree):
    y = BODY_Y + 0.65 + i * 0.43
    icon(s, "folder" if name.endswith("/") else "file-check", M + 0.3, y + 0.05, 0.3, variant="dark")
    tb(s, M + 0.75, y, 2.2, 0.4, name, size=14, bold=True, anchor="m")
    tb(s, M + 2.9, y, 3.5, 0.4, desc, size=13, color=MUTED, anchor="m")
x = M + 7.0; w = W - M - x
for i, (ic, h1, body) in enumerate([("stack-2", "結構是長出來的", "不用先設計；只有「都要外部化存起來」這個要求要先給 agent。"), ("book", "kb 是常見的處理方式", "材料、討論、筆記都進去；其他資料夾依專案需求跟著長。"), ("file-check", "有自己的方式就照抄", "叫 agent 照你熟悉的整理方式建，之後寫進 AGENTS.md。")]):
    y = BODY_Y + i * 1.55
    card(s, x, y, w, 1.4, h1, body, ic=ic, head_size=15, body_size=13)
notes(s, "有自己熟悉的整理方式，叫 agent 先照抄也可以。這個結構是這幾週跟 agent 互動長出來的，不是一開始設計的；kb 昨天才分成論點類與工具類。")

# 07 段
section_slide("三個迴圈", note="內容不是一次寫成的。先一張全圖，之後每圈兩頁：一頁講那一圈怎麼走，一頁用這份投影片當實例。")

# 08 全圖
s = assert_slide("內容要走三個迴圈", "三個迴圈")
px, py, pw, ph = picture(s, A / "week2-diagrams/three-loops-mermaid.png", M, BODY_Y - 0.2, 4.6, 5.3, align="l")
x = px + pw + 0.6; w = W - M - x
rows = [["圈", "產出物", "通過標準"], ["確認方向", "文稿", "文稿讀過撐得住方向"], ["建立架構", "逐頁稿", "只讀標題連讀能講完故事"], ["調整風格", "成品", "整份看像自己，試講過得去"]]
table(s, x, BODY_Y, w, rows, [1.6, 1.4, w - 3.0], size=14, row_h=0.6)
tb(s, x, BODY_Y + 2.7, w, 2.2, [{"text": "每圈都有人的判斷，圖上紅框那格。", "bullet": True}, {"text": "每圈以自己的產物收尾，產物就是這一圈的檢驗；測不過就沿虛線退回。", "bullet": True}, {"text": "對得上軟體開發：需求探索、建立架構、寫程式。", "bullet": True}], size=14, spacing=8)
notes(s, "跟軟體開發對得上，需求探索、建立架構、寫程式。接下來各看一圈。")

def loop_crop_auto(img, pad=36):
    """依亮圈的淡綠底色找出該圈的框，裁出來（其他圈在 h 圖裡已淡成白色）。"""
    import numpy as np
    src = A / "week2-diagrams" / img
    dst = A / "week2-diagrams" / img.replace(".png", "-crop.png")
    with Image.open(src) as im:
        a = np.asarray(im.convert("RGB")).astype(int)
        m = (abs(a[:, :, 0] - 0xEE) < 6) & (abs(a[:, :, 1] - 0xF2) < 6) & (abs(a[:, :, 2] - 0xEF) < 6)
        def band(idx):  # 取最長的連續區段，避開單像素的反鋸齒線
            best = (idx[0], idx[0]); s0 = prev = idx[0]
            for i in idx[1:]:
                if i != prev + 1:
                    if prev - s0 > best[1] - best[0]: best = (s0, prev)
                    s0 = i
                prev = i
            return best if best[1] - best[0] >= prev - s0 else (s0, prev)
        y0, y1 = band(np.where(m.sum(axis=1) > 80)[0]); x0, x1 = band(np.where(m.sum(axis=0) > 80)[0])
        im.crop((max(0, x0 - pad), max(0, y0 - 12), min(im.width, x1 + pad), min(im.height, y1 + 12))).save(dst)
    return dst


def loop_page(title, img, concept, product, standard, note):
    s = assert_slide(title, "三個迴圈")
    path = loop_crop_auto(img)
    px, py, pw, ph = picture(s, path, M, BODY_Y, 7.0, 4.5, align="l")
    x = px + pw + 0.5; w = W - M - x
    for i, (lab, txt) in enumerate([("概念", concept), ("產出物", product), ("通過標準", standard)]):
        y = BODY_Y + i * 1.5
        rect(s, x, y, w, 1.35)
        tb(s, x + 0.25, y + 0.15, w - 0.5, 0.3, lab, size=11, bold=True, color=ACCENT)
        tb(s, x + 0.25, y + 0.45, w - 0.5, 0.85, txt, size=14, bold=(lab != "概念"))
    notes(s, note)
    return s

# 09 確認方向
loop_page("確認方向", "three-loops-mermaid-h1.png", "帶著問題探索材料，人補入洞見，agent 順著討論長成文稿。", "文稿", "文稿讀過撐得住方向，不必回頭改主軸。",
          "有自己的想法就先以自己的為主，洞見在這一圈進去，成果才代表自己；不必先寫大綱，討論本身就會長成文稿。文稿讀起來撐不住，就回頭補充探索或改方向。")

# 10 方向改了三次
s = assert_slide("確認方向：方向改了三次才定下來", "三個迴圈")
cw = (W - 2 * M - 0.6) / 3
cols = [("compass", "方向", [("9/2", "文件專案化與模型能力"), ("9/4", "公部門用 AI 的阻礙與規範"), ("9/6", "先體驗 agent")]),
        ("bulb", "補入的洞見", [("", "迭代回圈小一點，內容留在 md"), ("", "一直在改就是缺一個原則，先找原則再套用"), ("", "第三個迴圈，讓交付物對齊自己的標準")]),
        ("arrows-left-right", "文稿退回的", [("", "客服例子不好講，拿掉"), ("", "NESA 與三種形式的對照組整段移出"), ("", "兩輪試跑看不懂的句子改寫")])]
for i, (ic, h1, items) in enumerate(cols):
    x = M + i * (cw + 0.3)
    rect(s, x, BODY_Y, cw, 4.5)
    icon(s, ic, x + 0.3, BODY_Y + 0.3, 0.65, circle=WHITE)
    tb(s, x + 1.1, BODY_Y + 0.3, cw - 1.3, 0.65, h1, size=19, bold=True, anchor="m")
    for j, (d, t) in enumerate(items):
        y = BODY_Y + 1.25 + j * 1.0
        if d:
            mini_tag(s, x + 0.3, y + 0.05, d, fill=DARK, w=0.7)
            tb(s, x + 1.15, y, cw - 1.4, 0.8, t, size=14)
        else:
            num(s, x + 0.3, y + 0.02, j + 1, d=0.36, size=12)
            tb(s, x + 0.8, y, cw - 1.1, 0.9, t, size=14)
notes(s, "方向改了不算失敗。文稿是方向的檢驗：兩輪學員試跑都看不懂的句子，退回來改的是方向與說法；總時數定為 60 分之後，文稿才有尺可量。連迴圈圖本身也改了五次才定型。")

# 11 建立架構
loop_page("建立架構", "three-loops-mermaid-h2.png", "agent 把文稿排成逐頁稿，人連讀後調整邏輯順序，agent 提議刪併，人決定取捨。", "逐頁稿", "只讀標題連讀能講完故事。",
          "逐頁稿的前置是只有標題的 ghost deck，一頁一句主張，連讀就看得出跳接。文稿像文章，投影片分口述跟畫面，節奏不一樣。越快進到具體改起來越慢，所以順序在 md 上調好再往下。")

# 12 文稿排成逐頁稿
s = assert_slide("建立架構：文稿排成逐頁稿", "三個迴圈")
pairs = [("還沒有方法時請教", "把 AI 當同事"), ("開空專案，建 kb 與 AGENTS.md", "開空專案"), ("確認表達", "調整風格"), ("寫成判準", "寫成標準"), ("交付出去的東西是要負責的", "交付物代表自己")]
lw = 5.4; rw = 5.4; gap = W - 2 * M - lw - rw
tb(s, M, BODY_Y, lw, 0.4, "agent 生成的標題", size=13, bold=True, color=MUTED)
tb(s, M + lw + gap, BODY_Y, rw, 0.4, "原話當底的標題", size=13, bold=True, color=ACCENT)
for i, (a, b) in enumerate(pairs):
    y = BODY_Y + 0.5 + i * 0.75
    rect(s, M, y, lw, 0.6, fill=WHITE, line=LINE); tb(s, M + 0.25, y, lw - 0.5, 0.6, a, size=15, color=MUTED, anchor="m")
    arrow(s, M + lw + 0.2, y + 0.3, M + lw + gap - 0.2, y + 0.3, color=ACCENT, width=2)
    rect(s, M + lw + gap, y, rw, 0.6, fill=TINT); tb(s, M + lw + gap + 0.25, y, rw - 0.5, 0.6, b, size=15, bold=True, anchor="m")
tb(s, M, BODY_Y + 4.4, 12, 0.4, "每頁標題附原話出處與日期，agent 補的標【無原話】。", size=13, color=MUTED)
notes(s, "生成的標題句通順但認不出自己的思路，改了七版還不是要的感覺；換成原話當底才看得懂、才判斷得了順序。這個做法留在 skills 裡。")

# 13 順序與刪併
s = assert_slide("建立架構：連讀後調整順序與刪併", "三個迴圈")
cw = (W - 2 * M - 0.4) / 2
for i, (ic, h1, items) in enumerate([("route", "調整順序", ["先講迴圈再講實例", "保存接在流程後面", "把 AI 當同事前移，外部化接交付責任", "迴圈與實例穿插，各接在對應的圈後面"]),
                                     ("stack-2", "刪併取捨", ["刪研究專案情境頁", "刪練習時間表頁", "段落頁加了又減", "歷程從五頁併成三頁"])]):
    x = M + i * (cw + 0.4)
    rect(s, x, BODY_Y, cw, 4.5)
    icon(s, ic, x + 0.3, BODY_Y + 0.3, 0.7, circle=WHITE)
    tb(s, x + 1.15, BODY_Y + 0.35, cw - 1.4, 0.6, h1, size=22, bold=True, anchor="m")
    for j, t in enumerate(items):
        y = BODY_Y + 1.3 + j * 0.75
        num(s, x + 0.3, y + 0.05, j + 1, d=0.38, size=12)
        tb(s, x + 0.85, y, cw - 1.1, 0.5, t, size=15, anchor="m")
tb(s, M, BODY_Y + 4.65, 12, 0.4, "agent 提的是刪併建議，留哪頁、什麼順序是人決定的。", size=13, color=MUTED)
notes(s, "連讀能講完故事，架構才算定。原本以為分頁在第三圈，改名建立架構之後才看清楚它是第二圈的起點。")

# 14 調整風格
loop_page("調整風格", "three-loops-mermaid-h3.png", "agent 尋找風格規則寫成標準，依標準產出一版，人依自身品味檢視整份；先語氣，再版面。", "成品", "整份看像自己，試講過得去。",
          "先語氣再版面，兩個面向做法相同。人依品味看哪裡不像自己，改的是標準不是那一頁；自己有判斷力的面向直接拿規則檔，用過有效的補進 AGENTS.md。看成品發現的內容問題退回第二圈。")

# 15 從第一版排到現在
s = assert_slide("調整風格：這份投影片從第一版排到現在", "三個迴圈")
px, py, pw, ph = picture(s, A / "week2-deck-history/v3-page02.png", M, BODY_Y + 0.3, 5.6, 3.6)
mini_tag(s, px, py - 0.35, "第一版的第 2 頁", fill=DARK)
x = px + pw + 0.5; w = W - M - x
for i, (h1, body) in enumerate([("找到的標準", "視覺設計規則一份、文案語氣規則一份、廠商語氣指引筆記。"), ("產出", "每版整份重建，不在 PPTX 上手改。"), ("人檢視後改的標準", "圖示統一用一套單色；文字改書面語與原話；流程圖改 mermaid 直式。")]):
    y = BODY_Y + i * 1.5
    rect(s, x, y, w, 1.35)
    num(s, x + 0.25, y + 0.2, i + 1, d=0.36, size=12)
    tb(s, x + 0.75, y + 0.15, w - 1.0, 0.4, h1, size=14, bold=True, anchor="m")
    tb(s, x + 0.25, y + 0.6, w - 0.5, 0.7, body, size=13)
notes(s, "每次都是整份重建，不在 PPTX 上手改；看畫面發現的內容問題退回前兩圈。")

# 16 段
section_slide("示範：向新進同仁介紹 GDMS", sub="示範 30 分", note="講師走一遍八步，只展開一條論點。學員記兩件事：自己會加哪個條件，最想先試哪一步。")

# 17 資料去哪裡
s = assert_slide("開始前先確認資料去哪裡", "示範 30 分")
items = [("lock", "資料使用設定", "把提供訓練關掉。"), ("shield", "repo 公開與否", "push GitHub 就是上雲，練習不用機密資料。"), ("device-projector", "PPTX 製作路徑", "agent 產出可編輯檔。"), ("eye", "預覽方式", "匯出 PDF 或圖片再看。")]
cw = (W - 2 * M - 0.9) / 4
for i, (ic, h1, body) in enumerate(items):
    x = M + i * (cw + 0.3)
    card(s, x, BODY_Y, cw, 2.6, h1, body, ic=ic, head_size=15, body_size=13)
rect(s, M, BODY_Y + 2.9, W - 2 * M, 1.4, fill=DARK)
tb(s, M + 0.4, BODY_Y + 2.9, W - 2 * M - 0.8, 1.4, [{"text": "先貼給 agent，讓它在背景做第一版", "size": 12, "color": SAGE}, {"text": "「幫我做一份向新進同仁介紹 GDMS 的簡報。」", "size": 20, "bold": True, "color": WHITE}], anchor="m")
notes(s, "示範只展開一條論點。接下來八頁，示範時看，練習時照做。")

# 18–25 八步
def ev14(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "練習專案／", size=14, bold=True)
    tb(s, x + 0.3, y + 0.7, w - 0.6, 2.5, [{"text": "AGENTS.md", "bold": True, "after": 2}, {"text": "保存方式與共用要求", "size": 12, "color": MUTED, "after": 14},
                                          {"text": "kb/第一次討論.md", "bold": True, "after": 2}, {"text": "題目、受眾、用途、想法、未定事項", "size": 12, "color": MUTED}], size=15)
    icon(s, "folder", x + w - 1.3, y + h - 1.3, 1.0)

def ev_gdms(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=ACCENT)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "預設題的材料", size=14, bold=True, color=ACCENT)
    tb(s, x + 0.3, y + 0.7, w - 0.6, h - 0.9, [{"text": "只用講師提供的 GDMS 公開頁面與說明文件。", "bullet": True},
                                              {"text": "需要帳號才看得到的畫面與資料，不提供給工具。", "bullet": True},
                                              {"text": "agent 寫的功能、資料範圍與數字，一律對照說明頁。", "bullet": True}], size=14, spacing=8)

def ev_rules(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "語氣的判準來源", size=14, bold=True, color=ACCENT)
    for i, t in enumerate(["能用自己說過的原話就用原話", "自己的文案語氣規則", "維基百科 AI 寫作特徵清單", "OpenAI 禁用詞、Anthropic 的 mannered prose"]):
        yy = y + 0.8 + i * 0.7
        num(s, x + 0.3, yy + 0.03, i + 1, d=0.38, size=12)
        tb(s, x + 0.85, yy, w - 1.1, 0.45, t, size=14, anchor="m")
    tb(s, x + 0.3, y + h - 0.7, w - 0.6, 0.5, "請 agent 標出沒有原話依據的句子。", size=12, color=MUTED)

def ev19(s, x, y, w, h):
    ph = (h - 0.9) / 2
    tb(s, x, y, w, 0.3, "首次輸出：整頁太空、字小", size=12, color=MUTED)
    picture(s, A / "week2-student-run/first-output-page1.png", x, y + 0.35, w, ph)
    tb(s, x, y + ph + 0.55, w, 0.3, "修改後：標題加大、關鍵字做成並排色塊", size=12, color=ACCENT, bold=True)
    picture(s, A / "week2-student-run/revised-page1.png", x, y + ph + 0.9, w, ph)

def ev20(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "agent 無法代做", size=14, bold=True, color=ACCENT)
    items = [("pointer", "親自點選文字，確認可編輯"), ("microphone", "自己找時間真的講一遍，計時")]
    for i, (ic, t) in enumerate(items):
        yy = y + 0.85 + i * 1.05
        icon(s, ic, x + 0.3, yy, 0.7, circle=TINT)
        tb(s, x + 1.2, yy, w - 1.5, 0.7, t, size=15, anchor="m")


def step_slide(n, seg, title, do, say, check, evidence, note):
    s = assert_slide(f"第{n}步：{title}", "示範與練習", right=seg)
    lx, lw = M, 6.9
    blocks = [("做什麼", do), ("對 agent 說", say), ("確認什麼", check)]
    y = BODY_Y
    hs = [1.45, 1.35, 1.35]
    for (lab, lines), h in zip(blocks, hs):
        rect(s, lx, y, lw, h)
        tb(s, lx + 0.25, y + 0.15, 1.6, 0.35, lab, size=12, bold=True, color=ACCENT)
        if lab == "對 agent 說":
            tb(s, lx + 0.25, y + 0.5, lw - 0.5, h - 0.6, lines, size=14, bold=True, spacing=4)
        else:
            tb(s, lx + 0.25, y + 0.5, lw - 0.5, h - 0.6, [{"text": t, "bullet": True} for t in lines], size=14, spacing=4)
        y += h + 0.15
    rx = lx + lw + 0.4
    evidence(s, rx, BODY_Y, W - M - rx, y - 0.15 - BODY_Y)
    notes(s, note)
    return s

def ev_ghost(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "這份投影片的 ghost deck 前幾行", size=14, bold=True, color=ACCENT)
    lines = ["2 AI 是放大器：領域知識 × agent 能力", "3 把 AI 當同事", "4 從自己需要補足的地方開始", "5 交付物代表自己", "6 東西都要外部化存起來", "8 內容要走三個迴圈"]
    tb(s, x + 0.3, y + 0.75, w - 0.6, h - 1.0, [{"text": t, "after": 6} for t in lines], size=12)

def ev_dir(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "方向收斂的例子", size=14, bold=True, color=ACCENT)
    tb(s, x + 0.3, y + 0.7, w - 0.6, 0.9, "「介紹 GDMS 所有功能」", size=15, color=MUTED)
    tb(s, x + 0.3, y + 1.35, w - 0.6, 0.4, "↓ 自己先說想講的方向", size=12, color=MUTED)
    tb(s, x + 0.3, y + 1.75, w - 0.6, 1.0, "「回答新同仁最先遇到的問題」", size=15, bold=True)
    tb(s, x + 0.3, y + 2.9, w - 0.6, 1.0, "棄案另存一份，記理由。", size=13, color=MUTED)

def ev_check(s, x, y, w, h):
    rect(s, x, y, w, h, fill=WHITE, line=LINE)
    tb(s, x + 0.3, y + 0.25, w - 0.6, 0.35, "挑一句斷言查證", size=14, bold=True, color=ACCENT)
    tb(s, x + 0.3, y + 0.7, w - 0.6, 0.9, "「這個系統功能完整，適合所有使用者。」", size=15, color=MUTED)
    tb(s, x + 0.3, y + 1.55, w - 0.6, 0.4, "缺條件：對誰、在什麼情況、哪些未確認", size=12, color=ACCENT)
    tb(s, x + 0.3, y + 2.0, w - 0.6, 1.6, "回到受眾的需要，說明他們最先需要的是什麼，再用查到的功能與限制支撐；未實測照標未實測。", size=13)

step_slide("一", "準備", "開空專案",
           ["開一個空的資料夾，先講這個專案大致要做什麼。"],
           "「我要向新進同仁介紹 GDMS。先建 kb/ 保存材料與討論，保存方式寫進 AGENTS.md。」",
           ["開啟檔案看寫了什麼，太長就刪短。", "之後明確請它讀取 AGENTS.md。"], ev14,
           "有自己熟悉的整理方式就叫 agent 照抄。開啟確認、刪短、明確請它讀取，這三條來自試跑。")
step_slide("二", "確認方向", "講背景與限制",
           ["用聊天講受眾、用途、時間、簡報長度、材料範圍。", "問它建議，最後落成 md 存起來。"],
           "「受眾是還沒用過 GDMS 的新進同仁。先讀我給的公開頁面，每一份整理進 kb。」",
           ["每份材料實際開啟、附來源。", "30 分停止搜尋。"], ev_gdms,
           "每份實際開啟、附來源、30 分停止搜尋，來自試跑。任何一步卡住都可以再找一輪材料。")
step_slide("三", "確認方向", "先找出想講的方向",
           ["先自己說想講的方向與理由。", "想不到時讓它先試串。"],
           "「我覺得新進同仁最先要知道的是＿＿，因為＿＿。沿這個方向拓展，看有沒有要調整的。」",
           ["逐段說認同或修改的理由。", "棄案另存並記理由。"], ev_dir,
           "想不到時讓它先試串，自己逐段說認同或修改的理由。")
step_slide("四", "確認方向", "起草文稿",
           ["把討論與洞見寫成文稿，讀過確認方向撐得住。", "把它的話順成自己的話，補來源。"],
           "「在主 draft 沿這個方向寫一版。」　「這句『＿＿』請對照說明頁檢查，前後版本都留。」",
           ["挑一句斷言查證。", "撐不住的段落，回第三步改方向。"], ev_check,
           "挑一句斷言查證是試跑後加的動作，學員不會主動做，第 50 分鐘全場再示範一次。")
step_slide("五", "建立架構", "分成逐頁稿",
           ["把文稿分成逐頁稿。", "先用原話與 ghost deck 做第一版邏輯。"],
           "「先用我的原話排一版只有標題的 ghost deck，每頁一句。」",
           ["只讀標題連讀能講完故事。", "順序與取捨改好，再請它補每頁畫面與口述。"], ev_ghost,
           "第一版邏輯用原話當底，看得懂才判斷得了順序；連讀通過之後才變成確定的逐頁稿。分頁的原則不必另外找，一頁一句主張、畫面是證據，直接寫進對 agent 說的話裡。")
step_slide("六", "調整風格", "修改語氣",
           ["整份改成書面文，不做金句。", "自己讀一遍，改掉不像自己的。"],
           "「照這份規則逐頁改寫，標出哪些句子沒有原話依據。」",
           ["還在 Markdown 上改。", "看畫面最刺眼的口號句在這一步解決。"], ev_rules,
           "請 agent 逐頁改寫並標出沒有原話依據的句子，自己讀一遍改掉不像自己的。")
step_slide("七", "調整風格", "找排版原則",
           ["先做一頁驗路徑，之後整份產出。", "版面問題改標準重建；內容問題退回第五、六步。"],
           "「先找排版的規則寫成標準。」　「照逐頁稿與這份標準做成可編輯的 PowerPoint，做完匯出 PDF 給我看。」",
           ["備註有口述與來源；文字都是文字框。"], ev19,
           "第一次先做一頁驗路徑，之後整份產出。版面問題改規則重建，內容問題退回第五、六步。")
step_slide("八", "確認", "整個過一遍",
           ["自己講一遍並計時。", "講不順的那頁，回逐頁稿補或刪。"],
           "「估每頁口述的字數和時間。」",
           ["開頭說的需求，每項都在成品裡。", "kb/、文稿、逐頁稿、PPTX 最新版找得到。"], ev20,
           "不用兩人一組，自己找時間真的講一遍，算是一個確認。")

# 26 段
section_slide("練習", sub="練習 120 分", note="自由發揮，不收成品。")

# 27 練習
s = assert_slide("練習：題目自選", "練習 120 分")
cols = [("tag", "題目三條件", ["給誰看。", "看完要做什麼。", "材料公開或可虛構，兩小時找得到依據。"]),
        ("player-play", "開始時兩件事", ["先貼一句話讓 agent 在背景做第一版。", "開另一個視窗，走八步。"]),
        ("stack-2", "成品", ["不收，自己留著比較。", "預設題同示範題。"])]
cw = (W - 2 * M - 0.6) / 3
for i, (ic, h1, lines) in enumerate(cols):
    x = M + i * (cw + 0.3)
    rect(s, x, BODY_Y + 0.1, cw, 4.0)
    icon(s, ic, x + 0.3, BODY_Y + 0.35, 0.7, circle=WHITE)
    tb(s, x + 1.15, BODY_Y + 0.4, cw - 1.4, 0.6, h1, size=21, bold=True, anchor="m")
    tb(s, x + 0.3, BODY_Y + 1.3, cw - 0.6, 2.7, [{"text": t, "bullet": True} for t in lines], size=14, spacing=8)
notes(s, "預設題同示範題。第 10 分鐘巡一輪，寫不出受眾與用途者改用預設題。")

# 28 回看
s = assert_slide("回看：第一版和自己做的並排", "練習 120 分")
for i, (lab, sub) in enumerate([("一句話生成版", "示範開頭那一版"), ("自己逐步完成版", "八步之後")]):
    x = M + 1.0 + i * 6.4
    rect(s, x, BODY_Y + 0.1, 4.6, 2.0)
    icon(s, "stack-2", x + 0.4, BODY_Y + 0.45, 1.2)
    tb(s, x + 1.9, BODY_Y + 0.5, 2.6, 0.6, lab, size=20, bold=True, anchor="m")
    tb(s, x + 1.9, BODY_Y + 1.15, 2.6, 0.5, sub, size=13, color=MUTED)
icon(s, "arrows-left-right", W / 2 - 0.45, BODY_Y + 0.65, 0.9, circle=TINT)
qs = [("方向與洞見是自己的嗎", "確認方向"), ("順序是自己調的嗎", "建立架構"), ("風格照了哪份標準", "調整風格")]
for i, (h1, loop) in enumerate(qs):
    y = BODY_Y + 2.5 + i * 0.7
    num(s, M + 1.0, y + 0.08, i + 1, d=0.4, size=13)
    tb(s, M + 1.6, y, 5.0, 0.55, h1, size=17, bold=True, anchor="m")
    mini_tag(s, M + 6.8, y + 0.12, loop, fill=SAGE, color=DARK, w=1.3)
tb(s, M + 1.0, BODY_Y + 4.65, 11, 0.4, "說不出理由的那頁，內容還不是自己的。", size=13, color=MUTED)
notes(s, "說不出理由的那頁，內容還不是自己的。三問對回三圈。")

prs.save(OUT)
print("saved", OUT, len(prs.slides), "pages")
