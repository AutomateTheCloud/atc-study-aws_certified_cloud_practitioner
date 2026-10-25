---
type: sim
id: clf-05-09
title: "Simulation S5: Run a year of lifecycle rules forward and find the cost traps"
tasks: ["3.6", "4.1"]
objectives: ["05.03a"]
reader: "Adult studying alone, possibly new to IT, who has read lesson 05.03; about 30 minutes; a calculator or spreadsheet helps"
prerequisites: ["clf-05-03", "clf-05-07"]
terms_introduced: []
pillars: [cost-optimization, sustainability]
lab: "S5"
rung: L2
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "30 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html"
  - "https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html"
  - "https://aws.amazon.com/s3/pricing/"
---

# Simulation S5: Run a year of lifecycle rules forward and find the cost traps

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [05.03](03-storage-classes-and-lifecycle.md), and ideally done [Lab 05](07-lab-05-versions-and-lifecycle.md). **Time:** about 30 minutes. **Cost:** $0; no AWS account is used. Lifecycle rules take months to show on a bill, so we run the year forward on paper.

**Goal:** choose a lifecycle plan for the bakery's backups, cost it over a year, and spot three plans that look cheaper and aren't. **End state:** a filled-in cost table and three one-line fixes.

**Why this matters:** keeping data only as long as you need it, in the cheapest class that meets its rules, is [COST04-BP05 Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html) and [SUS04-BP03 Use policies to manage the lifecycle of your datasets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html).

## The rules of this simulation

**The prices are AWS's, for US East (N. Virginia), as of 2026-10-24** ([Amazon S3 pricing](https://aws.amazon.com/s3/pricing/); we read them from AWS's price list files). Colder classes cost less to store and more, and longer, to read. Prices differ by Region and change, so check the pricing page before deciding anything real. The bakery's data volumes are made up.

| Class | Storage, $ per GB-month | Read fee, $ per GB (standard retrieval) | Minimum storage duration | Time to first byte |
|---|---|---|---|---|
| S3 Standard | 0.023 (first 50 TB) | none | none | milliseconds |
| S3 Standard-IA | 0.0125 | 0.01 | 30 days | milliseconds |
| S3 Glacier Flexible Retrieval | 0.0036 | 0.01 | 90 days | minutes to hours, after a restore |
| S3 Glacier Deep Archive | 0.00099 | 0.02 | 180 days | 12 to 48 hours, after a restore |

**The rules are AWS's** (Amazon S3 User Guide, checked 2026-10-23):

- Delete, overwrite or move a file before its class's minimum duration, and you are billed for the rest of the minimum, pro rata, so you pay for the full minimum in all ([S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)).
- Standard-IA bills any file smaller than 128 KB as 128 KB.
- With versioning on, every version is billed as a whole file ([S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)).
- Billing changes on the day a lifecycle rule applies, even if S3 moves or deletes the file days later ([Setting an S3 Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)).
- Each lifecycle transition is a charged request: $0.01 per 1,000 into Standard-IA, $0.03 into Glacier Flexible Retrieval and $0.05 into Deep Archive (US East (N. Virginia), as of 2026-10-24). For a few dozen large files that is under a cent, so we leave it out.

A month is 30 days.

## Part 1: one month of backups, four plans

Each night the bakery copies its order database's backup to S3: 30 files of 10 GB a month, **300 GB** (made-up volumes). The owner's rules:

- For 30 days, every backup must open at once: she test-restores one each week.
- After 30 days, a wait of up to two days is fine.
- Delete each backup after a year.

![Four bars on a day axis from 0 to 365, all ending at a line marked Deleted on day 365. Plan A: S3 Standard all year. Plan B: Standard to day 30, Standard-IA to day 90, Glacier Flexible Retrieval to day 365. Plan C: Glacier Deep Archive from day 0. Plan D: Standard to day 30, then Glacier Deep Archive.](../../images/05-09-lifecycle-timeline.svg)

*Notice that Plans B and D look alike for the first month and differ in how far they cool the data after it.*

**Long description.** Four bars on an age axis, 0 to 365 days, all ending in deletion on day 365. A: S3 Standard throughout. B: Standard to day 30, Standard-IA to day 90, Glacier Flexible Retrieval to day 365. C: Glacier Deep Archive throughout. D: Standard to day 30, then Glacier Deep Archive.

### Decision 1: which plans follow the owner's rules?

<details><summary>Model answer</summary>

A, B and D. **Plan C breaks the first rule:** a backup in Deep Archive must be restored before anyone can read it, which takes up to 48 hours, so the weekly test restore can't open at once.

</details>

### Decision 2: what does each plan cost for the year?

Fill in the storage cost. Plan A is worked for you: 300 GB × $0.023 × 365 ÷ 30 = **$83.95**.

| Plan | Your working | Year's storage cost |
|---|---|---|
| A | 300 × 0.023 × 365/30 | $83.95 |
| B | | |
| C | | |
| D | | |

<details><summary>Model answer</summary>

| Plan | Working | Year's storage cost |
|---|---|---|
| A | 300 × 0.023 × 365/30 | $83.95 |
| B | 300 × (0.023 × 30 + 0.0125 × 60 + 0.0036 × 275) / 30 | $24.30 |
| C | 300 × 0.00099 × 365/30 | $3.61, but it breaks a rule |
| D | 300 × (0.023 × 30 + 0.00099 × 335) / 30 | $10.22 |

![Line chart of running storage cost over 365 days at S3 prices for US East (N. Virginia) as of 2026-10-24. All three plans cost $6.90 for the first 30 days. Plan A climbs straight to $83.95. Plan B rises to $14.40 by day 90, then flattens, ending at $24.30. Plan D nearly flattens after day 30 and ends at $10.22.](../../images/05-09-cost-by-plan.svg)

*Notice where the lines part: on day 30. After that, how cold the data sits matters far more than how many steps the rule has.*

**Long description.** Running storage cost over 365 days at US East (N. Virginia) prices as of 2026-10-24. All three plans cost $6.90 for the first 30 days. A climbs straight to $83.95; B reaches $14.40 by day 90, then flattens to $24.30; D nearly flattens after day 30, ending at $10.22. C isn't drawn: it breaks the restore rule.

**Choose Plan D.** It meets every rule and costs about an eighth of Plan A. If a late mistake is found and one old 10 GB backup is needed, the standard read fee is 10 × $0.02 = $0.20, and the two-day wait is allowed.

</details>

### Decision 3: the owner asks why Plan B, with more steps, costs more

Answer in two sentences.

<details><summary>Model answer</summary>

After day 30 a two-day wait is allowed, so the faster classes buy nothing she needs. Extra steps pay only when each matches a real change in how the data is used.

</details>

## Part 2: three plans that look cheaper and aren't

For each, say why it costs more and give a one-line fix.

**Trap 1.** The site's 2,000,000 photo thumbnails are 20 KB each, 40 GB in all. A helper adds a lifecycle rule to move them to Standard-IA because "it's about half price".

**Trap 2.** To save money, a helper changes the backups to "straight into Deep Archive, delete after 7 days".

**Trap 3.** A script now overwrites one file, `backups/latest.sql`, every night, in a bucket with versioning on and no lifecycle rule.

![Line chart over 60 nights of GB stored for a 10 GB file overwritten nightly. With no rule for older versions, storage climbs in a straight line to 600 GB and keeps growing. With older versions deleted after 7 days, it levels off at 80 GB from night 8.](../../images/05-09-versions-pile-up.svg)

*Notice that the bucket list still shows one 10 GB file: older versions are hidden unless you turn on Show versions.*

**Long description.** GB stored over 60 nights for a 10 GB file overwritten nightly, versioning on. With no rule for older versions, storage climbs straight to 600 GB and keeps growing. With older versions deleted 7 days after they stop being current, it levels off at 80 GB from night 8.

<details><summary>Model answer</summary>

**Trap 1: the minimum billable size.** Each 20 KB thumbnail is billed as 128 KB, so 40 GB is billed as 256 GB: 256 × $0.0125 = $3.20 a month, against 40 × $0.023 = $0.92 in S3 Standard (counting 1 GB as a million KB). The move itself costs 2,000,000 transitions × $0.01 per 1,000 = $20. **Fix:** keep small files in S3 Standard.

**Trap 2: the minimum duration.** Each 10 GB backup is billed for 180 days, not 7: 10 × $0.00099 × 6 ≈ $0.059, against 10 × $0.023 × 7/30 ≈ $0.054 for a week in S3 Standard. The "cheapest" class ends up dearer, and it also breaks the owner's restore rule. **Fix:** short-lived data stays in S3 Standard; cold classes are for data you keep for months or years.

**Trap 3: versions pile up.** Every overwrite keeps the old 10 GB version, so after a year the bucket holds 3,650 GB: about $84 a month, and rising. **Fix:** a lifecycle rule that permanently deletes noncurrent versions after the recovery window the owner needs, such as 7 days, which holds storage at about 80 GB (about $1.84 a month).

</details>

## Part 3: the tax archive (challenge)

The bakery must keep each year's tax records, about 100 GB (a made-up volume), for seven years. The tax office might ask for one year's records once; the bakery then has a week to send them. An older study guide says: "create a Glacier vault for this".

### Decision 4: choose the class, work out seven years of storage, and answer the study guide

<details><summary>Model answer</summary>

**S3 Glacier Deep Archive**, through a lifecycle rule in a normal bucket, as in Lab 05's archive bucket. Seven years is 84 months:

| Class | 100 GB for 84 months |
|---|---|
| S3 Standard | $193.20 |
| S3 Glacier Flexible Retrieval | $30.24 |
| S3 Glacier Deep Archive | $8.32 |

Reading one year's 100 GB back with a standard retrieval costs 100 × $0.02 = $2.00 and finishes within 12 hours, well inside a week. The 180-day minimum is no trap for seven-year data.

**The study guide is out of date.** A "vault" belongs to the original Amazon Glacier service, which no longer accepts new customers; AWS recommends the S3 Glacier storage classes instead ([What is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html), checked 2026-10-23). When the exam guide says "Amazon S3 Glacier", study those classes.

</details>

## Recap

The cheapest class isn't always the cheapest choice: minimum durations, minimum sizes and read fees punish cold classes used for short-lived, small or busy data, and unmanaged versions grow without limit. The winning plan puts each stretch of the data's life in the coldest class its rules allow.

**Next:** [Simulation S6](10-sim-multi-az-vs-read-replica.md), which protects the order database itself. [05.04](04-hybrid-storage-and-backup.md) shows how AWS Backup can manage backup schedules and retention across services.

---

"Simulation S5: Run a year of lifecycle rules forward and find the cost traps" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
