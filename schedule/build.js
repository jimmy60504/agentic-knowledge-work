// 上課課程表：讀 schedule.tsv，產生 Word 檔（版面依紙本課程表），附課程網站的連結與 QR code。
// 用法見 schedule/build.sh。
const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,AlignmentType,BorderStyle,ShadingType,VerticalAlign,Footer,HeightRule,ImageRun,ExternalHyperlink}=require('docx');
const URL='https://jimmy60504.github.io/agentic-knowledge-work/';
const OUT=process.argv[2], QR=process.argv[3];
const NAVY='1F3864', GREY='D9DCE3', MUTED='8A8F99', FONT='Microsoft JhengHei';
const path=require('path');
const HERE=__dirname;
const rows=fs.readFileSync(path.join(HERE,'schedule.tsv'),'utf8').trim().split('\n').slice(1).map(l=>{const c=l.split('\t');while(c.length<4)c.push('');return c;});
const W=[1700,2300,2300,3338]; // sum 9638 (A4 text width w/ 1.0in margins ~9638)
const none={style:BorderStyle.NONE,size:0,color:'FFFFFF'};
const line={style:BorderStyle.SINGLE,size:4,color:GREY};
const cell=(t,i,head)=>new TableCell({width:{size:W[i],type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,
  shading: head?{type:ShadingType.CLEAR,color:'auto',fill:NAVY}:undefined,
  margins:{top:90,bottom:90,left:100,right:100},
  borders:{top:none,left:head?none:line,right:head?none:line,bottom:head?none:line},
  children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:t,font:FONT,size:head?24:24,bold:head||i===0,color:head?'FFFFFF':'222222'})]})]});
const table=new Table({width:{size:9638,type:WidthType.DXA},columnWidths:W,
  borders:{top:none,bottom:none,left:none,right:none,insideHorizontal:line,insideVertical:line},
  rows:[new TableRow({tableHeader:true,height:{value:540,rule:HeightRule.ATLEAST},children:['日期','時間','地點','課名'].map((t,i)=>cell(t,i,true))}),
        ...rows.map(r=>new TableRow({height:{value:540,rule:HeightRule.ATLEAST},children:r.map((t,i)=>cell(t,i,false))}))]});
const doc=new Document({styles:{default:{document:{run:{font:FONT}}}},
 sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1300,bottom:1000,left:1134,right:1134}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:'COURSE SCHEDULE',font:'Calibri',size:16,color:'B0B4BC',characterSpacing:40})]})]})},
  children:[
   new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:200},children:[new TextRun({text:'上課課程表',font:FONT,size:52,bold:true,color:NAVY})]}),
   new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:240},children:[new TextRun({text:'2026 年 9–12 月',font:FONT,size:24,color:'333333'})]}),
   new Paragraph({spacing:{after:0},border:{bottom:{style:BorderStyle.SINGLE,size:18,color:NAVY,space:1}},children:[]}),
   table,
   new Paragraph({spacing:{before:240},children:[new TextRun({text:'備註：課名可於確認後補填。',font:FONT,size:18,color:MUTED})]}),
   new Table({width:{size:9638,type:WidthType.DXA},columnWidths:[1900,7738],
     borders:{top:none,bottom:none,left:none,right:none,insideHorizontal:none,insideVertical:none},
     rows:[new TableRow({children:[
       new TableCell({width:{size:1900,type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,borders:{top:none,bottom:none,left:none,right:none},
         margins:{top:200,bottom:0,left:0,right:120},
         children:[new Paragraph({children:[new ImageRun({type:'png',data:fs.readFileSync(QR),transformation:{width:100,height:100}})]})]}),
       new TableCell({width:{size:7738,type:WidthType.DXA},verticalAlign:VerticalAlign.CENTER,borders:{top:none,bottom:none,left:none,right:none},
         margins:{top:200,bottom:0,left:120,right:0},
         children:[
           new Paragraph({spacing:{after:80},children:[new TextRun({text:'課程網站',font:FONT,size:22,bold:true,color:NAVY})]}),
           new Paragraph({spacing:{after:80},children:[new ExternalHyperlink({link:URL,children:[new TextRun({text:URL,font:'Calibri',size:20,color:'2F5597',underline:{}})]})]}),
           new Paragraph({children:[new TextRun({text:'掃描 QR code 開啟各週的教材與投影片。',font:FONT,size:18,color:MUTED})]}),
         ]})]})]}),
  ]}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync(OUT,b));
