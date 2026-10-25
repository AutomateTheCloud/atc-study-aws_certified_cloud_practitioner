---
type: lesson
id: clf-05-05
title: "Managed databases and choosing one"
tasks: ["3.4", "2.1"]
objectives: ["05.05a", "05.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 04, the guardrails primer and lessons 05.01 to 05.04; about 25 minutes; works on a phone"
prerequisites: [clf-04-01, clf-03-03, clf-05-04]
terms_introduced: [relational database, database engine, self-managed database, managed database, Multi-AZ deployment, standby, read replica, Amazon Aurora, NoSQL, key-value database, document database, in-memory database, graph database, data warehouse, Amazon DynamoDB, Amazon ElastiCache, Amazon DocumentDB, Amazon Neptune, Amazon Redshift, schema, AWS Database Migration Service, AWS Schema Conversion Tool]
pillars: [reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://aws.amazon.com/rds/faqs/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html"
  - "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"
  - "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html"
  - "https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html"
  - "https://docs.aws.amazon.com/neptune/latest/userguide/intro.html"
  - "https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html"
  - "https://aws.amazon.com/dms/faqs/"
  - "https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html"
---

# Let AWS run the database, give each copy of it one job, and pick the database by the shape of the data

AWS recommends a managed database, Amazon RDS, for most relational databases. On RDS, a Multi-AZ standby keeps the database running, a read replica takes extra reads, and backups take you back in time. Other AWS databases fit other shapes of data: items looked up by a key, documents, relationships, hot data in memory, and years of history for analysis.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 25 minutes. Reading works on a phone.

**Before you start:** this lesson uses who does what on EC2 and RDS from [lesson 04.01](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md), and backup vs replication from [lesson 03.03](../03-aws-around-the-world/03-surviving-failure.md).

## Warm-up: what you remember

1. The bakery moves its database from an EC2 server to Amazon RDS. Name one task that moves to AWS and one that stays with the bakery.
2. Paying for a server every hour whether it's busy or not, or paying for each request the site serves: which is a fixed cost and which is variable?

<details><summary>Feedback</summary>

1. **To AWS:** patching the operating system and database software, backups, high availability. **Stays:** tuning queries, and deciding who can reach the data (lesson 04.01).
2. **The hourly server is fixed** while it runs; **paying per request is variable** (lesson 02.02). One of this lesson's databases bills per request.

</details>

## What you'll learn

By the end of this lesson, you can choose between a self-managed and a managed database, and between high availability and read scaling (objective 05.05a), and pick a database for a shape of data (objective 05.06a).

Try this before you read on, and guess if you're unsure: the German partner's nightly sales reports slow the bakery's website down. Would a Multi-AZ standby fix that?

## AWS recommends a managed database unless you have a reason not to

A **relational database** keeps data in tables of rows and columns that link to each other, queried in SQL; the **database engine** is the software, such as MySQL or PostgreSQL. You can install an engine yourself on an EC2 server, a **self-managed database**, or let **Amazon Relational Database Service (Amazon RDS)** run it for you, a **managed database**. RDS offers six engines: IBM Db2, MariaDB, Microsoft SQL Server, MySQL, Oracle Database and PostgreSQL, plus Amazon Aurora ([What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), checked 2026-10-23).

On RDS, AWS installs and patches the operating system and database software and runs backups, failover and the hardware. You keep query tuning, who can reach the database, and which protections to turn on. On EC2, AWS runs only the hardware, and the rest is yours. AWS's RDS User Guide recommends RDS as the default for most relational databases and warns that manual patching is prone to mistakes. Our reasoning on when to run your own: when you need an engine RDS doesn't offer, or access to the server's operating system.

### Amazon Aurora is AWS's own relational engine in the RDS family

**Amazon Aurora** is compatible with MySQL and PostgreSQL, so software written for those works with it, and you manage it through RDS ([What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)). Its storage copies your data across three Availability Zones, it supports up to 15 replicas that can also be failover targets, and AWS says it's faster than standard MySQL and PostgreSQL. The exam names RDS and Aurora as its relational examples.

## Each copy of the database has one job

![Multi-AZ standby, read replica, and automated backups and snapshots compared on how each is copied, whether it answers queries, whether it takes over by itself, whether it saves you from a mistaken delete, and its job.](../../images/05-05-three-copies.svg)

*Notice the row "Saves you from a mistaken delete?" Only the backup column says yes. And only the standby takes over by itself.*

**Long description.** Three columns. Multi-AZ standby: every write copied synchronously to another AZ; answers no queries; takes over by itself, typically in one to two minutes; doesn't save you from a mistaken delete; job, high availability. Read replica: changes copied asynchronously, so it can lag; answers read-only queries; doesn't take over by itself, but can be promoted by hand, losing any lag; doesn't save you from a mistaken delete; job, read scaling and a disaster recovery option. Automated backups and snapshots: a daily snapshot plus a log of every change; answer no queries until restored to a new database; do save you from a mistaken delete; job, going back in time. A note says this is for RDS engines other than Aurora.

### A Multi-AZ deployment keeps the database running when an Availability Zone fails

With a **Multi-AZ deployment**, RDS keeps a **standby** copy in another AZ of the same Region and writes every change to it at the same moment as to the primary. In the classic Multi-AZ DB instance deployment, the standby serves no reads or writes. If the primary's AZ, server or storage fails, RDS fails over automatically, typically in one to two minutes, and your application reconnects to the same name ([Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/), checked 2026-10-23). It doesn't fail over for slow queries or corrupted data, and a mistaken delete reaches the standby at once. So the answer to the prequestion is no: the reports would still run on the primary.

### A read replica takes read-only work off the primary

A **read replica** is a read-only copy your application can query, for reports and other read-heavy work. RDS copies changes to it a little later, so it can lag behind the primary ([Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)). It can be in another AZ or, for most engines, another Region, and you can promote it into a separate, writable database, which makes a cross-Region replica a disaster recovery option. Each replica is billed as a database of its own.

### Backups and snapshots take you back in time

RDS automated backups let you restore to any second in the retention period (7 days by default, up to 35), and manual snapshots last until you delete them (lesson 05.04). Every restore creates a new database. They're the only copy that undoes damaged or deleted data, because the standby and the replica copy the damage.

### "A read replica gives you high availability" is wrong

Some study material says a read replica makes a database highly available. For the RDS engines above, it doesn't: if the primary fails, someone has to promote the replica and point the application at it, and changes it hadn't received yet are lost. For high availability, AWS's FAQ recommends Multi-AZ. The idea is tempting because a replica is a second running copy, often in another AZ, and in **Aurora** a replica can be the automatic failover target. For the other engines, keep the jobs apart: standby for availability, replica for reads.

## Choose the database by the shape of the data

![Six cards, one per shape of data, each with its AWS database: relational, key-value, document, in-memory, graph and data warehouse.](../../images/05-06-data-shapes.svg)

*Notice that the bakery has data of almost every shape. A real business rarely fits one database.*

**Long description.** Six cards, each with a bakery example. Relational, tables with rows and columns linked to each other: orders, customers and order lines; Amazon RDS and Amazon Aurora. Key-value, one item looked up by its key, fast, at any scale: shopping carts by cart ID; Amazon DynamoDB. Document, records stored as JSON documents whose fields can vary: a product catalog; Amazon DocumentDB, and DynamoDB also stores documents. In-memory, hot data held in memory and answered in microseconds: best sellers and sign-in sessions; Amazon ElastiCache. Graph, things and the relationships between them: customers who bought this also bought; Amazon Neptune. Data warehouse, years of data from many sources, for analysis: sales by month and product; Amazon Redshift.

### DynamoDB stores items by key, at any scale, with no servers to run

**Amazon DynamoDB** is AWS's main **NoSQL** database (one that uses a model other than linked tables). AWS describes it as serverless and fully managed, with single-digit millisecond responses at any scale; it stores items you fetch by a key (a **key-value database**) and documents, and by default copies data across three AZs ([What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), checked 2026-10-23). There are no servers to size or patch, and its on-demand mode bills per request. You give up the joins between tables that relational databases do.

### The database services side by side

| Shape and need | Choose | Not this, because |
|---|---|---|
| Linked tables; transactions saved whole | **Amazon RDS** or **Amazon Aurora** | DynamoDB doesn't join tables; Redshift is for analysis |
| Items by key; any scale; no servers | **Amazon DynamoDB** | RDS needs a server sized for the peak |
| Repeated reads or sessions in microseconds | **Amazon ElastiCache**, an **in-memory database**, usually a cache in front of a main store | DynamoDB answers in milliseconds from durable storage |
| JSON documents, especially with MongoDB code | **Amazon DocumentDB**, a **document database** compatible with MongoDB | DynamoDB stores documents too, without MongoDB compatibility |
| Relationships many links deep, such as fraud rings or recommendations | **Amazon Neptune**, a **graph database** | Relational joins get complex over long chains of links |
| Analysis over years of data from many sources | **Amazon Redshift**, a **data warehouse** (Module 10) | RDS and Aurora run the business; they aren't built for huge analytical queries |
| An engine RDS doesn't offer, or the server's operating system | **A database on EC2** | You then patch, back up and build failover yourself |

Sources: each service's "What is" page, checked 2026-10-23. Amazon MemoryDB is out of scope for the exam; treat it as a distractor next to ElastiCache.

## Moving a database in: DMS moves the data, SCT converts the schema

**AWS Database Migration Service (AWS DMS)** moves the **data**: it copies a database into AWS while the source keeps running, and can keep copying each new change until you switch over ([AWS DMS FAQs](https://aws.amazon.com/dms/faqs/), checked 2026-10-23). **AWS Schema Conversion Tool (AWS SCT)** converts the **schema**, the tables, views and code that define the database, when the engine changes, for example from Oracle to Aurora PostgreSQL; it lists what it can't convert for you to finish by hand ([What is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)). Same engine: DMS alone. Different engine: SCT first, then DMS.

> **Example:** the bakery's orders link customers, orders and lines and must be saved whole: **RDS**, with **Multi-AZ** so an AZ failure loses no orders, a **read replica** for the partner's reports, and automated backups long enough to notice a mistake. The shopping carts are fetched by cart ID, swing hugely in December and are thrown away after the visit: **DynamoDB**, on demand. Three years of sales stay on the read replica until the analysis outgrows it; then **Redshift**.

> **Your turn:** the German partner's old order system runs on Oracle in its office. The partner wants it on Aurora PostgreSQL, taking orders throughout the move. Which tools, in which order, and what does each do?

<details><summary>Model answer</summary>

First **AWS SCT** (or DMS Schema Conversion), to convert the Oracle schema and code to PostgreSQL, because the engine changes. Then **AWS DMS**, to copy the data while the Oracle system keeps running and keep copying new orders until the switch-over. SCT alone moves no data, and DMS alone can't change the engine.

</details>

## Summary

- **Managed by default:** AWS recommends RDS for most relational databases; self-manage on EC2 only for a real reason, and then patches, backups and failover are yours.
- **One copy, one job:** a Multi-AZ standby (synchronous, fails over automatically) for availability; a read replica (asynchronous, read-only) for reads; backups and snapshots for going back in time.
- **A read replica isn't high availability** on the RDS engines, except as Aurora's failover target.
- **By shape:** RDS or Aurora for linked tables, DynamoDB for items by key at any scale, ElastiCache for microsecond reads, DocumentDB for MongoDB documents, Neptune for relationships, Redshift for analysis.
- **DMS moves data; SCT converts the schema** when the engine changes.

## Practice

1. **Which RDS feature provides high availability by keeping a synchronous standby in another Availability Zone, with automatic failover?**

   A. Read replicas\
   B. Multi-AZ deployment\
   C. Automated backups\
   D. Manual snapshots

   <details><summary>Feedback</summary>

   **B is right.** Multi-AZ keeps a synchronous standby in another AZ and fails over automatically.

   - **A is wrong.** Read replicas copy asynchronously and don't fail over by themselves (outside Aurora).
   - **C is wrong.** Automated backups restore to a point in time, as a new database.
   - **D is wrong.** Snapshots are point-in-time copies, not a running standby.

   </details>

2. **A gaming company needs a leaderboard that thousands of players read every second, answered in microseconds. Which service fits?**

   A. Amazon ElastiCache\
   B. Amazon Neptune\
   C. Amazon Redshift\
   D. AWS DMS

   <details><summary>Feedback</summary>

   **A is right.** ElastiCache serves data from memory in microseconds; leaderboards are a common use.

   - **B is wrong.** Neptune is for relationship-heavy data.
   - **C is wrong.** Redshift runs large analytical queries, not microsecond reads.
   - **D is wrong.** DMS migrates databases; it doesn't serve data.

   </details>

3. **A colleague says, "We have Multi-AZ and two read replicas, so we don't need backups." Why is that wrong?**

   <details><summary>Feedback</summary>

   **The standby and the replicas copy every change,** so a deleted table or a bad update reaches them within moments. Only backups or snapshots, copies that stopped changing before the mistake, can bring the data back.

   </details>

**Next:** try [Simulation S6: Multi-AZ vs read replica](10-sim-multi-az-vs-read-replica.md), then the [mastery check](11-check.md).

## Where to check the current details

- [Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/): Multi-AZ, read replicas and backups (checked 2026-10-23)
- [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) (checked 2026-10-23)
- [AWS DMS FAQs](https://aws.amazon.com/dms/faqs/) (checked 2026-10-23)

---

"Managed databases and choosing one" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
