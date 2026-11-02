#!/usr/bin/env python3
"""第八週的示意圖：軟體開發生命週期的時間成本。寬度為相對的時間感受，不是實際工時。"""
from pathlib import Path

INK, MUTED, LINE, BG, ACCENT, ACCENT_BG = "#2A2623", "#6B6560", "#D8D2C9", "#F5F2EC", "#BE8979", "#F6E9E4"
X0, GAP = 250, 8


def text(x, y, s, size=24, fill=INK, weight=400, anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="central">{s}</text>'


def row(y, label, blocks):
    out = [text(60, y + 75, label, 30, INK, 600, "start")]
    x = X0
    spans = {}
    for name, sub, w, hot in blocks:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="150" rx="12" fill="{ACCENT_BG if hot else BG}" stroke="{ACCENT if hot else LINE}" stroke-width="{3 if hot else 2}"/>')
        out.append(text(x + w / 2, y + 52, name, 28, INK, 600))
        for i, line in enumerate(sub):
            out.append(text(x + w / 2, y + 92 + i * 28, line, 20, MUTED))
        spans[name] = (x, w)
        x += w + GAP
    return out, spans


before = [
    ("需求", [], 120, False),
    ("設計", ["規劃資料庫", "與資料格式"], 280, True),
    ("實作", ["撰寫功能與重構"], 460, True),
    ("測試", ["功能完成後進行"], 200, False),
    ("部署", [], 120, False),
]
after = [
    ("需求", [], 120, False),
    ("設計", ["畫面與操作", "要看到才能確定"], 340, True),
    ("實作", ["Agent", "很快完成"], 150, False),
    ("測試與驗證", ["人實際操作，提出修改"], 340, True),
    ("部署", [], 120, False),
]

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900" font-family="PingFang TC, Hiragino Sans GB, sans-serif">',
    f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ACCENT}"/></marker></defs>',
    '<rect width="1600" height="900" fill="#FFFFFF"/>',
    text(60, 80, "軟體開發生命週期的時間成本", 44, INK, 600, "start"),
    text(60, 132, "示意圖：寬度表示相對的時間，不是實際工時", 24, MUTED, 400, "start"),
]
a, _ = row(210, "過去", before)
b, sp = row(540, "使用 Agent", after)
parts += a + b

# 設計與驗證之間的迭代
dx, dw = sp["設計"]
tx, tw = sp["測試與驗證"]
x1, x2, top = tx + tw / 2, dx + dw / 2, 460
parts.append(f'<path d="M{x1},534 C{x1},{top} {x2},{top} {x2},534" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-dasharray="12 8" marker-end="url(#ah)"/>')
parts.append(text((x1 + x2) / 2, 452, "反覆多次，直到符合需要", 24, ACCENT, 600))
parts.append(text(800, 790, "Agent 縮短了實作的時間，設計的迭代與驗證仍然需要人投入時間。", 30, INK, 600))
parts.append("</svg>")
Path(__file__).with_name("w8-sdlc-cost.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
