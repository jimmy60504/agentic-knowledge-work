# 第七週概念圖

課程自繪的示意圖，用來呈現投影片的邏輯關係，不是研究證據或資料來源。授權同本 repo。保留 Mac、Windows、Thunderbolt、Tailscale、SSH、git、Python 等公開的技術名稱（使用者 2026-10-08 決定）；不含內部系統、程式、主機、位址、路徑與人名。

- 產生方式：`python3 assets/week7-diagrams/draw.py`，同時輸出 SVG 與 PNG（需要 `rsvg-convert`）。
- 色票與字型沿用 `assets/week5-diagrams/README.md`，繪圖方式同 `assets/week6-diagrams/draw.py`。

| 檔案 | 投影片 | 內容 |
|---|---|---|
| `w7-agent-remote-test` | 候選素材「由 Agent 操作測試機」 | 以 Agent 為主角：使用者在 Mac 之外交辦與檢查，Agent 修改程式、以 git push 送出、經 SSH 遠端執行測試，網頁轉回 Mac 的瀏覽器；連線為 Thunderbolt 直連或 Tailscale；Windows 測試機只負責執行 |
| `w7-03-route` | 第 3 頁 | 五段路線，第三、四段標為重點 |
| `w7-06-dependency` | 第 6 頁 | 定位端與檢查端都調用檢查程式（規則庫），兩端以檔案相接，共用資料夾在下方 |
| `w7-08-same-result` | 第 8 頁 | 同一筆定位結果檔經過新舊程式，結果必須逐筆相同，不同時找出原因並歸類 |
| `w7-20-counts` | 第 20 頁 | 一個月資料不通過的事件：324、315、101 筆 |
| `w7-22-single-source` | 第 22 頁 | 規則檔產生檢查程式的門檻、說明頁、大表與門檻圖、測試 |
| `w7-28-release` | 第 28 頁 | 推上版本標籤後測試與打包，版本資訊公開、更新套件另行交付 |
| `w7-05-shared-folder` | 第 5 頁 | 共用資料夾的七類內容，各附 Tabler 圖示（assets/week7-icons/）；定位計算程式、測站表、速度模型以強調色標出 |
