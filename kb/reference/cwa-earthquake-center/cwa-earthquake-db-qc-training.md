# Sb-A-3  地震資料庫品管與維護實務訓練(流程講解+隨堂演練)

> 由 pptx 自動抽取全部文字（含表格、群組內文字、講者備註）。圖片內的文字未包含。
> 已去識別化：人名、內部主機、網路磁碟與目錄結構、內部網址、系統設定與權限申請方式皆已移除或改以〈〉代稱；批次檔改寫為步驟摘要。命令列提示字元中的磁碟與路徑一律省略為 `>`。保留程式名稱、指令參數與檢查規則。


---

## 第 1 頁：地震資料庫品管與維護實務訓練(流程講解+隨堂演練)

- 交通部中央氣象署學習地圖專業核心能力項目教材
- 新進實務培訓課程教材

- 作者：〈教材作者〉
- 單位：地震測報中心
- 日期：113/7/27


---

## 第 2 頁：課程綱要

（公文格式的課程綱要表，已省略。）

---

## 第 3 頁：課程大綱

- 程式安裝與權限申請
- 認領QC
- QC步驟及程式說明

- 3


---

## 第 4 頁：程式安裝與權限申請

- 步驟【1】-1

- 確認網路連線磁碟機：〈工作磁碟〉（每日事件與程式）、〈資料庫磁碟〉（月份資料庫）、〈備份磁碟〉
- 向系統管理單位申請共用磁碟的讀寫權限
- 在個人電腦建立暫存目錄（CheckPF）與本機程式目錄（必要）
- 將〈工作磁碟〉上的資料庫整理程式全部複製至本機程式目錄，並將該目錄加入 PATH

- 4

**講者備註：**

> CWBSN: 1991~2023/9/14 
> CWASN:2023/9/15氣象局升格為氣象署後改稱


---

## 第 5 頁：認領QC

- 步驟【1】-2

- 到RTD網頁認領QC並列印所認領日的PFILES列表
- 執行EventPick_NB.exe或EventPick.exe
- 到認領日的目錄
- 先用VIEW TRACE將 --No Event – 的A FILE再看過,確認無地震即可將此A FILE刪除。

- 5

**講者備註：**

> 〈內部 RTD 網址〉
> CWB24區\認領地震\


---

## 第 6 頁：QC步驟及程式說明

- 步驟【2】-1

- 開啟命令提示字元
- > CD 〈當日目錄〉 	(到所認領日的資料夾)
- > RE_LIST
- (自動將所在FOLDER下的P FILES自動抽取至LIST.D中.  / 若進DATABASE欲針對某一日的PFILE做LIS, 則請用
- ”DIR/B  1919*>TOTAL.LIS “, 再用RE_LIST1, 輸入TOTAL.LIS以產生LIST FILE)
- > CheckPfile  –LLIST.D	⇒  ERRFILE.BAT
- (CheckPfile.exe 會針對P FILE做檢查, 但儘量不動P FILE內容, 除了遠震因距離太遠或規模太大會產生**,則會以00取代)
- (也可用CheckPfileII.exe, 此為〈同仁〉以CheckPfile.for為底, 針對origin time=60的錯誤而改寫, 此錯誤會列入Checktime的ERROR, 2024/9/27新增檢查ERH或ERZ=0或>2)

- 6


---

## 第 7 頁：QC步驟及CheckPfile程式說明

- 步驟【2】-2

- > PE2  ERRFILE.BAT(檢視檔案內容, 可用記事本, Notepad++等編輯工具)
- 檢查結果, 有問題者會列在ERRFILE.BAT 中, 項目有:
- ⇒ OutofAREA：遠震(119>lon>123,  21>lat>26)(會以00取代**)
- ⇒ DATA TOO FEW ：測站數或PHASE數不夠(station no.<3 or phase no.<5)
- ⇒ NO_ML_&_mb：沒做規模或S13的規模欄全=0(地震太大時)
- ⇒ CheckPICK：震央距離排序有誤(可能PICKING後沒HYPO)
- ⇒ CheckPick：或測站數與相位數相同（ ie. 可能全部為P 或 只有S）
- ⇒ Checkpick : abs(residual)>設定值(P=3s, S=5s), 可在下指令時加-P# -S#(#為自訂的秒數)
- ⇒ ML=0 地震規模≤ 0.0 (大陸區的地震規模若第1次算不出來, 可結束跳出, 再按PICKING進去重新HYPO, 就會算出規模)
- ⇒ ML<0 地震規模≤,且存在某些測站視規模<0.0
- ⇒ ml<0 存在某些測站視規模<0.0
- ⇒ ml ? 某些測站測站視規模=0.01

- 7


---

## 第 8 頁：QC步驟及CheckPfile程式說明

- 步驟【2】-3

- 檢查結果, 有問題者會列在ERRFILE.BAT 中, 項目有:
- ⇒ CheckTIME：後面FILE的ORIGIN TIME 比前面早 （ie. .P24 的時間比.124 的時間晚）-時間排序有誤
- ⇒ CheckTime: 發震時與檔名時間略有差異
- Checktime：分鐘有錯或秒數=60秒者    (注意!00時的檔案HEADER, 常會跑到前一天的24時,需自行手動修改)
- ⇒ CHECK D<0 : DEPTH 小於0, 用3D MODEL易發生
- ⇒ LogAx : logA=-9.99 or 99.99
- ⇒??? : 距離震央最近的???個站未picking /     (表覆蓋率不好或近站沒點, >6站以上最好看一下震央及測站分布是否合理!)
- ⇒ H : hypo case not X or F
- ⇒ h : 未收斂 (出現 ”- ”)
- Q : quality not ABCD
- ⇒ Er=0 水平或垂直誤差=0	| 2024/9/27新增檢查ERH或ERZ=0
- ⇒ Er>2 水平或垂直誤差>2	| 2024/9/27新增檢查ERH或ERZ >2
- ※目前無法檢查權重大於5以上的錯誤,請自行留意!!
- ※CheckPfile已於101/2/20更新, 會以00取代遠震因過遠或規模過大,     而在P HEADER出現**的問題.

- 8


---

## 第 9 頁：QC步驟及程式說明

- 步驟【2】-4

- > ck_pfile  –P9  –Ilist.d  –Herrfile.bat
- ⇒產生檔案： ERRFILE.BAT，內為所LIST P FILES 之HEADERS
- (或用PHEAD.BAT, 只要加LIST FILENAME即可, 如:> PHEAD LIST.D,
- 欲執行ck_pfile程式需先建立暫存目錄 CheckPF)

- > bigsort -Pt errfile.bat
- (將P.DAT格式的INPUT FILE按時間先後順序排列, t:近->遠, T: 遠->近)
- > Notepad++  errfile.bat
- ⇒逐一FILE檢查 / 1. ORIGIN TIME太相近者（小於1秒者，可能重複了）， / 2. PHASE數少於5（最少3個站, 5個PHASE）， / 3. ERH, ERZ 太大者（>2.0以上），必要時重新檢視及定位， / 4. 有無規模為0或字母者。
- 全部檢查完後再重複步驟【2】
- 有感地震（〈有感地震目錄〉）檢查步驟同上。

- 9


---

## 第 10 頁：QC步驟及程式說明

- 步驟【3】-1

- PC (到DATABASE所在，即〈資料庫磁碟〉)
- > CD 〈資料庫磁碟〉的〈月份目錄〉
- > COPY 〈當日目錄〉\1919*.P*	⇒先將當日的P FILES COPY至DATABASE
- > COPY 〈當日目錄〉\1919*.1*, .2*, .3*….依此類推, 將所有P FILES COPY至DATABASE
- > DIR/B  1919*>TOTAL.LIS (或LIST.D亦可)
- > COPY 〈有感地震目錄〉\1919*.P*  ⇒再將有感地震的P FILES COPY至DATABASE
- > COPY 〈有感地震目錄〉\1919 *.1* , .2*, .3*….
- > DIR/B 1919*>TOTAL.LIS
- > RE_LIST1
- RE_LISTING> INPUT LISTING FILE NAME :  TOTAL.LIS (或LIST.D亦可)
- RE_LISTING> FILE CASE 1) P_FILE
- 2) A800, A900
- 3) IDS, K2, SSA
- 4) BUILDING :  1
- > CheckPfile  –LTOTAL.LIS  ⇒  ERRFILE.BAT
- > PE2  ERRFILE.BAT	⇒ 再檢查一次，
- 同步驟【2】中的PE2  ERRFILE.BAT。再檢查看有無漏網之魚?

- 10


---

## 第 11 頁：QC步驟及程式說明

- 步驟【3】-2

- > ck_pfile –P9 –Itotal.lis –Herrfile.bat
- ⇒產生檔案： ERRFILE.BAT，內為所LIST P FILES 之HEADERS
- (或用PHEAD.BAT, 只要加LIST FILENAME即可, 如:> PHEAD TOTAL.LIS)

- 挑出符合進資料庫檔案
- 方法一:
- 執行MPE2ver.20141008.exe  -> Eq-Sort  ->  Datafile  ->  〈月份目錄〉\ERRFILE.BAT
- [S]ta No. 3  -> 1000 : 注意測站數要大於3
- [O]utput -> a.dat [i]  =>產生在監測範圍(119/121 21/26)內的P.DAT
- 或:
- 方法二:
- 執行chooseadat.exe, input: ERRFILE.BAT 選時間在2024年7月、範圍在119/121 21/26 、測站數3個以上、arrival數5個以上, output至a.dat,與用mpe2搜尋同
- chooseadat +PERRFILE.BAT –T202407  =R119/123/21/26  =S3/999  =H5/999  –Oa.dat
- (用法參考: 附錄1-應用程式說明.docx)

- 11


---

## 第 12 頁：QC步驟及程式說明

- 步驟【3】-3

- > BIGSORT1	按時間排序
- **This program sort file data by time
- File case 1) *P.dat  2) *A.ind :   1
- Input *P.dat format filename :  A.DAT
- *P.dat made filename listing? (Y/N)  N
- 亦可用freesort.exe, 可輸入: FREESORT  –T  –FA.DAT    即可按時間順序排列. 或 bigsort -Pt errfile.bat
- > Notepad++  A.DAT
- 1. 目視檢查ORIGIN TIME太相近者（小於1秒者，可能重複了），
- 2. 目視檢查PHASE數少於5（最少3個站, 5個PHASE）。
- 確定沒問題後，將P HEADER所對應之P FILE NAME，
- 以垂直選取(Shift+Alt)方式將所有P FILE NAME 複製到TOTAL.LIS，
- 此為經SORTING後，按照時間順序排列且已排除遠震及站數少於3之FILE LIST，
- 將多餘之FILE NAME刪除後存檔。
- > CheckPfile  –LTOTAL.LIS
- 此時ERRFILE.BAT應為空的,若有則需再檢查一次,,
- 若為ORIGIN TIME與FILE  NAME 不同，則可略過。

- 12


---

## 第 13 頁：QC步驟及程式說明

- 步驟【3】-4

- > MERGEPO
- Input *P.dat format filename_1 :  202407P.DAT
- Input *P.dat format filename_2 :  ERRFILE.BAT
- ( 若用mergep.exe 則用法如右:  Mergep –F1filename1 –F2filename2 –Ooutfilename )
- > BIGSORT1
- **This program sort file data by time
- File case 1) *P.dat  2) *A.ind :   1
- Input *P.dat format filename :  202407P.DAT
- *P.dat made filename listing? (Y/N)  Y
- Give listing filename: 202407.LIS
- 若出現 REPEAT FILENAME，表示其FILENAME早已存在，將只保留一筆。
- 若出現 REPEAT TIME，則表示有相同FILE NAME但HEADER不同，
- 須再檢查是否要RENAME或刪除P.DAT內的HEADER。
- > COPY 202407P.DAT 〈備份磁碟〉	⇒ 備份一份到〈備份磁碟〉
- > COPY 202407P.DAT 〈本機資料庫目錄〉	⇒ 備份一份到自己電腦

- 13


---

## 第 14 頁：QC步驟及程式說明

- 步驟【3】-5

- 或以下列指令取代以上動作
- > UPDATEP.BAT  202407P.DAT	⇒將以上的動作寫成BATCH JOB.
- UPDATEP.BAT 的步驟（2024/5/10 更新，原文省略）：
  - 複製月份資料庫至本機與〈備份磁碟〉
  - 以 GdmsCatalog 處理月份資料庫
  - 依年份複製至〈目錄暫存區〉，並複製處理紀錄檔
  - 以 Pdat2Scdb 寫入 SCDB（2020/12/17 因應 SCDB 要求新增；重跑時以新資料取代舊資料，避免兩邊資料不一致）

- 14

**講者備註：**

> QC完成後請至RTD網頁認領日下
> 〈內部 RTD 網址〉
> CWB24區\認領地震\認領地震\認領QC
> 填寫地震個數及進資料庫個數


---

## 第 15 頁：QC步驟及程式說明

- 步驟【3】-6

- QC完成後請至RTD網頁認領日下
- (〈內部 RTD 網址〉)
- CWB24區\認領地震\認領地震\認領QC
- 填寫地震個數及進資料庫個數, 才算完成一日的QC

- 15


---

## 第 16 頁：QC步驟及程式說明

- 其他:
- > CWBPFILE +IINFILE.LIS +OOUT.CWB
- ⇒將氣象局P FILE轉成地球所TTSN的格式，所有P_FIEL 會串在一起 /    只在一個月全部做完後才做
- 例: cwbpfile +i202407.lis +o202407.cwb
- > COPY 202407.CWB 〈本機 IES 目錄〉	⇒ 備份一份到自己電腦
- > COPY 202407.CWB 〈備份磁碟 IES 目錄〉	⇒ 備份一份到〈備份磁碟〉
- > COPY 202407.CWB 〈國際交換目錄〉	⇒ 備份一份到〈國際交換目錄〉 (與ISC交換資料用，需另外申請權限)
- OR以下列指令取代以上動作
- > BACKIES  202407.CWB

- 16

**講者備註：**

> Backies.bat 的步驟（原文省略）：複製至本機、〈國際交換目錄〉與〈備份磁碟〉三處。


---

## 第 17 頁：QC步驟及程式說明

- 其他:
- Samp.exe
- 程式自動檢查P HEADER ORIGIN TIME太相近者
- （預設為3秒, 若小於1秒者，可能重複了需比對波形及震央位置）
- 請參考 附錄2-SameP使用方法.ppt
- Q&A
- Q: hypo後點event location plot, 出現”type mismatch”後, 程式當掉跳出
- A: 檢查P FILE第一行時間, 是否進位至前一天, 時間為24##, 手動修正後,即可.

- 17


---

## 第 18 頁：課程結束


---

## 附加文件：QC 檢查項目（紙本，來源 IMG_8853.HEIC）

> 由照片辨識轉錄，文字照原樣保留。

QC

1. time，年月日時分秒，無24時，60秒
2. weighting 0-4，有無出現其他數字，手誤
3. station name，有無空白？是否新增，HYPO3D.sta是否同步新增？
4. 殘差值大於3，特別標示，是否再檢查確認？
5. GAP>160度，需再確認有無改善空間
6. 規模<0，一般為儀器有問題，需刪除.
7. 規模=0.01，一般為尚未做HYPO，若HYPO後仍為0.01，則刪除
8. 遠震太遠或規模超過0以上，會出現'-'或其他文字，需修正為'0'
9. 進資料庫時，檢查是否有重複？秒差<2秒，位置相近？
10. 是否為遠震？遠震一般不入資料庫，但若為有感地震則會放入資料庫，主動詢問是否放入資料庫。
