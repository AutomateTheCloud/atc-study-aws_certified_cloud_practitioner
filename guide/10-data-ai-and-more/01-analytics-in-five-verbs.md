---
type: lesson
id: clf-10-01
title: "Analytics in five verbs"
tasks: ["3.7"]
objectives: ["10.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 09 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-05-05, clf-05-01, clf-09-00]
terms_introduced: [data pipeline, streaming data, data lake, data catalog, ETL, search index, business intelligence, Amazon Kinesis, Amazon Kinesis Data Streams, Amazon Data Firehose, replay, AWS Glue, AWS Glue Data Catalog, crawler, Amazon Athena, Amazon EMR, Amazon OpenSearch Service, Amazon Quick Sight, Amazon Quick]
pillars: [performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/streams/latest/dev/introduction.html"
  - "https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html"
  - "https://aws.amazon.com/kinesis/data-streams/faqs/"
  - "https://aws.amazon.com/sqs/faqs/"
  - "https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html"
  - "https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html"
  - "https://docs.aws.amazon.com/athena/latest/ug/what-is.html"
  - "https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html"
  - "https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html"
  - "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html"
  - "https://docs.aws.amazon.com/quick/latest/userguide/what-is.html"
  - "https://aws.amazon.com/what-is/data-lake/"
---

# Every analytics service does one of five jobs: ingest, catalog, query, search or visualize

Getting from raw data to an answer takes five jobs, and AWS has a service for each. Place a service on its verb, and you can rule out the ones that only sound similar.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Managed databases and choosing one](../05-storing-data/05-managed-or-self-managed-databases.md) (Redshift). It answers the first of the bakery's requests in the [module brief](00-brief.md), the sales dashboard.

## Warm-up: what you remember

1. From Module 05: the accountant wants total sales by month and cake for the last three years. Should that run on the order database?

<details><summary>Feedback</summary>

1. **No.** It's analytics work: a few big queries over a lot of history, which could slow the website's many small reads and writes. That's why analytics gets its own tools.

</details>

## What you'll learn

By the end of this lesson, you can place each AWS analytics service on one of the five jobs of an analytics pipeline (objective 10.01a), and tell apart the services the exam pairs as wrong answers.

Try this before you read on, and guess if you're unsure: the bakery keeps a year of website logs as files in S3. Which service lets it run SQL on those files without loading them anywhere or running a server?

## The big picture: five verbs, from raw data to a dashboard

A **data pipeline** is the path data takes from where it's created to the screen where someone reads the answer. Each AWS analytics service does one step.

![An analytics pipeline from ingest through the S3 data lake to catalog, query and visualize, with search as a side branch; each step names its AWS services.](../../images/10-01-pipeline.svg)

*Notice the highlighted step, catalog. It's the verb people forget, and the reason Athena can treat a folder of files as a table.*

**Long description.** Top to bottom: ingest lands records in Amazon S3, the data lake, as files; catalog (highlighted) describes them; query answers questions; visualize shows the answers. Search is a side branch fed from Firehose. The table below names each step's services.

| Verb | The question it answers | AWS services on the exam |
|---|---|---|
| **Ingest** | How does the data get in, as it happens? | Amazon Kinesis Data Streams; Amazon Data Firehose |
| **Catalog** | What's in these files, and is it clean? | AWS Glue |
| **Query** | What does the data say? | Amazon Athena; Amazon Redshift; Amazon EMR |
| **Search** | Where does this word or error appear? | Amazon OpenSearch Service |
| **Visualize** | How do people in the business see it? | Amazon Quick Sight |

A **data lake** is one central store that keeps data of many kinds in its original form, for analysis later; on AWS it's usually an S3 bucket ([What is a data lake?](https://aws.amazon.com/what-is/data-lake/)).

## Ingest: Data Streams holds records for your programs; Firehose delivers them for you

**Streaming data** arrives continuously, a little at a time, such as clicks on a website. **Amazon Kinesis** is a family of services for streaming data, so ask which member a question means ([What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), checked 2026-10-24).

- **Amazon Kinesis Data Streams** keeps records in a stream for your own programs to read. Several programs can read the same records, and because records stay after they're read (24 hours by default), a program can read them again, called **replay**.
- **Amazon Data Firehose** (formerly Amazon Kinesis Data Firehose) delivers streaming data for you to a destination such as Amazon S3, Amazon Redshift or Amazon OpenSearch Service. You write no programs and manage no servers ([What is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), checked 2026-10-24).

> **Misconception:** "Kinesis Data Firehose is the current name." It isn't: AWS renamed it **Amazon Data Firehose**; an answer that says "Kinesis Data Firehose" means the same service. The old name sticks because Firehose is still in the Kinesis family.

**Amazon SQS** (Module 08), a message queue whose workers delete each message once the job is done, often appears beside these two as a wrong answer. What settles most questions is what happens after the data is read: records stay in Data Streams, Firehose hands data on, and SQS messages are deleted ([Kinesis Data Streams FAQ](https://aws.amazon.com/kinesis/data-streams/faqs/); [Amazon SQS FAQ](https://aws.amazon.com/sqs/faqs/), checked 2026-10-24).

| If the need is… | Choose | Not this, because… |
|---|---|---|
| Several programs read the same live data, and you may need to read it again | **Kinesis Data Streams** | SQS deletes each message once handled; Firehose only delivers |
| Land streaming data in S3, Redshift or OpenSearch Service with no code | **Amazon Data Firehose** | Data Streams needs consumer programs that you write |
| Pass jobs from one part of an application to a worker | **Amazon SQS** | A stream is for analyzing a flow of records, not handing out tasks |

> **Misconception:** "Kinesis Data Analytics runs SQL on the stream." Not any more: AWS stopped new Kinesis Data Analytics for SQL applications on 2025-10-15 and began deleting existing ones on 2026-01-27 ([Kinesis Data Analytics for SQL](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html), checked 2026-10-24). It's tempting because the name fits the job so well; treat it as a wrong answer.

## Catalog and query: describe the files, then ask them questions

### Catalog: Glue records what your data looks like and gets it ready

**AWS Glue** is a serverless data integration service that finds, describes, cleans and moves data ([What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), checked 2026-10-24). A **data catalog** lists what data you have, where it is and what its columns are. The **AWS Glue Data Catalog** holds a table definition for each set of files, which Athena, EMR and Redshift read. **Crawlers** scan your data and add the tables for you, and **ETL** jobs (extract, transform, load) clean or reshape data and put it where it will be analyzed.

Glue prepares data so that a query service can answer questions; it doesn't answer them itself. "Discovers, catalogs or transforms" points to Glue; "runs the query" doesn't.

### Query: Athena, Redshift and EMR answer questions in three different ways

- **Amazon Athena** runs standard SQL directly on files in S3, such as CSV, JSON or Parquet, and the files stay as they are. It's serverless: nothing to set up, and you pay for each query by the data it scans ([What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), checked 2026-10-24).
- **Amazon Redshift**, from Module 05, is a data warehouse. You load data from many sources into it, and it's built for complex queries that join many very large tables, run again and again for reports ([When should I use Athena?](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html)).
- **Amazon EMR** (formerly Amazon Elastic MapReduce) is a managed cluster platform for big-data frameworks such as Apache Spark and Apache Hadoop, where you run your own code on very large datasets ([What is Amazon EMR?](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)).

![Athena, Redshift, EMR and Glue compared side by side on main job, where the data is, and when to choose each.](../../images/10-01-query-compared.svg)

*Notice the last column. Glue appears in the same exam questions as the other three, but its job is preparing data, not answering questions about it.*

**Long description.** Four columns compared on three rows. Main job (highlighted): SQL on files where they sit; a data warehouse; Spark, Hadoop and similar frameworks; cataloging and preparing data. Where the data is: in S3, unchanged; loaded into Redshift; usually S3; wherever Glue connects. Choose it when: ad hoc questions about files in S3; complex, repeated reports from many sources; your own big-data code; making data findable and clean.

That answers the prequestion: the logs are files in S3, the questions are few, and nobody wants a server, so the answer is **Athena**.

## Search and visualize: find words fast, show answers to people

### Search: OpenSearch Service finds words and patterns in text and logs

**Amazon OpenSearch Service** (successor to Amazon Elasticsearch Service) runs OpenSearch, an open-source search and analytics engine, for log analytics, application monitoring and website search ([What is Amazon OpenSearch Service?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html), checked 2026-10-24). It keeps a **search index**, a list of which words appear in which records. Athena reads files to answer a SQL question; OpenSearch Service has already indexed every word, so a search for `payment failed` comes back at once, best matches first.

### Visualize: Quick Sight turns answers into dashboards

**Amazon Quick Sight** is AWS's **business intelligence (BI)** service: it connects to sources such as Athena, Redshift, RDS or uploaded files and builds interactive dashboards. If a question asks for "dashboards" or "visualizations for business users", the answer is Quick Sight, not the service that ran the query. Quick Sight is now part of a wider product, **Amazon Quick** ([What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html), checked 2026-10-24).

> **Misconception:** "QuickSight is the current name." It isn't: the same BI service is now **Amazon Quick Sight**, part of **Amazon Quick**. Older questions, and some AWS pages, still write "Amazon QuickSight", which keeps the old name alive.

> **Example:** the owner's dashboard. Orders are copied nightly from RDS to S3, and page views stream into S3 through **Firehose** (nobody needs replay, so not Data Streams). A **Glue** crawler catalogs both folders, **Athena** joins them with SQL (the data is small and the questions few, so not Redshift yet), and **Quick Sight** shows the result each morning.

> **Your turn:** A year later, the bakery has ten shops, a loyalty app and a supplier system, and the finance team runs the same 40 complex reports every morning, joining all of them. Which step of the pipeline changes, and to what?

<details><summary>Model answer</summary>

**The query step moves to Amazon Redshift.** Regular, complex reports joining data from many sources are the warehouse case. Quick Sight can read from Redshift, and Athena can still serve one-off questions on the files in S3.

</details>

## Summary

- **Five verbs:** ingest, catalog, query, search, visualize. Place each service on its verb first.
- **Ingest:** Kinesis Data Streams keeps records for your programs to read and replay; Amazon Data Firehose (formerly Kinesis Data Firehose) delivers streaming data with no code; SQS deletes each message once handled.
- **Catalog:** AWS Glue catalogs, discovers and cleans data. It doesn't answer questions.
- **Query:** Athena runs SQL on files in S3 with no servers; Redshift is the warehouse for complex, repeated reports from many sources; EMR runs your own big-data code.
- **Search and visualize:** OpenSearch Service indexes text and logs; Amazon Quick Sight (formerly QuickSight) turns results into dashboards.

## Practice

1. **A company wants one service to discover its data in S3, record its columns in a central catalog, and convert CSV files to Parquet each night. Which service?**

   A. Amazon Athena\
   B. AWS Glue\
   C. Amazon Quick Sight\
   D. Amazon Data Firehose

   <details><summary>Feedback</summary>

   **B is right.** Crawlers, the Data Catalog and ETL jobs are Glue's three parts.

   - **A is wrong.** Athena runs queries; it doesn't run conversion jobs.
   - **C is wrong.** Quick Sight builds dashboards.
   - **D is wrong.** Firehose delivers streaming data; it doesn't catalog data already in S3.

   </details>

2. **A game's click events must be read live by two separate programs: one updates a leaderboard within seconds, the other archives everything. After a bug, the team wants to reprocess the last six hours. Which service?**

   A. Amazon SQS\
   B. Amazon Data Firehose\
   C. Amazon Kinesis Data Streams\
   D. Amazon Redshift

   <details><summary>Feedback</summary>

   **C is right.** Several programs can read the same records, and records stay after they're read, so the team can replay them.

   - **A is wrong.** An SQS message is deleted once a worker handles it.
   - **B is wrong.** Firehose delivers data to a destination; your programs don't read or replay it.
   - **D is wrong.** Redshift is a warehouse for reports, not a stream that programs read within seconds.

   </details>

3. **Match each need to its verb and service: (a) a weekly chart of sales for the managers; (b) search the support team's emails for a product name; (c) a finance team's daily complex reports joining five systems' data.**

   <details><summary>Feedback</summary>

   (a) **Visualize: Amazon Quick Sight.** (b) **Search: Amazon OpenSearch Service**, because finding words in text is a search index's job. (c) **Query: Amazon Redshift**, the warehouse for repeated, complex reports over data from many sources.

   </details>

**Next:** lesson 10.02, [AI and machine learning](02-ai-and-ml.md). To run Athena yourself, do [Optional lab 13](04-lab-13-athena-query.md).

## Where to check the current details

- [What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) and [What is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) (checked 2026-10-24)
- [When should I use Athena?](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html): Athena compared with Redshift and EMR (checked 2026-10-24)
- [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html), including Quick Sight (checked 2026-10-24)

---

"Analytics in five verbs" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
