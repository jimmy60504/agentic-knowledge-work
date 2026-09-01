# PPTX 的 design token：佈景主題與母片系統

來源：
- 觸發文章：[AI Presentation Generator: 10 Skills for Professional Decks in 2026](https://youmind.com/zh-TW/blog/ai-presentation-generator-10-skills-for-professional-decks-in-2026)（YouMind blog）
- 文章提出專業 AI 簡報生成器的四個判準：設計意圖、視覺一致性、內容與設計整合、輸出保真度。

## 重點

.pptx 內建的 token 系統（`theme1.xml`）：

- **色彩槽位**：`dk1`/`lt1`、`dk2`/`lt2`、`accent1`–`accent6`、`hlink`/`folHlink` — 語意化引用，換主題整份變色。
- **字型槽位**：`majorFont`（標題）/ `minorFont`（內文），含拉丁／東亞／複雜文字 fallback。
- **效果槽位**：線條、填色、陰影層級。
- **母片 → 版面配置 → 投影片**的繼承鏈 + placeholder = component 層；`.potx` = 打包的 design system。

## 洞見

1. AI 簡報「每頁像不同人做的」= 工具逐頁 hardcode 顏色字型、不走 theme。
2. 輸出保真度崩壞常因為「先生 HTML 再轉 pptx」；原生產 pptx 並引用 theme 可避免。
3. 教學點：給 agent 一份 .potx + AGENTS.md 規則「只用 theme 色與 placeholder、禁止 hardcode」→ 一致性靠系統約束，不靠 agent 品味。python-pptx 可引用 `MSO_THEME_COLOR.ACCENT_1`。
4. 與第一堂同構：agent 表現由環境（約束）決定，不只由模型決定。

## 課程用途（候選，未定）

- 第二週美編段的核心教學點，或第四週深入。
- 實作素材：需要一份署內 .potx 範本。
