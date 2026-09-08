from reportlab.pdfgen.canvas import Canvas
from pathlib import Path
from pypdf import PdfReader
import hashlib
root=Path.cwd()
out=root/'drafts/week2-v10/week2-agent-knowledge-work-v10-blue-preview.pdf'
c=Canvas(str(out),pagesize=(960,540))
c.setTitle('Week 2 - Agent Knowledge Work - Blue Visual Draft')
for i in range(1,29):
 c.drawImage(str(root/f'tmp/week2-v10-build/slide-{i:02}.png'),0,0,width=960,height=540)
 c.showPage()
c.save()
assert len(PdfReader(str(out)).pages)==28
candidate=root/'tmp/week2-v10-build/candidate.pptx'
final=root/'drafts/week2-v10/week2-agent-knowledge-work-v10-blue-review.pptx'
assert hashlib.sha256(candidate.read_bytes()).digest()==hashlib.sha256(final.read_bytes()).digest()
print('28-page PDF created; rendered PPTX and final PPTX are byte-identical.')
