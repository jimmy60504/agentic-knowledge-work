# slides/

放「實際發布」的授課投影片（PPTX）。

- 檔案只靠 OneDrive 同步，不進 git（`.gitignore` 全域忽略 `*.pptx`）。
- 發布方式：在 OneDrive 網頁版對檔案按「共用」，建立「任何人（具有連結者）可檢視」
  的連結，貼到 `index.qmd` 每週進度表的「投影片」欄。
- 學生點連結會開啟 PowerPoint 網頁版的全頁檢視器；本機存檔、OneDrive 同步完成後，
  線上看到的就是最新版。
- 本課程的投影片本身就是用課程教的流程（agent 產 .pptx）做出來的，
  中間產物（論點、故事線）留在 `drafts/`。

## 第四週

- `build-week4.py`：把 `drafts/09、10、11` 三份逐頁稿各產成素版 PPTX（`week4-1.pptx`、`week4-2.pptx`、`week4-3.pptx`）。標題一句、內文條列或表格、原話與口述進備註；不做視覺設計。改內容改逐頁稿再重跑，改版面改腳本。
- 檢查方式：用 PowerPoint 匯出 PDF 後逐頁看，或 `osascript` 批次匯出。
- 注意：PowerPoint 直接開 OneDrive 路徑可能拿到未同步的舊檔，檢查前先把 PPTX 複製到本機暫存目錄再匯出 PDF。

