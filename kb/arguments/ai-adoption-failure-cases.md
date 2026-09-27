# 導入 AI 失敗的案例與原因

整理日期：2026-09-27。起因：第五週主線定為導入 AI 的兩種失敗——未經規劃而流於形式、為導入而導入而多此一舉（使用者原話：「做做樣子」「多此一舉」）；前段要給學員討論框架，需要別人的經驗作依據。由三個 sub-agent 分頭搜尋，主責整合；引用前仍須逐筆開原始連結核對。

相關：[[public-sector-ai-adoption-barriers-and-examples]]（阻礙與他國做法）、[[agent-value-workflow-and-knowledge-assets]]（價值與驗證）、[[moda-public-sector-ai-playbook]]（手冊 2.2 問題定義）。

## 一、來源

### 調查與研究

| 來源 | 量測方式 | 重點數字 | 可信度與注意 |
|---|---|---|---|
| RAND《The Root Causes of Failure for AI Projects》2024，[報告](https://www.rand.org/pubs/research_reports/RRA2680-1.html)、[簡報版](https://www.rand.org/pubs/presentations/PTA2680-1.html) | 訪談 65 位資料科學家與工程師 | AI 專案失敗率逾八成，約為一般 IT 專案兩倍 | 高。五個根因：領導層目標不清、資料品質、為用技術而用技術、部署基礎不足、問題超出 AI 能力 |
| MIT NANDA《The GenAI Divide》2025-08，[Fortune 報導](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) | 52 場訪談、153 份問卷、300 個公開案例 | 95% 試點沒有可量測的損益影響 | 方法受批評：樣本少、未經審查，且把「小規模試做後停止」也算失敗。[批評一](https://arnon.dk/mits-95-ai-failure-rate-is-wrong/)、[批評二](https://www.futuriom.com/articles/news/why-we-dont-believe-mit-nandas-werid-ai-study/2025/08) |
| Gartner 新聞稿 2024-07，[連結](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025) | 分析師預測 | 2025 年底前至少 30% 生成式 AI 專案在概念驗證後放棄 | 預測，非統計。原因：資料品質、風險控管、成本、商業價值不明 |
| Gartner 新聞稿 2025-06，[連結](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) | 分析師預測 | 2027 年底前逾 40% agentic AI 專案取消；「agent washing」 | 預測。強調取消是管理問題，不是模型能力問題 |
| S&P Global 2025-03，[CIO Dive 報導](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/) | 北美與歐洲逾千人問卷 | 放棄多數 AI 專案的企業由 17% 升至 42%；平均 46% 概念驗證未進入正式使用 | 中。建議查 S&P 官方頁面 |
| McKinsey《The State of AI》2025-03，[連結](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value) | 年度高管問卷 | 逾八成組織看不到生成式 AI 對整體獲利的影響 | 中。高管自陳 |
| BCG 2024-10 與 2025-09，[連結](https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap) | 全球企業問卷 | 74% 尚未看到可見價值 | 中。樣本數待查原文 |
| METR 隨機對照試驗 2025-07，[部落格](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)、[論文](https://arxiv.org/abs/2507.09089) | 資深開源開發者處理真實 issue | 用 AI 反而慢 19%；事前預期快 24%，事後仍自認快 20% | 高。主因是審查與整合 AI 產出的時間 |
| HBR「workslop」2025-09，[連結](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity) | 1,150 名美國全職員工 | 41% 一個月內收過 workslop，每次平均花近兩小時處理 | 高。成本轉到收件的同事身上 |
| Upwork 2024-07，[新聞稿](https://www.globenewswire.com/news-release/2024/07/23/2917274/0/en/Upwork-Study-Finds-Employee-Workloads-Rising-Despite-Increased-C-Suite-Investment-in-Artificial-Intelligence.html) | 2,500 人問卷 | 96% 高管期待提升生產力；77% 員工表示工作量反而增加 | 中。廠商調查 |
| 英國 NAO 2024-03，[報告](https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf) | 中央機關調查 | 七成在試辦或規劃，少數真正部署；缺乏成效追蹤 | 高。官方審計 |

### 案例

| 案例 | 經過 | 根因 | 可信度 |
|---|---|---|---|
| 紐約市 MyCity 聊天機器人 | 2024 年被測出建議店家扣員工小費、拒收房券等違法做法；市府只加免責聲明，持續運作近兩年，2026-01 新市長關閉。[The Markup 2024](https://themarkup.org/artificial-intelligence/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior)、[2026](https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law) | 容錯率極低的法規諮詢直接交給生成式 AI；上線前無正確率門檻，出錯後無暫停機制 | 高 |
| Deloitte 澳洲政府報告 | 2025 年替澳洲就業部撰寫的報告引用不存在的判決與論文，承認使用 GPT-4o，退還部分費用。[OECD.AI](https://oecd.ai/en/incidents/2025-10-05-be45) | 需逐條查證的引註交給 AI 產出後未查核 | 高 |
| Air Canada 聊天機器人 | 機器人說錯喪親票價退款規定，2024 年仲裁庭判公司須依機器人的說法退款，不接受「機器人自行負責」的抗辯。[ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/) | 對外答覆等同組織承諾，卻未確保與官方規定一致 | 高 |
| 英國 DSIT 試辦工具 | 2025 年推出 Redbox、Parlex、Caddy 等多項工具，數月後陸續關閉。[Global Government Forum](https://www.globalgovernmentforum.com/uk-closes-ai-pilots-amid-strategic-changes-to-prioritise-legacy-tech-overhaul/) | 試辦多、缺乏擴大採用標準與退場條件 | 中。官方說法為改用市售平台 |
| 美國聯邦機關 | 2024 年生成式 AI 用例增加近九倍，多數停在試辦。[The Register](https://www.theregister.com/2025/07/29/us_government_identified_ai_use/) | 先選工具、後補治理，缺乏成功指標 | 中 |
| 司法院判決書草稿 | 2023 年擬試辦 AI 產生判決書草稿，民間團體質疑訓練資料與偏誤後暫緩。[司法院](https://www.judicial.gov.tw/tw/cp-1887-951341-9add3-1.html)、[司改會](https://www.jrf.org.tw/articles/2550) | 風險評估、揭露與溝通落後於技術 | 高 |
| Klarna 客服 | 2023 年以 AI 取代約 700 名客服人力，2025 年執行長承認做過頭，回聘人力。[Forbes](https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/) | 客服不只是資訊處理，退款與帳務需要信任與判斷 | 高 |
| 澳洲聯邦銀行 | 2025 年以語音機器人為由裁撤 45 名客服，實際通話量上升，8 月撤回。[ABC](https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492) | 以單一指標評估效益，未驗證實際工作量 | 高 |
| 麥當勞與 IBM 點餐 | 百餘家門市測試語音點餐，錯誤頻傳，2024-06 終止。[CNBC](https://www.cnbc.com/2024/06/17/mcdonalds-to-end-ibm-ai-drive-thru-test.html) | 準確率不足，更正與善後成本超過效益 | 高 |
| 強制使用 AI | 多家企業把 AI 使用率納入績效，另有調查指員工繞過指定工具。[IT Brew](https://www.itbrew.com/stories/2026/02/27/most-companies-are-requiring-employees-to-use-ai-some-it-pros-think-that-could-backfire) | 以使用率代替解決問題作為成功指標 | 中。部分數字為媒體轉述 |
| SEC「AI washing」執法 | 2024 至 2025 年多家公司宣稱使用 AI 而實際沒有，遭裁罰。[DLA Piper](https://www.dlapiper.com/en/insights/publications/ai-outlook/2025/sec-emphasizes-focus-on-ai-washing) | 以「有 AI」作為賣點 | 高 |
| 澳洲 Robodebt、荷蘭育兒津貼 | 自動化決策（非生成式 AI）誤判大量民眾，前者和解賠償約 18 億澳幣，後者內閣總辭。[Robodebt](https://pursuit.unimelb.edu.au/articles/the-flawed-algorithm-at-the-heart-of-robodebt)、[荷蘭](https://www.lighthousereports.com/investigation/the-algorithm-addiction/) | 需個案判斷的認定工作全面自動化，移除人工複核 | 高。較早期案例 |

### 對照案例

| 案例 | 做法 | 可信度 |
|---|---|---|
| ECMWF AIFS | 2025-02 起正式營運，與物理模式並行；同時公開已知限制（極端值偏平滑、颱風強度低估）。[ECMWF](https://www.ecmwf.int/en/about/media-centre/science-blog/2023/rise-machine-learning-weather-forecasting)、[論文](https://arxiv.org/html/2509.18994v1) | 高 |
| 數發部 TryAI | 選定會議紀錄、報表審核等產出明確的工作，先試用再採購。[新聞稿](https://moda.gov.tw/press/press-releases/17952) | 中。成效數字為主管機關自述 |

### 不引用

- IBM CEO 研究的百分比：找不到對應的一手報告。
- Ford、IBM 等 2026 年回聘報導：來源多為內容農場，查無公司聲明。
- Duolingo 股價跌幅：未以一手資料核對；事件本身（2025-04 宣布 AI 優先引發反彈）可用 [TechCrunch](https://techcrunch.com/2025/08/07/the-backlash-against-duolingo-going-ai-first-didnt-even-matter/)。
- Gartner 2026-02「一半裁員企業將回聘」：屬預測，引用時須註明。

## 二、重點

失敗原因可歸成五類，前兩類對應「流於形式」，後三類對應「多此一舉」：

| 原因 | 例子 |
|---|---|
| 沒有具體問題，先有工具或口號 | RAND 的「為用技術而用技術」、強制使用率、AI washing、英國與美國聯邦試辦 |
| 沒有定義成功，也無從驗證效果 | McKinsey、BCG 看不到價值；CBA 用錯指標；NAO 缺成效追蹤；METR 的主觀感受與實測相反 |
| 檢查與修正的成本高於原本做法 | METR、workslop、Deloitte、麥當勞 |
| 做錯的代價高或難以還原 | MyCity、Air Canada、Klarna、Robodebt、荷蘭 |
| 問題本身超出 AI 能力，其他做法更合適 | RAND 第五項根因、Gartner 所說誤用場景 |

## 三、洞見

- 多數失敗原因與模型能力無關。RAND 與 Gartner 都指出主因在管理與規劃，這讓討論可以停留在業務，不需要技術背景。
- 主觀感受不能當作效果。METR 的受試者實際變慢卻自認變快；只問「用了覺得怎樣」，看不出多此一舉。
- 對外答覆由機關負責。Air Canada 與 MyCity 顯示，機器人說出的話等同組織的承諾，免責聲明無法轉移責任。
- 檢查成本可能轉嫁給別人。workslop 與 Deloitte 案例中，產出者省下時間，收件者或委託者付出查核成本。
- 試做後停止不一定是失敗。MIT 數字的批評指出，小規模試做後判斷不划算而停止是正常結果；差別在事前是否定好停止的條件。
- 做得好的例子共同點是範圍明確、並行驗證、公開限制（ECMWF、TryAI），與氣象署業務最接近的是 ECMWF。

## 四、課程用途（候選，未定）

- 第五週前段：每個討論問題配一兩個案例，說明沒有回答這一題會發生什麼；案例量不求多。
- 討論框架可能增加兩題：「如何知道真的有效，而非只是感覺有效」、「事先定好什麼情況下停止」。
- MIT 95% 可搭配批評一起給學員看，練習判斷數字的可信度。
- ECMWF 作為氣象業務的正面對照，說明並行驗證與公開限制。
