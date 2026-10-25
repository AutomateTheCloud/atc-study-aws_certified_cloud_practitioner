"""Build a corpus of existing question-like chunks from the guide and practice bundle,
and compare candidate items against it with a simple TF-IDF cosine."""
import json, math, re, sys, glob, os
from collections import Counter

REPO = "/data/atc/study/atc-study-aws_certified_cloud_practitioner"
HERE = os.path.dirname(os.path.abspath(__file__))
STOP = set("""a an the of to and or in on for is are be by with that this which what from as at it its
into your you their they them can than then not no do does will would should could must may has have
had was were been being one two three which who whom how when where why all any each other more most
company team needs need wants want select best describes statement true following option choice aws amazon""".split())


def tokens(text):
    return [w for w in re.findall(r"[a-z0-9][a-z0-9\-]+", text.lower()) if w not in STOP and len(w) > 2]


def guide_chunks():
    out = []
    for path in sorted(glob.glob(f"{REPO}/guide/*/*.md")):
        if "/90-exam-prep/" in path and os.path.basename(path)[:2] in ("01", "02", "03", "04"):
            continue
        text = open(path).read()
        text = re.sub(r"<details>.*?</details>", "", text, flags=re.S)
        lines = text.splitlines()
        start = re.compile(r"^(\*\*[A-Z]?\d+\.\*\*|\s*\d+\.\s+\*\*|> \*\*Your turn|> \*\*Check|\*\*Q\d)")
        cur, cur_start = [], None
        for i, ln in enumerate(lines):
            if start.match(ln) or ln.startswith("#"):
                if cur:
                    out.append((f"{os.path.relpath(path, REPO)}:{cur_start}", " ".join(cur)))
                cur, cur_start = ([ln], i + 1) if not ln.startswith("#") else ([], None)
            elif cur:
                cur.append(ln)
                if len(cur) > 14:
                    out.append((f"{os.path.relpath(path, REPO)}:{cur_start}", " ".join(cur)))
                    cur, cur_start = [], None
        if cur:
            out.append((f"{os.path.relpath(path, REPO)}:{cur_start}", " ".join(cur)))
    return out


def practice_chunks():
    import yaml
    out = []
    for path in sorted(glob.glob(f"{REPO}/practice/items/*.yaml")):
        data = yaml.safe_load(open(path))
        for q in data.get("questions", []) or []:
            t = q.get("prompt", {}).get("text", "")
            t += " " + " ".join(c.get("text", "") for c in q.get("choices", []) or [])
            out.append((f"practice:{q.get('id')}", t))
    return out


def main():
    cand_path = sys.argv[1]
    thresh = float(sys.argv[2]) if len(sys.argv) > 2 else 0.30
    corpus = guide_chunks() + practice_chunks()
    cands = [json.loads(l) for l in open(cand_path) if l.strip()]
    docs = [tokens(t) for _, t in corpus]
    ctoks = [tokens(c["question"] + " " + " ".join(c["options"].values())) for c in cands]
    df = Counter()
    for d in docs + ctoks:
        df.update(set(d))
    N = len(docs) + len(ctoks)
    idf = {w: math.log(N / (1 + n)) + 1 for w, n in df.items()}

    def vec(d):
        c = Counter(d)
        v = {w: (1 + math.log(n)) * idf[w] for w, n in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        return {w: x / norm for w, x in v.items()}

    dv = [vec(d) for d in docs]
    cv = [vec(d) for d in ctoks]
    # also compare candidates with each other
    for i, c in enumerate(cands):
        scores = []
        for j, d in enumerate(dv):
            s = sum(x * d.get(w, 0) for w, x in cv[i].items())
            scores.append((s, corpus[j][0]))
        for k, o in enumerate(cv):
            if k != i:
                s = sum(x * o.get(w, 0) for w, x in cv[i].items())
                scores.append((s, "cand:" + cands[k]["id"]))
        scores.sort(reverse=True)
        top = [f"{s:.2f} {ref}" for s, ref in scores[:3] if s >= thresh]
        print(f"{c['id']}: " + (" | ".join(top) if top else "ok"))


if __name__ == "__main__":
    main()
