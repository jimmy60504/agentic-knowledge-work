# Agent 時代的知識工作

這個 repo 同時保存課程整理筆記與正式授課教材，也是課程自己的示範專案：
它就是用課程教的流程（AGENTS.md ＋ 知識庫 ＋ 工作紀錄）長出來的。

- `docs/`：備課筆記（教案、課程地圖），不發布到課程網站。
- `kb/`：課程的知識庫。討論中撈到的素材與洞見，附來源，先進這裡再決定要不要進教材。
- `工作紀錄.md`：討論脈絡與決策紀錄，含「待消化」區。
- `notes/`：正式教材文章。每週一份 Quarto Markdown（`.qmd`）。
- `slides/`：授課投影片（PPTX），靠 OneDrive 同步、不進 git；網站連結指向 OneDrive 共用連結。

課程網站：<https://jimmy60504.github.io/agentic-knowledge-work/>

## 一句話定位

用 agent 走完知識工作的完整循環——收集、整理、蒸餾、表達——
簡報、報告、論文都是同一套流程；agent 讓產出變快，判斷成為最貴的環節。

## 編輯與預覽

先安裝 [Quarto](https://quarto.org/docs/get-started/)：

```bash
brew install --cask quarto
```

在 repo 根目錄啟動即時預覽：

```bash
quarto preview
```

完整建置網站：

```bash
quarto render
```

建置結果會放在 `_site/`。推送到 GitHub 後，GitHub Actions 會重新 render 並部署到 GitHub Pages。

## 目錄

- `_quarto.yml`：網站、輸出格式與公開內容範圍。
- `index.qmd`：課程網站首頁。
- `tools.qmd`：工具索引。
- `notes/`：各週文章版教材。
- `docs/`：教案與課程地圖，不公開。
- `kb/`：知識庫。
- `工作紀錄.md`：討論脈絡。
- `AGENTS.md`：給 agent 與後續協作者的維護規則。
