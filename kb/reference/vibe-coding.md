# Vibe coding：讓 AI 寫程式，人只引導、測試與回饋

整理日期：2026-09-20。使用者指出第四週介入方式第三種「建置工具後退出」就是 vibe coding，本筆記記下詞的出處與課程用法。

## 來源

- Andrej Karpathy 2025 年 2 月 2 日在 X 的貼文，原句：「There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.」他描述的是自己用 Cursor Composer 加語音輸入、接受所有建議、不讀程式碼的工作方式。整理自 [CodeRabbit 的詞源整理](https://www.coderabbit.ai/blog/a-semantic-history-how-the-term-vibe-coding-went-from-a-tweet-to-prod)與 [Wikipedia 條目](https://en.wikipedia.org/wiki/Vibe_coding)。
- Collins 詞典 2025 年度詞（Wikipedia 條目引述）。
- [The New Stack 報導](https://thenewstack.io/vibe-coding-is-passe/)：Karpathy 後來改稱專業用法為 agentic engineering，vibe coding 留給不讀程式碼的隨興用法。

## 重點

- 定義：用自然語言描述意圖，讓 AI 生成程式碼，人負責引導、測試、給回饋，不逐行寫、常常也不細讀。
- 與課程第三種介入方式的對應：人與 Agent 對話寫出程式，程式接進流程（排程或手動執行），之後 Agent 退出，運行時只有程式。差別只在「人讀不讀那段程式」；課程不要求學員讀懂程式，但要求驗收實際輸出。
- 與第二種「一次性交付」的差別：第二種交出的是檔案或分析結果，用完即止；第三種交出的是會反覆執行的工具。

## 洞見

- 對非工程背景的學員，vibe coding 是最容易理解「Agent 幫我做出一個以後每年自己跑的東西」的說法。課程用它當第三格的通俗名稱，投影片口述可提，畫面不必寫英文。
- Karpathy 自己已把專業用法改名，代表「不讀程式碼」在正式業務上有風險。課程的處理是：程式可以不讀，但輸出一定要驗；規則寫進腳本前，人要先確認規則本身。這與「模糊交 Agent、明確交程式」一致。

## 課程用途（候選）

- 第四週 4-1 第 8 頁六種介入方式第三格的名稱與口述。
- 工作坊：學員拆出的段若是「規則固定、每年或每月重跑」，提示可用這種方式，並提醒驗收輸出而非驗收程式。
