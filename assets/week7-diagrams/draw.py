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
    """Agent 操作測試機：以 Agent 為主角，人在 Mac 之外交辦與檢查，Agent 經私人網路操作 Windows 測試機。"""
    f = Fig(1600, 920)
    # 人：在兩台電腦之外
    f.card(30, 350, 190, 200, "人", ["提出需求", "檢查結果", "作出決定"], tsize=34)
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
    # 人與 Agent、瀏覽器
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
    f.text(800, 862, "人只在 Mac 上交辦與檢查；涉及 Windows 的每一個動作都由 Agent 經 SSH 執行，人不必親自操作測試機。",
           size=26, color=MUTED)
    f.save("w7-agent-remote-test")


if __name__ == "__main__":
    agent_remote_test()
