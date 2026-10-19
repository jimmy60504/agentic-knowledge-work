#!/bin/bash
# 重新產生上課課程表：Word（教育訓練資料夾外層）、PDF，並複製到網站提供下載。
# 用法：bash schedule/build.sh（在課程 repo 根目錄執行；需要 node 與 Microsoft Word）
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUTDIR="$(cd "$REPO/.." && pwd)"          # 氣象署計畫/115/教育訓練/
DOCX="$OUTDIR/上課課程表.docx"; PDF="$OUTDIR/上課課程表.pdf"
WORK="$(mktemp -d)"                          # npm 套件裝在暫存目錄，不進 repo
(cd "$WORK" && npm install --silent docx@9 qrcode@1 >/dev/null)
NODE_PATH="$WORK/node_modules" node -e "require('qrcode').toFile('$WORK/qr.png','https://jimmy60504.github.io/agentic-knowledge-work/',{width:600,margin:1,color:{dark:'#1F3864',light:'#FFFFFF'}},e=>{if(e)throw e})"
NODE_PATH="$WORK/node_modules" node "$REPO/schedule/build.js" "$DOCX" "$WORK/qr.png"
# Word 會沿用已開啟的同名檔，先複製成新檔名再匯出 PDF；PDF 直接覆蓋，不先刪除
TMPDOC="$OUTDIR/課程表-export-$(date +%H%M%S).docx"; cat "$DOCX" > "$TMPDOC"
osascript -e "with timeout of 300 seconds
tell application \"Microsoft Word\"
open POSIX file \"$TMPDOC\"
delay 2
set d to active document
save as d file name (POSIX file \"$PDF\" as string) file format format PDF
close d saving no
end tell
end timeout"
rm -f "$TMPDOC"
cp "$PDF" "$REPO/assets/site/course-schedule.pdf"
echo "已更新：$DOCX、$PDF、assets/site/course-schedule.pdf（頁數：$(pdfinfo "$PDF" | awk '/Pages/{print $2}')）"
