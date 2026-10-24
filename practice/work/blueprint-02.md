# Blueprint: Module 02, Why organizations use the cloud

Items file: `practice/items/02-why-the-cloud.yaml`. Targets from the brief: about 70 questions
(about 14 "Select TWO") and 18 concept cards, weighted to the lessons that teach tasks 1.1, 1.2,
1.4 and 3.1. The course plan gives one objective per lesson (02.01a to 02.05a); the rows below
split each into the outcomes its lesson lists under "What you'll learn", so the counts can be
checked. The lab and the simulation supply application scenarios for 02.02a, 02.03a and 02.04a.

Levels in the "Level" column are the course plan's ([C·Ap] = concept, apply; [C·An] = concept,
analyze); the two [C·Un] rows (concept, understand) are side topics with no course-plan level of
their own, so that level is ours. Counts are the **actual** counts in the items file (Q = questions, of which M = "Select
TWO"; C = concept cards).

| Objective | Outcome (from the lesson) | Level | Page, section | Q | M | C |
|---|---|---|---|---|---|---|
| 02.01a | Say which three features make something cloud computing | C·Ap | 01, "Three features together make something cloud computing" | 3 | 1 | 1 |
| 02.01a | Before the cloud: what owning on-premises IT involves | C·Ap | 01, "Before the cloud, organizations owned and ran their own equipment" | 1 | 0 | 0 |
| 02.01a | Classify a setup as cloud, hybrid or on-premises; AWS's three model names; why hybrid | C·Ap | 01, "The three deployment models...", "Worked example: classifying three setups", "Hybrid is often a deliberate choice..." | 5 | 1 | 2 |
| 02.01a | "Public, private, community" isn't AWS's vocabulary; private cloud is on-premises | C·Ap | 01, "\"Public, private and community\" are not AWS's deployment models" | 1 | 0 | 0 |
| 02.01a | IaaS, PaaS, SaaS (going deeper) | C·Un | 01, "Going deeper (optional): IaaS, PaaS and SaaS" | 1 | 0 | 0 |
| 02.01a | Undifferentiated heavy lifting (cost design principle) | C·Un | 01, "In real work: the deployment model is a business decision" | 1 | 0 | 0 |
| 02.02a | Read idle capacity and lost sales from a demand curve; capacity follows the curve | C·Ap | 02, "Buying for the peak...", "Buying for normal months...", "In the cloud, capacity follows the curve" | 4 | 1 | 1 |
| 02.02a | Fixed vs variable expense; variable isn't automatically cheaper | C·Ap | 02, "Fixed expense becomes variable expense...", "The cloud doesn't always cut operating costs" | 3 | 1 | 1 |
| 02.02a | Economies of scale lower the unit price, not the curve | C·Ap | 02, "Economies of scale..." | 2 | 0 | 1 |
| 02.02a | Link AWS's six advantages to the demand curve | C·Ap | 02, "Six advantages, one picture" | 3 | 1 | 0 |
| 02.03a | Elasticity, and the "scalability is manual" myth | C·An | 03, "Elasticity...", "\"Scalability is manual...\" is a myth" | 4 | 1 | 0 |
| 02.03a | Agility, and telling it from elasticity | C·An | 03, "Agility...", "Elasticity and agility both sound like \"fast\"" | 2 | 1 | 1 |
| 02.03a | High availability: failure, not load; the nines | C·An | 03, "High availability..." | 3 | 0 | 1 |
| 02.03a | Durability is not availability | C·An | 03, "Durability: stored data isn't lost", "Durability isn't availability" | 2 | 0 | 1 |
| 02.03a | Global reach, and telling it from agility | C·An | 03, "Global reach...", "Global reach and agility both happen \"in minutes\"" | 1 | 0 | 1 |
| 02.03a | Name the benefit and rule out the rest; benefits are possibilities, not defaults; benefits to pillars | C·An | 03, "All five side by side", "In real work: the benefits map to the Well-Architected pillars" | 3 | 1 | 1 |
| 02.04a | The seven on-premises cost groups; TCO; hidden costs (waiting) | C·Ap | 04, "On-premises costs come in seven groups" | 3 | 1 | 0 |
| 02.04a | Capital/operating vs fixed/variable are different questions | C·Ap | 04, "Capital or operating, fixed or variable..." | 2 | 0 | 1 |
| 02.04a | Compare costs in plain numbers; the cloud doesn't automatically cut costs; costs that stay | C·Ap | 04, "Worked example: the bakery's three-year comparison", "Moving to the cloud doesn't automatically lower costs" | 4 | 1 | 1 |
| 02.04a | Rightsizing and automation | C·Ap | 04, "Rightsizing and automation keep the variable bill small" | 3 | 0 | 1 |
| 02.05a | Six pillars (count, names); match a concern to a pillar | C·An | 05, "Six pillars, six questions" | 4 | 1 | 1 |
| 02.05a | Reliability vs performance efficiency; cost optimization vs sustainability; concern to pillar | C·An | 05, "Pillars that sound alike, side by side" | 5 | 0 | 0 |
| 02.05a | General design principles vs slogans | C·An | 05, "Real design principles, and slogans..." | 2 | 1 | 1 |
| 02.05a | Trade-offs; security and operational excellence not traded away | C·An | 05, "The pillars can be traded against each other..." | 2 | 1 | 1 |
| 02.05a | Framework vs Well-Architected Tool (vs Trusted Advisor); a review isn't an audit | C·An | 05, "The Framework is guidance; the Well-Architected Tool applies it" | 2 | 0 | 1 |
| 02.03a | Lab 01: agility measured; tag, delete and confirm | C·Ap | 06, "Recap", "Clean up" | 2 | 1 | 0 |
| 02.02a, 02.04a | Simulation S1: the matched-renting cost; what a flat owned price hides; the benefit it relies on | C·Ap | 07, "Decision 2", "Decision 5", "Decision 6" | 3 | 1 | 0 |
| **Total** | | | | **71** | **15** | **18** |

## Levels

Questions: 14 recall (20%), 33 understanding (46%), 24 application (34%), against the brief's
20/50/30. Concept cards are all recall or understanding.

## By page

| Page | Questions | Select TWO | Cards |
|---|---|---|---|
| 01 What cloud computing is | 12 | 2 | 3 |
| 02 Before and after: the demand curve | 12 | 3 | 3 |
| 03 Telling the benefits apart | 15 | 3 | 5 |
| 04 What a data center really costs | 12 | 2 | 3 |
| 05 The Well-Architected Framework | 15 | 3 | 4 |
| 06 Lab 01 | 2 | 1 | 0 |
| 07 Simulation S1 | 3 | 1 | 0 |

## Notes on the plan

- Glossary entries for Module 02 already produce term, abbreviation and confused-pair cards (elasticity
  vs scalability, durability vs high availability, Framework vs Tool, and so on), so the concept
  cards hold rules, causes and "how to choose" instead.
- Volatile facts (Region and AZ counts, S3's durability and availability figures, the Tool's price,
  data transfer terms) are not tested; where an item touches one, its explanation is dated.
- Left out on purpose: best-practice IDs (the lesson says not to memorize them), the Well-Architected
  Agent (not in the exam guide), Lab 01's console steps and bucket-naming rules.
