---
type: lesson
id: clf-03-03
title: "Surviving failure"
tasks: ["3.2", "1.1"]
objectives: ["03.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 15 minutes; works on a phone"
prerequisites: [clf-02-03, clf-03-01, clf-03-02]
terms_introduced: [blast radius, disaster recovery, failover, recovery Region, recovery time objective, recovery point objective, replication, backup, point-in-time backup, backup and restore, pilot light, warm standby, multi-site active/active]
pillars: [reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html"
  - "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"
  - "https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html"
  - "https://health.aws.amazon.com/health/status"
---

# High availability keeps the site running through a failure; disaster recovery brings it back after a bigger one

Two Availability Zones protect the bakery from losing a data center, but not from losing a whole Region, and not from a mistake that wipes its data. Those need disaster recovery, sized by two numbers the business sets: how long it can be down (RTO) and how much data it can lose (RPO).

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** read [Regions, Availability Zones and data centers](01-regions-availability-zones-data-centers.md) and [Choosing a Region](02-choosing-a-region.md) first.

## Warm-up: what you remember

1. In lesson 02.03, the bakery's site crashed in December under too many orders. A friend said, "You need high availability." What was the better word?
2. From lesson 03.01: is an Availability Zone "one data center"?

<details><summary>Feedback</summary>

1. **Elasticity.** Demand rose above capacity; no part broke.
2. **No.** AWS describes an AZ as one or more data centers.

</details>

## What you'll learn

By the end of this lesson, you can choose a resilience approach for a business from its RTO, its RPO and its budget (objective 03.03a).

Try this before you read on: the bakery's order database has a standby in a second AZ that receives every change within moments. Someone deletes last week's orders by mistake. Does the standby save them?

## The big picture: how far a failure reaches

How far a failure reaches is its **blast radius**, and the further it reaches, the more you need in place beforehand.

![A ladder of failures from one server up to a whole Region, with high availability for the lower rungs, disaster recovery for the top, and a separate box for mistakes in the data.](../../images/03-03-blast-radius-ladder.svg)

*Notice that the bottom three rungs stay inside one Region and are handled by high availability; only the top rung needs a second Region, and the box off the ladder needs backups.*

**Long description.** Four rungs, each wider the further the failure reaches. A whole Region unusable: a copy of the site, or at least its data, in another Region; disaster recovery. One Availability Zone lost to a flood or fire: servers and the database in two or more AZs; high availability. One data center losing power or cooling: the same protection; high availability. One server crashing: a second server and automatic replacement; high availability. Off the ladder, dashed: a mistake or attack on the data itself, such as a deleted orders table, reaches every live copy at once; only a point-in-time backup from before it undoes it.

## High availability and disaster recovery answer different questions

High availability keeps the system running *through* the failure of a part: a server, a data center, an AZ. **Disaster recovery (DR)** brings the whole workload back *after* a bigger event, from a separate copy, usually in a **recovery Region**; **failover** is switching users to that copy ([Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf), 2021). Neither replaces the other.

### "High availability is the same as disaster recovery" is wrong

A common belief is that a system spread over several AZs needs no DR plan. It still needs one: all its AZs sit in one Region, and a Region-wide outage or a deleted table takes a separate copy to recover. The belief is tempting because the same tools, such as automatic failover, serve both.

> **Example (AWS Health Dashboard, checked 2026-10-25):** since March 2026, AWS's Middle East (UAE) Region, `me-central-1`, has been "unable to reliably support customer applications", in AWS's words. In its update of 2026-09-15, AWS said it was "unable to restore access to the resources and data hosted exclusively in the mec1-az2 Availability Zone", and that "most customers have been able to re-establish their operations in other Regions by restoring backups or copying data that remained accessible" ([AWS Health Dashboard](https://health.aws.amazon.com/health/status)). Data kept in one place was lost; customers with a copy elsewhere recovered.

## RTO and RPO: how long you can be down, and how much you can lose

Every DR plan starts with two numbers the business sets ([Disaster Recovery (DR) objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html)):

- **Recovery time objective (RTO):** the longest acceptable time between the service stopping and working again. It looks *forward* from the failure.
- **Recovery point objective (RPO):** the longest acceptable time between the last saved copy of the data and the failure; everything after it is lost. It looks *back* from the failure.

![A time line: last backup at 02:00, failure at 10:00, service back at 14:00; 8 hours of data lost and 4 hours of downtime.](../../images/03-03-rto-rpo-timeline.svg)

*Notice that the failure sits in the middle. Data loss is measured back to the last backup; downtime forward to the restart. Improving one doesn't improve the other.*

**Long description.** A made-up time line from 00:00 to 16:00. At 02:00, the last good backup (the recovery point); at 10:00, the order database is lost; at 14:00, the site takes orders again. The span from 02:00 to 10:00 is labeled "Data lost: 8 hours of orders"; from 10:00 to 14:00, "Downtime: 4 hours".

To keep them apart: the **P** in RPO is a **point** in your data; the **T** in RTO is **time** without service. Both come from what an outage costs the business.

## Four strategies, from cheap and slow to costly and fast

AWS groups DR into four strategies. Each step keeps more running in the recovery Region, so it costs more every month and recovers faster ([Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)).

![Four disaster recovery strategies as rising stairs, from backup and restore to multi-site active/active: cost rises and recovery time falls.](../../images/03-03-dr-strategies.svg)

*Notice that the axes have no numbers: AWS gives an order and typical ranges, not prices. Each step right buys faster recovery with more money spent every month.*

**Long description.** Four boxes rise like stairs; moving right, running cost and complexity rise and typical recovery time falls. Backup and restore, hours: backups copied to the recovery Region, everything else rebuilt after the disaster. Pilot light, tens of minutes: data copied continuously and the database running, app servers off until needed. Warm standby, minutes: a smaller copy of the whole site always running, scaled up to take over. Multi-site active/active, near zero: full copies in two or more Regions all serving customers.

The four are **backup and restore**, **pilot light**, **warm standby** and **multi-site active/active**, with typical recovery in hours, tens of minutes, minutes and near zero (AWS's 2021 whitepaper, checked 2026-10-24). To tell pilot light from warm standby, a pair AWS itself calls hard to separate, ask: *could it serve a customer right now?* A pilot light can't until its app servers start; a warm standby can, at reduced size. The RTO and RPO can differ: a pilot light copies data continuously, so it can lose only minutes of data though starting it takes longer. **AWS Backup** and **AWS Elastic Disaster Recovery** do much of this work ([What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html); [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)); Module 05 compares them.

> **Example:** the owner can take phone orders for a day (RTO about a day) and survive losing a few hours of orders (RPO a few hours) on a small budget. Backup and restore recovers in hours, so it fits; a pilot light would pay all year for speed she doesn't need. German backups go to a second EU Region, such as Europe (Ireland): the recovery Region inherits the data's rules.

> **Your turn:** later, online orders grow and the owner sets an RTO of 30 minutes and an RPO of 5 minutes, with a larger budget. Which strategy now, and why not the one on either side?

<details><summary>Model answer</summary>

**Pilot light.** Recovery in tens of minutes fits 30, and continuously copied data keeps the RPO in minutes. Backup and restore takes hours: too slow. Warm standby works but costs more than needed. Test that the switch-on fits in 30 minutes.

</details>

## Replication copies your mistakes; backups undo them

**Replication** copies every change to a second place as it happens, bad ones included. A **backup** is a saved copy of data at one moment; a **point-in-time backup** lets you go back to that moment. So in the prequestion, the standby deletes the orders within moments, and only a backup from before the mistake brings them back.

### "Replication replaces backup" is wrong

You may hear that a database with a live copy elsewhere doesn't need backups. It does: replication copies deletions, corruption and an attacker's changes, and AWS notes that even multi-site active/active needs backups. It's tempting because a replica looks like a backup; but a replica shows the data as it is now, a backup as it was. RDS snapshots and S3 versioning (Module 05) are point-in-time copies.

## Summary

- **How far a failure reaches decides the protection.** A server, a data center or an AZ: high availability across AZs. A whole Region: disaster recovery, with a copy in another Region.
- **High availability isn't disaster recovery.** One keeps components working; the other brings the whole workload back.
- **RTO is the longest acceptable downtime; RPO is the most data you accept losing.** The business sets both.
- **Four DR strategies,** cheapest and slowest first: backup and restore (hours), pilot light (tens of minutes), warm standby (minutes), multi-site active/active (real time). Choose the cheapest that meets both numbers.
- **Replication copies mistakes; backups undo them.** Every strategy still needs point-in-time backups.

## Practice

1. **A company runs its application in three Availability Zones of one Region. Which event does this design NOT protect it against?**

   A. A power failure in one data center\
   B. A flood that closes one Availability Zone\
   C. A failed disk in one server\
   D. A large disaster that makes the whole Region unusable

   <details><summary>Feedback</summary>

   **D is right.** All three AZs are in one Region, so losing it stops everything; that needs disaster recovery.

   - **A is wrong.** A data center is inside one AZ; the others keep running.
   - **B is wrong.** Surviving one AZ's loss is what a multi-AZ design is for.
   - **C is wrong.** The other copies keep serving.

   </details>

2. **A company wants a copy in a second Region that can serve customers immediately, at lower capacity, if the main Region fails. It doesn't want both Regions serving customers every day. Which strategy fits?**

   A. Backup and restore\
   B. Pilot light\
   C. Warm standby\
   D. Multi-site active/active

   <details><summary>Feedback</summary>

   **C is right.** A warm standby is a smaller, fully working copy that can take traffic at once and then scale up.

   - **A is wrong.** Nothing runs in the second Region; it must be rebuilt first.
   - **B is wrong.** A pilot light's app servers are off, so it can't serve customers until they start.
   - **D is wrong.** Active/active serves customers from both Regions all the time.

   </details>

3. **The owner says, "If the site goes down, it must be back within two hours, and we can't lose more than 15 minutes of orders." Which is right?**

   A. RTO is 15 minutes; RPO is 2 hours.\
   B. RTO is 2 hours; RPO is 15 minutes.\
   C. Both are 2 hours, because the larger number decides.\
   D. Both are 15 minutes, because the stricter number decides.

   <details><summary>Feedback</summary>

   **B is right.** "Back within two hours" is downtime: RTO. "No more than 15 minutes of orders" is data: RPO.

   - **A is wrong.** It swaps them.
   - **C and D are wrong.** They measure different things and are met in different ways: frequent copies for RPO, a fast restart for RTO.

   </details>

**Next:** [The edge](04-the-edge.md). To practice choosing strategies, try [Simulation S2](06-sim-blast-radius.md).

## Where to check the current details

- [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), AWS whitepaper, published 2021-02-12 (checked 2026-10-24)
- [Disaster Recovery (DR) objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html), Reliability Pillar (checked 2026-10-24)
- [AWS Health Dashboard](https://health.aws.amazon.com/health/status), AWS's public status page (checked 2026-10-25)

---

"Surviving failure" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
