#!/usr/bin/env python3
"""第七週概念圖：以程式產生 SVG，再以 rsvg-convert 輸出 PNG。

用法：python3 assets/week7-diagrams/draw.py
色票與字型沿用 assets/week5-diagrams/README.md，繪圖方式同 assets/week6-diagrams/draw.py。
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DARK, MUTED, ACCENT, BLUE, GREY, IVORY = "#2A2623", "#6B6560", "#BE8979", "#A6B7BA", "#D8D2C9", "#F5F2EC"
PINK, BLUEBG = "#F6EAE5", "#EAF0F1"
FONT = "PingFang TC, Hiragino Sans GB, sans-serif"


class Fig:
    def __init__(self, w, h):
        self.w, self.h, self.items = w, h, []

    def add(self, s):
        self.items.append(s)

    def rect(self, x, y, w, h, fill=IVORY, stroke=GREY, dash=False, rx=16, sw=3):
        d = ' stroke-dasharray="12 8"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def card(self, x, y, w, h, title, subs=(), fill=IVORY, stroke=GREY, tsize=30, ssize=24):
        """標題加一至兩行說明的方塊。"""
        self.rect(x, y, w, h, fill=fill, stroke=stroke)
        lines = [(title, tsize, True, DARK)] + [(s, ssize, False, MUTED) for s in subs]
        heights = [sz * 1.35 for _, sz, _, _ in lines]
        y0 = y + h / 2 - sum(heights) / 2
        for (t, sz, bold, color), lh in zip(lines, heights):
            self.text(x + w / 2, y0 + lh / 2, t, size=sz, bold=bold, color=color)
            y0 += lh

    def text(self, x, y, s, size=26, bold=False, color=DARK, anchor="middle"):
        wt = ' font-weight="600"' if bold else ""
        self.add(f'<text x="{x}" y="{y:.1f}" font-size="{size}" fill="{color}"{wt} '
                 f'text-anchor="{anchor}" dominant-baseline="central">{s}</text>')

    def arrow(self, pts, color=MUTED, dash=False, sw=3):
        d = ' stroke-dasharray="12 8"' if dash else ""
        mk = "ahr" if color == ACCENT else "ah"
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{sw}"{d} '
                 f'marker-end="url(#{mk})"/>')

    def save(self, name):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" font-family="{FONT}">\n<defs>\n'
                f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker>\n'
                f'<marker id="ahr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ACCENT}"/></marker>\n'
                f'</defs>\n<rect width="{self.w}" height="{self.h}" fill="#FFFFFF"/>\n')
        svg = HERE / f"{name}.svg"
        svg.write_text(head + "\n".join(self.items) + "\n</svg>\n", encoding="utf-8")
        subprocess.run(["rsvg-convert", "-w", str(int(self.w * 1.2)), str(svg), "-o",
                        str(HERE / f"{name}.png")], check=True)
        print(name)


def agent_remote_test():
    """Agent 操作測試機：以 Agent 為主角，使用者在 Mac 之外交辦與檢查，Agent 經私人網路操作 Windows 測試機。"""
    f = Fig(1600, 920)
    # 使用者：在兩台電腦之外
    f.card(30, 350, 190, 200, "使用者", ["提出需求", "檢查結果", "作出決定"], tsize=34)
    # 三個區域
    f.rect(300, 60, 560, 740, fill="none", dash=True)
    f.text(580, 100, "Mac：開發機", size=32, bold=True)
    f.text(580, 140, "Agent 在這裡工作，討論與紀錄集中於此", size=24, color=MUTED)
    f.rect(890, 60, 210, 740, fill="none", stroke=BLUE, dash=True)
    f.text(995, 100, "連線", size=28, bold=True)
    f.text(995, 140, "Thunderbolt 直連", size=22, color=MUTED)
    f.text(995, 172, "或 Tailscale", size=22, color=MUTED)
    f.text(995, 204, "SSH 金鑰登入", size=22, color=MUTED)
    f.rect(1130, 60, 440, 740, fill="none", dash=True)
    f.text(1350, 100, "Windows：測試機", size=32, bold=True)
    f.text(1350, 140, "舊程式只能在 Windows 執行", size=24, color=MUTED)
    f.text(1350, 172, "只負責執行，不執行 Agent", size=24, color=MUTED)
    # Mac：專案資料夾在上，Agent 在中，瀏覽器在下
    f.card(330, 180, 500, 90, "專案資料夾", ["程式、規則、工作說明檔，以 git 管理"])
    f.rect(330, 340, 500, 220, fill=PINK, stroke=ACCENT, sw=5)
    f.text(580, 400, "Agent", size=42, bold=True)
    f.text(580, 462, "修改程式、送到測試機", size=26)
    f.text(580, 506, "遠端執行測試、回報結果", size=26)
    f.card(330, 660, 500, 100, "瀏覽器", ["測試機的網頁轉回此處"])
    f.arrow([(580, 340), (580, 276)])
    f.text(610, 305, "修改、提交", size=22, color=MUTED, anchor="start")
    # 使用者與 Agent、瀏覽器
    f.arrow([(220, 410), (324, 410)])
    f.text(260, 390, "交辦", size=22, color=MUTED)
    f.arrow([(330, 480), (226, 480)], color=ACCENT)
    f.text(260, 460, "回報", size=22, color=ACCENT)
    f.arrow([(330, 710), (125, 710), (125, 556)])
    f.text(228, 690, "檢視", size=22, color=MUTED)
    # Windows：git 副本在上，執行環境在中，舊程式在下
    f.card(1160, 325, 380, 110, "測試用的 git 副本", ["只接收已提交的版本"], fill=BLUEBG, stroke=BLUE)
    f.card(1160, 465, 380, 110, "Python 執行環境", ["執行測試、啟動網頁"], fill=BLUEBG, stroke=BLUE)
    f.card(1160, 660, 380, 100, "舊程式", ["與新的規則逐筆比對"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(1350, 575), (1350, 654)])
    f.text(1370, 615, "比對", size=22, color=MUTED, anchor="start")
    # Agent 發起的跨機器動作
    f.arrow([(830, 380), (1154, 380)], color=ACCENT, sw=4)
    f.text(1000, 358, "git push", size=24, color=ACCENT)
    f.arrow([(830, 520), (1154, 520)], color=ACCENT, sw=4)
    f.text(1000, 498, "SSH 遠端執行", size=24, color=ACCENT)
    f.arrow([(1160, 560), (1050, 560), (1050, 730), (836, 730)], dash=True)
    f.text(968, 708, "SSH 轉接網頁", size=22, color=MUTED)
    f.text(800, 862, "使用者只在 Mac 上交辦與檢查；涉及 Windows 的每一個動作都由 Agent 經 SSH 執行，使用者不必親自操作測試機。",
           size=26, color=MUTED)
    f.save("w7-agent-remote-test")


def route():
    """第 3 頁：五段路線。"""
    f = Fig(1600, 300)
    steps = [("一", "兩個題目與", "整體架構"), ("二", "從投影片到", "每個步驟"), ("三", "規則與來源", "的大表"),
             ("四", "證據鏈", "與測試"), ("五", "從原型到", "正式工具")]
    w, gap, x0 = 260, 60, 30
    for i, (n, a, b) in enumerate(steps):
        x = x0 + i * (w + gap)
        hl = i in (2, 3)
        f.rect(x, 60, w, 180, fill=PINK if hl else IVORY, stroke=ACCENT if hl else GREY)
        f.text(x + w / 2, 100, n, size=30, bold=True, color=ACCENT if hl else MUTED)
        f.text(x + w / 2, 155, a, size=28, bold=True)
        f.text(x + w / 2, 195, b, size=28, bold=True)
        if i < 4:
            f.arrow([(x + w + 6, 150), (x + w + gap - 6, 150)])
    f.text(800, 275, "第三、四段是本週的重點", size=22, color=ACCENT)
    f.save("w7-03-route")


def dependency():
    """第 6 頁：規則自成一塊，兩端依賴規則，以檔案相接。"""
    f = Fig(1600, 760)
    f.card(80, 60, 420, 150, "定位端", ["翻新後的定位軟體", "挑波時攔截"], fill=BLUEBG, stroke=BLUE)
    f.card(1100, 60, 420, 150, "檢查端", ["送出前的預檢關卡", "送出前把關"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(506, 120), (1094, 120)], sw=4)
    f.text(800, 92, "波形檔、定位結果檔", size=26, color=MUTED)
    f.text(800, 150, "兩端只以既有的檔案格式相接", size=22, color=MUTED)
    f.card(560, 330, 480, 170, "檢查程式", ["規則庫：規則只有一份", "加上依規則執行的程式"], fill=PINK, stroke=ACCENT, tsize=34)
    f.arrow([(290, 216), (290, 415), (554, 415)], color=ACCENT, sw=4)
    f.arrow([(1310, 216), (1310, 415), (1046, 415)], color=ACCENT, sw=4)
    f.text(310, 300, "調用", size=24, color=ACCENT, anchor="start")
    f.text(1290, 300, "調用", size=24, color=ACCENT, anchor="end")
    f.text(800, 540, "規則不依賴兩端，兩端依賴規則", size=26, bold=True, color=ACCENT)
    f.rect(80, 600, 1440, 120, fill=IVORY, stroke=GREY, dash=True)
    f.text(800, 640, "共用資料夾", size=28, bold=True)
    f.text(800, 685, "測站表、速度模型、定位計算程式：兩端都依賴，本身就是規格的一部分", size=22, color=MUTED)
    f.save("w7-06-dependency")


def same_result():
    """第 8 頁：同一筆資料經過新舊流程，結果必須相同。"""
    f = Fig(1600, 520)
    f.card(40, 170, 280, 170, "同一筆", ["定位結果檔"], tsize=32)
    f.card(480, 60, 380, 140, "原本的程式", ["舊的檢查程式"], fill=IVORY)
    f.card(480, 310, 380, 140, "新的程式", ["依規則庫執行"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(326, 230), (474, 140)])
    f.arrow([(326, 280), (474, 380)])
    f.card(1020, 60, 220, 140, "結果", [], tsize=30)
    f.card(1020, 310, 220, 140, "結果", [], tsize=30)
    f.arrow([(866, 130), (1014, 130)])
    f.arrow([(866, 380), (1014, 380)])
    f.rect(1300, 120, 260, 270, fill=PINK, stroke=ACCENT)
    f.text(1430, 190, "逐筆相同", size=30, bold=True, color=ACCENT)
    f.text(1430, 255, "不同時", size=24, color=MUTED)
    f.text(1430, 295, "必須找出原因", size=24, color=MUTED)
    f.text(1430, 335, "並歸類", size=24, color=MUTED)
    f.arrow([(1246, 130), (1294, 180)], color=ACCENT)
    f.arrow([(1246, 380), (1294, 330)], color=ACCENT)
    f.text(800, 495, "替換一支程式之前，先查清它對定位結果檔做的每一項改變", size=24, color=MUTED)
    f.save("w7-08-same-result")


def counts():
    """第 20 頁：一個月資料不通過的事件數。"""
    f = Fig(1600, 470)
    rows = [(324, "關卡加入判定時", DARK), (315, "入庫的篩選改為提示", MUTED), (101, "物理上可能的情形改為提示", ACCENT)]
    x0, maxw = 520, 900
    for i, (n, label, c) in enumerate(rows):
        y = 50 + i * 130
        f.text(490, y + 45, label, size=28, anchor="end", color=DARK)
        f.rect(x0, y, maxw * n / 324, 90, fill=PINK if c == ACCENT else IVORY, stroke=c, rx=8)
        f.text(x0 + maxw * n / 324 + 20, y + 45, f"{n} 筆", size=32, bold=True, color=c, anchor="start")
    f.text(800, 445, "一個月約一千筆資料；減少的部分改列為提示，仍交給承辦確認", size=24, color=MUTED)
    f.save("w7-20-counts")


def single_source():
    """第 22 頁：同一份規則檔產生各處。"""
    f = Fig(1600, 560)
    f.card(60, 170, 400, 220, "規則檔", ["檢查什麼、門檻代號", "方向、等級、來源"], fill=PINK, stroke=ACCENT, tsize=36)
    outs = [("檢查程式", "判斷函式讀取門檻，不寫死數字"), ("說明頁", "每條規則的作業標準"),
            ("大表與門檻圖", "來源並排，可通過範圍"), ("測試", "門檻兩邊自動產生案例")]
    for i, (t, sub) in enumerate(outs):
        y = 20 + i * 132
        f.card(820, y, 720, 110, t, [sub], fill=BLUEBG, stroke=BLUE, tsize=28, ssize=22)
        f.arrow([(466, 280), (640, 280), (640, y + 55), (814, y + 55)], color=ACCENT)
    f.text(260, 440, "修改一次，各處同時更新", size=26, bold=True, color=ACCENT)
    f.save("w7-22-single-source")


def release():
    """第 28 頁：只公開版本資訊，更新套件另行交付。"""
    f = Fig(1600, 470)
    f.card(30, 160, 260, 140, "推上版本標籤", [], tsize=28)
    f.card(370, 160, 300, 140, "雲端自動流程", ["測試、打包"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(296, 230), (364, 230)])
    f.card(760, 30, 380, 150, "版本資訊", ["發布到公開網站"], fill=BLUEBG, stroke=BLUE)
    f.card(760, 290, 380, 150, "更新套件", ["不公開：含內部業務的整理"], fill=PINK, stroke=ACCENT)
    f.arrow([(676, 200), (754, 110)])
    f.arrow([(676, 260), (754, 360)], color=ACCENT)
    f.card(1230, 30, 340, 150, "程式線上檢查", ["只通知有新版本"])
    f.card(1230, 290, 340, 150, "另行交付", ["使用者選擇檔案更新"])
    f.arrow([(1146, 105), (1224, 105)])
    f.arrow([(1146, 365), (1224, 365)], color=ACCENT)
    f.save("w7-28-release")


def icon(f, name, x, y, size, color):
    """嵌入 Tabler 圖示（assets/week7-icons/，MIT）：取 SVG 內的 path 等元素，縮放到 size。"""
    import re
    src = (HERE.parent / "week7-icons" / f"{name}.svg").read_text(encoding="utf-8")
    body = "".join(m for m in re.findall(r"<(?:path|circle|rect|line|polyline)[^>]*/>", src)
                   if 'stroke="none"' not in m)
    k = size / 24
    f.add(f'<g transform="translate({x},{y}) scale({k})" fill="none" stroke="{color}" stroke-width="1.8" '
          f'stroke-linecap="round" stroke-linejoin="round">{body}</g>')


def shared_folder():
    """第 5 頁：共用資料夾的七類內容，各附圖示；決定定位結果的三類以強調色標出。"""
    f = Fig(1600, 640)
    cats = [("map-pin", "定位計算程式", "三代：互動版、命令列版、三維", True),
            ("broadcast", "測站表", "兩代：舊表 2010 年停止維護", True),
            ("stack-2", "速度模型", "一維與三維的速度模型", True),
            ("activity", "規模與強震", "規模計算、場址係數、強震預測", False),
            ("wave-sine", "波形與格式轉換", "波形解讀、格式轉換、訊號處理", False),
            ("map-2", "地圖與繪圖", "行政區界、海岸、斷層、地形", False),
            ("folders", "其他", "參考目錄、範例檔、資料庫、字型", False)]
    w, h, gap = 360, 230, 40
    for i, (ic, title, sub, key) in enumerate(cats):
        row, col = divmod(i, 4)
        n = 4 if row == 0 else 3
        x0 = (1600 - (n * w + (n - 1) * gap)) / 2
        x, y = x0 + col * (w + gap), 30 + row * (h + 50)
        f.rect(x, y, w, h, fill=PINK if key else IVORY, stroke=ACCENT if key else GREY)
        f.add(f'<circle cx="{x + w / 2}" cy="{y + 62}" r="40" fill="#FFFFFF" stroke="{ACCENT if key else GREY}" stroke-width="3"/>')
        icon(f, ic, x + w / 2 - 24, y + 38, 48, ACCENT if key else MUTED)
        f.text(x + w / 2, y + 140, title, size=30, bold=True)
        f.text(x + w / 2, y + 185, sub, size=21, color=MUTED)
    f.text(800, 612, "強調色的三類決定了定位的結果，也是檢查規則的依據", size=24, color=ACCENT)
    f.save("w7-05-shared-folder")


def program_level():
    """第 9 頁：查到程式的層次。文件、原始碼、實際執行三層，越往下越接近實際；
    Agent 依程式有無原始碼選擇調查方式，查到的實際行為保存下來，作為重構或重寫後比對的標準。"""
    f = Fig(1600, 640)
    layers = [("文件", "訓練投影片、說明文件", IVORY, GREY),
              ("原始碼", "程式實際寫的判斷", BLUEBG, BLUE),
              ("實際執行", "舊程式跑出來的結果", PINK, ACCENT)]
    for i, (t, sub, fill, stroke) in enumerate(layers):
        y = 40 + i * 170
        f.card(60, y, 420, 130, t, [sub], fill=fill, stroke=stroke, tsize=32, ssize=22)
    f.arrow([(520, 60), (520, 470)], color=ACCENT, sw=4)
    f.text(545, 95, "越往下", size=24, color=ACCENT, anchor="start")
    f.text(545, 130, "越接近實際", size=24, color=ACCENT, anchor="start")
    # Agent 的兩種調查方式
    f.card(760, 180, 380, 130, "有原始碼", ["Agent 讀原始碼，對照文件"], fill=BLUEBG, stroke=BLUE)
    f.card(760, 350, 380, 130, "只有執行檔", ["Agent 在測試機執行、觀察"], fill=PINK, stroke=ACCENT)
    f.arrow([(1146, 245), (1240, 245), (1240, 330)])
    f.arrow([(1146, 415), (1240, 415), (1240, 360)])
    f.arrow([(540, 275), (754, 245)], dash=True)
    f.arrow([(540, 445), (754, 415)], dash=True)
    f.card(1280, 250, 290, 200, "保存行為", ["作為之後比對的標準", "（特性測試）"], fill=IVORY, stroke=ACCENT)
    f.arrow([(1236, 345), (1274, 345)], color=ACCENT)
    f.text(800, 600, "重構或重寫之前，先把舊程式實際的行為保存下來；文件與程式不一致時，以實際執行為準",
           size=24, color=MUTED)
    f.save("w7-09-program-level")


def slide_walkthrough():
    """第 7 頁：以訓練投影片為線索，沿著原本的流程走一遍，標出每一步是人工還是程式檢查。"""
    f = Fig(1600, 600)
    HUMAN, PROG = (PINK, ACCENT), (BLUEBG, BLUE)
    groups = [("第一步", [("檢視波形，刪除", "沒有地震的檔案", [HUMAN])]),
              ("第二步", [("執行檢查程式", "產生錯誤清單", [PROG]),
                          ("逐項判讀", "錯誤清單", [HUMAN]),
                          ("依時間排序", "逐筆檢視", [PROG, HUMAN])]),
              ("第三步", [("篩選範圍", "測站數、相位數", [PROG]),
                          ("比對時間", "相近的事件", [PROG]),
                          ("入庫、備份", "回報", [HUMAN])])]
    # 上方：投影片是線索
    f.rect(40, 30, 1520, 70, fill=IVORY, stroke=GREY, rx=12)
    icon(f, "presentation", 70, 47, 36, MUTED)
    f.text(125, 65, "訓練投影片：三大步驟是走一遍的線索", size=26, bold=True, anchor="start")
    w, gap, x = 180, 20, 60
    centers = []
    for gname, steps in groups:
        gw = len(steps) * w + (len(steps) - 1) * gap
        f.rect(x - 10, 130, gw + 20, 330, fill="none", stroke=GREY, dash=True, rx=14)
        f.text(x + gw / 2, 160, gname, size=26, bold=True, color=MUTED)
        for i, (a, b, kinds) in enumerate(steps):
            sx = x + i * (w + gap)
            fill, stroke = kinds[0]
            f.rect(sx, 190, w, 170, fill=fill, stroke=stroke)
            for j, (kf, ks) in enumerate(kinds):
                ic = "user" if (kf, ks) == HUMAN else "terminal-2"
                icon(f, ic, sx + w / 2 - 22 * len(kinds) + 44 * j, 202, 36, ks)
            f.text(sx + w / 2, 275, a, size=22, bold=True)
            f.text(sx + w / 2, 310, b, size=20, color=MUTED)
            centers.append(sx + w / 2)
        x += gw + 50
    for c1, c2 in zip(centers, centers[1:]):
        f.arrow([(c1 + w / 2 + 2, 275), (c2 - w / 2 - 4, 275)])
    # 第二步修正後重複
    f.arrow([(centers[3], 366), (centers[3], 420), (centers[1], 420), (centers[1], 366)], color=ACCENT, dash=True)
    f.text((centers[1] + centers[3]) / 2, 442, "修正後重複第二步", size=20, color=ACCENT)
    # 圖例
    f.rect(470, 505, 30, 30, fill=PINK, stroke=ACCENT, rx=6)
    f.text(512, 520, "人工檢查", size=22, anchor="start")
    f.rect(690, 505, 30, 30, fill=BLUEBG, stroke=BLUE, rx=6)
    f.text(732, 520, "程式檢查", size=22, anchor="start")
    f.text(890, 520, "逐一記下每一步讀了什麼、怎麼判斷、門檻多少", size=22, color=MUTED, anchor="start")
    f.save("w7-07-slide-walkthrough")


def rea_workflow():
    """第 10 頁（補充）：REA 的運作方式。依專案說明與 InfoQ 報導整理，開發者尚未實際試用。
    Agent 經 MCP 使用反組譯工具檢視執行檔，反覆追蹤與驗證假設，最後重建行為相同的程式並以測試和原程式比對。"""
    f = Fig(1200, 900)
    f.card(40, 60, 300, 140, "執行檔", ["只有執行檔，沒有原始碼"], fill=IVORY, stroke=GREY)
    f.card(450, 60, 300, 140, "反組譯工具", ["Ghidra、IDA 等"], fill=BLUEBG, stroke=BLUE)
    f.card(860, 60, 300, 140, "Agent", ["Claude Code、Codex 等"], fill=PINK, stroke=ACCENT)
    f.arrow([(346, 130), (444, 130)])
    f.text(395, 108, "分析", size=22, color=MUTED)
    f.arrow([(756, 115), (854, 115)], color=ACCENT)
    f.arrow([(854, 150), (756, 150)], color=ACCENT)
    f.text(805, 95, "MCP", size=22, bold=True, color=ACCENT)
    steps = [("1", "檢視程式", "查詢函式與呼叫關係"), ("2", "追蹤行為", "從想了解的功能往下追"),
             ("3", "驗證假設", "提出假設，回到執行檔確認"), ("4", "重建行為", "寫出行為相同的程式")]
    for i, (n, t, sub) in enumerate(steps):
        y = 260 + i * 120
        f.rect(560, y, 600, 96, fill="#FFFFFF", stroke=ACCENT if n in "34" else GREY)
        f.add(f'<circle cx="610" cy="{y + 48}" r="24" fill="{ACCENT}"/>')
        f.text(610, y + 48, n, size=24, bold=True, color="#FFFFFF")
        f.text(660, y + 33, t, size=26, bold=True, anchor="start")
        f.text(660, y + 68, sub, size=21, color=MUTED, anchor="start")
        if i < 3:
            f.arrow([(860, y + 98), (860, y + 118)])
    f.arrow([(1010, 214), (1010, 254)], color=ACCENT)
    f.arrow([(1166, 548), (1185, 548), (1185, 428), (1166, 428)], color=ACCENT, dash=True)
    f.text(1150, 488, "反覆", size=20, color=ACCENT, anchor="end")
    # 比對
    f.card(40, 720, 500, 130, "以測試與原程式比對", ["重建的程式與執行檔，結果逐一相同"], fill=IVORY, stroke=ACCENT)
    f.arrow([(556, 680), (290, 680), (290, 714)], color=ACCENT)
    f.arrow([(190, 714), (190, 206)], dash=True)
    f.text(205, 460, "對照", size=22, color=MUTED, anchor="start")
    f.text(850, 800, "重建的是行為，不是原始碼", size=24, bold=True, color=ACCENT)
    f.text(850, 840, "依專案說明整理，開發者尚未實際試用", size=20, color=MUTED)
    f.save("w7-10-rea-workflow")


def agent_survey():
    """第 13 頁：人讀不完這麼多來源，改由人指揮多個 Agent 平行調查；結果不夠時回去再調查一次，
    條目回到原文核對，最後由人決定去留。"""
    f = Fig(1600, 720)
    # 左：來源
    f.rect(30, 150, 300, 380, fill=IVORY, stroke=GREY)
    for i in range(4):
        icon(f, "file-text", 70 + i * 58, 190, 44, MUTED)
    f.text(180, 300, "18 個來源", size=34, bold=True)
    f.text(180, 350, "舊程式、投影片、", size=22, color=MUTED)
    f.text(180, 385, "文件、紙本清單", size=22, color=MUTED)
    f.text(180, 460, "人一個個讀不完", size=24, bold=True, color=ACCENT)
    # 上：開發者指揮
    f.rect(600, 20, 400, 110, fill=PINK, stroke=ACCENT)
    icon(f, "user", 630, 48, 52, ACCENT)
    f.text(700, 60, "開發者", size=30, bold=True, anchor="start")
    f.text(700, 100, "訂定格式，分派來源", size=22, color=MUTED, anchor="start")
    f.arrow([(800, 136), (800, 196)], color=ACCENT, sw=4)
    f.text(815, 165, "指揮", size=22, color=ACCENT, anchor="start")
    # 中：多個 Agent
    for i in range(4):
        y = 205 + i * 85
        f.rect(560, y, 480, 70, fill=BLUEBG, stroke=BLUE, rx=12)
        icon(f, "robot", 580, y + 15, 40, BLUE)
        f.text(640, y + 35, f"Agent {i + 1}：逐條列出判斷條件", size=22, anchor="start")
    f.arrow([(336, 340), (554, 340)])
    f.text(445, 315, "平行閱讀", size=22, color=MUTED)
    # 右：條目與人的決定
    f.rect(1170, 205, 400, 120, fill=IVORY, stroke=GREY)
    icon(f, "list-check", 1195, 237, 52, MUTED)
    f.text(1265, 248, "672 個條目", size=30, bold=True, anchor="start")
    f.text(1265, 290, "記錄原文位置與門檻", size=21, color=MUTED, anchor="start")
    f.arrow([(1046, 340), (1100, 340), (1100, 265), (1164, 265)])
    f.rect(1170, 400, 400, 200, fill=PINK, stroke=ACCENT)
    icon(f, "user", 1195, 420, 44, ACCENT)
    f.text(1255, 442, "人決定去留", size=28, bold=True, anchor="start")
    for j, t in enumerate(["不納入的理由", "待決定的項目", "不一致的數值送會議"]):
        f.text(1200, 495 + j * 34, "・" + t, size=21, color=DARK, anchor="start")
    f.arrow([(1370, 331), (1370, 394)], color=ACCENT)
    # 回去再調查
    f.arrow([(1170, 300), (1120, 300), (1120, 640), (800, 640), (800, 551)], color=ACCENT, dash=True, sw=3)
    f.text(960, 668, "漏掉或讀錯：回到原文核對，再調查一次（第二輪重掃）", size=22, color=ACCENT)
    f.save("w7-13-agent-survey")


def classify_by_object():
    """第 14 頁：依定位結果檔上被檢查的對象分成 9 個項目（左，3×3 圖示卡片）；
    偵測與處理分開，重跑與入庫分流另列兩組規則（右）。"""
    f = Fig(1600, 760)
    items = [("file-code", "檔案格式"), ("clock", "發震時間"), ("map-pin", "震央位置"),
             ("arrow-bar-to-down", "震源深度"), ("chart-bar", "規模"), ("hand-click", "挑波"),
             ("broadcast", "測站與資料量"), ("target", "定位品質"), ("database", "事件與入庫")]
    f.text(560, 30, "檢查規則：依被檢查的對象分成 9 個項目", size=26, bold=True)
    w, h, gx, gy, x0, y0 = 320, 180, 30, 30, 60, 70
    for i, (ic, t) in enumerate(items):
        r, c = divmod(i, 3)
        x, y = x0 + c * (w + gx), y0 + r * (h + gy)
        f.rect(x, y, w, h, fill=IVORY, stroke=GREY)
        f.add(f'<circle cx="{x + w / 2}" cy="{y + 65}" r="40" fill="#FFFFFF" stroke="{ACCENT}" stroke-width="3"/>')
        icon(f, ic, x + w / 2 - 24, y + 41, 48, ACCENT)
        f.text(x + w / 2, y + 140, t, size=28, bold=True)
    # 右：處理另列
    rx = 1150
    f.text(rx + 200, 30, "處理另列兩組規則", size=26, bold=True, color=MUTED)
    for j, (ic, t, sub) in enumerate([("refresh", "重跑", "觸發重新定位的條件"),
                                      ("arrows-split", "入庫分流", "決定資料的去向")]):
        y = 70 + j * 300
        f.rect(rx, y, 400, 270, fill=BLUEBG, stroke=BLUE)
        f.add(f'<circle cx="{rx + 200}" cy="{y + 80}" r="44" fill="#FFFFFF" stroke="{BLUE}" stroke-width="3"/>')
        icon(f, ic, rx + 200 - 26, y + 54, 52, BLUE)
        f.text(rx + 200, y + 165, t, size=30, bold=True)
        f.text(rx + 200, y + 210, sub, size=22, color=MUTED)
    f.add(f'<line x1="{rx - 50}" y1="70" x2="{rx - 50}" y2="670" stroke="{GREY}" stroke-width="3" stroke-dasharray="10 8"/>')
    f.text(800, 725, "同一件事只占一列；一條規則只檢查一件事、只有一個等級；名稱不寫門檻", size=22, color=MUTED)
    f.save("w7-14-classify")


if __name__ == "__main__":
    agent_remote_test()
    route()
    dependency()
    same_result()
    counts()
    single_source()
    release()
    shared_folder()
    program_level()
    slide_walkthrough()
    rea_workflow()
    agent_survey()
    classify_by_object()
