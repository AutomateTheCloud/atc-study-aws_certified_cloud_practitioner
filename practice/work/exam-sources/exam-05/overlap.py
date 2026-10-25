import json, re, glob, math, collections, yaml
G='/data/atc/study/atc-study-aws_certified_cloud_practitioner/'
corpus=[]
for f in glob.glob(G+'practice/items/*.yaml'):
    for q in yaml.safe_load(open(f)).get('questions',[]):
        corpus.append(('practice:'+q['id'], q['prompt']['text']+' '+' '.join(c['text'] for c in q['choices'])))
for c in json.load(open('check-items.json')): corpus.append(('check:'+c['src']+':'+c['id'], c['text']))
for f in glob.glob(G+'guide/*/*.md'):
    if '90-exam-prep/05' in f: continue
    t=open(f).read()
    if '90-exam-prep' in f:
        t=re.sub(r'<details>.*?</details>','',t,flags=re.S)
        for m in re.finditer(r'^\*\*(\d+)\.\*\*(.*?)(?=^\*\*\d+\.\*\*|^## )',t,flags=re.S|re.M):
            corpus.append(('prep:'+f.split('/')[-1]+':'+m.group(1),m.group(2)))
        continue
    for m in re.finditer(r'^> \*\*(Check|Your turn):\*\*(.*?)(?=^\s*$\n(?!>))',t,flags=re.S|re.M):
        corpus.append(('lesson:'+f.split('guide/')[1],m.group(2)))
tok=lambda s:[w for w in re.findall(r'[a-z0-9]+',s.lower()) if len(w)>2]
mine=[json.loads(l) for l in open('candidates.jsonl')]
docs=[tok(t) for _,t in corpus]
df=collections.Counter(w for d in docs for w in set(d))
N=len(docs)
def vec(ws):
    c=collections.Counter(ws); v={w:(1+math.log(n))*math.log(N/(1+df.get(w,0))) for w,n in c.items()}
    nrm=math.sqrt(sum(x*x for x in v.values())) or 1; return {w:x/nrm for w,x in v.items()}
V=[vec(d) for d in docs]
print('corpus',N, collections.Counter(k.split(':')[0] for k,_ in corpus))
for m in mine:
    v=vec(tok(m['question']+' '+' '.join(m['options'].values())))
    best=sorted(((sum(v.get(w,0)*x for w,x in V[i].items()),i) for i in range(N)),reverse=True)[:2]
    s,i=best[0]
    if s>0.33: print(f"{s:.2f} {m['id']} <-> {corpus[i][0]} :: {' '.join(corpus[i][1].split())[:160]}")
