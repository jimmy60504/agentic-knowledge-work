# NESA-SLIDE：簡報的三種形式（圖片、HTML、PPTX）與一套共用的設計流程

## 來源

- [slidefirm/NESA-SLIDE](https://github.com/slidefirm/NESA-SLIDE)，MIT 授權，繁體中文，給 Codex 與 Claude Code 用的開源簡報製作 skills。讀取時版本 v0.3.0（2026-09-03）。
- 使用者的提醒：重點不在 skill 本身，而是它把簡報形式分清楚了。三大類是圖片、HTML、PPTX（repo 把 HTML 再分成純版型與圖片背景兩種，共四種成品）。
- Demo 都掛在 GitHub Pages，每種形式各三份，可直接開來看差異。

## 重點

**四種成品，各對應一個 skill**

| 形式 | skill | 特性 |
|---|---|---|
| 純圖片（Image2） | generate-image-slide | 每頁生成一張 16:9 圖，視覺最完整，頁面物件不可編輯 |
| 純 HTML | html-pattern-slide | 1920×1080 可編輯 HTML，瀏覽器播放與編輯，視覺靠 pattern 圖樣 |
| 圖片背景 HTML | html-image-slide ＋ slide-background-image | 前景文字物件可編輯，背景是生成的 raster 或照片 |
| PPTX | ppt-builder | 原生可編輯，要求真的有 Slide Master、Custom Layout、Placeholder；整頁截圖不能冒充可編輯 PPTX |

**一套 renderer 無關的設計流程（design-presentations）**

```text
Story → Art Direction Brief → Scene Grammar → Theme + Layout → Renderer Handoff → Technical QA → Perceptual QA
```

- 第一步是阻擋式提問：先問要哪一種形式，收到答案前不開工。
- Story 先定一句核心主張、受眾要採取的行動、敘事弧線；每頁記錄單一主要訊息、證據、內容關係、密度。
- Art Direction Brief 要寫 visual_genre、narrative_metaphor、signature_move、spatial_rule，明講「不只寫高級、現代、好看」。
- 內容不得永久綁進 Theme 或 Layout；Theme 管外觀、Layout 管幾何，CSS 要有明確 owner。

**大綱規劃（slide-outline-planner）**

- 六階段：資訊收集、目標調整、受眾分析、內容規劃、資料研究、逐頁大綱。
- 每頁畫面內容可用主張、段落、比較、流程、時間軸、數據、表格、引言、案例、媒體任一主導，**不強制列點**。
- 只產大綱，不先選形式；產製另交 renderer skill。

**版型目錄**：幾十個有名字的 layout（toc、kpi-scorecards、matrix-4quadrant、process-flow、timeline、comparison-table、pyramid、funnel、cycle-hub、cards-1-plus-4……），附預覽圖與 gallery。

**AGENTS.md 是一份很重的專案規則**：把使用者要求轉成可觀察的完成條件、不得以檔案存在或程式跑過代替完成、未驗證項目要標 partial、未授權不 push 不部署、多 agent 共用工作樹的提交防護。

## 洞見（與本課程的對應）

1. **兩派變三段。** 教案目前把 AI 簡報分成生圖派與檔案派；這個 repo 顯示中間還有 HTML：文字可編輯、瀏覽器就能播、視覺自由度比 PPTX 高，但交接不如 PPTX。可以講成一條「從烤死到可編輯」的光譜：圖片 → HTML → PPTX，署內交付仍是 PPTX，HTML 適合示範與教學。
2. **它的流程跟課程的五步與六層要素是同一張圖。** Story 那一步要求一句核心主張、受眾行動、每頁單一訊息，就是教案的策略層判準；而且它把「先選形式」「補齊受眾與目標」做成阻擋式提問，正是「情境與核心訊息只能人給」的工程化版本。可當「別人也這樣拆」的印證。
3. **大綱規劃的「不強制列點」與十種畫面內容形式**，是「一頁一論點」往下一層的具體清單：這頁的論點該用比較、流程、時間軸還是數據來呈現。可以直接借進第二週的判準或第四週。
4. **版型有名字，就能下具體修改指令。** 五步流程的第五步「人下具體修改指令」，最缺的是詞彙；有了 layout 名稱與 gallery，學員可以說「這頁改成 matrix-4quadrant」而不是「幫我弄好看一點」。
5. **這是「速成班丟給你的 skill」的高階樣本。** 它很強，但只管結構層與表達層；受眾、目的、核心訊息它會反過來問你。用它示範正好說明：skill 再重，判斷還是要人給。也可以拿它的 AGENTS.md 當「重型專案規則長什麼樣」的對照，跟學員三行的 AGENTS.md 放在一起看。
6. 與 [[pptx-theme-design-token]]、[[design-system-as-skill]] 同一套想法：Theme 管不准變的、Layout 管幾何、內容當次輸入，不把文案烤進版型。

## 注意

- 對初學者太重，安裝提示詞本身就一頁；適合講師示範或視覺模組週，不適合第二週實作直接上。
- Image2 依賴內建生圖能力，等於需要付費方案。
- 只支援 Codex 與 Claude Code，跟教材「工具無關」的原則有落差；教材裡只引用它的分類與流程，不綁它的指令。

## 課程用途（候選，未定）

- 第二週「市面 AI 簡報服務」段：兩派改成三段光譜，用它的三組 demo 各開一份現場對比。
- 第二週實作第五步：把 layout 目錄當修改指令的詞彙表給學員看。
- 視覺模組週（場景矩陣 C 家族）：講師用它示範完整流程，並拆解它的 AGENTS.md。
- 待整理進教案的判準：十種畫面內容形式、Art Direction Brief 的四個欄位。
