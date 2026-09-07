# 第二週逐段圖文素材：來源、授權與處理

取得日期：2026-09-07。用途：第二週 draft 的選材與備課，尚未同步正式教材或 PPTX。SVG 為課程自繪；其他檔案保留外部來源。每項圖片旁的來源在正式排版時也要保留。

| 檔案 | 作者／來源與位置 | 授權或分享依據 | 本次處理 |
|---|---|---|---|
| `ai-at-work-figure3-page46.png` | Brynjolfsson、Li、Raymond，[Generative AI at Work v2 PDF](https://arxiv.org/pdf/2304.11771v2)，PDF 第 46 頁，印刷頁碼 45，Figure 3 | [arXiv v2 授權](https://arxiv.org/abs/2304.11771v2)連至 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) | 整頁轉圖，保留座標、圖說與頁碼；未裁切、翻譯或修改；非商業使用條件仍適用 |
| `sun-human-judgment-page61.png` | 孫以瀚，2026-05-11，[教育部臺灣學術倫理教育資源中心提供的講座 PDF](https://ethics.moe.edu.tw/files/resource/lecture/20260511/20260511_lecture_20260508.pdf)，第 61 頁 | 原稿第 1 頁寫明「PPT 可提供（細節慢慢看），歡迎分享出去」；未指定 CC 授權，不擴張成任意改作授權 | 整頁轉圖、未修改；目前 draft 改採可讀引文／整理自摘要，原檔保留作查核；屬講者個人意見 |
| `moda-problem-definition-page25.png` | 數位發展部，[公部門人工智慧應用參考手冊](https://www-api.moda.gov.tw/File/Get/moda/zh-tw/WwHCroVhwWy52dw)，V1.0，修訂頁日期 115.01.28，第 25 頁 | [數發部政府網站資料開放宣告 CC0](https://moda.gov.tw/announcement/publicdeclare/951) | 僅擷取下半部「提出問題」與對照文字，未改字；目前 draft 改採可讀整理，原檔保留作查核；排除上方 Freepik 插畫。座標見下方指令 |
| `design-council-double-diamond.png` | [Design Council，The Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) | 原頁明示 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 原始 PNG、未修改；保留英文標籤；為備講材料 |
| `zotero-pdf-reader.jpg` | [Zotero 官方 PDF Reader and Note Editor 文件](https://www.zotero.org/support/pdf_reader)，文件使用的 6.0 時期示範圖 | [Zotero 文件授權](https://www.zotero.org/support/licensing)：2015-04-26 之後文件內容 CC BY-SA 4.0 | 原圖未修改；保留整個工具示範，內嵌研究內容不另行取用；非本機操作截圖 |
| `three-artifacts.svg` | 本課原創示意，範例借用客服研究的題材；三種產出物為本課安排 | 原創課程圖，未另授予 CC 授權 | 使用 `build_diagrams.py` 生成；目前 draft 改採可編輯 Markdown 對照，圖檔保留作查核歷史；非引用作者原圖或真實軟體畫面 |
| `paragraph-before-after.svg` | 本課原創改寫例子；右側事實來源為 [客服研究 v2 摘要](https://arxiv.org/abs/2304.11771v2) | 原創課程圖，未另授予 CC 授權 | 使用 `build_diagrams.py` 生成；目前 draft 改採可編輯 Markdown 對照，圖檔保留作查核歷史；左側為自擬過度概括，右側為資料摘要，沒有改作原論文圖 |

外部 PNG／JPG 的直接下載位置：

- Design Council：https://www.designcouncil.org.uk/fileadmin/uploads/dc/Photos/banners/Double_Diamond.png
- Zotero：https://www.zotero.org/static/images/blog/6.0/pdf-reader.jpg

PDF 來源檔只放本地 `.quarto/week2-enrichment/` 檢查快取，不提交 PDF。可從上方原始連結重新下載。

## 重現擷取

使用 Poppler，尺寸參數以本次下載 PDF 為準：

```sh
pdftoppm -f 46 -l 46 -scale-to 1800 -singlefile -png ai-at-work-v2.pdf ai-at-work-figure3-page46
pdftoppm -f 61 -l 61 -scale-to 1800 -singlefile -png sun-ai-research.pdf sun-human-judgment-page61
pdftoppm -f 25 -l 25 -scale-to 1800 -x 120 -y 1060 -W 1070 -H 620 -singlefile -png moda.pdf moda-problem-definition-page25
python3 build_diagrams.py
```

本次已目視確認外部圖的文字與邊界；客服圖的縱軸不是百分比，圖中的 agent 是客服人員。原始研究頁字較密，保留作 draft 閱讀與選材；正式投影時仍需試讀，必要時使用已標明性質的摘要示意。

## 不納入這批圖片的材料

- Reynolds 的故事板照片、臺大教學札記圖 3：原站可閱讀，未確認公開再利用授權；出處與候選用途保留在選材筆記，主 draft 依需要連回來源。
- Assertion-Evidence 教學版面：已找到原作者教材入口，尚未逐頁審查，不宣稱完成圖片蒐集。
- 粗略故事板、實際 PPTX 前後版：留待課堂示範取得，不製造假操作截圖。
- 本次沒有 AI 生成的抽象照片；若後續確有概念圖需求，再依內容製作。

## 草案檢查

原有八個圖片檔均保留，且外部圖與兩張 SVG 已完成可解析及目視檢查；文字引用調整後，draft 曾採用 4 張圖片（放大鏡、研究 Figure 3、Design Council 備講圖、Zotero）與 5 個 Mermaid 區塊。孫以瀚、數發部兩張頁面截圖及兩張 SVG 改由可讀引文、整理自摘要或 Markdown 對照承擔內容。本次不新增研究論文首頁圖片；日後若首次介紹來源，可選用真實首頁／封面辨識作者、機構、期刊／版本，客服來源仍記為 arXiv v2。正式排版時仍需確認 Mermaid 換行與尺寸。

2026-09-07 整體精簡後：主 draft 保留放大鏡、Figure 3、Zotero 三張圖片與三個 Mermaid。Double Diamond 圖移至 `kb/week2-paragraph-evidence-and-visuals.md` 備講；原圖及授權不變。研究摘要與試講改用正文，其他已移出的文字圖片仍留查核。

2026-09-07 後續取捨：客服 Figure 3 因案例不好講而移出主 draft，原檔保留查核。主 draft 現有放大鏡、Zotero 兩張圖片及三個 Mermaid；此前採用狀態為歷史紀錄。
