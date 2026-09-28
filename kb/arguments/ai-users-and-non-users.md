# 為什麼用 AI 的人離不開，還有一堆人沒在用

整理日期：2026-09-28。起因：使用者提出「現在為什麼用 AI 的人離不開，但是還有一堆人沒有用？這些沒有日常使用的到底有什麼分類」。由 sub-agent 搜尋，主責整合；引用前須開原始連結核對。

相關：[[public-sector-ai-adoption-barriers-and-examples]]（四個阻礙、署內使用分層推估）、[[what-makes-civil-servants-want-to-learn-ai]]（拉力）、[[ai-enablement-what-changed]]、[[ai-adoption-failure-cases]]。

## 一、來源

### 使用者分群

| 來源 | 分群 | 可信度 |
|---|---|---|
| Slack Workforce Lab 2024，[Salesforce 整理](https://www.salesforce.com/news/stories/ai-personas-at-work/) | 積極公開使用 30%、私下使用不公開 20%、抗拒 19%、欣賞但未整合進工作 16%、觀望 16% | 中。企業調查，樣本大 |
| BCG AI at Work 2025，[連結](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain) | 推動者、自主探索者、跟隨組織者、被動觀察者、謹慎懷疑者；第一線員工經常使用率停在 51% | 中高。11 國逾 10,600 人 |
| Microsoft WTI 2025，[連結](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born) | 懷疑者、新手、探索者、重度使用者 | 中。廠商報告，未公布各類比例 |
| Microsoft WTI 2026，[報告頁](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)、[PDF](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2026/09/2026_Work_Trend_Index_Annual_Report_090326_6a99e3f096b6e.pdf) 第 12 頁 | 個人 AI 能力 × 組織準備度：Frontier 19%、Blocked agency 10%、Unclaimed capacity 5%、Stalled 16%、Emergent 50%；10 國逾 2 萬人，自陳問卷 | 中高。廠商報告，樣本大，有公布比例；2026-09-29 補 |

### 不用與少用的比例與原因

| 來源 | 重點數字 | 可信度 |
|---|---|---|
| Pew 2025-10，[連結](https://www.pewresearch.org/short-reads/2025/10/06/about-1-in-5-us-workers-now-use-ai-in-their-job-up-since-last-year/) | 21% 美國工作者在工作中使用 AI，65% 幾乎不用；非使用者中 45% 認為自己的工作幾乎沒有部分能用 AI | 高 |
| Gallup 2025 至 2026，[連結](https://www.gallup.com/699797/indicator-artificial-intelligence.aspx) | 每日使用由 8% 增至 12%（2025 年第二至第四季）；2026-05 科技業日用 42%，多數產業僅 9% 至 15% | 高 |
| St. Louis Fed，[連結](https://www.stlouisfed.org/on-the-economy/2025/nov/state-generative-ai-adoption-2025) | 上週 9% 每個工作日都用，14% 至少用過一天 | 高 |
| 英國 HMRC Copilot 試驗，[GOV.UK](https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot) | 拿到授權者 83% 實際使用；非使用者 46% 因資安與隱私疑慮 | 高。公部門最貼近的例子 |
| 資策會 MIC 2025，[連結](https://mic.iii.org.tw/research.aspx?id=726) | 46% 用過生成式 AI，9% 每天使用 | 中。消費者調查，非職場 |

台灣公部門的使用率與不用原因，查無系統性調查。

### 離不開的證據

- METR 2026，[連結](https://metr.org/blog/2026-02-24-uplift-update/)：重做對照實驗時，招募不到願意在部分任務不用 AI 的開發者，即使給付時薪。
- 英國跨部會 Copilot 試驗：82% 不想回到沒有工具的狀態。
- Anthropic Economic Index 2026-03，[連結](https://www.anthropic.com/research/economic-index-march-2026-report)：使用六個月以上者成功率較高，並嘗試價值較高、較多樣的任務。提升幅度 sub-agent 回報為 10%，先前筆記為約 4 個百分點，待核對原文。

### 理論

- **UTAUT**（Venkatesh）：是否採用取決於績效期望、努力期望、社會影響與便利條件；早期以好不好學為主，後期以主管與同儕的支持為主。
- **Rogers 創新擴散**：創新者 2.5%、早期採用者 13.5%、早期大眾 34%、晚期大眾 34%、落後者 16%。多數人未日常使用是常態。
- **能力邊界參差**（Dell'Acqua 等，Organization Science 2026）：能力範圍外的任務，使用 AI 反而正確率下降 19 個百分點；一般使用者無法憑直覺判斷任務落在哪一側。

## 二、重點

沒有日常使用的人可分為七類：

1. **沒有權限**：機關未提供或規定不允許。改變方式：提供合規工具與使用規範。
2. **用錯任務後放棄**：曾用在 AI 不擅長的工作，結果不好，就認定沒用。改變方式：說明哪些任務合適、哪些不合適。
3. **不知道和自己工作的關係**：人數最多，Pew 非使用者 45% 認為工作用不上。改變方式：提供同業務的具體例子。
4. **原則性不信任**：多為資深、能力強的人，擔心可靠性與專業認同。改變方式：請他擔任檢查 AI 產出的角色，借重其判斷。
5. **已在用但不公開**：Slack 調查約 20%。不需要說服，需要讓使用可以公開。
6. **沒時間學**：工作已滿，沒有學習的餘裕。改變方式：在上班時間與既有工作中學。
7. **工作確實不適合**：與第 3 類不同，是正確的判斷，應予尊重。

離不開的人，是已經找到合適任務、也累積了使用經驗的人；成功率隨使用時間提高。

## 三、洞見

- 用與不用的差別，主要不在工具，而在是否找到合適的任務。離不開的人找到了；第 2、3 類沒找到，第 7 類確實沒有。這正是第五週「找出合適的導入方向」要處理的事。
- 「用錯地方而浪費」（多此一舉）與「用錯地方之後放棄」（第 2 類）是同一個原因的兩種結果。
- 第 3 類與第 7 類外表相同，都說「我的工作用不上」，要逐一聊才分得出來；這支持第五週工作坊由講師一對一聊天的做法。
- 第 4 類的資深懷疑者，正是最有判斷力的人；讓他們負責檢查，比說服他們使用更有效，也與「判斷如何累積」的討論相連。
- 第 1、5、6 類要由組織處理，對應第五週第六步「條件」。
- 離不開也有風險：依賴不等於品質提升（METR 2025 使用者自認變快而實測變慢），重度使用者同樣需要以返工與完整度檢查效果。

## 四、課程用途（候選，未定）

- 第五週開場或第一步：請學員定位自己屬於哪一類，再帶出「差別在於有沒有找到合適的任務」。
- 工作坊聊天時辨認學員屬於哪一類：第 2、3 類幫忙找任務，第 4 類邀請擔任檢查者，第 7 類確認後不勉強，第 1、5、6 類記為須由機關處理的條件。
- Slack 與 BCG 的分群可作自我定位的參考，須註明為企業調查。
