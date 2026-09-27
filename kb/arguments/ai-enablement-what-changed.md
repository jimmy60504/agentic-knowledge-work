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
| Anthropic 內部研究 2025，[Anthropic 研究頁](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) | 132 人問卷、53 人訪談 | 可完全交出的工作約 0 至 20%，多為容易驗證或枯燥的任務 | 27% 是原本不會去做的工作 | 與同事協作與指導新人的機會減少 |
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

## 五、兩種賦能方式的對照（2026-09-27 補）

使用者記得聽過的說法：Agent 賦能個人有兩種，「以前做不到的現在能做」與「以前沒時間做的現在有時間做」。使用者舉的例子：PM 以前不會寫程式，現在可以寫簡單的小工具；RD 以前沒時間做 CI/CD 與測試，現在終於有時間把事情做好。原始出處待確認；Anthropic 內部研究同時有兩種描述：27% 是原本不會去做的工作（擴大專案、可有可無的儀表板、探索），工程師也能做超出原本專長的任務。

| | 以前做不到，現在能做 | 以前沒時間做，現在有時間做 |
|---|---|---|
| 證據 | P&G 一人跨職能；客服新手追上；Anthropic 工程師做超出專長的任務 | Anthropic 27% 原本不會做的工作；丹麥研究中省下的時間轉入新任務 |
| 主要風險 | 超出自己能判斷的範圍，錯了也看不出（BCG 範圍外正確率低 19 個百分點）；與課程「放大器」主張相衝突之處 | 做了但沒人用，或工作加密（柏克萊研究）；容易流於形式 |
| 規劃重點 | 自己是否知道好的結果長什麼樣；誰能檢查 | 這件事做出來給誰用、有何價值；原本的工作是否因此被擠壓 |
| 基準 | 以前由誰做、外包或請人協助的成本 | 沒有現行做法可比，改問不做會怎樣 |

讀法：課程主張 Agent 放大人本來就會的東西。「做不到」若指缺乏判斷能力，就不適合交給 Agent；若指知道要什麼、只是不熟操作（第二週的「有想法但不熟悉工具操作」），才是合適的賦能。

兩個例子都是合適的版本，可作為判斷的參照：

- PM 寫小工具：PM 清楚工具要解決什麼、結果對不對，缺的只是寫程式的操作；小工具自己使用，做錯的代價低。對應「知道要什麼、只是不熟操作」。
- RD 做 CI/CD 與測試：省下的時間用在把原本的工作做好，而不是做更多新東西；測試與自動部署本身就是檢查機制，會降低之後檢查 Agent 產出的成本。對應「省下的時間用在哪裡」的好答案。
- 反面版本：不懂業務的人用 Agent 做出看似完整的分析（做不到而且審不出）；省下的時間拿去接更多工作，而品質沒有改善（工作加密）。

## 六、省下的時間歸誰（2026-09-27 補）

起因：使用者提到新聞說導入 AI 後越來越忙，省下的時間紅利被公司吸收，員工因此不想用 AI，以免被塞更多工作。由 sub-agent 搜尋。

### 員工隱藏 AI 使用

| 來源 | 樣本 | 數字 | 原因 | 可信度 |
|---|---|---|---|---|
| KPMG 與墨爾本大學 2025-04，[連結](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html) | 47 國逾 48,000 人 | 57% 隱藏使用、把 AI 產出當自己的成果；66% 不驗證輸出 | 政策與信任落差 | 高 |
| Ivanti 2025-05，[新聞稿](https://www.ivanti.com/company/press-releases/2025/nearly-a-third-of-employees-are-keeping-their-ai-driven-productivity-a-secret-finds-ivanti-research) | 逾 6,000 名員工 | 約三分之一隱藏使用 | 36% 想保有優勢、30% 怕被裁、27% 怕能力被質疑 | 中。廠商調查 |
| Slack Workforce Lab 2024，[連結](https://slack.com/blog/transformation/how-workers-really-feel-about-ai) | 美國辦公室員工 | 48% 不願讓主管知道用 AI 做常見任務 | 怕被認為能力不足或作弊 | 中高 |
| Forbes 2026-08，[連結](https://www.forbes.com/sites/niritcohen/2026/08/02/ai-saves-time-66-of-employees-stay-online-to-hide-it/) | 未查到原始調查 | 66% 完成工作後仍掛線上裝忙，每週近 5 小時 | 怕被指派更多工作 | 中低。須查原始調查 |

Ethan Mollick 稱為「秘密半機械人」：規範只談禁止，員工改用私人帳號、不分享方法，組織學不到經驗。[One Useful Thing](https://www.oneusefulthing.org/p/detecting-the-secret-cyborgs)

### 省下的時間被吸收

| 來源 | 數字 | 可信度 |
|---|---|---|
| Workday 2026-01，[新聞稿](https://newsroom.workday.com/2026-01-14-New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table) | 3,200 名 AI 使用者；企業把省下的時間用於增加工作量者多於投入員工發展 | 中高。廠商委託 |
| Upwork 2025-07，[新聞稿](https://investors.upwork.com/news-releases/news-release-details/upwork-research-reveals-new-insights-ai-human-work-dynamic) | 生產力提升最多的 AI 使用者 88% 有倦怠，離職意願為低度使用者兩倍 | 高 |
| Allwork 2026-02，[連結](https://allwork.space/2026/02/31-of-workers-say-ai-added-tasks-instead-of-saving-time-at-work) | 31% 工作量增加、16% 減少；近半數表示主管派工時直接以「有 AI 可用」為由 | 中。媒體整理 |
| CIO Dive 2026，[連結](https://www.ciodive.com/news/workers-spend-more-time-managing-ai/822554/) | 省下的時間大量用於管理與校正 AI 輸出 | 中 |
| Orange Hello Future 整理 arXiv 2602.12695，[連結](https://hellofuture.orange.com/en/the-ai-productivity-paradox-the-new-tech-may-be-eating-into-your-leisure-time/) | 高度暴露者每週工時增加約 3 小時，休閒等量減少 | 中。須讀原論文 |

台灣未找到專門調查或深度報導。

### 把時間還給員工的做法

- 四天工作週試辦（Nature Human Behaviour 2025-07，141 家組織、2,896 人）：倦怠下降、身心改善，九成以上企業續行。[Autonomy](https://autonomy.work/portfolio/uk4dwpilotresults/)。注意：試辦本身與 AI 無直接關係，未量測企業生產力。
- OpenAI 2026-04 政策提案建議以誘因推動不減薪的四天工作制，屬倡議。[Forbes](https://www.forbes.com/sites/jodiecook/2026/04/28/openai-just-proposed-a-4-day-work-week-what-aprils-ai-news-means-for-you/)

### 洞見

- 越有效率、越忙、越要隱藏，形成循環；受益最多的人最傾向隱藏，組織因此看不到真正有效的用法，也無法擴散。
- 這是內驅力問題在組織層級的樣子：用 AI 對當事人無益（只換來更多工作），人就不會自發使用或分享。
- 隱藏使用也帶來風險：不驗證輸出、把公司資料放上公開平台，都發生在沒人知道的地方。
- 「省下的時間用在哪裡」須在導入前由當事人與主管說定；公部門以人力編制與業務量計算，這個問題可能更敏感。

### 兩種賦能的實際案例（2026-09-28 補）

使用者要求為 PM 與 RD 的例子找年會分享或文章。由 sub-agent 搜尋，截圖在 `assets/week5-sources/`。

- **做不到→能做**
  - [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)（2025-07）：法務自建電話樹雛形；成長行銷自建讀取廣告成效、生成新廣告的流程；Figma 外掛一次產生上百組廣告變體。公司自陳。
  - Colin Matthews〈[How to get your entire team prototyping with AI](https://www.lennysnewsletter.com/p/how-to-get-your-entire-team-prototyping)〉（Lenny's Newsletter，2025-06）：教過 500 多位 PM 用 v0、Bolt、Cursor 等工具做雛形。
  - 學術：〈[Vibe Coding in Product Teams](https://arxiv.org/pdf/2509.10652)〉（2025）：效率提升，也帶來信任與責任歸屬的新張力。
  - 台灣：僅查到社群發文，未找到具名的年會分享。
- **沒時間→有時間**
  - Airbnb〈[Accelerating Large-Scale Test Migration with LLMs](https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/)〉（2025）：約 3,500 個測試檔遷移，原估 1.5 年，6 週完成，自動成功率 97%。
  - Meta〈[Automated Unit Test Improvement using LLMs](https://arxiv.org/abs/2402.09171)〉（FSE 2024）：73% 的測試改善建議被工程師採納上線。
  - Google〈[Accelerating code migrations with AI](https://research.google/blog/accelerating-code-migrations-with-ai/)〉（2024）與 ICSE 2025 論文：遷移時間約省一半。
  - 台灣：DevOpsDays Taipei 2025，SmartNews 的 Ikuo Suyama〈[Creating "Awesome Change" in SmartNews](https://speakerdeck.com/martin_lover/devopsdays-taipei-2025-creating-awesome-change-in-smartnews)〉：過去趕工使測試被犧牲，以 LLM 協助補測試、提升覆蓋率。
- ~~反面提醒：iThome 2025 CIO 大調查~~：2026-09-28 使用者指出資料早於 2026 年 4、5 月 agent 產出品質提升的時間點，無法說明現況，不採用。

### 可驗證性決定賦能能走多遠（2026-09-28 使用者）

使用者：程式碼可以用測試驗證，不是 LLM 自己球員兼裁判；agent 可能偷改測試，但做隔離與限制即可處理。文獻是否存在、文件是否正確，很難用寫好的測試檢查，否則不需要 LLM 處理複雜的文字理解。

- 兩種賦能的成功案例多來自程式（Airbnb、Meta、Google、SmartNews），這與程式碼有外部檢查機制有關，不能直接類推到文書工作。
- 文書任務可以部分檢查（例如以 DOI 確認文獻存在），但「來源是否支持這個主張」仍需理解內容，檢查落回人的判斷。Deloitte 案例因此不因工具變強而過時。
- 選擇導入方向時，優先找有外部檢查方式的任務：測試、既有規則、已知答案。檢查者與產出者要分開，對應導入前規劃第 5 題。
- （agent 補充，待確認）氣象業務有不少可驗證的部分，例如資料品管規則、格式檢查、預報校驗；這類任務可能較適合先導入。

補充（同日使用者）：PM 或領域專家做出的小工具，本人就能驗證結果，這也是一種測試。由 LLM 在執行時直接產出文字對外的應用（聊天機器人）沒有機會先被檢查；程式則測試過才上線、行為固定，兩者本質不同。對應第四週六種介入方式：交辦（人檢查成品）與製作工具（AI 只在建置時參與）有檢查點；模型在流程中執行且直接對外時，缺少檢查點。

### 外部驗證是關鍵，但驗證不等於理解（2026-09-28 使用者）

使用者歸納：重點在於有沒有辦法外部驗證。查核成本高的是沒有外部檢查方式的產出，文字大多如此，沒有測試的程式碼亦同（workslop 定義含程式碼，[BetterUp](https://www.betterup.com/workslop)）；有明確標準的文字也能檢查（廣告成效、會議紀錄格式）。第五週草稿因此將三個失敗改寫為三種驗證問題：產出能不能驗證、成效能不能驗證、驗證的人還在不在。

使用者另舉數學為例：數學答案對不對很好驗證，所以 AI 能解題；但數學家認為單純找到答案無法推進人類對數學的理解。

- [Quanta Magazine〈Why the Legendary Erdős Problems Are Falling to AI〉](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)（2026-08-03）：形式化驗證工具（Harmonic 的 Aristotle）讓非專家也能確認證明成立；Thomas Bloom 擔心上百頁無人閱讀的 AI 證明；Wouter van Doorn 表示自己寫的證明比 ChatGPT 的更簡潔、更一般化、更易讀；Noga Alon 則因 AI 能解而放棄這類問題。
- Terence Tao 維護的 [AI 對 Erdős 問題的貢獻](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)；Tao 指出許多問題過去沒人認真嘗試，現有工具能在少量引導下解決的僅約一到二成（[Scientific American](https://www.scientificamerican.com/article/ai-uncovers-solutions-to-erdos-problems-moving-closer-to-transforming-math/)，比例待核對原文）。
- 洞見：通過檢查代表結果正確，不代表人理解問題或工作真正推進；與「做好工作」、「判斷如何累積」相連。

### 決策疲勞與認知負荷（2026-09-28）

使用者問決策疲勞如何放入第五週，並提出可連到認知負荷的觀念。

- 位置：驗證的人不只要在流程中，還要負荷得了；負荷過重時驗證變成蓋章，形同移除驗證者。
- 認知負荷理論（Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2)，原為教學設計理論，出處待核對）將負荷分為內在、外在、增生三類。對應到驗證工作：
  - 內在負荷＝判斷本身，應由人保留。
  - 外在負荷＝產出呈現與工作切換造成的負擔，應由 Agent 預處理、外部檢查減少。
  - 增生負荷＝形成理解的投入，應保留；全部交出會只得到答案而沒有理解（數學例子），也使新進人員失去練習。
- 佐證：HBR 2026 工作加密研究（認知疲勞、決策品質下降）；Upwork 2025（高產能 AI 使用者 88% 倦怠）；Microsoft 與 CMU 2025（越信任 AI，投入的批判思考越少）。
- 注意：「決策疲勞」常引用的假釋法官研究（Danziger 等 2011）與自我耗損研究有重現爭議，課堂以認知負荷理論與 AI 工作研究為主，不引用該研究。
