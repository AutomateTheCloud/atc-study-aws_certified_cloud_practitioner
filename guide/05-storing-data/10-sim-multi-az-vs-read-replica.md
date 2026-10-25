---
type: sim
id: clf-05-10
title: "Simulation S6: Multi-AZ, read replica or backup: protect the order database"
tasks: ["3.4", "3.2"]
objectives: ["05.05a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 03.03 and 05.05; about 20 minutes"
prerequisites: ["clf-03-03", "clf-05-05"]
terms_introduced: [replication lag, promote]
pillars: [reliability, performance-efficiency, cost-optimization]
lab: "S6"
rung: L2
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "20 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html"
  - "https://aws.amazon.com/rds/faqs/"
  - "https://aws.amazon.com/backup/faqs/"
---

# Simulation S6: Multi-AZ, read replica or backup: protect the order database

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [03.03 Surviving failure](../03-aws-around-the-world/03-surviving-failure.md) and [05.05 Managed databases and choosing one](05-managed-or-self-managed-databases.md). **Time:** about 20 minutes. **Cost:** $0; no AWS account is used.

**Why a simulation:** Amazon RDS bills for every second a database instance runs, with a 10-minute minimum, and a Multi-AZ deployment or a read replica adds to that ([Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/), checked 2026-10-23). You also can't make an Availability Zone fail.

**Goal:** match three kinds of extra copy to four things that can go wrong, then answer the owner's money-saving ideas. This is the decision the exam tests: Multi-AZ for availability, a read replica for reads, backups for mistakes.

## The rules of this simulation

The bakery's order database is as lesson 03.01 left it: Amazon RDS in US East (N. Virginia), with the primary in AZ a and a **Multi-AZ** standby in AZ b. Automated backups are on, with the default retention of 7 days (35 at most), and a restore can go to any second up to about five minutes ago. The events are **made up**; how each copy behaves is RDS's, from the RDS User Guide and FAQs (checked 2026-10-23).

Keep the comparison from [lesson 05.05](05-managed-or-self-managed-databases.md#each-copy-of-the-database-has-one-job) in view. Three facts you need:

- A read replica can fall behind its primary; the delay is called **replication lag**. To **promote** a replica is to turn it into a standalone database that accepts writes. Most engines can keep a replica in another Region ([Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)).
- Multi-AZ fails over when the primary's AZ, network or server fails. It doesn't fail over because of database errors such as long-running queries or corruption ([Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/)).
- Restoring from automated backups or a snapshot creates a new database instance ([Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/)).

## Part 1: four events

### Decision 1: for each event, which copy keeps the bakery going or gets its data back?

| # | Event |
|---|---|
| 1 | At 10:00 on a busy Saturday, AZ a loses power. |
| 2 | Every month-end, the accountant's sales reports slow the checkout page. |
| 3 | At 15:42, a staff member runs a wrong `DELETE` that removes yesterday's orders. |
| 4 | A large outage makes all of US East (N. Virginia) unusable for a day. |

<details><summary>Model answer</summary>

![A grid of the four events against Multi-AZ standby, read replica and automated backups. AZ a loses power: the standby solves it automatically in 1 to 2 minutes; a replica helps partly, by hand and possibly losing writes; backups are slow. Reports slow the site: the standby can't serve reads; a replica solves it; backups don't help. A wrong DELETE: standby and replica both copy it; backups solve it by restoring to 15:41. The Region is down: the standby can't help; a replica or backups help only if they're in, or copied to, another Region.](../../images/05-10-event-grid.svg)

*Notice that each event has a different answer. No single copy covers all four, which is why production databases usually have more than one.*

**Long description.** Four events against three kinds of copy. AZ a loses power: the standby solves it automatically in one to two minutes; a replica helps partly, by hand, possibly losing writes; backups are slow. Reports slow the site: the standby serves no reads; a replica solves it; backups don't help. A wrong DELETE at 15:42: the standby and the replica both copy it; backups solve it by restoring to 15:41. The Region is down: the standby is in the same Region; a replica or backups help only if they're in, or copied to, another Region.

1. **Multi-AZ.** RDS points the database's endpoint name at the standby, which becomes the primary, and orders resume within a couple of minutes. Because copying is synchronous, finished orders should already be on the standby.
2. **A read replica.** Point the reports at the replica's endpoint; checkout keeps the primary to itself.
3. **Automated backups.** Restore a new database to 15:41 and copy yesterday's orders back. Both live copies deleted them within moments.
4. **None of the three, as set up today.** It needs a copy in another Region. Part 2 returns to this.

</details>

## Part 2: the owner's money-saving ideas

Answer each in two or three sentences.

### Decision 2: "The standby sits idle all month. Send the month-end reports to it."

<details><summary>Model answer</summary>

It can't take them: in this kind of Multi-AZ deployment, the standby serves no reads and exists only to take over. Add a read replica for the reports, or run them at night. (RDS also offers a **Multi-AZ DB cluster**, whose two standbys can serve reads; it's a different, newer setup.)

</details>

### Decision 3: "We have a read replica now. Drop Multi-AZ: the replica is a copy in another AZ too."

<details><summary>Model answer</summary>

**No: a read replica isn't high availability.** It runs a little behind, so the latest orders may be missing; someone has to promote it; and the site must then be pointed at a new endpoint. AWS's RDS FAQ recommends Multi-AZ for availability. Both are "a copy in another AZ", but they're built for different jobs.

</details>

### Decision 4: "Backups are automatic, so we're covered for mistakes."

The bookkeeper checks the orders once a month, on the 1st.

<details><summary>Model answer</summary>

**Not with the defaults.** Automated backups are kept for 7 days unless you change it, so a mistake made on the 3rd and found on the 1st of the next month can't be undone. Raise the retention to the maximum, 35 days, and take a manual snapshot each month, because manual snapshots are kept until you delete them.

</details>

### Decision 5 (challenge): losing the whole Region

In [Simulation S2](../03-aws-around-the-world/06-sim-blast-radius.md), the bakery chose **backup and restore**: back within a day, losing at most a few hours of orders. US orders may be kept in any US Region. What do you add, and why not a cross-Region read replica?

<details><summary>Model answer</summary>

Copy the database backups to a second US Region, such as US East (Ohio), on a schedule of a few hours. AWS Backup can copy backups across Regions for RDS (lesson [05.04](04-hybrid-storage-and-backup.md); [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)). Restoring a new database there takes hours, which fits a one-day RTO. A cross-Region read replica would recover faster, closer to a pilot light, but it is a whole database instance running, and billing, all the time for a rare event the bakery can survive without it.

</details>

## Recap

Each extra copy has one job. A **Multi-AZ standby** keeps the database running through an AZ or server failure, automatically. A **read replica** spreads reading work, and only becomes a recovery copy if someone promotes it. **Backups** take you back to before a mistake, but only as far back as you keep them. A copy in another Region is a separate decision, driven by the recovery time the business needs.

**Next:** [the Module 05 mastery check](11-check.md). Before you take it, retry the practice questions at the end of [05.05](05-managed-or-self-managed-databases.md) without looking back.

---

"Simulation S6: Multi-AZ, read replica or backup: protect the order database" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
