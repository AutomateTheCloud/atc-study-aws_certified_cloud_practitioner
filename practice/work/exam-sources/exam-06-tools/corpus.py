# Build a corpus of existing question-like text from the guide and practice bundle,
# and score candidate items against it (TF-IDF cosine).
import sys, re, json, glob, math, os
from collections import Counter
REPO='/data/atc/study/atc-study-aws_certified_cloud_practitioner'
SELF=os.path.join(REPO,'guide/90-exam-prep/06-practice-exam-2.md')
def md_items(path):
    txt=open(path).read()
    txt=re.sub(r'<details>.*?</details>','',txt,flags=re.S)
    paras=re.split(r'\n\s*\n',txt)
    out=[]
    i=0
    while i<len(paras):
        p=paras[i]
        if ('?' in p or '(Select' in p) and len(p)>60 and not p.lstrip().startswith('|'):
            s=p
            if i+1<len(paras) and re.match(r'\s*(>\s*)?[-*]\s',paras[i+1]):
                s+=' '+paras[i+1]
            out.append(s)
        i+=1
    return out
def yaml_items(path):
    import yaml
    d=yaml.safe_load(open(path))
    out=[]
    for q in d.get('questions',[]) or []:
        t=q.get('prompt',{}).get('text','')
        for c in q.get('choices',[]) or []:
            t+=' '+str(c.get('text',''))
        out.append(t)
    return out
def corpus():
    docs=[]
    for f in sorted(glob.glob(REPO+'/guide/*/*.md')):
        if os.path.abspath(f)==SELF or '/99-reference/' in f: continue
        for s in md_items(f): docs.append((f.replace(REPO+'/',''),s))
    for f in sorted(glob.glob(REPO+'/practice/items/*.yaml')):
        for s in yaml_items(f): docs.append((f.replace(REPO+'/',''),s))
    return docs
STOP=set('a an the of to and or in on for is are be it its this that with which what by from as at their they them his her she he you your we our not no do does can will would should has have had was were than then into one two each more most only also but if when who whom'.split())
def toks(s):
    w=re.findall(r'[a-z0-9]+',s.lower())
    w=[x for x in w if x not in STOP and len(x)>2]
    return w+[a+'_'+b for a,b in zip(w,w[1:])]
def main():
    cands=[json.loads(l) for l in open(sys.argv[1])]
    docs=corpus()
    dt=[Counter(toks(s)) for _,s in docs]
    df=Counter()
    for c in dt: df.update(set(c))
    N=len(dt)
    def vec(c):
        v={t:n*math.log((N+1)/(df.get(t,0)+1)) for t,n in c.items()}
        nrm=math.sqrt(sum(x*x for x in v.values())) or 1
        return {t:x/nrm for t,x in v.items()}
    dv=[vec(c) for c in dt]
    thr=float(sys.argv[2]) if len(sys.argv)>2 else 0.25
    for c in cands:
        text=c['question']+' '+' '.join(c['options'].values())
        v=vec(Counter(toks(text)))
        sims=sorted(((sum(x*d.get(t,0) for t,x in v.items()),i) for i,d in enumerate(dv)),reverse=True)[:2]
        flag='HIGH' if sims[0][0]>=thr else 'ok'
        print(f"{c['id']}\t{flag}\t"+'\t'.join(f"{s:.2f} {docs[i][0]}" for s,i in sims))
        if flag=='HIGH' and '--show' in sys.argv:
            print('   >>', docs[sims[0][1]][1][:400].replace('\n',' '))
print_count = '--count' in sys.argv
if print_count:
    print(len(corpus()))
else:
    main()
