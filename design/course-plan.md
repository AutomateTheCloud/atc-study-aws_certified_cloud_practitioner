# Course plan: Automate the Cloud Study Guide for the AWS Certified Cloud Practitioner (CLF-C02) Exam

Design document for authors and reviewers. Drafted 2026-10-24.

- **Facts** come from the research repository (`study-aws-certified_cloud_practitioner`, docs 01,
  07, 10, 12, 13, 16 and 08-landscape), checked there on 2026-10-23 and 2026-10-24.
- **Owner decisions** are cited by their docs/13 numbers (A1–A9, B1–B11).

## 1. Outcome, reader and routing

**Outcome, in job terms.** By the end, a learner can work alongside technical and business teams on
cloud projects. They can:

- explain what moving to AWS changes for an organization and its costs;
- choose an AWS service for a stated need and defend the choice against the likely alternatives;
- say whether AWS or the customer is responsible for each security task, for the service in use;
- run an AWS account safely, with MFA-protected identities, least privilege, cost alerts, tagging
  and cleanup;
- estimate costs, read a bill, and know where to get help.

Passing CLF-C02 follows from this. The outcomes cover the exam's target candidate (up to six months
of AWS exposure) and add hands-on work, which the exam leaves out of scope.

**Reader statement** (every page carries its own version):

> An adult studying alone, possibly new to IT, who wants to understand AWS and use it safely, not
> only hold a certificate. About 5 hours a week for 12 weeks. A laptop or desktop for labs (reading
> works on a phone), an email address and a payment card.

The guide tells people who only want to memorize answers that it isn't built for them.

**Entry routing.** A diagnostic in Start here (about 15 items, 20 minutes) routes each learner to
one of three paths:

| Path | Who | What changes |
|---|---|---|
| On-ramp | Weak on IT basics (servers, networks, data, APIs) | Module 01 first; each page can be tested out of |
| Standard | Everyone else | Modules 02–14 in order |
| Fast path | Already works in IT or with AWS | Each module's mastery check is taken first as a pretest. Pass it and you skip the lessons, but still do the challenge-rung lab, spaced review and mixed practice |

On every path, the guardrails primer comes before Lab 01. No path skips practice or feedback. Start
here also asks learners to write a study plan (when, where and how long) and tells them plainly that
effective study feels harder than rereading.

## 2. Course map

Modules run simple → complex. Each opens with a scenario in its brief and ends by doing it.

**Numbering.** Lessons are `MM.PP`, and each lesson's objectives are `MM.PPa`, `MM.PPb`. Each
objective carries two tags:

- **Knowledge type:** F fact, C concept, P procedure, J judgment.
- **Thinking level:** Re recall, Un understand, Ap apply, An analyze, Ev evaluate.

| # | Module | Tasks | Hours | Lessons | Labs | Sims | Check items |
|---|---|---|---|---|---|---|---|
| 00 | Start here | — | 1 | — | — | — | diagnostic |
| 01 | On-ramp: IT foundations (optional) | prerequisites | 5 | 6 | — | — | per page |
| — | Guardrails primer (separate repository) | 2.3, 4.2 groundwork | 3–4 | 11 pages | — | — | — |
| 02 | Why organizations use the cloud | 1.1, 1.2, 1.4, 3.1 | 4 | 5 | 01 | S1 | 12 |
| 03 | AWS around the world | 3.2, 1.1 | 3 | 4 | 02 | S2 | 10 |
| 04 | Who secures what: shared responsibility and access | 2.1, 2.3 | 5 | 5 | 03, 04 | S3, S4 | 15 |
| 05 | Storing data: storage and databases | 3.6, 3.4, 4.1 | 4.5 | 6 | 05, 06 | S5, S6 | 15 |
| 06 | Running applications: compute | 3.3 | 3.5 | 4 | 07, 08 | S7 | 12 |
| 07 | Connecting it: networks and the edge | 3.5, 3.2, 4.1 | 3.5 | 4 | 09 | S8 | 12 |
| 08 | Building and operating | 3.1, 3.8, 2.2, 1.4 | 3.5 | 4 | 10, 11 | — | 12 |
| 09 | Protecting, governing and proving compliance | 2.2, 2.4, 2.3 | 5.5 | 6 | 12 | S9–S11 | 18 |
| 10 | Data, AI and the rest of the catalog | 3.7, 3.8 | 2.5 | 3 | 13, 14 | S12 | 10 |
| 11 | Paying for AWS | 4.1, 4.2, 1.4 | 4 | 4 | 15, 16 | S11, S13, S14 | 12 |
| 12 | Getting help | 4.3, 2.4, 3.8 | 3 | 4 | 17 | S15 | 10 |
| 13 | Moving to AWS | 1.3, 1.4 | 3.5 | 4 | — | S16, S17 | 12 |
| 14 | Capstone: a Well-Architected review | 1.2, all | 3 | — | 18, 19 | — | rubric |
| 90 | Exam preparation (written separately) | all | 8 | — | — | — | practice exams |

**Learner hours.** All are estimates until the pilot:

- Standard path: about 57 h, plus 3–4 h for the primer.
- On-ramp: about 5 h more.
- Fast path: about 25 h.
- At 5 h a week, the standard path takes 12–13 weeks, inside the Free plan's six months.

**Domain weights vs study time:**

| Domain | Exam weight | Study time |
|---|---|---|
| 1 | 24% | about 22% |
| 2 | 30% | about 28% (includes the "your side of the line" sections in 05–07) |
| 3 | 34% | about 37% |
| 4 | 12% | about 13% |

- **Domain 3 lessons** are short (about 25 minutes). The domain lists 111 services but draws only
  about 2 questions per task.
- **Domain 1 and 2 lessons** run about 35 minutes and carry more scenario practice.
- **Checks** are weighted to the blueprint, not to the number of lessons.

## 3. Threads that spiral through every module

| Thread | First taught | In every module | Ends in |
|---|---|---|---|
| Cost | 02.02 fixed vs variable | A "what you pay for" box in each service lesson; each lab's cost, worst case and cleanup check | 11; the 13 business case |
| Security and shared responsibility | 04.01 | A "your side of the line" section in each service lesson | 09.06 defense map; capstone |
| Well-Architected Framework | Primer page 00; formal in 02.05 | Each lesson's "in real work" names the pillar; each lab's "why this matters" cites one | 14 (WA Tool review) |
| Moving target and names | Start here | One dated-fact box per module; exam name plus today's name at first mention (docs/10 rule 1) | 12.02 Trusted Advisor (B3); 12.01 old-plans box (B5) |
| Lab habits | Primer page 07 | Region `us-east-1` (B10); tags `guide=clf`, `lab=NN` (B11); find, delete, next-day check | Lab 19 |

## 4. Modules and lessons

Every module has the same parts:

- **Brief:** scenario, tagged objectives, blueprint map, and "coming back" (topics reviewed from
  earlier modules).
- **Lessons.**
- **Lab ladder** (section 5).
- **Mastery check:** 80% to pass. Each miss points to the section to reread, followed by a parallel
  retest. Learners who pass first time get "going deeper" material.

### 01 On-ramp (optional)

Six concept lessons, each testable out:

- 01.01 Computers and servers
- 01.02 Networks, IP addresses, DNS and HTTPS
- 01.03 Files vs databases
- 01.04 Data centers and virtualization
- 01.05 APIs, the command line and JSON
- 01.06 Everyday security: passwords, MFA, encryption, least privilege

Objectives are [C·Un], except reading JSON, which is [P·Ap]. The final scope comes from the
prerequisites authors record while writing modules 02–04.

### 02 Why organizations use the cloud

**Scenario:** a bakery's ordering site crashes every holiday and sits idle in January. Write the
owner a one-page recommendation: should they move to the cloud, and what changes?

| Lesson | Covers | Objective |
|---|---|---|
| 02.01 What cloud computing is | On demand, over the internet, pay as you go; cloud, hybrid and on-premises deployment models | Classify a setup by deployment model [C·Ap] |
| 02.02 Before and after: the demand curve | The six advantages from one picture; fixed vs variable expense; economies of scale | Explain idle cost and lost sales from a demand curve [C·Ap] |
| 02.03 Telling the benefits apart | Elasticity, agility, high availability, durability, global reach | Name the benefit a scenario shows, and why not the others [C·An] |
| 02.04 What a data center really costs | On-premises cost categories (B4, our explanation); automation and rightsizing as ideas | Compare on-premises and pay-as-you-go costs in plain numbers [C·Ap] |
| 02.05 The Well-Architected Framework | Six pillars as six questions; design principles; trade-offs; the Framework vs the WA Tool | Match a concern to a pillar; explain a trade-off [C·An] |

### 03 AWS around the world

**Scenario:** the bakery sells in the US and Germany. German data must stay in the EU, and the site
must survive losing a data center. Choose Regions, the Availability Zone layout and a DR strategy.

| Lesson | Covers | Objective |
|---|---|---|
| 03.01 Regions, Availability Zones, data centers | An AZ is one or more data centers; at least three AZs per Region; no shared single points of failure | Explain how the three nest [C·Un] |
| 03.02 Choosing a Region | Latency, data sovereignty (B6), service availability, price | Choose and justify a Region [J·Ap] |
| 03.03 Surviving failure | High availability vs DR; RTO and RPO; the four DR strategies (A9); replication isn't backup | Choose a resilience approach from RTO, RPO and budget [J·Ev] |
| 03.04 The edge | Edge locations; CloudFront, Route 53, Global Accelerator (preview of 07.03); Local Zones; Outposts; Wavelength as an out-of-scope distractor | Say where each runs and what it's for [C·Un] |

### 04 Who secures what: shared responsibility and access

**Scenario:** give a new teammate access to the site's storage and nothing else, and prove it
works. Then explain who patches what for the server, the database and the functions.

| Lesson | Covers | Objective |
|---|---|---|
| 04.01 Security of vs in the cloud | AWS's own framing (B1); the line moves for EC2, RDS, Lambda and S3, using AWS-published statements only; data and access are always the customer's | Say who does a task for a given service, and why [C·Ap] |
| 04.02 Shared, inherited, customer-specific | Patching, configuration and training: each side in its own context | Explain "shared" with examples [C·Un] |
| 04.03 Identities | Authentication vs authorization; root, users, groups, roles; the current root-only tasks; protecting root (link to primer page 02) | Pick the identity for a case [C·Ap]; recognize root-only tasks [F·Re] |
| 04.04 Policies and least privilege | Identity vs resource policies; managed vs inline; default deny; an explicit deny wins | Predict allow or deny [P·An] |
| 04.05 Credentials and federation | MFA, password policy, why to avoid access keys, temporary credentials; Secrets Manager vs Parameter Store; Identity Center, federation, cross-account roles, Cognito, Directory Service; why our labs use an IAM user (B8) | Choose a credential store and an identity approach [J·Ap] |

### 05 Storing data: storage and databases

**Scenario:** place the bakery's orders, photos, nightly backups and seven-year tax archives. Set
lifecycle rules, and pick a database for orders and another for carts.

| Lesson | Covers | Objective |
|---|---|---|
| 05.01 Block, file, object | EBS, instance store, EFS, FSx, S3; durability vs availability | Choose a storage type for an access pattern [C·Ap] |
| 05.02 S3 in practice | Block Public Access, versioning, default encryption; your side of the line | Explain how each protects data [C·Un] |
| 05.03 Storage classes and lifecycle | Classes on a hot-to-cold chart; minimum durations, minimum billable size, retrieval fees; S3 Glacier classes vs closed Glacier vaults | Choose a class and lifecycle rule, avoiding cost traps [J·Ap] |
| 05.04 Hybrid storage and backup | Storage Gateway (S3 File, Volume, Tape); AWS Backup; Elastic Disaster Recovery; snapshots | Match a need to a service [C·Ap] |
| 05.05 Managed or self-managed databases | A database on EC2 vs RDS (AWS's responsibility table); Aurora; Multi-AZ vs read replica vs snapshot | Choose hosting, and HA vs read scaling [J·Ap] |
| 05.06 Choosing a database | By data shape: RDS/Aurora, DynamoDB, ElastiCache, DocumentDB, Neptune; Redshift is analytics; DMS vs SCT | Pick a database for a data shape [J·Ap] |

### 06 Running applications: compute

**Scenario:** choose compute for a spiky order site, a nightly image-resize job and a containerized
inventory app. Explain how each scales and who patches it.

| Lesson | Covers | Objective |
|---|---|---|
| 06.01 EC2 | Instances, AMIs, families by bottleneck; instance types aren't purchasing options | Choose a family from a bottleneck [C·Ap] |
| 06.02 Auto Scaling and load balancers | Auto Scaling sets how many; ELB spreads traffic; ALB, NLB, GWLB; Classic is previous generation | Explain elasticity plus high availability [C·Un] |
| 06.03 Containers and serverless | ECS, EKS, Fargate, ECR, Lambda; what you manage at each step | Pick EC2, Fargate or Lambda, and say what you manage [J·Ap] |
| 06.04 Simpler paths | Elastic Beanstalk, Lightsail, Batch, Outposts | Match each to its use [C·Ap] |

### 07 Connecting it: networks and the edge

**Scenario:** design the network: a public web tier and a private database. Block a bad IP range,
link head office securely, and serve photos from a CDN.

| Lesson | Covers | Objective |
|---|---|---|
| 07.01 Your own network | VPC; one AZ per subnet; route tables; internet gateway; NAT gateway and its cost; endpoints | Explain what makes a subnet public [C·An] |
| 07.02 Filtering traffic | Security groups (stateful) vs NACLs (stateless); the packet's path; Inspector reports, it doesn't filter | Predict whether traffic passes [P·An] |
| 07.03 Names and the edge | Route 53, CloudFront, Global Accelerator, API Gateway | Choose for a need [C·Ap] |
| 07.04 Connecting networks and offices | Site-to-Site VPN, Client VPN, Direct Connect; peering, Transit Gateway, PrivateLink; data transfer costs (A1, dated) | Choose a link by private, encrypted and setup speed [J·Ap] |

### 08 Building and operating

**Scenario:** rebuild the setup identically in a second Region, and email the owner when orders
fail. Choose how to provision, how to alert, and how the parts should communicate.

| Lesson | Covers | Objective |
|---|---|---|
| 08.01 Four ways in | Console, CLI, SDKs, infrastructure as code; one-time vs repeatable; CloudShell | Choose the method for a task [J·Ap] |
| 08.02 IaC and automation | CloudFormation; Service Catalog; benefits of automation (1.4) | Explain how IaC makes work repeatable and cheaper [C·Un] |
| 08.03 Watching workloads | CloudWatch metrics, logs and alarms; X-Ray; how both differ from CloudTrail | Pick the tool for an operations question [C·Ap] |
| 08.04 Connecting parts, shipping software | SNS, SQS, EventBridge, Step Functions, SES; CodeBuild, CodePipeline; CodeDeploy is out of scope; Cloud9 is closed to new customers (A6) | Choose by message shape; name the build or release tool [C·Ap] |

### 09 Protecting, governing and proving compliance

**Scenario:** an auditor arrives the week a competitor suffers a DDoS attack. Answer five evidence
questions, and choose layered protections for the site.

| Lesson | Covers | Objective |
|---|---|---|
| 09.01 Who did what, how it runs, how it was set | CloudTrail, CloudWatch, Config; where security logs live; access reports (A4) | Choose the service for an audit question [C·An] |
| 09.02 Encryption | At rest vs in transit; KMS, CloudHSM, ACM; who holds the key; Macie | Choose an encryption and key approach [J·Ap] |
| 09.03 Finding threats and weaknesses | GuardDuty, Inspector, Security Hub (CSPM vs the new unified product), Detective; Trusted Advisor security checks; Marketplace products | Match a finding to its service [C·Ap] |
| 09.04 The front door | Shield and the Shield Response Team (B2, dated); WAF; Firewall Manager; penetration-testing policy (A3) | Choose protections for an attack type [J·Ap] |
| 09.05 Compliance and governance | Artifact; compliance programs and services in scope; Organizations, SCPs, Control Tower; where AWS publishes security information | State the customer's remaining duty; explain an SCP as a ceiling [C·Ap] |
| 09.06 A defense map | Layers from the edge to the organization; shared responsibility recap | Assemble and justify layered controls [J·Ev] |

### 10 Data, AI and the rest of the catalog

**Scenario:** the owner has six requests: a sales dashboard, a phone bot, spoken product
descriptions, receipts turned into text, desktops for seasonal staff, and freezer sensors. Match
each to a service.

| Lesson | Covers | Objective |
|---|---|---|
| 10.01 Analytics in five verbs | Ingest (Kinesis, Data Firehose), catalog (Glue), query (Athena, Redshift, EMR), search (OpenSearch), visualize (Quick Sight) | Place services in a pipeline [C·Ap] |
| 10.02 AI and ML | An input → output grid; SageMaker AI vs ready-made services; Amazon Q Developer; Q Business is closed to new customers | Choose by input and output [C·Ap] |
| 10.03 People, apps and devices | WorkSpaces; AppStream 2.0 (now WorkSpaces Applications); Secure Browser (closed to new customers from 2026-10-29); Connect (now Connect Customer); SES; Amplify; IoT Core | Match a need to a service [C·Ap] |

### 11 Paying for AWS

**Scenario:** the bill has grown. Explain it, cut it, estimate a new feature, and give each of three
teams a view of its own costs.

| Lesson | Covers | Objective |
|---|---|---|
| 11.01 How AWS charges | Cost drivers; data transfer by direction (A1, dated). The Free Tier now: Free and Paid plans, credits, two clocks (plan 6 months, credits 12; checked 2026-10-23). A box for older "12 months free" material | Identify what drives a bill [C·Ap] |
| 11.02 Purchasing options | On-Demand; Savings Plans (four types); Reserved Instances (Standard and Convertible, zonal and Regional, size flexibility); Spot; Dedicated Hosts and Instances; Capacity Reservations | Choose an option for a usage pattern [J·Ap] |
| 11.03 Estimate, watch, analyze | Pricing Calculator; Budgets (they alert, they don't cap, unless actions are set); Cost Explorer; Anomaly Detection; CUR via Data Exports | Pick the tool for each stage [C·Ap] |
| 11.04 Many accounts, one bill | Consolidated billing; RI and Savings Plans sharing; cost allocation tags (two types, must be activated, not retroactive) | Explain who gets a discount, and how tags reach reports [C·An] |

### 12 Getting help

**Scenario:** the site is becoming business-critical. Recommend a Support plan, and route five
issues: a billing question, a how-to, a design review, abuse from an AWS IP address, and an AWS
outage.

| Lesson | Covers | Objective |
|---|---|---|
| 12.01 Support plans | Basic, Business Support+, Enterprise, Unified Operations (A2, dated); response times are targets, not guarantees; old-names box (B5) | Choose the cheapest plan that fits [J·Ap] |
| 12.02 Tools that watch your account | Trusted Advisor categories and plan access, with no check count (B3; the course's main "moving target" example); Health Dashboard vs Health API; Support Center | Say what each shows and who gets it [C·Un] |
| 12.03 Where to find answers | Documentation, whitepapers, blogs, re:Post, Knowledge Center, Prescriptive Guidance; Trust & Safety for abuse | Route a question [C·Ap] |
| 12.04 Partners and paid help | Partner Network (ISVs, system integrators); partner benefits (B6); Marketplace (cost, governance, entitlement); Professional Services; solutions architects | Choose the right kind of help [C·Ap] |

### 13 Moving to AWS

**Scenario:** a chain buys the bakery and runs ten applications on-premises. Build the case: CAF
outcomes, a strategy for each application, the tools, and costs including licensing.

| Lesson | Covers | Objective |
|---|---|---|
| 13.01 The Cloud Adoption Framework | Outcomes, perspectives, transformation domains, phases | Map a concern to a perspective [C·Ap] |
| 13.02 Seven migration strategies | The 7 Rs, with AWS's criteria | Assign and justify a strategy per application [J·An] |
| 13.03 Migration tools | Migration Evaluator; Discovery Service and Migration Hub (both closed to new customers; AWS points to AWS Transform); Application Migration Service (now AWS Transform MGN); DMS and SCT; contrast with Elastic Disaster Recovery | Choose a tool for a job [C·Ap] |
| 13.04 The business case | On-premises vs AWS costs; BYOL vs license-included; rightsizing with Compute Optimizer; no TCO Calculator (A7) | Build a cost comparison and make a licensing decision [J·Ev] |

### 14 Capstone

**Scenario:** review the workload you built in labs 05–11 against the six pillars. List its
high-risk issues, cost the fixes, and recommend a Support plan.

The capstone is scored with a rubric. It goes beyond the blueprint.

## 5. Lab ladder

**Rungs:**

- L1 follow-along
- L2 completion
- L3 challenge
- L4 break-fix (optional)

**Free plan column:** whether the lab works on the advanced sign-up path on the Free plan.

**Cost column:**

- On the Free plan, usage comes out of credits, and the learner can't be billed without upgrading
  (as of 2026-10-23).
- Each lab still states its worst case in dollars for learners on a Paid plan.
- "Low" means cents, or within an always-free allowance.

**Sim (S1–S17):** a simulation we build. Each one has a static fallback, so it works in all three
editions.

| Lab | Module | Rung | What the learner does | Free plan | Mode | Cost |
|---|---|---|---|---|---|---|
| 01 | 02 | L1 | Create an empty tagged bucket and time it (agility); find it by tag and in CloudTrail; delete it | Yes | Real | $0 |
| S1 | 02 | L2 | Demand-curve explorer: finish the bakery's cost comparison | — | Sim | $0 |
| 02 | 03 | L1 | Region selector; AZ names vs AZ IDs in CloudShell; Health Dashboard | Yes | Real, read-only | $0 |
| S2 | 03 | L2–L3 | Blast-radius ladder; pick DR strategies for three businesses | — | Sim | $0 |
| 03 | 04 | L1 | Group plus customer-managed policy for lab-tagged buckets; test it in the policy simulator | Yes (not on the new path) | Real | $0 |
| 04 | 04 | L2–L4 | Finish a policy and validate it with Access Analyzer; write one for the scenario; find a blocking explicit deny | Yes | Real | $0 |
| S3, S4 | 04 | L2 | Responsibility slider (on-premises → S3); policy-evaluation playground, including Identity Center and cross-account roles (an organization instance would upgrade the Free plan) | — | Sim | $0 |
| 05 | 05 | L1–L3 | Versioning; overwrite, delete and restore; lifecycle rule; delete all versions; then configure the archive bucket from requirements alone | Yes | Real | Low |
| 06 | 05 | L1 | DynamoDB table: put and get items, then delete | Yes | Real | Low |
| S5, S6 | 05 | L2 | Lifecycle cost timeline; RDS Multi-AZ failover vs read replica (RDS bills hourly) | — | Sim | $0 |
| 07 | 06 | L1 | Lambda function, test event, log retention | Yes | Real | Low |
| 08 | 06 | L1–L3 | Launch one eligible instance for at most 30 minutes: public IPv4, stop vs terminate, volume gone | Yes | Real | Medium: hourly, from credits |
| S7 | 06 | L2 | Elasticity with Auto Scaling and an ALB (an ALB bills hourly) | — | Sim | $0 |
| 09 | 07 | L1–L2 | VPC with two subnets in two AZs, an internet gateway route, security group and NACL rules; delete | Yes | Real | $0 with no NAT gateway and no Elastic IP |
| S8 | 07 | L3–L4 | Packet journey; find the blocking rule | — | Sim | $0 |
| 10 | 08 | L1–L2 | Same bucket three ways: console, CLI, and a CloudFormation template the learner completes; delete the stack | Yes | Real | Low |
| 11 | 08 | L3 | SNS email topic plus a CloudWatch alarm on Lab 07's errors; trigger it; clean up | Yes | Real | Low |
| 12 | 09 | L1–L3 | CloudTrail queries on earlier labs; IAM last-accessed; S3 encryption; one Artifact report (accept no agreements); answer the auditor | Yes | Real | $0 |
| S9–S11 | 09, 11 | L2 | Security findings tour (GuardDuty and Security Hub CSPM were blocked on the Free plan, 2026-10-23); Config timeline; Organizations, SCPs and consolidated billing | — | Sim | $0 |
| 13 | 10 | L1 | Athena query on a 1 KB CSV | Confirm on a fresh account | Real | Low |
| 14 | 10 | L1, optional | Polly text to speech (the console opened on the Free plan, 2026-10-23) | Confirm | Real | Low |
| S12 | 10 | L2–L3 | Input → output matcher (Comprehend was blocked on the Free plan) | — | Sim | $0 |
| 15 | 11 | L1–L3 | Pricing Calculator: price a setup, remove hourly items, compare purchasing options | Yes (web tool) | Real | $0 |
| 16 | 11 | L1 | Activate `guide` and `lab` as cost allocation tags; check Cost Explorer the next day | Yes | Real | $0 |
| S13, S14 | 11 | L2–L3 | Purchasing-option tree (commitments aren't available on the Free plan); guardrail timeline (alerts vs stops) | — | Sim | $0 |
| 17 | 12 | L1–L3 | Support Center case types on Basic; Health Dashboard; free Trusted Advisor checks mapped to pillars; one Knowledge Center article; one Marketplace listing, no subscription | Yes | Real | $0 |
| S15 | 12 | L3 | Support plan chooser | — | Sim | $0 |
| S16, S17 | 13 | L2–L3 | 7 Rs portfolio sorter; rightsizing and licensing trees. No real lab: DMS bills, and the discovery tools are closed | — | Sim | $0 |
| 18 | 14 | L3 | Well-Architected Tool review of the lab workload; save a milestone; delete the workload | Yes | Real | $0 |
| 19 | 14 | L1 | Close-out: sweep all Regions by tag; next-day bill check; optional account closure (primer page 09) | Yes | Real | $0 |

## 6. Spaced review and practice

**Spaced review.** Each lesson's warm-up draws on three earlier points:

- the previous module (about one week back);
- one module two to four back;
- one topic from modules 02–04.

| Module | Reviews | Module | Reviews |
|---|---|---|---|
| 03 | 02 | 09 | 08, 07, 04 |
| 04 | 03, 02 | 10 | 09, 05, 02 |
| 05 | 04, 03, 02 | 11 | 10, 06, 05, 02 |
| 06 | 05, 04, 02 | 12 | 11, 09, 02 |
| 07 | 06, 05, 03 | 13 | 12, 11, 04 |
| 08 | 07, 06, 04 | 14 | everything |

Mixed cumulative sets follow modules 05, 09 and 13. An item stays in rotation until it has been
answered correctly in several separate sessions.

**Practice and who writes it.** Lessons carry only the in-lesson items. A separate assessment
effort writes everything else later. That effort works clean-room from the blueprint and our
lessons, follows the skill's assessment notes, and runs the similarity checker before release.

| Practice | Where | Writer | Must cover |
|---|---|---|---|
| "Your turn" tasks and checks | Each section | Lesson author | The section's objective at its level; a model answer or per-option feedback |
| Retrieval | End of each lesson | Lesson author | 3–5 items on the lesson; 1–2 from the review table |
| Diagnostic | 00 | Assessment | IT basics (on-ramp routing); one item per module (fast path) |
| Mastery check and parallel retest | `NN-check` page | Assessment | Every objective at its level; scenarios for Ap and higher; the module's confused pairs (section 7); a correction map; enrichment |
| Mixed sets | After 05, 09, 13 | Assessment | Interleaved, weighted by domain |
| Practice exams | 90 | Assessment | At least two full forms in exam format (as of 2026-10-23: 65 items, 90 minutes, single and multiple response, weighted 24/30/34/12). Readiness scored only on unseen items, as a range per domain. Never claims to predict a score |
| Flashcards (optional) | Per module | Assessment | Root-only tasks (including "changing the Support plan isn't root-only"), old vs new names, the AI input → output grid, "why" cards |

## 7. Misconceptions and confused pairs, by module

These come from the research landscape analysis and docs/13. Each misconception gets a refutation
in its lesson, and each pair gets a side-by-side comparison that returns in mixed practice.

| Module | Refute | Compare |
|---|---|---|
| 02 | "Scalability is manual, elasticity automatic." The cloud always cuts operating cost (it makes fixed cost variable). "Geographic diversity", "design for failure" or "think parallel" are Framework principles. There are five pillars. "Public, private, community" are the deployment models | Elasticity, agility, availability, durability; fixed vs variable; cloud, hybrid, on-premises; reliability vs performance efficiency; cost optimization vs sustainability; Framework vs WA Tool |
| 03 | An AZ is one data center. A Region can have two AZs. High availability = DR. Replication replaces backup. Region counts are worth memorizing | Region, AZ, edge location, Local Zone, Outposts; HA vs DR; RTO vs RPO |
| 04 | Changing the Support plan needs root. Access keys are the normal way to use the CLI. "AWS Single Sign-On" (renamed 2022-07-26). "Shared" means both sides do the same task. Root MFA is optional. `AdministratorAccess` equals root | Of vs in; the three control types; user, group, role; managed vs inline; identity vs resource policy; IAM, Identity Center, Cognito, Directory Service; Secrets Manager vs Parameter Store |
| 05 | Largest S3 object is 5 TB (50 TB per the S3 FAQ, 2026-10-23). Standard-IA has Standard's availability. Glacier vaults = S3 Glacier classes. Instance store survives a stop. A read replica gives high availability. Snowball is current | Block, file, object; EBS vs instance store; EFS vs FSx; the IA classes; the three Glacier classes; Backup vs Elastic Disaster Recovery vs snapshots; the seven database services; Multi-AZ vs read replica; DMS vs SCT |
| 06 | On-Demand, Reserved and Spot are instance types. Fargate orchestrates. Auto Scaling spreads traffic. Classic Load Balancer is a current-generation peer of ALB. A stopped instance costs nothing | Instance families; ECS, EKS, Fargate, ECR; Lambda vs Fargate; Auto Scaling vs ELB; ALB, NLB, GWLB; EC2, Beanstalk, Lightsail |
| 07 | A public IP makes a subnet public. A VPN is private (it's encrypted, over the internet). Return traffic always passes (a NACL can block it). Route 53 is a CDN. A NAT gateway is free | Security group vs NACL; internet gateway vs NAT; gateway vs interface endpoint; peering, Transit Gateway, PrivateLink; VPN vs Direct Connect; CloudFront vs Global Accelerator |
| 08 | Console clicks are fine for production. CodeDeploy, Cloud9 or OpsWorks are current answers (A5, A6). An SNS email is SES | Console, CLI, SDK, IaC; SNS, SQS, EventBridge, Step Functions; CodeBuild vs CodePipeline; X-Ray, CloudWatch, CloudTrail |
| 09 | Inspector "assessment templates" (Inspector Classic, shut down 2026-05-20). Audit Manager is the compliance answer. Security Hub is one product. Artifact checks *your* compliance. Not in "services in scope" = can't use. Trusted Advisor has five categories. Any "Business" Support plan brings the Shield Response Team (it also needs Shield Advanced, and AWS's page still names the retiring Business plan; B2) | CloudTrail, CloudWatch, Config; GuardDuty, Inspector, Macie, Detective, Security Hub; Shield, WAF, Firewall Manager; KMS vs CloudHSM; ACM vs KMS; at rest vs in transit; SCP vs IAM policy; Organizations vs Control Tower |
| 10 | Old names as current: SageMaker, QuickSight, Kinesis Data Firehose, WorkSpaces Web, AppStream 2.0. Kendra or Kinesis Data Analytics as answers. Amazon Q is one product | Athena, Redshift, EMR, Glue; Data Streams, Firehose, SQS; Comprehend, Textract, Rekognition; Polly, Transcribe, Translate, Lex; SageMaker AI vs ready-made AI; WorkSpaces, Applications, Secure Browser; Connect vs Lex |
| 11 | "12 months free." Two Savings Plans types. "Up to 75%." Only "in free, out charged." A 12-month forecast. Budgets cap spending. A tag alone shows costs. Capacity Reservations discount. An RI is a machine | Savings Plans vs RIs; Compute vs EC2 Instance plans; Standard vs Convertible; zonal vs Regional; Dedicated Host vs Instance; Budgets, Cost Explorer, CUR, Pricing Calculator; the two tag types |
| 12 | The legacy plans are current. Response times are guaranteed. Basic gets a fixed number of checks. Personal and Service Health Dashboards are separate products. Abuse goes to Support | The four plans; re:Post, Knowledge Center, Prescriptive Guidance, Support Center; Professional Services, partners, Support, solutions architects; Health Dashboard vs Health API |
| 13 | Use the TCO Calculator (A7). Six Rs. The CAF perspectives include "process" (that's a transformation domain). Snowball migrates. The discovery tools are open to new customers | CAF vs 7 Rs; Business vs Governance perspective; rehost, replatform, refactor, relocate; MGN vs DMS; MGN vs Elastic Disaster Recovery; license-included vs BYOL |

## 8. Coverage matrix

**Exam ≈:** weight × 50 scored items, split evenly across each domain's tasks.

**Objectives:** the IDs of the lessons in section 4.

**Checks:** module mastery checks (C*nn*). Every task also appears in the mixed sets and the
practice exams.

| Task | Exam ≈ | Lessons | Labs and sims | Checks |
|---|---|---|---|---|
| 1.1 Cloud benefits | 3 | 02.01–02.03, 03.01–03.03, 06.02 | 01, 02; S1, S2, S7 | C02, C03, C06 |
| 1.2 Well-Architected | 3 | 02.05; the pillar link in every lesson; 12.02 | 17, 18 | C02, C12, capstone |
| 1.3 Migration | 3 | 13.01–13.03, 05.06 | S16 | C13 |
| 1.4 Cloud economics | 3 | 02.02, 02.04, 08.02, 11.01, 13.04 | 15; S1, S17 | C02, C08, C13 |
| 2.1 Shared responsibility | 3.75 | 04.01–04.02; "your side" sections in 05–07; 09.06 | S3; reflections in 05, 07, 09 | C04–C07, C09 |
| 2.2 Security and compliance concepts | 3.75 | 09.01–09.03, 09.05, 05.02, 08.03 | 11, 12; S9, S10 | C08, C09 |
| 2.3 Access management | 3.75 | 04.03–04.05, 09.05 | 03, 04; S4, S11 | C04, C09 |
| 2.4 Security resources | 3.75 | 09.03–09.05, 12.03 | 12, 17; S9 | C09, C12 |
| 3.1 Deploying and operating | 2 | 02.01, 08.01–08.02 | 10 | C02, C08 |
| 3.2 Global infrastructure | 2 | 03.01–03.04, 07.03 | 02; S2 | C03, C07 |
| 3.3 Compute | 2 | 06.01–06.04 | 07, 08; S7 | C06 |
| 3.4 Databases | 2 | 05.05–05.06, 13.03 | 06; S6 | C05, C13 |
| 3.5 Networking | 2 | 07.01–07.04 | 09; S8 | C07 |
| 3.6 Storage | 2 | 05.01–05.04 | 05; S5 | C05 |
| 3.7 AI/ML and analytics | 2 | 10.01–10.02 | 13, 14; S12 | C10 |
| 3.8 Other categories | 2 | 08.04, 10.03, 12.01 | 11 | C08, C10, C12 |
| 4.1 Pricing models | 2 | 11.01–11.02, 05.03, 07.04 | 15; S5, S13 | C05, C07, C11 |
| 4.2 Billing and cost tools | 2 | 11.03–11.04 | 15, 16; S11, S14; primer page 05 | C11 |
| 4.3 Resources and Support | 2 | 12.01–12.04 | 17; S15 | C12 |

**Beyond the blueprint, labeled as such:** hands-on implementation, the on-ramp, the capstone, and
the "going deeper" boxes.

## 9. File layout, page types and naming

```
guide/
  README.md                       contents; the source of every edition's table of contents
  00-start-here/                  01-welcome … 05-diagnostic, 06-before-your-first-lab
  01-on-ramp/                     01-computers-and-servers … 06-everyday-security
  02-why-the-cloud/
    00-brief.md                   module brief
    01-what-cloud-computing-is.md concept lesson
    06-lab-01-first-resource.md   lab; the number matches the lab=NN tag
    07-sim-demand-curve.md        simulation page with a static fallback
    08-check.md                   mastery check (items come later)
  03-… through 14-capstone/
  90-exam-prep/                   mixed sets, practice exams
  98-how-to/                      task cards
  99-reference/                   names, glossary, commonly confused, service map, cost traps, blueprint map
images/                           MM-PP-descriptor.svg|png
diagrams/                         diagram sources (AWS Icons for PlantUML only)
source/sims/<slug>/               interactive simulations (Apache-2.0)
```

**Page types:**

| Type | Pages |
|---|---|
| Concept lesson | Every lesson in section 4 |
| Lab | Labs 01–19, and sims with `mode: sim` |
| Task card | `98-how-to/`, for example: switch to `us-east-1`; empty a versioned bucket; find a lab's events in CloudTrail |
| Reference | `99-reference/`, and the exam-at-a-glance page |
| Module brief and check pages | Use the skill's brief template |

**Naming that works in all three editions:**

- Lowercase ASCII with hyphens.
- The two-digit prefix gives reading order, so the GitHub listing matches the book.
- The folder number is the module number in this plan, in IDs, in URLs and in PDF chapters.
- A stable front-matter `id` (`clf-05-03`) survives any rename. Published slugs never change; the
  site keeps redirects.
- Links are relative `.md` links, which the builds rewrite.
- Headings are unique within each page, so anchors work.
- Every page stands alone as a web page.

**Front matter:**

- Every page: `type`, `id`, `tasks`, `objectives`, `reader`, `prerequisites`, `terms_introduced`,
  `pillars`, `facts_checked`, `sources`, `reviewed`.
- Labs add: `lab`, `rung`, `mode`, `free_plan`, `signup_path`, `time`, `cost`, `worst_case`,
  `needs`, `last_run_pass`.

**Every lab:**

- opens with the docs/13 liability notice, word for word;
- links the primer pages it relies on;
- tags every resource it creates;
- uses `us-east-1`;
- has a sidebar for learners on the new sign-up path.

**Every lesson** ends with the playbook's attribution line. **Every edition's front matter** carries
the liability and trademark notices.

## 10. How it would run

| Item | Plan |
|---|---|
| Delivery | Self-paced and solo-complete. Three editions built from one Markdown source. No instructor |
| People | Lead author (the owner), with skill-guided drafting. AWS technical reviewer. Editor (style and accessibility). At least 5 target readers per lesson for paraphrase tests, including IT newcomers. Lab tester with fresh Free plan accounts. Front-end developer for sims. Site and PDF build engineer. The assessment effort |
| Learner needs and cost | A computer, an email address and a payment card (USD 1 held for 3–5 days). $0 expected on the Free plan: labs draw on credits ($100, plus $20 for creating a budget, as of 2026-10-23). Exam: USD 100 (as of 2026-10-23) |
| Free plan clock | The account closes six months after sign-up, or sooner if the credits run out. Learners open it at Lab 01, not before. Every lab can be redone in a fresh account after the primer |
| Build first | 1. Conventions: the front-matter schema, a lab conventions page, `99-reference/names-exam-vs-current` and a glossary seed. 2. A pipeline proof: one lesson, one lab and one sim fallback built as Markdown, site and PDF. 3. The pilot module |
| Evaluation | Pre- and post-scores on checks; performance on unseen items; item statistics; a reader pilot per module. Satisfaction and completion are not used as goals |

| Risk | Response |
|---|---|
| AWS changes names, plan rules or consoles | Facts dated with `facts_checked`; one names reference; labs re-run before each release; console labels hedged in the step that uses them |
| The live exam lags the 2026 guide (which names live items use is UNVERIFIED) | The B5 old-names box and the names reference teach both lineups |
| Accidental plan upgrade or credit burn | Primer first; cost box and "don't click Upgrade" in every lab; anything billed by the hour is simulated |
| Learner signed up on the new path | Per-lab sidebar (docs/12 A/N column); sim fallbacks for labs 03, 04, 17 and 18 |
| Sims are expensive to build | Static fallbacks ship first; build interactive S3, S8, S13 and S14 first |
| Errors in misconception lists and diagrams | A dedicated expert review pass |
| Overbuilding across 111 services | One line per service in the service map; depth only where the blueprint names a skill |
| Low self-paced completion | An early win (Lab 01 in the first session); modules with their own end points; the study-plan prompt |

**Update plan.** An editorial calendar from docs/10, re-checked before each release:

| Date | Change | Update |
|---|---|---|
| 2026-10-29 | WorkSpaces Secure Browser closes to new customers | 10.03 |
| 2026-12-31 | Snowball support ends | Distractor notes in 05 and 13 |
| 2027-01-01 | Developer, Business and Enterprise On-Ramp Support plans end | 12.01 old-names box; the B2 note in 09.04; the reference pages |
| 2027-04-30 | Q Developer IDE plugins reach end of support | 10.02 |
| 2027-06-30 | re:Post Private ends | 12.03 |

**Recurring checks:**

- **Quarterly:** re-check the Free plan pages and Support plan pages.
- **After a console change:** re-run the affected labs on a fresh account and log the result.
- **Exam guide:** watch AWS's exam-guide index for a revision or a successor exam, then update this
  matrix.
- **Each edition:** a version number, a changelog and an errata page.

## 11. Writing order

1. **The spine:** conventions, the names reference, the glossary seed and the pipeline proof.
2. **Module 04, written first as the pilot.**
   - **Why first:** Domain 2 is the heaviest per task, and 2.1 is the least served elsewhere. Its
     labs are real and free and build straight on the primer. It uses every page type, a sim and
     the full lab ladder, and nothing in it changes on 2027-01-01.
   - **Pilot:** test it with at least 5 readers and an expert, run its labs on a fresh account, then
     fix the templates.
3. **00 Start here and 02**, with the on-ramp pages scoped from the prerequisites recorded while
   writing 04 and 02.
4. **03, 05, 06 and 07.** Run labs 02 and 05–09 as one chain in a fresh account.
5. **08 and 09.**
6. **10.**
7. **11 and 13.**
8. **12**, finished after 2027-01-01, so the old-names box can say the legacy plans have ended.
9. **14 and 99-reference**, completed from the finished modules.
