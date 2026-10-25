---
type: lesson
id: clf-03-01
title: "Regions, Availability Zones and data centers"
tasks: ["3.2", "1.1"]
objectives: ["03.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 15 minutes; works on a phone"
prerequisites: [clf-02-03, guardrails-06, guardrails-07]
terms_introduced: [data center, Availability Zone, Region, single point of failure, Region code, zonal resource, Regional service, global service, load balancer, standby]
pillars: [reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/"
  - "https://aws.amazon.com/about-aws/global-infrastructure/"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html"
---

# A Region holds several Availability Zones, and each Availability Zone holds one or more data centers

AWS builds in three nested layers: data centers, inside Availability Zones, inside Regions. You choose Regions and Availability Zones, never buildings, so high availability on AWS means running copies in more than one Availability Zone.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Telling the benefits apart](../02-why-the-cloud/03-telling-the-benefits-apart.md) (high availability and durability); the bakery scenario is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. In lesson 02.03, what is the difference between high availability and durability?
2. The guardrails primer told you to search for lab resources "in every Region". Why isn't one search in your lab Region enough?

<details><summary>Feedback</summary>

1. **High availability:** the system keeps working when a part fails (can I reach it now?). **Durability:** stored data isn't lost (will it still exist later?).
2. Most resources live in one Region, and most console pages show only the selected Region, so a forgotten resource elsewhere is invisible but still bills ([primer page 07](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md)).

</details>

## What you'll learn

By the end of this lesson, you can explain how Regions, Availability Zones and data centers nest, why Availability Zones don't fail together, and how running in more than one of them gives high availability (objective 03.01a).

Try this before you read on, and guess if you're unsure: the bakery wants its site to "survive losing a data center". Is running everything in one Availability Zone enough?

## The big picture: boxes inside boxes

![A Region box holding three Availability Zones, each with one or more data centers, joined by fast links; another Region far away; edge locations outside.](../../images/03-01-nesting.svg)

*Notice that the boundaries you design around are the Availability Zone and the Region, not the data center. You choose zones and Regions; you never choose a building.*

**Long description.** A Region box holds three Availability Zone boxes, each with its own power, cooling and network, holding three, one and two data centers (an illustration only). Lines join the zones: fast encrypted fiber, many kilometers apart but within 100 km (60 miles). A dashed box is another Region, much farther away, holding nothing unless you copy it there. Four edge locations sit outside the Regions (lesson 03.04).

## A data center is a building; an Availability Zone is one or more of them

A **data center** is a building full of servers, storage and network equipment. AWS describes an **Availability Zone (AZ)** as **one or more** discrete data centers with redundant power, networking and connectivity ([AWS Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)). AWS doesn't say how many an AZ has, and you can't pick one: you choose a Region and, for some resources, an AZ.

### "An Availability Zone is one data center" is wrong

You may have read that an AZ is simply a data center. It isn't: AWS says *one or more*. It's tempting because many diagrams draw an AZ as one box. Since you can't place a copy in "the other building" of an AZ, "survive losing a data center" in practice means "run in at least two AZs".

## Availability Zones don't share a single point of failure

A **single point of failure** is one part whose failure stops the whole system. AZs are built so that one event shouldn't take out two of them. Each has ([Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/); [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html), 2022):

- **its own power** from different substations, with generators and cooling not shared;
- **distance** from the others: many kilometers, but within 100 km (60 miles), so one flood is unlikely to reach two;
- **fast, encrypted fiber** to the others, quick enough to keep two database copies in step;
- **software updates** rolled out one AZ at a time.

Nothing is failure-proof, but failures stay *separate*, so a copy in another AZ keeps running.

## A Region is at least three Availability Zones in one area

A **Region** is a separate geographic area with at least three isolated, physically separate AZs ([AWS Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html)). Regions are isolated from each other, and your resources stay in the Region where you create them unless you copy them.

Each Region has a name and a **Region code**: the bakery runs in **US East (N. Virginia)**, `us-east-1`; its German shop is near **Europe (Frankfurt)**, `eu-central-1`. An AZ's name is the Region code plus a letter, such as `us-east-1a`. Regions launched after 2019-03-20 start switched off in your account.

### "A Region can have just two AZs" is wrong

Some older notes say so, but AWS says every Region has at least three. It's tempting because two is the fewest that gives high availability, and your *account* may see two: newer accounts can use only two AZs in US West (N. California), which has three.

### "Region counts are worth memorizing" is wrong

A number feels like a solid fact, but these change within months, and AWS's own pages disagree on the same day. The exam asks how Regions, AZs and edge locations relate, not how many there are.

> **Dated (checked 2026-10-23):** AWS's [Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) page listed 124 AZs in 39 Regions; its documentation listed 34 Regions in a standard account, leaving out ones that need a separate kind of account, such as AWS GovCloud (US). US East (N. Virginia) had six AZs.

## High availability means running in more than one Availability Zone

Each service sits at a level of the nesting, which tells you what high availability needs from you ([AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)):

| Level | What it means | Examples | What you must do for high availability |
|---|---|---|---|
| **Zonal resource** | Lives in one AZ you choose, and fails with it | An EC2 virtual server; an EBS disk | Put copies in more than one AZ yourself |
| **Regional service** | AWS runs it across several AZs for you | Amazon S3 (most storage classes); AWS Lambda; Amazon DynamoDB | Usually nothing |
| **Global service** | Not tied to one Region | IAM; Amazon Route 53; Amazon CloudFront | Nothing at this level |

Amazon RDS sits in between: a database runs in one AZ unless you turn on **Multi-AZ**, which adds a **standby**, a copy in another AZ that takes over if the first fails ([Multi-AZ deployments for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)). A **load balancer** spreads requests across servers in several AZs and skips unhealthy ones (Module 06).

> **Example:** the bakery's web server and its database without a standby both sit in AZ a: two single points of failure. The fix is a second web server in AZ b behind a load balancer, and Multi-AZ for the database.

![The bakery's site before and after: the web server and database move from one AZ to copies in two AZs behind a load balancer.](../../images/03-01-bakery-layout.svg)

*Notice that only the two zonal parts changed. After the change, no single AZ holds the only copy of anything the site needs.*

**Long description.** Two panels with AZ columns a, b and c. Before: the only web server (EC2) and the database without a standby (RDS) are in AZ a; Lambda and S3 span all three AZs; if AZ a fails, the site stops. After: a load balancer spans AZs a and b, with web servers in both, and the database primary in a with its standby in b; if AZ a fails, web server 2 and the standby carry on.

The extra server, standby and load balancer all bill, failure or not. And this survives losing an AZ, **not** losing the Region or deleting orders by mistake (the standby copies the mistake); lesson 03.03 handles those.

> **Your turn:** a clinic runs its booking site on two EC2 servers, both in `eu-central-1a`, behind a load balancer, with an RDS database that has a standby in `eu-central-1b`. Is the site highly available? Name the single point of failure and the fix.

<details><summary>Model answer</summary>

No. Both web servers are in one AZ, so losing `eu-central-1a` stops the web tier even though the database could fail over. Move one web server to `eu-central-1b`. Two copies only help in different AZs.

</details>

## Summary

- **A data center is a building; an AZ is one or more of them.** You choose AZs, never buildings.
- **AZs don't share a single point of failure:** separate power, apart but within 100 km, joined by fast links.
- **A Region has at least three AZs** and is isolated from other Regions; resources stay in their Region unless you copy them. Don't memorize counts.
- **High availability means copies in at least two AZs.** You place copies of zonal resources such as EC2; Regional services such as S3 and Lambda are spread for you; RDS needs Multi-AZ.

## Practice

1. **How does AWS describe an Availability Zone?**

   A. A single data center in a Region\
   B. One or more data centers in a Region, with redundant power, networking and connectivity\
   C. A group of Regions on one continent\
   D. A small site in a city that caches content near users

   <details><summary>Feedback</summary>

   **B is right.** That is AWS's description.

   - **A is wrong.** An AZ can be several data centers.
   - **C is wrong.** That reverses the nesting: Regions contain AZs.
   - **D is wrong.** That describes an edge location (lesson 03.04).

   </details>

2. **Which statement about Regions is correct?**

   A. Each Region has at least two AZs.\
   B. AWS copies your resources to a second Region automatically.\
   C. Each Region has at least three AZs, and Regions are isolated from each other.\
   D. All Regions are switched on in every account.

   <details><summary>Feedback</summary>

   **C is right.**

   - **A is wrong.** AWS states a minimum of three, even where an account sees two.
   - **B is wrong.** Resources stay in their Region unless you copy or replicate them.
   - **D is wrong.** Regions launched after 2019-03-20 start switched off.

   </details>

3. **Which of these does a company need to set up itself to keep working if an AZ fails?**

   A. Copies of its EC2 web servers in a second AZ\
   B. Copies of its S3 Standard objects in a second AZ\
   C. Copies of its Lambda functions in a second AZ\
   D. A copy of its IAM users in a second AZ

   <details><summary>Feedback</summary>

   **A is right.** EC2 servers are zonal: each lives in one AZ.

   - **B is wrong.** S3 Standard already stores objects across at least three AZs ([Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/)).
   - **C is wrong.** Lambda runs across AZs for you.
   - **D is wrong.** IAM is a global service, not tied to an AZ or a Region.

   </details>

**Next:** [Choosing a Region](02-choosing-a-region.md). To see your account's Regions and AZs, do [Lab 02](05-lab-02-see-the-global-infrastructure.md).

## Where to check the current details

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/), for current counts (checked 2026-10-23)
- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html), AWS documentation (checked 2026-10-23)
- [REL10-BP01 Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html), AWS Well-Architected Framework (checked 2026-10-24)

---

"Regions, Availability Zones and data centers" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
