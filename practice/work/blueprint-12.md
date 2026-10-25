# Blueprint: Module 12, Getting help

Items file: `practice/items/12-getting-help.yaml`. Targets: about 60 questions (about 12 "Select
TWO") and 16 concept cards. Exam tasks: 4.3 (Support plans and technical resources), the security
resources of 2.4 (Trusted Advisor's security checks, the Security Blog, Trust & Safety, AWS CIRT,
who configures a Marketplace product) and the customer-support part of 3.8 where the pages map it.

The module has four objectives, one per lesson, so the table breaks each objective into the
sections that teach it. Simulation S15 serves 12.01a; Lab 17 serves 12.02a to 12.04a.

Counts: Q = questions, M = how many of them are "Select TWO", C = concept cards. Levels: Re recall,
Un understanding, Ap application. Counts are the actual ones in the items file.

Names: questions use today's Support plans (Basic, Business Support+, Enterprise Support, Unified
Operations). Developer, Business and Enterprise On-Ramp appear only as wrong answers or in
explanations, with their end date (2027-01-01). The old Personal and Service Health Dashboard names
appear only as things to translate. No item tests a Trusted Advisor check count, a price, a fee
figure, or whether Business Support+ qualifies for the Shield Response Team.

## 12.01a Choose the cheapest Support plan that fits a need [J·Ap] (lesson 12.01, Sim S15; tasks 4.3, 3.8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "Every account starts on Basic, which answers account questions but not technical ones" | What Basic includes; the cheapest way to a technical case; what Support never does | Un, Ap | 2 | 1 | 1 |
| 01, "Business Support+ adds technical help around the clock" | What the first paid plan adds; how its fee is worked out (no figures) | Un | 1 | 1 | 1 |
| 01, "Enterprise Support adds a named person who knows your setup" | Enterprise over B+ (TAM, Priority); Security Incident Response included | Re, Ap | 2 | 1 | 0 |
| 01, "Unified Operations is for systems where minutes matter" | Domain specialists and monitoring; fastest target | Re, Ap | 2 | 0 | 0 |
| 01, "Response times are targets for a first reply, not guarantees" | Paid plans share every target below business-critical | Un | 1 | 0 | 0 |
| 01, ""Response times are guaranteed" is wrong" | Targets for a first reply, not a fix | Un | 1 | 1 | 1 |
| 01, "Choose by starting at Basic and moving up only for a reason" | SRT also needs Shield Advanced (whether B+ qualifies is left open) | Un | 1 | 0 | 0 |
| 01, "Worked example: the bakery's recommendation" | B+ plus a free Well-Architected Tool review | Ap | 1 | 1 | 0 |
| 01, "Older material uses plan names that are being retired" | Today's four-plan lineup; Developer without a choice falls to Basic | Re | 1 | 1 | 1 |
| 01, ""Developer, Business and Enterprise On-Ramp are current plans" is out of date" | Translating an old plan name | Un | 1 | 0 | 1 |
| 06 (Sim S15), "Decision 2: the bakery in Module 11" | Basic when nothing needs fast help | Ap | 1 | 0 | 0 |
| 06 (Sim S15), "Decision 5: a design studio with four accounts" | B+ is per account: only production | Ap | 1 | 0 | 0 |
| 06 (Sim S15), "Decision 6: an online retailer and a payments processor" | Enterprise for a 15-minute target and a TAM | Ap | 1 | 0 | 0 |
| **Total 12.01a** | | | **16** | **6** | **5** |

## 12.02a Say what Trusted Advisor, AWS Health and Support Center each show, and who gets them [C·Un] (lesson 12.02, Lab 17; tasks 4.3, 2.4, 1.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "Trusted Advisor checks your setup against AWS's best practices, in six categories" | What TA does; a finding's category; the six categories; TA only reports; TA vs the WA Tool; categories aren't pillars | Re, Un, Ap | 5 | 1 | 1 |
| 02, "What you see in Trusted Advisor depends on your Support plan" | Basic's checks; cost checks need B+; Trusted Advisor Priority | Re, Un, Ap | 3 | 1 | 1 |
| 02, ""Basic gets a fixed number of checks" is wrong" | Why the guide gives no count | Un | 1 | 0 | 1 |
| 02, "AWS Health reports problems on AWS's side, through one dashboard with two views" | Dashboard first in an outage; Your account health; what's free; EventBridge on Basic | Un, Ap | 4 | 1 | 0 |
| 02, ""The Personal and Service Health Dashboards are separate products" is out of date" | Reading the old dashboard name | Un | 1 | 0 | 0 |
| 02, "Support Center is where you open cases and ask for more quota" | Quota requests on Basic; IAM, not root, opens cases | Un, Ap | 2 | 0 | 0 |
| 02, "Worked example: the bakery's week" | "Is it AWS or us?" first, then your own side | — | 0 | 0 | 1 |
| 05 (Lab 17), "Stop 4: the free Trusted Advisor checks, mapped to pillars" | The free checks serve security and reliability | Un | 1 | 1 | 0 |
| **Total 12.02a** | | | **17** | **4** | **4** |

## 12.03a Route a question to the right place [C·Ap] (lesson 12.03; tasks 4.3, 2.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "AWS's own pages explain how AWS works: documentation, whitepapers and blogs" | Documentation for exact facts; trust current docs over a dated whitepaper; the Security Blog | Un, Ap | 3 | 0 | 0 |
| 03, "re:Post is where people answer questions; the Knowledge Center is AWS's own articles inside it" | Who writes KC articles; re:Post for unusual problems on Basic; KC for common ones | Re, Ap | 3 | 0 | 0 |
| 03, "Prescriptive Guidance is for planning and building, not for fixing one error" | Patterns; the "We want to…" test | Ap | 1 | 0 | 1 |
| 03, "Support Center is the only door about your own account" | Only a case sees the account; when to open one | Un | 1 | 0 | 1 |
| 03, "Abuse from an AWS address goes to AWS Trust & Safety, not to Support" | The abuse form; evidence; ip-ranges.json; reporting doesn't block | Re, Ap | 3 | 1 | 1 |
| 03, ""Abuse goes to AWS Support" is wrong" | Own resource flagged; intruder is an urgent security case (AWS CIRT); Support can't take abuse reports | Un, Ap | 3 | 1 | 1 |
| **Total 12.03a** | | | **14** | **2** | **4** |

## 12.04a Choose the right kind of paid help: a partner, AWS Professional Services or AWS Support [C·Ap] (lesson 12.04; tasks 4.3, 2.4, 3.8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "AWS Support fixes problems with AWS; it doesn't build or run your systems" | No custom code, on any plan | Un | 1 | 0 | 0 |
| 04, "Solutions architects advise on design, free, through your account team" | Free design advice before building | Ap | 1 | 0 | 0 |
| 04, "AWS Professional Services does the project for you, for a fee" | AWS's own consultants under contract | Ap | 1 | 0 | 0 |
| 04, "AWS Partners are other companies: software vendors and services firms" | System integrator; Partner Solutions Finder and AWS Specialization | Re, Ap | 2 | 0 | 0 |
| 04, "What partners get from joining" | Partner benefits | Re | 1 | 1 | 0 |
| 04, "AWS Marketplace sells partners' products, with three services for the buyer" | An ISV sells on the AWS bill; Private Marketplace; License Manager; Procurement insights; private offer; the buyer configures | Re, Un, Ap | 6 | 0 | 2 |
| 04, "Professional Services, partners, Support or a solutions architect: compare them side by side" | Who does the hands-on work | Un | 1 | 1 | 1 |
| 04, "Worked example: five requests, five kinds of help" | Night-time operations from a managed services partner | Ap | 1 | 0 | 0 |
| **Total 12.04a** | | | **14** | **2** | **3** |

## Totals

61 questions (47 single, 14 "Select TWO"); 16 concept cards.

By page: 01 13, 02 16, 03 14, 04 14, 05 (Lab 17) 1, 06 (Sim S15) 3. By task: 4.3 50, 2.4 6, 3.8 5.
One card serves 1.2 (Trusted Advisor's categories against the pillars).

Question levels: 10 recall (16%), 22 understanding (36%), 29 application (48%). This leans toward
application on purpose: three of the four objectives are "choose" or "route" [Ap], and the
module's glossary (already 60-odd entries) carries the definitions as term cards. Correct single
answers sit A 12, B 13, C 11, D 11; the correct choice is the longest in 10 of 47.

"Select TWO" is 14 of 61 (23%), a little above the target of about 12, because several of the
module's facts are pairs (what Basic gets, what a plan adds, the two kinds of hands-on help).

Similarity: every question, in every wording, scores PASS (183 of 183). The first run flagged 16
wordings in 8 questions as REVIEW ("same services + same correct answer"); each got a new scenario
and a different choice set (`q12-bplus-adds-two`, `q12-production-down-stay-bplus`,
`q12-knowledge-center-who-writes`, which replaced a "which statement" item,
`q12-repost-for-unusual-error`, `q12-hands-on-help-two`), or a replaced distractor
(`q12-ta-empty-cost-category`, `q12-health-old-dashboard-name`).

Cards avoid what the module's glossary entries already hold (definitions of every plan, tool and
partner term); they carry rules, "why" and routing tests instead.

Left out on purpose: every price and fee figure (the B+ percentages, the Enterprise and Unified
Operations minimums), Trusted Advisor check counts, whether Business Support+ qualifies for the
Shield Response Team, case severity names beyond the top two, changing a case's severity on Basic,
re:Post Private (one dated box), AWS IQ and AWS Managed Services (AMS appears once as a wrong answer
that isn't a Support plan), AWS Skill Builder (a "going deeper" note), and the Free plan upgrade
triggers (volatile, and not exam content).
