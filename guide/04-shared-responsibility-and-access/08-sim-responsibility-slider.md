---
type: sim
id: clf-04-08
title: "Simulation S3: Slide the line from your own servers to Amazon S3"
tasks: ["2.1"]
objectives: ["04.01a", "04.02a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 04.01 and 04.02; about 20 minutes; paper or a spreadsheet helps"
prerequisites: ["clf-04-01", "clf-04-02"]
terms_introduced: []
pillars: [security]
lab: "S3"
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
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html"
---

# Simulation S3: Slide the line from your own servers to Amazon S3

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [04.01](01-security-of-vs-in-the-cloud.md) and [04.02](02-shared-inherited-customer-specific.md). **Time:** about 20 minutes. **Cost:** $0; this simulation uses no AWS account.

**Goal:** move the bakery's site one step at a time from servers in its back room to Amazon S3, and at each step decide which security tasks pass to AWS and which stay with the bakery. **End state:** a filled-in grid.

**Why this matters:** the exam asks how responsibilities shift between EC2, RDS and Lambda (task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1)), and the owner asked whether she still has to install security updates. The honest answer is "it depends on the service", and this grid shows it.

## The rules

1. **Use only what AWS publishes.** Every answer comes from an AWS page, cited in the model answers.
2. **"Not stated" is a real answer.** If the pages don't say who does a task for a service, write "not stated" rather than guess.
3. **You** means the customer: the bakery.

## The data

The bakery's site has four parts on AWS (from the [module brief](00-brief.md)): the web server on Amazon EC2, the order database on Amazon RDS, the order functions on AWS Lambda, and the cake photos in Amazon S3. Before the move, everything ran on the bakery's own servers.

Copy this grid. In each cell, write **AWS**, **You** or **Not stated**.

| Security task | On-premises | EC2 | RDS | Lambda | S3 |
|---|---|---|---|---|---|
| Facilities, power, cooling, hardware and servers | | | | | |
| Operating system: install and patch | | | | | |
| Database engine or language runtime: install and patch | | | | | |
| Backups, high availability and scaling | | | | | |
| Your code, its dependencies, and tuning | | | | | |
| Your data, its encryption, and who can access it | | | | | |

## Decisions

### Decision 1: from the back room to EC2

The bakery moves its web server, and for now its database too, onto EC2 virtual servers. Which rows of the grid move to AWS? Fill in the first two columns.

<details><summary>Model answer</summary>

On-premises, every row is **You**. On EC2, only the first row moves to **AWS**. AWS runs everything from the host operating system and the virtualization layer down to the buildings; you keep the guest operating system, including its security patches, any software you install, and the security group firewall settings ([Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)). For a database on EC2, the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) adds backups, high availability, scaling and the database software to your list.

</details>

### Decision 2: the database moves to RDS

The database moves from EC2 to Amazon RDS, a managed database service. Which rows move to AWS, and which two stay with the bakery?

<details><summary>Model answer</summary>

The operating system, the database software, backups, high availability and scaling all move to **AWS**. That's the RDS User Guide's own comparison of on-premises, EC2 and RDS. Two rows stay with **You**: tuning (RDS says query tuning is yours) and your data and who can access it, which you control with IAM and by placing the database in a virtual private cloud (VPC), a private network you'll meet in Module 07 ([What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)).

</details>

### Decision 3: the order functions on Lambda

Sort these eight statements into **AWS** and **You**, for the bakery's functions on AWS Lambda.

1. Maintaining the servers the functions run on.
2. Adding capacity and scaling when orders spike.
3. Publishing security updates for a supported managed runtime.
4. Fixing a security flaw in a library the function code uses.
5. Moving a function to a supported runtime before its runtime is deprecated.
6. Rebuilding a function packaged as a container image from the latest base image.
7. Deciding what the function's IAM role is allowed to do.
8. Judging how sensitive the order data is, and which laws apply.

<details><summary>Model answer</summary>

**AWS:** 1, 2 and 3. Lambda manages the infrastructure, including server maintenance, capacity, scaling and patching ([What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)). It publishes runtime security updates and, by default, applies them to functions on managed runtimes ([Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)).

**You:** 4 to 8. The runtimes page puts your code *and its dependencies*, the move off a deprecated runtime, and container-image rebuilds on you. The security page adds the sensitivity of your data, your company's requirements and the laws that apply ([Security in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)). The permissions you give the function's role are yours too, as on every service.

"On Lambda you manage only the code and its permissions" is too narrow: it leaves out the dependencies, the runtime deadline and container images.

</details>

### Decision 4: the cake photos in S3

What is left for the bakery in the S3 column? Then judge this case: a photo bucket was made public by mistake, and private photos leaked. Whose responsibility was it?

<details><summary>Model answer</summary>

For services such as S3, AWS runs the infrastructure, the operating system and the platform; you manage your data, including its encryption options, classify it, and set permissions with IAM ([Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)). So only the last row is **You**, and the "your code" row doesn't apply: no code of yours runs in S3.

The leak is the bakery's responsibility: who can access the data is the customer's job on every service. A new bucket blocks public access by default (Lab 01), so someone changed that setting.

</details>

## The whole slider

![A grid of six security tasks against five columns: on-premises, EC2, RDS, Lambda and S3. Moving right, more cells change from You to AWS. Your data and who can access it stays You in every column.](../../images/04-08-responsibility-grid.svg)

*Figure: the completed grid. Notice how the line between AWS and you climbs as you move right, and that the bottom row never moves: on every service, your data and who can access it are yours. The two dashed cells are where the pages publish nothing, or nothing applies.*

**Long description.** Six rows, five columns: on-premises, EC2, RDS, Lambda, S3. Facilities and hardware: You on-premises, AWS elsewhere. Operating system, and database engine or runtime: You on-premises and on EC2, AWS on RDS, Lambda and S3. Backups, high availability and scaling: You on-premises and on EC2, AWS on RDS, AWS for scaling on Lambda, not stated for S3. Your code, dependencies and tuning: You wherever code runs; none runs in S3. Your data and who can access it: You everywhere. Notes: Lambda's runtime patching is AWS's for managed runtimes and only until deprecation; you rebuild container images; no split is published for Lambda's backups or high availability.

Patching is the **shared control** from [04.02](02-shared-inherited-customer-specific.md): AWS patches its infrastructure, you patch your guest operating system and applications. The grid shows where your half starts for each service.

## Recap

Moving right, AWS takes on more of the work, but never your data or who can reach it. The exam's examples, EC2, RDS and Lambda, sit at three different points on the slider. When someone says "AWS handles security now", ask: which service, and which row?

**Next:** [Identities](03-identities.md), on the row that never moves: who can access what.

---

"Simulation S3: Slide the line from your own servers to Amazon S3" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
