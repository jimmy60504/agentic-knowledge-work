# 外部組織如何用 Agent 補業務缺口（2026-09）

> 狀態（2026-09-19）：案例表已併入 [[agent-use-patterns]] 的用法樣式；本檔保留來源連結與證據限制。

## 來源

- 查核日：2026-09-19。此處的 Agent 指能依目標跨步驟查找資料、使用工具、產生或更新工作成果，並交由人或系統驗收的 AI 工作流；不把所有聊天問答或傳統規則自動化都算進來。
- [McKinsey《The state of AI in 2025》](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf)：2025 年 6–7 月對 1,993 人的調查，用於掌握採用階段與部門分布；是受訪者回報，非全球企業普查。
- [Microsoft 2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)：20,000 名使用 AI 的工作者問卷及 Microsoft 365 使用訊號；樣本限十個市場及其產品生態。
- [Microsoft Agent 用例與衡量指標藍圖](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-business-value-use-case-blueprints)：列 16 個常見業務功能及可量測指標；是供選題的產品指南，不能當成實際部署率。
- 以下公司實例為公司／供應商公開案例，能說明工作做法；案例中的省時與成效多由當事企業自述，未作獨立驗證，也不能直接外推至其他組織。

## 重點

### 先看普及程度

McKinsey 的 2025 調查中，23% 受訪者表示所屬組織已在至少一項功能擴大 Agent 使用，另 39% 正在試驗；但**任一單一業務功能中，回報已擴大的受訪者都不超過 10%**。IT 和知識管理的 Agent 使用最常被回報；報告舉服務台管理與深入研究為例。因此「很多人在試」與「多數業務已成熟上線」須分開說。

### 外部案例：工作缺口 → Agent 的位置

| 業務缺口 | Agent 具體工作 | 人保留的工作與驗收 | 公開案例與證據性質 |
|---|---|---|---|
| 大量重複詢問，值班或服務人員反覆查同一套資訊 | 依個案查知識庫、回答例行問題、收集脈絡；不能解決時摘要並轉交 | 維護正確知識、處理例外與敏感情境、抽查回答 | [Newfront 保險福利助理](https://www.anthropic.com/customers/newfront)提供員工即時問答；[ServiceNow 自家 IT 服務台](https://www.servicenow.com/customers/now-on-now-autonomous-it-service-desk.html)處理符合條件的一線事件。兩者為業者案例。 |
| 資料散在文件、系統和歷史紀錄，查找與整合占去分析時間 | 跨來源檢索、整理相互矛盾的資料、附來源形成研究初稿 | 定義問題、檢查證據及重要判斷、決定結論 | [Schroders 投資研究助理](https://cloud.google.com/blog/topics/customers/how-schroders-built-its-multi-agent-financial-analysis-research-assistant)為原型；[Balyasny 投資研究系統](https://openai.com/index/balyasny-asset-management/)為公司公開的實際使用案例。 |
| 大量非結構化文件需要轉成欄位，例外條款容易漏看 | 讀取 PDF／掃描件、抽取欄位、標記非標準條件與原文位置 | 檢查欄位與例外、決定解釋及後續處置 | [OpenAI 內部合約資料 Agent](https://openai.com/index/openai-contract-data-agent/)從合約抽取資料，將非標準條款交財務人員審核；[Newfront](https://www.anthropic.com/customers/newfront)處理格式不一的保險文件。 |
| 警報、工單或事件多，專業人員難以逐件查上下文 | 自動彙集事件紀錄、查相似案例、初步分級、建議調查方向與處置 | 確認真正風險、處理重大事件、修正分級與處置規則 | [Trellix 資安警報分析](https://www.anthropic.com/customers/trellix)由 Agent 調查警報並提供脈絡；[ServiceNow 服務台](https://www.servicenow.com/customers/now-on-now-autonomous-it-service-desk.html)以歷史與即時資料支援事件分類和處理。 |
| 一項工作橫跨多個工具，人工複製、交接與追進度耗時 | 按流程查資料、填系統、建立工作項目、產出下一步所需內容；在核准點暫停 | 訂權限、核准對外或高影響動作、處理失敗與回復 | [ServiceNow 自家 IT 服務台](https://www.servicenow.com/customers/now-on-now-autonomous-it-service-desk.html)由 Agent 啟動處理流程；[OpenAI 內部合約 Agent](https://openai.com/index/openai-contract-data-agent/)將抽取、查證、審核串成工作流。 |
| 專業人員時間不足，研究、程式、資料表或文件的第一版做不完 | 接受任務後蒐集素材、寫程式或分析、形成可檢查的檔案與草稿 | 設定標準、執行測試、檢查數值及來源、接受或退回成品 | [OpenAI 內部跨部門 Codex 使用研究](https://openai.com/index/how-agents-are-transforming-work/)顯示工程以外部門也用 Agent 完成知識工作；[Stampli 產品發布](https://openai.com/index/stampli/)用 Agent 製作多種可審閱素材，對外內容仍由人核准。 |
| 銷售與行銷需要按客戶脈絡準備材料，但蒐集與改寫占去大量時間 | 查客戶／市場資料、依既定標準準備提案、更新 CRM 或製作素材 | 決定客戶策略、核對主張與承諾、核准對外溝通 | [OpenAI 自家銷售流程](https://openai.com/index/next-phase-of-enterprise-ai/)使用 Agent 研究及評分潛在客戶；[Stampli 發布案例](https://openai.com/index/stampli/)跨文案、設計與業務素材製作。前者含主動寄信，不能直接套到其他機關。 |

### 橫向歸納：缺口其實常長這樣

1. **量超過人能逐件處理的速度**：詢問、合約、警報或例行工單累積；Agent 先處理可定義的部分，把例外交人。
2. **資訊存在，但分散且難以追溯**：找資料、核對版本與來源的時間大於分析時間；Agent 先彙整成有來源的工作底稿。
3. **資料格式與系統交界需要人工搬運**：PDF、郵件、表格與業務系統之間的轉換反覆發生；Agent 協助抽取、比對、填入與留下紀錄。
4. **工作可拆解，卻常卡在初稿或交接**：研究、程式、報告與對外素材需要多種技能和工具；Agent 產出可檢查的中間成果，人決定方向與通過標準。
5. **例外少但代價高**：大量正常件可加速，但重大或模糊個案必須留有升級、核准、回退與稽核路徑。

以上是從案例抽出的**選題假說**，不是「Agent 一定能補上」的結論。若規則固定、輸入整齊、可用普通程式穩定處理，應先評估既有自動化；Agent 的增加價值通常在跨來源語意理解、彈性步驟與產生可審閱成果。

### 怎麼判斷一個缺口值得試

可先挑一件頻繁、耗時、輸入與產出說得清楚、錯誤可被人快速看出的工作。對照原流程記錄：每件處理時間、等待／交接時間、品質或錯誤、例外比例、審核與返工時間、工具成本。試作時保留來源、執行紀錄、權限邊界與人工核准點；若審核負擔超過節省時間，需縮小任務或改流程。衡量角度參照 [Microsoft 用例藍圖](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-business-value-use-case-blueprints)，不是照抄其示例數字。

## 洞見

- 外部案例較一致的切入點是**把人接手前的準備工作做完整**：查資料、整理脈絡、標記例外、產出可追溯底稿。這是對案例的綜合推論，不是調查證明的因果結論。
- 跨部門或高風險流程的價值，不只看 Agent 能做幾步，還要看交接後的人是否更容易查證與決定。把未標示來源的漂亮初稿交給審查者，可能只是移轉負擔。
- 公司案例偏向願意公開成果的使用者；供應商頁面往往挑選成功個案。2025 調查顯示多數組織尚未在單一功能規模化，討論時應把案例視為「做法」，不要視為平均效果。
- 這些外部模式可用來**產生訪談問題**，尚不能證明地震測報中心有相同缺口。可連到 [[cwa-earthquake-center-business-map]] 和 [[workshop-root-cause-and-value-discovery]]，逐項查實際工作量、交接、例外與責任。

## 課程用途（候選）

- 作為第四週工作坊的外部啟發材料：給學員「業務缺口 → Agent 位置 → 人的驗收」三欄，而非直接列工具名稱。
- 討論選題時，先問工作在哪裡卡住，再依上表找相似機制；不把外部案例移植為署內現況。
- 可以用兩個反例提醒驗證：資訊不完整導致研究底稿無法查證；初稿變快但退件與審核時間增加。是否納入正式教材待使用者決定。
