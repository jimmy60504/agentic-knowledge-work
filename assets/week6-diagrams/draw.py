#!/usr/bin/env python3
"""第六週概念圖：以程式產生 SVG，再以 rsvg-convert 輸出 PNG。

用法：python3 assets/week6-diagrams/draw.py
色票與字型沿用 assets/week5-diagrams/README.md。
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

    def box(self, x, y, w, h, lines, fill=IVORY, stroke=GREY, size=30, bold=True, color=DARK,
            dash=False, rx=16, sw=3):
        d = ' stroke-dasharray="12 8"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')
        self.text(x + w / 2, y + h / 2, lines, size=size, bold=bold, color=color)

    def text(self, x, y, lines, size=26, bold=False, color=DARK, anchor="middle"):
        if isinstance(lines, str):
            lines = [lines]
        lh = size * 1.3
        y0 = y - lh * (len(lines) - 1) / 2
        wt = ' font-weight="600"' if bold else ""
        for i, ln in enumerate(lines):
            self.add(f'<text x="{x}" y="{y0 + i * lh:.1f}" font-size="{size}" fill="{color}"{wt} '
                     f'text-anchor="{anchor}" dominant-baseline="central">{ln}</text>')

    def arrow(self, pts, color=MUTED, dash=False, sw=3, label=None, lpos=None, lcolor=None,
              lsize=24):
        d = ' stroke-dasharray="12 8"' if dash else ""
        mk = "ahr" if color == ACCENT else "ah"
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{sw}"{d} '
                 f'marker-end="url(#{mk})"/>')
        if label:
            lx, ly = lpos
            self.text(lx, ly, label, size=lsize, color=lcolor or color, bold=False)

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


def rework_loop():
    """第 3 頁：交出、退回、修正、再交出的迴圈。"""
    f = Fig(1600, 560)
    f.box(120, 190, 300, 150, ["資料處理承辦"], fill=BLUEBG, stroke=BLUE)
    f.box(1180, 190, 300, 150, ["主管"], fill=BLUEBG, stroke=BLUE)
    f.box(650, 60, 300, 110, ["定位結果檔"], size=28)
    f.arrow([(420, 230), (640, 130)])
    f.arrow([(960, 130), (1180, 230)])
    f.text(800, 205, "交出", size=26, color=MUTED)
    f.arrow([(1180, 320), (960, 420), (640, 420), (420, 320)], color=ACCENT, sw=4)
    f.text(800, 455, "退回：雙方重新打開同一筆資料，說明同一個問題", size=26, color=ACCENT)
    f.text(270, 380, "修正後再交", size=24, color=MUTED)
    f.save("w6-03-rework-loop")


def current_flow():
    """第 7 頁：派發、定位、自行檢查、主管檢視、退回。"""
    f = Fig(1600, 600)
    y, h = 220, 130
    xs = [40, 340, 640, 940, 1260]
    labels = [["主管派發"], ["承辦定位"], ["產出", "定位結果檔"], ["承辦自行檢查"], ["主管檢視"]]
    for i, (x, lb) in enumerate(zip(xs, labels)):
        manual = i in (3, 4)
        f.box(x, y, 260 if i < 4 else 300, h, lb, fill=PINK if manual else IVORY,
              stroke=ACCENT if manual else GREY, dash=(i == 3))
    for a, b in [(300, 340), (600, 640), (900, 940), (1200, 1260)]:
        f.arrow([(a, y + h / 2), (b, y + h / 2)])
    f.text(170, 390, "派工網頁", size=22, color=MUTED)
    f.text(470, 390, "定位軟體", size=22, color=MUTED)
    f.text(1070, 395, ["依訓練投影片與紙本清單", "做不做、做到哪裡都靠自己"], size=22, color=ACCENT)
    f.text(1340, 395, "人工檢視", size=22, color=ACCENT)
    f.arrow([(1410, y), (1410, 110), (470, 110), (470, y)], color=ACCENT, sw=4)
    f.text(940, 80, "發現問題就退回，修正後再交", size=26, color=ACCENT)
    f.arrow([(1410, y + h), (1410, 520)])
    f.text(1490, 540, "通過", size=24, color=MUTED)
    f.save("w6-07-current-flow")


def intercept_timeline():
    """第 9 頁：送出前自己修正，與經主管退回再修正。"""
    f = Fig(1600, 620)
    f.text(40, 70, "送出前自己發現", size=28, bold=True, anchor="start")
    steps_a = [("定位", 0), ("檢查", 1), ("修正", 2), ("送出", 3), ("通過", 4)]
    for name, i in steps_a:
        x = 60 + i * 170
        f.box(x, 110, 140, 80, [name], size=26, fill=BLUEBG if name == "檢查" else IVORY,
              stroke=BLUE if name == "檢查" else GREY)
        if i:
            f.arrow([(x - 30, 150), (x, 150)])
    f.text(60 + 5 * 170 + 20, 150, "幾乎沒有等待", size=24, color=MUTED, anchor="start")

    f.text(40, 290, "經主管退回再修正", size=28, bold=True, anchor="start")
    seq = ["定位", "送出", "等待", "主管檢視", "退回", "等待", "修正", "送出", "等待", "通過"]
    x = 60
    for i, name in enumerate(seq):
        w = 175 if name == "主管檢視" else 120
        wait = name == "等待"
        f.box(x, 330, w, 80, [name], size=24, fill="#FFFFFF" if wait else (PINK if name == "退回" else IVORY),
              stroke=ACCENT if name == "退回" else GREY, dash=wait, bold=not wait,
              color=MUTED if wait else DARK)
        if i:
            f.arrow([(x - 26, 370), (x, 370)])
        x += w + 26
    f.text(800, 500, "錯誤越晚被發現，經過的傳遞越多，每一次傳遞都要等待", size=28, color=ACCENT)
    f.save("w6-09-intercept-timeline")


def single_source():
    """第 24 頁：規則整理前後（方形）。"""
    f = Fig(1000, 1000)
    f.text(500, 50, "整理之前：一條規則散在五處", size=30, bold=True)
    srcs = ["規格表", "門檻表", "設定檔", "說明文件", "程式"]
    vals = ["≤ 180", "≤ 180", "≤ 200", "≤ 180", "≤ 200"]
    for i, (s, v) in enumerate(zip(srcs, vals)):
        x = 30 + i * 192
        diff = v != "≤ 180"
        f.box(x, 100, 172, 120, [s, v], size=26, fill=PINK if diff else IVORY,
              stroke=ACCENT if diff else GREY)
    f.text(500, 260, "各處的門檻不一定相同，修改時容易漏改", size=24, color=ACCENT)
    f.add(f'<line x1="60" y1="320" x2="940" y2="320" stroke="{GREY}" stroke-width="2"/>')
    f.text(500, 370, "整理之後：一條規則一個檔案", size=30, bold=True)
    f.box(330, 420, 340, 150, ["規則檔", "門檻與說明"], fill=BLUEBG, stroke=BLUE, size=30)
    f.box(60, 690, 300, 120, ["檢查程式", "依規則檔執行"], size=26)
    f.box(640, 690, 300, 120, ["網頁說明頁", "由規則檔產生"], size=26)
    f.arrow([(420, 570), (250, 690)])
    f.arrow([(580, 570), (750, 690)])
    f.box(200, 870, 600, 100, ["來源互相矛盾時：全部列出、標明出處，交由會議定案"],
          size=24, bold=False, fill="#FFFFFF", dash=True)
    f.save("w6-24-single-source")


def trace():
    """第 26 頁：新舊編號對照與一條規則的出處（方形）。"""
    f = Fig(1000, 1000)
    f.text(500, 50, "重新編號，保留舊編號對照", size=30, bold=True)
    rows = [("舊編號", "新編號", "依據"), ("A1", "P1", "檢查對象：相位"),
            ("A2", "P2", "檢查對象：相位"), ("B4", "H1", "檢查對象：檔頭")]
    for r, row in enumerate(rows):
        y = 100 + r * 70
        for c, (cell, x, w) in enumerate(zip(row, (60, 260, 460), (200, 200, 480))):
            f.add(f'<rect x="{x}" y="{y}" width="{w}" height="70" fill="{IVORY if r == 0 else "#FFFFFF"}" '
                  f'stroke="{GREY}" stroke-width="2"/>')
            f.text(x + w / 2, y + 35, cell, size=26, bold=(r == 0), color=DARK if c < 2 or r == 0 else MUTED)
    f.text(500, 430, "舊編號是 Agent 早期整理時自訂的，並非署內代碼", size=24, color=ACCENT)
    f.add(f'<line x1="60" y1="480" x2="940" y2="480" stroke="{GREY}" stroke-width="2"/>')
    f.text(500, 530, "每一條規則標出出處（示意）", size=30, bold=True)
    f.box(300, 580, 400, 120, ["規則 P1", "相位時間的順序"], fill=BLUEBG, stroke=BLUE, size=28)
    outs = [("訓練投影片", "第 N 頁"), ("紙本清單", "第 N 項"), ("舊程式", "實際的判斷式")]
    for i, (a, b) in enumerate(outs):
        x = 40 + i * 320
        f.box(x, 820, 280, 120, [a, b], size=26)
        f.arrow([(x + 140, 820), (500, 700)])
    f.save("w6-26-trace")


def upstream():
    """第 36 頁：上游防呆與下游攔截的位置。"""
    f = Fig(1600, 560)
    xs = [(60, "定位軟體", "上游"), (480, "定位結果檔", ""), (880, "預檢", "下游"), (1260, "主管檢視", "")]
    for x, name, tag in xs:
        hl = name in ("定位軟體", "預檢")
        f.box(x, 200, 280, 130, [name], fill=BLUEBG if hl else IVORY, stroke=BLUE if hl else GREY)
    for a, b in [(340, 480), (760, 880), (1160, 1260)]:
        f.arrow([(a, 265), (b, 265)])
    f.text(200, 140, "長期：程式更新時寫入防呆", size=26, color=ACCENT, bold=True)
    f.text(230, 400, ["產出的當下就阻止錯誤", "錯誤不再產生"], size=24, color=MUTED)
    f.text(1020, 140, "目前：上傳時攔截", size=26, color=DARK, bold=True)
    f.text(1020, 390, ["減少退回", "但錯誤仍會產生"], size=24, color=MUTED)
    f.arrow([(1020, 450), (1020, 500), (90, 500), (90, 340)], dash=True)
    f.text(610, 530, "整理好的規則檔，可以作為上游更新的規格", size=24, color=MUTED)
    f.save("w6-36-upstream")


def story_loop():
    """第 17 頁：收成迴圈之後（一般說法）。"""
    f = Fig(1600, 600)
    f.box(60, 230, 260, 140, ["資料處理承辦"], fill=BLUEBG, stroke=BLUE)
    f.box(500, 60, 300, 110, ["項目清單"], size=28)
    f.box(500, 430, 300, 110, ["定位結果檔"], size=28)
    f.box(980, 230, 260, 140, ["檢查程式"], size=28)
    f.box(1340, 230, 220, 140, ["主管"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(320, 270), (500, 130)], label="1 依清單檢查", lpos=(390, 165))
    f.arrow([(980, 260), (800, 130)], label="列出問題", lpos=(920, 165))
    f.arrow([(320, 330), (500, 470)], label="2 修正", lpos=(380, 440))
    f.arrow([(800, 485), (980, 340)], label="3 再檢查", lpos=(930, 440))
    f.arrow([(1240, 300), (1340, 300)])
    f.text(1290, 400, ["沒有問題", "或轉為特殊案例", "才上交"], size=22, color=MUTED)
    f.text(650, 300, ["重複 1 至 3", "直到清單清空"], size=26, color=ACCENT, bold=True)
    f.save("w6-17-story-loop")


def gap():
    """第 18 頁：現況的缺口與錯誤流向。"""
    f = Fig(1600, 600)
    f.box(60, 220, 280, 130, ["定位軟體"], size=30)
    f.box(500, 220, 280, 130, ["定位結果檔"], size=30)
    f.box(1220, 220, 300, 130, ["主管檢視"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(340, 285), (500, 285)])
    f.text(420, 380, ["缺少防呆", "能產出簡單錯誤"], size=22, color=ACCENT)
    f.arrow([(780, 285), (1220, 285)], color=ACCENT, sw=5)
    f.text(1000, 250, "直接上交", size=26, color=ACCENT, bold=True)
    f.box(860, 400, 280, 110, ["兩支檢查程式"], dash=True, size=26, bold=False, color=MUTED, fill="#FFFFFF")
    f.arrow([(1000, 400), (1000, 310)], dash=True)
    f.text(1000, 545, "不是必經的節點，執行與否靠承辦自己想到", size=24, color=MUTED)
    f.box(820, 70, 360, 100, ["缺口：沒有攔截的位置"], fill=PINK, stroke=ACCENT, size=26)
    f.save("w6-18-gap")


def before_after():
    """第 20 頁：現況與導入後：上傳即檢查。"""
    f = Fig(1600, 640)
    f.text(40, 60, "現況", size=30, bold=True, anchor="start")
    f.box(60, 100, 260, 110, ["承辦定位"], size=28)
    f.box(460, 100, 300, 110, ["上傳到派工網頁"], size=28)
    f.box(900, 100, 260, 110, ["主管檢視"], size=28)
    f.arrow([(320, 155), (460, 155)])
    f.arrow([(760, 155), (900, 155)])
    f.box(400, 240, 420, 80, ["自行檢查：可做可不做"], dash=True, size=24, bold=False, color=MUTED, fill="#FFFFFF")
    f.text(40, 390, "導入後", size=30, bold=True, anchor="start")
    f.box(60, 430, 260, 110, ["承辦定位"], size=28)
    f.box(460, 430, 300, 110, ["上傳到派工網頁"], size=28)
    f.box(900, 430, 300, 110, ["預檢自動執行"], fill=BLUEBG, stroke=BLUE, size=28)
    f.box(1340, 430, 220, 110, ["主管檢視"], size=28)
    f.arrow([(320, 485), (460, 485)])
    f.arrow([(760, 485), (900, 485)])
    f.arrow([(1200, 485), (1340, 485)])
    f.arrow([(1050, 540), (1050, 600), (190, 600), (190, 540)], color=ACCENT)
    f.text(620, 620, "有問題先回到承辦本人修正", size=22, color=ACCENT)
    f.text(1050, 400, "成為必經的節點", size=24, color=MUTED)
    f.save("w6-20-before-after")


if __name__ == "__main__":
    for fn in (rework_loop, current_flow, intercept_timeline, single_source, trace, upstream,
               story_loop, gap, before_after):
        fn()
