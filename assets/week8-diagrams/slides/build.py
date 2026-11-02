#!/usr/bin/env python3
"""第八週投影片式示意圖：每頁產生一份 HTML，再以 Chrome 無頭模式輸出 1600×900 的 PNG（2 倍解析度）。

用法：python3 assets/week8-diagrams/slides/build.py [頁碼 ...]
內容依 drafts/25-week8-slides.md。w8-12-map.json 只含地圖線條與測站的繪圖座標，不含站碼。
Icon 為 24×24 線條圖，樣式比照 Lucide。
"""
import json
import math
import random
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TMP = HERE / ".html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INK, MUTED, LINE, BG, ACCENT, ACCENT_BG, BLUE, BLUE_BG = "#2A2623", "#6B6560", "#D8D2C9", "#F5F2EC", "#BE8979", "#F6E9E4", "#5F7F95", "#E8EFF3"
ACCENT_D, BLUE_D, GOOD = "#A5604B", "#44657B", "#5E8467"

ICONS = {
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8M16 17H8M10 9H8"/>',
    "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
    "wave": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "ok": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "circle": '<circle cx="12" cy="12" r="10"/>',
    "warn": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4M12 17h.01"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "bot": '<path d="M12 8V4H8"/><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M2 14h2M20 14h2M15 13v2M9 13v2"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "drive": '<path d="M22 12H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><path d="M6 16h.01M10 16h.01"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "history": '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5M12 7v5l4 2"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "plus": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8M12 8v8"/>',
    "cursor": '<path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"/><path d="m13 13 6 6"/>',
    "move": '<path d="m5 9-3 3 3 3M9 5l3-3 3 3M15 19l-3 3-3-3M19 9l3 3-3 3M2 12h20M12 2v20"/>',
    "eye": '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    "pencil": '<path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/>',
    "refresh": '<path d="M21 12a9 9 0 1 1-2.64-6.36L21 8"/><path d="M21 3v5h-5"/>',
    "tasks": '<path d="m3 17 2 2 4-4M3 7l2 2 4-4M13 6h8M13 12h8M13 18h8"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.12 8.12 12 12M20 4 8.12 15.88M14.8 14.8 20 20"/>',
    "cross": '<circle cx="12" cy="12" r="10"/><path d="M22 12h-4M6 12H2M12 6V2M12 22v-4"/>',
    "box": '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="M3.3 7 12 12l8.7-5M12 22V12"/>',
    "trash": '<path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>',
    "chart": '<path d="M3 3v18h18M18 17V9M13 17V5M8 17v-3"/>',
    "flask": '<path d="M10 2v7.31M14 9.3V2M8.5 2h7M14 9.3a6.5 6.5 0 1 1-4 0M5.52 16h12.96"/>',
    "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/>',
    "sliders": '<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3M14 2v4M8 10v4M16 18v4"/>',
    "patch": '<path d="M19.44 7.85c-.49.49-1.28.49-1.77 0l-1.51-1.51a1.25 1.25 0 0 1 0-1.77l2.4-2.4A5 5 0 0 0 12 8.5l-8 8a2.12 2.12 0 0 0 3 3l8-8a5 5 0 0 0 6.83-6.56z"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
}


def ic(name, size=32, color=INK, sw=1.9):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def badge(name, kind="", size=34):
    """圓底 icon。"""
    col = {"a": ACCENT_D, "b": BLUE_D, "": INK, "g": GOOD}[kind]
    bg = {"a": ACCENT_BG, "b": BLUE_BG, "": BG, "g": "#E7EFE9"}[kind]
    d = size + 26
    return f'<span class="badge" style="width:{d}px;height:{d}px;background:{bg}">{ic(name, size, col)}</span>'


def arrow(w=56, color=MUTED, dash=False):
    d = ' stroke-dasharray="7 6"' if dash else ""
    return (f'<svg class="arr" width="{w}" height="24" viewBox="0 0 {w} 24" fill="none" stroke="{color}" stroke-width="2.6" '
            f'stroke-linecap="round" stroke-linejoin="round"><path d="M2 12H{w - 3}"{d}/><path d="M{w - 12} 4l9 8-9 8"/></svg>')


CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1600px;height:900px;overflow:hidden}}
body{{background:#FCFBF8;color:{INK};font-family:"PingFang TC","Noto Sans CJK TC","Hiragino Sans GB",sans-serif;font-size:24px;line-height:1.4;position:relative}}
.sec{{position:absolute;left:70px;top:40px;font-size:22px;color:{ACCENT_D};font-weight:600}}
h1{{position:absolute;left:70px;top:72px;font-size:44px;font-weight:700;line-height:1.2}}
.msg{{position:absolute;left:70px;right:70px;top:136px;font-size:30px;color:{INK};font-weight:500;line-height:1.35;border-left:6px solid {ACCENT};padding-left:18px}}
.body{{position:absolute;left:70px;right:70px;top:215px;bottom:62px}}
.foot{{position:absolute;left:70px;right:70px;bottom:22px;display:flex;justify-content:space-between;font-size:18px;color:{MUTED}}}
.ic{{display:block;flex:none}} .arr{{display:block;flex:none}}
.badge{{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;flex:none}}
.row{{display:flex;align-items:center}} .col{{display:flex;flex-direction:column}}
.card{{background:#fff;border:1.5px solid {LINE};border-radius:16px;padding:18px 22px}}
.a{{background:{ACCENT_BG};border-color:{ACCENT}}} .b{{background:{BLUE_BG};border-color:{BLUE}}}
.t{{font-weight:700;font-size:28px;line-height:1.3}} .s{{font-size:24px;color:{MUTED};line-height:1.4}}
.big{{font-size:60px;font-weight:700;line-height:1.05}}
.tag{{display:inline-block;font-size:20px;font-weight:600;padding:3px 13px;border-radius:999px;background:{BG};color:{MUTED}}}
.tag.a{{background:{ACCENT_BG};color:{ACCENT_D}}} .tag.b{{background:{BLUE_BG};color:{BLUE_D}}}
.note{{font-size:19px;color:{MUTED}}}
.abs{{position:absolute}}
"""

SLIDES = {}


def slide(no, name, sec, title, msg):
    def deco(fn):
        SLIDES[no] = (name, sec, title, msg, fn)
        return fn
    return deco


# ---------------- 第 4 頁
@slide(4, "event-order", "一、合併的理由", "消除格式錯誤", "檔名、時間與格式的問題，在挑波過程中已不會產生")
def s4():
    def ev(x, y, label, c, bg):
        return (f'<g><circle cx="{x}" cy="{y}" r="27" fill="{bg}" stroke="{c}" stroke-width="3"/>'
                f'<text x="{x}" y="{y + 9}" text-anchor="middle" font-size="26" font-weight="700" fill="{c}">{label}</text></g>')

    def axis(y, name):
        ticks = "".join(f'<line x1="{170 + i * 120}" y1="{y - 7}" x2="{170 + i * 120}" y2="{y + 7}" stroke="{MUTED}" stroke-width="2"/>'
                        f'<text x="{170 + i * 120}" y="{y + 56}" text-anchor="middle" font-size="22" fill="{MUTED}">{t}</text>'
                        for i, t in enumerate(["08:00", "08:02", "08:04", "08:06", "08:08"]))
        return (f'<text x="0" y="{y + 9}" font-size="24" font-weight="600" fill="{INK}">{name}</text>'
                f'<line x1="150" y1="{y}" x2="760" y2="{y}" stroke="{MUTED}" stroke-width="2.5"/>{ticks}')
    svg = (f'<svg width="750" height="462" viewBox="0 0 780 480" font-family="inherit">'
           f'<defs><marker id="m" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9z" fill="{ACCENT_D}"/></marker></defs>'
           + axis(90, "定位前") + axis(350, "定位後")
           + ev(350, 90, "1", BLUE_D, BLUE_BG) + ev(530, 90, "2", ACCENT_D, ACCENT_BG)
           + ev(350, 350, "1", BLUE_D, BLUE_BG) + ev(230, 350, "2", ACCENT_D, ACCENT_BG)
           + f'<path d="M520 118 C 500 230, 300 220, 242 318" fill="none" stroke="{ACCENT_D}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#m)"/>'
           + f'<line x1="350" y1="118" x2="350" y2="318" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="4 6"/>'
           + f'<text x="500" y="225" font-size="24" fill="{ACCENT_D}" font-weight="600">定位到很遠的地震，</text><text x="500" y="258" font-size="24" fill="{ACCENT_D}" font-weight="600">發震時間變早</text>'
           + '</svg>')
    def flow(tag, tagc, steps, end, endc):
        chips = arrow(30).join(f'<span style="font-size:25px">{s}</span>' for s in steps)
        return (f'<div class="card {tagc} col" style="padding:24px 28px;flex:1;justify-content:center;gap:10px"><span class="tag {tagc}" style="background:#fff;align-self:flex-start">{tag}</span>'
                f'<div class="row" style="flex-wrap:wrap;gap:8px 10px;margin-top:12px">{chips}</div>'
                f'<div class="row" style="gap:10px;margin-top:12px;font-weight:700;font-size:28px;color:{endc}">{end}</div></div>')
    return (f'<div class="row" style="gap:34px;align-items:flex-start;height:100%">'
            f'<div class="col" style="width:790px"><div class="card" style="padding:26px 20px 14px">{svg}</div>'
            f'<div class="note" style="margin-top:10px">圓圈的數字為事件編號，時間為示意</div></div>'
            f'<div class="col" style="flex:1;gap:22px;height:100%">'
            + flow("現行流程", "b", ["過程中決定檔名與順序", "定位改變發震時間"], ic("warn", 28, BLUE_D) + "順序顛倒，由 QC 退回", BLUE_D)
            + flow("翻新之後", "a", ["事件存於資料庫", "定位不影響順序", "輸出時才排序"], ic("ok", 28, ACCENT_D) + "同時產生檔名，不必檢查", ACCENT_D)
            + '</div></div>')


# ---------------- 第 7 頁
@slide(7, "format-limit", "二、資料與介面", "格式的限制", "各程式獨立演化，彼此以檔案交接，格式沿用數十年之後已無法應付現在的需求")
def s7():
    nodes = [("切事件程式", "scissors", 120, 60), ("挑波程式", "wave", 490, 60), ("定位程式", "pin", 120, 370), ("QC 與入庫程式", "shield", 490, 370)]
    lines = "".join(f'<line x1="{x + 70}" y1="{y + 40}" x2="340" y2="240" stroke="{MUTED}" stroke-width="3"/>' for _, _, x, y in nodes)
    boxes = "".join(f'<div class="card abs row" style="left:{x - 50}px;top:{y - 10}px;width:240px;height:84px;gap:12px;padding:10px 14px">{ic(i, 34, BLUE_D)}<span class="t" style="font-size:23px">{n}</span></div>' for n, i, x, y in nodes)
    hub = (f'<div class="abs col" style="left:232px;top:150px;width:216px;height:180px;align-items:center;justify-content:center;background:{ACCENT_BG};'
           f'border:2.5px solid {ACCENT};border-radius:20px">{ic("file", 62, ACCENT_D)}<div class="t" style="margin-top:6px">固定的檔案格式</div>'
           f'<div class="row" style="gap:6px;color:{ACCENT_D};font-size:20px">{ic("lock", 22, ACCENT_D)}難以更改</div></div>')
    limits = [("history", "無法記錄歷史", "檔案只留下最後的結果，追查修改要比對各階段的檔案"),
              ("target", "精度受到限制", "數值的位數受格式限制，無法隨需求提高"),
              ("plus", "新資訊難以加入", "任何改動都會牽動依賴這個格式的所有程式")]
    cards = "".join(f'<div class="card row" style="gap:22px;flex:1">{badge(i, "a", 40)}<div><div class="t">{t}</div><div class="s">{s}</div></div></div>' for i, t, s in limits)
    return (f'<div class="row" style="gap:40px;height:100%;align-items:stretch">'
            f'<div style="position:relative;width:690px;height:100%;top:50px"><svg class="abs" style="left:0;top:0" width="690" height="480">{lines}</svg>{hub}{boxes}</div>'
            f'<div class="col" style="flex:1;gap:20px">{cards}</div></div>')


# ---------------- 第 9 頁
@slide(9, "project-db", "二、資料與介面", "專案資料庫", "資料與處理都在專案內進行，因此可以保留每一次的歷史")
def s9():
    def ver(n, cur, res, top):
        k = "a" if cur else ""
        tag = f'<span class="tag a" style="background:#fff">目前採用</span>' if cur else ""
        return (f'<div class="card {k} row abs" style="left:300px;top:{top}px;width:430px;height:100px;gap:14px;padding:8px 18px">{ic("pin", 32, ACCENT_D if cur else MUTED)}'
                f'<div><div class="t" style="font-size:25px">定位解第 {n} 版 {tag}</div><div class="s" style="font-size:21px">{res}</div></div></div>')
    jobs = [("讀入相位檔", "輸入"), ("定位", "第 1 版"), ("修改挑選後定位", "第 2 版"), ("修改挑選後定位", "第 3 版"), ("輸出相位檔", "輸出")]
    joblist = "".join(f'<div class="row" style="gap:12px;padding:11px 0;border-top:{"none" if i == 0 else "1px solid " + LINE}">{ic("clock", 24, MUTED)}<span style="font-size:24px">{a}</span><span class="tag" style="margin-left:auto;font-size:19px">{b}</span></div>' for i, (a, b) in enumerate(jobs))
    tree = (f'<svg class="abs" style="left:0;top:0" width="740" height="480" fill="none" stroke="{MUTED}" stroke-width="2.5">'
            f'<path d="M250 190 C 280 190, 270 50, 300 50M250 190 H300M250 190 C 280 190, 270 330, 300 330"/>'
            f'<path d="M515 380 V 420M660 380 V 420" stroke-dasharray="5 5"/></svg>')
    event = (f'<div class="card abs col" style="left:0;top:85px;width:250px;height:210px;align-items:center;justify-content:center;border:2.5px solid {INK}">'
             f'{ic("wave", 50, INK)}<div class="t" style="margin-top:6px">事件</div><span class="tag" style="margin-top:6px">有自己的狀態</span></div>')
    sub = (f'<div class="abs row" style="left:300px;top:420px;width:430px;gap:12px">'
           f'<div class="card" style="flex:1;padding:10px 14px;font-size:21px;text-align:center">挑選與到時的關聯</div>'
           f'<div class="card" style="width:120px;padding:10px 14px;font-size:21px;text-align:center">規模</div></div>')
    return (f'<div style="position:relative;height:100%">{tree}{event}{ver(1, False, "第一次定位的結果", 0)}{ver(2, False, "修改挑選之後", 140)}{ver(3, True, "最新的結果，舊版仍保留", 280)}{sub}'
            f'<div class="abs col" style="left:790px;top:0;width:670px;gap:18px">'
            f'<div class="card" style="padding:14px 22px"><div class="row" style="gap:12px;margin-bottom:6px">{ic("history", 30, BLUE_D)}<span class="t">工作紀錄</span><span class="note" style="margin-left:6px">每一次輸入與輸出各記一筆</span></div>{joblist}</div>'
            f'<div class="card b row" style="gap:20px">{badge("drive", "b", 38)}<div><div class="t">波形只建索引，原檔留在外部</div><div class="s" style="color:{INK}">連續波形檔一天約 43 GB，不複製進資料庫</div></div></div>'
            f'</div>'
            f'<div class="abs note row" style="left:0;bottom:0;gap:8px">{ic("bulb", 24, MUTED)}想法來自反射震測處理系統與其他地震分析軟體，資料拆分依 QuakeML 的概念</div></div>')


# ---------------- 第 12 頁
@slide(12, "page-map", "三、畫面", "測站分頁", "不同分頁中位置相近的列，對應的測站在地圖上也相近")
def s12():
    m = json.loads((HERE / "w8-12-map.json").read_text())
    def panel(key, title, c, med):
        return (f'<div class="col" style="align-items:center"><div class="t" style="color:{c}">{title}</div>'
                f'<svg width="{m["w"]}" height="{m["h"]}" viewBox="0 0 {m["w"]} {m["h"]}" style="margin-top:6px">{m[key]}</svg>'
                f'<div class="row" style="gap:8px;margin-top:0;font-size:22px;color:{MUTED}">距離中位數 <b style="font-size:32px;color:{c}">{med}</b> 公里</div></div>')
    rows = [("第 1 頁", "第 2 頁", "84", "140"), ("第 1 頁", "第 3 頁", "39", "151"), ("第 2 頁", "第 3 頁", "73", "134")]
    tr = "".join(f'<tr><td style="padding:9px 8px;border-top:1px solid {LINE}">{a} 與 {b}</td><td style="text-align:right;padding:9px 8px;border-top:1px solid {LINE};font-weight:700;color:{ACCENT_D}">{c}</td><td style="text-align:right;padding:9px 8px;border-top:1px solid {LINE};color:{BLUE_D}">{d}</td></tr>' for a, b, c, d in rows)
    side = (f'<div class="col" style="flex:1;gap:18px">'
            f'<div class="card row" style="gap:18px">{badge("users", "a", 36)}<div><div class="t">請教使用者才得知的設計</div><div class="s">分頁切換之後，眼睛停在相同的位置，看到的仍是同一區域的測站</div></div></div>'
            f'<div class="card"><div class="row" style="gap:10px;margin-bottom:4px">{ic("search", 28, BLUE_D)}<span class="t">以排序表查證</span></div>'
            f'<table style="width:100%;border-collapse:collapse;font-size:22px"><tr style="color:{MUTED};font-size:19px"><td style="padding:4px 8px">同一列的兩站</td><td style="text-align:right;padding:4px 8px">實際（公里）</td><td style="text-align:right;padding:4px 8px">隨機（公里）</td></tr>{tr}</table></div>'
            f'<div class="note">地圖連接第 1 頁與第 3 頁同一列的兩站，圖面只顯示本島範圍內的測站</div></div>')
    return (f'<div class="row" style="gap:30px;height:100%;align-items:flex-start;margin-top:-12px">'
            + panel("same", "實際的排列", ACCENT_D, m["median_same"]) + panel("shuf", "隨機打亂", BLUE_D, m["median_shuf"]) + side + '</div>')


# ---------------- 第 14 頁
@slide(14, "feedback", "三、畫面", "即時回饋", "所有資訊都即時更新，是介面現代化最大的理由")
def s14():
    def step(i, t):
        return f'<div class="col" style="align-items:center;width:150px;text-align:center">{badge(i, "b", 34)}<div style="font-size:24px;margin-top:6px">{t}</div></div>'
    past = "".join(step(i, t) + (arrow(44) if n < 3 else "") for n, (i, t) in enumerate([("pencil", "修改挑選"), ("refresh", "全部跑完"), ("chart", "自行畫圖"), ("eye", "看到結果")]) )
    # 操作與面板的對應
    ops = [("pencil", "修改挑選", "重新定位，地圖與殘差更新"), ("eye", "懸停", "資訊欄顯示這一站的殘差"), ("move", "拖曳到時線", "S−P 距離圓即時更新"), ("cursor", "點選地圖", "波形列表跳到這一站的分頁")]
    grid = "".join(f'<div class="card row" style="gap:18px;padding:40px 22px">{badge(i, "a", 42)}<div><div class="t">{a}</div><div class="s">{b}</div></div></div>' for i, a, b in ops)
    return (f'<div class="col" style="gap:20px;height:100%">'
            f'<div class="card b row" style="gap:26px;padding:16px 26px"><div style="width:120px"><span class="tag b" style="background:#fff">過去</span><div class="s" style="margin-top:8px;color:{INK}">週期很長</div></div>'
            f'<div class="row" style="gap:6px;flex:1;justify-content:center">{past}</div></div>'
            f'<div class="card a" style="padding:16px 26px;flex:1"><div class="row" style="gap:26px;align-items:flex-start"><div style="width:120px"><span class="tag a" style="background:#fff">現在</span><div class="s" style="margin-top:8px;color:{INK}">操作的當下<br>即得到結果</div></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1">{grid}</div></div>'
            f'<div class="row" style="gap:12px;margin-top:26px;margin-left:146px;font-size:30px;font-weight:600;color:{ACCENT_D}">{ic("bulb", 30, ACCENT_D)}累積出體感，知道各個數值如何影響最終結果</div></div></div>')


# ---------------- 第 17 頁
@slide(17, "task-rewrite", "三、畫面", "正向引導", "QC 由批評與阻擋轉為正向引導")
def s17():
    bad = [("測站數不足", "挑波剛開始就出現"), ("近站未挑選", "要自行尋找是哪幾站"), ("方位角空隙過大", "只列出結果"), ("殘差過大", "只列出結果")]
    left = "".join(f'<div class="row" style="gap:14px;padding:22px 0;border-top:1px solid {LINE}">{ic("x", 32, ACCENT_D, 2.6)}<div><div style="font-size:27px;font-weight:600">{a}</div>' + (f'<div class="s" style="font-size:20px">{b}</div>' if b else "") + '</div></div>' for a, b in bad)
    quests = [("ok", GOOD, "挑選足夠的測站", "已完成", False), ("ok", GOOD, "定出震央", "已完成", False), ("cross", ACCENT_D, "確保震央穩定", "尚有 2 站近站，點選即前往", True), ("circle", LINE, "檢查離群的到時", "", False), ("circle", LINE, "量測規模", "", False)]
    right = "".join(f'<div class="row" style="gap:14px;padding:17px 14px;border-radius:10px;{"background:" + ACCENT_BG if cur else ""}">{ic(i, 30, c, 2.2)}<div style="flex:1;font-size:27px;font-weight:{700 if cur else 500};color:{INK if i != "circle" else MUTED}">{t}</div><div class="s" style="font-size:22px;{"color:" + ACCENT_D if cur else ""}">{n}</div></div>' for i, c, t, n, cur in quests)
    strip_items = [("pencil", "挑波時不阻擋"), ("db", "存檔只寫入資料庫，性質接近暫存"), ("shield", "實際的攔截在事件總覽的 QC")]
    strip = "".join((arrow(40) if n else "") + f'<div class="row" style="gap:10px">{ic(i, 30, BLUE_D)}<span style="font-size:23px">{t}</span></div>' for n, (i, t) in enumerate(strip_items))
    return (f'<div class="col" style="gap:16px;height:100%"><div class="row" style="gap:24px;align-items:stretch;flex:1">'
            f'<div class="card col" style="width:430px"><div class="row" style="gap:10px;margin-bottom:8px">{ic("warn", 28, MUTED)}<span class="t" style="color:{MUTED}">原本：錯在哪裡</span></div>{left}</div>'
            f'<div style="align-self:center">{arrow(64, ACCENT_D)}</div>'
            f'<div class="card col" style="flex:1;border:2px solid {ACCENT}"><div class="row" style="gap:10px">{ic("tasks", 30, ACCENT_D)}<span class="t">現在：還有哪件事要完成</span></div>'
            f'<div class="row" style="gap:10px;margin:8px 0 8px"><span class="tag a">主線</span><span style="font-size:23px">定出一個可以交付的地震</span><span class="note" style="margin-left:auto">不做分數、次數或排名</span></div>{right}</div></div>'
            f'<div class="card b row" style="justify-content:center;gap:16px;padding:12px 18px">{strip}</div></div>')


# ---------------- 第 20 頁
@slide(20, "stages", "四、接上現行流程", "分階段替換", "每一段都能單獨接上現行流程，不必一次全換")
def s20():
    new = [("scissors", "切地震"), ("cross", "定地震"), ("shield", "QC 與事件總覽")]
    old = [("wave", "現行的挑波程式"), ("shield", "現行的 QC 程式"), ("box", "現行的入庫與發布")]
    out = ["事件波形檔", "相位檔", "入庫包"]
    W = 400
    cols = ""
    for i in range(3):
        cols += (f'<div class="col" style="flex:1;align-items:center">'
                 f'<div class="card a row" style="width:100%;gap:14px;justify-content:center;height:110px">{ic(new[i][0], 36, ACCENT_D)}<span class="t">{new[i][1]}</span></div>'
                 f'<div style="width:3px;height:26px;background:{MUTED}"></div>'
                 f'<div class="row" style="gap:10px;padding:8px 18px;border:2px dashed {MUTED};border-radius:12px;background:#fff">{ic("file", 28, INK)}<span style="font-size:24px;font-weight:600">匯出{out[i]}</span></div>'
                 f'<svg width="24" height="42" viewBox="0 0 24 42" fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v36M4 30l8 9 8-9"/></svg>'
                 f'<div class="card b row" style="width:100%;gap:14px;justify-content:center;height:110px">{ic(old[i][0], 36, BLUE_D)}<span class="t" style="font-size:24px">{old[i][1]}</span></div></div>')
    labels = (f'<div class="col" style="width:112px;margin-right:18px;height:338px;justify-content:space-between;padding:32px 0">'
              f'<div class="t" style="color:{ACCENT_D}">新系統</div><div class="t" style="color:{BLUE_D}">現行<br>流程</div></div>')
    proof = [("263", "相位檔讀入再寫出，逐位元組相同"), ("228", "重新製作事件波形檔，逐位元組相同")]
    pcards = "".join(f'<div class="card row" style="gap:20px;flex:1"><div class="big" style="color:{ACCENT_D}">{n}</div><div class="s" style="color:{INK};flex:1">{t}</div>{ic("ok", 42, GOOD)}</div>' for n, t in proof)
    return (f'<div class="col" style="gap:20px;height:100%"><div class="row" style="align-items:flex-start;gap:20px;width:100%">{labels}{cols}</div>'
            f'<div class="row" style="gap:22px;flex:1">{pcards}</div></div>')


# ---------------- 第 21 頁
@slide(21, "weight-snr", "五、新的處理想法", "自動權重", "同仁給的權重與訊噪比關係一致，因此可以算出建議的權重，讓處理標準化")
def s21():
    d1, d2 = [1.11, .37, .19, .10, .04], [1.07, .35, .15, .08, .04]
    W, H, L, T, R, B = 810, 590, 88, 20, 150, 66
    px = lambda i: L + i * (W - L - R) / 4
    py = lambda v: T + (1.2 - v) / 1.2 * (H - T - B)
    grid = "".join(f'<line x1="{L}" y1="{py(v)}" x2="{W - R}" y2="{py(v)}" stroke="{LINE}" stroke-width="1"/><text x="{L - 14}" y="{py(v) + 7}" text-anchor="end" font-size="20" fill="{MUTED}">{v:.1f}</text>' for v in (0, .4, .8, 1.2))
    xt = "".join(f'<text x="{px(i)}" y="{H - B + 32}" text-anchor="middle" font-size="22" fill="{MUTED}">{i}</text>' for i in range(5))
    def ser(d, c, shape):
        pts = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(d))
        marks = "".join((f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="7" fill="{c}" stroke="#fff" stroke-width="2"/>' if shape == "c" else
                         f'<rect x="{px(i) - 6.5:.1f}" y="{py(v) - 6.5:.1f}" width="13" height="13" rx="2" fill="{c}" stroke="#fff" stroke-width="2"/>') for i, v in enumerate(d))
        return f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.5"/>{marks}'
    C1, C2 = "#C2603F", "#2E7EB8"
    legend = (f'<g transform="translate({px(1) + 30},{T + 20})"><circle cx="8" cy="0" r="7" fill="{C1}"/><text x="24" y="7" font-size="22" fill="{INK}">9 月 1 日（3,814 個挑選）</text>'
              f'<rect x="1.5" y="27" width="13" height="13" rx="2" fill="{C2}"/><text x="24" y="41" font-size="22" fill="{INK}">9 月 2 日（6,073 個挑選）</text></g>')
    chart = (f'<svg width="{W - R + 40}" height="{H}" viewBox="0 0 {W - R + 40} {H}" font-family="inherit">{grid}{xt}{ser(d1, C1, "c")}{ser(d2, C2, "s")}{legend}'
             f'<text x="{(L + W - R) / 2}" y="{H - 4}" text-anchor="middle" font-size="22" fill="{INK}">同仁給的 P 波權重（0 最清楚）</text>'
             f'<text transform="translate(22,{(T + H - B) / 2}) rotate(-90)" text-anchor="middle" font-size="22" fill="{INK}">訊噪比中位數（log10）</text></svg>')
    rules = [("0、1", "不濾波就清楚", "eye"), ("2", "要濾波才清楚", "sliders"), ("3", "濾波後仍不清楚", "search")]
    rc = "".join(f'<div class="card row" style="gap:18px;padding:24px 22px">{ic(i, 38, ACCENT_D)}<div style="flex:1;font-size:27px">{t}</div><div class="row" style="gap:8px"><span class="note">權重</span><b style="font-size:34px;color:{ACCENT_D}">{w}</b></div></div>' for w, t, i in rules)
    return (f'<div class="row" style="gap:30px;height:100%;align-items:flex-start"><div class="card" style="padding:14px 10px 8px">{chart}</div>'
            f'<div class="col" style="flex:1;gap:14px"><div class="row" style="gap:12px">{ic("bulb", 30, INK)}<span class="t">判斷的規則</span></div>{rc}'
            f'<div class="card b" style="margin-top:6px"><div class="row" style="gap:12px;margin-bottom:4px">{ic("flask", 28, BLUE_D)}<span class="t" style="font-size:26px">實驗性功能，尚未定案</span></div><div class="s" style="color:{INK};font-size:23px">目前改用起始分析的訊噪比，門檻與同仁確認之前不視為定案</div></div></div></div>')


# ---------------- 第 22 頁
@slide(22, "pick-first", "五、新的處理想法", "先挑再關聯", "看到就先挑，再組成地震，可能減少許多步驟")
def s22():
    # 走時圖示意：兩個地震的挑選在距離與時間上各成一條斜線
    W, H = 420, 300
    a = [(30, 40), (80, 62), (130, 92), (190, 118), (250, 150), (320, 186)]
    b = [(50, 150), (110, 172), (170, 196), (240, 222), (310, 252)]
    a = [(x, 296 - y) for x, y in a]
    b = [(x, 296 - y) for x, y in b]
    def plot(ca, cb, lines):
        o = f'<svg width="{W}" height="370" viewBox="0 0 {W} {H}"><line x1="16" y1="282" x2="404" y2="282" stroke="{MUTED}" stroke-width="2"/><line x1="16" y1="282" x2="16" y2="14" stroke="{MUTED}" stroke-width="2"/>'
        o += f'<text x="400" y="274" text-anchor="end" font-size="18" fill="{MUTED}">時間</text><text x="26" y="30" font-size="18" fill="{MUTED}">距離</text>'
        if lines:
            o += f'<line x1="{a[0][0]}" y1="{a[0][1]+0}" x2="{a[-1][0]}" y2="{a[-1][1]}" stroke="{ca}" stroke-width="2.5" opacity=".55"/><line x1="{b[0][0]}" y1="{b[0][1]}" x2="{b[-1][0]}" y2="{b[-1][1]}" stroke="{cb}" stroke-width="2.5" opacity=".55"/>'
        for x, y in a:
            o += f'<rect x="{x-3}" y="{y-13}" width="6" height="26" rx="2" fill="{ca}"/>'
        for x, y in b:
            o += f'<rect x="{x-3}" y="{y-13}" width="6" height="26" rx="2" fill="{cb}"/>'
        return o + '</svg>'
    old = [("flag", "先開一個事件"), ("wave", "看到遠處的訊號，不確定是否同一個地震"), ("pencil", "仍先挑選"), ("trash", "不是同一個就刪除")]
    oldh = "".join(f'<div class="row" style="gap:12px;padding:15px 0">{ic(i, 32, BLUE_D if i != "trash" else ACCENT_D)}<span style="font-size:26px">{t}</span></div>' for i, t in old)
    return (f'<div class="row" style="gap:24px;height:100%;align-items:stretch">'
            f'<div class="card b col" style="width:430px"><span class="tag b" style="background:#fff;align-self:flex-start">原本的做法</span><div style="margin-top:10px">{oldh}</div>'
            f'<div class="s" style="margin-top:auto;color:{INK}">已經挑好的挑選其實可以先留著，再判斷是否屬於其他地震</div></div>'
            f'<div class="card a col" style="flex:1"><span class="tag a" style="background:#fff;align-self:flex-start">先挑再關聯</span>'
            f'<div class="row" style="gap:6px;margin-top:6px"><div class="col" style="align-items:center"><div class="t" style="font-size:25px">混在一起的挑選</div>{plot(INK, INK, False)}</div>'
            f'<div class="col" style="align-items:center;gap:4px">{ic("bot", 32, ACCENT_D)}<div style="font-size:19px;color:{ACCENT_D};font-weight:600">關聯程式</div>{arrow(70, ACCENT_D)}</div>'
            f'<div class="col" style="align-items:center"><div class="t" style="font-size:25px">分成不同的地震</div>{plot(ACCENT_D, BLUE_D, True)}</div></div>'
            f'<div class="row" style="gap:18px;margin-top:auto;background:#fff;border-radius:12px;padding:10px 20px"><div class="big" style="color:{ACCENT_D};font-size:52px">108<span style="font-size:28px;color:{MUTED}"> / 119</span></div><div style="font-size:23px">把同一時間窗的挑選混在一起交給關聯程式，找回的事件數</div></div>'
            f'</div></div>')


# ---------------- 第 23 頁
@slide(23, "sdlc", "六、開發的時間成本", "時間成本的轉移", "Agent 降低了撰寫功能的成本，但軟體開發有很大一部分在設計的迭代")
def s23():
    def seg(flex, t, kind, icon=None):
        st = {"a": f"background:{ACCENT_BG};border:2px solid {ACCENT};color:{ACCENT_D}", "b": f"background:{BLUE_BG};border:2px solid {BLUE};color:{BLUE_D}", "": f"background:{BG};border:2px solid {LINE};color:{MUTED}"}[kind]
        i = ic(icon, 32, {"a": ACCENT_D, "b": BLUE_D, "": MUTED}[kind]) if icon else ""
        return f'<div class="row" style="flex:{flex};height:130px;justify-content:center;gap:8px;border-radius:12px;font-size:25px;font-weight:600;text-align:center;{st};padding:0 6px">{i}<span>{t}</span></div>'
    loop = (f'<svg class="abs" style="left:0;top:-58px" width="100%" height="60" viewBox="0 0 860 60" preserveAspectRatio="none" fill="none" stroke="{ACCENT_D}" stroke-width="3">'
            f'<path d="M210 56 C 300 0, 600 0, 690 56" stroke-dasharray="8 6"/></svg>')
    past = seg(3, "規劃資料庫與資料格式", "b", "db") + seg(4, "撰寫功能與重構", "b", "wrench") + seg(1.2, "測試", "", "check") + seg(1, "部署", "")
    now_ = (seg(1.4, "規劃", "") + seg(.9, "實作", "", "bot")
            + f'<div style="flex:5.9;position:relative;display:flex;gap:6px">{seg(1, "設計", "a", "pencil")}{seg(1, "測試與驗證", "a", "eye")}'
              f'<div class="abs row" style="left:0;right:0;top:-56px;justify-content:center;gap:10px;color:{ACCENT_D};font-weight:700;font-size:28px">{ic("refresh", 30, ACCENT_D, 2.4)}反覆迭代，直到使用者認為合用</div></div>'
            + seg(1, "部署", ""))
    points = [("flask", "功能變多，要測試的項目隨之增加", "因此拆到可以獨立開關、獨立驗證"), ("cross", "自動測試處理格式與計算", "操作與畫面只能由人實際使用來判斷")]
    pc = "".join(f'<div class="card row" style="flex:1;gap:18px">{badge(i, "a", 34)}<div><div class="t" style="font-size:24px">{a}</div><div class="s">{b}</div></div></div>' for i, a, b in points)
    return (f'<div class="col" style="height:100%;gap:0">'
            f'<div class="row" style="gap:18px"><div class="t" style="width:90px;color:{BLUE_D}">過去</div><div class="row" style="flex:1;gap:6px">{past}</div></div>'
            f'<div class="row" style="gap:18px;margin-top:96px"><div class="t" style="width:90px;color:{ACCENT_D}">現在</div><div class="row" style="flex:1;gap:6px">{now_}</div></div>'
            f'<div class="note" style="margin:10px 0 0 108px">方塊寬度為概念示意，並非實際量測的比例</div>'
            f'<div class="row" style="gap:22px;margin-top:auto">{pc}</div></div>')


# ---------------- 第 25 頁
@slide(25, "iterations", "六、開發的時間成本", "反覆修改", "畫面要反覆修改才接近需要的樣子，需求也要看到畫面才能確定")
def s25():
    st = [(1, "加上截離群"), (2, "預設改為關閉"), (4, "加上滑桿"), (5, "上限改為 5"), (8, "改名為標準差"), (10, "調整位置"), (22, "改為三個按鈕")]
    X0, X1, Y = 40, 1420, 190
    px = lambda m: X0 + (m - 1) / 21 * (X1 - X0)
    n = len(st)
    W = 1460
    cw = 192
    cx = lambda i: cw / 2 + i * (W - cw) / (n - 1)
    links = ""
    cards = ""
    for i, (m, t) in enumerate(st):
        last = i == n - 1
        c = ACCENT_D if last else MUTED
        links += f'<path d="M{cx(i):.0f} 118 C {cx(i):.0f} 150, {px(m):.0f} 150, {px(m):.0f} {Y - 8}" fill="none" stroke="{c}" stroke-width="2"/>'
        links += f'<circle cx="{px(m):.0f}" cy="{Y}" r="9" fill="{ACCENT if last else INK}"/>'
        cards += (f'<div class="card abs {"a" if last else ""}" style="left:{cx(i) - cw / 2:.0f}px;top:0;width:{cw}px;height:118px;padding:10px 12px;text-align:center">'
                  f'<div style="font-size:20px;color:{MUTED}">第 {i + 1} 次</div><div style="font-size:23px;font-weight:600;line-height:1.3;margin-top:4px">{t}</div></div>')
    axis = (f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="{MUTED}" stroke-width="3"/>'
            + "".join(f'<text x="{px(m):.0f}" y="{Y + 36}" text-anchor="middle" font-size="20" fill="{MUTED}">{m - 1} 分</text>' for m in (1, 8, 15, 22)))
    tl = f'<div style="position:relative;height:240px">{cards}<svg class="abs" style="left:0;top:0" width="{W}" height="240" font-family="inherit">{links}{axis}</svg></div>'
    slider = (f'<div style="position:relative;height:10px;background:{LINE};border-radius:5px;width:250px"><div style="position:absolute;left:150px;top:-9px;width:28px;height:28px;border-radius:50%;background:{BLUE}"></div></div>')
    btns = "".join(f'<span style="padding:9px 22px;border-radius:9px;font-size:26px;{"background:" + ACCENT_D + ";color:#fff;font-weight:600" if i == 2 else "border:1.5px solid " + LINE}">{t}</span>' for i, t in enumerate(["1σ", "2σ", "3σ"]))
    return (f'<div class="col" style="height:100%;gap:16px"><div class="row" style="gap:14px">{ic("sliders", 32, INK)}<span class="t">標準差截斷</span><span class="tag a">21 分鐘內修改 7 次</span></div>{tl}'
            f'<div class="row" style="gap:22px;flex:1;align-items:stretch">'
            f'<div class="card row" style="flex:1.25;gap:18px;justify-content:center"><div class="col" style="gap:20px;align-items:center"><div class="note">開始：滑桿 1～10</div>{slider}</div>{arrow(60, ACCENT_D)}<div class="col" style="gap:12px;align-items:center"><div class="note">最後：三個按鈕</div><div class="row" style="gap:8px">{btns}</div></div></div>'
            f'<div class="card b row" style="flex:1;gap:18px">{badge("wave", "b", 36)}<div><div class="t" style="font-size:26px">波形獨立視窗：10 分鐘內修改 6 次</div><div class="s" style="color:{INK}">功能完成後，實際操作才發現點選沒有反應、畫布大小不正確</div></div></div>'
            f'</div></div>')


# ---------------- 第 27 頁
@slide(27, "software-org", "六、開發的時間成本", "軟體與組織", "軟體反映組織的流程，兩者會一起演化")
def s27():
    # 現行：主結構加上修補的模組
    blocks = "".join(f'<rect x="{10 + i * 88}" y="60" width="78" height="58" rx="8" fill="{BLUE_BG}" stroke="{BLUE}" stroke-width="2"/>' for i in range(4))
    patches = "".join(f'<rect x="{x}" y="{y}" width="46" height="36" rx="6" fill="{ACCENT_BG}" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="5 4"/>' for x, y in [(30, 14), (150, 14), (110, 132), (232, 132), (304, 14)])
    a = f'<svg width="440" height="250" viewBox="0 0 370 180" style="max-width:100%">{blocks}{patches}</svg>'
    # 新系統：設計與實際運作之間的摩擦與迭代
    b = (f'<svg width="440" height="250" viewBox="0 0 370 180" style="max-width:100%" fill="none" stroke-linecap="round" font-family="inherit">'
         f'<rect x="20" y="58" width="130" height="64" rx="10" fill="{BLUE_BG}" stroke="{BLUE}" stroke-width="2"/><text x="85" y="97" text-anchor="middle" font-size="22" fill="{BLUE_D}" stroke="none">新的設計</text>'
         f'<rect x="220" y="58" width="130" height="64" rx="10" fill="#fff" stroke="{MUTED}" stroke-width="2"/><text x="285" y="97" text-anchor="middle" font-size="22" fill="{INK}" stroke="none">實際運作</text>'
         f'<path d="M85 50 C 110 4, 260 4, 285 50" stroke="{ACCENT_D}" stroke-width="3"/><path d="m272 42 13 9 3-15" stroke="{ACCENT_D}" stroke-width="3"/>'
         f'<path d="M285 130 C 260 176, 110 176, 85 130" stroke="{ACCENT_D}" stroke-width="3"/><path d="m98 138-13-9-3 15" stroke="{ACCENT_D}" stroke-width="3"/>'
         f'<path d="M172 76l10 10-10 10 10 10M198 76l-10 10 10 10-10 10" stroke="{ACCENT_D}" stroke-width="2.5"/></svg>')
    c = (f'<div class="col" style="gap:26px;width:100%;height:250px;justify-content:center">'
         f'<div class="row" style="gap:16px">{badge("user", "a", 34)}<div><div style="font-weight:700;font-size:26px">分工</div><div class="s" style="font-size:22px">一個人一個時間段，從頭處理到尾</div></div></div>'
         f'<div class="row" style="gap:16px">{badge("drive", "b", 34)}<div><div style="font-weight:700;font-size:26px">基礎設施</div><div class="s" style="font-size:22px">頻繁讀取連續波形檔，存放方式要重新調整</div></div></div></div>')
    def col(title, tag, vis, txt):
        return (f'<div class="card col" style="flex:1;gap:8px;align-items:center;padding:20px 18px"><span class="tag {tag}">{title}</span>{vis}<div style="font-size:25px;line-height:1.45;margin-top:auto">{txt}</div></div>')
    return (f'<div class="col" style="height:100%;gap:14px"><div class="row" style="gap:20px;flex:1;align-items:stretch">'
            + col("現行系統", "b", a, "組織的結構已與當初設計軟體時不同，因此陸續補上許多新的模組，這些修補反映出實際運作的樣子。")
            + col("新系統", "a", b, "一開始的設計，實際使用時可能與原本的運作方式產生摩擦，要經由迭代才能符合實際情況。")
            + col("周邊調整", "", c, "導入新系統時，組織與基礎設施都可能跟著改變。")
            + f'</div><div class="note row" style="gap:8px">{ic("building", 24, MUTED)}這個觀察稱為康威定律（Conway\'s Law，Melvin Conway 1968）</div></div>')


# ---------------- 第 29 頁
@slide(29, "span", "下一步與結語", "跨越的範圍", "一個人能跨越的範圍變大，軟體的邊界因此可以改變")
def s29():
    tasks = [("scissors", "切事件"), ("wave", "挑波"), ("pin", "定位"), ("shield", "QC")]
    def head(i, t):
        return f'<div class="col" style="flex:1;align-items:center;gap:4px">{ic(i, 42, INK)}<span style="font-size:26px;font-weight:600">{t}</span></div>'
    heads = "".join(head(i, t) for i, t in tasks)
    bef = "".join(f'<div class="col" style="flex:1;align-items:center;gap:8px"><div class="card b" style="padding:24px 0;width:92%;text-align:center;font-size:25px">獨立的程式</div>{ic("user", 46, BLUE_D)}</div>' for _ in tasks)
    aft = (f'<div class="card a" style="padding:30px 0;text-align:center;font-size:30px;font-weight:700;color:{ACCENT_D}">合併成一個系統：資料庫、定位、畫面與規則</div>'
           f'<div class="row" style="justify-content:center;gap:14px;margin-top:12px">{ic("user", 46, ACCENT_D)}<span style="font-size:28px;font-weight:600">一個懂領域的人</span><span style="font-size:30px;color:{MUTED}">＋</span>{ic("bot", 46, ACCENT_D)}<span style="font-size:28px;font-weight:600">Agent</span></div>')
    def rowx(t, c, inner):
        return f'<div class="row" style="gap:18px;align-items:flex-start"><div class="t" style="width:90px;color:{c};padding-top:12px">{t}</div><div style="flex:1">{inner}</div></div>'
    return (f'<div class="col" style="height:100%;gap:18px">'
            + f'<div class="row" style="gap:18px"><div style="width:90px"></div><div class="row" style="flex:1">{heads}</div></div>'
            + rowx("過去", BLUE_D, f'<div class="row">{bef}</div>')
            + rowx("現在", ACCENT_D, aft)
            + f'<div class="row" style="gap:20px;margin-top:auto"><div class="note" style="flex:1">過去的邊界與當時分工的關聯為推測，尚未查證當時的紀錄</div>'
              f'<div class="card row" style="flex:1.4;gap:16px;padding:12px 20px">{ic("warn", 34, ACCENT_D)}<div style="font-size:24px"><b>代價：</b>系統集中依賴少數人，離開之後由誰接手值得討論</div></div></div></div>')


# ---------------- 第 31 頁
@slide(31, "delivery", "下一步與結語", "新的交付模式", "小幅修改由業務單位透過 Agent 完成，大的功能由開發者處理，這是一種可能的交付模式")
def s31():
    bar = (f'<div class="row" style="height:130px;border-radius:14px;overflow:hidden;font-weight:700;font-size:28px">'
           f'<div class="row" style="flex:4;height:100%;background:{ACCENT_BG};color:{ACCENT_D};justify-content:center;gap:12px">{ic("bot", 36, ACCENT_D)}業務單位透過設計好的 Agent 流程</div>'
           f'<div class="row" style="flex:2;height:100%;background:linear-gradient(90deg,{ACCENT_BG},{BLUE_BG});color:{INK};justify-content:center;font-size:25px;font-weight:600">兩者皆可，自行選擇</div>'
           f'<div class="row" style="flex:4;height:100%;background:{BLUE_BG};color:{BLUE_D};justify-content:center;gap:12px">{ic("users", 36, BLUE_D)}開發者</div></div>')
    ticks = (f'<div class="row" style="justify-content:space-between;margin-top:14px;font-size:25px"><span>緊急而不大的問題</span><span style="color:{MUTED}">想請開發者修改時，仍然可以找開發者</span><span>大的功能與重新設計</span></div>')
    why = (f'<div class="row" style="gap:18px;flex:1;align-items:stretch">'
           f'<div class="card row" style="flex:1;gap:16px">{badge("clock", "a", 44)}<div><div class="t">出發點</div><div class="s">請開發者來修常要等上好幾天，緊急又不大的問題，自己修會更快</div></div></div>'
           f'<div class="card row" style="flex:1;gap:16px">{badge("building", "b", 44)}<div><div class="t">概念</div><div class="s">接近駐點工程師，多一個選擇，並不取代開發者</div></div></div></div>')
    pre = [("target", "明確的修改範圍"), ("check", "測試基準"), ("file", "設計紀錄")]
    prec = "".join(f'<div class="row" style="gap:10px">{ic(i, 30, GOOD)}<span style="font-size:24px;font-weight:600">{t}</span></div>' for i, t in pre)
    return (f'<div class="col" style="height:100%;gap:20px"><div><div class="note" style="margin-bottom:8px">修改的規模：小 → 大</div>{bar}{ticks}</div>{why}'
            f'<div class="card row" style="justify-content:center;gap:40px;padding:14px 22px"><span style="font-size:23px;color:{MUTED}">判斷改動是否安全的前提</span>{prec}</div></div>')


# ---------------- 共用：波形與畫面示意
def wave(w, h, seed=1, onset=.35, amp=.9, noise=.05, color=INK, sw=1.4, flat=False, gap=None):
    """合成的示意波形，不是實際資料。"""
    rnd = random.Random(seed)
    n = int(w / 2)
    mid = h / 2
    d = []
    for i in range(n):
        x = i * w / n
        t = i / n
        if flat:
            y = mid + rnd.uniform(-.4, .4)
        else:
            e = noise
            if t > onset:
                dt = (t - onset) * 14
                e = noise + amp * min(1, dt * 3) * math.exp(-dt * .55)
            y = mid + rnd.uniform(-1, 1) * e * h / 2
        if gap and gap[0] <= t <= gap[1]:
            d.append(f"M{x:.1f},{mid:.1f}" if False else "")
            continue
        d.append(f"{'M' if not d or d[-1] == '' else 'L'}{x:.1f},{y:.1f}")
    path = " ".join(p for p in d if p)
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="{path}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/></svg>'


def tw_outline():
    m = json.loads((HERE / "w8-12-map.json").read_text())
    return m["same"].split("/>")[0] + "/>", m["w"], m["h"]


def tw_map(w, h, extra=""):
    p, mw, mh = tw_outline()
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {mw} {mh}">{p}{extra}</svg>'


def window(title, inner, icon="wave", style=""):
    """仿應用程式的面板。"""
    return (f'<div style="background:#fff;border:1.5px solid {LINE};border-radius:14px;overflow:hidden;{style}">'
            f'<div class="row" style="gap:10px;background:{BG};padding:8px 16px;font-size:21px;font-weight:600;border-bottom:1.5px solid {LINE}">{ic(icon, 24, MUTED)}{title}</div>{inner}</div>')


def trace(label, w, seed, pick=None, tagtxt="", hot=False, h=58, **kw):
    bar = (f'<div class="abs" style="left:{pick * w:.0f}px;top:0;bottom:0;width:3px;background:{ACCENT_D}"></div>' if pick else "")
    tag = f'<span class="tag a abs" style="right:6px;top:8px;background:#fff;border:1.5px solid {ACCENT}">{tagtxt}</span>' if tagtxt else ""
    bg = f"background:{ACCENT_BG};" if hot else ""
    return (f'<div class="row" style="gap:10px;padding:2px 14px;{bg}"><span style="width:92px;font-size:21px;color:{MUTED}">{label}</span>'
            f'<div style="position:relative;width:{w}px;height:{h}px">{wave(w, h, seed, **kw)}{bar}{tag}</div></div>')


NOTE_MOCK = "畫面為示意，波形與站名皆為虛構"


# ---------------- 實際畫面（僅投影片使用，文稿的圖仍用示意畫面）
USE_SHOTS = True
SHOTS = HERE.parents[1] / "week8-shots"
MASKED = "開發中的系統畫面，測站代碼與名稱已替換"


def shot_img(name, w, h=None, pos="top"):
    st = f"width:{w}px;" + (f"height:{h}px;object-fit:cover;object-position:{pos};" if h else "")
    return f'<img src="{(SHOTS / name).as_uri()}" style="{st}display:block;border-radius:10px;border:1.5px solid {LINE}">'


def marker(n, x, y):
    return (f'<span class="abs row" style="left:{x}%;top:{y}%;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;background:{ACCENT_D};color:#fff;'
            f'font-size:25px;font-weight:700;justify-content:center;border:3px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.35)">{n}</span>')


def shot_page(name, marks, notes, foot=""):
    """左邊大張截圖加編號，右邊說明。"""
    W = 1040
    ms = "".join(marker(i + 1, x, y) for i, (x, y) in enumerate(marks))
    ns = "".join(f'<div class="row" style="gap:12px;align-items:flex-start"><span class="row" style="width:38px;height:38px;border-radius:50%;background:{ACCENT_D};color:#fff;font-size:22px;font-weight:700;justify-content:center;flex:none">{i + 1}</span>'
                 f'<div><div style="font-size:25px;font-weight:700;line-height:1.3">{t}</div><div style="font-size:22px;color:{MUTED};line-height:1.4">{d}</div></div></div>' for i, (t, d) in enumerate(notes))
    f = f'<div class="card b" style="margin-top:auto;padding:12px 16px;font-size:22px;line-height:1.4">{foot}</div>' if foot else ""
    return (f'<div class="row" style="gap:22px;height:100%;align-items:flex-start"><div class="col" style="gap:6px"><div style="position:relative;width:{W}px">{shot_img(name, W)}{ms}</div><div class="note">{MASKED}</div></div>'
            f'<div class="col" style="flex:1;gap:18px;height:100%">{ns}{f}</div></div>')


def real5():
    return shot_page("pick-task.png", [(96, 65.5), (12, 28), (82, 6)],
                     [("任務列表", "放在挑波畫面旁邊，挑波當下就看得到還差哪件事"), ("依距離排列", "尚未挑選的測站直接標出"), ("定位品質的指示條", "顯示站數、相位、GAP 等與標準的距離")],
                     "現行流程要挑完、定完、執行檢查程式之後才知道問題，再回到挑波程式修改")


def real6():
    return shot_page("pick-near-jump.png", [(14, 19), (45, 78)],
                     [("最近的站沒有挑選", "距離最近的測站標為未挑選"), ("從波形判斷原因", "這一站看不出明顯的起跳，在挑波時就看得出來")],
                     "這項資訊可以記錄下來，QC 因此能區分遺漏與資料本來如此。測站品質篩選依平直、缺漏、雜訊判斷，標準無法達到時至少有個根據")


def real10():
    items = [("home.png", "首頁", "以專案為中心"), ("cut.png", "切地震", "對應切事件程式"), ("pick-task.png", "定地震", "對應挑波與定位程式"), ("overview.png", "事件總覽與 QC", "對應檢查程式")]
    g = "".join(f'<div class="col" style="gap:4px">{shot_img(n, 472)}<div class="row" style="gap:10px"><b style="font-size:24px">{t}</b><span style="font-size:21px;color:{MUTED}">{d}</span></div></div>' for n, t, d in items)
    side = (f'<div class="col" style="flex:1;gap:14px;height:100%"><div class="card row" style="gap:14px">{badge("db", "a", 34)}<div><div style="font-size:25px;font-weight:700">以資料庫串接</div><div style="font-size:22px;color:{MUTED}">新增模組時接上同一個資料庫</div></div></div>'
            f'<div class="card row" style="gap:14px">{badge("wave", "b", 34)}<div><div style="font-size:25px;font-weight:700">獨立的頁面</div><div style="font-size:22px;color:{MUTED}">單螢幕時為分頁，多螢幕時各放一個螢幕</div></div></div>'
            f'<div class="card b row" style="gap:14px">{ic("flask", 34, BLUE_D)}<div><div style="font-size:25px;font-weight:700">試做比討論更快</div><div style="font-size:22px">原本以為需要獨立的波形目錄，試做之後改為切地震的時間軸</div></div></div><div class="note">{MASKED}</div></div>')
    return f'<div class="row" style="gap:20px;height:100%;align-items:flex-start"><div style="display:grid;grid-template-columns:472px 472px;gap:12px 14px">{g}</div>{side}</div>'


def real13():
    def col(n, t, d):
        return f'<div class="col" style="gap:6px"><div class="row" style="gap:10px"><b style="font-size:26px">{t}</b><span style="font-size:22px;color:{MUTED}">{d}</span></div>{shot_img(n, 720, 480)}</div>'
    stage = [("flask", "實驗性功能"), ("user", "使用者逐項打開"), ("ok", "併入一般功能")]
    st = arrow(40, ACCENT_D).join(f'<div class="row" style="gap:10px;font-size:25px;font-weight:600">{ic(i, 32, ACCENT_D)}{t}</div>' for i, t in stage)
    return (f'<div class="col" style="gap:14px;height:100%"><div class="row" style="gap:20px;align-items:flex-start">{col("settings-exp-c.png", "實驗性功能", "共 14 項，各設開關，預設關閉")}{col("settings-op-c.png", "自訂操作", "新想法作為選項，工作趕時間時不受阻礙")}</div>'
            f'<div class="card a row" style="justify-content:center;gap:22px;padding:12px">{st}</div></div>')


def real15():
    return shot_page("pick-hover.png", [(87, 21), (92, 92), (24, 25)],
                     [("懸停", "滑鼠移到測站的格子，地圖的資訊欄即顯示這一站的殘差"), ("點選", "在地圖或格子上點選測站，波形跟著切換"), ("修改挑選", "新增、刪除或修改到時與權重，隨即重新定位")],
                     "拖曳波形上的到時線時，地圖上由 S−P 換算的距離圓即時更新")


def real19():
    return shot_page("pick-near-jump.png", [(96, 65.5), (45, 78), (14, 19)],
                     [("任務列出近站", "標明距離，並可以直接前往"), ("自動跳到目標測站", "單站顯示這一站的波形，直接判斷要挑選或記錄為沒有訊號"), ("依距離排列同步", "目標測站在列表中標出")],
                     "過去看到近站沒有挑選的提示之後，要自行尋找近站是哪幾站")


# ---------------- 第 1 頁
@slide(1, "cover", "", "", "")
def s1():
    w = wave(1600, 300, 8, onset=.3, amp=1, noise=.03, color=ACCENT, sw=1.6)
    items = [("scissors", "切事件"), ("wave", "挑波"), ("pin", "定位"), ("shield", "QC")]
    chain = arrow(44).join(f'<div class="row" style="gap:10px;font-size:28px;font-weight:600">{ic(i, 36, ACCENT_D)}{t}</div>' for i, t in items)
    return (f'<div class="abs" style="left:-70px;top:330px;opacity:.55">{w}</div>'
            f'<div class="abs" style="left:0;top:-30px"><div style="font-size:26px;color:{ACCENT_D};font-weight:600">第八週｜Agent 時代的知識工作</div>'
            f'<div style="font-size:84px;font-weight:700;line-height:1.25;margin-top:14px">定位工作的翻新設計</div>'
            f'<div style="font-size:32px;color:{MUTED};margin-top:12px">切事件、挑波與檢查合併為一個系統的設計方向</div></div>'
            f'<div class="abs row" style="left:0;bottom:30px;gap:18px">{chain}</div>')


# ---------------- 第 2 頁
@slide(2, "route", "開場", "本週路線", "系統仍在開發，本週說明設計方向，細節用來佐證方向可行")
def s2():
    items = [("一", "合併的理由", "從流程上解決 QC 的問題", "shield", 0), ("二", "資料與介面", "資料存於專案資料庫，只在邊界轉換格式", "db", 1),
             ("三", "畫面", "模組化、逐步導入、即時回饋、任務引導", "tasks", 1), ("四", "接上現行流程", "每一段都能單獨接上，分階段替換", "refresh", 0),
             ("五", "新的處理想法", "處理更標準、步驟更少", "bulb", 0), ("六", "開發的時間成本", "設計的迭代仍然需要大量時間", "clock", 0)]
    cards = ""
    for n, t, d, i, hot in items:
        tag = '<span class="tag a" style="background:#fff;margin-left:10px;vertical-align:3px">本週重點</span>' if hot else ""
        cards += (f'<div class="card {"a" if hot else ""} row" style="gap:20px;padding:22px 24px">{badge(i, "a" if not hot else "", 42) if not hot else f"<span class=badge style=width:68px;height:68px;background:#fff>{ic(i, 42, ACCENT_D)}</span>"}'
                  f'<div><div class="t">{n}、{t}{tag}</div><div class="s" style="{"color:" + INK if hot else ""}">{d}</div></div></div>')
    return (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:510px;grid-auto-rows:1fr">{cards}</div>'
            f'<div class="row" style="gap:12px;margin-top:26px;font-size:25px;color:{MUTED}">{ic("flask", 30, MUTED)}部分功能尚未完成，自動挑波只在下一步略提</div>')


# ---------------- 第 3 頁
@slide(3, "flow-before", "一、合併的理由", "現行流程", "可以用流程方法解決 QC 遇到的問題，減少後面真正需要 QC 的項目")
def s3():
    def f(t, i, x, y):
        return f'<div class="card abs row" style="left:{x}px;top:{y}px;width:230px;height:84px;gap:10px;padding:8px 14px;background:{BG}">{ic(i, 30, MUTED)}<span style="font-size:24px;font-weight:600">{t}</span></div>'
    def p(t, i, x, y):
        return f'<div class="card b abs row" style="left:{x}px;top:{y}px;width:230px;height:84px;gap:10px;padding:8px 14px">{ic(i, 30, BLUE_D)}<span style="font-size:24px;font-weight:700">{t}</span></div>'
    A = 'marker-end="url(#a)"'
    svg = (f'<svg class="abs" style="left:0;top:0" width="880" height="500" fill="none" stroke="{MUTED}" stroke-width="2.5">'
           f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker>'
           f'<marker id="b" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{ACCENT_D}"/></marker></defs>'
           f'<path d="M230 42H292" {A}/><path d="M530 42H592" {A}/>'
           f'<path d="M710 84V186" {A}/>'
           f'<path d="M592 215H530" {A}/><path d="M530 240H592" {A}/>'
           f'<path d="M710 270V372" {A}/><path d="M592 414H530" {A}/><path d="M300 414H238" {A}/>'
           f'<path d="M825 414H860V42H825" stroke="{ACCENT_D}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#b)"/></svg>')
    nodes = (f("連續波形檔", "wave", 0, 0) + p("切事件程式", "scissors", 300, 0) + f("事件波形檔", "file", 600, 0)
             .replace("left:600px", "left:600px") )
    # 排成三列：上列往右，右側往下，下列往左；挑波程式與相位檔放在右欄
    nodes = (f("連續波形檔", "wave", 0, 0) + p("切事件程式", "scissors", 300, 0) + p("挑波程式", "cross", 600, 0)
             + p("定位程式", "pin", 300, 186) + f("相位檔", "file", 600, 186)
             + f("地震目錄", "db", 8, 372) + p("入庫程式", "box", 308, 372) + p("QC 預檢", "shield", 600, 372))
    back = f'<div class="abs" style="left:480px;top:92px;width:170px;text-align:center;font-size:21px;color:{MUTED}">事件波形檔</div>'
    tip = (f'<div class="abs tag a" style="left:0;top:210px;font-size:22px;padding:8px 14px;line-height:1.35;border-radius:14px;width:270px">'
           f'退件時回到挑波程式，<br>修改之後重新定位</div>')
    methods = [("ok", "消除格式類的錯誤", "輸出時才排序並產生檔名"), ("tasks", "挑波時即時輔助", "不必在兩支程式之間往返"), ("file", "留下 QC 判斷的依據", "記錄沒有資料或訊號不佳"), ("shield", "規則仍只有一份", "各模組直接引用")]
    cards = "".join(f'<div class="card a row" style="gap:16px;flex:1;padding:12px 18px">{ic(i, 38, ACCENT_D)}<div><div style="font-size:25px;font-weight:700">{t}</div><div class="s" style="color:{INK};font-size:22px">{d}</div></div></div>' for i, t, d in methods)
    return (f'<div class="row" style="gap:40px;height:100%;align-items:stretch"><div style="position:relative;width:880px;top:40px">{svg}{nodes}{back}{tip}</div>'
            f'<div class="col" style="flex:1;gap:14px"><div class="t">合併之後的做法</div>{cards}</div></div>')


# ---------------- 第 5 頁
@slide(5, "assist", "一、合併的理由", "挑波時的輔助", "任務列表在挑波當下提示，不必在兩支程式之間往返")
def s5():
    if USE_SHOTS:
        return real5()
    w = 610
    tr = (trace("測站 A", w, 3, .22, h=80, onset=.22) + trace("測站 B", w, 4, .32, h=80, onset=.32, amp=.8) + trace("測站 C", w, 5, None, h=80, onset=.4, amp=.7, tagtxt="尚未挑選", hot=True)
          + trace("測站 D", w, 6, .5, h=80, onset=.5, amp=.6) + trace("測站 E", w, 7, .6, h=80, onset=.6, amp=.5))
    quests = [("ok", GOOD, "挑選足夠的測站"), ("ok", GOOD, "定出震央"), ("cross", ACCENT_D, "確保震央穩定"), ("circle", LINE, "量測規模")]
    q = "".join(f'<div class="row" style="gap:12px;padding:24px 16px;{"background:" + ACCENT_BG + ";font-weight:700" if c == ACCENT_D else ""};font-size:27px">{ic(i, 32, c, 2.2)}{t}</div>' for i, c, t in quests)
    old = [("wave", "挑波"), ("pin", "定位"), ("shield", "執行檢查程式"), ("warn", "發現問題"), ("refresh", "回到挑波")]
    oldr = arrow(30).join(f'<div class="row" style="gap:8px;font-size:23px">{ic(i, 28, BLUE_D)}{t}</div>' for i, t in old)
    return (f'<div class="col" style="gap:16px;height:100%"><div class="row" style="gap:18px;align-items:flex-start">'
            + window("挑波畫面", f'<div style="padding:10px 0">{tr}</div>')
            + window("任務列表", f'<div style="padding:8px 4px">{q}</div>', "tasks", "flex:1;border:2px solid " + ACCENT)
            + f'</div><div class="card b row" style="gap:20px;padding:14px 22px;margin-top:auto"><span class="tag b" style="background:#fff">現行</span>{oldr}</div>'
            f'<div class="note">{NOTE_MOCK}</div></div>')


# ---------------- 第 6 頁
@slide(6, "qc-basis", "一、合併的理由", "QC 的依據", "挑波時看到的資訊可以記錄下來，成為 QC 判斷的依據")
def s6():
    if USE_SHOTS:
        return real6()
    w = 560
    tr = (trace("最近的站", w, 2, None, h=112, flat=True, hot=True, tagtxt="沒有訊號") + trace("第 2 近", w, 3, .3, h=112, onset=.3) + trace("第 3 近", w, 4, .38, h=112, onset=.38, amp=.8) + trace("第 4 近", w, 5, .46, h=112, onset=.46, amp=.6))
    flow = [("eye", "挑波時從波形看得出"), ("pencil", "標記為沒有訊號並記錄"), ("shield", "QC 可以區分遺漏與資料本來如此")]
    fl = "".join(f'<div class="row" style="gap:14px;padding:12px 0">{badge(i, "a", 30)}<span style="font-size:26px">{t}</span></div>' for i, t in flow)
    q = [("平直", wave(190, 90, 11, flat=True, color=BLUE_D)), ("缺漏", wave(190, 90, 12, onset=0, amp=0, noise=.5, color=BLUE_D, gap=(.35, .7))), ("雜訊", wave(190, 90, 13, onset=0, amp=0, noise=1, color=BLUE_D))]
    qc = "".join(f'<div class="col" style="align-items:center;gap:4px;flex:1">{v}<span style="font-size:23px;font-weight:600">{t}</span></div>' for t, v in q)
    return (f'<div class="row" style="gap:24px;height:100%;align-items:flex-start"><div class="col" style="gap:8px">'
            + window("依距離排列", f'<div style="padding:10px 0">{tr}</div>')
            + f'<div class="note">{NOTE_MOCK}</div></div>'
            f'<div class="col" style="flex:1;gap:16px">{"<div class=card style=padding:12px&#32;22px>" + fl + "</div>"}'
            f'<div class="card b"><div class="row" style="gap:10px">{ic("search", 28, BLUE_D)}<span class="t" style="font-size:26px">測站品質篩選</span></div>'
            f'<div class="row" style="margin:10px 0">{qc}</div><div class="s" style="color:{INK};font-size:23px">標準無法達到時，至少有個根據</div></div></div></div>')


# ---------------- 第 8 頁
@slide(8, "boundary", "二、資料與介面", "只在邊界轉換", "資料都存於專案資料庫，只在對接外部時轉換格式")
def s8():
    mods = [("scissors", "切地震"), ("cross", "定地震"), ("shield", "QC"), ("db", "資料管理")]
    m = "".join(f'<div class="card b row" style="flex:1;gap:10px;justify-content:center;padding:14px 8px">{ic(i, 30, BLUE_D)}<span style="font-size:25px;font-weight:700">{t}</span></div>' for i, t in mods)
    links = lambda n: f'<div class="row" style="justify-content:space-around;height:40px">' + "".join(f'<svg width="20" height="40" fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3V37M4 10l6-7 6 7M4 30l6 7 6-7"/></svg>' for _ in range(n)) + '</div>'
    db = (f'<div class="card a" style="text-align:center;padding:16px"><div class="row" style="gap:12px;justify-content:center">{ic("db", 40, ACCENT_D)}<span class="t" style="font-size:32px">專案資料庫</span></div>'
          f'<div class="s" style="color:{INK}">挑選、定位解、到時的關聯、規模、修改紀錄</div></div>')
    ad = [("wave", "波形轉接", "連續、事件波形", False), ("file", "相位檔轉接", "讀入、匯出", False), ("pin", "定位轉接", "現行的定位程式", False), ("plus", "其他格式", "更通用的格式", True), ("cross", "其他定位程式", "較新的定位程式", True)]
    a = "".join(f'<div class="card col" style="flex:1;align-items:center;padding:12px 6px;gap:2px;{"border-style:dashed;" if d else ""}">{ic(i, 30, ACCENT_D if not d else MUTED)}<div style="font-size:23px;font-weight:700">{t}</div><div style="font-size:20px;color:{MUTED}">{s}</div></div>' for i, t, s, d in ad)
    pts = [("file", "檔案格式", "對接現有系統時才輸出相位檔，做法接近向下相容。"), ("pin", "定位程式", "介面傳遞定位本身的內容，每一種定位程式各寫一個轉接。"), ("plus", "未來的擴充", "改用新格式或新程式時，只需增加一個轉接，不必重新撰寫。")]
    p = "".join(f'<div class="card row" style="flex:1;gap:16px;padding:12px 18px">{badge(i, "a", 32)}<div><div style="font-size:25px;font-weight:700">{t}</div><div class="s" style="font-size:22px">{d}</div></div></div>' for i, t, d in pts)
    return (f'<div class="row" style="gap:28px;height:100%;align-items:stretch"><div class="col" style="width:930px">'
            f'<div style="background:{BG};border:1.5px solid {LINE};border-radius:18px;padding:16px"><div class="row" style="gap:14px">{m}</div>{links(4)}{db}</div>{links(5)}<div class="row" style="gap:12px">{a}</div>'
            f'<div class="note" style="margin-top:8px">虛線為規劃中，尚未實作</div></div>'
            f'<div class="col" style="flex:1;gap:14px">{p}</div></div>')


# ---------------- 第 10 頁
@slide(10, "modules", "三、畫面", "模組化", "每個模組對應原本的一個步驟，以資料庫串接，日後容易增加新功能")
def s10():
    if USE_SHOTS:
        return real10()
    rows = [("切事件程式", "切地震", "scissors"), ("挑波與定位程式", "定地震", "cross"), ("檢查程式", "QC", "shield")]
    r = "".join(f'<div class="row" style="gap:14px;margin-bottom:14px"><div class="card b" style="width:250px;text-align:center;padding:28px 14px;font-size:24px;font-weight:600">{a}</div>{arrow(46)}<div class="card a row" style="flex:1;gap:12px;justify-content:center;padding:28px 14px;font-size:28px;font-weight:700">{ic(i, 36, ACCENT_D)}{b}</div></div>' for a, b, i in rows)
    add = f'<div class="row" style="gap:14px;margin-bottom:14px"><div style="width:250px;text-align:center;font-size:24px;color:{MUTED}">新的需求</div>{arrow(46, MUTED, True)}<div class="card row" style="flex:1;gap:12px;justify-content:center;padding:28px 14px;font-size:26px;border-style:dashed;color:{MUTED}">{ic("plus", 32, MUTED)}新的模組</div></div>'
    db = f'<div class="card row" style="gap:12px;justify-content:center;background:{INK};color:#fff;border-color:{INK};padding:22px;font-size:26px;font-weight:700;margin-left:310px">{ic("db", 32, "#fff")}以專案資料庫串接</div>'
    def scr(n, parts):
        boxes = "".join(f'<div style="width:{118 if n > 1 else 240}px;height:112px;background:#fff;border:2.5px solid {MUTED};border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:19px">{p}</div>' for p in parts)
        return f'<div class="row" style="gap:8px;justify-content:center">{boxes}</div>'
    tab = '<span style="display:flex;gap:3px">' + "".join(f'<span style="padding:0 5px;background:{ACCENT_BG if i == 0 else BG};border-radius:4px;font-size:17px">{t}</span>' for i, t in enumerate(["切", "定", "QC"])) + '</span>'
    screens = (f'<div class="card"><div class="t" style="font-size:26px;margin-bottom:10px">每個模組是獨立的頁面</div>'
               f'<div class="row" style="justify-content:space-around;gap:14px"><div class="col" style="align-items:center;gap:6px">{scr(1, [tab])}<span style="font-size:22px">單螢幕：分頁</span></div>'
               f'<div class="col" style="align-items:center;gap:6px">{scr(2, ["切地震", "定地震"])}<span style="font-size:22px">多螢幕：各放一個</span></div></div></div>')
    case = (f'<div class="card b"><div class="row" style="gap:10px">{ic("flask", 30, BLUE_D)}<span class="t" style="font-size:26px">試做比討論更快</span></div>'
            f'<div class="s" style="color:{INK};margin-top:4px">原本以為需要獨立的波形目錄，試做之後改為切地震的時間軸</div></div>')
    return (f'<div class="row" style="gap:30px;height:100%;align-items:flex-start"><div style="width:850px">{r}{add}{db}</div>'
            f'<div class="col" style="flex:1;gap:18px">{screens}{case}</div></div>')


# ---------------- 第 11 頁
@slide(11, "habit", "三、畫面", "沿用習慣", "原有的功能多半有其目的，重寫之前先向使用者請教，尚未確認的先沿用")
def s11():
    src = (f'<div class="card col" style="width:360px;align-items:center;text-align:center;gap:10px;padding:26px 18px">{badge("search", "", 44)}<div class="t">原有的功能</div>'
           f'<div class="s">目的不一定寫在程式碼或文件中</div></div>')
    ask = (f'<div class="card a col" style="width:330px;align-items:center;text-align:center;gap:10px;padding:26px 18px">{badge("users", "", 44).replace(BG, "#fff")}<div class="t">請教使用者</div>'
           f'<div class="s" style="color:{INK}">這個功能在什麼情況下使用，依賴哪些資訊</div></div>')
    res = [("ok", GOOD, "已確認目的", "保留目的，可以改善做法"), ("history", BLUE_D, "尚未確認", "先沿用，保留原本的行為")]
    rc = "".join(f'<div class="card row" style="gap:16px;flex:1">{ic(i, 44, c)}<div><div class="t" style="font-size:27px">{a}</div><div class="s">{b}</div></div></div>' for i, c, a, b in res)
    warn = (f'<div class="card b row" style="gap:18px;margin-top:30px;padding:26px">{badge("warn", "b", 36)}<div style="font-size:26px">若未沿用，使用者可能找不到原本依賴的資訊。'
            f'<span style="color:{MUTED}">下一頁是其中一個例子。</span></div></div>')
    return (f'<div class="row" style="gap:16px;align-items:stretch;height:420px">{src}<div style="align-self:center">{arrow(50)}</div>{ask}<div style="align-self:center">{arrow(50)}</div><div class="col" style="flex:1;gap:16px">{rc}</div></div>{warn}')


# ---------------- 第 13 頁
@slide(13, "gradual", "三、畫面", "逐步導入", "新功能與新操作由使用者自行選擇，逐步吸收")
def s13():
    if USE_SHOTS:
        return real13()
    def tog(on):
        c = ACCENT_D if on else LINE
        x = 26 if on else 2
        return f'<span style="position:relative;display:block;width:54px;height:30px;border-radius:15px;background:{c};flex:none"><span style="position:absolute;left:{x}px;top:2px;width:26px;height:26px;border-radius:50%;background:#fff"></span></span>'
    ex = [("任務列表", True), ("自動權重", True), ("先挑再關聯", False), ("測站品質", False)]
    li = "".join(f'<div class="row" style="justify-content:space-between;padding:19px 18px;border-top:{"none" if n == 0 else "1px solid " + LINE};font-size:25px">{t}{tog(o)}</div>' for n, (t, o) in enumerate(ex))
    li += f'<div style="padding:8px 18px;border-top:1px solid {LINE};font-size:22px;color:{MUTED}">共 14 項，各設開關，預設關閉</div>'
    op = f'<div class="row" style="justify-content:space-between;padding:20px 18px;font-size:25px">Shift＋滾輪調整振幅{tog(False)}</div>'
    stage = [("flask", "實驗性功能", "測試尚未成熟的功能"), ("user", "使用者逐項打開", "學習門檻因此降低"), ("ok", "併入一般功能", "大家接受並使用一段時間之後")]
    st = arrow(36).join(f'<div class="col" style="align-items:center;text-align:center;flex:1;gap:6px">{badge(i, "a", 40)}<div style="font-size:25px;font-weight:700">{a}</div><div class="s" style="font-size:22px">{b}</div></div>' for i, a, b in stage)
    return (f'<div class="row" style="gap:26px;height:100%;align-items:flex-start"><div class="col" style="width:520px;gap:14px">'
            + window("設定頁：實驗性功能", li, "flask")
            + window("設定頁：操作", op, "sliders")
            + f'<div class="note">{"畫面為示意"}</div></div>'
            f'<div class="col" style="flex:1;gap:18px"><div class="card a" style="padding:22px 18px"><div class="row" style="align-items:flex-start;gap:6px">{st}</div></div>'
            f'<div class="card row" style="gap:18px">{badge("bulb", "b", 38)}<div><div class="t">開發者的新想法放到設定頁作為選項</div><div class="s">開發保有創新的空間</div></div></div>'
            f'<div class="card row" style="gap:18px">{badge("clock", "b", 38)}<div><div class="t">工作趕時間時不受阻礙</div><div class="s">不推新功能給使用者，由使用者自行選擇</div></div></div></div></div>')


# ---------------- 第 15 頁
@slide(15, "linked", "三、畫面", "示範：面板連動", "滑鼠懸停、拖曳或點選時，相關的面板都立即更新")
def s15():
    if USE_SHOTS:
        return real15()
    w = 470
    tr = trace("測站 A", w, 3, .25, h=92, onset=.25) + trace("測站 B", w, 4, .35, h=92, onset=.35, amp=.8, hot=True) + trace("測站 C", w, 5, .47, h=92, onset=.47, amp=.6) + trace("測站 D", w, 6, .58, h=92, onset=.58, amp=.5)
    # 地圖上的距離圓
    extra = (f'<circle cx="155" cy="260" r="84" fill="{ACCENT_BG}" fill-opacity=".5" stroke="{ACCENT_D}" stroke-width="3" stroke-dasharray="8 6"/>'
             f'<circle cx="155" cy="260" r="7" fill="{INK}"/><path d="M155 170l10 18h-20z" fill="{ACCENT_D}" transform="translate(30 60)"/>')
    res = [("測站 A", "+0.1"), ("測站 B", "−0.4"), ("測站 C", "+0.2")]
    rt = "".join(f'<div class="row" style="justify-content:space-between;padding:18px 16px;font-size:24px;{"background:" + ACCENT_BG + ";font-weight:700" if n == 1 else ""}"><span>{a}</span><span>{b} 秒</span></div>' for n, (a, b) in enumerate(res))
    ops = [("pencil", "修改挑選", "重新定位，地圖與殘差更新"), ("eye", "懸停", "地圖的資訊欄顯示這一站的殘差"), ("move", "拖曳到時線", "S−P 距離圓即時更新"), ("cursor", "點選地圖", "波形列表跳到這一站的分頁")]
    oc = "".join(f'<div class="row" style="gap:14px;flex:1">{badge(i, "a", 28)}<div><div style="font-size:24px;font-weight:700">{a}</div><div style="font-size:21px;color:{MUTED}">{b}</div></div></div>' for i, a, b in ops)
    return (f'<div class="col" style="gap:14px;height:100%"><div class="row" style="gap:16px;align-items:stretch">'
            + window("波形", f'<div style="padding:8px 0">{tr}</div>')
            + window("地圖", f'<div class="row" style="justify-content:center;padding:4px">{tw_map(250, 364, extra)}</div>', "pin", "width:300px")
            + window("殘差", f'<div style="padding:8px 0">{rt}</div><div class="row" style="gap:8px;justify-content:center;padding:14px;font-size:21px;color:{ACCENT_D}">{ic("refresh", 24, ACCENT_D)}每次修改後更新</div>', "chart", "flex:1")
            + f'</div><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-top:auto">{oc}</div><div class="note">{NOTE_MOCK}，課堂上實際操作</div></div>')


# ---------------- 第 16 頁
@slide(16, "quest-line", "三、畫面", "任務列表", "業務單位希望有一個在旁邊協助檢查 QC 的程式，這個形式接近遊戲的任務列表")
def s16():
    main = ["確認窗內的地震", "挑選足夠的測站", "定出震央", "確保震央穩定", "檢查離群的到時", "量測規模"]
    n = len(main)
    nodes = ""
    for i, t in enumerate(main):
        done = i < 3
        cur = i == 3
        c = GOOD if done else (ACCENT_D if cur else MUTED)
        ico = ic("ok" if done else ("cross" if cur else "circle"), 44, c, 2)
        nodes += f'<div class="col" style="flex:1;align-items:center;gap:8px;text-align:center;z-index:1"><span style="background:#FCFBF8;padding:0 6px">{ico}</span><div style="font-size:24px;font-weight:{700 if cur else 500};color:{INK if i <= 3 else MUTED};line-height:1.25;padding:0 6px">{t}</div></div>'
    flag = f'<div class="col" style="width:150px;align-items:center;gap:8px;text-align:center;z-index:1"><span style="background:#FCFBF8;padding:0 6px">{ic("flag", 44, ACCENT_D, 2)}</span><div style="font-size:24px;font-weight:700;color:{ACCENT_D};line-height:1.25">可以交付的地震</div></div>'
    line = (f'<div class="t" style="margin-bottom:12px"><span class="tag a" style="margin-right:10px">主線</span>定出一個可以交付的地震，依挑波的進度逐步出現下一個目標</div>'
            f'<div style="position:relative"><div class="abs" style="left:90px;right:70px;top:22px;height:4px;background:{LINE}"></div><div class="row" style="align-items:flex-start">{nodes}{flag}</div></div>')
    side = ["是否為遠震", "是否為西部深震", "檢查深度", "檢查規模"]
    sc = "".join(f'<div class="card row" style="flex:1;gap:10px;justify-content:center;border-style:dashed;padding:14px 8px;font-size:24px">{ic("search", 28, BLUE_D)}{t}</div>' for t in side)
    origin = (f'<div class="card a row" style="gap:18px;margin-top:auto">{badge("bot", "", 38).replace(BG, "#fff")}<div style="font-size:25px">在旁邊協助，只呈現這個地震還差哪幾件事。<span style="color:{MUTED}">兩個設計方向都尚待同仁實際試用確認。</span></div></div>')
    if USE_SHOTS:
        origin = f'<div class="row" style="gap:18px;margin-top:auto;align-items:flex-end">{shot_img("task-panel.png", 330)}{origin}</div>'
    return (f'<div class="col" style="gap:18px;height:100%">{line}<div><div class="t" style="margin-bottom:12px"><span class="tag b" style="margin-right:10px">支線</span>遇到特殊情況才出現</div><div class="row" style="gap:14px">{sc}</div></div>{origin}</div>')


# ---------------- 第 18 頁
@slide(18, "assistant", "三、畫面", "主動提供資訊", "程式依目前的進度調整介面，主動提供這個階段需要的資訊")
def s18():
    def zoomed(cx, cy, r, title, sub, icon):
        ps = [(150, 150), (185, 130), (120, 190), (205, 200), (100, 120), (160, 250), (130, 300), (190, 320), (150, 380), (215, 90), (95, 240), (225, 280)]
        dots = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{ACCENT_D if (x - cx) ** 2 + (y - cy) ** 2 < r ** 2 else "#B8B0A5"}"/>' for x, y in ps)
        box = f'<rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" rx="10" fill="{ACCENT_BG}" fill-opacity=".6" stroke="{ACCENT_D}" stroke-width="3"/>'
        return (f'<div class="card col" style="flex:1;align-items:center;gap:8px;padding:16px">{tw_map(235, 342, box + dots)}'
                f'<div class="row" style="gap:12px;margin-top:4px">{badge(icon, "a", 30)}<div><div style="font-size:26px;font-weight:700">{title}</div><div class="s" style="font-size:22px">{sub}</div></div></div></div>')
    bot = (f'<div class="card a col" style="width:400px;gap:16px;justify-content:center;padding:24px">{badge("bot", "", 46).replace(BG, "#fff")}<div class="t" style="font-size:30px">使用起來像有一位助手</div>'
           f'<div style="font-size:25px;line-height:1.45">使用者想知道的通常是下一步要看什麼。程式已經掌握目前的進度，可以先準備好，不必手動切換。</div></div>')
    return (f'<div class="row" style="gap:20px;height:100%;align-items:stretch">{zoomed(155, 170, 72, "挑完第一站之後", "地圖自動放大到最近幾站", "wave")}'
            f'{zoomed(160, 310, 82, "點開某個任務時", "地圖移到那個任務的範圍", "tasks")}{bot}</div>')


# ---------------- 第 19 頁
@slide(19, "near", "三、畫面", "示範：近站任務", "規則提示近站沒有挑選時，任務列出這些近站，點選後自動跳到目標測站")
def s19():
    if USE_SHOTS:
        return real19()
    w1 = (f'<div style="padding:12px 16px"><div class="row" style="gap:10px;font-size:25px;font-weight:700">{ic("cross", 30, ACCENT_D)}確保震央穩定</div><div class="s" style="margin-top:8px;font-size:22px">近站尚未挑選</div></div>')
    li = "".join(f'<div class="row" style="justify-content:space-between;padding:20px 16px;font-size:26px;border-top:1px solid {LINE};{"background:" + ACCENT_BG + ";font-weight:700" if i == 0 else ""}"><span>測站 {s}</span><span class="row" style="gap:6px;color:{ACCENT_D}">{d} 公里{ic("cursor", 24, ACCENT_D) if i == 0 else ""}</span></div>' for i, (s, d) in enumerate([("A", 6), ("B", 11), ("C", 18)]))
    w2 = f'<div style="padding:10px 12px">{wave(600, 270, 3, onset=.35, amp=.95)}<div class="row" style="justify-content:space-between;margin-top:10px;font-size:23px"><span class="tag a">挑選到時</span><span class="tag">標為沒有訊號</span></div></div>'
    cols = (window("任務", w1 + li, "tasks", "width:610px;flex:none") + f'<div style="align-self:center">{arrow(50, ACCENT_D)}</div>'
            + window("自動跳到測站 A", w2, "wave", "flex:1"))
    before = (f'<div class="card b row" style="gap:20px;margin-top:auto">{badge("search", "b", 36)}<div style="font-size:26px"><b>過去：</b>看到近站沒有挑選的提示之後，要自行尋找近站是哪幾站</div></div>')
    return (f'<div class="col" style="gap:14px;height:100%"><div class="row" style="gap:18px;align-items:flex-start">{cols}</div>{before}<div class="note">{NOTE_MOCK}，課堂上實際操作</div></div>')


# ---------------- 第 24 頁
@slide(24, "verify", "六、開發的時間成本", "驗證的負擔", "功能做得快就會做更多功能，要測試的項目與一次要考慮的事情也隨之增加")
def s24():
    ui, other = 202, 66
    bar = (f'<div class="row" style="height:96px;gap:4px;border-radius:12px;overflow:hidden;margin-top:12px"><div class="row" style="flex:{ui};height:100%;background:{ACCENT_BG};justify-content:center;font-size:30px;font-weight:700;color:{ACCENT_D}">202 筆只改畫面</div>'
           f'<div class="row" style="flex:{other};height:100%;background:{BG};justify-content:center;font-size:24px;color:{MUTED}">其他 66 筆</div></div>')
    head = (f'<div class="card"><div class="row" style="gap:16px;align-items:baseline"><span class="big">268</span><span style="font-size:27px">筆 app 修改（10/21 至 11/01）</span><span class="note" style="margin-left:auto">筆數不等於時間，只作為參考</span></div>{bar}</div>')
    def col(icon, kind, title, items):
        li = "".join(f'<div class="row" style="gap:12px;padding:7px 0;font-size:26px">{ic("check", 28, GOOD, 2.6)}{t}</div>' for t in items)
        return f'<div class="card row" style="flex:1;gap:22px;padding:22px 26px">{badge(icon, kind, 46)}<div><div class="t">{title}</div>{li}</div></div>'
    bottom = (f'<div class="card a row" style="gap:18px;margin-top:auto">{badge("sliders", "", 36).replace(BG, "#fff")}<div style="font-size:27px;font-weight:600">因此要把每個功能拆到可以獨立開關、獨立驗證</div></div>')
    return (f'<div class="col" style="gap:18px;height:100%">{head}<div class="row" style="gap:18px;align-items:stretch">{col("bot", "b", "自動測試能處理", ["檔案格式", "計算結果"])}{col("user", "a", "只能由人實際使用來判斷", ["操作是否順手", "畫面是否合理"])}</div>{bottom}</div>')


# ---------------- 第 26 頁
@slide(26, "premise", "六、開發的時間成本", "原型的前提", "能在約兩週內做出原型，是因為有舊程式可以參考，開發者也已有研究")
def s26():
    pre = [("file", "有舊程式可以參考", "行為與格式可以直接對照"), ("bulb", "開發者已有研究", "熟悉這個主題，能夠判斷方向")]
    pc = "".join(f'<div class="card row" style="gap:18px">{badge(i, "a", 38)}<div><div class="t">{a}</div><div class="s">{b}</div></div></div>' for i, a, b in pre)
    tl = (f'<div style="position:relative;margin-top:6px"><div class="row" style="height:140px;gap:0">'
          f'<div class="row" style="width:300px;height:100%;background:{ACCENT};color:#fff;font-size:28px;font-weight:700;justify-content:center;border-radius:12px 0 0 12px">原型｜約兩週</div>'
          f'<div class="row" style="flex:1;height:100%;background:repeating-linear-gradient(90deg,{ACCENT_BG} 0 26px,#FCFBF8 26px 36px);justify-content:space-around;font-size:26px;font-weight:600;border-radius:0 12px 12px 0;padding:0 20px">'
          f'<span style="background:#FCFBF8;padding:4px 12px;border-radius:8px">細修流程上的細節</span><span style="background:#FCFBF8;padding:4px 12px;border-radius:8px">交給使用者測試</span><span style="background:#FCFBF8;padding:4px 12px;border-radius:8px">依回饋迭代</span></div></div>'
          f'<div class="note" style="margin-top:8px">後段的長度尚未確定，圖面僅為示意</div></div>')
    warn = (f'<div class="card b row" style="gap:18px;margin-top:auto">{badge("warn", "b", 36)}<div style="font-size:26px">兩週這個數字不宜直接套用到其他專案。沒有舊程式可以對照、也不熟悉主題時，光是確認要做什麼就需要更多時間。</div></div>')
    return f'<div class="col" style="gap:22px;height:100%"><div class="row" style="gap:18px"><div style="flex:1">{pc.split("</div></div></div>")[0]}</div></div></div></div><div style="flex:1">{pc.split("</div></div></div>")[1]}</div></div></div></div></div><div class="t">從原型到完整的系統</div>{tl}{warn}</div>'


# ---------------- 第 28 頁
@slide(28, "next", "下一步與結語", "下一步", "最具體的下一步，是讓一些人實際使用，並重新思考要評估的指標")
def s28():
    cards = [("users", "a", "實際試用", "讓一些人實際使用，並訂出評估指標，以便記錄成效", "最具體的下一步"),
             ("tasks", "b", "互動式教學", "選出幾個案例，以引導的方式教導操作，降低培養新人的門檻。日後也可以作為學校的教具", "沿用任務列表的形式"),
             ("bot", "b", "自動挑波", "以機器學習模型自動挑波並關聯成粗略的事件，作為切事件的參考，結果仍由人確認", "內部已有部分在進行")]
    c = "".join(f'<div class="card {"a" if k == "a" else ""} col" style="flex:1;gap:12px;padding:28px 26px">{badge(i, "b" if k == "b" else "", 50).replace(BG, "#fff") if k == "a" else badge(i, "b", 50)}<div class="t" style="font-size:32px">{t}</div><div style="font-size:25px;line-height:1.5">{d}</div><span class="tag {k}" style="margin-top:auto;align-self:flex-start;{"background:#fff" if k == "a" else ""}">{n}</span></div>' for i, k, t, d, n in cards)
    note = (f'<div class="card row" style="gap:18px;padding:14px 22px">{ic("shield", 36, GOOD)}<div style="font-size:25px">物理方法的檢查與機器學習保持獨立，例如起始分析與測站品質，日後可以用來攔截自動挑波的錯誤</div></div>')
    return f'<div class="col" style="gap:18px;height:100%"><div class="row" style="gap:18px;flex:1;align-items:stretch">{c}</div>{note}</div>'


# ---------------- 第 30 頁
@slide(30, "intent", "下一步與結語", "設計意圖的保存", "設計意圖可以低成本地保存下來")
def s30():
    old = (f'<div class="card b col" style="flex:1;gap:26px;padding:28px"><span class="tag b" style="background:#fff;align-self:flex-start">舊程式</span>'
           f'<div class="row" style="gap:16px">{ic("user", 62, BLUE_D, 1.5)}<div style="font-size:27px;font-weight:700">設計意圖多半留在使用者的記憶裡</div></div>'
           f'<div class="row" style="gap:14px;font-size:25px">{ic("search", 32, BLUE_D)}要靠訪談才問得出來</div><div class="row" style="gap:14px;font-size:25px">{ic("warn", 32, BLUE_D)}程式碼本身看不出原因</div></div>')
    doc = (f'<div style="padding:16px 20px;font-size:23px;line-height:1.7;font-family:Menlo,monospace,\'PingFang TC\';color:{MUTED}">'
           f'<div style="color:{INK};font-family:\'PingFang TC\'">任務的定義</div>'
           f'<div style="background:{ACCENT_BG};border-left:5px solid {ACCENT};padding:8px 14px;margin:8px 0;color:{INK};font-family:\'PingFang TC\'">寫法參照遊戲的任務<b style="color:{ACCENT_D}">（使用者 2026-10-26 提出：</b>任務要引導使用者完成正確的工作，而不是列出底層的規則<b style="color:{ACCENT_D}">）</b></div>'
           f'<div style="font-family:\'PingFang TC\'">一個任務代表一個要達成的結果……</div></div>')
    new = (f'<div class="col" style="flex:1.4;gap:14px"><span class="tag a" style="align-self:flex-start">翻新時</span>{window("說明文件的片段", doc, "file")}'
           f'<div class="row" style="gap:18px"><div class="big" style="color:{ACCENT_D};white-space:nowrap">約 150</div><div style="font-size:26px">處記下提出的人與理由，隨著開發一併記下，日後不必再靠訪談推測原因</div></div></div>')
    return f'<div class="row" style="gap:26px;height:100%;align-items:stretch">{old}<div style="align-self:center">{arrow(50, ACCENT_D)}</div>{new}</div>'


# ---------------- 第 32 頁
@slide(32, "discuss", "討論", "討論與交換意見", "歡迎提出自己業務中的題目，逐一討論")
def s32():
    q = [("file", "哪一個沿用多年的檔案格式已不敷使用，卻因為多支程式依賴而難以更改"), ("search", "有沒有相鄰領域的成熟做法可以參考"), ("users", "手上的工具有哪些功能的用途沒有寫下，只有使用者知道"),
         ("eye", "交給 Agent 之後，哪些成果只有自己實際使用才能驗證"), ("history", "系統由誰接手、如何交接"), ("wrench", "哪些修改適合由業務單位透過 Agent 自行完成")]
    c = "".join(f'<div class="card row" style="gap:20px;padding:22px 24px">{badge(i, "a", 40)}<div style="font-size:27px;line-height:1.4">{t}</div></div>' for i, t in q)
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:100%;grid-auto-rows:1fr;padding-bottom:6px">{c}</div>'


SECTIONS = [("一", "合併的理由", "從流程上解決 QC 的問題，減少後面真正需要 QC 的項目", "shield"), ("二", "資料與介面", "資料都存於專案資料庫，只在邊界轉換格式", "db"), ("三", "畫面", "模組化、逐步導入改變、即時回饋、以任務列表引導並主動協助", "tasks"),
            ("四", "接上現行流程", "每一段都能單獨接上，分階段替換", "refresh"), ("五", "新的處理想法", "讓處理更標準、步驟更少", "bulb"), ("六", "開發的時間成本", "Agent 降低撰寫程式的成本，設計的迭代仍然需要大量時間", "clock"),
            ("", "下一步與結語", "實際試用、互動式教學與自動挑波，以及 Agent 帶來的改變", "flag")]


def section_html(n, t, d, i):
    num = f'<div style="font-size:150px;font-weight:700;color:{ACCENT};line-height:1">{n}</div>' if n else f'<div>{ic(i, 130, ACCENT, 1.4)}</div>'
    return (f'<!doctype html><meta charset="utf-8"><style>{CSS}body{{background:{INK};color:#fff}}</style><body>'
            f'<div class="abs" style="left:120px;top:250px">{num}<div style="font-size:72px;font-weight:700;margin-top:22px">{t}</div><div style="font-size:32px;color:#D8D2C9;margin-top:18px;max-width:1300px">{d}</div></div>'
            f'<div class="abs" style="right:120px;top:300px;opacity:.9">{ic(i, 210, "#6B6560", 1.1) if n else ""}</div>')


def shot(src, out):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=1600,900", f"--screenshot={out}", src.as_uri()],
                   check=True, capture_output=True, timeout=90)


def figures():
    """網頁文稿用的圖：只留各頁的主體，不含標題與頁碼，輸出到 assets/week8-figs/。"""
    global USE_SHOTS
    USE_SHOTS = False
    out = HERE.parents[1] / "week8-figs"
    out.mkdir(exist_ok=True)
    for no in [n for n in sorted(SLIDES) if n not in (1, 24, 26, 28, 32)]:
        body = SLIDES[no][4]().replace("，課堂上實際操作", "").replace("下一頁是其中一個例子。", "")
        html = (f'<!doctype html><meta charset="utf-8"><style>{CSS}html,body{{width:1500px;height:665px;background:#fff}}.body{{left:20px;right:20px;top:20px;bottom:20px}}</style>'
                f'<body><div class="body">{body}</div>')
        src = TMP / f"fig-{no:02d}.html"
        src.write_text(html, encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1.5",
                        "--window-size=1500,665", f"--screenshot={out / f'w8-{no:02d}.png'}", src.as_uri()],
                       check=True, capture_output=True, timeout=90)


def main():
    TMP.mkdir(exist_ok=True)
    if sys.argv[1:] == ["figs"]:
        return figures()
    want = [int(a) for a in sys.argv[1:]] or sorted(SLIDES)
    if not sys.argv[1:]:
        for k, sec in enumerate(SECTIONS, 1):
            src = TMP / f"w8-sec{k}.html"
            src.write_text(section_html(*sec), encoding="utf-8")
            shot(src, HERE / f"w8-sec{k}.png")
    for no in want:
        name, sec, title, msg, fn = SLIDES[no]
        head = f'<div class="sec">{sec}</div><h1>{title}</h1><div class="msg">{msg}</div>' if title else ""
        html = (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>{head}'
                f'<div class="body">{fn()}</div><div class="foot"><span>第八週｜Agent 時代的知識工作</span><span>{no}</span></div>')
        src = TMP / f"w8-{no:02d}.html"
        src.write_text(html, encoding="utf-8")
        out = HERE / f"w8-{no:02d}-{name}.png"
        shot(src, out)
        print(out.name)


if __name__ == "__main__":
    main()
