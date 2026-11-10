#!/usr/bin/env python3
"""第九週投影片式示意圖：每頁產生一份 HTML，再以 Chrome 無頭模式輸出 1600×900 的 PNG（2 倍解析度）。

用法：python3 assets/week9-diagrams/slides/build.py [頁碼 ...]
內容依 drafts/28-week9-slides.md。全部為示意圖，波形、數值與畫面都是虛構或只標量級，不含真實資料。
配色、icon 與共用元件沿用第八週的 build.py。
"""
import importlib.util
import math
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W8 = HERE.parents[1] / "week8-diagrams/slides/build.py"
_spec = importlib.util.spec_from_file_location("w8build", W8)
w8 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(w8)

INK, MUTED, LINE, BG, ACCENT, ACCENT_BG, BLUE, BLUE_BG = w8.INK, w8.MUTED, w8.LINE, w8.BG, w8.ACCENT, w8.ACCENT_BG, w8.BLUE, w8.BLUE_BG
ACCENT_D, BLUE_D, GOOD = w8.ACCENT_D, w8.BLUE_D, w8.GOOD
CSS, ic, badge, arrow, wave, window, shot = w8.CSS, w8.ic, w8.badge, w8.arrow, w8.wave, w8.window, w8.shot
w8.ICONS.update({
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
    "scale": '<path d="M12 3v18M5 21h14M3 7h18M6 7l-3 7a3 3 0 0 0 6 0ZM18 7l-3 7a3 3 0 0 0 6 0Z"/>',
    "book": '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14M7 22l-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
    "split": '<path d="M16 3h5v5M8 3H3v5M12 22v-8.3a4 4 0 0 0-1.17-2.83L3 3M21 3l-7.83 7.83"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "grid": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',
    "cube": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96 12 12.01l8.73-5.05M12 22.08V12"/>',
    "radio": '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5M19.1 4.9C23 8.8 23 15.1 19.1 19"/><circle cx="12" cy="12" r="2"/>',
    "down": '<path d="M12 5v14M19 12l-7 7-7-7"/>',
    "up": '<path d="M12 19V5M5 12l7-7 7 7"/>',
})

SLIDES = {}
NOTE = "示意圖，數值只標量級，波形為虛構"


def slide(no, name, sec, title, msg):
    def deco(fn):
        SLIDES[no] = (name, sec, title, msg, fn)
        return fn
    return deco


def icard(i, kind, t, d, style="", size=36):
    k = {"a": "a", "b": "b"}.get(kind, "")
    return f'<div class="card {k} row" style="gap:18px;{style}">{badge(i, kind if kind in ("a", "b", "g") else "", size)}<div><div class="t">{t}</div><div class="s" style="color:{INK if k else MUTED}">{d}</div></div></div>'


def node(i, t, sub="", kind="", w=230, tag=""):
    k = {"a": "a", "b": "b"}.get(kind, "")
    col = {"a": ACCENT_D, "b": BLUE_D}.get(kind, INK)
    tg = f'<span class="tag {k}" style="background:#fff;margin-top:6px">{tag}</span>' if tag else ""
    s = f'<div class="s" style="font-size:20px;text-align:center">{sub}</div>' if sub else ""
    return f'<div class="card {k} col" style="width:{w}px;align-items:center;gap:6px;padding:16px 12px">{ic(i, 40, col)}<div class="t" style="font-size:25px;text-align:center">{t}</div>{s}{tg}</div>'


S1, S2, S3 = "一、工具配合人", "二、模型的更新可以信任", "三、重新評估"


# ---------------- 第 1 頁
@slide(1, "cover", "", "", "")
def s1():
    w = wave(1600, 300, 11, onset=.42, amp=1, noise=.04, color=BLUE, sw=1.5)
    items = [("bot", "AI 掃描"), ("scissors", "切事件審核"), ("pin", "定位補齊"), ("shield", "治理")]
    chain = arrow(44).join(f'<div class="row" style="gap:10px;font-size:28px;font-weight:600">{ic(i, 36, BLUE_D)}{t}</div>' for i, t in items)
    return (f'<div class="abs" style="left:-70px;top:330px;opacity:.5">{w}</div>'
            f'<div class="abs" style="left:0;top:-30px"><div style="font-size:26px;color:{ACCENT_D};font-weight:600">第九週｜Agent 時代的知識工作</div>'
            f'<div style="font-size:84px;font-weight:700;line-height:1.25;margin-top:14px">自動挑波的導入與重新評估</div>'
            f'<div style="font-size:32px;color:{MUTED};margin-top:12px">以一週的實際開發，說明 AI 的導入如何從工具走到業務目標的重新檢視</div></div>'
            f'<div class="abs row" style="left:0;bottom:30px;gap:18px">{chain}</div>')


# ---------------- 第 2 頁
@slide(2, "route", "本週路線", "本週路線", "本週以開發本身作為示範，依序回答三個問題")
def s2():
    tl = [("gauge", "量測延遲"), ("bot", "AI 掃描"), ("shield", "治理流程"), ("search", "重新評估")]
    line = "".join((f'<div style="flex:1;height:3px;background:{LINE};margin:0 8px"></div>' if n else "") +
                   f'<div class="row" style="gap:10px">{badge(i, "b", 30)}<span style="font-size:25px;font-weight:600">{t}</span></div>' for n, (i, t) in enumerate(tl))
    q = [("1", "工具配合人", "同仁的操作時間很短，又有既定的交接方式，工具如何配合"),
         ("2", "模型的更新可以信任", "模型會持續更新，如何確保每次更新都有依據、可以退回"),
         ("3", "重新評估", "加快每個事件的處理，是否解決了業務真正的問題")]
    cards = "".join(f'<div class="card {"a" if n == 2 else ""} col" style="flex:1;gap:12px;padding:26px"><div style="font-size:64px;font-weight:700;color:{ACCENT if n == 2 else BLUE};line-height:1">{a}</div>'
                    f'<div class="t" style="font-size:32px">{b}</div><div style="font-size:25px;line-height:1.5">{c}</div>'
                    + (f'<span class="tag a" style="background:#fff;margin-top:auto;align-self:flex-start">開發後半才出現</span>' if n == 2 else "") + '</div>' for n, (a, b, c) in enumerate(q))
    return (f'<div class="col" style="gap:26px;height:100%"><div class="card row" style="padding:16px 26px">{line}</div>'
            f'<div class="row" style="gap:20px;flex:1;align-items:stretch">{cards}</div>'
            f'<div class="note">訪談是過場：評估之後，依同仁的工作條件重新安排開發的方向</div></div>')


# ---------------- 第 3 頁
@slide(3, "conditions", "開場", "同仁的工作條件", "開發的方向由同仁實際的工作條件決定")
def s3():
    cs = [("clock", "a", "操作的速度", "點擊與切換非常快，每站只能花很短的時間，操作必須幾乎沒有延遲", "對應：操作延遲"),
          ("eye", "", "現行的做法", "以自動結果為底，確認是地震後逐站快速瀏覽，只修正有問題的測站", "對應：審核的設計"),
          ("history", "b", "自動結果的時效", "事件波形檔產生一段時間之後才補上，切事件時無法使用", "對應：AI 掃描"),
          ("users", "", "分工", "切事件與定位由不同的同仁負責，每個步驟各自專注，以檔案交接", "對應：與原有流程的銜接")]
    g = "".join(f'<div class="card col" style="gap:10px;padding:22px 24px"><div class="row" style="gap:16px">{badge(i, k or "", 34)}<div class="t">{t}</div></div>'
                f'<div style="font-size:24px;line-height:1.45">{d}</div><span class="tag {k}" style="margin-top:auto;align-self:flex-start">{m}</span></div>' for i, k, t, d, m in cs)
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:100%;grid-auto-rows:1fr">{g}</div>'


# ---------------- 第 4 頁
@slide(4, "latency", S1, "操作延遲", "先量測，再改善，並找出程式無法省略的部分")
def s4():
    def bar(label, before, after, unit_b, unit_a):
        return (f'<div class="col" style="gap:6px"><div style="font-size:24px;font-weight:600">{label}</div>'
                f'<div class="row" style="gap:12px"><span class="note" style="width:70px">修改前</span><div style="height:26px;width:{before}px;background:{BLUE};border-radius:6px"></div><span style="font-size:21px;color:{BLUE_D}">{unit_b}</span></div>'
                f'<div class="row" style="gap:12px"><span class="note" style="width:70px">修改後</span><div style="height:26px;width:{after}px;background:{ACCENT};border-radius:6px"></div><span style="font-size:21px;color:{ACCENT_D}">{unit_a}</span></div></div>')
    bars = (bar("縮小時間軸", 520, 8, "數秒", "數十毫秒") + bar("第一次打開三分量視窗", 330, 40, "約兩秒", "約兩百毫秒")
            + bar("到沒讀過的檔", 360, 300, "兩秒多", "將近兩秒"))
    comp = (f'<div class="col" style="gap:8px"><div style="font-size:24px;font-weight:600">沒讀過的檔：時間的組成</div>'
            f'<div class="row" style="height:44px;border-radius:8px;overflow:hidden;font-size:21px;color:#fff;font-weight:600">'
            f'<div class="row" style="width:76%;height:100%;background:{BLUE_D};justify-content:center">網路磁碟讀取</div>'
            f'<div class="row" style="width:24%;height:100%;background:{ACCENT};justify-content:center">程式</div></div>'
            f'<div class="note">檔案超過 100 MB，讀取就要一秒以上，程式只能提早讀</div></div>')
    pts = [("ok", "g", "等待最久的操作改善最多"), ("ok", "g", "已預讀的資料幾乎不必等待"), ("warn", "b", "沒讀過的檔受網路限制，下一步改為調整架構")]
    left = "".join(f'<div class="card row" style="gap:16px;padding:18px 20px">{badge(i, k, 30)}<div style="font-size:26px;font-weight:600">{t}</div></div>' for i, k, t in pts)
    return (f'<div class="row" style="gap:30px;height:100%;align-items:stretch"><div class="col" style="width:560px;gap:16px">{left}'
            f'<div class="card b" style="font-size:23px;margin-top:auto">交班前由伺服器先算好波形的摘要，輪班時只傳送摘要</div></div>'
            f'<div class="card col" style="flex:1;gap:20px;padding:22px 28px">{bars}{comp}</div></div>')


# ---------------- 第 5 頁
@slide(5, "pipeline", S1, "自動挑波的流水線", "AI 先掃描連續波形，切事件與定位改為審核系統的候選結果")
def s5():
    def row(tag, k, items):
        chips = "".join((arrow(36) if n else "") + node(*it) for n, it in enumerate(items))
        return f'<div class="row" style="gap:18px"><div style="width:150px"><span class="tag {k}" style="white-space:nowrap">{tag}</span></div><div class="row" style="gap:6px">{chips}</div></div>'
    old = [("wave", "連續波形", "", "", 200), ("scissors", "切事件", "人工瀏覽整天", "b", 230), ("pin", "定位", "從空白開始挑波", "b", 230), ("shield", "檢查", "", "", 200)]
    new = [("wave", "連續波形", "", "", 200), ("bot", "AI 掃描", "挑波、關聯、定位", "a", 230, "已完成"), ("scissors", "切事件審核", "接受、調整、刪除", "", 230, "待做"),
           ("pin", "定位補齊", "確認、微調、補挑", "", 230, "待做"), ("shield", "檢查", "", "", 200)]
    return (f'<div class="col" style="gap:34px;height:100%;justify-content:center">{row("原有流程", "b", old)}{row("加入 AI 掃描", "a", new)}'
            f'<div class="card row" style="gap:14px;padding:14px 22px">{ic("bulb", 30, ACCENT_D)}<span style="font-size:25px">先求流水線完整，模型的準確度之後再以自己的資料訓練。系統沒有找到的地震，照原本的方式補上。</span></div></div>')


# ---------------- 第 6 頁
@slide(6, "window", S1, "關聯的範圍", "關聯的範圍由實驗決定，以 16 分鐘為一段")
def s6():
    steps = [("wave", "挑波", "各站的 P、S 到時"), ("layers", "關聯", "哪些到時屬於同一個地震"), ("pin", "定位", "求出震源")]
    st = "".join((arrow(34) if n else "") + node(i, t, d, "b", 190) for n, (i, t, d) in enumerate(steps))
    data = [("4 分鐘", 73, 11), ("15 分鐘", 18, 11), ("1 小時", 16, 11), ("整個班次", 16, 12)]
    H = 400
    bars = "".join(f'<div class="col" style="align-items:center;gap:8px;flex:1"><div class="row" style="align-items:flex-end;gap:10px;height:{H}px">'
                   f'<div style="width:46px;height:{c / 73 * H:.0f}px;background:{BLUE};border-radius:6px 6px 0 0"></div>'
                   f'<div style="width:46px;height:{m / 73 * H:.0f}px;background:{ACCENT};border-radius:6px 6px 0 0"></div></div>'
                   f'<div style="font-size:23px;font-weight:{700 if lab == "15 分鐘" else 500}">{lab}</div></div>' for lab, c, m in data)
    legend = (f'<div class="row" style="gap:22px;font-size:21px"><span class="row" style="gap:8px"><span style="width:18px;height:18px;background:{BLUE};border-radius:4px"></span>候選事件</span>'
              f'<span class="row" style="gap:8px"><span style="width:18px;height:18px;background:{ACCENT};border-radius:4px"></span>與人工結果相符</span></div>')
    return (f'<div class="row" style="gap:28px;height:100%;align-items:stretch"><div class="col" style="width:640px;gap:18px"><div class="row" style="gap:4px">{st}</div>'
            f'<div class="card" style="font-size:24px;line-height:1.5">逐檔關聯時，雜訊湊成大量假事件。挑波不變、只改關聯的範圍，<b>15 分鐘以上假事件大幅減少，真實事件幾乎不變</b>。取結果穩定的最短範圍：16 分鐘，一天 90 段。</div>'
            f'<div class="note">範圍更換權重或關聯工具之後需要重新檢驗</div></div>'
            f'<div class="card col" style="flex:1;gap:14px;padding:22px 26px"><div class="row" style="justify-content:space-between"><b style="font-size:24px">一次關聯的範圍</b>{legend}</div>'
            f'<div class="row" style="gap:6px;border-bottom:2px solid {MUTED}">{bars}</div><div class="note">{NOTE}</div></div></div>')


# ---------------- 截圖
SHOTS = HERE.parents[1] / "week9-shots"
MASKED = "開發中的系統畫面，測站代碼、檔名與件數已模糊"


def has_shot(name):
    return (SHOTS / name).exists()


def blurs(regions):
    """以百分比座標 (x, y, w, h) 模糊截圖中的識別資訊。"""
    return "".join(f'<div class="abs" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%;backdrop-filter:blur(5px);-webkit-backdrop-filter:blur(5px);background:rgba(255,255,255,.15)"></div>' for x, y, w, h in regions)


def mark(n, x, y):
    return (f'<span class="abs row" style="left:{x}%;top:{y}%;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;background:{ACCENT_D};color:#fff;'
            f'font-size:25px;font-weight:700;justify-content:center;border:3px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.35)">{n}</span>')


def numbered(notes, start=1):
    return "".join(f'<div class="row" style="gap:12px;align-items:flex-start"><span class="row" style="width:38px;height:38px;border-radius:50%;background:{ACCENT_D};color:#fff;font-size:22px;font-weight:700;justify-content:center;flex:none">{i + start}</span>'
                   f'<div><div style="font-size:25px;font-weight:700;line-height:1.3">{a}</div><div style="font-size:22px;color:{MUTED};line-height:1.4">{d}</div></div></div>' for i, (a, d) in enumerate(notes))


def shot_box(name, W, marks, regions):
    img = f'<img src="{(SHOTS / name).as_uri()}" style="width:{W}px;display:block;border-radius:10px;border:1.5px solid {LINE}">'
    ms = "".join(mark(i + 1, x, y) for i, (x, y) in enumerate(marks))
    return f'<div class="col" style="gap:6px"><div style="position:relative;width:{W}px;border-radius:10px;overflow:hidden">{img}{blurs(regions)}{ms}</div><div class="note">{MASKED}</div></div>'


def real7():
    regions = [(0, 15.5, 4.2, 45), (3.5, 9, 36, 2.6), (0, 61.3, 2.6, 2.4), (6.3, 14.3, 3.4, 1.8),
               (75.6, 60.5, 5.2, 39.5), (92.8, 60.5, 7.2, 39.5), (79.4, 45.6, 15.8, 2.6), (0.5, 9, 3, 2.6)]
    marks = [(9, 26), (17, 17), (8, 75), (25, 62.7), (90, 47)]
    notes = [("波形牆", "涵蓋整天，看得到模型沒有標出事件的時段"), ("走時曲線", "依緯度排列時畫成雙曲線，與挑選的短線容易區分"),
             ("單站預覽", "三個分量放大顯示，最下面一列是模型的機率曲線"), ("參數面板", "前處理與門檻先作用在預覽上，確認後才重掃"),
             ("評估視窗", "依規模、位置分項列出偵測率，例如外海明顯偏低")]
    return (f'<div class="row" style="gap:22px;height:100%;align-items:flex-start">{shot_box("w9-07-tools.png", 1040, marks, regions)}'
            f'<div class="col" style="flex:1;gap:16px">{numbered(notes)}</div></div>')


def real8():
    regions = [(1.8, 16, 4.4, 56), (4.6, 7.6, 6.2, 2.4), (26.6, 78.4, 6.4, 2.2), (78, 64.5, 20.5, 11.5), (87, 79.5, 6.6, 18.5), (79, 82, 3.2, 3), (93.3, 85, 4.8, 9), (20.5, 38.9, 9.8, 2.6)]
    marks = [(96, 58.5), (8, 92)]
    notes = [("每日的時間窗清單", "看過的連續波形檔各寫一份瀏覽紀錄檔，一天累積成一份清單"), ("時間軸", "新的檔案出現時自動接上，跨日接到隔天的資料夾")]
    side = (f'<div class="col" style="flex:1;gap:16px;height:100%">{numbered(notes)}'
            f'<div class="card b row" style="gap:14px;align-items:flex-start">{ic("lock", 30, BLUE_D)}<div><div style="font-size:24px;font-weight:700">不寫回正式的資料</div><div style="font-size:21px;line-height:1.4">輸出寫在專案資料夾，禁止指向原始資料的網路磁碟</div></div></div>'
            f'<div class="card a row" style="gap:14px;align-items:flex-start">{ic("wrench", 30, ACCENT_D)}<div><div style="font-size:24px;font-weight:700">交付後依回饋修正</div><div style="font-size:21px;line-height:1.4">重新安裝後，一天內發布數個修正版本</div></div></div></div>')
    return f'<div class="row" style="gap:22px;height:100%;align-items:flex-start">{shot_box("w9-09-windows.png", 1040, marks, regions)}{side}</div>'


# ---------------- 第 7 頁
@slide(7, "scan", S1, "AI 掃描", "同仁可以檢查模型的判斷，不必直接相信結果")
def s8():
    if has_shot("w9-07-tools.png"):
        return real7()
    Wd, Hd = 980, 600
    tr = ""
    for k in range(10):
        y = 30 + k * 34
        on = .30 + abs(k - 4.5) * .028
        tr += f'<div class="abs" style="left:20px;top:{y}px">{wave(640, 32, 40 + k, onset=on, amp=.9, noise=.09, color=INK, sw=1)}</div>'
        tr += f'<div class="abs" style="left:{20 + on * 640:.0f}px;top:{y + 4}px;width:3px;height:24px;background:{BLUE_D}"></div>'
    curve = f'<svg class="abs" style="left:20px;top:30px" width="640" height="345"><path d="M{.30 * 640 + 80:.0f} 0 Q {.30 * 640 - 35:.0f} 172 {.30 * 640 + 80:.0f} 345" fill="none" stroke="{ACCENT_D}" stroke-width="3" stroke-dasharray="7 6"/></svg>'
    prev = (f'<div class="abs" style="left:20px;top:395px;width:640px;height:190px;background:{BG};border-radius:10px;padding:8px 10px">'
            + "".join(f'<div style="height:38px">{wave(620, 38, 70 + j, onset=.45, amp=.9, noise=.06, color=INK, sw=1)}</div>' for j in range(3))
            + f'<svg width="620" height="50"><path d="M0 46 L270 46 Q 285 46 290 8 Q 295 46 310 46 L 620 46" fill="none" stroke="{BLUE_D}" stroke-width="2.5"/><line x1="0" y1="24" x2="620" y2="24" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5 5"/></svg></div>')
    side = (f'<div class="abs col" style="left:690px;top:30px;width:270px;gap:10px"><div class="card" style="padding:10px 14px;height:150px;background:{BLUE_BG};border-color:{BLUE}"></div>'
            + "".join(f'<div style="height:26px;background:{BG};border-radius:5px"></div>' for _ in range(6))
            + f'<div class="card a" style="padding:10px 14px;font-size:20px">評估：分項偵測率</div></div>')
    def mk(n, x, y):
        return (f'<span class="abs row" style="left:{x}px;top:{y}px;width:42px;height:42px;border-radius:50%;background:{ACCENT_D};color:#fff;font-size:24px;font-weight:700;justify-content:center;border:3px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.3)">{n}</span>')
    mock = (f'<div style="position:relative;width:{Wd}px;height:{Hd}px;background:#fff;border:1.5px solid {LINE};border-radius:14px">{tr}{curve}{prev}{side}'
            + mk(1, 6, 6) + mk(2, 300, 6) + mk(3, 40, 380) + mk(4, 560, 520) + mk(5, 900, 540) + '</div>')
    notes = [("波形牆", "涵蓋整天，看得到模型沒有標出事件的時段"), ("走時曲線", "依緯度排列時畫成雙曲線，與挑選的短線容易區分"), ("單站預覽", "三個分量放大顯示，最下面一列是模型的機率曲線"),
             ("參數面板", "前處理與門檻先作用在預覽上，確認後才重掃"), ("評估視窗", "依規模、位置分項列出偵測率，例如外海明顯偏低")]
    ns = "".join(f'<div class="row" style="gap:12px;align-items:flex-start"><span class="row" style="width:38px;height:38px;border-radius:50%;background:{ACCENT_D};color:#fff;font-size:22px;font-weight:700;justify-content:center;flex:none">{i + 1}</span>'
                 f'<div><div style="font-size:25px;font-weight:700">{t}</div><div style="font-size:22px;color:{MUTED};line-height:1.4">{d}</div></div></div>' for i, (t, d) in enumerate(notes))
    return (f'<div class="row" style="gap:24px;height:100%;align-items:flex-start"><div class="col" style="gap:6px">{mock}<div class="note">畫面為示意，波形與版面皆為虛構</div></div>'
            f'<div class="col" style="flex:1;gap:20px">{ns}</div></div>')


# ---------------- 第 8 頁
@slide(8, "integration", S1, "與原有流程的銜接", "新工具產出原有流程需要的檔案，環境不如預期時仍可工作")
def s9():
    if has_shot("w9-09-windows.png"):
        return real8()
    files = [("file", "瀏覽紀錄檔", "看過的檔各寫一份"), ("list", "每日的時間窗清單", "一天累積成一份")]
    fc = "".join(f'<div class="card row" style="gap:14px;padding:14px 18px">{ic(i, 32, ACCENT_D)}<div><div style="font-size:24px;font-weight:700">{t}</div><div class="s" style="font-size:20px">{d}</div></div></div>' for i, t, d in files)
    flow = (f'<div class="row" style="gap:14px;align-items:center">{node("scissors", "切事件", "新工具", "a", 200)}{arrow(40)}<div class="col" style="gap:12px">{fc}</div>{arrow(40)}{node("refresh", "原有流程", "照常交接", "b", 200)}</div>')
    guard = (f'<div class="row" style="gap:18px"><div class="card b row" style="flex:1;gap:16px">{badge("lock", "b", 32)}<div><div class="t">不寫回正式的資料</div><div class="s" style="color:{INK}">輸出寫在專案資料夾，設定上禁止指向原始資料的網路磁碟</div></div></div>'
             f'<div class="card row" style="flex:1;gap:16px">{badge("clock", "", 32)}<div><div class="t">自動接上新的檔案</div><div class="s">新的連續波形檔出現時接上，跨日接到隔天的資料夾</div></div></div></div>')
    fix = [("wrench", "資料夾一律由同仁選擇"), ("drive", "網路磁碟連不上時照常啟動"), ("gauge", "只讀選擇的資料夾，開啟變快")]
    fx = "".join(f'<div class="row" style="gap:10px;font-size:23px">{ic(i, 28, ACCENT_D)}{t}</div>' for i, t in fix)
    deliver = (f'<div class="card a row" style="gap:26px;padding:16px 24px"><div style="width:250px"><div class="t">交付後依回饋修正</div><div class="s" style="color:{INK}">重新安裝後，一天內發布數個修正版本</div></div>'
               f'<div class="row" style="gap:26px;flex:1;flex-wrap:wrap">{fx}</div></div>')
    return f'<div class="col" style="gap:22px;height:100%">{flow}{guard}{deliver}</div>'


# ---------------- 第 9 頁
@slide(9, "governance", S2, "治理流程", "先把更新的流程做出來，再追求模型的表現")
def s10():
    st = [("box", "匯出", "雜湊值與說明書", "來源不明的權重"), ("book", "入倉", "先看說明書與檢查結果", "未經檢視就使用"), ("search", "掃描", "結果記下權重版本", "事後無法追溯"),
          ("scale", "比較", "只計兩版都掃過的檔", "以不同資料比較"), ("repeat", "換版與退版", "都要填寫理由", "換版沒有依據")]
    cols = "".join((f'<div style="align-self:flex-start;margin-top:100px">{arrow(30)}</div>' if n else "") +
                   f'<div class="col" style="flex:1;gap:12px"><div class="card a col" style="align-items:center;justify-content:center;gap:10px;padding:18px 10px;height:220px">{ic(i, 54, ACCENT_D)}<div class="t" style="font-size:30px">{t}</div><div style="font-size:22px;text-align:center">{d}</div></div>'
                   f'<div class="card col" style="gap:8px;padding:16px 16px;height:110px"><div class="row" style="gap:6px;font-size:20px;color:{BLUE_D};font-weight:600">{ic("shield", 24, BLUE_D)}防止</div><div style="font-size:24px">{r}</div></div></div>' for n, (i, t, d, r) in enumerate(st))
    log = [("入倉", ""), ("入倉", ""), ("比較報告", ""), ("設為預設", "理由"), ("退版", "理由")]
    lg = "".join(f'<div class="row" style="gap:8px;padding:6px 14px;background:{BG};border-radius:8px;font-size:21px">{ic("history", 22, MUTED)}{t}' + (f'<span class="tag a" style="font-size:16px">{x}</span>' if x else "") + '</div>' for t, x in log)
    return (f'<div class="col" style="gap:22px;height:100%"><div class="row" style="gap:6px;align-items:flex-start">{cols}</div>'
            f'<div class="card row" style="gap:14px;padding:14px 20px;margin-top:auto"><span class="t" style="font-size:23px;white-space:nowrap">操作紀錄｜只增不改</span>{lg}</div>'
            f'<div class="note">以一組已訓練好的權重走完全程，不要求它的表現。入倉、比較與換版都由人觸發，不做自動排程。</div></div>')


# ---------------- 第 10 頁
@slide(10, "continual", S2, "持續訓練", "離線測試通過關卡，不代表在實際資料上比較好")
def s11():
    W, H = 600, 380
    pts = []
    for r in range(3):
        x0 = 40 + r * 180
        pts.append(f"M{x0} {H - 30}")
        pts.append(f"L{x0 + 25} 40")
        for k in range(1, 21):
            x = x0 + 25 + k * 7.5
            y = 40 + (H - 70) * (1 - math.cos(math.pi * k / 20)) / 2
            pts.append(f"L{x:.1f} {y:.1f}")
    lr = (f'<svg width="{W}" height="{H}"><line x1="30" y1="{H - 30}" x2="{W}" y2="{H - 30}" stroke="{MUTED}" stroke-width="2"/>'
          f'<path d="{" ".join(pts)}" fill="none" stroke="{BLUE_D}" stroke-width="3"/>'
          + "".join(f'<text x="{40 + r * 180 + 80}" y="{H - 6}" text-anchor="middle" font-size="19" fill="{MUTED}">第 {r + 1} 輪</text>' for r in range(3))
          + f'<text x="34" y="26" font-size="19" fill="{MUTED}">學習率</text></svg>')
    left = (f'<div class="card col" style="width:660px;gap:10px"><div class="t">每一輪重新安排學習率</div>{lr}'
            f'<div style="font-size:23px;line-height:1.5">每輪先短暫升高再衰減，並混入一半的舊資料，避免模型遺忘</div></div>')
    res = (f'<div class="row" style="gap:16px"><div class="card col" style="flex:1;gap:8px;align-items:center;padding:20px">{ic("up", 46, GOOD)}<div class="t">離線測試集</div><div class="s">新舊兩份都比上一版好</div><span class="tag" style="background:#E7EFE9;color:{GOOD}">通過關卡</span></div>'
           f'<div class="card a col" style="flex:1;gap:8px;align-items:center;padding:20px">{ic("down", 46, ACCENT_D)}<div class="t">實際掃描同一天</div><div class="s" style="color:{INK}">事件的偵測率大幅下降</div><span class="tag a" style="background:#fff">退步</span></div></div>')
    cause = (f'<div class="card b col" style="gap:8px"><div class="row" style="gap:10px">{ic("search", 28, BLUE_D)}<span class="t">原因</span></div>'
             f'<div style="font-size:23px;line-height:1.5">微調後機率的峰值變低，挑選的門檻隨權重調低，關聯的門檻沒有跟著改。關聯的門檻也要隨權重一起交付。</div></div>')
    return f'<div class="row" style="gap:24px;height:100%;align-items:stretch">{left}<div class="col" style="flex:1;gap:18px">{res}{cause}</div></div>'


# ---------------- 第 11 頁
@slide(11, "packages", S2, "交付到署內的電腦", "主程式、執行環境與模型分開交付，各自可以單獨更新")
def s12():
    pk = [("cube", "主程式", "所有電腦都安裝", ""), ("cpu" if "cpu" in w8.ICONS else "box", "執行環境", "ONNX 推論，不帶深度學習框架，只裝在需要的電腦", "b"), ("box", "模型包", "附說明書，在設定頁選擇後入倉", "a")]
    cards = "".join(f'<div class="card {k} col" style="flex:1;gap:12px;padding:24px;align-items:flex-start">{badge(i, k, 44)}<div class="t" style="font-size:30px">{t}</div><div style="font-size:24px;line-height:1.5">{d}</div></div>' for i, t, d, k in pk)
    entry = (f'<div class="row" style="gap:18px;align-items:center"><div class="card a row" style="gap:12px;padding:14px 20px">{ic("box", 30, ACCENT_D)}<b style="font-size:25px">模型包</b></div>{arrow(50, ACCENT_D)}'
             f'<div class="card a row" style="gap:12px;padding:14px 20px">{ic("db", 30, ACCENT_D)}<b style="font-size:25px">模型倉</b></div>{arrow(50, ACCENT_D)}'
             f'<div class="card row" style="gap:12px;padding:14px 20px">{ic("bot", 30, INK)}<b style="font-size:25px">AI 掃描</b></div>'
             f'<div style="font-size:24px;margin-left:16px">模型進入署內電腦的入口只有這一個，與治理流程使用同一個模型倉</div></div>')
    return (f'<div class="col" style="gap:24px;height:100%"><div class="row" style="gap:20px;flex:1;align-items:stretch">{cards}</div>{entry}'
            f'<div class="note">中文資料夾的路徑、預設的文字編碼等問題，都在 Windows 測試機上實際執行才發現</div></div>')


# ---------------- 第 12 頁
@slide(12, "basis", S2, "制度的依據", "以公部門既有的手冊與法規檢查導入的規劃")
def s13():
    refs = ["數位發展部《公部門人工智慧應用參考手冊》", "iPAS AI 應用規劃師中級學習指引", "人工智慧基本法", "資通安全的相關規定", "ISO/IEC 42001 人工智慧管理系統"]
    rl = "".join(f'<div class="row" style="gap:12px;padding:12px 0;border-top:{"none" if n == 0 else "1px solid " + LINE};font-size:24px">{ic("book", 28, BLUE_D)}{t}</div>' for n, t in enumerate(refs))
    left = (f'<div class="card col" style="width:640px"><div class="row" style="gap:10px;margin-bottom:6px"><span class="t">參考資料</span><span class="tag">提案書撰寫中</span></div>{rl}'
            f'<div class="note" style="margin-top:auto">Agent 讀取原文並整理成可以對照的形式，由人挑選適用的部分</div></div>')
    cs = [("tasks", "a", "管理制度要回答五件事", "使用者、系統的目標、利害關係人、如何檢查使用紀錄、誰有監督與糾正錯誤的權限"),
          ("lock", "b", "提供者不能自行換版", "新版本設為預設之前，須經核准者同意"),
          ("shield", "", "紀錄不用於考核", "審核與修改的紀錄只用於模型的評估與訓練")]
    right = "".join(icard(i, k, t, d, "flex:1") for i, k, t, d in cs)
    return f'<div class="row" style="gap:24px;height:100%;align-items:stretch">{left}<div class="col" style="flex:1;gap:16px">{right}</div></div>'


# ---------------- 第 13 頁
@slide(13, "baseline", S2, "比較的基準", "比較的基準要在看到結果之前決定並固定")
def s14():
    cs = [("target", "a", "比較的對象", "開源權重、即時系統的自動結果、上一個正式版本、同仁之間的差異"),
          ("layers", "b", "測試資料", "與訓練資料分開，固定的測試集加上版本，涵蓋困難情境並分項計分"),
          ("sliders", "", "計分方式", "前處理與門檻隨權重固定，容許誤差依「差多少以內不必修改」訂定"),
          ("search", "", "找出困難的資料", "多個模型挑同一批標記，都挑在別處或都沒挑到的，問題可能在標記本身")]
    g = "".join(f'<div class="card {k} col" style="gap:10px;padding:22px 24px"><div class="row" style="gap:16px">{badge(i, k, 32)}<div class="t">{t}</div></div><div style="font-size:24px;line-height:1.45">{d}</div></div>' for i, k, t, d in cs)
    fifth = (f'<div class="card row" style="gap:16px;padding:14px 22px;border-style:dashed">{ic("flag", 30, MUTED)}<span style="font-size:24px">第五件事是<b>正確答案</b>，在第三大段落回答</span>'
             f'<span class="row" style="gap:8px;margin-left:auto;font-size:23px;color:{ACCENT_D};font-weight:600">{ic("lock", 26, ACCENT_D)}更改需經核准並留下紀錄</span></div>')
    return f'<div class="col" style="gap:18px;height:100%"><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;flex:1;grid-auto-rows:1fr">{g}</div>{fifth}</div>'


# ---------------- 第 14 頁
@slide(14, "filled", S3, "件數壓力下的補齊", "參考理論到時補上的測站，可能混入實際上沒有相位的雜訊")
def s15():
    W = 760
    def tr(seed, onset, flat, label, mark=None, theo=None):
        w = wave(W - 120, 70, seed, onset=onset, amp=.9, noise=.1, color=INK, sw=1.1, flat=flat)
        th = f'<div class="abs" style="left:{theo * (W - 120):.0f}px;top:-4px;bottom:-4px;border-left:2.5px dashed {BLUE_D}"></div>' if theo else ""
        mk = f'<div class="abs" style="left:{mark * (W - 120):.0f}px;top:6px;width:4px;height:58px;background:{ACCENT_D}"></div>' if mark else ""
        return f'<div class="row" style="gap:12px;padding:6px 0"><span style="width:96px;font-size:20px;color:{MUTED}">{label}</span><div style="position:relative;width:{W - 120}px;height:70px">{w}{th}{mk}</div></div>'
    rows = tr(81, .32, False, "清楚的站", .32) + tr(82, .40, False, "清楚的站", .40) + tr(83, .5, True, "補上的站", .55, .55)
    lg = (f'<div class="row" style="gap:24px;font-size:20px;margin-top:6px"><span class="row" style="gap:8px"><span style="width:4px;height:22px;background:{ACCENT_D}"></span>到時</span>'
          f'<span class="row" style="gap:8px"><span style="width:0;height:22px;border-left:2.5px dashed {BLUE_D}"></span>理論到時</span><span class="note">{NOTE}</span></div>')
    eff = [("chart", "殘差偏小", "定位品質看起來比實際好"), ("layers", "進入訓練的標記", "以空間一致性檢查時反而最正常"), ("bot", "AI 導入後更快", "補齊的速度跟著提高")]
    ec = "".join(icard(i, "b", t, d, "flex:1", 30) for i, t, d in eff)
    return (f'<div class="row" style="gap:24px;height:100%;align-items:stretch"><div class="card col" style="width:{W + 30}px;gap:4px">{rows}{lg}'
            f'<div style="font-size:23px;line-height:1.5;margin-top:auto">時間有限，檢查又以測站數量作為品質條件之一，參考理論到時補上波相不清楚的測站，容易成為完成工作的方式。這是流程與指標的設計問題。</div></div>'
            f'<div class="col" style="flex:1;gap:14px">{ec}</div></div>')


# ---------------- 第 15 頁
@slide(15, "solved", S3, "導入 AI 是否解決了問題", "只把 AI 放進現有的流程，解決的是速度，沒有解決品質與落後")
def s16():
    W, H = 640, 420
    months = 10
    def px(i): return 50 + i * (W - 80) / (months - 1)
    newp = " ".join(f"{'M' if i == 0 else 'L'}{px(i):.0f} {110 + 6 * math.sin(i):.0f}" for i in range(months))
    proc = " ".join(f"{'M' if i == 0 else 'L'}{px(i):.0f} {230 + 6 * math.cos(i):.0f}" for i in range(months))
    chart = (f'<svg width="{W}" height="{H}"><line x1="40" y1="{H - 40}" x2="{W}" y2="{H - 40}" stroke="{MUTED}" stroke-width="2"/><line x1="40" y1="20" x2="40" y2="{H - 40}" stroke="{MUTED}" stroke-width="2"/>'
             f'<path d="{newp}" fill="none" stroke="{ACCENT_D}" stroke-width="3.5"/><path d="{proc}" fill="none" stroke="{BLUE_D}" stroke-width="3.5"/>'
             f'<text x="{W - 10}" y="105" text-anchor="end" font-size="21" fill="{ACCENT_D}" font-weight="600">每月新增的量</text>'
             f'<text x="{W - 10}" y="265" text-anchor="end" font-size="21" fill="{BLUE_D}" font-weight="600">每月處理的量</text>'
             f'<text x="{W / 2 + 20}" y="{H - 10}" text-anchor="middle" font-size="19" fill="{MUTED}">月份</text></svg>')
    left = f'<div class="card col" style="width:700px;gap:8px"><div class="t">處理量低於新增量，落後持續累積</div>{chart}<div class="note">示意圖，不代表實際的數量</div></div>'
    chk = [("ok", "g", "速度", "每個事件的處理時間縮短"), ("x", "a", "落後", "人力仍與事件數成正比，只是補得比較快"), ("x", "a", "品質", "以測站數量為條件，補齊的誘因仍在，品質無從得知")]
    rc = "".join(f'<div class="card row" style="gap:16px;padding:18px 22px">{badge(i, k, 30)}<div><div class="t">{t}</div><div class="s">{d}</div></div></div>' for i, k, t, d in chk)
    return (f'<div class="row" style="gap:24px;height:100%;align-items:stretch">{left}<div class="col" style="flex:1;gap:14px"><div class="t" style="color:{MUTED}">最大的業務目標：補齊落後的月份</div>{rc}'
            f'<div class="card b" style="font-size:23px;margin-top:auto">需要重新思考人的角色、效益的衡量方式與交付的成果</div></div></div>')


# ---------------- 第 16 頁
@slide(16, "triage", S3, "品質先於數量", "品質放在數量之前，人力集中在困難或不確定的事件")
def s17():
    qs = [("radio", "是不是地震", "多站是否一致"), ("repeat", "附近有沒有已確認的地震", "相似的波形可以當樣板"), ("pin", "定位的約束夠不夠", "測站不足時不補站")]
    qc = "".join((f'<div style="align-self:center">{arrow(28)}</div>' if n else "") + f'<div class="card b col" style="flex:1;gap:6px;padding:14px 16px"><div class="row" style="gap:10px">{ic(i, 28, BLUE_D)}<b style="font-size:23px">{t}</b></div><div class="s" style="font-size:20px;color:{INK}">{d}</div></div>' for n, (i, t, d) in enumerate(qs))
    cats = [("repeat", "g", "與已確認事件相似", "由樣板推得到時，自動定位", "抽查"), ("ok", "g", "清楚的測站足夠", "自動接受", "抽查"),
            ("clock", "", "確定是地震但測站太少", "保留事件與不確定度", "暫定"), ("user", "a", "存疑", "人工審核", "人力集中")]
    cc = "".join(f'<div class="card {"a" if k == "a" else ""} col" style="flex:1;gap:10px;padding:20px">{badge(i, k, 32)}<div class="t" style="font-size:25px">{t}</div><div style="font-size:22px">{d}</div><span class="tag {"a" if k == "a" else ""}" style="margin-top:auto;align-self:flex-start;{"background:#fff" if k == "a" else ""}">{m}</span></div>' for i, k, t, d, m in cats)
    head = (f'<div class="row" style="gap:16px;font-size:23px"><span class="tag">大地震、有感地震</span>現有的自動化已可大致完成<span class="tag a" style="margin-left:18px">小地震</span>數量最多，有研究價值，需要分流</div>')
    return f'<div class="col" style="gap:18px;height:100%">{head}<div class="row" style="gap:8px">{qc}</div><div class="row" style="gap:16px;flex:1;align-items:stretch">{cc}</div></div>'


# ---------------- 第 17 頁
@slide(17, "benefit", S3, "效益的呈現", "在固定的品質關卡下，有多少事件不需要人處理")
def s18():
    cs = [("gauge", "a", "自動接受的比例", "先固定抽查錯誤率的上限，再報告通過關卡的事件占多少"), ("chart", "b", "落後量的方向", "每月的處理量是否超過每月的新增量"),
          ("eye", "", "品質由未知變為已知", "改為抽查之後，每一批資料都有錯誤率的估計"), ("layers", "", "自動化的等級", "依地震的類別列出目前的等級，見下一頁")]
    g = "".join(f'<div class="card {k} col" style="gap:10px;padding:22px 24px"><div class="row" style="gap:16px">{badge(i, k, 34)}<div class="t" style="font-size:29px">{t}</div></div><div style="font-size:24px;line-height:1.45">{d}</div></div>' for i, k, t, d in cs)
    note = (f'<div class="card row" style="gap:14px;padding:12px 20px">{ic("warn", 28, MUTED)}<span style="font-size:22px">準確率以人工結果為正確答案，人工結果可能含補上的到時，數字難以解讀。同仁修正的筆數只用來比較權重的版本。</span></div>')
    return f'<div class="col" style="gap:16px;height:100%"><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;flex:1;grid-auto-rows:1fr">{g}</div>{note}</div>'


# ---------------- 第 18 頁
@slide(18, "levels", S3, "自動化的等級", "工作的結構在人力與事件數脫鉤之後才改變")
def s19():
    lv = [("0", "逐站挑波"), ("1", "帶入自動挑選，逐筆修改"), ("2", "逐筆審核"), ("3", "只處理存疑的事件，其餘抽查"), ("4", "訂定標準、抽查、整批重跑")]
    steps = ""
    for n, (k, t) in enumerate(lv):
        h = 110 + n * 70
        hot = n >= 3
        cur = n == 2
        bgc = ACCENT_BG if hot else ("#fff" if not cur else BLUE_BG)
        bd = ACCENT if hot else (BLUE if cur else LINE)
        tag = f'<span class="tag b" style="background:#fff">本週</span>' if cur else ""
        steps += (f'<div class="col" style="flex:1;justify-content:flex-end"><div class="col" style="height:{h}px;background:{bgc};border:2px solid {bd};border-radius:12px 12px 0 0;padding:14px;gap:6px">'
                  f'<div style="font-size:44px;font-weight:700;color:{ACCENT_D if hot else BLUE_D};line-height:1">{k}</div><div style="font-size:22px;font-weight:600;line-height:1.35">{t}</div>{tag}</div></div>')
    brace = (f'<div class="row" style="gap:10px;margin-top:10px"><div class="col" style="flex:3;align-items:center;border-top:3px solid {BLUE};padding-top:8px;font-size:23px;color:{BLUE_D};font-weight:600">人力與事件數成正比｜量的改變</div>'
             f'<div class="col" style="flex:2;align-items:center;border-top:3px solid {ACCENT};padding-top:8px;font-size:23px;color:{ACCENT_D};font-weight:600">人力與事件數脫鉤｜結構的改變</div></div>')
    why = [("users", "抽查的樣本數隨批量成長得很慢"), ("refresh", "整年的資料可以在數天內重跑"), ("repeat", "同一份資料重跑的結果相同")]
    wy = "".join(f'<div class="row" style="gap:10px;font-size:23px">{ic(i, 28, ACCENT_D)}{t}</div>' for i, t in why)
    return (f'<div class="col" style="gap:14px;height:100%"><div class="row" style="gap:12px;align-items:flex-end;flex:1;border-bottom:3px solid {MUTED}">{steps}</div>{brace}'
            f'<div class="card a row" style="gap:30px;padding:12px 22px;justify-content:space-around">{wy}</div></div>')


# ---------------- 第 19 頁
@slide(19, "supervisor", S3, "監督角色的條件", "人由逐筆審核改為監督，模型需要的條件與整體準確率無關")
def s20():
    cs = [("target", "信心能區分對錯", "錯誤集中在信心低的部分"), ("radio", "事件的偵測率要高", "沒有候選的地震無從補救，需要獨立來源互補"),
          ("gauge", "自動接受的比例有下限", "1 − 人力產能 ÷ 每月需要處理的量"), ("warn", "失效可以察覺", "抽查不通過時整批降級重審")]
    cc = "".join(f'<div class="card row" style="gap:14px;padding:14px 18px">{badge(i, "a", 28)}<div><div style="font-size:24px;font-weight:700">{t}</div><div class="s" style="font-size:21px">{d}</div></div></div>' for i, t, d in cs)
    W, H = 600, 300
    bars = [("低", .33), ("", .2), ("", .1), ("", .04), ("高", .01)]
    bw = 80
    bs = "".join(f'<rect x="{70 + n * (bw + 25)}" y="{H - 50 - v * 600:.0f}" width="{bw}" height="{v * 600:.0f}" fill="{ACCENT if n < 2 else BLUE}" rx="6"/>'
                 f'<text x="{70 + n * (bw + 25) + bw / 2}" y="{H - 22}" text-anchor="middle" font-size="20" fill="{MUTED}">{lab}</text>' for n, (lab, v) in enumerate(bars))
    chart = (f'<svg width="{W}" height="{H}"><line x1="60" y1="{H - 50}" x2="{W}" y2="{H - 50}" stroke="{MUTED}" stroke-width="2"/>{bs}'
             f'<text x="{W / 2 + 30}" y="{H}" text-anchor="middle" font-size="20" fill="{MUTED}">模型給的信心</text>'
             f'<text x="60" y="22" font-size="20" fill="{MUTED}">與人工相差較大的比例</text></svg>')
    cov = (f'<div class="col" style="gap:6px"><div style="font-size:22px;font-weight:600">高信心候選涵蓋的人工事件</div><div class="row" style="height:30px;border-radius:6px;overflow:hidden">'
           f'<div style="width:25%;background:{ACCENT_D}"></div><div style="width:75%;background:{BG}"></div></div><div class="note">約四分之一，瓶頸在偵測率與涵蓋率</div></div>')
    right = f'<div class="card col" style="flex:1;gap:12px"><div class="row" style="gap:10px"><span class="t">初步試算</span><span class="tag">一天的資料，只看方向</span></div>{chart}{cov}</div>'
    return f'<div class="row" style="gap:22px;height:100%;align-items:stretch"><div class="col" style="width:640px;gap:12px">{cc}</div>{right}</div>'


# ---------------- 第 20 頁
@slide(20, "truth", S3, "正確答案的選擇", "到時是唯一直接的觀測，正確答案應以到時為準，並先確認到時的品質")
def s21():
    d = (f'<div class="row" style="gap:14px;align-items:center">'
         f'<div class="card a col" style="width:220px;align-items:center;gap:6px;padding:18px">{ic("wave", 40, ACCENT_D)}<div class="t">到時</div><span class="tag a" style="background:#fff">直接觀測</span></div>'
         f'<div class="col" style="align-items:center">{ic("plus", 30, MUTED)}</div>'
         f'<div class="card col" style="width:200px;align-items:center;gap:6px;padding:18px">{ic("layers", 40, INK)}<div class="t">速度模型</div><span class="tag">假設</span></div>{arrow(40)}'
         f'<div class="card col" style="width:170px;align-items:center;gap:6px;padding:18px">{ic("refresh", 40, INK)}<div class="t">迭代</div></div>{arrow(40)}'
         f'<div class="card b col" style="width:250px;align-items:center;gap:6px;padding:18px;border-style:dashed"><svg width="80" height="50"><ellipse cx="40" cy="25" rx="36" ry="18" fill="{BLUE_BG}" stroke="{BLUE_D}" stroke-width="2.5" stroke-dasharray="5 4"/><circle cx="40" cy="25" r="5" fill="{BLUE_D}"/></svg><div class="t">震源位置</div><span class="tag b" style="background:#fff">推得，帶有不確定度</span></div></div>')
    opts = [("filter" if "filter" in w8.ICONS else "check", "只採用清楚的到時", "做法簡單，但會排除最困難的情境"), ("users", "建立少量的精審資料", "資深同仁在沒有件數壓力下，兩人以上獨立審核"), ("shield", "以物理方法交叉驗證", "不以另一個模型判斷模型的對錯")]
    oc = "".join(icard(i, "", t, x, "flex:1", 30) for i, t, x in opts)
    return (f'<div class="col" style="gap:22px;height:100%">{d}<div class="note">地震本身也有方向性、不是一個點。模型失分的地方集中在人工也沒有把握的到時。</div>'
            f'<div class="row" style="gap:16px;flex:1;align-items:stretch">{oc}</div></div>')


# ---------------- 第 21 頁
@slide(21, "beyond", S3, "跳脫框架的方向", "交付的成果與工作的分配，也可以重新設計")
def s22():
    loop = (f'<div class="row" style="gap:12px;align-items:center;margin-top:8px">{node("layers", "落後與過去的資料", "", "", 190)}{arrow(34, ACCENT_D)}{node("bot", "固定的自動流程", "整批處理", "a", 190)}{arrow(34, ACCENT_D)}'
            f'<div class="col" style="gap:8px">' + "".join(f'<div class="card row" style="gap:10px;padding:8px 14px;font-size:22px;font-weight:600">{ic("book", 24, ACCENT_D)}研究用目錄 v{v}</div>' for v in (1, 2, 3)) + '</div></div>')
    big = (f'<div class="card a col" style="width:820px;gap:8px;padding:22px 26px"><div class="row" style="gap:12px">{ic("repeat", 34, ACCENT_D)}<span class="t" style="font-size:30px">地震目錄的再分析</span></div>'
           f'<div style="font-size:23px;line-height:1.5">比照氣象的再分析資料，以同一套流程批次處理，產出有版本的目錄。模型改進後整批重跑，人力轉為驗證與抽查。</div>{loop}</div>')
    sm = [("split", "作業目錄與研究目錄分開"), ("cube", "以三維速度模型統一定位"), ("repeat", "小地震以樣板比對與相對定位處理"),
          ("book", "人的工作改為教導系統"), ("sliders", "以定位的不確定度取代測站數量"), ("radio", "把功夫往前移到測站")]
    sc = "".join(f'<div class="card row" style="gap:12px;padding:12px 16px;font-size:24px;font-weight:600;flex:1">{ic(i, 28, BLUE_D)}{t}</div>' for i, t in sm)
    return (f'<div class="row" style="gap:22px;height:100%;align-items:stretch">{big}<div class="col" style="flex:1;gap:10px">{sc}'
            f'<div class="note" style="margin-top:auto">都還沒有評估可行性，需要署內決定</div></div></div>')


# ---------------- 第 22 頁
@slide(22, "closing", "結語", "結語", "意圖與判斷由人提出，agent 負責把意圖做成可以檢驗的結果")
def s23():
    ag = ["撰寫與修改程式，量測延遲", "依回饋連續修正並發布", "以實驗比較關聯的範圍，試跑持續訓練", "讀取手冊與法規，整理成可以對照的形式", "試算信心與錯誤的關係"]
    hu = ["以 16 分鐘為一段", "換版要經過核准", "把品質放在數量之前"]
    al = "".join(f'<div class="row" style="gap:12px;font-size:25px;padding:8px 0">{ic("check", 26, BLUE_D)}{t}</div>' for t in ag)
    hl = "".join(f'<div class="row" style="gap:12px;font-size:27px;font-weight:600;padding:10px 0">{ic("user", 28, ACCENT_D)}{t}</div>' for t in hu)
    return (f'<div class="row" style="gap:26px;height:100%;align-items:stretch">'
            f'<div class="card b col" style="flex:1;gap:4px;padding:26px"><div class="row" style="gap:12px;margin-bottom:8px">{badge("bot", "b", 34)}<span class="t" style="font-size:30px">Agent 分擔的工作</span></div>{al}</div>'
            f'<div class="card a col" style="flex:1;gap:4px;padding:26px"><div class="row" style="gap:12px;margin-bottom:8px">{badge("user", "a", 34)}<span class="t" style="font-size:30px">由人提出的判斷</span></div>{hl}'
            f'<div style="font-size:23px;line-height:1.5;margin-top:auto">品質先於數量來自與同仁討論實際的工作量，這是程式本身無法提供的資訊</div></div></div>')


SECTIONS = [("一", "工具配合人", "同仁的操作時間很短，又有既定的交接方式，工具如何配合", "users"),
            ("二", "模型的更新可以信任", "每次更新都有依據、可以退回", "shield"),
            ("三", "重新評估", "加快每個事件的處理，是否解決了業務真正的問題", "search")]


def main():
    w8.TMP = HERE / ".html"
    w8.TMP.mkdir(exist_ok=True)
    want = [int(a) for a in sys.argv[1:]] or sorted(SLIDES)
    if not sys.argv[1:]:
        for k, sec in enumerate(SECTIONS, 1):
            src = w8.TMP / f"w9-sec{k}.html"
            src.write_text(w8.section_html(*sec), encoding="utf-8")
            shot(src, HERE / f"w9-sec{k}.png")
    for no in want:
        name, sec, title, msg, fn = SLIDES[no]
        head = f'<div class="sec">{sec}</div><h1>{title}</h1><div class="msg">{msg}</div>' if title else ""
        html = (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>{head}'
                f'<div class="body">{fn()}</div><div class="foot"><span>第九週｜Agent 時代的知識工作</span><span>{no}</span></div>')
        src = w8.TMP / f"w9-{no:02d}.html"
        src.write_text(html, encoding="utf-8")
        out = HERE / f"w9-{no:02d}-{name}.png"
        shot(src, out)
        print(out.name)


if __name__ == "__main__":
    main()
