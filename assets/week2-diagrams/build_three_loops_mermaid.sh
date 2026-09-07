#!/bin/zsh
# 用 mermaid-cli 出 SVG，再以系統 WebKit（qlmanage）轉 PNG，字型才會是 PingFang。
# 用法：zsh assets/week2-diagrams/build_three_loops_mermaid.sh
set -e
cd "$(dirname "$0")"
for name in three-loops three-loops-h1 three-loops-h2 three-loops-h3; do
  out="${name/three-loops/three-loops-mermaid}"
  npx -y @mermaid-js/mermaid-cli -i "$name.mmd" -o "$out.svg" -b white -p puppeteer.json >/dev/null
  python3 - "$out" <<'PY'
import re, sys
out=sys.argv[1]
s=open(out+'.svg',encoding='utf-8').read()
m=re.search(r'viewBox="([\d\.\-\s]+)"', s); vb=m.group(1).split(); w=float(vb[2]); h=float(vb[3]); scale=3
s=re.sub(r'<svg([^>]*?)\swidth="[^"]*"', r'<svg\1 width="%d"'%int(w*scale), s, count=1)
s=re.sub(r'<svg([^>]*?)\sheight="[^"]*"', r'<svg\1 height="%d"'%int(h*scale), s, count=1)
s=re.sub(r'font-family:[^;"}]*', 'font-family:"PingFang TC","Heiti TC",sans-serif', s)
s=re.sub(r'(<svg[^>]*>)', r'\1<style>*{font-family:"PingFang TC","Heiti TC",sans-serif !important;}</style>', s, count=1)
open(out+'-big.svg','w',encoding='utf-8').write(s)
PY
  rm -f "$out-big.svg.png"
  qlmanage -t -s 4000 -o . "$out-big.svg" >/dev/null 2>&1
  python3 - "$out" <<'PY'
import sys, os
from PIL import Image, ImageChops
out=sys.argv[1]
im=Image.open(out+'-big.svg.png').convert('RGB')
bg=Image.new('RGB', im.size, (255,255,255)); x0,y0,x1,y1=ImageChops.difference(im,bg).getbbox(); pad=40
im.crop((max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad))).save(out+'.png')
os.remove(out+'-big.svg.png'); os.remove(out+'-big.svg')
print(out, Image.open(out+'.png').size)
PY
done
