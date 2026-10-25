# Blueprint: Module 14, Capstone: a Well-Architected review

Items file: `practice/items/14-capstone.yaml`. Targets: about 30 questions (about 6 "Select TWO")
and 10 concept cards. Exam tasks: 1.2 (the Well-Architected pillars applied to one workload: which
pillar a finding belongs to, which risk is highest, which fix addresses it; the Well-Architected
Tool), with the cross-domain decisions the capstone makes: 2.1 (who patches the web servers), 2.2
(CloudTrail history beyond 90 days), 3.3 (a single-AZ web tier, Auto Scaling and a load balancer),
4.1 (which charges are hourly; when to commit), 4.2 (Tag Editor, the bill) and 4.3 (a Support plan
for a small bill). No prices are tested: every figure in the lesson is dated and volatile, so items
ask about the reasoning, not the numbers.

The glossary's Module 14 entries (accepted risk, close-out, high-risk issue, improvement plan,
milestone, review question, review scope, scoring rubric, workload inventory) already become term
cards, so the concept cards hold rules and "why" facts that no term card states. Four first-draft
cards that restated those entries were replaced. Module 02 already tests "a review is not pass or fail", what the Tool is, and simple
pillar-to-scenario mapping; this module's items apply those ideas to the bakery's inventory instead
of restating them.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

## 14.01a Assemble a pillar-by-pillar review of a workload, price the fixes and recommend a Support plan, justifying each choice [J·Ev] (lesson 14.01; tasks 1.2, 2.1, 2.2, 3.3, 4.1, 4.3)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "Step 1: start from the inventory, and write down what's out of scope" | A part nobody reviewed is written down as out of scope | Un | 1 | 0 | 0 |
| 01, "Step 2: ask each pillar's own question" | A review that finds nothing asked too few questions; strengths are recorded too | Un | 1 | 0 | 1 |
| 01, "Step 3: rate each finding by what it would do to the business" | The highest risk among findings; the same gap rated lower where harm is small; three-AZ copies are not backups | Ap, Un | 3 | 0 | 0 |
| 01, "Step 4: price each fix with dated rates, and count people's time" | Which charges bill every hour; hours of work count too | Un | 1 | 1 | 1 |
| 01, "Worked example: the reliability pillar" | Pillar of the single-AZ server; what an Auto Scaling group of one leaves undone; weighing a fix against the harm; why a launch template and a second public subnet | Ap, Un | 3 | 0 | 2 |
| 01, "Step 5: recommend a Support plan from the review's findings" | The cheapest plan with technical cases for a small bill; recording the owner's decision as an accepted risk | Ap | 2 | 0 | 0 |
| 01, "Step 6: write the improvement plan the owner can act on" | Order of fixes: high risks first, then quick and cheap within a level | Ap | 1 | 0 | 1 |
| 01, "Your review, then the model answer" | Pillar of log retention, of an instance size chosen by a label; the two security findings; CloudTrail beyond 90 days; actionable alerts; a noisy alarm; the log retention fix; who patches; when to commit to Reserved Instances; Graviton for sustainability | Ap, Un | 9 | 2 | 2 |
| 01, "In real work: review early, review again, and keep the list short" | When the Framework recommends reviews; reviewing is operational excellence | Re | 1 | 1 | 1 |
| **Total 14.01a** | | | **22** | **4** | **8** |

## 14.02a Record a review in the Well-Architected Tool and read its risks [P·Ap] (Lab 18; task 1.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "Before you start: your account, your responsibility" | The Tool has no additional charge and needs no paid Support plan | Re | 1 | 0 | 0 |
| 02, "Part B: answer four questions from evidence (challenge)" | Where a risk comes from (a missing High practice); marking a practice not applicable; what the Tool's improvement plan leaves out | Un, Ap | 3 | 1 | 0 |
| 02, "Part D: save a milestone (follow-along)" | A milestone to prove progress next quarter | Ap | 1 | 0 | 0 |
| 02, "Recap" | The Tool records answers; it doesn't inspect the account | Un | 1 | 0 | 0 |
| 02, "Clean up" | Tag Editor can't find a workload; check the Tool's own list | Re | 0 | 0 | 1 |
| **Total 14.02a** | | | **6** | **1** | **1** |

## 14.03a Close out an AWS account safely: find every leftover, check the bill and keep the guardrails [P·Ap] (Lab 19; task 4.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "Part A: sweep every Region by tag" | Tag Editor across all Regions; searching by key alone | Re | 1 | 0 | 1 |
| 03, "Part B: check what tags can't find" | Why an empty tag search can still miss leftovers | Un | 1 | 1 | 0 |
| 03, "Part C: read the bill and the credits" | A charge in an unfamiliar Region | Ap | 1 | 0 | 0 |
| 03, "Part D: review your guardrails, and keep them" | Guardrails stay whatever happens to the account | Ap | 1 | 0 | 0 |
| 03, "Part E: the next day" | Why the bill is checked again the next day | Un | 1 | 0 | 0 |
| **Total 14.03a** | | | **5** | **1** | **1** |

## Totals

| | Q | M | C | Re | Un | Ap |
|---|---|---|---|---|---|---|
| Actual | 33 | 6 | 10 | 3 | 14 | 16 |

The level mix leans to application (48%) and away from recall (9%), against the brief's 20/50/30:
the module's three objectives are all judgment or procedure applied to a workload (J·Ev, P·Ap), and
the recall it would need (pillar names, what the Tool is) is already tested in Module 02.
