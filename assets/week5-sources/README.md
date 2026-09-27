# 第五週來源截圖

截取日期：2026-09-27、2026-09-28。以 headless Chrome 截取 1440×900 的首屏，PDF 取第一頁。用途是投影片中介紹來源、讓聽眾看到資料真實存在；內容主張與數字以 kb 筆記為準。圖片檔依 `.gitignore` 不進 git，只保存在本機與 OneDrive。

新聞與網站截圖屬原網站著作，僅供課堂介紹出處使用，投影片需標示來源。

檔名前綴 s6 為早期命名，對應草稿第七步「條件」；草稿第六步「對象」目前無截圖。

## 篩選原則（2026-09-28 使用者要求）

保留 agent 大量使用後仍成立的結論。依賴工具能力的結論（變快多少、哪類任務做得差、錯誤率）以 2023 至 2024 年聊天工具量得，已刪除；依賴人與組織的結論（問題定義、時間紅利、考核與動機、主管）保留；agent 時代的證據補上。

補充原則（2026-09-28 使用者）：agent 產出幾乎不需檢查，大約是 2026 年 4、5 月的事。此前的「能力做不到」類負面結論多已過時；此前的「做得到」類正面案例（如補測試、做雛形），工具變強後只會更成立，可保留但標示年份。

## agent 時代的證據

| 檔案 | 步驟 | 來源 | 要點 |
|---|---|---|---|
| `s1-anthropic-teams-claude-code.png` | 一 | [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)（Anthropic，2025-07-24） | 做不到→能做：法務自建電話樹雛形、行銷自建廣告生成流程；設計團隊補寫測試。公司自陳 |
| `s1-lenny-pm-prototyping.png` | 一 | [How to get your entire team prototyping with AI](https://www.lennysnewsletter.com/p/how-to-get-your-entire-team-prototyping)（Colin Matthews，Lenny's Newsletter，2025-06-10） | 做不到→能做：教過 500 多位 PM 用 AI 做雛形 |
| `s1-airbnb-test-migration.png` | 一 | [Accelerating Large-Scale Test Migration with LLMs](https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/)（Airbnb，2025） | 沒時間→有時間：約 3,500 個測試檔遷移，原估 1.5 年，6 週完成 |
| `s1-devopsdays-tpe-smartnews.png` | 一 | [Creating "Awesome Change" in SmartNews](https://speakerdeck.com/martin_lover/devopsdays-taipei-2025-creating-awesome-change-in-smartnews)（Ikuo Suyama，DevOpsDays Taipei 2025） | 沒時間→有時間：以 LLM 補測試、提升覆蓋率；台灣年會分享 |
| `s1-meta-testgen-llm.png` | 一 | [Automated Unit Test Improvement using LLMs at Meta](https://arxiv.org/abs/2402.09171)（Meta，FSE 2024） | 沒時間→有時間：73% 的測試建議被工程師採納 |
| `s1-anthropic-internal-study.png` | 一 | [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)（Anthropic，2025-12-02） | 工程師大量使用 Claude Code，約 27% 是原本不會做的工作；也擔心指導新人的機會減少 |
| `s3-hbr-intensifies.png` | 三 | [AI Doesn't Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)（HBR，2026-02） | 同時處理多條工作、反覆檢查 AI 產出，工作加密；頁首有廣告 |
| `s3-metr-2026-update.png` | 三 | [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)（METR，2026-02-24） | 開發者不願在沒有 AI 的情況下工作，同時使用多個 agent 時連耗時都量不準；取代 2025 年的舊研究 |
| `s3-quanta-erdos-ai.png` | 三 | [Why the Legendary Erdős Problems Are Falling to AI](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)（Quanta Magazine，2026-08-03） | 數學容易驗證所以 AI 能解，但找到答案不等於推進理解 |
| `s4-ms-work-trend-index-2026.png` | 五 | [Agents, human agency, and the opportunity for every organization](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)（Microsoft，2026-05-05） | 人的工作轉向定方向、定標準、看結果 |
| `s3-allwork-added-tasks.png` | 三 | [31% Of Workers Say AI Added Tasks](https://allwork.space/2026/02/31-of-workers-say-ai-added-tasks-instead-of-saving-time-at-work)（Allwork，2026-02） | 媒體整理，可信度中等；頁首有廣告 |

## 不依賴工具能力，保留

| 檔案 | 步驟 | 來源 | 要點 |
|---|---|---|---|
| `s1-pg-cybernetic-teammate.png` | 一 | [The Cybernetic Teammate](https://www.nber.org/papers/w33641)（NBER） | 一人加 AI 追平兩人團隊、跨職能觀點；工具變強只會更成立；有 cookie 框 |
| `s2-rand-root-causes.png` | 二 | [Root Causes of Failure for AI Projects](https://www.rand.org/pubs/research_reports/RRA2680-1.html)（RAND 2024） | 五個根因，多與模型無關 |
| `s2-oecd-governing-with-ai.png` | 二 | [Governing with Artificial Intelligence](https://www.oecd.org/en/publications/governing-with-artificial-intelligence_795de142-en.html)（OECD 2025） | 兩百個政府案例，多數停在試點 |
| `s2-uk-ai-pilots-closed.png` | 二 | [UK closes AI pilots](https://www.globalgovernmentforum.com/uk-closes-ai-pilots-amid-strategic-changes-to-prioritise-legacy-tech-overhaul/)（Global Government Forum） | 流於形式；有 cookie 框 |
| `s2-us-federal-pilots.png` | 二 | [US agencies log nearly 9x more GenAI use cases](https://www.theregister.com/2025/07/29/us_government_identified_ai_use/)（The Register） | 流於形式；頁首有廣告 |
| `s2-cba-reverses-cuts.png` | 二 | [CBA backtracks on AI job cuts](https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492)（ABC News） | 用錯指標 |
| `s2-deloitte-report-incident.png` | 二 | [Deloitte Refunds Australia](https://oecd.ai/en/incidents/2025-10-05-be45)（OECD.AI） | 多此一舉；查核責任 |
| `s2-shu-ltn-ai-replaces-office.png` | 二 | [世新砍光系辦、拔行政權限「改用AI」](https://news.ltn.com.tw/news/life/breakingnews/5582285)（自由時報，2026-09-22） | 台灣案例；頁面有廣告與訂閱提示 |
| `s2-shu-ctwant-ai-no-answer.png` | 二 | [世新大亂象1／問事全推AI「查無此題」](https://www.ctwant.com/article/499621/)（CTWANT，2026-09-25） | 台灣案例；有廣告與 cookie 提示。校方說法見[太報／Yahoo](https://tw.news.yahoo.com/%E7%B3%BB%E8%BE%A6%E8%A2%AB%E7%A0%8D-%E6%94%B9%E5%95%8Fai-%E5%AD%B8%E7%94%9F%E6%8A%B1%E6%80%A8%E9%80%A3%E9%80%A3-%E4%B8%96%E6%96%B0%E5%A4%A7%E5%AD%B8-%E5%9B%9E%E6%AD%B8-134642655.html)，截圖未取得 |
| `s2-judicial-ai-draft-paused.png` | 二 | [生成式AI導入司法判決書系統喊停](https://futurecity.cw.com.tw/article/3272)（未來城市） | 台灣案例：司法院；有 cookie 提示與頂部廣告位 |
| `s2b-robodebt-algorithm.png` | 二 | [The flawed algorithm at the heart of Robodebt](https://pursuit.unimelb.edu.au/articles/the-flawed-algorithm-at-the-heart-of-robodebt)（墨爾本大學 Pursuit） | 完全取代：移除人工複核；較早期自動化決策；有 cookie 框 |
| `s2b-stanford-canaries.png` | 二 | [No Widespread Displacement, but the AI Employment Gap for Young Workers Has Widened to 19%](https://digitaleconomy.stanford.edu/news/canariesaug26/)（史丹佛數位經濟實驗室，2026-08-12） | 取代多在任務層級，新進人員受影響；頁面有半透明遮罩 |
| `s2-nyc-mycity-2024.png` | 二 | [Malfunctioning NYC AI Chatbot](https://themarkup.org/artificial-intelligence/2024/04/02/malfunctioning-nyc-ai-chatbot-still-active-despite-widespread-evidence-its-encouraging-illegal-behavior)（The Markup） | 多此一舉；與下一張擇一 |
| `s2-nyc-mycity-2026.png` | 二 | [Mamdani to kill the NYC AI chatbot](https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law)（The Markup） | 同一事件的結局 |
| `s3-humlum-denmark.png` | 三 | [Still Waters, Rapid Currents](https://www.nber.org/papers/w33777)（NBER） | 省下的時間轉為檢查與新任務；有 cookie 框 |
| `s3-hbr-workslop.png` | 三 | [AI-Generated "Workslop"](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)（HBR 2025） | 查核成本轉給別人；頁首有廣告 |
| `s3-kpmg-trust-study.png` | 三 | [Trust, attitudes and use of AI 2025](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html)（KPMG） | 57% 隱藏使用；有 cookie 框 |
| `s4-deci-koestner-ryan-1999.png` | 四 | [Deci、Koestner、Ryan](https://www.selfdeterminationtheory.org/SDT/documents/2001_DeciKoestnerRyan.pdf)（PDF） | 獎勵削弱內在動機 |
| `s4b-dora-2025.png` | 四（評估） | [DORA Research: 2025](https://dora.dev/dora-report-2025/)（Google Cloud DORA） | AI 是放大器、返工率；頁面有繁體中文摘要版可供學員閱讀 |
| `s4b-oecd-dgo-2026.png` | 四（評估） | [Digital Government Outlook 2026](https://www.oecd.org/en/publications/digital-government-outlook_0496b2bc-en/)（OECD，2026-06-15） | 政府 AI 影響評估最落後 |
| `s6-singapore-pair.png` | 七 | [Pair](https://www.tech.gov.sg/products-and-services/for-government-agencies/productivity-and-marketing/pair/)（GovTech） | 政府提供環境；有 cookie 框 |
| `s6-uk-copilot-statement.png` | 七 | [AI in Government: Cross Government Experiment Report](https://questions-statements.parliament.uk/written-statements/detail/2025-06-02/hlws667)（英國國會） | 政府提供環境；有 cookie 框 |
| `s6-gsa-onegov.png` | 七 | [GSA OneGov deal with Anthropic](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-strikes-onegov-deal-with-anthropic-08122025)（GSA） | 集中採購 |
| `s6-gallup-global-workplace.png` | 七 | [State of the Global Workplace](https://www.gallup.com/workplace/349484/state-of-the-global-workplace.aspx)（Gallup） | 主管的影響；有 cookie 框 |
| `s7-ey-genai-guideline.png` | 七 | [行政院及所屬機關(構)使用生成式AI參考指引](https://www.ey.gov.tw/Page/448DE008087A1971/40c1a925-121d-4b6b-8f40-7e9e1a5401f2)（行政院） | 台灣已有的資源 |
| `s7-moda-ai-playbook.png` | 七 | [公部門人工智慧應用參考手冊](https://moda.gov.tw/digital-affairs/digital-service/ai-resource/18248)（數發部） | 台灣已有的資源 |
| `s6-moda-tryai.png` | 七 | [政府 AI 應用平臺](https://moda.gov.tw/press/press-releases/17952)（數發部） | 台灣的環境 |
| `x-ecmwf-ml-forecasting.png` | 備用 | [The rise of machine learning in weather forecasting](https://www.ecmwf.int/en/about/media-centre/science-blog/2023/rise-machine-learning-weather-forecasting)（ECMWF） | 氣象業務的正面例子 |

## 已刪除（依賴聊天時代的工具能力）

- METR 2025 隨機對照試驗：官方已註明過時，改用 2026 追蹤。
- 英國商業貿易部 Copilot 評估（The Register 與官方部落格）：Excel、簡報表現屬 2024 年 Copilot 能力。
- Brynjolfsson 客服研究：2020 至 2021 年的工具。
- 澳洲財政部 Copilot 評估（The Register 與 PDF）：評估 2024 年 Copilot；期望落差改以講師自身經驗說明。
- iThome 2025 CIO 大調查：資料為 2025 年，早於 2026 年 4、5 月 agent 產出品質明顯提升的時間點，屬能力限制類的負面結論，已過時（使用者 2026-09-28）。
- Axios 報導 Anthropic 研究：內容為另一份就業影響研究，與內部研究不同，避免混淆。

未取得：Workday〈Beyond Productivity〉頁面（截圖逾時，連結 https://www.workday.com/en-us/artificial-intelligence/research/beyond-productivity-ai-value.html ）；Klarna 回聘人力（Forbes 阻擋、CX Dive 為廣告頁，改附連結 https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/ ）；Lyytinen 與 Hirschheim 1987（ResearchGate 阻擋）。
