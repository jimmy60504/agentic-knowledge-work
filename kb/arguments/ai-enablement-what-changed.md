# 員工拿到 AI 之後：賦能了什麼、哪些工作減少、哪些增加

整理日期：2026-09-27。起因：課程原本的主軸是員工賦能，使用者要求查證「大家到底賦能了什麼，真的用了之後減少與增加的地方在哪」，作為第五週「導入前要規劃與測量什麼」的依據。由三個 sub-agent 分頭搜尋（任務層級實驗、工作增減、政府試辦），主責整合；引用前仍須開原始連結核對。

相關：[[agent-era-2026-what-changed]]（WTI 2026、Anthropic 經濟指數、METR，本檔不重複）、[[ai-adoption-failure-cases]]（失敗案例）、[[public-sector-ai-adoption-barriers-and-examples]]（英國 Copilot 試驗、新加坡 Pair）。

## 一、來源

### 任務層級的實驗：誰得到什麼能力

| 研究 | 方法 | 結果 | 注意 |
|---|---|---|---|
| Brynjolfsson、Li、Raymond〈Generative AI at Work〉QJE 2025，[論文](https://academic.oup.com/qje/article/140/2/889/7990658) | 5,172 名客服人員分階段導入 | 平均每小時解決問題數提升約 15%；新手提升 34%，資深者幾乎沒有提升、品質略降 | 有標準答案、最佳做法可複製的工作 |
| Dell'Acqua 等〈Navigating the Jagged Technological Frontier〉2023，[HBS](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700) | 758 名 BCG 顧問隨機分組，18 項任務 | 能力範圍內的任務：完成數多 12.2%、快 25.1%、品質高逾四成；範圍外任務正確率低 19 個百分點 | 使用者難以自行判斷任務在範圍內或外 |
| Noy、Zhang，Science 2023，[論文](https://www.science.org/doi/10.1126/science.adh2586) | 453 名專業人士寫作任務 | 時間減少 40%、品質提升 18%；寫作能力較弱者受益較多 | 單次任務，非長期追蹤 |
| Dell'Acqua 等〈The Cybernetic Teammate〉2025，[NBER](https://www.nber.org/papers/w33641) | P&G 776 人，個人或團隊 × 有無 AI | 一人加 AI 的方案品質追平兩人團隊；商業與研發背景者都能提出涵蓋另一方觀點的方案 | 以評分衡量，非長期商業結果 |
| OpenAI〈How People Use ChatGPT〉2025，[NBER](https://www.nber.org/papers/w34255) | 150 萬則對話 | 詢問約 49%、執行約 40%；工作用途中執行類過半，多為寫作 | 使用分布，非能力提升的因果證據 |
| Anthropic Economic Index 2025-02，[連結](https://www.anthropic.com/news/the-anthropic-economic-index) | Claude 對話對應職業任務 | 增強 57%、自動化 43%；中高薪職業用得最多 | 樣本限於已在使用者 |

### 工作的增減

| 研究 | 方法 | 減少 | 增加 | 注意 |
|---|---|---|---|---|
| Humlum、Vestergaard（丹麥）2025，[NBER w33777](https://www.nber.org/papers/w33777) | 約 25,000 名勞工問卷串接薪資與工時紀錄 | 平均省下約 3% 工時；對薪資與工時的效果接近零 | 檢查 AI 產出、AI 相關的新任務、職務重組 | 前兩年的早期效果 |
| St. Louis Fed（Bick、Blandin、Deming），[2025-11](https://www.stlouisfed.org/on-the-economy/2025/nov/state-generative-ai-adoption-2025) | 全美代表性問卷 | 使用者自報省 5.4% 工時，換算全體勞工約 1.4% | 使用逐漸常態化 | 自陳 |
| Dillon 等（微軟）〈Shifting Work Patterns〉2025，[arXiv](https://arxiv.org/abs/2504.11436) | 66 家企業約 6,000 人隨機分派，以系統紀錄追蹤 | 處理信件每週少近 3 小時 | 會議時間與性質沒有改變 | 只有個人能自行調整的工作改變 |
| Ranganathan、Ye（柏克萊）HBR 2026-02，[連結](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it) | 一家科技公司約 200 人追蹤 | 無明顯減少 | 節奏加快、範圍擴大、工作時段延長、同時處理多件事與反覆檢查 | 單一公司、質性研究 |
| Anthropic 內部研究 2025，[Axios 報導](https://www.axios.com/2026/01/15/anthropic-study-work-ai-jobs) | 132 人問卷、53 人訪談 | 可完全交出的工作約 0 至 20%，多為容易驗證或枯燥的任務 | 27% 是原本不會去做的工作 | 與同事協作與指導新人的機會減少 |
| Lancet Gastro 2025-08，[摘要](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00289-4/abstract) | 內視鏡醫師接觸 AI 前後比較 | 不用 AI 時腺瘤偵測率由 28.4% 降至 22.4% | — | 觀察性研究 |
| Lee 等（微軟與 CMU）CHI 2025，[論文](https://dl.acm.org/doi/full/10.1145/3706598.3713778) | 319 名知識工作者、936 個案例 | 越信任 AI，投入的批判思考越少 | 思考的內容轉為查證、整合與監督 | 自陳、橫斷面 |
| Brynjolfsson 等〈Canaries in the Coal Mine〉2026-08 更新，[連結](https://digitaleconomy.stanford.edu/news/canariesaug26/) | 薪資服務商資料 | AI 以取代為主的職業中，22 至 25 歲就業相對落後 19% | 以輔助為主的職業，資深者就業持平或上升 | 相關性，非實驗 |

### 政府的員工試辦

| 試辦 | 規模 | 改善的任務 | 沒有改善或變差 | 新增負擔 | 受益較多者 |
|---|---|---|---|---|---|
| 澳洲全政府 Copilot（DTA）2024，[評估](https://www.dta.gov.au/articles/evaluation-whole-government-trial-generative-ai-now-available) | 60 多個機關、逾 5,000 人 | 摘要、草擬、資訊檢索；自陳每日約省 1 小時 | 報告未列 | 使用被視為偷懶、怕被取代、寫作能力退化、責任歸屬 | 資淺與資訊職務 |
| 澳洲財政部 2025-02，[摘要 PDF](https://evaluation.treasury.gov.au/sites/evaluation.treasury.gov.au/files/2025-02/evaluation-generative-artificial-intelligence-summary.pdf)、[The Register](https://www.theregister.com/2025/02/12/australian_treasury_copilot_pilot_assessment) | 218 人，14 週 | 找資料、摘要、會議紀錄 | 複雜任務；認為有幫助者由事前 75% 降為 38% | 敏感資料疑慮 | 神經多樣性與部分工時者 |
| 英國商業貿易部（DBT）2025-09，[The Register](https://www.theregister.com/2025/09/04/m365_copilot_uk_government/)、[官方部落格](https://digitaltrade.blog.gov.uk/2025/09/25/discover-dbts-m365-copilot-evaluation-report) | 1,000 席、300 人分析 | 會議摘要、信件撰寫較快且較準確 | Excel 分析較慢且較差；簡報較快但品質較差 | 22% 遇過幻覺；未發現省時轉為生產力的有力證據 | 神經多樣性、英語非母語者 |
| 英國工作與年金部（DWP）2026-01，[Civil Service World](https://www.civilserviceworld.com/professions/article/copilot-trial-dwp-staff-save-19-minutes-per-day) | 3,549 人，六個月 | 資訊檢索、摘要、溝通；每日約省 19 分鐘 | 報告未列 | — | ADHD、讀寫障礙者 |
| 美國賓州 ChatGPT 2025-03，[官方報告](https://www.pa.gov/content/dam/copapwp-pagov/en/oa/documents/programs/information-technology/documents/openai-pilot-report-2025.pdf) | 14 個機關、175 人 | 草擬、摘要、研究；自報每日省 95 分鐘 | 未列 | 未列 | — |
| 數發部 TryAI，[新聞稿](https://moda.gov.tw/press/press-releases/17952) | 30 多個機關 | 衛福部會議紀錄由 30 至 40 小時降至 6 小時 | 未列 | 未列 | — |

賓州與 TryAI 為機關自報，方法未公開；澳洲與英國四份為獨立或半獨立評估。氣象機構員工使用生成式 AI 助理的公開評估查無資料；ECMWF 等 AI 預報模式屬另一件事，不混用。

## 二、重點

**賦能的實際樣子有三種，都有條件：**

| 賦能的樣子 | 證據 | 條件 |
|---|---|---|
| 熟悉的例行工作變快 | 摘要、草擬、信件、資訊檢索在所有政府試辦中都改善 | 產出容易檢查 |
| 新手與能力較弱者追上 | 客服新手提升 34%；寫作較弱者受益較多；神經多樣性與非母語者在三份政府評估中都受益 | 有標準答案或最佳做法可複製 |
| 做到原本做不到或不會做的事 | 一人追平兩人團隊；Anthropic 員工 27% 是原本不會做的工作 | 仍需有人判斷品質 |

**減少與增加：**

| 減少的工作 | 增加的工作 |
|---|---|
| 信件處理、摘要、初稿 | 檢查與驗證 AI 產出 |
| 新手的學習曲線 | 原本不做的延伸工作 |
| 自己動腦的投入（信任 AI 越多越少） | 工作節奏、範圍與同時處理的事項 |
| 不用 AI 時的基本技能（醫療案例） | 期望落差造成的失望（澳洲財政部） |
| 新人的職缺（取代型職業） | 使用的污名與被取代的焦慮 |
| — | 會議與跨團隊協調：幾乎不變 |

## 三、洞見

- 個人省時不等於組織產出增加。丹麥全國資料顯示平均只省約 3% 工時，省下的時間轉到檢查與新任務；英國 DBT 也找不到省時轉為生產力的證據。
- 同一個人在不同任務上受益與受害並存。DBT 的會議摘要變好、Excel 分析變差；BCG 顧問在能力範圍外的任務正確率下降。賦能要以任務為單位評估，不能以人或工具為單位。
- 滿意度與效果可能不一致。DBT 72% 滿意，卻沒有生產力證據；澳洲財政部則是期望過高導致失望。導入前要先說清楚預期。
- 只有個人能自行調整的工作會改變。會議與協調不因 AI 變快，涉及多人的流程要另外規劃。
- 賦能最明確的對象是新手與原本受限的人。但新手若把學習交給 AI，也可能失去練習機會；Anthropic 員工也擔心指導新人的機會減少。
- 省下的時間去了哪裡，應該在導入前決定：拿來檢查、做原本想做卻沒時間的事，或單純減少工時。沒有決定時，多半會變成工作加密。

## 四、課程用途（候選，未定）

- 第五週「要測量什麼」：除了省下多少時間，也要看時間轉到哪裡、下游與協調是否改變、品質與錯誤，以及滿意度和實際效果是否一致。
- 用 DBT 的「會議摘要變好、Excel 分析變差、簡報快但品質差」說明要以任務為單位判斷，比整體數字更具體。
- 與課程主軸對照：賦能不是讓每個人變強，而是在適合的任務上縮小差距、擴大可做的範圍；判斷任務是否適合，仍依賴懂業務的人。
- 氣象署沒有同類評估可引用，可以說明這正是本課程要自己量測的原因。
