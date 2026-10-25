---
type: page
id: clf-10-08
title: "Module 10: beyond the exam"
reader: "Adult who has finished Module 10 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-10-00]
pillars: [performance-efficiency, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html"
  - "https://aws.amazon.com/firehose/faqs/"
  - "https://aws.amazon.com/athena/pricing/"
  - "https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html"
  - "https://aws.amazon.com/workspaces-family/workspaces/faqs/"
  - "https://aws.amazon.com/iot-core/faqs/"
---

# Module 10: what we left out, and where to read it

The CLF-C02 exam asks which analytics, AI or end-user service fits a need, not how to build with it. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Analytics

- **How long streams hold data.** Kinesis Data Streams keeps records 24 hours by default and up to 365 days at extra cost; SQS keeps messages 4 days by default, 1 minute to 14 days; Firehose only buffers, for up to 900 seconds for S3 and OpenSearch destinations (as of 2026-10-24). See [Change the data retention period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) and the [Firehose FAQ](https://aws.amazon.com/firehose/faqs/).
- **Other Kinesis members.** Kinesis Video Streams takes video from cameras, and Amazon Managed Service for Apache Flink is where AWS points former Kinesis Data Analytics users. See [What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- **Schema on read, and making Athena cheaper.** Athena applies the table layout as it reads the files and charges by the data each query scans; compressing, partitioning and columnar formats such as Parquet cut both time and cost. See [Athena pricing](https://aws.amazon.com/athena/pricing/) and the [Athena FAQ](https://aws.amazon.com/athena/faqs/).
- **Redshift Spectrum, Redshift Serverless and EMR Serverless.** Ways to query S3 from Redshift, or to run a warehouse or big-data jobs without managing clusters. See [What is Amazon Redshift?](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) and [What is Amazon EMR?](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
- **OpenSearch Dashboards and domains.** Sizing a domain or going serverless, and charting logs in OpenSearch Dashboards. See [What is Amazon OpenSearch Service?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- **The rest of Amazon Quick.** Its AI agents, automation and research tools beyond Quick Sight dashboards. See [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)

## AI and machine learning

- **Building a Lex bot.** Intents (what a customer wants), slots (the details to collect), and a Lambda function to act on them; Lex V1 reached end of support on 2025-09-15. See [What is Amazon Lex V2?](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)
- **Specialized Textract and Transcribe features.** Textract's AnalyzeExpense for receipts and AnalyzeID for identity documents; Transcribe's speaker labels and removal of personal data. See [What is Amazon Textract?](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) and [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html)
- **Amazon Bedrock and Knowledge Bases.** Building generative AI applications on foundation models, and the Knowledge Bases feature AWS suggests instead of Kendra. See [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- **Opting out of content use.** AWS AI services may use customer content to improve the service; an AI services opt-out policy in AWS Organizations stops that. See [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html).
- **AI service prices.** Per character for Polly and Translate, per second of audio for Transcribe, per page for Textract; Q Developer's Pro tier no longer takes new subscriptions. See [Amazon Polly pricing](https://aws.amazon.com/polly/pricing/) and [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/).

## People, apps and devices

- **WorkSpaces billing.** Monthly billing is a fixed fee; hourly billing is a low monthly fee plus each hour run, and AutoStop stops a desktop a set time after the user disconnects (60 minutes by default). The break-even depends on the bundle and Region. See the [Amazon WorkSpaces FAQs](https://aws.amazon.com/workspaces-family/workspaces/faqs/).
- **Connect Customer's own AI self-service,** which AWS now steers new builds toward alongside Lex. See [Connect Customer AI self-service](https://docs.aws.amazon.com/connect/latest/adminguide/generative-ai-powered-self-service.html).
- **SES production access.** New accounts start in the SES sandbox, sending only to verified addresses until AWS grants production access. See the [Amazon SES FAQs](https://aws.amazon.com/ses/faqs/).
- **IoT Core in depth.** Device Shadows (a stored copy of each device's last reported state), certificates and policies, and rule actions. AWS IoT Greengrass and Device Defender are out of the exam's scope. See the [AWS IoT Core FAQs](https://aws.amazon.com/iot-core/faqs/) and [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

## Well-Architected practices

Picking the store that fits the access pattern ([PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html)), protecting sensitive data such as receipts and call recordings ([SEC07-BP02 Apply data protection controls based on data sensitivity](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html)) and comparing billing models ([COST07-BP01 Perform pricing model analysis](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_analysis.html)) belong to designing workloads, not to this exam.

---

"Module 10: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
