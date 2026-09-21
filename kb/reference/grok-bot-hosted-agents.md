# Grok Bot：託管在雲端的常駐 Agent（xAI，2026-08）

整理日期：2026-09-21。使用者問 Grok Bot 是不是另一種「龍蝦」（OpenClaw）。本筆記查核它是什麼、與 OpenClaw 的差別、在課程六種介入方式裡的位置。功能與價格為廠商自述與第三方評測，未獨立驗證。

## 來源

- [xAI〈Introducing Grok Bot〉](https://x.ai/news/introducing-grok-bot)：2026 年 8 月 11 日發布。Bot 在雲端有自己的電腦，「jobs do not stall when you step away」；能登入並跨 App、工具與網站工作，包括沒有乾淨 API 或 MCP 的平台；只在需要核准時回來找人；記住對話、學習使用者偏好，示範一次流程之後下次自己跑。透過訊息介面互動，桌面與手機皆可。SuperGrok、Cursor Pro 與 Teams 訂閱者可用，用量另計，企業版排隊，仍在 beta。
- [Composio〈A Guide to Grok Bot〉](https://composio.dev/content/guide-to-frok-bot)、[mem0〈Grok Bot Guide〉](https://mem0.ai/blog/grok-bot-guide)：第三方整理的功能、價格與設定。
- [Grok Bot Wiki〈Grok Bot vs OpenClaw〉](https://www.grokbotwiki.com/guides/grok-bot-vs-openclaw)、[Whisker Beacon 比較](https://whiskerbeacon.com/compare/grok-bot-vs-openclaw/)、[Lenny's Newsletter 使用心得](https://www.lennysnewsletter.com/p/grok-bot-vs-openclaw-how-i-replaced)：兩者比較的共同結論見下。
- [[openclaw-how-people-use-it]]：OpenClaw 的架構與用法。

## 重點

### 它是什麼

Grok Bot 是 xAI 推出的一組常駐 Agent，每個 Bot 在雲端有自己的電腦，人用聊天介面交辦，它登入使用者既有的工具（CRM、信箱、產品後台、網站）做多步驟的工作，做完或需要核准時回來找人。定位是「AI 同事」：不用設定自動化，示範一次它就會照做。

### 與 OpenClaw 的異同

| | Grok Bot | OpenClaw（龍蝦） |
|---|---|---|
| 形態 | 託管服務，Bot 跑在 xAI 的雲端電腦 | 自架的 Gateway，跑在自己控制的電腦 |
| 模型 | xAI 的 Grok | 可接多家模型，含 Grok |
| 工具 | 登入 App、瀏覽器操作、沒有 API 的平台也能用畫面操作 | 工具、Skill、插件由自己接；可讀本機檔案 |
| 持續運作 | 電腦關了照跑 | 要自己的機器開著或另外部署 |
| 控制 | 少：憑證、模型、資料都在對方那邊 | 多：憑證、模型、資料自己管，也要自己維護 |
| 入門 | 易，訂閱即用 | 需要設定與維護 |

兩者是同一個形狀的兩種做法：都是「聊天入口、常駐、自己跑迴圈用工具、做完回報」。差別在誰管那台電腦與那些憑證。第三方比較的共同結論是：想省事用 Grok Bot，想控制模型、外掛、本機檔案與憑證用 OpenClaw。

### 在課程六種介入方式裡的位置

與 OpenClaw 一樣落在第五種「流程節點呼叫 Agent」與第六種「協調跨節點工作」：事件或訊息觸發，Agent 自己選工具、跑迴圈、在核准點停下。Grok Bot 多了一層「託管」：不用自己接工具與部署，代價是資料與帳號要交給第三方。這對公務機關是明確的條件問題，不是功能問題。

## 洞見

- **「龍蝦」其實是一類產品，不是一個產品。** 常駐、有自己的執行環境、聊天交辦、跨 App 操作、核准點回報，這個形狀現在至少有自架（OpenClaw）與託管（Grok Bot）兩種。課程講第五、六種介入方式時可以說「這一類產品」，不點名。
- **託管 Agent 把「工具與權限」的問題換成「資料與帳號給誰」的問題。** 4-1 講「接了哪些工具、授了哪些權決定能做到哪一步」，託管版本是把工具與權限一併交出去；工作坊評估表「條件」列的資料與權限兩題，在這裡是決定性的。
- **示範一次就會照做，是第三種與第五種的混合。** 人示範流程，Bot 記住之後自己跑，等於「建置工具後退出」的工具換成了 Bot 的記憶，運行時仍有模型參與。分類要看它跑的時候有沒有模型在選步驟。

## 課程用途（候選）

- 4-1 第 7 頁工具型態的口述：第五種「常駐 Agent」有自架與託管兩種，不點名。
- 工作坊：學員若提到這類產品，引導回評估表的條件列，資料與帳號能不能交出去。
- 不推薦採購；價格與功能以廠商頁面為準。
