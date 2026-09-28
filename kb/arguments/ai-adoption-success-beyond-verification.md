# 驗證條件以外的成功導入因素

整理日期：2026-09-29。起因：第五週第一段把成功條件歸納為三項（成效有明確的驗收標準、產出在交付前經過外部檢查、判斷與責任仍由熟悉業務的人承擔），使用者想知道是否有成功的關鍵落在這三項之外的案例。由 sub-agent 搜尋，主責抽查兩筆來源；引用前仍須逐筆開原始連結核對。相關：[[ai-adoption-failure-cases]]、[[public-sector-ai-adoption-barriers-and-examples]]、[[what-makes-civil-servants-want-to-learn-ai]]。

## 一、來源

| 案例 | 經過與結果 | 成功關鍵 | 可信度 |
|---|---|---|---|
| 賓州政府 ChatGPT Enterprise 試辦（2024 至 2025-03） | 14 個機關、175 人分五個梯次導入，搭配現場教學與每週焦點團體、599 人問卷；使用者平均每週省約 8 小時，85% 以上回報正面，導入前 48% 未用過。[新聞稿](https://www.pa.gov/agencies/oa/newsroom/icymi--shapiro-administration-s-generative-ai-pilot-for-state-wo)、[報告](https://www.pa.gov/content/dam/copapwp-pagov/en/oa/documents/programs/information-technology/documents/openai-pilot-report-2025.pdf) | 分梯次導入，投資在教人並持續收集回饋 | 高。官方報告；數字為自陳 |
| 賓州政府與 SEIU Local 668 側信協議（2025-03） | 與代表近萬名公務員的工會簽署協議，成立生成式 AI 勞資協作小組；據整理包含 AI 不用於懲戒、導入新工具須提供訓練等條款。[Partnership on AI 案例研究](https://partnershiponai.org/wp-content/uploads/2026/04/PAI_shared-prosperity-case-study_CoPA-SEIU.pdf) | 受影響的人參與訂規則，利益與保障先說定 | 高。條款細節主責尚未核對原文 |
| Bank of Ireland 與金融業工會 AI 協議（2025-03） | 零售銀行業首份 AI 協議：人在決策核心、優先再訓練而非裁員。[FSU](https://www.fsunion.org/latest/news/fsu-and-bank-of-ireland-launch-ai-agreement/)、[協議原文](https://www.fsunion.org/assets/files/pdf/boi_fsu_ai_agreement.pdf) | 同上，企業對照 | 高 |
| NHS 倫敦九個場域 AI 語音病歷試驗（2024-06 至 2025-02） | 醫院、基層診所、心理健康服務、救護車同步試驗，逾 17,000 次看診；與病人直接互動時間增加 23.5%，急診每班看診人數增加 13.4%。[GOSH，2025-09-04](https://www.gosh.nhs.uk/news/researchgosh-led-trial-of-ai-scribe-technology-shows-transformative-benefits-for-patients-and-clinicians-across-london/) | 跨差異大的場域用同一套指標比較，累積證據後才談擴大 | 高。主責已核對數字；全國推估金額各來源不一，不引用 |
| 氣象署 AI 颱風預報（2024 起） | AI 模式先作輔助，與物理模式並行，經凱米、楊柳等颱風實戰比對後，發展為 AI 與 TWRF 融合的預報架構；3 至 5 天路徑誤差下降 12%。[iThome 176214](https://www.ithome.com.tw/news/176214)、[iThome 178595](https://www.ithome.com.tw/news/178595) | 以多次真實事件累積信任，逐步由參考升格為正式依據 | 高。公開報導，非署內資料 |
| Revenue NSW 弱勢客戶辨識（2019 上線，2021 倫理審查） | 辨識約 4.6 萬名財務弱勢者，改轉介替代方案而非強制執行；主動公開案例研究，並經政府 AI 倫理委員會獨立審查。[NSW 案例](https://www.digital.nsw.gov.au/article/case-studies-ai-nsw-government)、[ISJ 論文](https://onlinelibrary.wiley.com/doi/10.1111/isj.70025) | 對外透明並由組織外部審查，建立系統本身的可信度 | 中高。較早期的機器學習，結論與模型能力無關 |

### 不收錄

- 巴西聯邦區內控單位的結構化教學法（arXiv 2606.01517）：單一作者預印本，量化數字未見於摘要。
- Veterans Evaluation Services 文件處理（Maximus 案例研究）：承包商自述，未見第三方查證。
- 新加坡 VICA、愛沙尼亞 Bürokratt、日本數位廳 GENAI：缺一手成效數字或看不出新的成功因素。

## 二、重點

三項驗證條件都落在單一工作或流程的層次；這些案例的成功關鍵則在組織層次，可歸為三類：

- **受影響的人參與訂規則**：工會協議先說定 AI 不用於懲戒、優先再訓練、省下的利益如何處理。對應第二段的上下層目標不一致。
- **信任逐步累積，分階段擴大**：NHS 先跨場域試驗再談擴大；氣象署 AI 颱風模式經多次實戰才升格；賓州分梯次導入。對應一步到位的期待。
- **投資在教人**：賓州以現場教學與持續回饋支撐導入。對應第五段的建立使用環境。

Revenue NSW 的透明與外部審查，屬於利害關係人溝通，可作為司法院判決書草稿暫緩的對照。

## 三、洞見

- 三項驗證條件回答「這件工作能不能交給 AI」；組織層次的因素回答「導入能不能持續、擴大」。兩者層次不同，不必合併成同一張清單。
- 失敗案例中的上下層目標不一致與一步到位的期待，在成功案例中都有對應的做法：先與受影響的人說定規則，並以分階段累積的證據決定是否擴大。
- 氣象署自己的颱風 AI 是逐步升格的現成例子，比外國案例更貼近學員。要與外部檢查區分：這裡談的是信任與地位累積的節奏，不是單次產出的查核。

## 四、課程用途（候選）

- 第五週第五段主管的作為：工會協議與分階段擴大，作為建立誘因與評估成效的佐證。
- 第五週第三段初期變慢，或第一段開頭：氣象署 AI 颱風模式作為逐步升格的例子，回應一步到位的期待。
- 第一段三個條件維持工作層次，不因這些案例增加條件。
