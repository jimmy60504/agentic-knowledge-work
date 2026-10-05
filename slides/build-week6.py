#!/usr/bin/env python3
"""第六週投影片建置：把 drafts/18-week6-slides.md 產成素版 PPTX（slides/week6.pptx）。

用法：python3 slides/build-week6.py

版面、配色與圖片處理全部沿用 build-week5.py，只替換來源與輸出檔。
素版原則：只做文字階層與圖片位置，不做視覺設計；圖片檔不存在時以灰框標示預留位置。
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bw5", HERE / "build-week5.py")
bw5 = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(HERE))
spec.loader.exec_module(bw5)

bw5.SRC = bw5.ROOT / "drafts/18-week6-slides.md"
bw5.OUT = HERE / "week6.pptx"

if __name__ == "__main__":
    bw5.main()
