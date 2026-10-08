# 第七週概念圖

課程自繪的示意圖，用來呈現投影片的邏輯關係，不是研究證據或資料來源。授權同本 repo。保留 Mac、Windows、Thunderbolt、Tailscale、SSH、git、Python 等公開的技術名稱（使用者 2026-10-08 決定）；不含內部系統、程式、主機、位址、路徑與人名。

- 產生方式：`python3 assets/week7-diagrams/draw.py`，同時輸出 SVG 與 PNG（需要 `rsvg-convert`）。
- 色票與字型沿用 `assets/week5-diagrams/README.md`，繪圖方式同 `assets/week6-diagrams/draw.py`。

| 檔案 | 投影片 | 內容 |
|---|---|---|
| `w7-agent-remote-test` | 候選素材「由 Agent 操作測試機」 | 以 Agent 為主角：人在 Mac 之外交辦與檢查，Agent 修改程式、以 git push 送出、經 SSH 遠端執行測試，網頁轉回 Mac 的瀏覽器；連線為 Thunderbolt 直連或 Tailscale；Windows 測試機只負責執行 |
