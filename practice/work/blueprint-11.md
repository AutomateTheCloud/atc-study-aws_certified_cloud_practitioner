# Blueprint: Module 11, Paying for AWS

Items file: `practice/items/11-paying-for-aws.yaml`. Targets: about 75 questions (about 15 "Select
TWO") and 20 concept cards. Exam tasks: 4.1 (pricing models and cost drivers, including data
transfer by direction and Reserved Instance behavior in AWS Organizations), 4.2 (billing, budget and
cost management tools, consolidated billing, cost allocation tags, the Free Tier) and 1.4 (cloud
economics: consumption model, economies of scale).

The module has four objectives, one per lesson, so the tables break each objective into the
sections that teach it. Lab 15 and Sim S13 serve 11.02a and 11.03a, Lab 16 serves 11.04a, and Sim
S14 serves 11.03a. Counts are the actual ones in the items file (Q = questions, M = how many of them
are "Select TWO", C = concept cards). Levels: Re recall, Un understanding, Ap application.

Names: the exam's "AWS Cost and Usage Report" is taught as CUR 2.0, created in AWS Data Exports
(one wording of the CUR choices keeps the exam name). The legacy "12 months free" Free Tier, "two
Savings Plans types", "a budget caps spending", "a tag alone shows costs", "a Capacity Reservation
discounts" and the retired Simple Monthly and TCO calculators appear only as wrong answers or as
the thing a question corrects.

Not tested on purpose: any price or rate; exact discount maximums ("up to 72%" vs the older "75%",
66%, 90% and the rest; the one "up to" question keys on what a ceiling means, not on a number);
Free Tier credit amounts and the credit expiry after an upgrade (AWS's pages disagree); Cost
Explorer's 13/18/38-month horizons (dated, and the page itself says to look for "visualize,
analyze, forecast", not a number); Budgets and Cost Explorer API prices; the Savings Plans return
rule; the new sign-up experience's spend limit; account tags for cost allocation (dated, new).

## 11.01a Identify what drives a bill [C·Ap] (lesson 11.01, tasks 4.1, 4.2, 1.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "Pay as you go means every charge is a quantity times a rate" | "Adopt a consumption model"; rates that fall with volume (economies of scale) | Re, Un | 2 | 0 | 0 |
| 01, "Time-based charges run whether or not anyone uses the resource" | Which charges continue in a quiet fortnight | Ap | 1 | 1 | 1 |
| 01, "Storage bills for what you keep; requests bill for what's used" | Sorting a line onto its meter | Un | 1 | 0 | 0 |
| 01, "Data transfer is priced by direction: in is free, but out, across and between usually cost" | NAT gateway fee on a free path; the cross-AZ trade-off | Ap | 2 | 0 | 0 |
| 01, ""In is free, out is charged" is only half the rule" | Cross-Region copies are charged | Un | 1 | 0 | 1 |
| 01, "Worked example: why did the bakery's bill nearly triple?" | The line that won't fall; the expert's question | Un, Ap | 2 | 0 | 1 |
| 01, "The Free Tier now: two plans, credits and two clocks" | Two clocks; Paid-plan-only offers; legacy "12 months"; credits running out on each plan; joining an organization upgrades; Always Free | Re, Un | 6 | 2 | 2 |
| **Total 11.01a** | | | **15** | **3** | **5** |

## 11.02a Choose a purchasing option for a usage pattern [J·Ap] (lesson 11.02, tasks 4.1, 1.4; Sim S13)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "The big picture: purchasing options do three different jobs" | Options bought for a rule or a guarantee, not a discount | Un | 1 | 1 | 0 |
| 02, "On-Demand is the default and the yardstick" | Why new work starts On-Demand | Un | 1 | 0 | 0 |
| 02, "A commitment trades flexibility for a lower rate" | What Savings Plans and RIs share; what earns a bigger discount; no renewal (card) | Re, Un | 2 | 2 | 1 |
| 02, "Savings Plans: commit to dollars per hour, in four types" | Unused hourly commitment is lost; usage above it (card) | Ap | 1 | 0 | 1 |
| 02, ""There are two types of Savings Plans" is out of date" | The two newer types | Re | 1 | 1 | 0 |
| 02, "Compute or EC2 Instance Savings Plan: flexibility or a deeper discount" | Moving to Fargate and another Region; OS change inside one family | Ap | 2 | 0 | 1 |
| 02, ""A Reserved Instance is a server set aside for you" is wrong" | An RI with nothing matching | Un | 1 | 0 | 0 |
| 02, "Standard or Convertible" | Exchange for a new family; sell on the Marketplace | Un, Ap | 2 | 0 | 1 |
| 02, "Zonal or Regional" | Zonal's two traits; size flexibility arithmetic; where size flexibility is missing | Un, Ap | 3 | 1 | 1 |
| 02, "Savings Plans or Reserved Instances: what follows your usage?" | Discount and capacity from one purchase | Ap | 1 | 0 | 0 |
| 02, ""Up to" is a ceiling, not a promise" | What "up to" means (no number keyed) | Un | 1 | 0 | 0 |
| 02, "Spot Instances: deep discounts for work that can stop" | Spot for restartable batch work; Spot sits outside Savings Plans | Un, Ap | 2 | 0 | 1 |
| 02, "Dedicated Hosts and Dedicated Instances: hardware with no other customers" | Why a Host suits per-core licenses; Instance for an isolation rule; what the two share | Un, Ap | 3 | 1 | 1 |
| 02, ""A Capacity Reservation gets you a discount" is wrong" | How a reservation bills; what discounts it | Un, Ap | 2 | 0 | 1 |
| 07 (Sim S13), "Decision 1: choose an option for each workload, and give the reason" | Capacity on set days; Database Savings Plan through an engine change | Ap | 2 | 0 | 0 |
| 07 (Sim S13), "Decision 2: commit to 0, 2 or 6 servers?" | Commit to the baseline | Ap | 1 | 0 | 1 |
| **Total 11.02a** | | | **26** | **6** | **9** |

## 11.03a Pick the tool for each stage: estimate, watch, analyze [C·Ap] (lesson 11.03, task 4.2; Lab 15; Sim S14)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "AWS Pricing Calculator estimates a design before it exists" | Estimating an unbuilt feature; the public calculator's traits; an estimate is only as good as its inputs; the retired calculators | Re, Un, Ap | 4 | 1 | 0 |
| 03, "AWS Budgets tells you when you pass a limit; it stops nothing unless you add an action" | Forecasted alerts; data delay | Un, Ap | 2 | 0 | 0 |
| 03, ""A budget caps your spending" is wrong" | No cap without an action; two of the three actions; SCP actions need the management account; what keeps billing after a stop | Re, Un | 4 | 1 | 2 |
| 03, "Cost Anomaly Detection tells you when spending is unusual, not when it is high" | Slow growth needs a budget; a small new charge needs anomaly detection; what it does | Un, Ap | 3 | 1 | 1 |
| 03, "Cost Explorer shows where the money went, and forecasts 18 months ahead" | Forecast and recommendations (no horizon number) | Un | 1 | 1 | 0 |
| 03, "The Cost and Usage Report holds every line item, delivered through Data Exports" | Exam name and today's place; line items for chargeback | Re, Ap | 2 | 0 | 0 |
| 03, "Pick the tool by the question it answers" | Which tools alert; the keyword for the CUR (card) | Un | 1 | 1 | 1 |
| 03, "Worked example: one forgotten instance in January" | Drill down one level at a time | Ap | 1 | 0 | 0 |
| 05 (Lab 15), "Part 2: find the hourly items, and trim the test copy" | Removing whole hourly items | Ap | 1 | 0 | 0 |
| 08 (Sim S14), Decisions 2, 3 and 5 | Anomaly detection silent on a new account; a deny policy leaves running instances alone; approval-based actions in production | Un, Ap | 3 | 0 | 0 |
| **Total 11.03a** | | | **22** | **5** | **4** |

## 11.04a Explain who gets a discount in an organization, and how tags reach cost reports [C·An] (lesson 11.04, tasks 4.2, 4.1; Lab 16)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "Consolidated billing combines usage and sends one bill" | Who pays; combined volume tiers | Un | 2 | 0 | 0 |
| 04, "A commitment discount goes to its owner first, then to matching usage anywhere in the organization" | Savings Plan sharing; RIs before Savings Plans; a zonal RI's capacity stays home | Re, Un | 3 | 0 | 1 |
| 04, "Discounts are shared across the organization unless the management account turns sharing off" | Sharing off for one account; prioritized vs restricted group sharing | Un, Ap | 2 | 0 | 0 |
| 04, "A tag reaches your cost reports only after you activate it" | What both tag types share; who activates in an organization; case-sensitive keys; `aws:createdBy` | Re, Un, Ap | 4 | 1 | 0 |
| 04, ""A tag shows costs" is wrong" | Activation missing; backfill's limit | Un, Ap | 2 | 0 | 1 |
| 04, "Give each team a view: accounts first, tags inside shared accounts, cost categories to name the groups" | Accounts split costs without tags; split charge rules | Un, Ap | 2 | 0 | 0 |
| **Total 11.04a** | | | **15** | **1** | **2** |

Lab 16's steps (activation, the two waits, the gray days before activation) are tested through
lesson 11.04's sections, which teach the same rules; no item cites the lab page.

## Totals

78 questions (63 single, 15 "Select TWO"); 20 concept cards.

By page: 01 15, 02 23, 03 18, 04 15, 05 (Lab 15) 1, 07 (Sim S13) 3, 08 (Sim S14) 3; none cites 06
(Lab 16). By task: 4.1 39, 4.2 37, 1.4 2 (1.4 is also served by the volume-tier item under 4.2).

Question levels: 11 recall (14%), 36 understanding (46%), 31 application (40%). This leans toward
application and away from recall compared with the 20/50/30 target, on purpose: three of the four
objectives are "choose" or "pick the tool" [C·Ap, J·Ap], and the module's glossary term cards carry
recall of names and definitions. Correct single answers sit A 16, B 16, C 16, D 15; the correct
choice is the longest in 22 of 63.

Similarity: every question, in every wording, scores PASS (234 of 234). One item needed a rewrite
(`q11-retired-calculators`, REVIEW for "same services + same correct answer"); it now asks what
became of the Simple Monthly Calculator, with statement choices instead of a list of tools.
