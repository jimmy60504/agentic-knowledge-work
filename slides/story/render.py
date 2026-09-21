#!/usr/bin/env python3
"""把 slides/story/*.puml 轉成 SVG。需要本機安裝 PlantUML（brew install plantuml，會一併安裝 Java）。

用法：python3 slides/story/render.py            → 轉全部
      python3 slides/story/render.py research-idea → 只轉一份
故事先由 agent 依逐頁稿寫成 .puml（誰、做了什麼、交出什麼，一行一個活動），內容改 .puml，版面由 PlantUML 排。
"""
import shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if not shutil.which("plantuml"):
    sys.exit("找不到 plantuml。安裝：brew install plantuml")
names = sys.argv[1:] or [p.stem for p in HERE.glob("*.puml")]
for n in names:
    src = HERE / f"{n}.puml"
    subprocess.run(["plantuml", "-tsvg", "-charset", "UTF-8", str(src)], check=True)
    print(f"{src.name} → {n}.svg")
