"""Generate original, editable SVG teaching sketches; no external image editing."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
FONT = "PingFang TC, Noto Sans CJK TC, sans-serif"

def text(x, y, value, size=25, color="#263449", weight=400):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(value)}</text>'

def rect(x, y, w, h, fill="#ffffff", stroke="#d7dfe8"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}"/>'

def svg(name, title, body, h):
    data = f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="1200" height="{h}" fill="#f4f6f8"/>{body}</svg>'
    (ROOT / name).write_text(data, encoding="utf-8")

body = text(40, 57, "同一個想法，留下三種可以接續使用的版本", 31, weight=600)
cards = [
    (40, "論點", "我想傳達什麼？", ["AI 也可能協助補足經驗", "依據：客服研究 v2", "限制：效果依情境而異", "棄案：人人都會同等受益"]),
    (435, "文章", "把脈絡說完整", ["先交代研究的工作情境，", "再說明結果與適用範圍，", "最後連到自己的工作。", "保留引用與修改理由。"]),
    (830, "投影片", "安排口述與畫面", ["畫面：一個重點與研究圖", "口述：情境、限制、例子", "頁腳：短來源", "備註：完整資料與連結"]),
]
for x, label, sub, lines in cards:
    body += rect(x, 93, 330, 350)
    body += text(x+24, 139, label, 34, "#126b72", 600)
    body += text(x+24, 182, sub, 23)
    body += f'<path d="M{x+24} 202 H{x+306}" stroke="#d7dfe8"/>'
    for i, line in enumerate(lines):
        body += text(x+24, 246+i*45, line, 21)
for x in (385, 780):
    body += text(x, 285, "→", 33, "#126b72")
body += text(40, 489, "課程自繪示意；三種產出物為本課安排，並非引用作者的原版分類。", 21, "#516174")
svg("three-artifacts.svg", "論點、文章與投影片的內容對照", body, 520)

body = text(40, 58, "充實文章：讓主張有依據，也保留適用範圍", 31, weight=600)
body += rect(40, 95, 500, 300, "#fff6ec", "#efcfab")
body += text(66, 143, "待修正的草稿", 28, "#885019", 600)
body += text(66, 200, "使用 AI 能提升所有人的工作效率。", 25)
body += text(66, 264, "「所有人」超出了這份研究的範圍。", 22, "#885019")
body += text(66, 308, "尚未交代哪種工作、如何衡量。", 22, "#885019")
body += text(564, 253, "→", 34, "#126b72")
body += rect(630, 95, 530, 300, "#edf8f6", "#aacfc9")
body += text(656, 143, "補入資料與限制", 28, "#126b72", 600)
for i, line in enumerate(["一項客服研究發現，導入 AI 助理後，", "每小時解決問題數平均增加 15%。", "較少經驗者受益較多；其他工作情境", "是否適用，仍需另外確認。"]):
    body += text(656, 200+i*43, line, 23)
body += text(40, 447, "資料：Brynjolfsson、Li、Raymond，Generative AI at Work，2024 v2。", 21, "#516174")
body += text(40, 486, "課程自擬的改寫例子；左側句子不是引文，也不是研究結論。", 21, "#516174")
svg("paragraph-before-after.svg", "文章草稿補入研究依據與限制的示意", body, 520)
