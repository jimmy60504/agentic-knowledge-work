#!/bin/zsh
# mermaid-cli 出 SVG → 改字型 → 系統 WebKit（qlmanage）轉 PNG → 裁白邊。
# dagre 的左右走向由圖的結構決定，調不動時可設 MIRROR=1 左右鏡射（文字會翻回）。
set -e
cd "$(dirname "$0")"
MIRROR="${MIRROR:-0}"   # 1 = 左右鏡射（dagre 排成往左時用）
for name in three-loops three-loops-h1 three-loops-h2 three-loops-h3; do
  out="${name/three-loops/three-loops-mermaid}"
  npx -y @mermaid-js/mermaid-cli -i "$name.mmd" -o "$out.svg" -b white -p puppeteer.json >/dev/null
  python3 - "$out" "$MIRROR" <<'PY'
import re, sys
out=sys.argv[1]; mirror=sys.argv[2]=="1"
s=open(out+'.svg',encoding='utf-8').read()
m=re.search(r'viewBox="([\d\.\-\s]+)"', s); vb=m.group(1).split(); x0=float(vb[0]); w=float(vb[2]); h=float(vb[3]); scale=3
# 文字翻回：每個 <text> 加 translate(2x,0) scale(-1,1)
def fix_text(m):
    tag=m.group(0)
    xm=re.search(r'\sx="([\d\.\-]+)"', tag); x=float(xm.group(1)) if xm else 0.0
    tm=re.search(r'\stransform="([^"]*)"', tag)
    extra=f'translate({2*x},0) scale(-1,1)'
    if tm:
        return tag.replace(tm.group(0), f' transform="{tm.group(1)} {extra}"')
    return tag[:-1]+f' transform="{extra}">'
# 節點標籤的 foreignObject 寬度是用量測字型算的，換成 PingFang 後英文較寬會被切字：加寬並保持置中
def widen_fo(m):
    st=m.group(1); tx=float(m.group(2)); ty=float(m.group(3)); W=float(m.group(4)); H=m.group(5)
    W2=W*1.12+8
    return f'<g class="label" style="{st}" transform="translate({tx-(W2-W)/2}, {ty})"><rect/><foreignObject width="{W2}" height="{H}" style="overflow:visible">'
s=re.sub(r'<g class="label" style="([^"]*)" transform="translate\(([\d\.\-]+), ([\d\.\-]+)\)"><rect/><foreignObject width="([\d\.]+)" height="([\d\.]+)">', widen_fo, s)
s=s.replace('display: table-cell;', 'display: block; width: 100%;')  # 加寬後仍置中
if mirror:
    s=re.sub(r'<text\b[^>]*>', fix_text, s)
# foreignObject 的節點標籤：把 <g class="label" transform="translate(tx,ty)"> 改成 translate(tx+W,ty) scale(-1,1)
def fix_fo(m):
    st=m.group(1); tx=float(m.group(2)); ty=float(m.group(3)); W=float(m.group(4))
    return f'<g class="label" style="{st}" transform="translate({tx+W}, {ty}) scale(-1,1)"><rect/><foreignObject width="{m.group(4)}"'
if mirror:
    s=re.sub(r'<g class="label" style="([^"]*)" transform="translate\(([\d\.\-]+), ([\d\.\-]+)\)"><rect/><foreignObject width="([\d\.]+)"', fix_fo, s)  # 加寬後仍匹配
    s=re.sub(r'(<svg[^>]*>)', r'\1<g transform="translate(%f,0) scale(-1,1)">'%(2*x0+w), s, count=1)
    s=s.replace('</svg>','</g></svg>')
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
