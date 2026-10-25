---
type: sim
id: clf-03-06
title: "Simulation S2: The blast-radius ladder and three recovery plans"
tasks: ["3.2", "1.1"]
objectives: ["03.03a"]
reader: "Adult studying alone, possibly new to IT; about 20 minutes; paper or a spreadsheet helps"
prerequisites: ["clf-03-01", "clf-03-03"]
terms_introduced: []
pillars: [reliability, cost-optimization]
lab: "S2"
rung: L2-L3
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "20 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
---

# Simulation S2: The blast-radius ladder and three recovery plans

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [03.01](01-regions-availability-zones-data-centers.md) and [03.03](03-surviving-failure.md). **Time:** about 20 minutes. **Cost:** $0; no AWS account is used. You can't fail an Availability Zone or a Region for real, so we simulate it.

**Goal:** practice the two decisions the exam tests here: which protection a failure needs (high availability, disaster recovery or a backup), and which of AWS's four disaster recovery strategies fits a business's RTO, RPO and budget. **End state:** a completed ladder table and three one-line recommendations.

## The rules of this simulation

The businesses and their numbers are **made up for teaching**. The strategies, their order and their typical recovery times are AWS's, from its disaster recovery whitepaper (2021, checked 2026-10-24) ([Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)).

| Strategy, cheapest first | Typical RTO and RPO |
|---|---|
| Backup and restore | Hours |
| Pilot light | Tens of minutes |
| Warm standby | Minutes |
| Multi-site active/active | Near zero (real time) |

- **High availability** (two or more AZs in one Region) handles a failed server, data center or AZ.
- **Disaster recovery** handles losing a whole Region. Pick the **cheapest strategy that meets both the RTO and the RPO**.
- **Replication copies mistakes.** Only a point-in-time backup undoes damage to the data itself.

![A ladder of failures from one server up to a whole Region, with high availability for the lower rungs, disaster recovery for the top, and a separate box for mistakes in the data.](../../images/03-03-blast-radius-ladder.svg)

*Notice the box off the ladder. Part 1 has two events that belong there.*

**Long description.** Four rungs, largest first. A whole Region: a copy in another Region; disaster recovery. One Availability Zone, one data center, one server: running in two or more AZs, plus automatic replacement for a server; high availability. Off the ladder, dashed: a mistake or attack on the data itself reaches every live copy; only a point-in-time backup from before it undoes it.

## Part 1: the blast-radius ladder

The bakery's site runs as lesson 03.01 left it: two web servers in two AZs behind a load balancer, and an order database with a standby in the second AZ. German customers are served from Europe (Frankfurt).

### Decision 1: place each event on the ladder

For each event, write its rung (server, data center, AZ, Region, or off the ladder) and what keeps the bakery going.

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
| 1 | Server | Web server 2 keeps taking orders. High availability. |
| 2 | Data center | The AZ may carry on; if not, the copies in the second AZ take over. High availability. |
| 3 | AZ | Web server 2 and the standby database take over. High availability. |
| 4 | Region | Nothing in Frankfurt helps: both AZs are in it. The bakery needs backups, or a copy, in another EU Region. Disaster recovery. |
| 5 | Off the ladder | The standby deletes the orders too, within moments. Only a point-in-time backup from before the mistake brings them back. |
| 6 | Off the ladder | Earlier versions (S3 versioning) or a backup restore the photos. Don't count on other live copies: a stolen password may reach them too. Then lock out the attacker (Module 04). |

Events 4, 5 and 6 would still stop the bakery or lose data, even with two AZs. Events 5 and 6 are the ones people miss: a second live copy doesn't protect data from a mistake, or from someone who can reach it.

</details>

## Part 2: three businesses, three plans

Each business already runs in two or more AZs. Now each needs a plan for losing its Region.

| Business | What an outage costs | RTO if the Region is lost | RPO | Budget for DR |
|---|---|---|---|---|
| **The bakery** | Small: it can take phone orders | Within a day | A few hours | Small |
| **A concert-ticket website** | Large on sale days | About 5 minutes | A few minutes | Moderate |
| **A payment service** used by thousands of shops | Very large: every shop stops taking money | Near zero | Near zero | Large |

### Decision 2: choose a strategy for each

For each business, choose the cheapest strategy that meets both its RTO and its RPO, and say in one line why the next cheaper strategy fails.

<details><summary>Model answer</summary>

![A grid of the three businesses against the four strategies, cheapest first, marking for each row which strategies are too slow, which one is the choice, and which meet the need at higher cost.](../../images/03-06-fit-grid.svg)

*Notice that each row's choice is the leftmost cell that fits. Every cell to its right also works, at a higher monthly cost.*

**Long description.** A grid of three made-up businesses against the four strategies, from cheapest to most expensive. The bakery, RTO within a day: backup and restore is the choice; pilot light, warm standby and multi-site meet it but cost more. Ticket website, RTO about 5 minutes: backup and restore and pilot light are too slow; warm standby is the choice; multi-site meets it but costs more. Payment service, RTO near zero: the first three are too slow; multi-site active/active is the choice.

- **The bakery: backup and restore.** Recovery in hours fits a day, and there is no cheaper strategy.
- **Ticket website: warm standby.** It can take traffic at once and scale up within minutes. A pilot light typically needs tens of minutes, because its app servers must first be switched on.
- **Payment service: multi-site active/active.** Only copies already serving customers in two or more Regions give a near-zero RTO. A warm standby still needs minutes to scale up.

</details>

### Decision 3: the budget changes

The ticket website's owner decides a 45-minute outage is survivable; the RPO stays at a few minutes. What do you recommend now, and what would you check first?

<details><summary>Model answer</summary>

**Pilot light.** Tens of minutes fits 45, and continuously copied data keeps the RPO in minutes, for less than a warm standby. Test it first and time the failover: AWS's ranges are typical, not promises. If it takes longer than 45 minutes, stay with warm standby.

</details>

### Decision 4: backups for whom?

Which of the three businesses also need point-in-time backups, in addition to their chosen strategy?

<details><summary>Model answer</summary>

**All three.** Every strategy that copies data continuously, including multi-site active/active, copies mistakes, corruption and attacks too. AWS's whitepaper says even active/active needs backups ([Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf)).

</details>

## Recap

You sorted failures by how far they reach, found two that weren't on the ladder at all, and matched three businesses to the cheapest strategy that fits. Two rules carry over to the exam: high availability doesn't replace disaster recovery, and replication doesn't replace backups.

**Next:** [the Module 03 mastery check](07-check.md).

---

"Simulation S2: The blast-radius ladder and three recovery plans" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
