import json, random, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from items import ITEMS

GUIDE = "/data/atc/study/atc-study-aws_certified_cloud_practitioner/guide/"
OUT = GUIDE + "90-exam-prep/05-practice-exam-1.md"
HERE = os.path.dirname(os.path.abspath(__file__))
TITLE = "Practice exam 1"
LETTERS = "ABCDE"

def slug(h):
    s = h.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")

def task_url(t):
    d = t.split(".")[0]
    return f"https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain{d}.html#cloud-practitioner-02-task{t}"

# check counts and links
assert len(ITEMS) == 65, len(ITEMS)
for it in ITEMS:
    n = len(it["choices"]); k = sum(c for _, c in it["choices"])
    if it.get("multi"):
        assert n == 5 and k == 2, it["id"]
        assert it["stem"].endswith("(Select TWO.)"), it["id"]
    else:
        assert n == 4 and k == 1, it["id"]
    for f, h in it["links"]:
        heads = [l[3:].strip() for l in open(GUIDE + f) if l.startswith("## ") or l.startswith("### ")]
        assert h in heads, (it["id"], f, h)

# order: shuffle until no two neighbours share a task or a domain run of 3, and no two Select TWO in a row
seed = 11
while True:
    r = random.Random(seed); order = ITEMS[:]; r.shuffle(order)
    ok = True
    for i in range(1, 65):
        if order[i]["task"] == order[i-1]["task"]: ok = False
        if order[i].get("multi") and order[i-1].get("multi"): ok = False
        if i >= 2 and order[i]["task"][0] == order[i-1]["task"][0] == order[i-2]["task"][0]: ok = False
    if ok: break
    seed += 1

# key positions for single-answer items
rp = random.Random(7)
singles = [it for it in order if not it.get("multi")]
fixed_pos = {it["id"]: [c for _, c in it["choices"]].index(1) for it in singles if it.get("fixed")}
need = {p: 13 for p in range(4)}
for p in fixed_pos.values(): need[p] -= 1
targets = [p for p in range(4) for _ in range(need[p])]
rp.shuffle(targets)
ti = 0
import itertools
pairs = list(itertools.combinations(range(5), 2)); rp.shuffle(pairs)
pairs = pairs + pairs[:3]; pi = 0
for it in order:
    ch = it["choices"][:]
    if it.get("multi"):
        keys = [c for c in ch if c[1]]; rest = [c for c in ch if not c[1]]
        rp.shuffle(keys); rp.shuffle(rest); a, b = pairs[pi]; pi += 1
        ch = [None]*5; ch[a], ch[b] = keys
        it_r = iter(rest); ch = [x if x else next(it_r) for x in ch]
    elif not it.get("fixed"):
        key = [c for c in ch if c[1]][0]; rest = [c for c in ch if not c[1]]
        rp.shuffle(rest); pos = targets[ti]; ti += 1
        ch = rest[:pos] + [key] + rest[pos:]
    it["_choices"] = ch
    it["_key"] = [LETTERS[i] for i, c in enumerate(ch) if c[1]]

# ---- page ----
DOM = {"1": ("Domain 1: Cloud Concepts", 24), "2": ("Domain 2: Security and Compliance", 30),
       "3": ("Domain 3: Cloud Technology and Services", 34), "4": ("Domain 4: Billing, Pricing, and Support", 12)}
tasks = sorted({it["task"] for it in ITEMS}, key=lambda t: [int(x) for x in t.split(".")])
fm = f"""---
type: check
id: clf-90-05
title: "{TITLE}"
tasks: [{", ".join('"%s"' % t for t in tasks)}]
objectives: []
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 13; 90 minutes for the exam and about an hour to review it"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00, clf-10-00, clf-11-00, clf-12-00, clf-13-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html"
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://aws.amazon.com/cloud-adoption-framework/"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://aws.amazon.com/compliance/programs/"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html"
  - "https://aws.amazon.com/premiumsupport/plans/"
---
"""

doms = {d: [i+1 for i, it in enumerate(order) if it["task"][0] == d] for d in "1234"}
counts = {d: len(v) for d, v in doms.items()}
nmulti = sum(1 for it in order if it.get("multi"))

body = []
body.append("# Practice exam 1: a full 65-question form, timed and weighted like the CLF-C02 exam\n")
body.append(f"Sixty-five questions in 90 minutes, spread across all four domains and all 19 task statements in the same proportions as the real exam. Take it in one sitting, closed book, then score each domain separately to see where you're ready and what to restudy.\n")
body.append("**For:** an adult studying alone, possibly new to IT, who has finished Modules 02 to 13 of this guide (start from the [Module 02 brief](../02-why-the-cloud/00-brief.md) if you haven't). **Time:** 90 minutes for the questions, and about an hour to go through the answer key. No AWS account is needed.\n")
body.append("## How to take it\n")
body.append(f"""- **Set a timer for 90 minutes** and work in one sitting, as on exam day. Closed book: no notes, no guide pages, no searching. If you will take the exam in English as a non-native speaker with the extra 30 minutes, set 120.
- **Write your answers down** as you go (question number and letter), and don't open the answer key until you have answered all 65. Answer every question: on the real exam a blank counts as wrong and a wrong guess costs nothing.
- **Two question types**, as on the exam. Most questions have one correct answer out of four. {nmulti} questions end with "(Select TWO.)" and have two correct answers out of five; they count only if both of your choices are right.
- **Score it by domain** with the table under the answer key. A domain score tells you what to do next; it doesn't predict your exam score.
- **Count it only once.** A form shows your readiness only the first time you take it. When you come back to it after restudying, treat it as practice, not as a readiness check.

Where the exam guide uses an older name for a service or plan, the questions use the exam's name and the answer key gives today's name. No question needs a price or a count. Facts were checked on 2026-10-24. The real exam has 65 questions too, but 15 of them are unscored trial questions that you can't identify ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md)); on this form, all 65 count.
""")
body.append("## Questions\n")
for i, it in enumerate(order, 1):
    body.append(f"**{i}.** {it['stem']}\n")
    for L, (txt, _) in zip(LETTERS, it["_choices"]):
        body.append(f"- {L}. {txt}")
    body.append("")
body.append("## Answer key\n")
body.append("Open it only after you have answered all 65 questions. Each answer names its task statement in the exam guide, explains why the answer is right and why the most tempting wrong choice is wrong, and links to the section that teaches it.\n")
body.append("<details><summary>Answer key</summary>\n")
for i, it in enumerate(order, 1):
    key = " and ".join(it["_key"])
    links = "; ".join(f"[{h}](../{f}#{slug(h)})" for f, h in it["links"])
    body.append(f"**{i}. {key}** ([Task {it['task']}]({task_url(it['task'])}))\n")
    body.append(f"{it['expl']} **Reread:** {links}.\n")
body.append("</details>\n")

def bands(n):
    lo = -(-6 * n // 10)  # ceil 60%
    hi = -(-8 * n // 10)  # ceil 80%
    return lo, hi
body.append("## Score by domain\n")
body.append("Count your correct answers in each domain. A \"(Select TWO.)\" question counts only if both choices are right. Then find your band.\n")
body.append("| Domain | Share of the exam | Questions on this form | Below 60%: restudy | 60% to 79%: review the linked sections | 80% or more: ready on this domain |")
body.append("|---|---|---|---|---|---|")
for d in "1234":
    name, w = DOM[d]; n = counts[d]; lo, hi = bands(n)
    mid = f"{lo}" if lo == hi-1 else f"{lo} to {hi-1}"
    body.append(f"| {name} | {w}% | {n} | 0 to {lo-1} | {mid} | {hi} to {n} |")
body.append("")
body.append("Which questions belong to which domain:\n")
for d in "1234":
    body.append(f"- **{DOM[d][0]}:** questions {', '.join(map(str, doms[d]))}.")
body.append("")
body.append("""What to do with each band:

- **Restudy:** go back to the module lessons for that domain, redo their labs or simulations, and take the module mastery checks again before another full form.
- **Review the linked sections:** reread the section linked beside each question you missed, and write one sentence on why the right answer beats the choice you picked.
- **Ready on this domain:** keep it fresh with short mixed practice, and spend most of your time on the domains below 80%.

For an overall figure, weight each domain's percentage by its share of the exam: 0.24 × Domain 1 + 0.30 × Domain 2 + 0.34 × Domain 3 + 0.12 × Domain 4. Read every result as a range, not a point. On 65 questions, three or four lucky or unlucky answers move the total by about five points, and Domain 4 has only seven questions, so one answer moves it by about fourteen.

**A practice score is not a prediction of your exam score.** The real exam reports a scaled score from 100 to 1,000 with a pass mark of 700, uses different questions, and includes unscored ones. What this form can tell you is which domains need more study. Before booking, take a second form you haven't seen, and check that your weaker domains have moved up.
""")
body.append(f"""---

"{TITLE}" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
""")
page = fm + "\n" + "\n".join(body)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page)

# blind copy (no answer key)
blind = re.sub(r"## Answer key.*?</details>\n", "", page, flags=re.S)
blind = re.sub(r"## Score by domain.*", "", blind, flags=re.S)
open(os.path.join(HERE, "blind-exam.md"), "w").write(blind)

# similarity candidates
with open(os.path.join(HERE, "candidates.jsonl"), "w") as f:
    for i, it in enumerate(order, 1):
        f.write(json.dumps({"id": f"pe1-q{i:02d}-{it['id']}", "question": it["stem"],
                            "options": {L: t for L, (t, _) in zip(LETTERS, it["_choices"])},
                            "answer": it["_key"]}) + "\n")
# key for comparison
json.dump({i: {"key": it["_key"], "id": it["id"], "task": it["task"]} for i, it in enumerate(order, 1)},
          open(os.path.join(HERE, "key.json"), "w"), indent=0)
from collections import Counter
print("seed", seed, "domain counts", counts, "multi", nmulti)
print("single key positions", Counter(it["_key"][0] for it in order if not it.get("multi")))
print("multi keys", [ "".join(it["_key"]) for it in order if it.get("multi")])
