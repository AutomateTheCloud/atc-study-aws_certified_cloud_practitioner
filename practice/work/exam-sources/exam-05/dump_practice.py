import sys, yaml, glob, collections
by = collections.defaultdict(list)
for f in sorted(glob.glob('/data/atc/study/atc-study-aws_certified_cloud_practitioner/practice/items/*.yaml')):
    d = yaml.safe_load(open(f))
    for q in d.get('questions', []):
        t = q.get('task')
        p = ' '.join(q['prompt']['text'].split())
        key = [c['text'] for c in q['choices'] if c['id'] in q['correct_answers']]
        by[t].append(f"{q['id']}: {p} => {key}")
for t in sorted(by):
    print('##', t, len(by[t]))
    for l in by[t]: print('-', l)
