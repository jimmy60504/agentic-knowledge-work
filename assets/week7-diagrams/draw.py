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


if __name__ == "__main__":
    agent_remote_test()
    route()
    dependency()
    same_result()
    counts()
    single_source()
    release()
