import re, glob, json
out=[]
for f in sorted(glob.glob('/data/atc/study/atc-study-aws_certified_cloud_practitioner/guide/*/*-check.md')):
    text=open(f).read()
    text=re.sub(r'<details>.*?</details>','',text,flags=re.S)
    for m in re.finditer(r'^\*\*([AB]\d+)\.\*\*(.*?)(?=^\*\*[AB]\d+\.\*\*|^## )',text,flags=re.S|re.M):
        out.append({'src':f.split('/guide/')[1],'id':m.group(1),'text':' '.join(m.group(2).split())})
json.dump(out,open('check-items.json','w'),indent=0)
print(len(out))
