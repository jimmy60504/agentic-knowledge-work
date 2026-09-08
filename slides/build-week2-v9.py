# 第二週投影片 v9：素版。只放內容與圖，不做特別排版；版面之後再用第三圈調。
# 內容以 drafts/08-week2-slide-copy.md 為準，這裡的 PAGES 同時回寫該檔的「內文／圖」欄。
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = lambda *p: os.path.join(ROOT, 'assets', *p)
DARK = RGBColor(0x2A, 0x26, 0x23); ACCENT = RGBColor(0xB8, 0x50, 0x42); MUTED = RGBColor(0x6B, 0x65, 0x60)
FONT = 'PingFang TC'

# 每頁：(標題, 類型, 內文, 圖, 備註)
# 類型 title / section / body / step；內文為條列，子條列用 tuple(標籤, [條])
PAGES = [
 ('先玩玩看 agent 吧', 'title', ['Agent 時代的知識工作｜第二週'], None,
  '上次介紹了 agent 是什麼，這次讓大家有個方向怎麼學。前半段 30 分講怎麼合作，示範 30 分看一遍，練習 120 分自己做一份。'),
 ('AI 是放大器：領域知識 × agent 能力', 'body', [
  '領域知識：知道方法的因果關係，知道現在缺什麼、該怎麼跟 agent 講才會得到預期的結果',
  '駕馭 agent 的能力：知道不同模型擅長什麼、能做到什麼程度，偏工具的熟悉度',
  '兩邊都要有，才發揮得出來'], None,
  '兩個族群。學得快沒有包袱的，缺的是領域知識；經驗老到的，不用把原本工作流程打掉換新的，分析自己工作流裡重複機械式或目標明確的部分，用 agent 試試看，也可以去補過去一直想補但沒時間補的短板。'),
 ('把 AI 當同事', 'body', [
  ('請教', ['像請教不同領域的同事，先以自己的想法為主，不被牽著走', '例：GDMS 的新進同仁最常卡在哪裡，有什麼介紹方式']),
  ('交辦', ['講明確的方向跟重要的限制：格式、範圍、長度；具體怎麼做留給它', '例：只用 GDMS 公開頁面，做 10 到 12 頁，先給我逐頁稿']),
  '最省事的交辦：只給一句話、不給材料、不請教'], None,
  '太籠統會沒跟自己對齊，太細節可能會錯過更好的方法。已有自己累積的工作流程，不用急著全部切換。示範開頭會先做一次只給一句話的版本。'),
 ('從自己需要補足的地方開始', 'body', [
  '缺知識與方向：請它拓展材料',
  '有想法但不熟工具：請它實作',
  '簡單重複的雜工：交給它整理與排版',
  '需要人抓盲點：讓它當審查者'], None,
  '同一件事可能同時需要幾種。選定之後，下一步是把需要向 agent 說清楚。'),
 ('交付物代表自己', 'body', [
  '用幾句話完成什麼東西看起來很厲害，但那不是你要的東西',
  '與其 AI 一次吐一堆看不完的東西，不如一點一點的把工作流程替換',
  '右圖：一句話生成的對照組。做得不錯，拿去報就會卡，被問就答不出來'], A('week2-baseline', 'baseline-method-card.png'),
  '對照組的反應：做得不錯，但拿去報就會卡，被問就答不出來。漂亮這點可以吸收，後面第三圈會用到。'),
 ('東西都要外部化存起來', 'body', [
  'AGENTS.md　給 agent 的工作規則',
  '工作紀錄.md　每次的決定與待辦',
  'kb/　材料與筆記，分 arguments 與 tools',
  'drafts/　文稿、逐頁稿與棄案',
  'skills/　用過有效的標準',
  'assets/　圖與素材',
  'slides/　成品',
  'lessons/　公開教材',
  'tmp/　不進 git'], None,
  '有自己熟悉的整理方式，叫 agent 先照抄也可以。這個結構是這幾週跟 agent 互動長出來的，不是一開始設計的；kb 昨天才分成論點類與工具類。'),
 ('三個迴圈', 'section', [], None,
  '內容不是一次寫成的。先一張全圖，之後每圈兩頁：一頁講那一圈怎麼走，一頁用這份投影片當實例。'),
 ('內容要走三個迴圈', 'body', [
  '確認方向、建立架構、調整風格，每圈都有人的判斷（紅框）',
  '每圈以自己的產物收尾，產物就是這一圈的檢驗：文稿測方向、逐頁稿測架構、成品測風格',
  '測不過就退回：出現新資料時重看方向、內容有問題則退回架構',
  '對得上軟體開發：需求探索、建立架構、寫程式'], A('week2-diagrams', 'three-loops-mermaid.png'),
  '跟軟體開發對得上，需求探索、建立架構、寫程式。接下來各看一圈。'),
 ('確認方向', 'body', [
  '概念：帶著問題探索材料，人補入洞見，agent 順著討論長成文稿',
  '產出物：文稿',
  '通過標準：文稿讀過撐得住方向，不必回頭改主軸'], A('week2-diagrams', 'three-loops-mermaid-h1.png'),
  '有自己的想法就先以自己的為主，洞見在這一圈進去，成果才代表自己；不必先寫大綱，討論本身就會長成文稿。文稿讀起來撐不住，就回頭補充探索或改方向；後面才看到的資料也可能推翻論點，但會隨著交付日期接近而鎖定。'),
 ('確認方向：方向改了三次才定下來', 'body', [
  ('方向', ['9/2 文件專案化與模型能力', '9/4 公部門用 AI 的阻礙與規範', '9/6 先體驗 agent']),
  ('補入的洞見', ['迭代回圈小一點，內容留在 md', '一直在改就是缺一個原則，先找原則再套用', '第三個迴圈，讓交付物對齊自己的標準']),
  ('文稿退回的', ['客服例子不好講，拿掉', 'NESA 與三種形式的對照組整段移出', '兩輪試跑看不懂的句子改寫'])], None,
  '方向改了不算失敗。文稿是方向的檢驗：兩輪學員試跑都看不懂的句子，退回來改的是方向與說法；總時數定為 60 分之後，文稿才有尺可量。連迴圈圖本身也改了五次才定型。'),
 ('建立架構', 'body', [
  '概念：agent 把文稿排成逐頁稿，人連讀後調整邏輯順序，agent 提議刪併，人決定取捨',
  '產出物：逐頁稿',
  '通過標準：只讀標題連讀能講完故事'], A('week2-diagrams', 'three-loops-mermaid-h2.png'),
  '逐頁稿的前置是只有標題的 ghost deck，一頁一句主張，連讀就看得出跳接。文稿像文章，投影片分口述跟畫面，節奏不一樣。越快進到具體改起來越慢，所以順序在 md 上調好再往下。'),
 ('建立架構：文稿排成逐頁稿', 'body', [
  ('生成的標題 → 原話當底的標題', [
   '還沒有方法時請教 → 聊天像請教導師 → 把 AI 當同事',
   '開空專案，建 kb 與 AGENTS.md → 開空專案',
   '確認表達 → 調整風格',
   '判準 → 標準',
   '交付出去的東西是要負責的 → 交付物代表自己']),
  '每頁標題附原話出處與日期，agent 補的標【無原話】'], None,
  '生成的標題句通順但認不出自己的思路，改了七版還不是要的感覺；換成原話當底才看得懂、才判斷得了順序。這個做法留在 skills 裡。'),
 ('建立架構：連讀後調整順序與刪併', 'body', [
  ('調整順序', ['先講迴圈再講實例', '保存接在流程後面', '把 AI 當同事前移，外部化接交付責任', '迴圈與實例穿插，各接在對應的圈後面']),
  ('刪併取捨', ['刪研究專案情境頁', '刪練習時間表頁', '段落頁加了又減', '歷程從五頁併成三頁'])], None,
  'agent 提的是刪併建議，留哪頁、什麼順序是人決定的。連讀能講完故事，架構才算定。原本以為分頁在第三圈，改名建立架構之後才看清楚它是第二圈的起點。'),
 ('調整風格', 'body', [
  '概念：agent 尋找風格規則寫成標準，依標準產出一版，人依自身品味檢視整份',
  '產出物：成品',
  '通過標準：整份看像自己，試講過得去'], A('week2-diagrams', 'three-loops-mermaid-h3.png'),
  '先語氣再版面，兩個面向做法相同。人依品味看哪裡不像自己，改的是標準不是那一頁；自己有判斷力的面向直接拿規則檔，用過有效的補進 AGENTS.md，下次這一格就變短。看成品發現的內容問題退回第二圈。'),
 ('調整風格：這份投影片從第一版排到現在', 'body', [
  ('找到的標準', ['視覺設計規則一份', '文案語氣規則一份', '廠商語氣指引筆記']),
  ('產出', ['每版整份重建，不在 PPTX 上手改']),
  ('人檢視後改的標準', ['圖示統一用一套單色', '文字改書面語與原話', '流程圖改 mermaid 直式']),
  '右圖：第一版的第 2 頁'], A('week2-deck-history', 'v3-page02.png'),
  '每次都是整份重建，不在 PPTX 上手改；看畫面發現的內容問題退回前兩圈。'),
 ('示範：向新進同仁介紹 GDMS', 'section', ['示範 30 分'], None,
  '講師走一遍八步，只展開一條論點。學員記兩件事：自己會加哪個條件，最想先試哪一步。'),
 ('開始前先確認資料去哪裡', 'body', [
  '資料使用設定：把提供訓練關掉',
  'repo 公開與否：push GitHub 就是上雲，練習不用機密資料',
  'PPTX 製作路徑：agent 產出可編輯檔',
  '預覽方式：匯出 PDF 或圖片再看',
  '先把「幫我做一份向新進同仁介紹 GDMS 的簡報」貼給 agent，在背景做第一版'], None,
  '示範只展開一條論點。接下來八頁，示範時看，練習時照做。'),
 ('第一步：開空專案', 'step', [
  ('做什麼', ['開一個空的資料夾，先講這個專案大致要做什麼']),
  ('對 agent 說', ['建立 kb，把討論都寫進 kb；這個規則寫進 AGENTS.md']),
  ('確認什麼', ['開啟檔案看寫了什麼，太長就刪短，之後明確請它讀取'])], None,
  '準備。有自己熟悉的整理方式就叫 agent 照抄。開啟檔案確認、太長就刪短、明確請它讀取，這三條來自試跑。'),
 ('第二步：講背景與限制', 'step', [
  ('做什麼', ['用聊天講受眾、用途、時間、簡報長度、材料範圍']),
  ('對 agent 說', ['問它建議，最後落成 md 存起來；預設題只用 GDMS 公開頁面']),
  ('確認什麼', ['每份材料實際開啟、附來源；30 分停止搜尋'])], None,
  '確認方向。每份實際開啟、附來源、30 分停止搜尋，來自試跑。任何一步卡住都可以再找一輪材料。'),
 ('第三步：先找出想講的方向', 'step', [
  ('做什麼', ['先自己說想講的方向與理由']),
  ('對 agent 說', ['沿這個方向拓展，看有沒有要調整的；想不到時讓它先試串']),
  ('確認什麼', ['逐段說認同或修改的理由；棄案另存並記理由'])], None,
  '確認方向。想不到時讓它先試串，自己逐段說認同或修改的理由。例：把「介紹所有功能」收斂到「回答新同仁最先遇到的問題」。'),
 ('第四步：起草文稿', 'step', [
  ('做什麼', ['把討論與洞見寫成文稿，讀過確認方向撐得住']),
  ('對 agent 說', ['在主 draft 沿方向寫一版；把它的話順成自己的話，補來源']),
  ('確認什麼', ['挑一句斷言查證，例如「系統功能完整，適合所有使用者」缺了條件'])], None,
  '確認方向。挑一句斷言查證是試跑後加的動作，學員不會主動做，第 50 分鐘全場再示範一次。'),
 ('第五步：分成逐頁稿', 'step', [
  ('做什麼', ['把文稿分成逐頁稿']),
  ('對 agent 說', ['先用我的原話排一版只有標題的 ghost deck，每頁一句']),
  ('確認什麼', ['只讀標題連讀能講完故事；順序與取捨改好，再請它補每頁畫面與口述'])], None,
  '建立架構。第一版邏輯用原話當底，看得懂才判斷得了順序；連讀通過之後才變成確定的逐頁稿，之後的修改都在這份檔案上做。分頁的原則不必另外找，一頁一句主張、畫面是證據，直接寫進對 agent 說的話裡。'),
 ('第六步：修改語氣', 'step', [
  ('做什麼', ['整份改成書面文，不做金句']),
  ('對 agent 說', ['逐頁改寫並標出沒有原話依據的句子；標準來源：原話、文案語氣規則、維基 AI 寫作特徵清單、OpenAI 與 Anthropic 的語氣指引']),
  ('確認什麼', ['自己讀一遍，改掉不像自己的'])], None,
  '調整風格。請 agent 逐頁改寫並標出沒有原話依據的句子，自己讀一遍改掉不像自己的。看畫面最刺眼的口號句在這一步解決。'),
 ('第七步：找排版原則', 'step', [
  ('做什麼', ['先做一頁驗路徑，之後整份產出']),
  ('對 agent 說', ['先找排版的規則寫成標準；交逐頁稿與標準，整份產出並匯出圖片']),
  ('確認什麼', ['版面問題改標準重建；內容問題退回第五、六步'])], None,
  '調整風格。第一次先做一頁驗路徑，之後整份產出。版面問題改規則重建，內容問題退回第五、六步。'),
 ('第八步：整個過一遍', 'step', [
  ('做什麼', ['自己講一遍並計時']),
  ('agent 無法代做', ['親自在簡報軟體點選文字，確認可編輯']),
  ('確認什麼', ['開頭說的需求每項都在成品裡'])], None,
  '確認。不用兩人一組，自己找時間真的講一遍，算是一個確認。'),
 ('練習', 'section', ['練習 120 分'], None, '自由發揮，不收成品。'),
 ('練習：題目自選', 'body', [
  ('題目三條件', ['給誰看', '看完要做什麼', '材料公開或可虛構，兩小時找得到依據']),
  ('開始時兩件事', ['先貼一句話讓 agent 在背景做第一版', '開另一個視窗，走八步']),
  ('成品', ['不收，自己留著比較；預設題同示範題'])], None,
  '預設題同示範題。第 10 分鐘巡一輪，寫不出受眾與用途者改用預設題。'),
 ('回看：第一版和自己做的並排', 'body', [
  '把一句話生成版與自己逐步完成版並排',
  ('三問對三圈', ['方向與洞見是自己的嗎', '順序是自己調的嗎', '風格照了哪份標準']),
  '說不出理由的那頁，內容還不是自己的'], None,
  '說不出理由的那頁，內容還不是自己的。三問對回三圈。'),
]

def set_font(run, size, bold=False, color=DARK):
    run.font.name = FONT; run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    for tag in ('a:ea', 'a:cs'):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {}); rPr.append(el)
        el.set('typeface', FONT)

def textbox(slide, x, y, w, h, lines, size=18, color=DARK, bold=False, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    first = True
    for item in lines:
        if isinstance(item, tuple):
            label, subs = item
            p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
            r = p.add_run(); r.text = label; set_font(r, size, True, color); p.space_before = Pt(8)
            for sub in subs:
                p = tf.add_paragraph(); r = p.add_run(); r.text = '・' + sub; set_font(r, size - 2, False, color); p.level = 1
        else:
            p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
            r = p.add_run(); r.text = item; set_font(r, size, bold, color); p.space_before = Pt(6)
    return tb

def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

def build(out):
    prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    W, H = prs.slide_width, prs.slide_height; blank = prs.slide_layouts[6]
    for i, (title, kind, body, img, note) in enumerate(PAGES, 1):
        s = prs.slides.add_slide(blank)
        if kind in ('title', 'section'):
            bg = s.shapes.add_shape(1, 0, 0, W, H); bg.fill.solid(); bg.fill.fore_color.rgb = DARK; bg.line.fill.background()
            textbox(s, Inches(1), Inches(2.6), Inches(11.3), Inches(1.5), [title], size=44 if kind == 'title' else 40, color=RGBColor(255, 255, 255), bold=True)
            if body:
                textbox(s, Inches(1), Inches(4.2), Inches(11.3), Inches(1), body, size=22, color=RGBColor(0xD9, 0xD4, 0xCE))
        else:
            textbox(s, Inches(0.7), Inches(0.45), Inches(12), Inches(1), [title], size=32, bold=True)
            ln = s.shapes.add_shape(1, Inches(0.7), Inches(1.35), Inches(1.2), Emu(45720)); ln.fill.solid(); ln.fill.fore_color.rgb = ACCENT; ln.line.fill.background()
            if img and os.path.exists(img):
                iw, ih = Image.open(img).size
                box_w, box_h = Inches(5.2), Inches(5.4)
                scale = min(box_w / iw, box_h / ih); pw, ph = int(iw * scale), int(ih * scale)
                s.shapes.add_picture(img, W - Inches(0.7) - pw, Inches(1.7), pw, ph)
                textbox(s, Inches(0.7), Inches(1.7), Inches(6.6), Inches(5.4), body, size=18)
            else:
                textbox(s, Inches(0.7), Inches(1.7), Inches(12), Inches(5.4), body, size=20)
            textbox(s, Inches(0.7), Inches(6.95), Inches(6), Inches(0.4), [f'{i}'], size=10, color=MUTED)
        notes(s, note)
    prs.save(out); print('saved', out, len(PAGES), 'pages')

def write_copy():
    """把 PAGES 回寫進逐頁稿：畫面欄改為內文／圖欄。"""
    p = os.path.join(ROOT, 'drafts', '08-week2-slide-copy.md'); s = open(p, encoding='utf-8').read()
    import re
    heads = [m for m in re.finditer(r'^### (\d\d)｜(.*)$', s, re.M)]
    assert len(heads) == len(PAGES), (len(heads), len(PAGES))
    out = []; pos = 0
    for k, m in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else s.find('\n## ', m.end())
        block = s[m.start():end]
        title, kind, body, img, note = PAGES[k]
        lines = []
        for item in body:
            if isinstance(item, tuple):
                lines.append(item[0] + '：' + '；'.join(item[1]))
            else:
                lines.append(item)
        inner = '- 內文：' + ('／'.join(lines) if lines else '無，只有段名') + '\n'
        if img:
            inner += '- 圖：`' + os.path.relpath(img, ROOT) + '`\n'
        block = re.sub(r'^- 畫面：.*\n', inner, block, count=1, flags=re.M)
        out.append(s[pos:m.start()] + block); pos = end
    out.append(s[pos:]); s = ''.join(out)
    open(p, 'w', encoding='utf-8').write(s); print('copy updated')

if __name__ == '__main__':
    build(os.path.join(ROOT, 'slides', 'week2-agent-knowledge-work-v9.pptx'))
    if '--copy' in sys.argv:
        write_copy()
