# ssot/

課程核心概念的唯一正本（single source of truth）。目前兩個：`three-loops.md` 三個迴圈，`project-structure.md` 專案資料夾結構。一個概念一檔，定義與流程圖來源（mermaid 區塊）都在同一份 `.md` 裡。

規則：

- 教案、文章、投影片、工具索引只引用或複製這裡的內容，不各自改寫；發現要改，先改這裡，再同步出去。
- 每次改動在 `.md` 的版本紀錄加一行：日期、改了什麼、為什麼。舊版不留檔，看 git。
- 已發布的週次用的是當時的版本，不回改；`assets/week2-diagrams/three-loops.mmd` 是第二週的凍結快照，不再是正本。
- 這個資料夾不進網站（`_quarto.yml` 的 render 清單沒有它），但在 git 裡。
