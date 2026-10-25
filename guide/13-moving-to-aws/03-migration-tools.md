---
type: lesson
id: clf-13-03
title: "Migration tools"
tasks: ["1.3", "3.4"]
objectives: ["13.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 12 and lessons 13.01 and 13.02; about 20 minutes; works on a phone"
prerequisites: [clf-13-02, clf-05-04, clf-05-05]
terms_introduced: [Migration Evaluator, AWS Application Discovery Service, dependency, AWS Migration Hub, AWS Transform, AWS Transform MGN, cutover, AWS Data Transfer Terminal]
pillars: [operational-excellence, reliability, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/migration-evaluator/faqs/"
  - "https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html"
  - "https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html"
  - "https://aws.amazon.com/transform/"
  - "https://aws.amazon.com/application-migration-service/"
  - "https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html"
  - "https://aws.amazon.com/dms/faqs/"
  - "https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html"
  - "https://aws.amazon.com/snowball/"
  - "https://aws.amazon.com/snowball/faqs/"
  - "https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html"
  - "https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html"
---

# Pick a migration tool by what it moves: a business case, whole servers, database data or files

Each AWS migration tool does one job, and the exam tests whether you can match the job to the tool. Two of the tools the exam names are closed to new customers, and Snowball is being retired, so this lesson also tells you what AWS offers today.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [lesson 13.02](02-seven-migration-strategies.md), on [hybrid storage and backup](../05-storing-data/04-hybrid-storage-and-backup.md) (Elastic Disaster Recovery, DataSync) and on [managed databases](../05-storing-data/05-managed-or-self-managed-databases.md) (DMS and SCT).

## Warm-up: what you remember

1. From Module 11, "Paying for AWS": before you've built anything in AWS, which tool estimates its monthly cost, and which shows what you've already spent?

<details><summary>Feedback</summary>

1. **The AWS Pricing Calculator** estimates; **Cost Explorer** shows what you've spent. A migration also needs a tool that starts from the servers you run today: Migration Evaluator.

</details>

## What you'll learn

By the end of this lesson, you can choose a migration tool for a job and say why the likely alternatives are wrong (objective 13.03a).

Try this before you read on, and guess if you're unsure: can a new AWS customer sign up for AWS Application Discovery Service today?

## The big picture: tools to plan, tools to move, and one to stay ready

![Migration tools in three columns: plan (Migration Evaluator, Application Discovery Service, Migration Hub), move (Application Migration Service, AWS DMS with AWS SCT, AWS DataSync) and stay ready (Elastic Disaster Recovery). Discovery Service and Migration Hub are outlined as closed to new customers, with an arrow to AWS Transform.](../../images/13-03-big-picture.svg)

*Notice the two outlined boxes in the planning column. The exam still names them; a new customer can't sign up for them.*

**Long description.** Three columns. Plan: Migration Evaluator prices the move; AWS Application Discovery Service finds servers, their use and their dependencies; AWS Migration Hub tracks each application's migration. Discovery Service and Migration Hub are highlighted as closed to new customers since 2025-11-07, with an arrow to AWS Transform. Move: AWS Application Migration Service, now AWS Transform MGN, copies whole servers onto EC2; AWS DMS copies the data inside databases, with AWS SCT or DMS Schema Conversion converting the schema first when the engine changes; AWS DataSync copies files and objects. Stay ready: AWS Elastic Disaster Recovery keeps copying servers so they can be launched in AWS after a disaster. Snowball isn't on the chart, because it's being retired.

## Planning tools build the cost case and the inventory

**Migration Evaluator** builds the business case: what your current servers would cost to run on AWS, and how much you could save. It starts from measured data about what you run today, collected without installing anything on each server, finds servers that are bigger than they need to be, and can model bringing your own Windows Server and SQL Server licenses ([Migration Evaluator FAQs](https://aws.amazon.com/migration-evaluator/faqs/), checked 2026-10-24). You request an assessment from AWS rather than switching it on in the console. Lesson 13.04 uses its kind of output.

**AWS Application Discovery Service** collects data about on-premises servers and databases: their configuration, how busy they are, and their **dependencies**, the network connections between them. You use it to group servers into applications that should move together. **AWS Migration Hub** is one place to track each application's migration, whichever tool does the moving; it moves nothing itself.

Both stopped accepting new customers on **2025-11-07**. Existing customers can keep using them. AWS recommends **AWS Transform**, an AWS service that uses AI agents to help plan and carry out migrations and modernization, and which the exam guide doesn't list ([Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html); [Migration Hub availability change](https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html), checked 2026-10-24).

### "The discovery tools are open to new customers" is wrong

Courses written before late 2025 tell every migration team to turn on Application Discovery Service and track the work in Migration Hub. A team starting today can't sign up for either; it would use AWS Transform or a Partner's tool. The belief survives because the exam guide still lists both. On the exam, "collect server inventory and dependencies" still points to Application Discovery Service, and "track migrations across tools" to Migration Hub. That answers the prequestion.

## Application Migration Service, now AWS Transform MGN, rehosts whole servers

**AWS Application Migration Service** is AWS's tool for the **rehost** strategy. AWS now calls it **AWS Transform MGN**; the exam uses the old name ([AWS Transform MGN](https://aws.amazon.com/application-migration-service/), checked 2026-10-24). It copies whole servers, with their operating system, applications and data, from physical machines, virtual machines or another cloud, and launches them as EC2 instances, unchanged. It keeps copying every change while the source keeps running, so you can launch test copies as often as you like, and the **cutover**, the moment users switch to the new servers, is a short planned switch: AWS says cutover windows are typically measured in minutes ([What is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html)). Afterwards you still patch the server's operating system, as on any EC2 instance.

### MGN moves servers; DMS moves the data inside databases

Lesson 05.05 introduced the database pair: **AWS DMS** copies the data in a database while the source keeps running, and can keep copying every change; **AWS SCT** (or DMS Schema Conversion, in the DMS console) converts the schema first when the database engine changes. MGN and DMS both copy continuously with little downtime, so they're easy to confuse. The difference is **what lands in AWS**.

![Two panels: Application Migration Service copies a whole server and lands it as an EC2 instance you still run and patch; AWS DMS copies only the data and lands it in a managed database where AWS runs the software. The table below gives the same comparison.](../../images/13-03-mgn-vs-dms.svg)

*Notice the bottom row of each panel: after MGN you still run a server; after DMS you run only a database.*

| | Application Migration Service (AWS Transform MGN) | AWS DMS (with SCT when the engine changes) |
|---|---|---|
| **Copies** | Whole servers: operating system, software, disks | The data inside a database |
| **Lands as** | EC2 instances | A database such as RDS, Aurora or Redshift, or S3 |
| **Afterwards** | You patch the operating system and database software | AWS runs and patches the database software |
| **Usual strategy** | Rehost | Replatform; also database replication |

If the job is "the whole server, unchanged", choose MGN. If it's "the data, into a managed or different database", choose DMS, with SCT first when the engine changes. That's why the chain's loyalty database, replatformed from SQL Server into Amazon RDS for SQL Server, needs DMS alone: same engine, no conversion.

## MGN or Elastic Disaster Recovery: same copying, different ending

**AWS Elastic Disaster Recovery** (lesson 05.04) also copies a server's disks continuously into AWS, and launches recovery servers within minutes after a disaster. The ending differs.

![Two timelines: Application Migration Service replicates, tests, cuts over, then stops and the source is retired; Elastic Disaster Recovery replicates, runs drills, recovers after a disaster, fails back and keeps replicating in a loop. The table below gives the same comparison.](../../images/13-03-mgn-vs-drs.svg)

*Notice the end of each timeline: MGN's line stops at cutover; Elastic Disaster Recovery's line loops back, because protection never ends.*

| | Application Migration Service (AWS Transform MGN) | AWS Elastic Disaster Recovery |
|---|---|---|
| **Goal** | Move servers to AWS, once | Get servers running again after a disaster |
| **After the switch** | Replication stops; the old server is retired | Replication continues; you can fail back |
| **Practice runs** | Test launches before cutover | Drills, for as long as you protect the server |

Ask whether the old server should still exist afterwards. If not, it's a migration: MGN. If it should, and AWS is the place to recover it, it's disaster recovery.

> **Your turn:** The chain retains its accounting servers until their next refresh, but the finance director wants them running within minutes if the data center fails before then. Which tool, and why not MGN or AWS Backup?

<details><summary>Model answer</summary>

**AWS Elastic Disaster Recovery.** The servers stay where they are, and it keeps a current copy in AWS ready to launch. MGN is for moving them, which the plan postpones. A backup gives back data, and someone still has to rebuild the server.

</details>

## Files move over the network with DataSync; Snowball is no longer the answer

**AWS DataSync** copies files and objects over the network, between on-premises storage, other clouds and AWS storage such as S3, EFS and FSx, with encryption and checks that the copy is complete ([What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)). For a migration, it moves file shares and archives, not live databases.

### "Snowball migrates large data sets" is wrong

Older courses say that for tens of terabytes or more, you ship the data on an AWS Snowball device. That's no longer a current answer. Snowball Edge has been closed to new customers since 2025-11-07 ([AWS Snowball FAQs](https://aws.amazon.com/snowball/faqs/)), and AWS ends support for Snowball devices in its commercial Regions on **2026-12-31** ([AWS Snowball](https://aws.amazon.com/snowball/), checked 2026-10-24). For new customers AWS points to DataSync for online transfers, **AWS Data Transfer Terminal** (AWS sites where you bring your own storage devices and upload over a fast connection) for physical transfers, or AWS Partners ([Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)). The current exam guide no longer lists the Snow Family; the belief lives on because Snowball was the textbook answer for years. By our arithmetic, a 1 Gbps link used at 80% moves 60 TB in about a week, so "large" alone no longer means "ship a device".

## Summary

- **Planning tools move nothing:** Migration Evaluator builds the cost case from measured data; Application Discovery Service collects inventory and dependencies; Migration Hub tracks progress. The last two are closed to new customers, who are sent to AWS Transform.
- **Application Migration Service (AWS Transform MGN)** rehosts whole servers onto EC2 with test launches and a short cutover.
- **MGN moves servers; DMS moves database data,** with SCT first when the engine changes.
- **MGN ends at cutover; Elastic Disaster Recovery keeps copying** so a server that stays can be recovered in AWS.
- **Files move with DataSync.** Snowball is closed to new customers, and device support ends on 2026-12-31.

## Practice

1. **Which tool rehosts physical and virtual servers onto Amazon EC2 with minimal downtime?**

   A. AWS DMS\
   B. AWS Application Migration Service (AWS Transform MGN)\
   C. AWS Migration Hub\
   D. AWS DataSync

   <details><summary>Feedback</summary>

   **B is right.** It copies whole servers and launches them as EC2 instances.

   - **A is wrong.** DMS moves the data inside databases, not whole servers.
   - **C is wrong.** Migration Hub tracks migrations and moves nothing.
   - **D is wrong.** DataSync copies files and objects.

   </details>

2. **A company moves its product database from Microsoft SQL Server on its own server to Amazon Aurora PostgreSQL, and the shop keeps taking orders during the copy. Which tools does it need?**

   A. AWS Application Migration Service alone\
   B. AWS SCT, then AWS DMS\
   C. AWS DMS alone\
   D. AWS DataSync

   <details><summary>Feedback</summary>

   **B is right.** The engine changes, so SCT converts the schema first; then DMS copies the data and every new change until cutover.

   - **A is wrong.** MGN would land the SQL Server machine on EC2, unchanged.
   - **C is wrong.** DMS alone fits when the engine stays the same; here it changes.
   - **D is wrong.** DataSync copies files, not live database tables.

   </details>

3. **Which pair is correctly matched?**

   A. Elastic Disaster Recovery: a one-time move that ends at cutover\
   B. Migration Evaluator: a business case from data about current servers\
   C. AWS SCT: ongoing replication of data\
   D. Snowball: the current answer for a new customer moving 100 TB

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** That's Application Migration Service; Elastic Disaster Recovery keeps replicating.
   - **C is wrong.** SCT converts schemas; DMS replicates data.
   - **D is wrong.** Snowball is closed to new customers; DataSync, Data Transfer Terminal or a Partner are the current choices.

   </details>

**Next:** [The business case](04-the-business-case.md).

## Where to check the current details

- [Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html) and [AWS Transform](https://aws.amazon.com/transform/) (checked 2026-10-24)
- [AWS Transform MGN](https://aws.amazon.com/application-migration-service/), formerly AWS Application Migration Service (checked 2026-10-24)
- [AWS Snowball](https://aws.amazon.com/snowball/): the end-of-support date and the alternatives (checked 2026-10-24)

---

"Migration tools" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
