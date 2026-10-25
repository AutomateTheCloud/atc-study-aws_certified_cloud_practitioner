# Blueprint: Module 13, Moving to AWS

Items file: `practice/items/13-moving-to-aws.yaml`. Targets: about 65 questions (about 13 "Select
TWO") and 18 concept cards. Exam tasks: 1.3 (the AWS CAF's outcomes, perspectives, domains and
phases; the 7 Rs with AWS's criteria; migration tools and Migration Evaluator), 1.4 (on-premises vs
AWS costs, license-included vs BYOL, Dedicated Hosts, rightsizing with Compute Optimizer), 3.4 for
DMS and SCT, and 2.1 where a "Your side of the line" section is tested. No prices are tested.

The module has four objectives, one per lesson, so the table breaks each objective into the sections
that teach it. Simulation S16 serves 13.02a and 13.01a; Simulation S17 serves 13.04a.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

Names: choices use today's names. AWS Transform MGN carries the exam's name, AWS Application
Migration Service, in its wordings, and explanations give both. Closed or gone tools (Application
Discovery Service, Migration Hub, Snowball, the TCO Calculator) appear only as wrong answers, with a
dated explanation (checked 2026-10-24). AWS Transform is the correct answer where a new customer
needs discovery, as lesson 13.03 teaches.

## 13.01a Map a concern to a perspective of the AWS Cloud Adoption Framework [C·Ap] (lesson 13.01, task 1.3)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "The CAF aims at four business outcomes" | The four outcomes vs domains and technical results; a goal mapped to an outcome | Re, Ap | 2 | 1 | 0 |
| 01, "Four domains change, each enabling the next" | The chain of domains; why moving servers is only the first link | Re | 1 | 0 | 1 |
| 01, ""Process is one of the CAF perspectives" is wrong" | Process is a domain; which names are perspectives | Re, Un | 2 | 1 | 0 |
| 01, "Six perspectives group the capabilities, each owned by different people" | People (skills and roles); Security (protect records, pass an audit); capability names that mislead | Ap | 2 | 0 | 1 |
| 01, "Map a concern by asking what is at stake, not who is asking" | Operations; Platform; a CFO's concern that is People's | Ap | 3 | 0 | 0 |
| 01, "Business or Governance: deciding what to do, or overseeing how it goes" | Governance tracks spend and licenses; Business decides what to fund first; Governance's concerns | Un, Ap | 3 | 1 | 0 |
| 01, "Four phases, repeated: Envision, Align, Launch, Scale" | Phase order (vs MAP's phases); Align finds gaps; why the phases repeat | Re, Ap | 2 | 0 | 1 |
| 01, "The CAF and the 7 Rs work at different levels" | Organization vs one application; portfolio management; a Well-Architected review for one workload | Re, Un | 3 | 0 | 0 |
| **Total 13.01a** | | | **18** | **3** | **3** |

## 13.02a Assign and justify a migration strategy for each application [J·An] (lesson 13.02, Sim S16, task 1.3; 2.1 for the responsibility line)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, ""There are six Rs" is wrong" | Which names are among the 7 Rs | Re | 1 | 1 | 0 |
| 02, "Retire and retain: decide first what doesn't move" | Retire criteria; low use doesn't decide; retain for special hardware; retain criteria; why decide these first | Un, Ap | 4 | 1 | 1 |
| 02, "Rehost and relocate: move without changing the application" | Rehost to meet a deadline; relocate VMware; relocate between accounts; why rehost isn't just quick; relocate is the quickest | Un, Ap | 3 | 0 | 2 |
| 02, "Replatform and repurchase: change something on the way" | Database onto RDS; containers without code changes; SaaS; what remains after repurchase | Un, Ap | 4 | 1 | 0 |
| 02, "Refactor: redesign for the cloud when the business demands it" | Refactor criteria; move first, modernize after; splitting sensitive tables | Un, Ap | 2 | 0 | 1 |
| 02, "Database replication is a technique, used inside a strategy" | Replication with DMS carries out a replatform | Un | 1 | 0 | 0 |
| 02, "Your side of the line" | What stays the customer's after replatforming onto RDS, and under every strategy (task 2.1) | Un, Re | 1 | 1 | 1 |
| 05 (Sim S16), "Decision 4: the slide below has five errors; find them" | Correcting a slide with six Rs and a "process" perspective | Un | 1 | 1 | 0 |
| **Total 13.02a** | | | **17** | **5** | **5** |

## 13.03a Choose a migration tool for a job [C·Ap] (lesson 13.03, tasks 1.3 and 3.4; 2.1 for the responsibility line)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "Migration Evaluator prices the move before anyone commits" | A data-driven case with license options; its agentless collector and what it doesn't do | Re, Ap | 2 | 0 | 0 |
| 03, "The discovery and tracking tools are closed to new customers" | AWS Transform for a new customer's discovery | Ap | 1 | 0 | 0 |
| 03, ""The discovery tools are open to new customers" is wrong" | Migration Hub's status in a plan; the exam's answer vs today's | Re | 1 | 0 | 1 |
| 03, "Application Migration Service, now AWS Transform MGN, rehosts whole servers" | MGN for whole servers; block-level replication keeps downtime short; why waves | Un, Ap | 2 | 0 | 1 |
| 03, "MGN moves servers; DMS moves the data inside databases" | Same engine: DMS alone; engine change: SCT and DMS; why DMS rather than MGN | Un, Ap | 3 | 1 | 0 |
| 03, "Files move over the network with DataSync; Snowball is no longer the answer" | DataSync for a large file share, not Snowball; the network arithmetic | Ap | 1 | 0 | 1 |
| 03, "MGN or Elastic Disaster Recovery: same copying, different ending" | Elastic Disaster Recovery for servers that stay; what separates the two | Un, Ap | 2 | 0 | 0 |
| 03, "Worked example: a tool for each of the chain's jobs" | Job and tool pairs | Un | 1 | 1 | 0 |
| 03, "Your side of the line" | Who patches a rehosted server (task 2.1) | Un | 1 | 0 | 0 |
| **Total 13.03a** | | | **14** | **2** | **4** |

## 13.04a Build a cost comparison and make a licensing decision [J·Ev] (lesson 13.04, Sim S17, task 1.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "The big picture: three ways to spend the next three years" | Why moving as it is can cost more than staying | — | 0 | 0 | 1 |
| 04, "Count every cost on both sides, including the move itself" | What a draft leaves out; why licenses get their own line | Un | 2 | 1 | 0 |
| 04, "There is no TCO Calculator: use Migration Evaluator for the case, and the Pricing Calculator for estimates" | What the Pricing Calculator does and doesn't do; the TCO idea outlives the calculator | Un | 1 | 0 | 1 |
| 04, "Rightsize twice: before the move from measured data, and after it with Compute Optimizer" | Compute Optimizer for over-sized instances; its facts; the SQL Server edition finding | Re, Ap | 3 | 1 | 0 |
| 04, "License-included or bring your own license: who pays the software vendor" | BYOL compliance is the customer's; which license routes exist; RDS with your own licenses; License Manager; Windows and License Mobility; the 2019-10-01 rule | Re, Ap | 4 | 1 | 2 |
| 04, "Worked example: licensing a distributor's reporting database" | Why BYOL on a Dedicated Host can cost the most; sunk cost | Un | 1 | 0 | 1 |
| 04, "In real work: finance and technology build the case together" | Who owns which numbers (COST01-BP02) | — | 0 | 0 | 1 |
| 06 (Sim S17), "How the data gets made" | What Compute Optimizer needs before a finding (dated) | — | 0 | 0 | 1 |
| 06 (Sim S17), "Decision 1: for each server, choose downsize, upsize, keep, schedule or wait, and say why" | Rightsize before committing; schedule a part-time server; wait for memory data; upsizing | Un, Ap | 4 | 0 | 0 |
| 06 (Sim S17), "Decision 2: choose a route for each workload" | Per-core licenses on a Dedicated Host | Ap | 1 | 0 | 0 |
| **Total 13.04a** | | | **16** | **3** | **6** |

## Totals

65 questions (52 single, 13 "Select TWO"); 18 concept cards.

By page: 01 18, 02 16, 03 14, 04 11, 05 (Sim S16) 1, 06 (Sim S17) 5. By task: 1.3 45, 1.4 16,
2.1 2, 3.4 2.

Question levels: 11 recall (17%), 22 understanding (34%), 32 application (49%). This leans toward
application on purpose: all four objectives are apply, analyze or evaluate ([C·Ap], [J·An], [J·Ev]),
and recall of names and definitions is carried by the 81 glossary cards for this module. Correct
single answers sit A 13, B 13, C 13, D 13; the correct choice is the longest in 16 of 52.

Similarity: every question, in every wording, scores PASS (195 of 195). Six items needed rewrites on
the first run: q13-perspectives-select-two (REJECT, stem overlap; now a working-group scenario),
q13-review-workload-design and q13-license-routes-select-two ("same services + same correct
answer"; new scenarios and choice sets), and q13-relocate-county-vmware, q13-replatform-mysql-rds
and q13-replatform-into-containers ("combined"; new scenarios and choice sets).

Cards avoid what the module's glossary entries already hold (definitions, the 7 Rs' names, MAP's
phases, zombie and idle thresholds, the rehost/relocate, MGN/DMS/DRS, BYOL/license-included and
Compute Optimizer/Auto Scaling contrasts). They carry rules, causes, "why" and exam-vs-today points.

Left out on purpose: prices of every kind (the m7i figures, Dedicated Host rates, MGN's free
replication hours, Compute Optimizer's paid option); the Cloud Economics Center's five value
dimensions (a list of five, and a marketing framing); the count of 47 capabilities; Amazon EVS as a
named answer (not on the exam's list); MGN's pricing; the Migration Readiness Assessment and MAP
beyond their glossary cards.
