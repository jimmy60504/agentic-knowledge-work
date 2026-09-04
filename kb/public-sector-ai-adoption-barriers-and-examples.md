# 公部門用 agent 的阻礙，以及其他機關與國家已經做到的事

整理日期：2026-09-04。起因：盤點署內同仁大多停在「私下用聊天機器人」這一層，想把阻礙攤開來在課堂上討論，慢慢推動改變。

## 一、現況分層（推估，無署內資料）

| 層 | 樣子 |
|---|---|
| 0 沒用過 | 聽過，業務上沒碰 |
| 1 聊天機器人 | 免費網頁版潤稿、翻譯、擬公文草稿；私人帳號、私下用、不貼或偷偷貼內部資料。大多數 |
| 2 付費聊天 | 訂了一家，會用推理模式、上傳檔案、Deep Research、NotebookLM |
| 3 agent 工具 | 裝過 Claude Code、Codex、Antigravity，多半有程式背景 |
| 4 專案化工作 | AGENTS.md、知識庫、版本紀錄，agent 帶著檔案做事。幾乎沒有 |

可驗證的數字很少。資策會 MIC 2024 年底消費者調查：46% 用過生成式 AI、自費 17%、每天用 9%、用途八成是文字（[來源](https://mic.iii.org.tw/research.aspx?id=726)）。網傳「78% 公務員用過、19% 在機關允許下用」號稱出自國發會 2026 年 4 月調查，出處那篇文章其他數字明顯錯誤，查無原始報告，不引用。

## 二、四個阻礙

1. **指引與責任**：規則講清楚的是不能做什麼，沒說可以怎麼做，於是變成私下用、不說。
2. **帳號與費用**：機關不提供帳號，用私人帳號就不敢放公務資料，用途停在潤稿。
3. **電腦與網路**：不能自行安裝軟體、連外受限，agent 桌面程式裝不起來。
4. **心智模型**：把 AI 當問答視窗，沒體驗過「AI 在資料夾裡帶著檔案工作」。

## 三、台灣的規範與資源（其實比多數人以為的多）

- **行政院參考指引（2023-08-31 院會通過，10-03 函頒）**：產出須由承辦人做最終判斷；機密文書禁用；不得輸入應保密、個資、未經同意公開的資訊；使用應適當揭露；各機關得自訂規範或內控。[院會議案](https://www.ey.gov.tw/Page/448DE008087A1971/40c1a925-121d-4b6b-8f40-7e9e1a5401f2)、[國科會頁面](https://www.nstc.gov.tw/folksonomy/list/c79bf57b-dc94-4aff-8d14-3262b5559cfc?l=ch)。
- **行政院第 3938 次院會（2025-02-06）「公務機關使用生成式 AI 相關管理規範」**：建立 AI 評測制度（公平、準確、可靠、隱私、資安）與 AI 評測中心；機關導入 AI 業務需經評測；平台提供 10 種語言模型（含 TAIDE）與 20 項共通 AI Bots 供試用；受限產品需資安長逐級核可。[懶人包](https://www.slideshare.net/slideshow/ai-pdf-f162/275407431)。
- **數發部「公部門人工智慧應用參考手冊」**：試行版 2024-12，正式版 2025-12-17，2026-02-03 更新，附 PDF，有回饋信箱。[頁面](https://moda.gov.tw/digital-affairs/digital-service/ai-resource/18248)、[PDF](https://www-api.moda.gov.tw/File/Get/moda/zh-tw/WwHCroVhwWy52dw)。內容待讀。
- **數發部「政府 AI 應用平臺」TryAI**：針對機關「不敢用、成本高、應用少」三個痛點，先試用再採購，符合政府資安規範的環境，AI Bots 市集彙整公文助理、新聞稿生成等共通需求。[新聞稿](https://moda.gov.tw/press/press-releases/17952)。
- **國科會 2026 年「生成式 AI 與 AI Agent 工具應用之廉政風險提醒」**：資訊外洩、著作權、假訊息、資安詐騙、誠實申報五類風險；建議去識別化、實質修改、二次查證、多層驗證、誠實揭露，並優先使用機關內建置的封閉系統。[報導](https://www.cio.com.tw/116021/)。
- **TAIDE**：國科會主導的本土模型，2024-04 釋出 LX-7B 與 LX-13B，定位是可地端部署的可信任對話引擎。[維基](https://zh.wikipedia.org/zh-tw/TAIDE)、[行政院政策](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e)。

**讀法**：阻礙 1 的「沒說可以怎麼做」在中央層級其實已經開始補（手冊、TryAI、評測制度），問題是這些資源沒有下到各機關的日常，多數承辦人不知道。

## 四、台灣機關的案例

- **司法院**：2022-04 起自建模型（地端部署）產生刑事裁判草稿，先做不能安全駕駛與幫助詐欺兩類；2023 年民間團體質疑後暫停試辦。教訓是透明與範圍，而不是技術。[司法院新聞稿](https://www.judicial.gov.tw/tw/cp-1887-929494-8a9fb-1.html)、[未來城市報導](https://futurecity.cw.com.tw/article/3272)。
- **地方政府**：台北、新北、桃園、新竹、台中、高雄等有內部試行 SOP；台南推生成式 AI 學習平台；花蓮鼓勵以 ChatGPT 寫新聞稿（來源為搜尋摘要，各案細節待查證）。
- **公文系統廠商**：叡揚 2024-09 推「公文 AI 助理」對話式生成公文，2026-03 研討會分享校務導入經驗。代表公文場景已有現成產品，課程的差異在人的判斷與可回溯，不在生成本身。[叡揚](https://www.gss.com.tw/focus/news-center/4003-speednews20240902_AI_Gen_OD)。

## 五、國外公務體系的做法

- **新加坡 Pair（GovTech / OGP）**：Pair Chat、Pair Search、自訂助理、會議紀錄。公務員用政府設備即可用，可處理 Restricted、Sensitive、Normal 等級資料，資料留在政府環境。試用兩個月內破 11,000 人、100 多個機關；累計 6 萬註冊、每週 2 萬活躍、千萬則訊息，估計省下 46% 行政時間。**解的是阻礙 1 與 2：政府自己提供帳號與合規環境。** [GovTech](https://www.tech.gov.sg/products-and-services/for-government-agencies/productivity-and-marketing/pair/)、[UNDP](https://www.undp.org/policy-centre/singapore/blog/pairing-ai-public-sector-impact-singapore)。
- **英國 Humphrey 與 Copilot 試驗**：2024-09 至 12 月 12 個部會 2 萬名公務員試用 M365 Copilot，平均每天省 26 分鐘，寫文件與做簡報省最多（24 與 19 分鐘），82% 不想回到沒有工具的狀態，17% 沒省到時間；2025-01 推出公務員專用工具組 Humphrey。**解的是阻礙 2 與 4：組織買單，並用試驗數據說服。** [The Register](https://www.theregister.com/2025/06/03/uk_government_study_ai_time_savings/)、[UK Parliament 書面聲明](https://questions-statements.parliament.uk/written-statements/detail/2025-06-02/hlws667)。
- **美國 GSA OneGov**：2025-08 起 ChatGPT Enterprise、Claude for Government 各以每機關每年 1 美元供應，Gemini for Government 0.47 美元。後續有政策變動（Anthropic 一度遭禁用並提訴），代表供應商依賴是新風險。**解的是阻礙 2，用集中採購把價格談到零。** [GSA 新聞稿](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-strikes-onegov-deal-with-anthropic-08122025)、[FedScoop](https://fedscoop.com/openai-chatgpt-enterprise-federal-government-gsa-deal-general-services-administration-anthropic/)。

共同點：三個國家都是**政府出面提供帳號與合規環境**，而不是要求個人自己解決。台灣中央已有 TryAI 與評測平台，缺的是下放到機關日常。

## 六、對課程的用法（候選，未定）

- 第二週或風險週開一個討論段：把四個阻礙攤開，問學員各自卡在哪一個；把新加坡、英國的做法當「別人已經解掉了」的參照。
- 專案化本身就是合規的做法：資料夾是邊界、工作紀錄與 commit 是揭露與負責的證據、AGENTS.md 是人審過的判斷標準。可以直接對照行政院指引的三項要求講。
- 資安邊界提早到第二週講，附「哪些可以放進專案、哪些不行」清單，依指引與國科會五類風險整理。
- 課堂上記錄免費額度用完人數與卡點，加上英國試驗的數字，作為署內採購的依據；TryAI 是可以建議機關走的正式管道。
- 數發部手冊已讀，整理在 [[moda-public-sector-ai-playbook]]：手冊管的是機關導入 AI 系統，承辦人日常使用幾乎沒寫，課程補的正是這一層；可直接引用的是 2.2 問題定義格式、3.5 訓練檢核、4.2.17、4.3.6、4.4.3。
