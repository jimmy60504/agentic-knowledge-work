# AI 放大器：論點階段的文獻與圖片蒐集測試

## 來源

2026-09-07，使用者詢問是否應在建立論點時先蒐集文獻與圖片，並要求實際測試。Agent 以第二週主 draft 的「AI 是放大器」作為測試主題；以下為候選材料，尚未整合教案或投影片。查閱日：2026-09-07。

1. HBS AI Institute，〈Navigating the Jagged Technological Frontier〉，2023-09-21，[研究機構摘要](https://aiinstitute.hbs.edu/navigating-the-jagged-technological-frontier/)。已讀摘要的 Key Findings 與 Shifting the Debate；[論文入口](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321) 回傳 403，本次未讀全文，不宣稱完成方法審查。
2. Erik Brynjolfsson、Danielle Li、Lindsey Raymond，*Generative AI at Work*，[arXiv v2](https://arxiv.org/abs/2304.11771v2)，2024-11-06 修訂；[HTML 全文](https://arxiv.org/html/2304.11771v2)。已核對摘要及 Figure 3、4 圖說，未完整審查所有模型。固定採 v2 的樣本與數字，不混用其他版本。arXiv 頁的授權連到 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)。
3. Joel Becker 等，METR，〈We are Changing our Developer Productivity Experiment Design〉，2026-02-24，[研究團隊更新](https://metr.org/blog/2026-02-24-uplift-update/)。已讀結果、選樣問題及設計更新說明。
4. Julo，*Lupa.na.encyklopedii.jpg*，2007-08-10，[Commons 圖片頁](https://commons.wikimedia.org/wiki/File:Lupa.na.encyklopedii.jpg)，作者釋出至公有領域。
5. Iainf，*LeverPrincleple.svg*，2006，[Commons 圖片頁](https://commons.wikimedia.org/wiki/File:LeverPrincleple.svg)，本次依頁面提供的 CC BY-SA 3.0 保存。

相關：[[presentation-process-before-and-after]]、[[purposeful-reading-and-agent-assisted-practice]]。圖片與完整署名見 `assets/week2-evidence-pilot/README.md`。

## 重點

### 文獻先幫助判斷要說什麼

| 材料 | 本次查到的內容 | 可以支持的說法 | 限制與取捨 |
|---|---|---|---|
| HBS／BCG 顧問研究 | 758 位顧問；在 AI 能力範圍內的任務，完成速度、評分與完成量改善；能力邊界不均勻 | 應依任務安排人與 AI 的分工 | 2023 年 GPT-4 情境，不能套成所有工作或目前 agent 的固定效益；本次只讀機構摘要 |
| Generative AI at Work，v2 | 5,172 位客服人員，每小時解決問題數平均增加 15%；較少經驗、較低原始技能者改善較多，最高技能與經驗者速度小幅改善、品質略降 | AI 可以協助補足經驗，效益因人而異 | 單一客服導入情境，不能推成所有新手都受益，也不能推成專業知識不重要 |
| METR 2026 更新 | 2025 年初研究曾發現耗時增加 19%；後續樣本出現加速跡象，但參與者與任務選樣、時間記錄等問題使幅度難以可靠解讀 | 研究引用要連日期、工具情境與後續修正一起看 | 作為備講材料；本課並非 coding 課程，不必為這個例子展開技術細節，不能把舊數字當成 2026 現況 |

### 圖片與圖表候選

| 素材 | 角色與候選用法 | 已完成／待處理 |
|---|---|---|
| 放大鏡與書本照片 | 用於「放大器」或查閱材料的概念引入；是比喻，不能佐證 AI 效果 | 已下載原圖並目視檢查。橫式 1971×1074；畫面偏暗、文字密集，適合獨立圖片區，避免再疊長文字 |
| 槓桿原理 SVG | 用於「工具如何擴展能力」的抽象類比，並可討論支點與操作方式 | 已下載原 SVG、核對雜湊與原頁一致。原圖為物理示意，若引入過多公式可能分散主題；保留作備選，不直接認定適合主頁 |
| 客服研究 Figure 3：Heterogeneity of AI Impact, by Skill and Tenure | 真正對應論點的研究圖，呈現原始技能、年資不同時的效果差異 | 已核對圖說與位置，未下載圖像；HTML 缺少相應可直接下載的圖像，下一次製作時從 PDF 檢查。原文授權含 NC／ND，不直接翻譯改圖後發布 |
| 客服研究 Figure 4：Experience Curves by Deployment Cohort | 可用於解釋 AI 與經驗累積的關係 | 已定位圖說，尚未擷取與視覺檢查；保留為候選，避免把相關曲線簡化成保證學習效果 |

目前沒有生成抽象圖片。若採用放大器比喻後仍缺合適畫面，可再生成；先確認要表達的關係，再投入製作。

## 洞見

以下是 agent 的解讀與候選改寫，不是論文的直接結論。

- 使用者提議提早蒐集是合理的：這次客服材料就使「原本越強，AI 放大越多」的直覺需要修正。現有「領域知識 × 駕馭 agent 的能力」可保留為教學比喻，但上述研究未驗證這個乘法公式。
- 候選說法：「AI 能協助補足經驗、擴展產出能力；效果取決於任務、工具與使用方式。自己的專業與查核，幫助我們判斷結果是否適用。」其中後一句是課程的實務判準，不應包裝成這三篇共同驗證的因果結論。
- 圖片也能帶出新的敘事，但有來源不代表能佐證。放大鏡與槓桿屬概念類比，研究資料圖才對應實證；保留圖片時就記下角色。
- METR 案例顯示，先查後寫能避免只挑符合自己立場的舊數字。文獻蒐集包含更新與限制，找到不同結果時先改論點。

## 課程用途（候選）

論點圈可改為：帶著問題蒐集文獻、案例與圖片 → 人通讀，比較支持與限制 → 形成論點與故事線；文章階段補缺口，分頁階段挑圖與安排畫面，最後排版。

每個素材保留五件事即可：支持或挑戰哪個想法、原始來源與位置、候選用途、限制、採用狀態。圖片另附作者與授權。初期收少量候選，避免先累積大量無法解釋用途的圖片。

第二週測試用法：先展示「AI 是放大器」的起始想法，再看客服研究如何促使我們改寫；同時展示放大鏡照片與研究 Figure 3 的角色差別，讓學員看到資料、畫面、論點一起形成。Figure 3 仍需取得與檢查，不列為已完成投影片。

初次蒐集時只完成測試；2026-09-07 後續依使用者要求試整合回第二週主 draft，加入放大鏡照片、客服研究摘要示意、Figure 3 待取得註記與版面草圖，並將蒐集文獻、案例與圖片明列於論點圈。槓桿圖與 METR 更新保留為備選。這份圖文整合仍為可修改的草案，正式 lesson 與 PPTX 未同步。
