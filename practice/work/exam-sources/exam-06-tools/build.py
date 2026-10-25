# Build guide/90-exam-prep/06-practice-exam-2.md, candidates.jsonl and a blind copy.
import sys, re, json, os, collections
SCR = '/tmp/claude-1000/-data-atc-study-study-aws-certified-cloud-practitioner/90d7019c-4727-40dc-b5e8-2d3498ef2995/scratchpad/exam-06'
REPO = '/data/atc/study/atc-study-aws_certified_cloud_practitioner'
sys.path.insert(0, SCR)
from items import ITEMS

def slug(h):
    s = h.strip().lower()
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    return s.replace(' ', '-')

errors = []
def link(f, h):
    path = os.path.join(REPO, 'guide', f)
    heads = [l.lstrip('#').strip() for l in open(path) if re.match(r'#{2,3} ', l)]
    if h not in heads:
        errors.append(f'missing heading {f} :: {h}')
    return f'[{h}](../{f}#{slug(h)})'

assert len(ITEMS) == 65, len(ITEMS)
PLACE = {10:'A',39:'C',35:'C',15:'C',2:'D',11:'D',16:'D',21:'D',56:'D',58:'C',9:'D',30:'D',50:'D',37:'C',
         18:'BD',23:'BE',26:'CE',27:'BD',32:'AE',47:'BE',48:'BC',52:'CE',63:'DE'}
for k, it in enumerate(ITEMS, 1):
    if k not in PLACE: continue
    opts = it['options']; L = 'ABCDE'[:len(opts)]
    right = [opts[L.index(a)] for a in it['answer']]
    wrong = [o for j, o in enumerate(opts) if L[j] not in it['answer']]
    tgt = PLACE[k]; assert len(tgt) == len(it['answer'])
    new = []
    for j in range(len(opts)):
        new.append(right.pop(0) if L[j] in tgt else wrong.pop(0))
    it['options'] = new; it['answer'] = tgt
dom = lambda t: t.split('.')[0]
cnt = collections.Counter(dom(i['task']) for i in ITEMS)
tcnt = collections.Counter(i['task'] for i in ITEMS)
multi = sum(1 for i in ITEMS if len(i['answer']) > 1)
pos = collections.Counter(i['answer'] for i in ITEMS if len(i['answer']) == 1)
mpos = collections.Counter(i['answer'] for i in ITEMS if len(i['answer']) > 1)
for i in ITEMS:
    n = len(i['options'])
    if len(i['answer']) == 1: assert n == 4, i['stem'][:40]
    else: assert n == 5 and '(Select TWO.)' in i['stem'], i['stem'][:40]
print('domains', dict(cnt), 'multi', multi, 'single positions', dict(pos), 'multi', dict(mpos))
print('tasks', dict(sorted(tcnt.items())))

TASKURL = {'1': 'domain1', '2': 'domain2', '3': 'domain3', '4': 'domain4'}
def taskref(t):
    d = dom(t)
    return f'[{t}](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-{TASKURL[d]}.html#cloud-practitioner-02-task{t})'

TITLE = 'Practice exam 2'
alltasks = sorted(tcnt, key=lambda t: [int(x) for x in t.split('.')])
fm = f'''---
type: check
id: clf-90-06
title: "{TITLE}"
tasks: [{", ".join('"%s"' % t for t in alltasks)}]
objectives: []
reader: "Adult studying alone who has finished Modules 02 to 13 and wants a full timed rehearsal; 90 minutes, then about 45 minutes to score and review"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00, clf-10-00, clf-11-00, clf-12-00, clf-13-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
---
'''

intro = '''# Practice exam 2: a second full rehearsal in exam format

This is a second complete practice exam: 65 questions in 90 minutes, spread across the four domains in the same proportions as the real CLF-C02 exam, and across all 19 task statements. None of its questions appears anywhere else in this guide, so it measures what you can do with situations you haven't seen.

**For:** an adult studying alone who has finished Modules 02 to 13 and wants a timed rehearsal before booking or sitting the exam. **Time:** 90 minutes for the questions, then about 45 minutes to score them and read the explanations.

## How to take it

- **Set a timer for 90 minutes** and take the whole exam in one sitting, as you will on the day. That's a little under a minute and a half per question.
- **Closed book.** No lessons, notes, AWS pages or search. Answer from what you know.
- **Answer every question.** On the real exam a blank counts as wrong and a wrong guess costs nothing more, so guess when you must and flag the question to come back to.
- **Don't open the answer key until you've finished** all 65. Looking early turns the rest of the exam into practice, not a measure.
- **Score it:** one point per question. A "(Select TWO.)" question scores only if you chose both correct answers and nothing else, as on the exam. Then count your points per domain and use the [score table](#score-by-domain) to find what to do next.
- **Use it once as a measure.** Your first attempt is the readiness signal. After you've read the key, a retake shows that you remember these questions, not that you're ready for new ones. Take [Practice exam 1](05-practice-exam-1.md) on a different day for a second measure.

The real exam has 65 questions too, but 15 of them are unscored trials you can't identify, and it reports a scaled score. Here every question counts and you get a raw count, so the two aren't directly comparable. The questions use the exam's names for services; where AWS has renamed something, the explanation gives today's name.

## The questions

'''

def letters(n): return 'ABCDE'[:n]

q = []
for k, it in enumerate(ITEMS, 1):
    q.append(f'**{k}.** {it["stem"]}\n')
    for L, o in zip(letters(len(it['options'])), it['options']):
        q.append(f'- **{L}.** {o}')
    q.append('')
questions = '\n'.join(q)

key = ['## Answer key', '', 'Score yourself before you read this. Each entry gives the answer, the task statement it tests, why the answer is right and why the most tempting wrong choice is wrong, and the section of the guide that teaches it.', '', '<details><summary>Answer key</summary>', '']
for k, it in enumerate(ITEMS, 1):
    ans = ' and '.join(it['answer'])
    links = '; '.join(link(f, h) for f, h in it['links'])
    key.append(f'**{k}. {ans}.** Task {taskref(it["task"])}. {it["expl"]} *Reread:* {links}.')
    key.append('')
key.append('</details>')
key.append('')
keytxt = '\n'.join(key)

def band(n):
    lo = -(-6 * n // 10)  # ceil(0.6n)
    hi = -(-8 * n // 10)  # ceil(0.8n)
    return lo, hi
rows = []
rng = lambda a, b: str(a) if a == b else f'{a} to {b}'
names = {'1': ('Domain 1: Cloud Concepts', '24%'), '2': ('Domain 2: Security and Compliance', '30%'),
         '3': ('Domain 3: Cloud Technology and Services', '34%'), '4': ('Domain 4: Billing, Pricing, and Support', '12%')}
for d in '1234':
    n = cnt[d]; lo, hi = band(n)
    qs = [str(k) for k, it in enumerate(ITEMS, 1) if dom(it['task']) == d]
    rows.append(f'| {names[d][0]} | {names[d][1]} | {n} | {rng(0, lo-1)} | {rng(lo, hi-1)} | {rng(hi, n)} |')
lo, hi = band(65)
rows.append(f'| **Whole exam** | 100% | 65 | 0 to {lo-1} | {lo} to {hi-1} | {hi} to 65 |')
qmap = []
for d in '1234':
    qs = ', '.join(str(k) for k, it in enumerate(ITEMS, 1) if dom(it['task']) == d)
    qmap.append(f'- **{names[d][0]}:** questions {qs}.')

score = f'''## Score by domain

Count your correct answers in each domain. The questions belong to these domains:

{chr(10).join(qmap)}

Then find your count in the table. The bands are percentages of each domain's questions: below 60%, from 60% to 79%, and 80% or more.

| Domain | Share of the exam | Questions here | Restudy the domain (below 60%) | Review the linked sections (60% to 79%) | Ready on this domain (80% or more) |
|---|---|---|---|---|---|
{chr(10).join(rows)}

What each band means:

- **Restudy the domain:** go back through the modules behind it (the [blueprint map](../99-reference/06-blueprint-map.md) lists them by task statement), redo their mastery checks, then come back to Practice exam 1 if you haven't taken it.
- **Review the linked sections:** for every question you missed, reread the section its answer links to, and write one sentence on why the right answer beats the one you chose.
- **Ready on this domain:** read the explanations of anything you missed, then spend your study time on your weakest domain.

Read your result as a range, not a point. A domain with few questions moves a whole band with one answer: Domain 4 has only 7 questions here, so a single miss or lucky guess changes its percentage by about 14 points. Two practice exams on different days, each taken once and unseen, give a steadier picture than one.

> **Note:** a practice score is not a prediction of your exam score. These are our questions, written from AWS's public exam guide; they aren't AWS's, they aren't scaled the way the exam is, and real exam forms differ from each other. Use the result to decide what to study next, not whether you'll pass.

---

"{TITLE}" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
'''

page = fm + '\n' + intro + questions + '\n' + keytxt + '\n' + score
if errors:
    print('\n'.join(errors)); sys.exit(1)
open(os.path.join(REPO, 'guide/90-exam-prep/06-practice-exam-2.md'), 'w').write(page)
blind = '# Practice exam (answers removed)\n\n' + questions
open(os.path.join(SCR, 'blind.md'), 'w').write(blind)
with open(os.path.join(SCR, 'candidates.jsonl'), 'w') as f:
    for k, it in enumerate(ITEMS, 1):
        f.write(json.dumps({'id': f'pe2-{k:02d}', 'question': it['stem'],
                            'options': dict(zip(letters(len(it['options'])), it['options'])),
                            'answer': list(it['answer'])}) + '\n')
with open(os.path.join(SCR, 'answers.txt'), 'w') as f:
    for k, it in enumerate(ITEMS, 1): f.write(f'{k} {it["answer"]}\n')
print('written')
