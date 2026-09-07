# 第二週流程圖

三個迴圈的直式流程圖，mermaid 產生。來源與輸出：

| 檔案 | 用途 |
|---|---|
| `three-loops.mmd` | 全圖來源；`three-loops-h1.mmd`、`-h2`、`-h3` 由它衍生，各圈亮、其他淡化（節點、群組、連線都淡） |
| `three-loops-mermaid.png` | 全圖，投影片「內容要走三個迴圈」 |
| `three-loops-mermaid-h1.png`、`-h2`、`-h3` | 確認方向、建立架構、調整風格三頁，以及歷程頁右上角的縮小版 |
| `build_three_loops_mermaid.sh` | 重出四張：mermaid-cli（npx，需網路）出 SVG，改字型後以系統 WebKit（qlmanage）轉 PNG 並裁白邊 |

直接用 mermaid-cli 出 PNG 會落到襯線體，因為它的 headless Chrome 沒有 PingFang；改走 SVG 加系統 WebKit 才正確。matplotlib 版已捨棄，箭頭繞法不如 mermaid。

課程原創圖，2026-09-08。PNG 與 SVG 依 `.gitignore` 不進版本管理，重跑腳本即可產生。
