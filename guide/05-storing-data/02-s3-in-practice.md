---
type: lesson
id: clf-05-02
title: "S3 protection, storage classes and lifecycle"
tasks: ["3.6", "4.1", "2.2", "2.1"]
objectives: ["05.02a", "05.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 04, the guardrails primer and lesson 05.01; about 25 minutes; works on a phone"
prerequisites: [clf-05-01, clf-04-04, clf-03-03, guardrails-06]
terms_introduced: [Block Public Access, encryption at rest, encryption in transit, server-side encryption, SSE-S3, SSE-KMS, versioning, current version, noncurrent version, delete marker, S3 Object Lock, WORM, S3 Replication, storage class, S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, Amazon Glacier (vault service), restore, retrieval fee, minimum storage duration, S3 Lifecycle, lifecycle rule, transition action, expiration action]
pillars: [security, reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-08.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html"
  - "https://aws.amazon.com/s3/faqs/"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://aws.amazon.com/s3/storage-classes/glacier/"
  - "https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html"
  - "https://aws.amazon.com/s3/pricing/"
---

# S3 starts every bucket private and encrypted; you add versioning to undo mistakes, and storage classes and lifecycle rules to cut the bill

A new bucket already blocks public access and encrypts what you upload, but only versioning, which you switch on, undoes your own overwrites and deletes. Colder storage classes cost less to keep data in and more to read, so a lifecycle rule moves each object to a colder class as it ages.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 25 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [lesson 05.01](01-block-file-object.md) and on bucket policies from [lesson 04.04](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md). The photo bucket is the one the new teammate looks after in Module 04.

## Warm-up: what you remember

1. The order database has a standby copy in a second AZ that receives every change within moments. Someone deletes last week's orders. Does the standby still have them?

<details><summary>Feedback</summary>

1. **No.** Replication copies the deletion too; only a point-in-time backup undoes it (lesson 03.03). S3 has the same problem, and this lesson shows its answer.

</details>

## What you'll learn

By the end of this lesson, you can explain how Block Public Access, default encryption and versioning each protect data in S3 (objective 05.02a), and choose a storage class and a lifecycle rule for a kind of data (objective 05.03a).

Try this before you read on, and guess if you're unsure: the teammate deletes the birthday-cake photo by mistake, in a bucket with its default settings. Can AWS get it back?

## The big picture: five layers, three of them already on

![Five layers of S3 protection and how each starts: Block Public Access, on; policies, on; encryption at rest, on; versioning, off; a copy somewhere else, off.](../../images/05-02-protection-layers.svg)

*Notice that the three layers that start on all stop the wrong people. The two that start off protect you from accidents, including your own.*

**Long description.** Five numbered rows. 1, Block Public Access: stops data being made public by mistake; on. 2, IAM and bucket policies: stop the wrong person; on, private until a policy allows. 3, encryption at rest: protects the stored bytes; on, SSE-S3. 4, versioning: undoes an overwrite or delete; off. 5, a copy somewhere else: survives losing the bucket, Region or account; off. Durability, AWS's side of the line, sits under all five.

## Private and encrypted from the start

A new bucket and its objects aren't public, but a bucket policy or an access control list could later make them so. **Block Public Access** overrides any such grant ([Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)). It works at the account level and for each bucket, and where they differ the most restrictive wins. It's on by default for buckets created since 2023-04-28 ([ACCT.08](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-08.html)), but in the new account we created on 2026-10-23 the account-level settings were off. That's why the primer had you turn them on.

**Encryption at rest** scrambles stored data so only someone with the key can read it. Since 2023-01-05, S3 encrypts every new object with **SSE-S3** (server-side encryption with keys S3 manages), at no extra cost ([Default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html)). Choose **SSE-KMS** instead, with a key in AWS Key Management Service (Module 09), when you must control who can decrypt. **Encryption in transit** protects data on the move, with TLS, the protection behind HTTPS. Neither decides *who* may read: S3 decrypts an object for any request your policies allow, so you need access control too.

## Versioning lets you undo an overwrite or a delete

**Versioning** keeps every version of every object in the bucket ([S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)). It's **off** by default, and you turn it on per bucket. An overwrite makes a new **current version** and keeps the old one as a **noncurrent version**. A plain delete only adds a **delete marker**: the object looks gone, its versions are still there, and removing the marker brings it back. Each version is billed in full, and once enabled, versioning can be suspended but not turned off.

That answers the prequestion: with default settings the photo is gone. The S3 FAQ says durability doesn't protect against accidental or malicious deletes, and AWS can't recover deleted data ([Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/)). With versioning on, it comes back.

Two more protections go further:

- **S3 Object Lock** blocks deletes and overwrites of a version until a date you set: write once, read many (**WORM**). In compliance mode, nobody can remove the protection early, not even the root user.
- **S3 Replication** copies new objects automatically to another bucket, in another Region or the same one. Versions live inside their bucket, so only a copy elsewhere, by replication or a backup (lesson 05.04), survives losing the bucket or the Region.

## Storage classes: how often, how fast, how replaceable

Each object has a **storage class**, which decides how it's stored, how fast you get it back and how it's billed. New objects go to **S3 Standard** unless you choose otherwise. Colder classes cost less to store but charge a **retrieval fee** per GB read, and a **minimum storage duration**: delete or move an object out early, and you're billed for the rest of that minimum. Pick a class with three questions: *How often is it read? How fast must it come back? Could you recreate it if an AZ were destroyed?*

![Seven S3 storage classes from hot to cold, from S3 Standard to Glacier Deep Archive, with each one's minimum stay, time to first byte and retrieval fee.](../../images/05-03-hot-to-cold.svg)

*Notice that going down, storage gets cheaper, the minimum stay grows, and reads slow from milliseconds to hours at Glacier Flexible Retrieval.*

**Long description.** Seven rows from hot to cold, each showing its minimum stay, time to first byte and retrieval fee: the same values as the dated table below. Standard and Intelligent-Tiering have no minimum stay and no retrieval fee; One Zone-IA is the only class in one AZ; the two coldest classes need a restore before you can read.

- **S3 Standard:** read often. The default.
- **S3 Intelligent-Tiering:** the access pattern is unknown or changes. S3 moves each object to a cheaper tier after 30 days without a read, and cheaper again after 90; a read moves it back. No retrieval fees, but a monitoring fee per object; objects under 128 KB are never moved.
- **S3 Standard-IA** (infrequent access): read about once a month, and must come back in milliseconds.
- **S3 One Zone-IA:** the same, for less, but stored in **one AZ**: use it only for data you can recreate.
- **The three S3 Glacier classes**, for archives ([Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/)): **Glacier Instant Retrieval**, read about once a quarter, back in milliseconds; **Glacier Flexible Retrieval**, read once or twice a year, after a **restore** (a temporary readable copy) that takes minutes to hours; **Glacier Deep Archive**, S3's cheapest, read less than once a year, restored within 12 to 48 hours.

> **Dated (checked 2026-10-25):** check the [S3 storage class comparison](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) for current values. Storage prices are for US East (N. Virginia), as of 2026-10-24.
>
> | Class | Designed availability | Minimum stay | Storage, per GB-month |
> |---|---|---|---|
> | S3 Standard | 99.99% | None | $0.023 (first 50 TB) |
> | S3 Intelligent-Tiering | 99.9% | None | Varies by tier |
> | S3 Standard-IA | 99.9% | 30 days | $0.0125 |
> | S3 One Zone-IA | 99.5% (one AZ) | 30 days | $0.01 |
> | S3 Glacier Instant Retrieval | 99.9% | 90 days | $0.004 |
> | S3 Glacier Flexible Retrieval | 99.99% after restore | 90 days | $0.0036 |
> | S3 Glacier Deep Archive | 99.99% after restore | 180 days | $0.00099 |
>
> Every class above is designed for 99.999999999% durability.

Learn the pattern, not the digits: Deep Archive stores data for about a twenty-third of Standard's price, but reading it back takes hours and costs a fee per GB.

### "Standard-IA is as available as Standard" is wrong

It's easy to assume Standard-IA has Standard's availability and only costs less. It doesn't: AWS designs S3 Standard for 99.99% availability and Standard-IA for 99.9%. It's tempting because their *durability* is the same eleven nines and both answer in milliseconds, but durability and availability are different promises (lesson 02.03).

### "Glacier vaults are the S3 Glacier classes" is wrong

Older courses teach Glacier "vaults" as if they were the classes above. They aren't. The original vault service, now called **Amazon Glacier**, has its own API and no longer accepts new customers; AWS recommends the S3 Glacier storage classes instead ([What is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html), checked 2026-10-23). The mix-up is natural, because Glacier Flexible Retrieval used to be named "S3 Glacier". When a question says "S3 Glacier", think of the three classes.

## Lifecycle rules move and delete objects for you

**S3 Lifecycle** is a set of rules on a bucket ([Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)). A **lifecycle rule** acts a number of days after an object is created: a **transition action** moves it to another class, and an **expiration action** deletes it. A rule can cover the whole bucket or only objects with a given prefix or tag, and in a versioned bucket it can delete noncurrent versions, so they don't pile up on the bill.

Use **lifecycle rules** when you know how the data cools, and **Intelligent-Tiering** when you don't: a cake photo might be popular for years or forgotten next week. Either way, check each stay against its class's minimum before you save the rule: a rule that moves files to Glacier Flexible Retrieval at day 30 and deletes them at day 60 pays for 90 days in that class.

> **Example:** the photo bucket gets versioning, Intelligent-Tiering, and a rule that deletes noncurrent versions after 30 days. The monthly sales records get a rule: Standard-IA at day 30, Glacier Deep Archive at day 365, and expiration at day 2,557, about seven years. Every stay passes its minimum.

> **Your turn:** the bakery copies a 10 GB backup to S3 every night. Each backup must open at once for its first 30 days; after that, a wait of up to two days is fine, and it's deleted after a year. Which plan fits, and why not the others? (a) S3 Standard all year. (b) Glacier Deep Archive from day 0. (c) Standard for 30 days, then Deep Archive, expiring at day 365.

<details><summary>Model answer</summary>

**(c)** meets every rule and, after the first month, stores each backup at about a twenty-third of Standard's price. (a) works but pays Standard's price all year for data nobody reads. (b) breaks the first rule: a Deep Archive restore can take up to 48 hours.

</details>

## Summary

- **On by default:** Block Public Access (for new buckets), private policies and SSE-S3 encryption. **Off until you turn it on:** versioning and a copy elsewhere.
- **Versioning** keeps every version, and a delete adds a marker. Durability doesn't undo deletes.
- **Pick a class** by how often the data is read, how fast it must come back, and whether you could recreate it. Standard-IA is designed for 99.9% availability, not Standard's 99.99%.
- **The three S3 Glacier classes** are archive classes in normal buckets; the vault service Amazon Glacier is closed to new customers.
- **Lifecycle rules** transition objects to colder classes and expire them by age; colder classes add retrieval fees and minimum stays.

## Practice

1. **A company must keep audit records unchanged for five years, and even administrators must not be able to delete them early. Which S3 feature meets this?**

   A. Versioning\
   B. Default encryption\
   C. S3 Object Lock in compliance mode\
   D. Same-Region Replication

   <details><summary>Feedback</summary>

   **C is right.** In compliance mode, nobody, including the root user, can remove Object Lock's protection before the retention date.

   - **A is wrong.** Someone with permission can still delete a version permanently.
   - **B is wrong.** Encryption protects the stored bytes, not against deletion.
   - **D is wrong.** Replication copies objects; it doesn't stop deletes.

   </details>

2. **A company keeps scanned contracts that are read about once a quarter, but a lawyer may need any one of them in milliseconds. Which class fits best?**

   A. S3 Standard\
   B. S3 Glacier Instant Retrieval\
   C. S3 Glacier Flexible Retrieval\
   D. S3 Glacier Deep Archive

   <details><summary>Feedback</summary>

   **B is right.** It's for data read about once a quarter that must come back in milliseconds.

   - **A is wrong.** It works but costs more to store data read so rarely.
   - **C is wrong.** It needs a restore first: minutes at best.
   - **D is wrong.** Restores take hours.

   </details>

3. **Which statement about S3 One Zone-IA is true?**

   A. It is designed for the same availability as S3 Standard.\
   B. It stores data in one Availability Zone, so data can be lost if that AZ is destroyed.\
   C. It has no minimum storage duration.\
   D. It is the same as the Amazon Glacier vault service.

   <details><summary>Feedback</summary>

   **B is right.** Use it only for data you can recreate.

   - **A is wrong.** It's designed for 99.5%; Standard for 99.99%.
   - **C is wrong.** Its minimum stay is 30 days.
   - **D is wrong.** It's an S3 class; Amazon Glacier is a separate, older vault service.

   </details>

**Next:** [Hybrid storage and backup](04-hybrid-storage-and-backup.md). To practice, do [Lab 05](07-lab-05-versions-and-lifecycle.md), where you build the tax archive bucket from the owner's requirements.

## Where to check the current details

- [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) (checked 2026-10-24)
- [Understanding and managing Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) (checked 2026-10-25)
- [Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/): durability and deletes, Object Lock, Replication (checked 2026-10-23)

---

"S3 protection, storage classes and lifecycle" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
