# Agent 的角色：網路上有人在用的有哪些

整理日期：2026-09-21。使用者指出「扮演幾種角色」與六種介入方式是兩條軸：介入方式是 Agent 站在流程的哪裡，角色是它在那個位置上做哪一種事，任何一種介入方式裡都可以套角色。本筆記查核網路上實際有人在用的角色有哪些、從哪裡來、收斂成幾種，供 4-1 角色頁使用。

## 來源

角色的說法來自三個地方，各自的用語不同，底層的分工大致一樣。

### 一、對話提示裡的人設

- [Mike Kentz〈The Butler-Thinking-Sparring Framework〉](https://mikekentz.substack.com/p/the-butler-thinking-sparring-framework)：把對話裡的 AI 分成三種模式。管家（Butler）：人知道要什麼、能判斷好壞，AI 照做，人驗收。思考夥伴（Thinking Partner）：人有專業但方向未定，AI 給多個選項附利弊，人選。陪練（Sparring Partner）：人對題目還生、或想測自己的立場，AI 當懷疑的對手來挑戰。選哪一種問兩題：我知不知道要什麼、我能不能評斷產出。
- [Prompt Architects〈Persona Prompting〉](https://prompt-architects.com/blog/45-persona-prompting-make-chatgpt-think-like-an-expert)、[Mindful Chase〈The Art of Role Prompting〉](https://mindfulchase.com/deep-dives/chatgpt-prompt-mastery/the-art-of-role-prompting-assigning-personas-to-chatgpt.html)：常見的「請你扮演」人設有家教、編輯、客服、面試官、唱反調的人、模擬的使用者或客戶。沒有找到 2026 年按使用頻率排序的調查，以上是教學文章反覆出現的例子。
- [Jabra〈AI as a Thought Partner〉](https://www.jabra.com/blog/the-future-of-ai-in-the-workplace/)、[openPR〈AI as a sparring partner〉](https://www.openpr.com/news/4412815/artificial-intelligence-as-a-sparring-partner-how-ai-can-change)、[prmptengineer〈The AI Rubber Duck〉](https://www.prmptengineer.ai/post/the-ai-rubber-duck-and-the-evolution-of-knowledge-work)：知識工作裡的三個常用比喻，思考夥伴、陪練、橡皮鴨（對它講一遍，自己就想通）。共同點是 AI 不做決定，用來測想法、找反例、換角度。

### 二、多 Agent 系統的分工

- [〈The Hitchhiker's Guide to Agentic AI〉（arXiv 2606.24937）](https://arxiv.org/pdf/2606.24937)、[〈LLM-Based Multi-Agent Systems for Software Engineering〉（arXiv 2404.04834）](https://arxiv.org/pdf/2404.04834)：常見角色為研究者（查資料）、規劃者（拆任務）、程式員（寫程式）、審查者（評品質）、測試者（跑測試）、寫手（寫文字）、批評者（對抗式評估）、協調者（分派與收攏）。軟體工程裡收成五個：協調者、程式員、審查者、測試者、資訊檢索者。
- [Towards Data Science〈Single Agent vs Multi-Agent〉](https://towardsdatascience.com/single-agent-vs-multi-agent-when-to-build-a-multi-agent-system/)、[Daily Dose of DS〈Multi-agent Pattern〉](https://www.dailydoseofds.com/ai-agents-crash-course-part-12-with-implementation/)：最常見的組合是「規劃、執行、批評」三角，寫程式的工具幾乎都是這個形狀；再多一個「修正者」處理審查意見。

### 三、子 Agent 目錄

- [Claude Code 文件〈Create custom subagents〉](https://code.claude.com/docs/en/sub-agents)：內建三個，探索者（只讀、搜尋）、規劃者（先查再提計畫）、通用。範例有程式審查者、安全研究者（只讀）、資料庫讀取者（只能查詢）、瀏覽器測試者、儲存庫稽核者。文件的原則：範圍窄、工具只給需要的、審查類角色只讀不寫、說明要短。
- [VoltAgent〈awesome-claude-code-subagents〉](https://github.com/VoltAgent/awesome-claude-code-subagents)：161 個以上，分十類。大多數是職業名稱（前端工程師、Python 專家、雲端架構師、法務顧問、產品經理），真正不同的動作只有幾種：審查、測試、除錯、稽核、寫文件、檢索、規劃、協調、整理記憶。

## 重點

### 收斂：職業名稱之下只有幾種動作

三個來源的角色名稱加起來上百個，去掉職業與領域，按「對工作做什麼」收斂，大約十種：

| 群 | 角色 | 做什麼 | 留下什麼 | 需要的權限 |
|---|---|---|---|---|
| 想事情 | 討論者 | 給方向、列選項附利弊 | 建議 | 只讀 |
| 想事情 | 對手 | 找反例、挑毛病、質疑立場 | 意見 | 只讀 |
| 想事情 | 模擬對象 | 扮民眾、記者、學員、使用者提問 | 問題清單 | 只讀 |
| 做事情 | 整理者 | 查找、擷取、比對、排成可比較的樣子 | 表、清單、底稿 | 讀資料 |
| 做事情 | 起草者 | 寫可修改的草稿、程式 | 檔案 | 寫檔 |
| 做事情 | 操作員 | 跑程式、操作軟體、檢查輸出 | 執行結果 | 執行 |
| 管事情 | 規劃者 | 把一件事拆成步驟與順序 | 計畫 | 只讀 |
| 管事情 | 記錄者 | 留下決定、理由、未解的問題 | 紀錄 | 寫筆記 |
| 管事情 | 審查者 | 對照標準逐項檢查產出 | 檢查表 | 只讀 |
| 管事情 | 協調者 | 分派給其他角色、在核准點停下、追到結案 | 進度 | 分派、通知 |

使用者 09-18 原本列的六個（討論者、整理者、記錄者、審查者、起草者、操作員）都在裡面；多出來的是對手、模擬對象、規劃者、協調者。

### 角色與介入方式的關係

- 兩條軸互不決定。對話裡可以當討論者也可以當審查者；交辦一份統計表時它先當起草者再當審查者；流程指派 Agent 那一種在運行時多半是操作員加詢問核准；Agent 管理流程就是協調者。
- 同一件工作裡角色會輪流換。多 Agent 系統把角色拆成不同的 Agent，是為了各自的上下文乾淨、權限各自限制；一個人用一個 Agent 時，換角色就是換一段對話或換一個指示，效果類似但沒有隔離。
- 角色決定權限。審查類角色只讀不寫，是 Claude Code 文件與多 Agent 文獻共同的做法；反過來說，給它寫檔或執行的權限，就是讓它從想事情走到做事情。這一條接回 4-1 總結講的信任與權限。

## 洞見

- **網路上上百個角色，其實是職業名稱加上十種動作。** 學員不用記職業名稱，記動作就夠：想事情三種、做事情三種、管事情四種。自己的專業名稱套在前面就是那個「專家」。
- **管家、思考夥伴、陪練三分法最適合非工程學員。** 它用兩個問題（知不知道要什麼、能不能評斷）決定該用哪一種，比講角色名稱更容易上手；可以當角色頁的開場。
- **審查者只讀不寫，是最便宜的信任建立方式。** 反向審查（人做、Agent 檢查）不需要任何寫入權，公務機關最容易起步的角色就是它。
- **拆成多個 Agent 的理由是隔離，不是品質。** 一個人在對話裡換角色也能做到大部分效果；真正需要多個 Agent 的時候是要各自限制權限或各自保有乾淨的上下文，這是第六種介入方式才會碰到的問題。

## 課程用途（候選）

- 4-1 第 14 到 17 頁：角色是另一個維度、想事情、做事情、管事情各一頁。
- 4-2 C 由誰做：呼應 4-1，加「一段工作裡角色的先後」。
- 工作坊：工作單「Agent 具體操作」欄填完後，可以再問這一段 Agent 當的是哪個角色、需要什麼權限。
