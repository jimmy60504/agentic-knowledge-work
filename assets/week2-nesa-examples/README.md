# 第二週實作起始材料：三種簡報形式的範例

取得日期：2026-09-07。用途：第二週投影片示意三種形式的總覽圖，以及學員的 agent 從 repo 抓不到範例檔時的講師備援。授課時給學員 repo 連結，由他們自行查看範例；不安裝或執行原專案的 skill。

來源：[slidefirm/NESA-SLIDE](https://github.com/slidefirm/NESA-SLIDE)，[MIT License](https://github.com/slidefirm/NESA-SLIDE/blob/main/LICENSE)，讀取時版本 v0.3.0。六個檔案皆為原檔，未修改、未裁切；檔名加上形式前綴以便辨識。原站把 HTML 分成純版型與圖片背景兩型，本課合併為 HTML 一類，只取純版型範例。

| 檔案 | 形式 | 原站位置 | 檔案說明 |
|---|---|---|---|
| `image2-voltgo-city.pdf` | 圖片式 | [demo PDF](https://slidefirm.github.io/NESA-SLIDE/image2/voltgo-city/voltgo-city-image2.pdf) | 每頁為一張生成圖片，文字無法選取 |
| `image2-voltgo-city-3x2.jpg` | 圖片式總覽圖 | [readme montage](https://raw.githubusercontent.com/slidefirm/NESA-SLIDE/main/demos/readme-montages/image2/voltgo-city-3x2.jpg) | README 用的六頁縮圖 |
| `html-store-manager-30-60-90.html` | HTML | [demo 頁面](https://slidefirm.github.io/NESA-SLIDE/store-manager-30-60-90/store-manager-30-60-90.html) | 單一 HTML 檔，瀏覽器播放與編輯；草稿存於瀏覽器本機，寫回檔案需另備 server（作者說明） |
| `html-store-manager-30-60-90-3x2.jpg` | HTML 總覽圖 | [readme montage](https://raw.githubusercontent.com/slidefirm/NESA-SLIDE/main/demos/readme-montages/html-pattern/store-manager-30-60-90-3x2.jpg) | README 用的六頁縮圖 |
| `pptx-flowpilot-2026-q2-clean.pptx` | PPTX | [demo 檔（Git LFS）](https://media.githubusercontent.com/media/slidefirm/NESA-SLIDE/main/demos/pptx/flowpilot-2026-q2-clean.pptx) | 八頁，文字為文字框、圖表為原生圖表 |
| `pptx-flowpilot-2026-q2-clean-3x2.jpg` | PPTX 總覽圖 | [readme montage](https://raw.githubusercontent.com/slidefirm/NESA-SLIDE/main/demos/readme-montages/pptx/flowpilot-2026-q2-clean-3x2.jpg) | README 用的六頁縮圖 |

## 使用方式

- 學員平時從 repo 連結取得範例；agent 抓不到時（例如 PPTX 在 Git LFS），講師再提供這裡的檔案。請 agent 逐一打開，記錄實際看見的功能與限制；未在瀏覽器實際操作的 HTML 功能標為待確認。
- 投影片引用總覽圖時，畫面標「範例：NESA-SLIDE（MIT）」，完整連結放備註。
- 「檔案說明」欄整理自第一輪試跑的實際檢查與原站 skill 說明，授課前可再核對。

## 保存方式

jpg、pdf、pptx 依 repo 的 `.gitignore` 不進版本管理，留在 OneDrive 同步的本機資料夾；README 與 HTML 檔進 git。遺失時依上表連結重新下載。PPTX 在 Git LFS，用 raw 連結只會拿到指標檔，須用表中的 media.githubusercontent.com 連結。
