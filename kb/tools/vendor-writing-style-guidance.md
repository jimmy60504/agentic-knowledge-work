# 模型廠商自己出的語氣修正指引，與 AI 寫作特徵清單

查閱日期：2026-09-08。用途：第二週第三圈「文字與語氣」面向的判準來源；也回答「OpenAI 與 Anthropic 是否各出了針對自家模型的語氣修正」。

## 來源

- OpenAI，GPT-6 Astra 模型指南「Personality and writing style」一節，[developers.openai.com](https://developers.openai.com/api/docs/guides/latest-model)，2026-09-05 發布；報導見 [The Decoder](https://the-decoder.com/openai-shares-prompting-tips-for-gpt-6-astra-including-a-blocklist-of-slop-words/)。
- Anthropic，「Prompting Claude Fable 5.1」的「Writing density」一節，[platform.claude.com](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)。
- 維基百科 WikiProject AI Cleanup，[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)。
- 本 repo 既有：[[chinese-copy-style]]（`skills/`）、[[ghost-deck-from-own-words]]（`skills/`）。

## 重點

**OpenAI 的做法是給禁用清單加正面規則。** 要模型刪掉的固定用語包括 "Bottom Line:"、delve、foster、leverage、"it's worth noting"、importantly、"Question? Answer." 這種自問自答；不要用 "In short:" 這類收尾總結句；不要用「X, not Y」的對比句型；不要自造連字號複合詞。正面規則是：段落清楚簡短、一段一個主旨；用熟悉的字、具體例子、精確的動詞；主動語態、直接陳述。

**Anthropic 的做法是定義一個反模式，讓模型自己對照。** 反模式叫 mannered prose，用比喻與修飾代替直述：不說 "a parameter worth varying" 而說 "a dial worth turning"；不說 "this point still matters" 而說 "this point earns its keep"。文件指出這些句子是為了展示作者而不是傳達意思，讀者看得出來，而且比喻會帶進作者沒選的含意。修法是「說你要說的，有直述可用就用直述」。短版指令是 "Please remove all mannered prose."。同頁另一節說明格式：需要時才用條列與粗體，對話與個人交流用平鋪的散文。

**維基百科的清單分八類。** 內容（過度強調重要性、表面分析、宣傳語氣、模糊歸屬）、用語與文法（過用詞彙、迴避簡單的是非句）、風格（過多粗體、奇怪的標題結構、破折號過用）、對使用者說話的痕跡、標記、引用、編輯摘要、其他。頁面強調這些只是跡象，不是問題本身。

## 洞見

1. **三份東西是同一件事的三個層次。** 維基的清單是「症狀」，OpenAI 的禁用清單是「症狀對應的規則」，Anthropic 的反模式是「症狀背後的原因」，即為了表演而寫。教學上先給原因再給清單，學員才會自己判斷，而不是拿清單逐字比對。
2. **這正是第三圈「文字與語氣」面向的判準。** 自己沒有語氣判斷力的人，可以先拿這三份當判準交給 agent；有自己規則的人拿自己的，例如本 repo 的文案語氣規則。兩者都用得上「原話優先」：自己說過的句子沒有 AI 語氣的問題。
3. **兩家指引都是給自家模型的，但規則可互通。** OpenAI 的禁用詞多為英文；中文場景要自己補，本 repo 的修改對照表就是中文版的累積。
4. **廠商自己承認模型有固定腔調，並教使用者怎麼壓掉。** 這件事本身可以講給學員聽：語氣不是模型不能改，是沒有給判準。

## 課程用途（候選，未定）

- 第二週練習第六步「文字與語氣」的判準來源；draft 已引用維基頁，可補這兩份廠商指引。
- 中文版的 AI 語氣特徵清單，可從 `skills/chinese-copy-style.md` 的修改對照表抽出，另成一節。
- 後續「表達」主題：mannered prose 的定義可直接當講稿例子，與課程「不用金句口號」的規則同源。
