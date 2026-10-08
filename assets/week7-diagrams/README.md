# 第七週概念圖

課程自繪的示意圖，用來呈現投影片的邏輯關係，不是研究證據或資料來源。授權同本 repo。名稱一律使用一般說法，不含系統、程式、主機與人名。

- 產生方式：`python3 assets/week7-diagrams/draw.py`，同時輸出 SVG 與 PNG（需要 `rsvg-convert`）。
- 色票與字型沿用 `assets/week5-diagrams/README.md`，繪圖方式同 `assets/week6-diagrams/draw.py`。

| 檔案 | 投影片 | 內容 |
|---|---|---|
| `w7-agent-remote-test` | 候選素材「由 Agent 操作測試機」 | 開發機與測試機的分工：人交辦、Agent 修改程式並經私人網路送出、遠端執行測試，網頁轉回開發機的瀏覽器；測試機只負責執行 |
