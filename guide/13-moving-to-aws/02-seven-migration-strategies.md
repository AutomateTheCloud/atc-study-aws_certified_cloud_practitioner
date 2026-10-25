---
type: lesson
id: clf-13-02
title: "Seven migration strategies"
tasks: ["1.3", "2.1"]
objectives: ["13.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 12 and lesson 13.01; about 20 minutes; works on a phone"
prerequisites: [clf-13-01, clf-04-01, clf-05-05]
terms_introduced: [migration strategy, application portfolio, 7 Rs, retire, retain, rehost, lift and shift, relocate, VMware, repurchase, software as a service, replatform, refactor, cloud-native, monolith, modernize, database replication]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/"
  - "https://aws.amazon.com/vmware/aws-services/"
  - "https://aws.amazon.com/application-migration-service/"
  - "https://aws.amazon.com/dms/faqs/"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html"
---

# Give each application one of seven migration strategies, and justify it with AWS's own criteria

An organization decides, application by application, whether to switch it off, leave it, move it as it is, or change it on the way. AWS names seven such strategies, the **7 Rs**, and the exam asks which one fits a situation.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [lesson 13.01](01-the-cloud-adoption-framework.md), on [who patches what](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md) (lesson 04.01) and on AWS DMS from [lesson 05.05](../05-storing-data/05-managed-or-self-managed-databases.md).

## Warm-up: what you remember

1. From lesson 04.01: a database runs on an EC2 instance. Who patches its operating system and database software? And if it moves to Amazon RDS?

<details><summary>Feedback</summary>

1. **On EC2, the customer patches both.** On RDS, AWS patches the operating system and the database software. Several strategies in this lesson move that line, which is part of why teams choose them.

</details>

## What you'll learn

By the end of this lesson, you can name the seven strategies, tell rehost, relocate, replatform and refactor apart, and assign a strategy to an application with a reason (objective 13.02a).

Try this before you read on, and guess if you're unsure: moving a Microsoft SQL Server database from your own server onto Amazon RDS for SQL Server, with no code changes. Is that rehost or replatform?

## The big picture: seven strategies in three groups

A **migration strategy** is the approach used to move one workload into the AWS Cloud. AWS lists seven: retire, retain, rehost, relocate, repurchase, replatform, and refactor or re-architect ([About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html), AWS Prescriptive Guidance, checked 2026-10-24). They're applied to the **application portfolio**, all the applications an organization runs, one application at a time. Grouping them by what happens to the application makes them easier to hold apart; the grouping is ours, not AWS's.

![The 7 Rs as seven cards in three groups: doesn't move (retire, retain), moves without changing the application (rehost, relocate), and changes on the way (replatform, repurchase, refactor).](../../images/13-02-big-picture.svg)

*Notice that two strategies don't move anything, and two move the application without changing it. Only the last three change what the application is.*

**Long description.** Three groups of cards. Doesn't move: retire, switch it off and archive the data you must keep; retain, keep it where it is for now. Moves without changing the application: rehost, each server as it is onto Amazon EC2; relocate, highlighted as the seventh R added after AWS's 2016 list of six, a whole platform such as VMware to its AWS version, or a resource to another VPC, Region or account. Changes on the way: replatform, a few changes such as moving the database onto Amazon RDS; repurchase, a different product, often software as a service; refactor, a redesign for cloud-native features.

### "There are six Rs" is wrong

"The six Rs" was AWS's list in 2016 ([6 Strategies for Migrating Applications to the Cloud](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/), AWS blog, 2016-11-01). AWS's current guidance lists seven: it adds **relocate**. The older list is tempting because it still circulates in courses, and it was correct when written. If a question describes moving a whole VMware environment as it is, the answer is relocate.

## Retire and retain: decide first what doesn't move

The cheapest migration is the one you don't do, so sort these out first.

**Retire** means decommissioning an application, after archiving any data you must keep, so its servers can be shut down. AWS's signs: no business value in keeping or moving it; it runs on an operating system or components that are no longer supported; nobody has connected to it in the last 90 days; or its use is very low ([Retire](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#retire), checked 2026-10-24).

**Retain** means keeping an application where it is, at least for now. AWS's reasons include compliance rules on where the data must stay; high risk or dependencies on applications that must move first; a recent upgrade, so you wait for the next refresh; waiting for a SaaS version the vendor hasn't released yet; and special hardware with no cloud equivalent, such as machines in a factory ([Retain](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#retain)).

Low use alone doesn't decide. The chain's payroll looks idle most of the month, but it pays everyone; business value settles it.

## Rehost and relocate: move without changing the application

**Rehost**, also called **lift and shift**, moves each server to AWS as it is: it becomes an Amazon EC2 instance with the same operating system and software ([Rehost](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#rehost)). You gain no cloud optimizations at first, but an application already on AWS is easier to improve later.

**Relocate** moves many servers at once, from an on-premises platform to a cloud version of the *same* platform, without buying hardware, rewriting anything or changing how you operate. It also covers moving resources already on AWS to a different VPC, Region or account, such as an RDS database moved to another account. AWS rates relocate the fastest way to get a workload running and operated on AWS ([Relocate](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#relocate)). The common case is **VMware**, software that runs many virtual machines on shared physical servers: AWS calls moving VMware workloads to Amazon Elastic VMware Service, which runs VMware's software on AWS, "relocate" ([Migrate VMware to the cloud](https://aws.amazon.com/vmware/aws-services/), checked 2026-10-24).

So rehost moves each **server** onto EC2. Relocate moves the whole **platform** the servers run on, so the virtual machines and the team's tools stay the same.

> **Your turn:** Two companies want to leave their data centers within a year without changing their applications. Company A has 40 physical Linux servers. Company B has 600 virtual machines on VMware, and its team runs everything through VMware's tools. Which strategy fits each?

<details><summary>Model answer</summary>

**Company A: rehost.** Each server moves, unchanged, onto EC2; there's no platform to carry over. **Company B: relocate.** The whole VMware platform moves at once and the team keeps operating it the same way. Rehosting B's machines onto EC2 is possible too, but it changes how the team runs them.

</details>

## Replatform and repurchase: change something on the way

**Replatform** ("lift, tinker and shift") moves the application and changes what it runs on, so it runs more efficiently, costs less or uses cloud features, while its code barely changes. AWS's own example is moving a SQL Server database onto Amazon RDS for SQL Server ([Replatform](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#replatform)). Other uses: moving to a managed or serverless service, upgrading the operating system, or moving from Windows to Linux to cut license costs. A managed service also moves the patching line: on RDS, AWS patches the database software and its operating system. That answers the prequestion: it's replatform.

**Repurchase** ("drop and shop") replaces the application with a different product, often **software as a service (SaaS)**: an application you use over the internet by subscription while the vendor runs everything underneath. AWS says it typically cuts maintenance, infrastructure and licensing costs ([Repurchase](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#repurchase)). The chain's email moving to a subscription email service is a repurchase; so is its payroll package moving to the vendor's SaaS version.

## Rehost, relocate, replatform, refactor side by side

**Refactor**, also called re-architect, changes an application's design to use **cloud-native** features, such as managed services, automatic scaling and serverless computing. AWS says strong business demand drives it: to scale, release features faster or cut costs ([Refactor or re-architect](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#refactor)). A typical case is a **monolith**, one large program where every change means releasing the whole thing, like the chain's wholesale portal. AWS calls refactoring the most complex and costly strategy. In large migrations it recommends moving first (rehost, relocate or replatform), then you **modernize**, improving the design once the application runs on AWS.

All four move the application to AWS, and their names sound alike. Read the highlighted row first.

![Rehost, relocate, replatform and refactor compared on five rows, with the row "what changes in the application" highlighted. The table below gives the same comparison.](../../images/13-02-four-rs-compared.svg)

*Notice that rehost and relocate both change nothing in the application. What tells them apart is what moves: servers one by one, or a whole platform at once.*

| | Rehost | Relocate | Replatform | Refactor |
|---|---|---|---|---|
| **Also called** | Lift and shift | (no other name) | Lift, tinker and shift; lift and reshape | Re-architect |
| **What moves** | Each server, as it is, onto EC2 | A whole platform to its AWS version, or a resource to another VPC, Region or account | The application, onto better-fitting services | The application, rebuilt |
| **What changes in the application** | Nothing | Nothing, not even how you operate it | A few parts, such as the database host or operating system | Its design, to use cloud-native features |
| **AWS's example** | An application stack from on-premises | VMware workloads to Amazon EVS; an RDS database to another account | SQL Server to Amazon RDS for SQL Server | A monolith that slows every release |
| **What AWS says about effort** | Many servers without compatibility worries; optimize later | The quickest way to migrate and operate a workload | A few or many changes, depending on your goals | The most complex and costly |

To choose, ask in order and stop at the first "yes" (our teaching aid, built from AWS's criteria): no business value, **retire**; a reason to stay for now, **retain**; a product does the job as a service, **repurchase**; strong demand the design blocks, **refactor**, usually after moving; a few changes bring clear savings, **replatform**; a whole platform can move as it is, **relocate**; otherwise, **rehost**.

### Database replication is a technique, used inside a strategy

The exam guide's example of a migration strategy is "database replication" (task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3)). It isn't an eighth R; it's how a database moves. AWS DMS copies the database to AWS while the source keeps running, then keeps copying every new change until you switch over ([AWS DMS FAQs](https://aws.amazon.com/dms/faqs/), checked 2026-10-24), so downtime is short. If a question asks how to migrate a database with minimal downtime, database replication is the answer.

> **Example:** the chain's loyalty database runs on SQL Server, and the team loses days each month to patches and backups. It has business value and no reason to stay, and a managed database removes the patching: **replatform** onto Amazon RDS for SQL Server, with **database replication** through DMS so the loyalty program stays open during the copy. Rehost would carry the patching burden to EC2 unchanged.

## Summary

- **The 7 Rs:** retire, retain, rehost, relocate, repurchase, replatform, refactor. The 2016 list had six; relocate is the newer one.
- **Retire and retain come first.** Retire what has no value; retain what has a reason to stay for now. Business value decides, not low use alone.
- **Rehost** moves each server onto EC2 unchanged; **relocate** moves a whole platform such as VMware, and is AWS's quickest route.
- **Replatform** changes what the application runs on (SQL Server onto RDS); **repurchase** swaps in a different product, often SaaS; **refactor** redesigns it, the most complex and costly, usually after the move.
- **Database replication** with AWS DMS is a technique inside a strategy, for minimal downtime.

## Practice

1. **Which list contains only strategies from AWS's 7 Rs?**

   A. Rehost, replatform, refactor, rebuild\
   B. Retire, retain, relocate, repurchase\
   C. Rehost, redeploy, replatform, retain\
   D. Refactor, reconfigure, retire, rehost

   <details><summary>Feedback</summary>

   **B is right.** All four are among the seven.

   - **A is wrong.** "Rebuild" isn't one of the 7 Rs.
   - **C is wrong.** "Redeploy" isn't one.
   - **D is wrong.** "Reconfigure" isn't one.

   </details>

2. **A company has an application that nobody has connected to in four months, running on an operating system that is out of support. Which strategy fits best?**

   A. Rehost\
   B. Retire\
   C. Retain\
   D. Refactor

   <details><summary>Feedback</summary>

   **B is right.** No connections for over 90 days and an unsupported operating system are both AWS signs to retire. Archive any data the company must keep first.

   - **A is wrong.** Rehosting would carry an unpatched system to AWS and keep paying for something nobody uses.
   - **C is wrong.** Retain needs a reason to stay, such as compliance or a recent upgrade.
   - **D is wrong.** Nobody would redesign an application nobody uses.

   </details>

3. **A company moves its servers to EC2 unchanged and wants minimal downtime for its customer database during the switch. Which strategy and technique?**

   A. Rehost, with database replication through AWS DMS\
   B. Refactor, with a nightly backup and restore\
   C. Relocate, with AWS DataSync\
   D. Repurchase, with a SaaS database

   <details><summary>Feedback</summary>

   **A is right.** Moving servers unchanged is rehost, and DMS copies the database while the source keeps serving customers, then every change until the switch-over.

   - **B is wrong.** Nothing is redesigned, and a backup misses later changes.
   - **C is wrong.** Relocate moves a whole platform; DataSync copies files.
   - **D is wrong.** Nothing is replaced with a different product.

   </details>

**Next:** [Migration tools](03-migration-tools.md). To sort all ten of the chain's applications, try the optional [Simulation S16: the portfolio sorter](05-sim-portfolio-sorter.md).

## Where to check the current details

- [About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html), AWS Prescriptive Guidance (checked 2026-10-24)
- [Migrate VMware to the cloud](https://aws.amazon.com/vmware/aws-services/): relocate or rehost (checked 2026-10-24)
- [AWS DMS FAQs](https://aws.amazon.com/dms/faqs/): ongoing replication (checked 2026-10-24)

---

"Seven migration strategies" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
