# 模型強弱、推理強度與額度：配置是判斷題，不是推銷

第二週前半段「免費 vs 付費」的素材與講法。定案方向：**簡報只用一張非常簡單的表格帶過（約 5 分鐘、兩三頁）**，詳細比較給連結讓學員回去自己看；初接觸的人吸收不了太多資訊，而且差異要實際操作才會有感。

## 來源

- [Artificial Analysis：模型比較（智慧指數 vs 每任務成本、vs 時間）](https://artificialanalysis.ai/models)。免費、常更新的散布圖，一眼看出強模型又貴又慢。
- [Reasoning Effort: Cost vs Quality Benchmarks 2026（Digital Applied）](https://www.digitalapplied.com/blog/reasoning-effort-cost-vs-quality-benchmarks-2026)。推理強度的圖表：高推理首字延遲是低推理的 5 到 60 倍；某些任務中等推理贏過高推理，因為想太多會過度設計。
- [Claude Code 官方文件：Model configuration](https://code.claude.com/docs/en/model-config)。`opusplan`：規劃用 Opus、執行用 Sonnet；effort 等級 low 到 max。工具內建「強模型規劃、弱模型執行」的實例。
- [數位時代：Claude、Gemini、ChatGPT 訂閱費多少？2026 方案價格比較](https://www.bnext.com.tw/article/90197/ethan-mollick-which-ai-to-use)。中文整理 Mollick 觀點，附三家方案價格表。學員回去看這篇最省力。
- [Ethan Mollick：An Opinionated Guide to Using AI Right Now](https://www.oneusefulthing.org/p/an-opinionated-guide-to-using-ai)。抓到的是 2025-10 版；搜尋顯示 2026-07 有更新版，據報已把 Gemini 拿掉、只推 ChatGPT 或 Claude（[報導](https://marketinghelm.com/news/mollick-ai-guide-drops-gemini)）。**開課前確認用哪個版本連結。**
- Codex 與 Claude Code 額度比較文章（例：[Morphllm](https://www.morphllm.com/comparisons/claude-code-vs-codex)）。數字每季變、各篇互相矛盾，**不放進教材**，口頭一句「額度制各家不同，實際用一個月再說」。

## 重點

兩個旋鈕，三個問題：

| | 你要說多少 | 它會做多少 | 燒多少 |
|---|---|---|---|
| 弱模型 | 說很清楚、來回多次 | 按部就班，可控 | 少 |
| 強模型 | 一句話就接近可用 | 深、快就想很久、容易自己多做 | 多 |

- 旋鈕一：模型等級（選哪台）。旋鈕二：推理強度（踩多深），常是同一台上的刻度，可自己調。兩者方向一樣：深度換速度與額度。
- 「它會做多少」同時涵蓋深度與自作主張；強模型多做的事有時是幫忙、有時是失控，這是可控性的成本。
- 強模型規劃、弱模型執行：規劃是判斷密集的，執行是按部就班的。前提是計畫寫得夠清楚，而那份計畫就是一個 md 檔，跟 AGENTS.md 同類。接到下一段專案化。

## 洞見

1. 這樣講把「選模型」變成配置題，跟課程主張同一件事：模型是放大器的倍率，倍率開多大取決於這件事需要多少判斷。訂不訂閱是配置的結果，那條線自己會浮出來，不像推銷。
2. 額度那條線給可執行的建議，不給結論：先訂最低方案用一個月，記下額度什麼時候燒完、當時在做什麼，再決定要不要往上。
3. 錢誰出：不在課堂處理。實際用了、長官也用了，採購會跟上（署內曾提過、計畫未下）。下午 2 小時免費額度燒完的人數與卡點，本身就是日後採購的數字，順手記。
4. 推廣靠學員互傳：第二頁講完問「有訂閱的舉手」，分組時拆開；巡視遇到免費額度燒完的人，請同桌有訂閱的跑一次同樣的東西給他看。同事示範比講師示範有說服力，也是「強模型規劃、弱模型執行」的人肉版：燒完的人拿論點 md 回免費工具做後面幾步。
5. 「三塊都是說明的成本」主線：訂閱降低每次說明的深度，AGENTS.md 降低說明的重複，兩者解不同成本、互不取代。學員問「寫好 AGENTS.md 免費不就夠了」的答案：夠用於重複的部分，不夠用於每次都新的判斷。

## 課程用途（候選，未定）

- 第二週前半段「免費 vs 付費」段，約 5 分鐘：一張簡表（上表）＋一組同任務並排截圖（強模型一句話 vs 弱模型來回幾輪）＋三個延伸連結（Artificial Analysis 看關係、數位時代看價格、Mollick 看怎麼選）。
- 取代原本的 2×2 現場對照（見教案原理篇第 3 節），現場不 live。
- 並排截圖的任務開課前定、先跑好存進 kb/。
