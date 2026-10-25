---
type: page
id: clf-05-12
title: "Module 05: beyond the exam"
reader: "Adult who has finished Module 05 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-05-00]
pillars: [reliability, cost-optimization, performance-efficiency]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/ebs/faqs/"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html"
  - "https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html"
  - "https://aws.amazon.com/dynamodb/faqs/"
  - "https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html"
---

# Module 05: what we left out, and where to read it

The CLF-C02 exam asks which storage or database service fits a need, not how to configure it. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Storage

- **EBS volume types and durability.** Volume types trade cost against performance, and their designed durability differs: 99.8% to 99.9% for most, higher for io2 Block Express (as of 2026-10-23). See the [Amazon EBS FAQs](https://aws.amazon.com/ebs/faqs/).
- **The other FSx file systems.** FSx for NetApp ONTAP and FSx for OpenZFS serve teams already using those systems; FSx for Lustre is a high-speed file system that the exam lists as out of scope. See [When to choose Amazon FSx](https://aws.amazon.com/fsx/when-to-choose-fsx/).
- **More S3 encryption choices.** Besides SSE-S3 and SSE-KMS, there's SSE-C, where you supply the key with each request (turned off for new buckets since April 2026 until you enable it), and client-side encryption. See [Protecting data with encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html).
- **MFA Delete and Object Lock modes.** MFA Delete makes a permanent delete need the account's MFA code, and only the root user can turn it on. Object Lock has more than one retention mode. See [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) and the [Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/).
- **Storage class billing details.** Standard-IA, One Zone-IA and Glacier Instant Retrieval bill objects under 128 KB as 128 KB; Flexible Retrieval and Deep Archive add about 40 KB of billed metadata per object; each lifecycle transition is a billed request; Flexible Retrieval offers expedited, standard and bulk restores. Two more classes exist: S3 Express One Zone and Reduced Redundancy Storage. See [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).
- **Costing a lifecycle rule.** Working out a year of storage, minimum-stay charges and piled-up versions is cost arithmetic beyond the exam. See [Setting an S3 Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).
- **Volume Gateway modes.** In cached mode the full data lives in AWS and busy data stays local; in stored mode the full data stays local and AWS holds point-in-time copies. Amazon FSx File Gateway has been closed to new customers since 2024-10-28. See the [Storage Gateway documentation](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html).
- **AWS Backup in depth.** Vault Lock has a governance mode as well as compliance mode; backups moved to cold storage must be kept 90 days or you pay for the rest. See [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) and [AWS Backup pricing](https://aws.amazon.com/backup/pricing/).
- **Running Elastic Disaster Recovery.** Staging areas, drills and failing back once the original site is fixed. See [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- **Moving data in.** AWS DataSync copies data online; AWS Data Transfer Terminal lets you upload from your own drives at an AWS site. See [What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) and [AWS Snowball](https://aws.amazon.com/snowball/).

## Databases

- **Multi-AZ DB clusters.** A newer Multi-AZ form with two standbys in three AZs that can also serve reads. See [Configuring and managing a Multi-AZ deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).
- **Read replica limits by engine.** How many replicas each engine allows, and the licenses some need. See [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).
- **RDS billing.** Per-second billing with a 10-minute minimum, a stopped database that RDS starts again after seven days, and Reserved Instances or Database Savings Plans for steady databases. See [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/) and [Stopping an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html).
- **Aurora in depth.** Storage that grows by itself, a serverless option, and replicas as failover targets. See the [Amazon Aurora FAQ](https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq.html).
- **DynamoDB features.** On-demand and provisioned capacity, global tables across Regions, DynamoDB Accelerator (DAX) as a cache, and point-in-time recovery. See the [DynamoDB FAQs](https://aws.amazon.com/dynamodb/faqs/) and [on-demand pricing](https://aws.amazon.com/dynamodb/pricing/on-demand/).
- **ElastiCache engines.** Valkey, Memcached and Redis OSS, serverless or on nodes you choose. See [What is Amazon ElastiCache?](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
- **Migration details.** Change data capture, DMS Schema Conversion inside the DMS console, and homogeneous vs heterogeneous migrations. See [What is AWS DMS?](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)

## Well-Architected practices for data

Backing up by policy and proving you can restore ([REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html)), retention rules ([COST04-BP05 Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html)) and purpose-built data stores ([PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html)) belong to designing workloads, not to this exam.

---

"Module 05: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
