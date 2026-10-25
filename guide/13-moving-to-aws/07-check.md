---
type: check
id: clf-13-07
title: "Module 13 mastery check"
tasks: ["1.3", "1.4"]
objectives: ["13.01a", "13.02a", "13.03a", "13.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 13's lessons; about 25 minutes for Check A"
prerequisites: [clf-13-01, clf-13-02, clf-13-03, clf-13-04]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://aws.amazon.com/application-migration-service/"
  - "https://aws.amazon.com/migration-evaluator/faqs/"
  - "https://aws.amazon.com/windows/resources/licensing/"
---

# Module 13 mastery check: map the concern, choose the strategy and the tool, and defend the cost case

Map concerns to CAF perspectives, choose strategies and tools, and judge a cost case and a license choice.

**For:** an adult who has finished the lessons of [Module 13](00-brief.md). **Time:** about 25 minutes per check.

## How to use this check

Take **Check A** closed-book. A "(Select TWO.)" question counts only if both choices are right, as on the exam. You pass at **80%**: 8 of 10. Otherwise, reread what the [correction map](#correction-map) names for each miss, then take [Check B](#check-b-parallel-retest). Questions use the exam's service names.

## Check A

**A1.** Halfway through a hotel group's migration, its chief information security officer is asked to keep the program's risk register: risks to the schedule, budget and promised benefits, reviewed monthly. Which AWS Cloud Adoption Framework (AWS CAF) perspective does this belong to?

- **A.** Security
- **B.** Business
- **C.** Governance
- **D.** Operations

<details><summary>Answer</summary>

**C is right.** Managing risks to the transformation program is Governance's risk management capability, beside program and benefits management.

- **A is wrong.** The job title doesn't decide; these risks are to the program, not to data or systems.
- **B is wrong.** Business decided the move; overseeing how it goes is Governance.
- **D is wrong.** Operations keeps running services healthy, not the migration program.

</details>

**A2.** A transport company's migration lead decides, one application at a time, which of its 50 applications to retire, rehost or replatform, for the business case. Where does this work sit?

- **A.** In the CAF's Process perspective
- **B.** In a Well-Architected review, pillar by pillar
- **C.** In the CAF's Scale phase, after the pilots
- **D.** In the 7 Rs, within portfolio management

<details><summary>Answer</summary>

**D is right.** A strategy per application is the 7 Rs, which the Business perspective's portfolio management uses for the business case.

- **A is wrong.** There's no Process perspective; process is a transformation domain.
- **B is wrong.** A Well-Architected review judges how well one workload is built.
- **C is wrong.** Scale expands the pilots.

</details>

**A3.** A logistics company wants to stop running VMware: each of its 120 virtual machines should become an Amazon EC2 instance, unchanged. Which migration strategy is this?

- **A.** Relocate
- **B.** Rehost
- **C.** Replatform
- **D.** Refactor

<details><summary>Answer</summary>

**B is right.** Rehost moves each server, as it is, onto EC2; AWS names it as one of the two routes for VMware.

- **A is wrong.** Relocate keeps the VMware platform, on a VMware-based service on AWS; this company wants to leave VMware.
- **C is wrong.** Replatform changes something on the way; nothing changes here.
- **D is wrong.** Nothing is redesigned.

</details>

**A4.** An insurer's claims application, used all day, runs on an operating system that will soon lose support. In the move, the team runs it on EC2 with the latest version of that operating system, changing no code. Which strategy is this?

- **A.** Retire, because the operating system will lose support
- **B.** Rehost, because no code changes
- **C.** Replatform, because the operating system is upgraded on the way
- **D.** Refactor, because the move modernizes the application

<details><summary>Answer</summary>

**C is right.** Upgrading the operating system on the way is an AWS use case for replatforming: the code stays, what it runs on changes.

- **A is wrong.** Business value decides, and agents use it all day.
- **B is wrong.** Rehost would move the old operating system unchanged.
- **D is wrong.** Nothing in the design changes.

</details>

**A5.** A drug company reviews five applications. Which two should it retain for now? (Select TWO.)

- **A.** A controller wired to its laboratory instruments
- **B.** A reporting tool nobody has opened in five months
- **C.** A package whose vendor releases a SaaS version next year
- **D.** An ordering program the business needs to scale tenfold
- **E.** 200 VMware machines that must move quickly, with the same tools

<details><summary>Answer</summary>

**A and C are right.** Special hardware with no cloud equivalent, and waiting for a vendor's SaaS version, are both AWS reasons to retain.

- **B is wrong.** No connections for over 90 days is a retire sign.
- **D is wrong.** That points to refactor.
- **E is wrong.** That points to relocate.

</details>

**A6.** A retailer moves its catalog database from SQL Server on its own server to Amazon Aurora PostgreSQL, and the shop keeps taking orders during the copy. Which two AWS tools does it need? (Select TWO.)

- **A.** AWS Application Migration Service
- **B.** AWS Schema Conversion Tool (AWS SCT)
- **C.** AWS DataSync
- **D.** AWS Database Migration Service (AWS DMS)
- **E.** AWS Migration Hub

<details><summary>Answer</summary>

**B and D are right.** The engine changes, so AWS SCT converts the schema first; then AWS DMS copies the data and each new order until cutover.

- **A is wrong.** Application Migration Service (now AWS Transform MGN) copies whole servers, still on SQL Server.
- **C is wrong.** DataSync copies files, not live database tables.
- **E is wrong.** Migration Hub tracks migrations and moves nothing; it's closed to new customers since 2025-11-07 (checked 2026-10-24).

</details>

**A7.** A clinic group's booking servers (1) move to Amazon EC2 this quarter, unchanged, then the old servers are retired. Its lab-results servers (2) stay in the clinics two more years but must run in AWS within minutes if a building fails. Which tools fit?

- **A.** (1) AWS Elastic Disaster Recovery; (2) AWS Application Migration Service
- **B.** (1) AWS DataSync; (2) AWS Elastic Disaster Recovery
- **C.** (1) AWS Application Migration Service; (2) AWS Elastic Disaster Recovery
- **D.** (1) AWS DMS; (2) AWS Backup alone

<details><summary>Answer</summary>

**C is right.** Both copy servers continuously; Application Migration Service stops at cutover, while Elastic Disaster Recovery keeps replicating for recovery.

- **A is wrong.** It swaps the two tools.
- **B is wrong.** DataSync copies files, not whole servers.
- **D is wrong.** DMS copies database data; a backup leaves the server to rebuild.

</details>

**A8.** A manufacturer's CFO wants a three-year comparison of staying on-premises against moving to AWS. A consultant's plan says: "Enter both sides into the AWS TCO Calculator." What should the plan say instead?

- **A.** Keep it: the TCO Calculator compares both sides
- **B.** Project the AWS side with Migration Evaluator
- **C.** Size the on-premises servers with AWS Compute Optimizer
- **D.** Forecast both sides in AWS Cost Explorer

<details><summary>Answer</summary>

**B is right.** Migration Evaluator projects the AWS cost of the servers the company runs, from measured data; the on-premises side is the company's own figures.

- **A is wrong.** The TCO Calculator no longer exists: its address opens the AWS Pricing Calculator (checked 2026-10-24).
- **C is wrong.** Compute Optimizer analyzes resources already running in AWS.
- **D is wrong.** Cost Explorer knows only AWS spending you already have.

</details>

**A9.** Which two statements about licensing Windows Server and SQL Server on Amazon EC2 are true? (Select TWO.)

- **A.** With license-included, the price covers the license and AWS handles compliance.
- **B.** With BYOL, AWS becomes responsible for the vendor's license terms.
- **C.** BYOL is always cheaper, since the licenses are paid for.
- **D.** With BYOL, the license terms decide where and how the software may run.
- **E.** License-included instances need a Dedicated Host.

<details><summary>Answer</summary>

**A and D are right.** License-included is pay-as-you-go with compliance handled by AWS. With BYOL, the terms set the rules; some licenses need extra vendor rights or Dedicated Hosts.

- **B is wrong.** With BYOL, compliance is the customer's job; AWS License Manager helps track it.
- **C is wrong.** A short project, or a Dedicated Host you can't fill, can make license-included cheaper.
- **E is wrong.** License-included runs on ordinary shared instances.

</details>

**A10.** A business case shows three-year costs for three options: stay; move every server at its current size with licenses bought from AWS; and the same move, rightsized from measured use with licenses chosen per workload. The first move costs more than staying, the second less. Which conclusion does it support?

- **A.** The saving comes from rightsizing and licensing, not the move.
- **B.** Moving is too expensive, so the company should stay.
- **C.** Rightsizing can wait until a Savings Plan is in place.
- **D.** The case is inconsistent and must be redone.

<details><summary>Answer</summary>

**A is right.** Copying oversized servers and buying every license by the hour costs more than staying; the two decisions make the move cheaper.

- **B is wrong.** It ignores the third column.
- **C is wrong.** A commitment bought for an oversized server locks the waste in. Rightsize first.
- **D is wrong.** The columns differ only in the two decisions.

</details>

## Correction map

For each miss, reread the section named.

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 13.01a Map a concern to a CAF perspective | [Business or Governance](01-the-cloud-adoption-framework.md#business-or-governance-deciding-what-to-do-or-overseeing-how-it-goes) |
| A2, B2 | 13.01a | [The CAF and the 7 Rs work at different levels](01-the-cloud-adoption-framework.md#the-caf-and-the-7-rs-work-at-different-levels) |
| A3, B3 | 13.02a Assign and justify a strategy | [Rehost and relocate](02-seven-migration-strategies.md#rehost-and-relocate-move-without-changing-the-application) |
| A4, B4 | 13.02a | [Replatform and repurchase](02-seven-migration-strategies.md#replatform-and-repurchase-change-something-on-the-way) |
| A5, B5 | 13.02a | [Retire and retain](02-seven-migration-strategies.md#retire-and-retain-decide-first-what-doesnt-move) |
| A6, B6 | 13.03a Choose a migration tool | [MGN moves servers; DMS moves the data](03-migration-tools.md#mgn-moves-servers-dms-moves-the-data-inside-databases) |
| A7, B7 | 13.03a | [MGN or Elastic Disaster Recovery](03-migration-tools.md#mgn-or-elastic-disaster-recovery-same-copying-different-ending) |
| A8, B8 | 13.04a Build a cost comparison and make a licensing decision | ["Use the AWS TCO Calculator" is out of date](04-the-business-case.md#use-the-aws-tco-calculator-is-out-of-date) |
| A9, B9 | 13.04a | [License-included or bring your own license](04-the-business-case.md#license-included-or-bring-your-own-license-who-pays-the-software-vendor) |
| A10, B10 | 13.04a | [Rightsize twice](04-the-business-case.md#rightsize-twice-before-the-move-from-measured-data-and-after-it-with-compute-optimizer) |

## Check B: parallel retest

You pass at 8 of 10.

**B1.** A city council's IT director wants a current inventory of every application, with each one's owner, licenses and running cost, as they move to AWS. Which AWS CAF perspective does this belong to?

- **A.** Platform
- **B.** Governance
- **C.** Operations
- **D.** Business

<details><summary>Answer</summary>

**B is right.** Keeping the application inventory, with owners, licenses and costs, is Governance's application portfolio management.

- **A is wrong.** Platform builds the environment, not the record of what runs in it.
- **C is wrong.** Operations runs services.
- **D is wrong.** Business's portfolio capability chooses what to invest in.

</details>

**B2.** Before committing to a move, a charity's trustees ask whether the organization is ready: staff skills, oversight of spending and risk, security and operations. Which approach fits?

- **A.** An assessment across the six perspectives of the AWS CAF
- **B.** A review of each workload in the AWS Well-Architected Tool
- **C.** One of the 7 Rs assigned to each of its applications
- **D.** A Migration Evaluator projection of its server costs

<details><summary>Answer</summary>

**A is right.** The readiness of the whole organization is what the CAF's six perspectives cover.

- **B is wrong.** A Well-Architected review judges one workload's design.
- **C is wrong.** The 7 Rs decide each application's fate, not the organization's readiness.
- **D is wrong.** Migration Evaluator prices servers, not skills or oversight.

</details>

**B3.** A software company's customer portal keeps its data in an Amazon RDS database in one AWS Region. To be nearer its customers, it moves the database, unchanged, to a closer Region. Which strategy describes the move?

- **A.** Relocate
- **B.** Rehost
- **C.** Replatform
- **D.** Retain

<details><summary>Answer</summary>

**A is right.** Relocate also covers moving resources already on AWS to another VPC, Region or account.

- **B is wrong.** Rehost moves servers from where they run today onto EC2.
- **C is wrong.** Nothing changes on the way.
- **D is wrong.** Retain keeps an application where it is.

</details>

**B4.** An online magazine moves its website: the web server becomes an EC2 instance as it is, and its MySQL database moves to Amazon RDS for MySQL, with no code changes. Which strategy describes this?

- **A.** Rehost, because the web server moves as it is
- **B.** Replatform, because the database moves onto a managed service
- **C.** Refactor, because AWS now patches the database software
- **D.** Relocate, because both servers move together

<details><summary>Answer</summary>

**B is right.** Moving the database onto a managed service, code unchanged, is replatforming.

- **A is wrong.** The database changes what it runs on.
- **C is wrong.** A managed database without code changes isn't a redesign.
- **D is wrong.** Relocate moves a whole platform.

</details>

**B5.** A school district reviews five applications. Which two should it retain for now? (Select TWO.)

- **A.** An intranet with no visitors since last year
- **B.** A billing system upgraded six months ago
- **C.** A payroll package the vendor now sells as a service
- **D.** A records system whose data must legally stay on site
- **E.** A working Linux application that must move soon, unchanged

<details><summary>Answer</summary>

**B and D are right.** A recent upgrade and compliance rules on where data must stay are both AWS reasons to retain.

- **A is wrong.** No visitors for over 90 days is a retire sign.
- **C is wrong.** The service version exists, so it's a repurchase.
- **E is wrong.** That's a rehost.

</details>

**B6.** A wholesaler's migration plan pairs each job with an AWS tool. Which two pairs are right? (Select TWO.)

- **A.** Copy its Linux servers to EC2, unchanged: AWS Application Migration Service
- **B.** Copy its live SQL Server data into Amazon RDS for SQL Server: AWS DataSync
- **C.** Copy its live MySQL data into Amazon RDS for MySQL: AWS DMS
- **D.** Copy its file shares into Amazon S3: AWS Application Migration Service
- **E.** Keep standby copies of the servers that stay behind: AWS DMS

<details><summary>Answer</summary>

**A and C are right.** Whole servers go with Application Migration Service; database data goes with DMS (same engine, so no conversion).

- **B is wrong.** DataSync copies files, not live database tables.
- **D is wrong.** File shares go to S3 with DataSync, or a direct upload.
- **E is wrong.** Standby copies of servers are a job for Elastic Disaster Recovery.

</details>

**B7.** A law firm wants to launch test copies of its servers in AWS without disturbing the originals, then cut over and retire the old servers. Which service fits?

- **A.** AWS Application Migration Service
- **B.** AWS Elastic Disaster Recovery
- **C.** AWS Database Migration Service
- **D.** AWS Backup

<details><summary>Answer</summary>

**A is right.** It copies whole servers while they run, allows test launches, and ends at cutover.

- **B is wrong.** Elastic Disaster Recovery is for servers that stay where they are.
- **C is wrong.** DMS copies database data, not whole servers.
- **D is wrong.** A backup gives back data, not a running server.

</details>

**B8.** A retailer wants to know what its 300 on-premises servers would cost on AWS, based on their measured use and including SQL Server licenses. Which AWS offering fits?

- **A.** The AWS Pricing Calculator, with each server at its current size
- **B.** Migration Evaluator
- **C.** AWS Cost Explorer
- **D.** AWS Compute Optimizer

<details><summary>Answer</summary>

**B is right.** It projects the servers' AWS cost from measured use, with license options.

- **A is wrong.** It prices what you type in; at current sizes it copies the waste.
- **C is wrong.** Cost Explorer shows AWS spending the retailer doesn't have yet.
- **D is wrong.** Compute Optimizer analyzes resources already running in AWS.

</details>

**B9.** A company needs SQL Server on AWS for a four-month project. Its own SQL Server licenses would need a Software Assurance renewal paid only for this project. Which choice does the evidence support?

- **A.** Renew Software Assurance and bring the licenses
- **B.** Bring the licenses to a Dedicated Host without renewing
- **C.** Use license-included instances and let the renewal lapse
- **D.** Repurchase the workload as SaaS

<details><summary>Answer</summary>

**C is right.** License-included usually wins for short-lived workloads: pay by the hour, stop when the project ends.

- **A is wrong.** The renewal is a new cost for four months of use.
- **B is wrong.** The terms may not allow it, and a whole host for a short project is rarely cheaper.
- **D is wrong.** Repurchase is a migration strategy, not a license route.

</details>

**B10.** A company has rehosted 80 servers onto EC2 at their on-premises sizes, and finance wants a three-year Savings Plan next week. What should it do first?

- **A.** Buy the Savings Plan now, so the discount starts sooner
- **B.** Rightsize from measured use, for example with AWS Compute Optimizer, then commit
- **C.** Move the servers onto Dedicated Hosts
- **D.** Turn on EC2 Auto Scaling to resize each instance

<details><summary>Answer</summary>

**B is right.** On-premises sizes are often far bigger than needed; rightsize first, then commit.

- **A is wrong.** A commitment on oversized instances locks the waste in for three years.
- **C is wrong.** Dedicated Hosts add cost; they serve license or compliance needs.
- **D is wrong.** Auto Scaling changes the number of instances, not their size.

</details>

**Next:** [Module 13: beyond the exam](08-beyond-the-exam.md), then [Module 14, the capstone](../14-capstone/00-brief.md).

---

"Module 13 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
