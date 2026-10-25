---
type: sim
id: clf-03-06
title: "Simulation S2: The blast-radius ladder and three recovery plans"
tasks: ["3.2", "1.1"]
objectives: ["03.03a"]
reader: "Adult studying alone, possibly new to IT; about 30 minutes; paper or a spreadsheet helps"
prerequisites: ["clf-03-01", "clf-03-03"]
terms_introduced: []
pillars: [reliability, cost-optimization]
lab: "S2"
rung: L2-L3
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "30 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-marker-replication.html"
---

# Simulation S2: The blast-radius ladder and three recovery plans

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [03.01](01-regions-availability-zones-data-centers.md) and [03.03](03-surviving-failure.md). **Time:** about 30 minutes. **Cost:** $0; no AWS account is used. You can't fail an Availability Zone or a Region for real, so we simulate it.

**Goal:** sort six failures by how far they reach, then choose a disaster recovery strategy for three businesses and defend each choice. **End state:** a completed ladder table and three one-line recommendations.

**Why this matters:** you practice [REL13-BP01 Define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html) and [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) in the Well-Architected reliability pillar. Too little protection risks the business; too much wastes money every month.

## The rules of this simulation

The businesses and their numbers are **made up for teaching**. The strategies, their order and their typical recovery times are AWS's, from its disaster recovery whitepaper (2021, checked 2026-10-24) ([Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)).

| Strategy, cheapest first | Typical RTO and RPO |
|---|---|
| Backup and restore | Hours |
| Pilot light | Tens of minutes |
| Warm standby | Minutes |
| Multi-site active/active | Near zero (real time) |

- **High availability** (two or more AZs in one Region) handles failures inside a Region: a server, a data center, an AZ.
- **Disaster recovery** handles losing a whole Region. Pick the **cheapest strategy that meets both the RTO and the RPO**.
- **The RTO and the RPO can differ.** AWS's table gives one range for both, but a pilot light, like a warm standby, copies data continuously, so its RPO can be a few minutes or less even though its recovery takes tens of minutes (lesson 03.03).
- **Replication copies mistakes.** Only a point-in-time backup undoes damage to the data itself.

Keep the ladder from lesson 03.03 in view:

![The blast-radius ladder. A whole Region: disaster recovery, a copy in another Region. One Availability Zone, one data center, one server: high availability, more than one AZ. Off the ladder: a mistake or attack on the data reaches every live copy; only a point-in-time backup undoes it.](../../images/03-03-blast-radius-ladder.svg)

*Notice the box off the ladder. Part 1 has two events that belong there.*

**Long description.** Four rungs, largest first. A whole Region: protected by a copy in another Region; disaster recovery. One Availability Zone: protected by running in two or more AZs; high availability. One data center: the same protection; high availability. One server: a second server and automatic replacement; high availability. Off the ladder, dashed: a mistake or attack on the data itself reaches every live copy; only a point-in-time backup from before it undoes it.

## Part 1: the blast-radius ladder

The bakery's site runs as lesson 03.01 left it: two web servers in two AZs behind a load balancer, and an order database with a standby in the second AZ. German customers are served from Europe (Frankfurt).

### Decision 1: place each event on the ladder

For each event, write its rung (server, data center, AZ, Region, or off the ladder: data) and what keeps the bakery going.

| # | Event |
|---|---|
| 1 | A disk fails in the server running web server 1. |
| 2 | A cooling failure shuts one data center in the bakery's first AZ. |
| 3 | A flood closes every data center in the bakery's first AZ. |
| 4 | A large outage makes the whole Frankfurt Region unusable for a day. |
| 5 | A staff member deletes last week's orders by mistake. |
| 6 | Someone signs in with a stolen password and deletes every cake photo in the bucket. |

<details><summary>Model answer</summary>

| # | Rung | What keeps the bakery going |
|---|---|---|
| 1 | Server | Web server 2 keeps taking orders; the failed server is replaced. High availability. |
| 2 | Data center | If the AZ has other data centers, it may carry on; if not, the copies in the second AZ take over. High availability either way. |
| 3 | AZ | Web server 2 and the standby database in the second AZ take over. High availability. |
| 4 | Region | Nothing in Frankfurt helps: both AZs are in it. The bakery needs a copy, or at least backups, in another EU Region. Disaster recovery. |
| 5 | Off the ladder: data | The standby deletes the orders too, within moments. Only a point-in-time backup from before the mistake brings them back. |
| 6 | Off the ladder: data | A deletion doesn't always reach every copy: with current S3 Replication rules, a deletion is copied only if delete marker replication is turned on, and the permanent deletion of a specific version is never copied ([What does Amazon S3 replicate?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-what-is-isnot-replicated.html)). But a stolen password may reach the copies too, so don't count on them. Earlier versions (S3 versioning) or a backup restore the photos. Then lock out the attacker: Module 04 shows how. |

Events 5 and 6 are the ones people miss: damage to the data travels with the data.

</details>

### Decision 2: the owner's question

The owner asks: "We run in two AZs now. Which of these six events would still stop us, or lose data?" Answer in two sentences.

<details><summary>Model answer</summary>

Losing the whole Frankfurt Region (event 4) would stop the site, because both AZs are inside it. Events 5 and 6 would lose data, because live copies faithfully copy deletions; only backups protect against those.

</details>

## Part 2: three businesses, three plans

Each business already runs in two or more AZs. Now each needs a plan for losing its Region.

| Business | What an outage costs | RTO if the Region is lost | RPO | Budget for DR |
|---|---|---|---|---|
| **The bakery** | Small: it can take phone orders, and every order also sends an email it can rebuild from | Within a day | A few hours | Small |
| **A concert-ticket website** | Large on sale days: every minute down loses thousands of sales | About 5 minutes | A few minutes | Moderate |
| **A payment service** used by thousands of online shops | Very large: when it stops, every shop stops taking money | Near zero: no noticeable outage | Near zero | Large |

### Decision 3: choose a strategy for each

For each business, choose the cheapest strategy that meets both its RTO and its RPO, and say in one line why the next cheaper strategy fails.

<details><summary>Model answer</summary>

![A grid of the three businesses against the four strategies, cheapest first. The bakery: backup and restore is the choice; the other three meet the RTO but cost more. Ticket website: backup and restore and pilot light are too slow; warm standby is the choice; multi-site meets it but costs more. Payment service: the first three are too slow; multi-site active/active is the choice.](../../images/03-06-fit-grid.svg)

*Notice that each row's choice is the leftmost cell that fits. Every cell to its right also works, at a higher monthly cost.*

**Long description.** A grid of three made-up businesses against the four strategies, from cheapest to most expensive. The bakery, RTO within a day: backup and restore is the choice; pilot light, warm standby and multi-site meet it but cost more. Ticket website, RTO about 5 minutes: backup and restore and pilot light are too slow; warm standby is the choice; multi-site meets it but costs more. Payment service, RTO near zero: the first three are too slow; multi-site active/active is the choice.

- **The bakery: backup and restore.** Recovery in hours fits a day, and there is no cheaper strategy.
- **Ticket website: warm standby.** It can take traffic at once and scale up within minutes. A pilot light, the next cheaper, typically needs tens of minutes, because its app servers must first be switched on.
- **Payment service: multi-site active/active.** Only copies already serving customers in two or more Regions give a near-zero RTO. A warm standby still needs minutes to scale up.

</details>

### Decision 4: the budget changes

The ticket website's owner reviews the numbers. A whole-Region outage is rare, and on most days a 45-minute outage is survivable. The new RTO is **45 minutes**; the RPO stays at a few minutes. What do you recommend now, and what would you check before agreeing?

<details><summary>Model answer</summary>

**Pilot light.** Its typical recovery, tens of minutes, fits 45 minutes, and its continuously copied data keeps the RPO in minutes, at a lower running cost than a warm standby. Before agreeing, test it: switch on the app servers in the recovery Region and time the whole failover. AWS's ranges are typical, not promises; if the test takes longer than 45 minutes, stay with warm standby.

</details>

### Decision 5: one plan for all three

Which of the three businesses also need point-in-time backups, in addition to their chosen strategy? Why?

<details><summary>Model answer</summary>

**All three.** Every strategy that copies data continuously, including multi-site active/active, copies mistakes, corruption and attacks too. AWS's whitepaper says even active/active needs backups, and that recovering from a data disaster means going back to a point before the damage.

</details>

### Decision 6 (challenge): the bakery's recovery Region

The bakery's German customers' data must stay in the EU. Its US orders have no such rule. Where should each set of backups go, and what happens if someone sets the German backups to copy to US East (Ohio)?

<details><summary>Model answer</summary>

German customers' backups go to a second EU Region, such as Europe (Ireland); US backups can go to a second US Region, such as US East (Ohio). Copying German backups to Ohio would move German customers' data out of the EU and break the bakery's rule, even though the restore would work. The recovery Region inherits the data's rules ([Choosing a Region](02-choosing-a-region.md)).

</details>

## Recap

You sorted failures by how far they reach, and found two, a mistake and an attack, that weren't on the ladder at all. You then matched three businesses to the cheapest of AWS's four strategies that fits their RTO, RPO and budget. Two rules carry over: high availability doesn't replace disaster recovery, and replication doesn't replace backups.

**Next:** [the Module 03 mastery check](07-check.md). Before you take it, retry the practice questions at the end of [03.03](03-surviving-failure.md) and [03.04](04-the-edge.md) without looking back.

---

"Simulation S2: The blast-radius ladder and three recovery plans" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
