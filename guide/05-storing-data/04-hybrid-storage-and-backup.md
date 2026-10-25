---
type: lesson
id: clf-05-04
title: "Hybrid storage and backup"
tasks: ["3.6", "2.1"]
objectives: ["05.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 04, the guardrails primer and lessons 05.01 and 05.02; about 20 minutes; works on a phone"
prerequisites: [clf-05-01, clf-05-02, clf-03-03, clf-02-01]
terms_introduced: [hybrid storage, iSCSI, cache, AWS Storage Gateway, S3 File Gateway, Volume Gateway, Tape Gateway, snapshot, automated backup, AWS Backup, backup plan, backup vault, Vault Lock, AWS Elastic Disaster Recovery, AWS DataSync]
pillars: [reliability, security]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/storagegateway/faqs/"
  - "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html"
  - "https://aws.amazon.com/rds/faqs/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"
  - "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"
  - "https://aws.amazon.com/backup/faqs/"
  - "https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html"
  - "https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html"
  - "https://aws.amazon.com/disaster-recovery/faqs/"
  - "https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html"
  - "https://aws.amazon.com/snowball/"
---

# Storage Gateway lets the shop keep working while its data lives in AWS; backups bring data back, and disaster recovery brings servers back

AWS Storage Gateway connects software in your building to AWS storage without changing the software. AWS Backup runs backups of many AWS services from one set of rules. AWS Elastic Disaster Recovery keeps whole servers ready to launch in minutes.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson uses EBS and S3 from [lesson 05.01](01-block-file-object.md), the S3 Glacier classes from [lesson 05.02](02-s3-in-practice.md), and RTO and RPO from [Surviving failure](../03-aws-around-the-world/03-surviving-failure.md).

## Warm-up: what you remember

1. The bakery runs its website at AWS and its till system on a computer in the shop, with orders flowing between them. Which deployment model is that?
2. The order database runs on Amazon RDS. Who takes its backups, and who decides how long they're kept?

<details><summary>Feedback</summary>

1. **Hybrid:** some parts run at AWS and some on premises, connected (lesson 02.01).
2. **AWS takes them** (lesson 04.01), but **the bakery** chooses the settings, such as how many days to keep them.

</details>

## What you'll learn

By the end of this lesson, you can match a hybrid storage or backup need to AWS Storage Gateway, snapshots, AWS Backup or AWS Elastic Disaster Recovery, and reject the ones that look similar (objective 05.04a).

Try this before you read on, and guess if you're unsure: the till server in the shop must be running again within 15 minutes if its hardware dies. Is a nightly backup enough?

## Storage Gateway lets on-premises software use AWS storage without changing

**AWS Storage Gateway** is a **hybrid storage** service: software in your building keeps talking to storage the way it always has, while the data is stored in AWS. The gateway runs on premises, usually as a virtual machine, and keeps frequently used data in a local **cache** (a nearby copy, kept so reads are fast) ([AWS Storage Gateway FAQs](https://aws.amazon.com/storagegateway/faqs/)). That cache is why the exam guide gives Storage Gateway as its example of a "cached file system".

![Three Storage Gateway types side by side: S3 File Gateway, Volume Gateway and Tape Gateway, each showing what the software in the shop sends and where the data lands in AWS.](../../images/05-04-gateway-types.svg)

*Notice that the top box is the same in every column: software that doesn't change. Only the protocol and where the data lands differ.*

**Long description.** Three columns. S3 File Gateway: apps in the shop send files over NFS or SMB to the gateway, which caches recent files and stores them as objects in an S3 bucket. Volume Gateway: servers use disks over iSCSI; in cached mode the data lives in S3 with busy data cached locally, and in stored mode the data stays local with point-in-time copies in AWS as EBS snapshots. Tape Gateway: backup software writes virtual tapes over iSCSI; the tapes are stored in S3 and archived to the S3 Glacier classes. A note says Amazon FSx File Gateway has been closed to new customers since 2024-10-28.

Each type looks like something the software already knows:

- **Amazon S3 File Gateway** looks like a shared folder (NFS or SMB) and stores each file as an object in S3.
- **Volume Gateway** looks like disks, over **iSCSI** (the protocol for reaching disks over a network), and keeps the data in AWS, with point-in-time copies as EBS snapshots.
- **Tape Gateway** looks like a tape library to existing backup software and archives the virtual tapes to the S3 Glacier classes.

## Snapshots, AWS Backup and Elastic Disaster Recovery

All three keep a copy in AWS. They differ in what they copy, how often, and what you get back.

**A snapshot** is a point-in-time copy of one disk or one database; restoring it gives you a new one as it was then. An **EBS snapshot** outlives its volume and can be restored in any AZ of its Region or copied to another Region ([Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)). RDS **automated backups** let you restore to any second within the retention period, 7 days by default and up to 35, but they're deleted with the database unless you choose to retain them; manual snapshots stay until you delete them ([Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/); [Deleting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html), checked 2026-10-24).

### AWS Backup runs backups for many services from one set of rules

**AWS Backup** puts backups for many AWS services, and some on-premises systems, under one set of rules ([What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)). You write a **backup plan** (how often, how long to keep each backup, where to copy it) and assign resources to it, for example by tag. It covers EC2, EBS, S3, EFS, FSx, RDS, DynamoDB and more, across accounts, and can copy backups to another Region or account. Backups are kept in a **backup vault**; with **Vault Lock** in compliance mode, once its grace period ends, no one, not even the root user, can delete them before their retention ends ([AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)). It governs only the backups it manages, not snapshots someone takes by hand.

### Elastic Disaster Recovery keeps whole servers ready to launch

**AWS Elastic Disaster Recovery** (AWS DRS) protects whole servers: their disks, operating system and applications. It copies every change to their disks, continuously, into low-cost storage in an AWS Region; after a disaster you launch recovery servers there within minutes. AWS says it supports recovery points of seconds and recovery times of minutes ([What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html), checked 2026-10-23). You can run drills without disturbing the servers it protects. AWS's FAQ draws the line: a backup is an extra copy of your **data**; disaster recovery restores your **applications and servers** quickly ([AWS Elastic Disaster Recovery FAQs](https://aws.amazon.com/disaster-recovery/faqs/)).

![A snapshot, AWS Backup and Elastic Disaster Recovery compared on the job each does, what it copies, how often, what you get back and how fast.](../../images/05-04-backup-dr-snapshot.svg)

*Notice the last row. Only Elastic Disaster Recovery gives you running servers; the other two give you data to restore.*

**Long description.** Three columns compared. A snapshot copies one EBS volume or RDS database, when you take one or on a schedule, and gives back a new volume or database as it was. AWS Backup copies many resources across services and accounts, chosen by tag, on a plan's schedule, and gives back recovery points of your data, also copied to other Regions or accounts; servers still need relaunching. Elastic Disaster Recovery copies whole servers continuously and gives back running recovery servers; AWS says seconds of data lost and running again in minutes.

> **Your turn:** answer the prequestion. The till server must run again within 15 minutes if its hardware dies, losing at most a minute of sales. A nightly backup to AWS exists. Is it enough, and if not, what closes the gap?

<details><summary>Model answer</summary>

**No.** A nightly backup can lose a day of sales, and restoring it onto a new server takes far longer than 15 minutes. **Elastic Disaster Recovery** copies every change continuously and launches the server in AWS within minutes. Keep the backup too, for when a mistake or an attack damages the data.

</details>

## Moving data once, without Snowball

### "Snowball is the answer for moving lots of data" is wrong

You may have learned that AWS Snowball, a storage device AWS ships to you, is how you move terabytes into AWS. That's out of date: Snowball Edge stopped taking new customers on 2025-11-07, and AWS ends support for Snowball devices in its commercial Regions on 2026-12-31 ([AWS Snowball](https://aws.amazon.com/snowball/), checked 2026-10-23). It's tempting because Snowball was the textbook answer for years. The exam guide no longer lists it, so treat it as a wrong answer. For moving data once, over the network, AWS now points to **AWS DataSync**, which copies between on-premises storage, other clouds and AWS storage ([What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)). DataSync isn't in the exam's service list either.

> **Example:** the owner's list, matched by where the software runs and what must come back. Nightly backups of the order database and the web server's disk, copied to a second Region: **AWS Backup**, one plan for both. Invoices that staff save to the shop's shared folder, kept in AWS: **S3 File Gateway**. The German partner's weekly backups to tape: **Tape Gateway**, sending the tapes to an EU Region.

**Your side of the line:** AWS runs these services and keeps backups durable and encrypted. You decide what's backed up, how often and for how long, who may delete backups, and which Regions copies go to, and you run the drills and test restores.

## Summary

- **Storage Gateway** lets on-premises software keep working while the data lives in AWS: S3 File Gateway looks like a shared folder, Volume Gateway like disks, Tape Gateway like a tape library.
- **A snapshot** is a point-in-time copy of one disk or database. RDS automated backups are deleted with the database unless you choose to retain them.
- **AWS Backup** runs backups for many services and accounts from one plan, copies them to other Regions or accounts, and can lock them with Vault Lock.
- **Elastic Disaster Recovery** copies whole servers continuously and launches them in minutes: backups bring back data, disaster recovery brings back servers.

## Practice

1. **Which AWS service lets an on-premises backup application keep writing to "tapes" while the data is stored in AWS?**

   A. AWS Backup\
   B. Tape Gateway, a type of AWS Storage Gateway\
   C. AWS DataSync\
   D. S3 Glacier Deep Archive

   <details><summary>Feedback</summary>

   **B is right.** Tape Gateway looks like a tape library to the backup software and stores the virtual tapes in AWS.

   - **A is wrong.** AWS Backup manages backups of resources; it doesn't pose as a tape library.
   - **C is wrong.** DataSync moves files and objects over the network; it isn't a tape interface.
   - **D is wrong.** Archived tapes can end up there, but software can't write to it as tapes.

   </details>

2. **A company wants its on-premises servers to restart in AWS within minutes after a site failure, losing only seconds of data, and wants to test this without disturbing production. Which service fits?**

   A. AWS Backup\
   B. AWS Elastic Disaster Recovery\
   C. Amazon EBS snapshots\
   D. AWS Snowball

   <details><summary>Feedback</summary>

   **B is right.** It copies servers continuously, launches them within minutes, and supports drills that don't disturb the source.

   - **A is wrong.** It restores data from scheduled backups; servers must still be relaunched.
   - **C is wrong.** EBS snapshots copy volumes already in AWS; they don't launch servers.
   - **D is wrong.** Snowball moved data on a device and is being retired.

   </details>

3. **A company has 200 EBS volumes and 30 RDS databases in three accounts. Its auditor wants each backed up daily, kept 90 days and copied to a second Region. Which service fits best, and why not snapshots taken by each team?**

   <details><summary>Feedback</summary>

   **AWS Backup.** One plan covers both services across the accounts, keeps each backup 90 days and copies it to another Region. Snapshots taken by each team could work, but nothing would enforce one schedule across them.

   </details>

**Next:** [Managed databases and choosing one](05-managed-or-self-managed-databases.md).

## Where to check the current details

- [AWS Storage Gateway FAQs](https://aws.amazon.com/storagegateway/faqs/) (checked 2026-10-23)
- [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) (checked 2026-10-23)
- [AWS Elastic Disaster Recovery FAQs](https://aws.amazon.com/disaster-recovery/faqs/) (checked 2026-10-23)

---

"Hybrid storage and backup" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
