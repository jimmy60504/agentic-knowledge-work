# 2026 年 agent 普及之後，研究看到什麼新的變化

整理日期：2026-09-05。先前收的證據（英國 Copilot 試驗、新加坡 Pair、WTI 2024）都是聊天工具時代的資料，這份補 2026 年上半年針對 agent 的報告，並比較兩個時代的差別。相關：[[what-makes-civil-servants-want-to-learn-ai]]、[[public-sector-ai-adoption-barriers-and-examples]]。

## 一、來源

- **Microsoft 2026 Work Trend Index**（2026-05，兆級 M365 訊號加 10 國 2 萬名 AI 使用者問卷）。[報告頁](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)、[GeekWire 摘要](https://www.geekwire.com/2026/microsofts-new-research-finds-an-ai-paradox-holding-companies-back/)。
- **Anthropic Economic Index**：2026-03「Learning curves」、2026-06「Cadences」，比較 Claude.ai、Cowork、Claude Code 的使用型態。[三月報告](https://www.anthropic.com/research/economic-index-march-2026-report)、[六月報告](https://www.anthropic.com/research/economic-index-june-2026-report)。
- **METR 開發者生產力研究**：2025-07 的隨機試驗（用 AI 慢 19%）與 2026-02 的追蹤更新。[2025 研究](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)、[2026 更新](https://metr.org/blog/2026-02-24-uplift-update/)。
- **arXiv 2605.24688**「Adopting AI in Practice Does Not Guarantee the Productivity Boost」（2026-05 立場論文）。[摘要](https://arxiv.org/abs/2605.24688)。
- 公部門 agent：[WEF 政府 agentic AI 就緒框架（2026-01）](https://www.weforum.org/publications/making-agentic-ai-work-for-government-a-readiness-framework/)、[techUK：The Agentic Civil Service](https://www.techuk.org/resource/the-agentic-civil-service-breaking-free-from-legacy-it-one-workflow-at-a-time.html)、[Route Fifty](https://www.route-fifty.com/artificial-intelligence/2026/06/ai-agents-will-transform-government-services-will-we-build-future-prosperity-together/413936/)。

## 二、agent 跟聊天工具差在哪，數據怎麼說

**1. 互動的形狀變了：從來回對話變成交辦整件事。**
- 同樣產出一篇文章，Claude Code 平均 1 個人類提示，聊天要 13 輪；agent 的自主程度高 0.37 分（1 到 5 分）。
- 93% 的對話會產出可辨識的成品，文件與報告佔 15%。交辦深度依任務而異：翻譯與算數約 1.5 分，做網站與應用約 4 分。
- 高薪職業的任務消耗 2.07 倍 token；agent 式、產出成品的工作流每次更貴，也集中在價值較高的任務。
- **讀法**：人的貢獻從「每一輪的回覆」移到兩端：前面的交辦說明，後面的驗收。中間那段變成 agent 的。

**2. 人的工作往「定方向、定標準、看結果」移動。**
- WTI 2026 用四種協作模式描述：Author（自己做、AI 幫忙）、Editor（你定意圖、AI 出初稿、你改）、Director（你寫規格、整件交出去背景執行）、Orchestrator（多個 agent 平行跑，只把例外丟回給你）。
- 使用者認為越來越重要的人類技能：品質控管 50%、批判思考 46%。下降的是逐步執行。
- 「前沿專業者」的習慣：動手前先停下來想（53% 對 33%）、刻意不用 AI 練習（43% 對 30%）、把可重複的流程記錄下來。
- **讀法**：2025 年的公務員試驗量到的是 Editor 模式（初稿、摘要省時間）；2026 年 agent 把人推向 Director 模式。技能從「會下 prompt」變成「會寫規格、會驗收」。

**3. 學習曲線是真的，而且老手走向協作而不是全自動。**
- 使用 6 個月以上的人，控制任務後成功率高約 4 個百分點；會把較難的任務分配給較強的模型（任務時薪每高 10 美元，Opus 使用率高 1.5 個百分點）。
- 老手偏好反覆協作，而不是一句話全交出去，與原先「老手會走向全自動」的假設相反。
- 68% 的人不論自動化程度都說有學到東西（自陳）。
- **讀法**：兩小時的課看不到這條曲線，十六週看得到；而且該教的是反覆協作，不是一鍵完成。「依任務價值選模型」正是老手的行為，配置題的講法有數據撐。

**4. 影響的決定因素在組織，不在個人。**
- WTI 2026：AI 影響 67% 來自組織因素（文化、主管支持、人才制度），32% 來自個人心態與能力。
- 主管自己示範用 AI：員工對 AI 價值的認同高 17 個百分點，對 agent 的信任高 30 個百分點。
- 65% 怕不用會落後，但 45% 認為重新設計工作比維持現狀更冒險。報告點名需要「評估基礎建設」：誰看 agent 的表現、誰更新流程、局部成功怎麼擴散。
- arXiv 立場論文：人力組成、基礎能力、學習曲線、合理使用的誘因、目標的彈性，五個組織因素可以抵銷甚至反轉技術上的生產力。
- **讀法**：這條直接支持兩件事。阻礙那份的結論（環境把人卡在第一層），以及主管加量會把判斷往上推那條：主管的角色是定標準與看結果，不是加件數。

**5. 生產力證據在 agent 時代反而更難量。**
- METR 2025：資深開發者用早期 2025 工具，反而慢 19%，自己卻以為快 20%。
- METR 2026 追蹤：點估計轉為加速，但信賴區間很寬、跨過零；而且方法失效：不想在沒有 AI 的情況下工作的人拒絕參加、參與者跳過他們認為 AI 能加速的任務、同時跑多個 agent 讓「花多少時間」無法計算。
- **讀法**：agent 帶來的新工作型態是平行交辦，人變成排程與審核者。這正是決策疲勞與傳話筒風險的土壤，也是為什麼「來回次數」比「件數」更值得管。

**6. 公部門的 agent 試驗多半對外，不對內。**
- 英國 GOV.UK Chat 2025/26 試 agent 式的人生轉換服務，2026/27 擴大；新加坡用 agent 跨機關比對福利與補助；賓州訓練 3,000 名公務員與 agent 協作。IDC 說 71% 的機關計畫在 2026 到 2027 擴大 agent 使用；Gartner 預估 40% 的 agent 專案在 2027 前取消（成本、價值不清、風險控管不足）。
- 台灣：DIGITIMES 稱 2025 年底 45% 上市公司啟動 agent 專案（二手引述，待查證）。
- **讀法**：政府在試的是對民眾的 agent 服務，承辦人自己桌上的 agent 幾乎沒有機關在系統性地做。這門課的位置沒有被填掉。

## 三、兩個時代的對照

| | 聊天工具時代（2024 至 2025 的證據） | agent 時代（2026 的證據） |
|---|---|---|
| 人做什麼 | 下 prompt、改初稿（Editor） | 寫規格、驗收成品（Director） |
| 省下的是 | 初稿、摘要、找資料的時間 | 整段執行過程 |
| 新增的負擔 | 檢查每一段 | 檢查整份成品與流程，平行任務的排程 |
| 最重要的技能 | 問對問題 | 定標準、看結果、記錄可重複的流程 |
| 風險的形狀 | 一段話裡的幻覺、AI 腔 | 整份東西沒經過你、判斷上移、傳話筒 |
| 決定成敗的 | 個人會不會用 | 組織有沒有評估與標準的基礎建設 |

## 四、對課程的意義（候選，未定）

- 課程主張有了 2026 年的外部證據：agent 時代人的工作是定標準與驗收，前沿專業者的三個習慣（先停下來想、刻意不用 AI 練習、記錄可重複流程）剛好對應思考框架、風險週的「定期不開 agent 寫一段」、AGENTS.md 與 skill。
- 前半段可以用「四種協作模式」一張圖講 agent 跟聊天的差別，比講技術原理更貼學員經驗；第二週實作就是從 Editor 走到 Director 一次。
- 老手走向協作而非全自動，支持第二週重頭戲放在發散與收斂的來回，而不是一句話產一份。
- 組織因素 67%、主管示範加 30 個百分點的信任：給主管版那一頁的數字。
- 誠實面：agent 時代的生產力證據方法上更弱，METR 的自我感覺與實測相反那筆要講，提醒學員自己量。
