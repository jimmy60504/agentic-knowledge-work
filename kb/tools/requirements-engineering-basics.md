# 需求工程的基本觀念

整理日期：2026-09-28。起因：使用者指出第五週的主題對應軟體工程的需求工程；把 Agent 導入流程通常也是一個軟體開發的過程，第五週討論的是最前面找需求的階段。內容取自 2026-09-27 第五週草稿的講師參考（commit `b2eb425`），原為 agent 整理，出處待逐一查證。

相關：[[ai-pre-adoption-plan-frameworks]]、[[ai-adoption-failure-cases]]、[[ai-users-and-non-users]]、[[domain-storytelling]]。

## 來源（待查證）

- Zave, P. & Jackson, M. (1997). Four dark corners of requirements engineering. ACM TOSEM.
- Robertson, S. & Robertson, J. *Mastering the Requirements Process*（Volere 範本與 fit criterion）。
- Wiegers, K. & Beatty, J. *Software Requirements*（業務、使用者、功能需求三層）。
- Gause, D. & Weinberg, G. *Are Your Lights On?*（找出真正的問題）。

## 重點：五個觀念

1. **需求需要挖掘。** 熟練的工作已成習慣，提出者常直接說解法，而且只看得到自己那一段。
2. **區分問題與解法。** Zave 與 Jackson 將需求（R，世界應成立的狀況）、領域知識（D，世界本來的運作方式）與規格（S，系統的行為）分開；許多失敗來自 D 的假設錯誤。
3. **需求是協商後的共識。** 利害關係人的需求會衝突，需求文件記錄的是決定。
4. **需求必須可驗證。** 每條需求附判斷標準（Volere 的 fit criterion）。
5. **需求會改變。** 需要能追溯來源與影響範圍。

## 洞見

- Agent 降低了撰寫規格與程式（S）的成本，但需求（R）與領域知識（D）仍須由懂業務的人說清楚；這是「判斷不能外包」在軟體工程裡的說法。
- 第五週的內容與五個觀念一一對應：
  - 需求需要挖掘 → 講師一對一聊天、以實際發生的事件為起點。
  - 區分問題與解法 → 流於形式（先有工具再找問題）；規劃第 3 題「有沒有比 AI 更合適的做法」。
  - 需求是協商後的共識 → 上下層利益衝突；每個人的起點不同。
  - 需求必須可驗證 → 規劃第 6 題成功條件；以返工與完整度衡量。
  - 需求會改變 → 認真做好時，以前沒考慮的東西會顯現。
- 需求探索之後是規格：需要正式專案的方向（例如舊地震資料庫整理），可接 Domain Storytelling 從圖到規格的路徑。

## 課程用途（候選）

- 第五週定位為需求工程中的需求探索階段；後續若排規格、設計、實作與驗證，可依此延伸。
- 與第一門課「Agentic 開發與維運」同源，提及時一句帶過。

## 與第四週 Story 圖的關係（2026-09-28 使用者）

第五週是第四週為什麼要畫 Story 圖的緣由：導入 Agent 通常是軟體開發過程，不先做需求工程釐清問題，最後做出來的方向很可能是錯的。Domain Storytelling 本身即是需求工程與領域驅動設計中釐清現況的方法，見 [[domain-storytelling]]。
