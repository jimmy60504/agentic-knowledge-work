# Jev：只回傳決定、不生成文字的模型（TypeSafe AI，2026-09）

整理日期：2026-09-20。使用者在討論第四週「六種介入方式」時提到第四種「固定節點呼叫一次模型」很像近日流行的 Jev，本筆記查核它是什麼、怎麼接、能做與不能做什麼。數字為廠商自述，未獨立驗證。

## 來源

- [TypeSafe AI 官方文件〈System One〉](https://docs.typesafe.ai/concepts/system-one)：System One 模型的定義、`POST /v1/systemone` 端點、`jev-latest` 模型代號、Python 與 JavaScript SDK，文字輸入、32K 上下文。
- [TypeSafe AI 部落格〈Introducing System One Models & Jev〉](https://typesafe.ai/blog/introducing-system-one-models-and-jev)：2026 年 9 月 15 日發表。
- [LangChain 部落格〈What Is Jev?〉](https://www.langchain.com/blog/building-a-harness-with-jev)：輸入是狀態加問題，輸出三類決定；以 LangChain 的 `TypeSafeClassifier` 呼叫；定位為「LLM 做開放式推理與生成，Jev 做快速結構化決定」。
- [MarkTechPost 報導](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/)：三種問題原語、價格、延遲、早期存取需排隊；未公開權重與參數量，基準為廠商自測。
- [INSIDE 報導](https://www.inside.com.tw/article/42431-jev-ultrafast-browser-agent-gregpr07)：Browser Use 結合 Jev 的開源瀏覽器 Agent 案例。

## 重點

### 它是什麼

Jev 是 TypeSafe AI 稱為「System One」的決策模型。輸入是一段狀態（文字或結構化資料）與一組有型別的問題，輸出是帶機率與信心的決定，不生成文字。三種問題：

| 問題原語 | 回答 |
|---|---|
| Choice | 從給定選項中選一個，附各選項機率 |
| Score | 依有序等級評分，附分布 |
| Noul | 這句話是否為真，回傳 0 到 1 的機率 |

呼叫方式是 HTTP API 或 SDK，程式把狀態與問題送去，取回結構化答案後由程式分支。廠商宣稱比同類 LLM 快數十到兩百倍、便宜數百倍，回應時間數十到數百毫秒；早期存取需排隊，也可經 Vercel AI Gateway、OpenRouter 等中介取用。

### 它不做什麼

不聊天、不生成文字、不選工具、不決定下一步。它只回答程式事先定好的問題。因此它是**流程裡的一個固定節點**：程式把每一筆輸入送去問一個或幾個問題，拿到答案照固定路徑走。這正是第四週介入方式表第四種「固定節點呼叫一次模型」的形狀，而且比用一般 LLM 做這件事更純粹，因為它連生成文字的能力都沒有。

### 與 LLM Agent 的關係

LangChain 與多篇評論的定位一致：Jev 不取代 LLM，而是放在 Agent 迴圈裡的判斷點，做路由、分類、分流、守門、驗證。例如 Agent 產出後由 Jev 判斷「這個結果可以交出去嗎」；或流程進來的每一筆先由 Jev 分類，再決定要不要叫 LLM。

## 洞見

- **第四種介入方式有了現成的名字。** 講「固定節點呼叫一次模型，模型參與但不是 Agent」時，Jev 是最乾淨的例子：輸入狀態、輸出決定、不碰工具、不選步驟。地震預警管線裡的 P 波拾取與震度預測模型也是同一形狀，只是那是專用模型，Jev 是通用的決策 API。
- **年度成效統計案例的第四種可以改用 Jev 的形狀。** 原本寫「擷取第一報時間與規模」偏向抽取，比較像 LLM；改成「判斷這件事件是否納入、多報次取哪一報」，是 Choice 與 Noul 的形狀，更貼切。
- **對業務的意義是：不是每個判斷點都需要 Agent。** 規則說得清楚、選項事先知道的判斷，可以放一個決策節點；只有需要查資料、選工具、迭代的段落才需要 Agent。這與課程「模糊交 Agent、明確交程式」一致，決策模型介於兩者之間。
- 廠商數字未獨立驗證，權重未公開；課堂只用它說明形狀，不推薦採購。

## 課程用途（候選）

- 第四週 4-1 第 8 頁六種介入方式的第四格：接 API 的決策模型，畫成「流程節點送狀態與問題，模型回選項與機率，節點照固定路徑走」。
- 第 10 頁「第四種的現成例子」可並列兩個：預警管線內的專用模型（中心自己的）與 Jev（通用的）。
- 工作坊：學員拆出的段若是「規則清楚、選項已知的判斷」，可提示這種形狀，不必上 Agent。
