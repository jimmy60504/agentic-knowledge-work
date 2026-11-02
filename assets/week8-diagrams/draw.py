#!/usr/bin/env python3
"""第八週的示意圖，尺寸 1600×900。示意的數值與站名都不是實際資料，圖上另有註明的除外。"""
from pathlib import Path

HERE = Path(__file__).parent
INK, MUTED, LINE, BG, ACCENT, ACCENT_BG = "#2A2623", "#6B6560", "#D8D2C9", "#F5F2EC", "#BE8979", "#F6E9E4"
BLUE, BLUE_BG = "#5F7F95", "#E8EFF3"
COLORS = {"am": MUTED, "aa": ACCENT, "ab": BLUE}


def width(s, size):
    return sum(size if ord(c) > 255 else size * 0.56 for c in s)


class Fig:
    def __init__(self, name, title, sub=None):
        self.name, self.out = name, [
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900" font-family="PingFang TC, Hiragino Sans GB, sans-serif">',
            f'<defs>{"".join(self.marker(i, c) for i, c in COLORS.items())}</defs>',
            '<rect width="1600" height="900" fill="#FFFFFF"/>']
        self.text(60, 80, title, 44, INK, 600, "start")
        if sub:
            self.text(60, 132, sub, 24, MUTED, 400, "start")

    @staticmethod
    def marker(i, c):
        return f'<marker id="{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'

    def text(self, x, y, s, size=24, fill=INK, weight=400, anchor="middle"):
        self.out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="central">{s}</text>')

    def box(self, x, y, w, h, title=None, lines=(), kind="", tsize=28, size=22):
        fill, stroke, sw = {"hot": (ACCENT_BG, ACCENT, 3), "blue": (BLUE_BG, BLUE, 3), "plain": ("#FFFFFF", LINE, 2)}.get(kind, (BG, LINE, 2))
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        for s, z in [(title, tsize)] + [(l, size) for l in lines]:
            if s and width(s, z) > w - 16:
                raise ValueError(f"{self.name}：放不下「{s}」")
        step = size + 12
        total = (tsize + 14 if title else 0) + step * len(lines) - (12 if lines else 14 if title else 0)
        cy = y + h / 2 - total / 2
        if title:
            self.text(x + w / 2, cy + tsize / 2, title, tsize, INK, 600)
            cy += tsize + 14
        for l in lines:
            self.text(x + w / 2, cy + size / 2, l, size, MUTED)
            cy += step

    def arrow(self, x1, y1, x2, y2, color="am", dash=False, sw=3):
        d = ' stroke-dasharray="10 7"' if dash else ""
        self.out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{COLORS[color]}" stroke-width="{sw}"{d} marker-end="url(#{color})"/>')

    def curve(self, d, color="aa", dash=True, sw=4):
        da = ' stroke-dasharray="12 8"' if dash else ""
        self.out.append(f'<path d="{d}" fill="none" stroke="{COLORS[color]}" stroke-width="{sw}"{da} marker-end="url(#{color})"/>')

    def foot(self, s, y=820, size=28):
        if width(s, size) > 1500:
            raise ValueError(f"{self.name}：底註太長「{s}」")
        self.text(800, y, s, size, INK, 600)

    def save(self):
        (HERE / f"{self.name}.svg").write_text("\n".join(self.out + ["</svg>"]) + "\n", encoding="utf-8")


def route():
    f = Fig("w8-02-route", "本週的路線", "系統仍在開發，本週說明設計方向，細節用來佐證方向可行")
    items = [("一", "合併的理由", ["以流程解決", "QC 的問題"], ""), ("二", "資料與介面", ["資料存在資料庫", "只在邊界轉換"], "hot"),
             ("三", "畫面", ["即時回饋", "任務列表"], "hot"), ("四", "接上現行流程", ["分階段替換"], ""),
             ("五", "新的處理想法", ["更標準", "步驟更少"], ""), ("六", "開發的時間成本", ["設計的迭代", "仍需要時間"], "")]
    w, gap, x = 225, 26, 60
    for i, (n, t, ls, k) in enumerate(items):
        f.box(x, 280, w, 300, None, [], k)
        f.text(x + w / 2, 330, n, 40, ACCENT, 600)
        f.text(x + w / 2, 395, t, 24 if len(t) > 5 else 28, INK, 600)
        for j, l in enumerate(ls):
            f.text(x + w / 2, 460 + j * 36, l, 21, MUTED)
        if i < 5:
            f.arrow(x + w + 2, 430, x + w + gap - 2, 430)
        x += w + gap
    f.text(800, 690, "下一步與結語：實際試用、互動式教學、自動挑波、新的交付模式", 28, INK, 600)
    f.save()


def event_order():
    f = Fig("w8-04-event-order", "事件順序的處理方式", "以虛構的時間為例：重新定位到很遠的地震，發震時間變早")
    f.text(60, 240, "現行", 30, INK, 600, "start")
    f.box(200, 180, 310, 120, "第一個檔 02:50", ["第二個檔 03:20"], "", 24, 24)
    f.arrow(512, 240, 628, 240)
    f.box(630, 180, 380, 120, "第二個檔重新定位", ["發震時間變為 01:40"], "", 24, 22)
    f.arrow(1012, 240, 1128, 240)
    f.box(1130, 180, 410, 120, "檔名與時間順序顛倒", ["QC 攔下，回頭修改"], "hot", 24, 22)
    f.text(60, 500, "翻新後", 30, INK, 600, "start")
    f.box(200, 440, 310, 120, "事件存在資料庫", ["以事件本身識別"], "blue", 24, 22)
    f.arrow(512, 500, 628, 500, "ab")
    f.box(630, 440, 380, 120, "重新定位", ["只更新這個事件的定位解"], "blue", 24, 22)
    f.arrow(1012, 500, 1128, 500, "ab")
    f.box(1130, 440, 410, 120, "輸出時才排序", ["依發震時間產生檔名"], "blue", 24, 22)
    f.foot("順序與檔名在輸出時決定，挑波過程不會產生這類錯誤。", 680)
    f.save()


def fixed_format():
    f = Fig("w8-07-fixed-format", "沿用數十年的固定格式", "各程式獨立演化，彼此以檔案交接，任何一支程式都難以更改格式")
    cells = [("年月日", 150), ("時分", 90), ("秒", 90), ("緯度", 110), ("經度", 110), ("深度", 90), ("規模", 90), ("站數", 80), ("定位品質", 130)]
    x = 110
    f.text(x, 225, "每個欄位的寬度都已固定（示意）", 24, MUTED, 400, "start")
    for name, w in cells:
        f.box(x, 260, w, 90, name, [], "plain", 22)
        x += w
    f.box(x + 10, 260, 170, 90, "新資訊？", [], "hot", 24)
    for i, (t, ls) in enumerate([("無法記錄歷史", ["沒有多餘的位置", "重新定位時整檔改寫"]), ("精度受到限制", ["小數位數由欄寬決定"]), ("新資訊難以加入", ["多支程式都依賴這個格式"])]):
        f.box(110 + i * 470, 470, 440, 170, t, ls, "", 28, 22)
    f.foot("已無法應付現在的需求。", 750)
    f.save()


def project_db():
    f = Fig("w8-09-project-db", "專案資料庫的內容", "想法來自反射震測處理系統與其他類似的地震分析軟體")
    f.box(590, 330, 420, 200, "專案資料庫", ["各模組共用", "資料與處理都在專案內"], "blue", 34, 24)
    parts = [(120, 190, "事件", ["工作的單位", "有自己的狀態"]), (120, 400, "定位解", ["每次定位都保留一版"]), (120, 610, "挑選與關聯", ["依 QuakeML 的概念拆分"]),
             (1080, 190, "工作紀錄", ["每次輸入與輸出", "查得到根據哪一版"]), (1080, 400, "波形索引", ["原檔留在外部"]), (1080, 610, "進度", ["以工作日計算"])]
    for x, y, t, ls in parts:
        f.box(x, y, 400, 130, t, ls, "", 26, 22)
        if x < 500:
            f.arrow(522, y + 65, 588, 430 + (y - 400) * 0.25, "ab")
        else:
            f.arrow(1078, y + 65, 1012, 430 + (y - 400) * 0.25, "ab")
    f.save()


def page_map():
    f = Fig("w8-13-page-map", "測站分頁與地圖的對應", "示意圖：站名為虛構。不同分頁中位置相近的列，對應的測站在地圖上也相近")
    pages = [("第 1 頁", ["A1", "A2", "A3", "A4", "A5"]), ("第 2 頁", ["B1", "B2", "B3", "B4", "B5"]), ("第 3 頁", ["C1", "C2", "C3", "C4", "C5"])]
    for i, (p, sts) in enumerate(pages):
        x = 150 + i * 210
        f.text(x + 90, 215, p, 26, INK, 600)
        for j, s in enumerate(sts):
            f.box(x, 245 + j * 88, 180, 72, s, [], "hot" if j == 2 else "plain", 24)
    f.text(95, 400, "由北", 22, MUTED)
    f.text(95, 435, "而南", 22, MUTED)
    f.out.append(f'<path d="M1120,200 C1230,210 1290,300 1270,410 C1255,520 1200,650 1130,700 C1050,650 1010,520 1020,400 C1030,290 1060,215 1120,200 z" fill="{BG}" stroke="{LINE}" stroke-width="2"/>')
    for x, y in [(1110, 250), (1170, 300), (1070, 330), (1130, 360), (1230, 340), (1115, 590), (1160, 620), (1095, 640)]:
        f.out.append(f'<circle cx="{x}" cy="{y}" r="9" fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>')
    for x, y in [(1110, 450), (1165, 475), (1085, 500)]:
        f.out.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{ACCENT}"/>')
    f.text(900, 445, "同一列", 24, ACCENT, 600)
    f.arrow(795, 476, 1065, 476, "aa", True)
    f.text(800, 770, "前三頁同一列的測站，距離中位數 39 至 84 公里，隨機打亂時為 135 至 150 公里（實際測站）。", 26, INK, 600)
    f.save()


def feedback():
    f = Fig("w8-16-feedback", "迭代週期的對照", "短時間得到回饋，操作時累積體感，知道哪些值如何影響最終結果")
    f.text(60, 260, "過去", 30, INK, 600, "start")
    for x, w, t in [(190, 260, "修改到時"), (510, 260, "全部跑完"), (830, 320, "自己想辦法畫圖"), (1210, 290, "才看到結果")]:
        f.box(x, 210, w, 100, t, [], "", 26)
    for a, b in ((452, 508), (772, 828), (1152, 1208)):
        f.arrow(a, 260, b, 260)
    f.curve("M1355,312 C1355,410 335,410 320,318", "am")
    f.text(800, 420, "一次迭代的週期很長", 24, MUTED)
    f.text(60, 620, "現在", 30, INK, 600, "start")
    f.box(190, 560, 260, 110, "修改到時", [], "blue", 26)
    f.box(620, 560, 420, 110, "地圖與殘差立即更新", [], "blue", 26)
    f.curve("M452,590 C520,540 560,540 618,590", "ab", False)
    f.curve("M618,645 C560,700 520,700 452,645", "ab", False)
    f.text(1090, 615, "反覆多次，在腦中建立連結", 26, BLUE, 600, "start")
    f.save()


def task_rewrite():
    f = Fig("w8-19-task-rewrite", "同一條規則的兩種寫法", "由批評與阻擋轉為正向引導")
    f.text(380, 215, "錯在哪裡", 32, MUTED, 600)
    f.text(1140, 215, "還有哪件事要完成", 32, ACCENT, 600)
    rows = [("測站數不足", "挑選足夠的測站"), ("近站未挑選", "挑選更近的測站"), ("方位角空隙過大", "確保震央穩定"), ("殘差過大", "檢查離群的到時")]
    for i, (a, b) in enumerate(rows):
        y = 255 + i * 118
        f.box(110, y, 540, 98, a, [], "plain", 28)
        f.arrow(670, y + 49, 840, y + 49, "aa")
        f.box(860, y, 560, 98, b, [], "hot", 28)
    f.foot("剛開始挑波時測站數不足，呈現為尚未完成，不列為錯誤。", 790)
    f.save()


def save_gate():
    f = Fig("w8-20-save-gate", "挑波時不阻擋，攔截在後面", "所有狀態都在專案資料庫內")
    f.box(70, 300, 330, 180, "挑波", ["任務列表即時提示"], "blue", 30, 22)
    f.box(470, 300, 330, 180, "存檔", ["只寫入資料庫", "接近工作階段的暫存"], "", 30, 22)
    f.box(870, 300, 310, 180, "事件總覽的 QC", ["實際的攔截"], "hot", 28, 22)
    f.box(1250, 300, 290, 180, "匯出", ["相位檔、入庫包"], "", 30, 22)
    f.arrow(402, 390, 468, 390)
    f.arrow(802, 390, 868, 390)
    f.arrow(1182, 390, 1248, 390)
    f.text(1215, 360, "通過", 20, MUTED)
    f.curve("M1025,482 C1025,640 235,640 235,484")
    f.text(630, 650, "未通過時回來修改", 26, ACCENT, 600)
    f.save()


def auto_weight():
    f = Fig("w8-25-auto-weight", "自動權重的判斷規則", "教材沒有「多清楚算清楚」的數值，改以訊噪比算出建議的權重，讓處理標準化")
    f.box(70, 340, 300, 150, "挑選的到時", ["計算訊噪比"], "", 28, 22)
    for y, a, b, k in [(230, "不濾波就清楚", "權重 0、1", "blue"), (390, "要濾波才清楚", "權重 2", "plain"), (550, "濾波後仍不清楚", "權重 3", "plain")]:
        f.box(520, y, 460, 120, a, [], "plain", 28)
        f.box(1130, y, 340, 120, b, [], k, 30)
        f.arrow(372, 415, 518, y + 60)
        f.arrow(982, y + 60, 1128, y + 60)
    f.foot("門檻來自同仁實際給的權重，與同仁確認之前不視為定案。", 780)
    f.save()


def pick_first():
    f = Fig("w8-26-pick-first", "挑波順序的對照", "距離很遠看到一個地震時，常不確定是不是同一個地震")
    f.text(60, 265, "現行", 30, INK, 600, "start")
    for x, w, t, k in [(190, 280, "先開一個事件", ""), (540, 280, "在事件裡挑波", ""), (890, 310, "不是同一個地震", "hot"), (1270, 270, "刪掉重來", "hot")]:
        f.box(x, 210, w, 110, t, [], k, 26)
    for a, b in ((472, 538), (822, 888), (1202, 1268)):
        f.arrow(a, 265, b, 265)
    f.text(60, 540, "先挑", 30, INK, 600, "start")
    f.text(60, 582, "再關聯", 30, INK, 600, "start")
    for x, w, t in [(190, 280, "看到起跳就先挑"), (540, 280, "挑選都先留著"), (890, 310, "關聯成候選事件"), (1270, 270, "由人確認")]:
        f.box(x, 505, w, 110, t, [], "blue", 26)
    for a, b in ((472, 538), (822, 888), (1202, 1268)):
        f.arrow(a, 560, b, 560, "ab")
    f.foot("產出仍是同格式的相位檔，改變的只有挑波的順序，可能少掉很多步驟。", 740)
    f.save()


def std_iter():
    f = Fig("w8-29-std-iterations", "一個小功能的反覆修改", "波形的標準差截斷：21 分鐘內修改 7 次（依修改紀錄）")
    steps = [("08:01", "加上", "截離群"), ("08:02", "預設", "改為關閉"), ("08:04", "加上", "滑桿"), ("08:05", "上限", "改為 5"), ("08:08", "改名", "標準差"), ("08:10", "調整", "位置"), ("08:22", "改為", "三個按鈕")]
    w, gap, x = 192, 20, 60
    f.out.append(f'<line x1="60" y1="300" x2="1540" y2="300" stroke="{LINE}" stroke-width="4"/>')
    for i, (t, a, b) in enumerate(steps):
        last = i == len(steps) - 1
        f.out.append(f'<circle cx="{x + w / 2}" cy="300" r="10" fill="{ACCENT if last else MUTED}"/>')
        f.text(x + w / 2, 255, t, 24, MUTED)
        f.box(x, 340, w, 170, a, [b], "hot" if last else "", 26, 24)
        x += w + gap
    f.foot("需求要看到畫面才能確定，這些修改只能由人實際操作之後提出。", 640)
    f.save()


def software_org():
    f = Fig("w8-31-software-org", "軟體與組織一起演化", "軟體反映組織的流程與溝通方式（康威定律，Conway 1968）")
    cols = [("現行系統", ["組織與當初設計時不同", "陸續補上許多模組", "修補反映實際的運作"], ""),
            ("新系統", ["一開始的設計", "實際使用時產生摩擦", "經由迭代符合實際情況"], "hot"),
            ("周邊的調整", ["組織的分工可能轉變", "基礎設施可能重新調整", "（例如波形的存放與讀取）"], "")]
    for i, (t, ls, k) in enumerate(cols):
        f.box(70 + i * 495, 230, 470, 330, t, ls, k, 34, 24)
    f.foot("新系統的迭代，就是花時間的地方。", 680, 32)
    f.save()


def span():
    f = Fig("w8-34-span", "一個人能跨越的範圍", "過去的程式邊界與分工有關（推測）")
    steps = ["切事件", "挑波", "定位", "檢查"]
    f.text(60, 275, "過去", 30, INK, 600, "start")
    for i, s in enumerate(steps):
        f.box(200 + i * 340, 210, 300, 130, s, ["各自的程式"], "", 28, 22)
    for i in range(3):
        f.arrow(502 + i * 340, 275, 538 + i * 340, 275)
    f.text(860, 380, "彼此以檔案交接", 24, MUTED)
    f.text(60, 565, "現在", 30, INK, 600, "start")
    f.out.append(f'<rect x="200" y="470" width="1320" height="190" rx="14" fill="{BLUE_BG}" stroke="{BLUE}" stroke-width="3"/>')
    for i, s in enumerate(steps):
        f.box(220 + i * 325, 490, 305, 90, s, [], "plain", 26)
    f.text(860, 622, "一個懂領域的人配上 Agent，可以同時處理，合併成一個系統才變得可行", 25, BLUE, 600)
    f.foot("代價是系統集中依賴少數人，接手與交接值得一起討論。", 760)
    f.save()


def delivery():
    f = Fig("w8-36-delivery", "新的交付模式（構想）", "多一個選擇：緊急又不大的問題，不必等開發者安排時間")
    f.box(90, 210, 620, 240, "業務單位", ["透過設計好的 Agent 流程", "自行完成小幅的修改", "概念接近駐點工程師"], "blue", 34, 24)
    f.box(890, 210, 620, 240, "開發者", ["建立整個流程", "處理大的功能與重新設計", "仍然可以直接請開發者修改"], "hot", 34, 24)
    f.arrow(715, 300, 885, 300, "ab")
    f.text(800, 268, "回報大的需求", 22, BLUE, 600)
    f.arrow(885, 380, 715, 380, "aa")
    f.text(800, 412, "交付流程與基準", 22, ACCENT, 600)
    f.box(90, 520, 1420, 150, "讓修改可以安全進行的條件", ["明確的修改範圍、測試基準、設計紀錄"], "", 30, 26)
    f.save()


def sdlc():
    f = Fig("w8-sdlc-cost", "軟體開發生命週期的時間成本", "示意圖：寬度表示相對的時間，不是實際工時")

    def row(y, label, blocks):
        f.text(60, y + 75, label, 30, INK, 600, "start")
        x, spans = 250, {}
        for name, sub, w, hot in blocks:
            f.box(x, y, w, 150, name, sub, "hot" if hot else "", 28, 20)
            spans[name] = (x, w)
            x += w + 8
        return spans
    row(210, "過去", [("需求", [], 120, False), ("設計", ["規劃資料庫", "與資料格式"], 280, True), ("實作", ["撰寫功能與重構"], 460, True), ("測試", ["功能完成後進行"], 200, False), ("部署", [], 120, False)])
    sp = row(540, "使用 Agent", [("需求", [], 120, False), ("設計", ["畫面與操作", "要看到才能確定"], 340, True), ("實作", ["Agent", "很快完成"], 150, False), ("測試與驗證", ["人實際操作，提出修改"], 340, True), ("部署", [], 120, False)])
    dx, dw = sp["設計"]
    tx, tw = sp["測試與驗證"]
    x1, x2 = tx + tw / 2, dx + dw / 2
    f.curve(f"M{x1},534 C{x1},460 {x2},460 {x2},534")
    f.text((x1 + x2) / 2, 452, "反覆多次，直到符合需要", 24, ACCENT, 600)
    f.text(800, 790, "Agent 縮短了實作的時間，設計的迭代與驗證仍然需要人投入時間。", 30, INK, 600)
    f.save()


for fn in (route, event_order, fixed_format, project_db, page_map, feedback, task_rewrite, save_gate, auto_weight, pick_first, std_iter, software_org, span, delivery, sdlc):
    fn()
