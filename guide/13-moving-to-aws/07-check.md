---
type: check
id: clf-13-07
title: "Module 13 mastery check"
tasks: ["1.3", "1.4"]
objectives: ["13.01a", "13.02a", "13.03a", "13.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 13's lessons; about 40 minutes for Check A"
prerequisites: [clf-13-01, clf-13-02, clf-13-03, clf-13-04]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://aws.amazon.com/application-migration-service/"
  - "https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html"
  - "https://aws.amazon.com/snowball/"
  - "https://aws.amazon.com/migration-evaluator/faqs/"
  - "https://aws.amazon.com/windows/resources/licensing/"
  - "https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing.html"
---

# Module 13 mastery check: map the concern, choose the strategy and the tool, and defend the cost case

This check tests whether you can do what Module 13 set out to teach: map a concern to a perspective of the AWS Cloud Adoption Framework, choose and justify a migration strategy, choose a migration tool, and judge a cost comparison and a licensing decision. Every question is a short situation, like the ones on the exam.

**For:** an adult studying alone, possibly new to IT, who has finished the four lessons of [Module 13](00-brief.md). **Time:** about 40 minutes for Check A, and the same for Check B if you need it.

## How to use this check

Take **Check A** closed-book: no lessons, notes or AWS pages. Answer all twelve questions, then open the answers and count your score. A "(Select TWO.)" question counts as right only if you chose both correct answers, as on the exam. You pass at **80%**, which here is 10 of 12.

- **If you scored 10 or more:** you have passed. Read the feedback on anything you missed, then try the [enrichment tasks](#enrichment-for-learners-who-passed).
- **If you scored less than 10:** use the [correction map](#correction-map) to reread the exact section behind each miss, and redo the simulation it names. Then take [Check B](#check-b-parallel-retest), which asks about the same objectives with new situations.

The questions use the exam's service names. Where AWS has renamed or closed a service since, the feedback says so, with the date we checked.

## Check A

**A1.** A hotel group is halfway through its migration to AWS. Its chief information security officer has been asked to keep the program's risk register: every risk to the migration's schedule, budget and promised benefits, each with an owner, reviewed every month. Which perspective of the AWS Cloud Adoption Framework (AWS CAF) does this work belong to?

- **A.** Security
- **B.** Business
- **C.** Governance
- **D.** Operations

<details><summary>Answer</summary>

**C is right.** Managing the risks to the transformation program is Governance's risk management capability, beside program and project management and benefits management. What's at stake is the program, not the protection of data or systems.

- **A is wrong.** The person asking leads security, but a job title doesn't decide the perspective. Security protects data, identities and systems; these risks are to the schedule, the budget and the benefits.
- **B is wrong.** Business decides what to change and whether it's worth it. The move is already decided; this is about overseeing how it goes.
- **D is wrong.** Operations keeps running services healthy, not the migration program.

</details>

**A2.** The head of an insurer's claims department asks: "When the claims service fails at night, how will we record the incident, escalate it, restore the service, and then find the root cause so that the same failure doesn't come back?" Which AWS CAF perspective deals with this concern?

- **A.** Operations
- **B.** Security
- **C.** Platform
- **D.** People

<details><summary>Answer</summary>

**A is right.** Keeping a service running at the level the business agreed, through incident and problem management, is the Operations perspective. The person asking runs a business department, but what's at stake is the health of a running service.

- **B is wrong.** Security has a capability called incident response, but it's for security events. A service failing at night, with no attack involved, is an Operations incident. The word "incident" alone doesn't decide it.
- **C is wrong.** Platform builds and standardizes the environment; it doesn't run incidents.
- **D is wrong.** People covers skills, roles and culture.

</details>

**A3.** A transport company has finished its CAF Align workshops. Its migration lead must now decide, application by application, which of the company's 50 applications to retire, rehost or replatform, and group the results into a business case. Where does this work sit?

- **A.** In the CAF's Process perspective
- **B.** In a Well-Architected review, pillar by pillar
- **C.** In the CAF's Scale phase, after the pilots
- **D.** In the 7 Rs, within portfolio management

<details><summary>Answer</summary>

**D is right.** Choosing a strategy for one application at a time is the 7 Rs. In the CAF, the Business perspective's portfolio management capability uses the 7 Rs to sort the existing applications and build the business case. That's where the two frameworks meet.

- **A is wrong.** There's no Process perspective. Process is one of the four transformation domains; the six perspectives are Business, People, Governance, Platform, Security and Operations.
- **B is wrong.** A Well-Architected review judges how well one workload is built, against six pillars. It doesn't choose a migration strategy.
- **C is wrong.** The phases are the order of work for the organization. Scale expands the pilots; it isn't where each application's strategy is chosen.

</details>

**A4.** A logistics company runs 120 virtual machines on VMware in its data center. It wants to stop paying for VMware and stop running it altogether. Each machine should become an Amazon EC2 instance with the same operating system and software, unchanged. Which migration strategy is this?

- **A.** Relocate
- **B.** Rehost
- **C.** Replatform
- **D.** Refactor

<details><summary>Answer</summary>

**B is right.** Rehost moves each server, as it is, onto EC2. AWS names rehosting VMware virtual machines onto EC2 as one of the two routes for VMware.

- **A is wrong.** Relocate is the other route: it moves the whole VMware platform to a VMware-based service on AWS, so the team keeps running VMware with the same tools. This company wants the opposite. (Relocate is the seventh R, the one that older lists of "six Rs" leave out.)
- **C is wrong.** Replatform changes something on the way, such as the operating system or a managed database. Here nothing in the machines changes.
- **D is wrong.** Refactor redesigns the application, and nothing is redesigned.

</details>

**A5.** An insurer's claims application runs on an operating system version that will soon lose support. Claims agents use the application all day. As part of the move to AWS, the team runs it on EC2 with the latest version of the same operating system, and changes none of the application's code. Which strategy is this?

- **A.** Retire, because its operating system will soon lose its support
- **B.** Rehost, because none of the application's code is changed
- **C.** Replatform, because the operating system is upgraded on the way
- **D.** Refactor, because the move modernizes the whole application

<details><summary>Answer</summary>

**C is right.** Upgrading the operating system to the latest version, for security and compliance, is one of AWS's use cases for replatforming: the code stays, and what it runs on changes.

- **A is wrong.** An unsupported operating system is one of AWS's retire criteria, but business value decides, and agents use this application all day.
- **B is wrong.** Rehost would move the server unchanged, old operating system included.
- **D is wrong.** Refactor changes the application's design to use cloud-native features. Nothing in the design changes here.

</details>

**A6.** A pharmaceutical company's portfolio review lists five applications. Which two should it retain for now? (Select TWO.)

- **A.** A controller that talks directly to the instruments in its laboratory
- **B.** A reporting tool that nobody has opened in five months
- **C.** A customer database package whose vendor releases a SaaS version next year
- **D.** A large ordering program that the business needs to scale tenfold
- **E.** 200 VMware virtual machines that must move quickly, run with the same tools

<details><summary>Answer</summary>

**A and C are right.** AWS lists both as reasons to retain: a physical dependency on special hardware with no cloud equivalent, and waiting for a SaaS version the vendor hasn't released yet. The second is a retain only for now: once the SaaS version exists, it becomes a repurchase.

- **B is wrong.** No connections for well over 90 days is one of AWS's retire criteria. Archive anything the company must keep, then switch it off.
- **D is wrong.** Strong business demand that the current design blocks points to refactor, probably after a first move.
- **E is wrong.** A whole VMware platform that can move as it is points to relocate.

</details>

**A7.** A retailer is moving its product catalog database from Microsoft SQL Server on its own server to Amazon Aurora PostgreSQL, to stop paying for SQL Server licenses. The online shop keeps taking orders while the data is copied. Which two AWS tools does the move need? (Select TWO.)

- **A.** AWS Application Migration Service
- **B.** AWS Schema Conversion Tool (AWS SCT)
- **C.** AWS DataSync
- **D.** AWS Database Migration Service (AWS DMS)
- **E.** AWS Migration Hub

<details><summary>Answer</summary>

**B and D are right.** The engine changes, so AWS SCT (or DMS Schema Conversion, in the DMS console) converts the schema first. Then AWS DMS copies the data and keeps copying each new order until the cutover, so the shop stays open.

- **A is wrong.** Application Migration Service, now AWS Transform MGN, copies whole servers onto EC2. The catalog would still be SQL Server, on a server the retailer patches.
- **C is wrong.** DataSync copies files and objects, not live database tables.
- **E is wrong.** Migration Hub tracks migrations and moves nothing. It has also been closed to new customers since 2025-11-07 (checked 2026-10-24); AWS points them to AWS Transform.

</details>

**A8.** A research institute must move 80 TB of instrument files from a file server into Amazon S3 within two months. The institute is new to AWS, and its 2 Gbps internet link is nearly idle at night. A colleague suggests ordering an AWS Snowball device, "because the data set is large". What should the institute use?

- **A.** An AWS Snowball Edge device, shipped to the institute
- **B.** AWS Application Migration Service, copying the file server
- **C.** AWS Elastic Disaster Recovery, replicating the file server
- **D.** AWS DataSync, copying the files over the network

<details><summary>Answer</summary>

**D is right.** DataSync copies files over the network into S3, with encryption and checks that the copy is complete. The arithmetic shows the network is fast enough: at 80% of 2 Gbps, 80 TB takes under a week, so even night-time copying finishes well within two months. A bandwidth limit on the task keeps daytime traffic free.

- **A is wrong.** Snowball Edge has been closed to new customers since 2025-11-07, and AWS ends support for Snowball devices in its commercial Regions on 2026-12-31 (checked 2026-10-24). "Large" alone no longer means "ship a device".
- **B is wrong.** Application Migration Service would copy the whole file server onto EC2, not the files into S3.
- **C is wrong.** Elastic Disaster Recovery keeps a standby copy of a server for recovery; it doesn't move files into S3.

</details>

**A9.** A clinic group has two jobs:

1. Its booking servers move to Amazon EC2 this quarter, unchanged, and the old servers are then retired.
2. Its lab-results servers stay in the clinics for two more years, but must be running in AWS within minutes if a clinic's building fails.

Which tools fit?

- **A.** (1) AWS Elastic Disaster Recovery; (2) AWS Application Migration Service
- **B.** (1) AWS DataSync; (2) AWS Elastic Disaster Recovery
- **C.** (1) AWS Application Migration Service; (2) AWS Elastic Disaster Recovery
- **D.** (1) AWS DMS; (2) AWS Backup alone

<details><summary>Answer</summary>

**C is right.** Both tools copy a server's disks continuously into AWS; the ending differs. Application Migration Service (now AWS Transform MGN) is a one-time move: replication stops at cutover and the old server is retired. Elastic Disaster Recovery keeps replicating for as long as the server stays where it is, so it can be launched in AWS within minutes and failed back later.

- **A is wrong.** It swaps the two tools.
- **B is wrong.** DataSync copies files, not whole servers.
- **D is wrong.** DMS copies database data, not whole servers. A backup gives back data, but someone still has to rebuild the server, which takes far longer than minutes.

</details>

**A10.** A manufacturer's CFO wants a three-year comparison of staying on-premises against moving to AWS before the board votes. A consultant's plan says: "Enter both sides into the AWS TCO Calculator." What should the plan say instead?

- **A.** Keep it: the TCO Calculator still compares both sides for you
- **B.** Project the AWS side with Migration Evaluator, from measured use
- **C.** Run AWS Compute Optimizer on the on-premises servers to size them
- **D.** Forecast both sides in AWS Cost Explorer from last year's AWS bill

<details><summary>Answer</summary>

**B is right.** Migration Evaluator starts from measured data about the servers the company runs, finds the over-sized ones, and projects their AWS cost, including license options. For the on-premises side, the lesson uses the company's own figures from its finance team.

- **A is wrong.** The TCO Calculator no longer exists: its address now opens the AWS Pricing Calculator (checked 2026-10-24). The idea of total cost of ownership lives on; that tool doesn't.
- **C is wrong.** Compute Optimizer analyzes resources already running in AWS, from their CloudWatch metrics. It can't see on-premises servers.
- **D is wrong.** Cost Explorer shows and forecasts AWS spending you already have. It knows nothing about the data center.

</details>

**A11.** An engineering firm owns 200 Windows Server licenses bought in 2018, without Software Assurance. It plans to rehost 60 Windows servers onto Amazon EC2. Which two conclusions are justified? (Select TWO.)

- **A.** It can bring the licenses to shared instances under License Mobility.
- **B.** It can bring these licenses to AWS only on Dedicated Hosts.
- **C.** Once it brings them, AWS checks that it follows Microsoft's terms.
- **D.** License-included instances are ruled out, since it already owns licenses.
- **E.** It should compare BYOL on hosts it can fill with license-included.

<details><summary>Answer</summary>

**B and E are right.** Windows Server licenses without Software Assurance can come to AWS only on Dedicated Hosts, and only if they were bought before 2019-10-01, which these were (AWS's Microsoft licensing page, checked 2026-10-24). A Dedicated Host is billed as a whole server, so BYOL pays off only if the firm can fill its hosts. With 60 servers it may, so both routes are worth pricing.

- **A is wrong.** Windows Server isn't eligible for License Mobility, and License Mobility needs active Software Assurance anyway.
- **C is wrong.** With licenses you bring, following the terms is your job. AWS License Manager helps you track them, but it doesn't make AWS responsible.
- **D is wrong.** License-included is always allowed. Owning licenses is a reason to compare, not a rule.

</details>

**A12.** A distribution company's business case shows three columns over three years: stay on-premises; move every server at its current size, with licenses bought from AWS; and the same move with servers rightsized from measured use and licenses chosen for each workload. Both move columns include the same one-time migration costs. The first move column costs more than staying, and the second costs less. Which conclusion does the case support?

- **A.** The saving comes from rightsizing and licensing, not the move.
- **B.** Moving is too expensive, so the company should stay where it is.
- **C.** Rightsizing can wait until a three-year Savings Plan is in place.
- **D.** The two move columns can't both be right, so the case must be redone.

<details><summary>Answer</summary>

**A is right.** The move alone doesn't save money; copying over-sized servers and buying every license by the hour costs more than staying. The two decisions, sizing from measured use and choosing each license route, make the move cheaper. So the plan must commit to both, and keep checking after the move with Compute Optimizer.

- **B is wrong.** The case shows a cheaper way to move. Rejecting the move ignores the third column, and the value beyond cost, such as agility and resilience.
- **C is wrong.** A commitment bought for an over-sized server locks the waste in for one or three years. Rightsize first, then commit.
- **D is wrong.** The columns differ only in the two decisions, so the difference between them is the point of the case, not an error.

</details>

## Correction map

For each question you missed, reread the section named, then try the explanation in the last column, which puts the idea a different way. Then redo the practice named.

| Question | Objective | Reread | Practice | Another way to see it |
|---|---|---|---|---|
| A1 | 13.01a Map a concern to a CAF perspective | [Business or Governance: deciding what to do, or overseeing how it goes](01-the-cloud-adoption-framework.md#business-or-governance-deciding-what-to-do-or-overseeing-how-it-goes), and the traps under [Six perspectives group the capabilities](01-the-cloud-adoption-framework.md#six-perspectives-group-the-capabilities-each-owned-by-different-people) | [Simulation S16](05-sim-portfolio-sorter.md), decision 2 | Picture the program as a building project: Business decided to build; Governance is the site manager who tracks the schedule, the budget and the risks, whoever is asked to do it. |
| A2 | 13.01a | [Map a concern by asking what is at stake, not who is asking](01-the-cloud-adoption-framework.md#map-a-concern-by-asking-what-is-at-stake-not-who-is-asking) | [Simulation S16](05-sim-portfolio-sorter.md), decision 2 | Ask "is anyone attacking us?" If no, a failure that stops a service is Operations, however serious it is. |
| A3 | 13.01a | [The CAF and the 7 Rs work at different levels](01-the-cloud-adoption-framework.md#the-caf-and-the-7-rs-work-at-different-levels) | [Simulation S16](05-sim-portfolio-sorter.md), decisions 1 and 4 | The CAF asks about the whole company; the 7 Rs ask about one application. If the question names a single application's fate, it's the 7 Rs. |
| A4 | 13.02a Assign and justify a strategy | [Rehost and relocate: move without changing the application](02-seven-migration-strategies.md#rehost-and-relocate-move-without-changing-the-application) | [Simulation S16](05-sim-portfolio-sorter.md), decision 1 (shop tools) | Ask what moves: each server on its own (rehost), or the platform they all live on (relocate). |
| A5 | 13.02a | [Replatform and repurchase: change something on the way](02-seven-migration-strategies.md#replatform-and-repurchase-change-something-on-the-way) | [Simulation S16](05-sim-portfolio-sorter.md), decision 1 (loyalty database) | Replatform is moving house and replacing the old boiler on the way: same household, a better system under it. |
| A6 | 13.02a | [Retire and retain: decide first what doesn't move](02-seven-migration-strategies.md#retire-and-retain-decide-first-what-doesnt-move) | [Simulation S16](05-sim-portfolio-sorter.md), decision 1 (oven control, accounting) | Retain means "not yet, for a reason you can name". If you can't name the reason, it isn't a retain. |
| A7 | 13.03a Choose a migration tool | [MGN moves servers; DMS moves the data inside databases](03-migration-tools.md#mgn-moves-servers-dms-moves-the-data-inside-databases) | The lesson's [worked example](03-migration-tools.md#worked-example-a-tool-for-each-of-the-chains-jobs) | Name the unit that moves first: a whole server, or the rows in a database. Then ask whether the database engine changes. |
| A8 | 13.03a | [Files move over the network with DataSync; Snowball is no longer the answer](03-migration-tools.md#files-move-over-the-network-with-datasync-snowball-is-no-longer-the-answer) | The 60 TB "Your turn" in that section | Do the arithmetic before reaching for a device: terabytes × 8,000,000 ÷ (megabits per second × 0.8) gives seconds. |
| A9 | 13.03a | [MGN or Elastic Disaster Recovery: same copying, different ending](03-migration-tools.md#mgn-or-elastic-disaster-recovery-same-copying-different-ending) | The lesson's [worked example](03-migration-tools.md#worked-example-a-tool-for-each-of-the-chains-jobs) | Ask whether the old server should still exist afterwards. No: a migration. Yes: disaster recovery. |
| A10 | 13.04a Build a cost comparison and make a licensing decision | [There is no TCO Calculator](04-the-business-case.md#there-is-no-tco-calculator-use-migration-evaluator-for-the-case-and-the-pricing-calculator-for-estimates) | [Simulation S17](06-sim-rightsizing-and-licensing.md), part 1 | Each tool answers one question: Migration Evaluator, "what would what we run cost on AWS?"; the Pricing Calculator, "what does this AWS design cost?"; Cost Explorer, "what have we spent?". |
| A11 | 13.04a | [License-included or bring your own license: who pays the software vendor](04-the-business-case.md#license-included-or-bring-your-own-license-who-pays-the-software-vendor) | [Simulation S17](06-sim-rightsizing-and-licensing.md), decisions 2 and 3 | Follow S17's licensing tree from the top: own licenses? mobility rights? tied to hardware? Each "no" closes a route. |
| A12 | 13.04a | [The big picture: three ways to spend the next three years](04-the-business-case.md#the-big-picture-three-ways-to-spend-the-next-three-years) and [Rightsize twice](04-the-business-case.md#rightsize-twice-before-the-move-from-measured-data-and-after-it-with-compute-optimizer) | [Simulation S17](06-sim-rightsizing-and-licensing.md), part 1 | Moving an over-sized server is like renting a bigger flat than you need because your old house was big: the move doesn't save money; choosing the right size does. |

## Check B: parallel retest

Take Check B after you've reread and practiced. It tests the same objectives as Check A, one for one, with new situations. You pass at 10 of 12.

**B1.** A city council's IT director wants an up-to-date inventory of every application the council runs, with each one's owner, licenses and running cost, kept current as the applications move to AWS. Which AWS CAF perspective does this work belong to?

- **A.** Platform
- **B.** Governance
- **C.** Operations
- **D.** Business

<details><summary>Answer</summary>

**B is right.** Keeping the inventory of applications, with their owners, licenses and costs, is Governance's application portfolio management capability, close to its cloud financial management.

- **A is wrong.** Platform builds and standardizes the cloud environment; it doesn't keep the inventory of what runs in it.
- **C is wrong.** Operations keeps running services healthy, not the record of who owns them and what they cost.
- **D is wrong.** Business has a "portfolio" capability too, but it chooses which initiatives to invest in and in what order. Keeping the inventory and tracking spend and results is Governance.

</details>

**B2.** A food-delivery company's head of customer experience wants dashboards and alerts that show, minute by minute, whether the ordering service is meeting the response times agreed with the business. Which AWS CAF perspective deals with this concern?

- **A.** Platform
- **B.** Governance
- **C.** Security
- **D.** Operations

<details><summary>Answer</summary>

**D is right.** Watching a service's health against the level the business agreed is observability, an Operations capability. The person asking works in customer experience, but what's at stake is how the running service performs.

- **A is wrong.** Platform builds the environment the service runs in; watching it run is Operations.
- **B is wrong.** "Agreed with the business" sounds like oversight, but Governance oversees the transformation program, not a running service's response times.
- **C is wrong.** Security protects data and systems. Nothing here is a threat.

</details>

**B3.** Before committing to a move, a charity's trustees want to know whether the organization itself is ready for the cloud: whether staff have the skills, whether spending and risks will be overseen, and whether security and operations can cope. Which approach fits that question?

- **A.** An assessment across the six perspectives of the AWS CAF
- **B.** A review of each workload in the AWS Well-Architected Tool
- **C.** One of the 7 Rs assigned to each of its applications
- **D.** A Migration Evaluator projection of its server costs

<details><summary>Answer</summary>

**A is right.** Readiness of the whole organization, its skills, oversight, security and operations, is what the CAF's six perspectives cover. AWS's Migration Readiness Assessment uses the CAF this way at the start of a large migration.

- **B is wrong.** A Well-Architected review judges how well one workload is built, against six pillars. It doesn't assess the organization's readiness.
- **C is wrong.** The 7 Rs decide what happens to each application, one at a time. They come after, or alongside, the readiness question.
- **D is wrong.** Migration Evaluator prices the servers on AWS. Cost is one input, but it says nothing about skills or oversight.

</details>

**B4.** A software company's customer portal keeps its data in an Amazon RDS database in one AWS Region. To keep the data nearer its customers, the company moves the database, unchanged, to an AWS Region closer to them. Which migration strategy describes the move?

- **A.** Relocate
- **B.** Rehost
- **C.** Replatform
- **D.** Retain

<details><summary>Answer</summary>

**A is right.** Besides moving a whole platform such as VMware, relocate covers moving resources that are already on AWS to a different VPC, Region or account, without changing them.

- **B is wrong.** Rehost moves servers from where they run today, such as a data center, onto EC2. This is a managed database that already runs on AWS.
- **C is wrong.** Replatform changes something on the way, such as the database host. Nothing changes here.
- **D is wrong.** Retain keeps an application where it is. This one moves.

</details>

**B5.** An online magazine runs its website and its MySQL database on two on-premises servers. In the move, the web server becomes an EC2 instance as it is, and the database moves to Amazon RDS for MySQL. No code changes. Which strategy describes the move of this application?

- **A.** Rehost, because the web server moves over exactly as it is
- **B.** Replatform, because the database moves onto a managed service
- **C.** Refactor, because AWS now runs and patches the database software
- **D.** Relocate, because both of the servers move together in one go

<details><summary>Answer</summary>

**B is right.** Moving the database onto a managed service while the code stays the same is replatforming, the same kind of change as AWS's own example of SQL Server moving onto Amazon RDS for SQL Server. The magazine also stops patching the database software.

- **A is wrong.** If everything moved unchanged, it would be rehost, but the database changes what it runs on.
- **C is wrong.** Refactor redesigns the application for cloud-native features. Using a managed database without changing the code isn't a redesign.
- **D is wrong.** Relocate moves a whole platform, such as VMware, or moves resources that are already on AWS.

</details>

**B6.** A school district's portfolio review lists five applications. Which two should it retain for now? (Select TWO.)

- **A.** An intranet site that has had no visitors since last year
- **B.** A billing system upgraded six months ago
- **C.** A payroll package whose vendor now sells the same product as a service
- **D.** A records system whose data must legally stay on site
- **E.** A custom Linux application that works well and must move soon, unchanged

<details><summary>Answer</summary>

**B and D are right.** AWS lists both as reasons to retain: a recent upgrade (wait for the next technology refresh), and compliance rules about where data must stay.

- **A is wrong.** No visitors for well over 90 days is a retire criterion.
- **C is wrong.** The service version already exists, so it's a repurchase: swap the licensed package for the vendor's service.
- **E is wrong.** A working application that must move fast without changes is a rehost.

</details>

**B7.** A wholesaler's migration plan pairs each job with an AWS tool. Which two pairs are right? (Select TWO.)

- **A.** Copy its Linux servers to EC2, unchanged: AWS Application Migration Service
- **B.** Copy its live SQL Server data into Amazon RDS for SQL Server: AWS DataSync
- **C.** Copy its live MySQL data into Amazon RDS for MySQL: AWS DMS
- **D.** Copy its file shares into Amazon S3: AWS Application Migration Service
- **E.** Keep standby copies of the servers that stay behind: AWS DMS

<details><summary>Answer</summary>

**A and C are right.** Whole servers, unchanged, are a job for Application Migration Service (now AWS Transform MGN). The data inside a database is a job for AWS DMS, which keeps copying changes until the cutover. The engine stays MySQL, so no schema conversion is needed.

- **B is wrong.** DataSync copies files and objects, not live database tables. This is a job for AWS DMS.
- **D is wrong.** Application Migration Service copies whole servers onto EC2. File shares go to S3 with DataSync, or a direct upload if they're small.
- **E is wrong.** DMS copies database data. Standby copies of servers that stay are a job for Elastic Disaster Recovery.

</details>

**B8.** A film archive that is new to AWS must move 500 TB of scanned film from its storage servers into Amazon S3 within six weeks. Its only internet link runs at 100 Mbps. Which option fits?

- **A.** AWS DataSync over the existing internet link
- **B.** AWS Snowball Edge devices ordered from AWS
- **C.** AWS Data Transfer Terminal, bringing the archive's own devices
- **D.** AWS Application Migration Service, copying the servers

<details><summary>Answer</summary>

**C is right.** Do the arithmetic first: at 80% of 100 Mbps, 500 TB takes well over a year, so this network can't finish in six weeks. For physical transfers, AWS now points new customers to AWS Data Transfer Terminal, AWS sites where you bring your own storage devices and upload over a fast connection, or to AWS Partners (checked 2026-10-24). Older question banks key Snowball for this situation, and the exam guide doesn't list Data Transfer Terminal; for a customer new to AWS today, Snowball isn't available.

- **A is wrong.** DataSync is the right tool when the network is fast enough. Here it isn't.
- **B is wrong.** Snowball Edge has been closed to new customers since 2025-11-07, and support for Snowball devices in AWS's commercial Regions ends on 2026-12-31 (checked 2026-10-24).
- **D is wrong.** Application Migration Service copies whole servers onto EC2, over the same slow link, and doesn't put files into S3.

</details>

**B9.** A law firm wants to launch test copies of its case-management servers in AWS as often as it likes, without disturbing the originals, then switch users over in a short cutover and retire the old servers. Which AWS service fits?

- **A.** AWS Application Migration Service
- **B.** AWS Elastic Disaster Recovery
- **C.** AWS Database Migration Service
- **D.** AWS Backup

<details><summary>Answer</summary>

**A is right.** Application Migration Service (now AWS Transform MGN) copies whole servers into a staging area while they keep running, lets you launch and throw away test instances, and cuts over in a short switch. After cutover, replication stops and the old servers are retired: a one-time move.

- **B is wrong.** Elastic Disaster Recovery copies servers the same way, but for servers that stay where they are. The firm wants the old servers gone.
- **C is wrong.** DMS copies the data inside databases, not whole servers.
- **D is wrong.** A backup gives back data, not a tested, running copy of a server with a planned cutover.

</details>

**B10.** A business case for moving to AWS is about to go to the board. It already counts every cost on both sides, including the one-time costs of the move. Which addition would most strengthen it?

- **A.** A second copy of the on-premises costs, raised for safety
- **B.** A rule that staff costs drop to zero once the servers move
- **C.** A line removing one-time costs, since they happen only once
- **D.** The value beyond cost, such as faster launches and resilience

<details><summary>Answer</summary>

**D is right.** Money isn't the whole case. AWS's Cloud Economics Center describes cloud value in five dimensions: cost savings, staff productivity, operational resilience, business agility and sustainability. A strong case states those benefits in the board's terms next to the numbers.

- **A is wrong.** Inflating one side makes the comparison less honest, not stronger.
- **B is wrong.** Staff don't drop to zero: people still run, secure and improve what's in AWS.
- **C is wrong.** Leaving out one-time costs flatters the move; they belong in the case.

</details>

**B11.** A company runs license-included SQL Server Enterprise on several EC2 instances. Its database team confirms that no Enterprise-only features are in use. Which two conclusions are justified? (Select TWO.)

- **A.** The company must bring its own licenses before it can change edition.
- **B.** Moving to Standard edition would cut the license part of the hourly price.
- **C.** AWS Compute Optimizer can report the license as not optimized.
- **D.** AWS License Manager will switch the edition for it automatically.
- **E.** The edition doesn't change the price of a license-included instance.

<details><summary>Answer</summary>

**B and C are right.** On a license-included instance, the SQL Server license is a large part of the hourly price, and Enterprise costs much more than Standard. Compute Optimizer, once you opt in, reports an Enterprise license that uses no Enterprise features as not optimized and shows the saving from Standard.

- **A is wrong.** License-included instances come in both editions; no licenses of your own are needed to change.
- **D is wrong.** License Manager tracks licenses and can stop launches that go over what you own. It doesn't choose or change editions for you.
- **E is wrong.** The edition is the biggest difference in a license-included SQL Server price.

</details>

**B12.** A company needs SQL Server on AWS for a four-month project, after which the workload is retired. It owns SQL Server licenses, bought in 2022, whose Software Assurance is due for renewal next month, and the renewal would be paid only for this project. Which licensing choice does the evidence support?

- **A.** Renew Software Assurance and bring the licenses, since owned licenses are free
- **B.** Bring the licenses to a Dedicated Host, without renewing Software Assurance
- **C.** Use license-included instances, paid by the hour, and let the renewal lapse
- **D.** Repurchase the workload as SaaS, since BYOL is never allowed for projects

<details><summary>Answer</summary>

**C is right.** License-included usually wins for small, short-lived or changing workloads: you pay by the hour, stop when the project ends, and AWS handles the licensing. Renewing Software Assurance only to move one short project would add a yearly cost for four months of use.

- **A is wrong.** What was paid for the licenses in the past doesn't decide; the renewal is a new cost, and BYOL also makes compliance the company's job.
- **B is wrong.** Without Software Assurance, only licenses bought before 2019-10-01 can go on Dedicated Hosts (checked 2026-10-24); these were bought in 2022. A whole host for a short project would rarely be cheaper anyway.
- **D is wrong.** Repurchase is a migration strategy, not a license route, and BYOL is allowed where the license terms permit it.

</details>

## Enrichment for learners who passed

These tasks go past the exam. Each has no single right answer; compare yours with the model answer.

**E1. Defend the wholesale portal plan.** The chain's board has just hired six developers, and the head of wholesale argues: "Now that we have the people, let's refactor the wholesale portal during the move, so we only move it once." The data center lease still ends in 18 months, and nine other applications must move too. Write a recommendation of four or five sentences: rehost now and refactor later, or refactor during the move. Name the facts that would change your answer, and link your answer to a Well-Architected design principle.

<details><summary>Model answer</summary>

Rehost the portal now and refactor it on AWS afterwards. The portal meets AWS's refactor criteria, but refactoring is the most complex and costly strategy, and AWS's guidance for large migrations is to move first and modernize once the application runs on AWS. Six new developers will take time to learn the portal, and a refactor that slips would put the lease deadline, and the other nine moves, at risk. Once the portal runs on EC2, the team can break it into smaller pieces one at a time, testing each change, which is the operational excellence design principle "[Make frequent, small, reversible changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html)". The answer would change if the lease were extended, if the portal's current design couldn't survive the next busy season, or if the developers already knew the code well enough to deliver the refactor with months to spare.

</details>

**E2. When the bill misses the forecast.** Six months after the first wave moved, the chain's monthly AWS bill is well above what the business case forecast. The finance director asks the migration team for a plan. List what you'd check, in order, and the tool or data for each.

<details><summary>Model answer</summary>

1. **Rightsizing:** opt in to AWS Compute Optimizer if it isn't on yet, and read its findings for the moved instances. Install the CloudWatch agent where memory data is missing, so that no instance is downsized blind.
2. **Schedules:** find test and development instances that run around the clock but are used only in working hours, and stop them outside those hours.
3. **Licenses:** check license-included instances, especially SQL Server Enterprise. Compute Optimizer can show where Enterprise features aren't used and Standard edition would do.
4. **Leftovers:** check that the old environments really are gone, on both sides: data center contracts and AWS resources from test launches.
5. **Commitments:** only after sizing is settled, consider a Savings Plan for the steady load.
6. **The case itself:** compare each line of the forecast with Cost Explorer's actual figures, so the next wave is priced better.

This is [COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html), and finance and engineers working through it together is [COST01-BP02 Establish a partnership between finance and technology](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_partnership.html).

</details>

**E3. Outcomes the board can measure.** For each of the four CAF business outcomes, write one measurable target for the chain, and say which transformation domain delivers it. Then explain in one sentence why the "technology" domain alone delivers the smallest part of the value.

<details><summary>Model answer</summary>

| Outcome | A measurable target for the chain | Domain that delivers it |
|---|---|---|
| Reduce business risk | No December slowdown of the website; no system on an unsupported operating system after the move | Technology |
| Improve ESG performance | A yearly energy and carbon figure for the chain's IT, which a supermarket customer can be sent | Process (reporting from data the chain didn't collect before) |
| Grow revenue | Five times the wholesale café customers within three years | Product (a café ordering and subscription service), enabled by organization (one team owning wholesale) |
| Increase operational efficiency | The data center contract ended; the two mail-server staff moved to other work | Technology and process |

Moving servers (technology) mostly removes costs and risks; most of the growth comes from the changes the move makes possible next, in process, organization and product, which is why the CAF describes the four domains as a chain, each enabling the next ([AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/)).

</details>

**Next:** [Module 14, the capstone](../14-capstone/00-brief.md).

---

"Module 13 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
