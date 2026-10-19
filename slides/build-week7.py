#!/usr/bin/env python3
"""第七週投影片建置：把 drafts/22-week7-slides.md 產成 PPTX（slides/week7.pptx）。

用法：python3 slides/build-week7.py
草稿截圖：設定環境變數 WEEK7_DRAFT_IMAGES 指向講師本機的對照表（TSV，不進 repo），
格式同第六週：「頁碼<TAB>圖片路徑<TAB>圖說」，有對照的頁以截圖取代預留位置並標【草稿截圖】。

版面、配色與解析全部沿用 build-week6.py（再往上沿用 build-week5.py），這裡只換來源與輸出。
"""
import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("bw6", HERE / "build-week6.py")
bw6 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bw6)

bw5 = bw6.bw5
bw5.SRC = bw5.ROOT / "drafts/22-week7-slides.md"
bw5.OUT = HERE / "week7.pptx"

if os.environ.get("WEEK7_DRAFT_IMAGES"):
    os.environ["WEEK6_DRAFT_IMAGES"] = os.environ["WEEK7_DRAFT_IMAGES"]
    bw6.DRAFT.clear()
    bw6.DRAFT.update(bw6.draft_images())

if __name__ == "__main__":
    bw5.main()
