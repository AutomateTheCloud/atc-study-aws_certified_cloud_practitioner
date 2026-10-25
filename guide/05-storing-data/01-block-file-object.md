---
type: lesson
id: clf-05-01
title: "Block, file and object storage"
tasks: ["3.6", "4.1", "2.1"]
objectives: ["05.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 04 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-02-03, clf-03-01, clf-04-01]
terms_introduced: [block storage, file storage, object storage, volume, Amazon EBS, EBS snapshot, instance store, persistent, Amazon EFS, NFS, SMB, Amazon FSx, Amazon S3, bucket, object, key, metadata]
pillars: [performance-efficiency, reliability, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html"
  - "https://aws.amazon.com/ebs/faqs/"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html"
  - "https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html"
  - "https://aws.amazon.com/efs/faq/"
  - "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html"
  - "https://aws.amazon.com/s3/faqs/"
  - "https://aws.amazon.com/s3/pricing/"
---

# Block storage is a disk for one server, file storage is a shared folder, and object storage is a bucket you reach over the web

AWS sells storage in three shapes. Pick the shape from how a program reaches the data, and the service follows.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson uses durability from [lesson 02.03](../02-why-the-cloud/03-telling-the-benefits-apart.md) and Availability Zones from [lesson 03.01](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md).

## Warm-up: what you remember

1. S3 Standard is designed for "eleven nines" of durability and 99.99% availability (as of 2026-10-23). What does each number promise?

<details><summary>Feedback</summary>

1. **Durability:** the data will still exist later. **Availability:** you can reach it right now (lesson 02.03).

</details>

## What you'll learn

By the end of this lesson, you can name the AWS services for block, file and object storage, and choose one for an access pattern (objective 05.01a).

Try this before you read on, and guess if you're unsure: a server's fastest disk is "instance store". The server is stopped overnight and started in the morning. Is the data on that disk still there?

## The big picture: three shapes of storage

![Three panels: block storage, a disk for one server (EBS, instance store); file storage, a folder tree that several servers share (EFS, FSx); object storage, whole objects in a bucket, reached over HTTPS (S3).](../../images/05-01-three-kinds.svg)

*Notice who connects in each panel: one server to a block disk, several servers to a file system, and any allowed program, from anywhere, to an object bucket.*

**Long description.** Three panels. Block, "a disk for one server": one server and a disk of numbered blocks; Amazon EBS and EC2 instance store. File, "a shared folder tree": three servers use one tree of folders at once; Amazon EFS and Amazon FSx. Object, "whole objects in a bucket": an app and a phone reach a bucket over HTTPS, and each object has a key, data and metadata; Amazon S3.

- **Block storage** is a disk that one server sees as its own and formats. One such disk is a **volume**.
- **File storage** is a shared tree of folders and files that many servers use over the network at once. Linux usually shares files with **NFS**, Windows with **SMB**.
- **Object storage** keeps whole files, called **objects**, in a **bucket**, reached through a web API. Each object has a **key** (its name) and **metadata** (facts about it, such as its type).

## Block storage: a disk attached to one server

**Amazon Elastic Block Store (Amazon EBS)** provides volumes that you attach to an EC2 instance and use like a local drive ([What is Amazon EBS?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)). A volume and its instance must be in the same Availability Zone, and AWS copies the volume's data within that one AZ. A volume is **persistent**: it exists apart from the instance, so its data is kept when the instance stops ([Amazon EBS FAQs](https://aws.amazon.com/ebs/faqs/)). An **EBS snapshot** is a point-in-time copy of a volume that persists on its own, and you can create new volumes from it (lesson 05.04).

**EC2 instance store** is temporary block storage on disks physically attached to the computer that runs your instance. Not every instance type has it. It suits caches and scratch data, where losing it is fine.

![A grid of four server events, reboot, stop, hibernate and terminate, showing whether data on EBS and on instance store is kept; the table below gives the same facts.](../../images/05-01-what-survives.svg)

*Notice that a reboot is the only event instance store survives.*

| Server event | Data on an EBS volume | Data on instance store |
|---|---|---|
| Reboot | Kept | Kept |
| Stop or hibernate | Kept | Lost |
| Terminate (delete the server) | Kept only if the volume's **Delete on termination** setting is No | Lost |

### "Instance store survives a stop" is wrong

You may have read that instance store data is still there after you stop and start the server. It's gone: AWS says it persists through a reboot, but a stop, hibernation or termination erases it ([Data persistence for instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html), checked 2026-10-24). That answers the prequestion.

The mistake is easy because a reboot keeps the data, and "stop" sounds like a longer reboot. It isn't: instance store disks belong to the physical computer, and a stop releases them.

## File storage: one folder tree that many servers share

**Amazon Elastic File System (Amazon EFS)** is AWS's own file system for Linux, using NFS ([What is Amazon EFS?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)). Up to thousands of EC2 instances can connect at once, along with containers, Lambda functions and on-premises servers, and it grows and shrinks with your files. A **Regional** file system stores data across several AZs; a **One Zone** file system keeps it in one AZ, where it can be lost with the AZ. AWS doesn't support EFS with Windows-based EC2 instances ([Amazon EFS FAQ](https://aws.amazon.com/efs/faq/)).

**Amazon FSx** runs well-known third-party file systems for you, so applications move without changes. **FSx for Windows File Server** gives Windows file shares over SMB, joined to Microsoft Active Directory ([What is FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)): the usual answer for "Windows" plus "shared files". FSx also offers NetApp ONTAP and OpenZFS, and FSx for Lustre, which the exam guide lists as out of scope.

## Object storage: whole objects in a bucket, reached over the web

**Amazon Simple Storage Service (Amazon S3)** is AWS's object storage. You create a bucket in a Region and upload objects to it; a program stores or reads a whole object with one request. There's no disk to attach and no folder to mount. Total data and the number of objects are unlimited ([Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/)), any program you allow can reach it, and objects stay in their bucket's Region unless you copy them out. S3 Standard keeps copies in at least three AZs.

AWS lists its uses as backup and restore, archives, media, website files, mobile apps and **data lakes** (large collections of raw data for analysis): whole files, rarely changed, read by many programs.

### "The largest S3 object is 5 TB" is out of date

You may have read that one S3 object can be at most 5 TB. That figure is old: the S3 FAQ, checked on 2026-10-23, says an object can be up to **50 TB**. It's tempting because older courses and practice questions still say 5 TB.

## Block, file and object side by side

| | Block (EBS, instance store) | File (EFS, FSx) | Object (S3) |
|---|---|---|---|
| What a program sees | A disk | Folders and files | Whole objects, by key |
| How many computers | One (a few, in special cases) | Many at once | Any allowed program, anywhere |
| Where the copies live | EBS: one AZ. Instance store: one host | EFS Regional: several AZs. One Zone: one AZ | S3 Standard: at least three AZs |
| Choose it for | Boot disks, a database on one server, scratch space | Shared content; moving an existing file server | Photos, media, backups, archives, data lakes |

> **Your turn:** the site runs on two Linux web servers in two AZs, so it survives an AZ failure. Both must show the same menu files, which the owner edits every week. Which storage shape and service fit, and why not EBS?

<details><summary>Model answer</summary>

**File storage, Amazon EFS (Regional).** Both Linux servers need the same files at once, and a Regional file system keeps data across AZs, so it keeps working if one AZ fails. Not EBS: a volume attaches to one server in one AZ.

</details>

### What you pay for

Checked 2026-10-23: **EBS** bills what you **provision**, the volume's size, full or empty, so it behaves like a small fixed cost. Instance store is included in the instance's price. **EFS**, **FSx** and **S3** bill what you **use**; for S3, that's storage per GB-month, requests and data transferred out ([Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)).

### Your side of the line

AWS runs the disks, replaces failed ones and copies data as each service is designed. You decide who can reach each file system and bucket, whether to take snapshots or backups, and whether EBS volumes are encrypted: in the new account we created on 2026-10-23, that setting was off until [primer page 06](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md) turned it on.

## Summary

- **Block** storage is a disk for one server: EBS volumes persist apart from the instance and live in one AZ; instance store survives a reboot but not a stop.
- **File** storage is a folder tree many servers share: EFS for Linux over NFS, FSx for a familiar file system, such as Windows shares over SMB.
- **Object** storage keeps whole objects in a bucket, reached through a web API: S3, with no capacity to plan.
- **Start from the access pattern;** the shape, then the service, follows. EBS bills what you provision; S3 and EFS bill what you use.

## Practice

1. **A video-editing company runs a group of Linux servers that must all read and write the same project files at the same time. Which service fits best?**

   A. Amazon EBS\
   B. Amazon EFS\
   C. EC2 instance store\
   D. Amazon S3 Glacier Deep Archive

   <details><summary>Feedback</summary>

   **B is right.** Many Linux servers sharing the same files at once is file storage over NFS, which is EFS.

   - **A is wrong.** An EBS volume attaches to one instance.
   - **C is wrong.** Instance store is temporary and belongs to one instance.
   - **D is wrong.** Deep Archive is for data read less than once a year, with hours to get it back.

   </details>

2. **A company is moving its Windows file server, which uses Active Directory for permissions, to AWS. Users must notice no difference. Which service fits?**

   A. Amazon EFS\
   B. Amazon FSx for Windows File Server\
   C. An Amazon EBS volume\
   D. Amazon S3

   <details><summary>Feedback</summary>

   **B is right.** It provides Windows shares over SMB and joins Active Directory, so users and permissions work as before.

   - **A is wrong.** EFS uses NFS, and AWS doesn't support it with Windows-based EC2 instances.
   - **C is wrong.** A volume attaches to one server.
   - **D is wrong.** S3 isn't opened as a Windows share.

   </details>

3. **The bakery keeps the order database's data on one EBS volume and takes no snapshots. The volume's AZ is destroyed. What is lost, and what would have prevented it?**

   <details><summary>Feedback</summary>

   **The data, because every copy of an EBS volume lives in one AZ.** A snapshot, or another backup kept outside that AZ, would have let the bakery restore it elsewhere.

   </details>

**Next:** [S3 protection, storage classes and lifecycle](02-s3-in-practice.md).

## Where to check the current details

- [Amazon EFS FAQ](https://aws.amazon.com/efs/faq/): "When should I use Amazon EFS vs. Amazon EBS vs. Amazon S3?" (checked 2026-10-24)
- [Amazon EBS FAQs](https://aws.amazon.com/ebs/faqs/) (checked 2026-10-24)
- [Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/) (checked 2026-10-23)

---

"Block, file and object storage" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
