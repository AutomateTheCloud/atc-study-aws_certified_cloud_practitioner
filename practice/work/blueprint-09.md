# Blueprint: Module 09, Protecting, governing and proving compliance

Items file: `practice/items/09-protecting-and-governing.yaml`. Targets: about 90 questions (about
18 "Select TWO") and 24 concept cards. Exam tasks: 2.2 (CloudTrail, CloudWatch, Config, access
reports; encryption at rest and in transit; KMS, CloudHSM, ACM, Macie; GuardDuty, Inspector,
Security Hub, Detective; Artifact and compliance programs), 2.4 (Shield, WAF, Firewall Manager;
Trusted Advisor's security checks; AWS Marketplace security products; where AWS publishes security
information), 2.3 (Organizations, SCPs, Control Tower, as lesson 09.05 teaches them) and 2.1 (the
shared responsibility recap in lesson 09.06). One question serves 4.2 (consolidated billing, from
Simulation S11).

The module has six objectives, one per lesson, so the table breaks each objective into the
sections that teach it. Lab 12 (page 07) serves 09.01a and 09.05a; Simulation S9 (page 08) serves
09.03a; S10 (page 09) serves 09.01a; S11 (page 10) serves 09.05a.

**Not keyed, because the pages hedge them:** whether Business Support+ qualifies for the Shield
Response Team (questions say only that the SRT needs Shield Advanced *and* a qualifying Support
plan); Trusted Advisor's number of checks; the date of Security Hub's split; whether Macie opens on
the Free plan. No prices are tested; dated facts carry "(as of 2026-10-24)" in explanations.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

## 09.01a Choose the service that answers an audit question [C·An] (lesson 09.01, task 2.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "The big picture: four records, four questions" | Classify the question (who, how running, how set, who can) to pick the record | Ap | 2 | 1 | 0 |
| 01, "CloudTrail records who did what, when and from where" | A trail for more than 90 days; console trails are multi-Region; log file integrity validation | Ap, Re, Un | 3 | 0 | 0 |
| 01, ""CloudTrail records everything, forever" is wrong" | Data events off by default; why a trail on day one | Ap | 1 | 0 | 1 |
| 01, "CloudWatch shows how things are running, not who changed them" | EC2 logs need the agent, Lambda logs don't; a trail into CloudWatch Logs for a root sign-in alarm | Ap | 2 | 1 | 1 |
| 01, "AWS Config records how each resource was set, and judges it against your rules" | History starts when recording starts; rule results; conformance packs | Ap, Un | 3 | 1 | 0 |
| 01, "Access reports show who can do what, and whether they still use it" | Credential report; last accessed reports attempts, identity policies only | Ap, Un | 2 | 0 | 1 |
| 01, "Security logs live in a few known places, for set lengths of time" | What exists with nothing turned on | Un | 1 | 1 | 0 |
| 01, "Worked example: three of the auditor's questions" | Config first, then CloudTrail, for "who opened it" | Ap | 1 | 0 | 0 |
| 07 (Lab 12), "Part A: follow one change from start to finish (follow-along)" | What Event history can answer; per-Region view of sign-ins | Un | 1 | 0 | 1 |
| 09 (S10), "Decision 1: answer the auditor's four questions" | A configuration item stays true until the next one | Ap | 1 | 0 | 0 |
| 09 (S10), "Decision 2: the owner says, "Config caught it, so Config would have stopped it next time."" | Detect, fix, prevent are different tools | Un | 1 | 0 | 1 |
| **Total 09.01a** | | | **18** | **4** | **5** |

## 09.02a Choose an encryption and key approach [J·Ap] (lesson 09.02, task 2.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "At rest and in transit are two protections against two different threats" | Which protection fits which threat; AWS encrypts its own links, not your site; encrypted isn't access-controlled | Un | 3 | 1 | 0 |
| 02, "TLS certificates from ACM protect data in transit" | ACM for HTTPS that renews itself; ACM vs KMS; requiring HTTPS with a bucket policy; CloudFront certificates in N. Virginia | Ap, Re | 3 | 0 | 1 |
| 02, "KMS holds the keys for data at rest, and records every use" | AWS managed keys; the second gate; rotation keeps old material; disable rather than delete; what a customer managed key adds | Ap, Re, Un | 5 | 1 | 2 |
| 02, "CloudHSM gives you hardware no one else uses, and more of the work" | Custom key store for a single-tenant rule | Ap | 1 | 0 | 0 |
| 02, ""Compliance needs CloudHSM" is wrong" | KMS already uses validated HSMs; the order of the key decision | Un | 1 | 0 | 1 |
| 02, "Macie finds sensitive data in S3, so you know what to protect" | Acting on a Macie finding; Macie's two kinds of finding | Ap, Re | 2 | 1 | 0 |
| **Total 09.02a** | | | **15** | **3** | **4** |

## 09.03a Match a security finding to the service that raised it [C·Ap] (lesson 09.03, tasks 2.2 and 2.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "GuardDuty watches activity and reports threats happening now" | Its sources with nothing to set up; per Region; reports, doesn't block; EventBridge for alerts | Ap, Re, Un | 3 | 1 | 1 |
| 03, "Inspector scans workloads and reports weaknesses before an attacker finds them" | Continuous rescans on a new CVE; its two kinds of finding; vs GuardDuty | Ap, Un | 2 | 1 | 1 |
| 03, ""Create an assessment template and install the Inspector agent" is out of date" | Inspector Classic | Un | 1 | 0 | 0 |
| 03, "Security Hub gathers every finding and checks your settings, and the name now covers two products" | One place for findings plus standards; needs Config | Ap, Un | 2 | 0 | 1 |
| 03, ""Security Hub is one product" is no longer right" | Security Hub CSPM and the unified Security Hub | Re | 1 | 1 | 0 |
| 03, "Detective explains what happened after a finding" | Root cause and scope; GuardDuty detects, Detective investigates | Ap, Un | 2 | 0 | 0 |
| 03, "Trusted Advisor is a first look at your settings, with a few security checks free" | Basic Support's checks; categories; vs Security Hub CSPM | Re, Un | 2 | 0 | 1 |
| 03, "AWS Marketplace sells third-party security products, billed through AWS" | Third-party products billed through AWS; still yours to run | Un | 2 | 1 | 0 |
| 03, "Match a finding to its service by asking what it looked at" | Pick Macie's finding from a mixed list | Ap | 1 | 0 | 0 |
| 08 (S9), "Decision 1: name the service that raised each finding" | A failed standard control; two findings on one port from two services | Ap | 2 | 0 | 0 |
| **Total 09.03a** | | | **18** | **4** | **4** |

## 09.04a Choose protections for an attack type [J·Ap] (lesson 09.04, tasks 2.4 and 2.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "AWS Shield Standard is already protecting every AWS account" | Automatic and free; network floods; CloudFront in front strengthens it | Re, Un | 3 | 1 | 1 |
| 04, "Shield Advanced adds detection, people and bill protection, for a price" | DDoS cost protection; what it adds over Standard | Ap, Un | 2 | 1 | 0 |
| 04, ""Any Business Support plan brings the Shield Response Team" is wrong" | The SRT needs Shield Advanced; no plan is keyed | Un | 1 | 0 | 1 |
| 04, "AWS WAF reads each web request and allows, blocks or challenges it" | Cross-site scripting; where a web ACL attaches; rate-based rules; WAF vs security group | Ap, Re | 3 | 0 | 1 |
| 04, "Firewall Manager applies the same protections in every account" | Organization-wide policies including new accounts; prerequisites; Shield, WAF, Firewall Manager in one line | Ap, Re | 2 | 1 | 1 |
| 04, "Choose the protection by the attack, then check the cost" | Flood plus injection; blocking a range from a non-web server | Ap | 2 | 0 | 0 |
| 04, "Testing your own front door: AWS's penetration-testing policy" | No approval for listed services; flooding forbidden | Un | 2 | 0 | 0 |
| **Total 09.04a** | | | **15** | **3** | **4** |

## 09.05a State the compliance work that stays yours, and explain an SCP as a ceiling [C·Ap] (lesson 09.05, tasks 2.2, 2.4 and 2.3; S11 also 4.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 05, "AWS Artifact hands you AWS's audit reports, not a verdict on you" | A SOC 2 report for a partner; accepting a BAA | Ap, Un | 2 | 0 | 0 |
| 05, ""Artifact checks your compliance" is wrong" | A report covers AWS's controls only | Un | 1 | 1 | 1 |
| 05, "AWS lists its compliance programs, and which services each one covers" | Programs vary by country and industry | Re | 1 | 0 | 0 |
| 05, ""Not in Services in Scope means you can't use it" is wrong" | Not listed isn't forbidden | Un | 1 | 0 | 1 |
| 05, "Your remaining duty: what no AWS document does for you" | What stays the customer's | Un | 1 | 1 | 0 |
| 05, ""Audit Manager is the compliance answer" is wrong" | Conformance packs instead | Un | 1 | 0 | 0 |
| 05, "AWS Organizations groups accounts so you can govern them together" | A policy on an OU reaches nested OUs; why the management account holds no workloads | Re | 1 | 0 | 1 |
| 05, "An SCP is a ceiling: it limits everyone in a member account, and grants nothing" | Member root limited; management account exempt; FullAWSAccess removed | Ap | 2 | 0 | 1 |
| 10 (S11), "Part 1: predict" | Every level must allow | Ap | 1 | 0 | 0 |
| 10 (S11), "Part 2: diagnose" | FullAWSAccess detached from an OU | Ap | 1 | 0 | 0 |
| 05, "SCP or IAM policy: a ceiling or a key" | Grants nothing; limits member root | Un | 1 | 1 | 0 |
| 05, "AWS Control Tower sets up and watches a multi-account environment, on top of Organizations" | Control Tower for a governed setup; proactive controls; vs Organizations | Ap, Re | 2 | 0 | 1 |
| 05, "Where AWS publishes security information" | Knowledge Center; Security Bulletins | Re, Un | 2 | 0 | 0 |
| 10 (S11), "Part 3: the bill" | What consolidated billing gives (task 4.2) | Un | 1 | 0 | 0 |
| **Total 09.05a** | | | **18** | **3** | **5** |

## 09.06a Assemble and justify layered controls [J·Ev] (lesson 09.06, tasks 2.1, 2.2 and 2.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 06, "Each layer stops different attacks" | Detective controls; layer and kind of a control | Un | 2 | 1 | 0 |
| 06, "Cover every threat with at least two layers: one that stops it and one that finds it" | A leaked key passes network filters; a prevention-only plan | Ap | 2 | 0 | 1 |
| 06, "The shared responsibility model holds at every layer" | Data and access stay the customer's (task 2.1) | Un | 1 | 0 | 1 |
| 06, "Worked example: the bakery's plan after a competitor's attack" | Shield Advanced covers one layer | Ap | 1 | 0 | 0 |
| **Total 09.06a** | | | **6** | **1** | **2** |

## Totals

| | Questions | Select TWO | Cards |
|---|---|---|---|
| 09.01a | 18 | 4 | 5 |
| 09.02a | 15 | 3 | 4 |
| 09.03a | 18 | 4 | 4 |
| 09.04a | 15 | 3 | 4 |
| 09.05a | 18 | 3 | 5 |
| 09.06a | 6 | 1 | 2 |
| **Module 09** | **90** | **18** | **24** |

Levels of the 90 questions: 14 recall (16%), 37 understanding (41%), 39 application (43%); the module
is "which service" heavy, so application runs above the 30% target. Tasks: 2.2 on 60, 2.4 on 20,
2.3 on 8, 2.1 on 1, 4.2 on 1. Single-answer correct positions: A 17, B 19, C 18, D 18; the correct
choice is the longest in 20 of 72.

Checks (2026-10-24): build clean; OpenWaymark lint 0 errors, 0 warnings; `check_items.py` 0
warnings and 0 notes on `q09-`/`c09-` items; dump similarity 270 of 270 wordings PASS.
