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
    """Agent 操作測試機：開發機與測試機的分工，以及 Agent 經私人網路遠端執行測試。"""
    f = Fig(1600, 920)
    # 三個區域
    f.rect(60, 60, 640, 740, fill="none", dash=True)
    f.text(380, 100, "開發機", size=32, bold=True)
    f.text(380, 140, "所有修改、討論與 Agent 的對話", size=24, color=MUTED)
    f.rect(740, 60, 240, 740, fill="none", stroke=BLUE, dash=True)
    f.text(860, 100, "私人網路", size=28, bold=True)
    f.text(860, 140, "只用金鑰登入", size=24, color=MUTED)
    f.rect(1020, 60, 520, 740, fill="none", dash=True)
    f.text(1280, 100, "測試機", size=32, bold=True)
    f.text(1280, 140, "舊程式需要的作業系統，只負責執行", size=24, color=MUTED)
    # 開發機
    f.card(100, 180, 560, 110, "人", ["提出需求、檢查結果、作出決定"])
    f.card(100, 340, 560, 140, "Agent", ["修改程式、送到測試機、遠端執行測試", "整理結果回報給人"],
           fill=PINK, stroke=ACCENT)
    f.card(100, 530, 560, 100, "專案資料夾", ["程式、規則、工作說明檔，保存於版本紀錄"])
    f.card(100, 670, 560, 100, "瀏覽器", ["檢視測試機轉回的網頁"])
    f.arrow([(330, 290), (330, 334)])
    f.text(300, 312, "交辦", size=22, color=MUTED, anchor="end")
    f.arrow([(430, 340), (430, 296)], color=ACCENT)
    f.text(460, 318, "回報", size=22, color=ACCENT, anchor="start")
    f.arrow([(380, 480), (380, 524)])
    f.text(410, 502, "修改、提交", size=22, color=MUTED, anchor="start")
    # 測試機
    f.card(1060, 340, 440, 120, "測試用的副本", ["只接收已提交的版本"], fill=BLUEBG, stroke=BLUE)
    f.card(1060, 510, 440, 100, "舊程式", ["與新的規則逐筆比對"], fill=BLUEBG, stroke=BLUE)
    f.card(1060, 660, 440, 110, "執行環境", ["執行測試、啟動網頁"], fill=BLUEBG, stroke=BLUE)
    f.arrow([(1280, 660), (1280, 616)])
    f.text(1300, 638, "比對", size=22, color=MUTED, anchor="start")
    # 跨機器的動作（Agent 發起）
    f.arrow([(660, 400), (1054, 400)], color=ACCENT)
    f.text(860, 380, "送出程式", size=24, color=ACCENT)
    f.arrow([(660, 450), (760, 450), (760, 690), (1054, 690)], color=ACCENT)
    f.text(870, 560, "遠端執行測試", size=24, color=ACCENT)
    f.arrow([(1060, 745), (666, 745)], dash=True)
    f.text(860, 722, "網頁轉回", size=24, color=MUTED)
    f.text(800, 860, "測試機不執行 Agent，也不在兩台共用的資料夾內修改檔案；討論與紀錄集中於開發機，下一次對話得以接續。",
           size=26, color=MUTED)
    f.save("w7-agent-remote-test")


if __name__ == "__main__":
    agent_remote_test()
