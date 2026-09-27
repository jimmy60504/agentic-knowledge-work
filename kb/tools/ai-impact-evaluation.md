# 組織如何評估 AI 導入成效

整理日期：2026-09-28。起因：第五週第三段主張「初期變慢，效果看返工與完整度，不看速度」，使用者問組織那段是否要討論怎麼評估成效較恰當，現在有沒有方向，還是大家仍在摸索。由 sub-agent 搜尋，主責整合；標「待核對」者引用前須開原文確認。

相關：[[ai-enablement-what-changed]]、[[ai-adoption-failure-cases]]、[[retention-and-intrinsic-motivation]]、[[ai-pre-adoption-plan-frameworks]]。

## 一、來源

### 軟體工程

| 來源 | 重點 | 可信度 |
|---|---|---|
| DORA〈State of AI-assisted Software Development 2025〉，[連結](https://dora.dev/dora-report-2025/) | AI 是放大器：組織體質好則放大交付，體質差則放大混亂；AI 採用與產出量正相關、與穩定性負相關；返工率（非計畫性修復部署占比）列為核心指標；提出七項組織能力的 AI 能力模型 | 高。返工率納入的年份（2024 或 2025）待核對 |
| SPACE 框架的檢討（Forsgren 等） | 活動量維度在 AI 時代最先失效：產出量膨脹後變成雜訊 | 中高 |
| DX AI Measurement Framework，[連結](https://getdx.com/blog/ai-measurement-framework-guide/) | 使用度、影響、成本三軸合併看，只看使用度會誤導 | 中。量測平台廠商；其支出成長數字不引用 |
| GitHub 與 Accenture 研究，[連結](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/) | 工具廠商也建議不要只看採用率與建議接受率 | 中 |
| METR 2026，[自陳調查](https://metr.org/blog/2026-05-11-ai-usage-survey/)、[實驗設計更新](https://metr.org/blog/2026-02-24-uplift-update/) | 自陳效益系統性高估；不願在無 AI 條件下工作者退出實驗，量測方法本身出現偏誤 | 高 |

### 一般知識工作

| 來源 | 重點 | 可信度 |
|---|---|---|
| Workday〈Beyond Productivity〉2026-01，[連結](https://www.workday.com/en-us/artificial-intelligence/research/beyond-productivity-ai-value.html) | 3,200 人；多數員工表示省時，但省下的時間約四成又用於審查、修正與重做 AI 產出；僅少數能穩定得到明確正面結果 | 中。廠商委託，比例待核對 |
| Microsoft WTI 2026，[連結](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization) | 組織因素決定約 67% 的效益差異 | 中高 |
| Gartner〈AI value metrics〉，[連結](https://www.gartner.com/en/articles/ai-value-metrics) | 多數組織缺乏衡量 AI 商業成果的框架 | 中。比例待核對 |

### 公部門

| 來源 | 重點 | 可信度 |
|---|---|---|
| 英國 NAO 2024-03，[PDF](https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf) | 政府 AI 的成效指標尚待建立 | 高 |
| 英國跨部會 Copilot 試驗與 DWP、HMRC 評估，[GOV.UK](https://www.gov.uk/government/news/landmark-government-trial-shows-ai-could-save-civil-servants-nearly-2-weeks-a-year) | 混合問卷、計量分析與訪談；公開承認在複雜、敏感的政策判斷工作上表現不佳 | 高。評估的是 2024 年工具 |
| 澳洲 DTA AI 保證框架，[連結](https://www.dta.gov.au/articles/dta-pilots-new-ai-assurance-framework) | 以生命週期各階段的提問、系統與個案負責人、中央登記取代單一績效數字 | 中高 |
| OECD〈Generative AI experimentation in government〉2026-07、《Digital Government Outlook 2026》，[連結](https://www.oecd.org/en/publications/digital-government-outlook_0496b2bc-en/) | 影響評估是政府 AI 治理中發展最落後的一環；曾做過影響評估的會員國約三成 | 高。國家數待核對 |
| 數發部 TryAI，[中央社](https://www.cna.com.tw/news/afe/202511180268.aspx) | 公開成效多為個案時數縮短，尚未見系統性的品質或返工評估 | 中 |

### 指標被操弄

- 程式行數本就是失真的指標，AI 使生成成本趨近於零，失真更嚴重（[The Pragmatic CTO](https://www.thepragmaticcto.com/p/lines-of-code-are-back-and-its-worse)，評論文章）。
- 以使用率為考核指標，會出現為用而用；見 [[ai-adoption-failure-cases]] 的強制使用案例。

## 二、重點

- **沒有共識的評估標準**，各機構各提框架；但「不該怎麼測」已有相當共識：不能只看速度、使用率或產出量。
- **收斂中的面向**：
  1. 品質、返工與穩定性（DORA 返工率、Workday 重做時間）。
  2. 成果而非活動量（DX 影響軸、SPACE 檢討）。
  3. 組織條件（DORA 能力模型、WTI 67%）。
  4. 成本。
  5. 質化回饋（英國試驗的訪談）。
- **公部門普遍尚未評估**：NAO、OECD 都指出影響評估最落後。

## 三、洞見

- 課程「看返工與完整度」的主張，與 2025 至 2026 年主要機構的方向一致，不是少數觀點。
- 「怎麼測」還沒有標準答案；主管可以把這一點誠實告訴同仁，並從低成本的做法開始。
- 評估的對象應先是組織條件，再是個人：同樣的工具，組織體質決定放大的是優點還是缺點。
- 可與「測量是給做事的人自己看的回饋」並存：返工紀錄先作為當事人的回饋；組織層看的是趨勢與條件，不拿來考核個人。

## 四、課程用途（候選）

第五週第四段組織層可加入「評估成效」：

1. 先蒐集返工與修正紀錄：哪些產出被退回、為什麼；作為當事人的回饋。
2. 以個案訪談加少量問卷的混合方式，不只看滿意度或使用率。
3. 先評估組織條件：規定是否清楚、資料品質、審核流程跟不跟得上。
4. 使用率可作為管理參考，不列入考核。
5. 測不出來就承認，比照英國試驗報告直接寫出不適用的工作。
