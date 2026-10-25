---
type: brief
id: clf-05-00
title: "Module 05: Storing data: storage and databases"
tasks: ["3.6", "3.4", "4.1", "2.1"]
objectives: ["05.01a", "05.02a", "05.03a", "05.04a", "05.05a", "05.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 04 and the guardrails primer; about 3 hours in total"
prerequisites: [clf-04-00, clf-03-00, clf-02-00, guardrails-00]
pillars: [reliability, security, cost-optimization, performance-efficiency]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 05: Find the right home for each kind of the bakery's data, and keep it safe and affordable

This module teaches where data lives on AWS: on disks, in shared folders, in object storage and in databases. The exam asks which service fits a need, and so do you.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have done Modules [02](../02-why-the-cloud/00-brief.md), [03](../03-aws-around-the-world/00-brief.md) and [04](../04-shared-responsibility-and-access/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 3 hours, plus 30 minutes for the optional lab.

## The scenario

The owner wants a plan for all the bakery's data (made-up details).

| The bakery's data | What it is like | Placed in |
|---|---|---|
| **Orders** | Written all day; must never be lost | 05.05 |
| **Shopping carts** | Read and written constantly; thrown away after the visit | 05.05 |
| **Cake photos** | Shown on the site; old ones rarely viewed | 05.01, 05.02 |
| **Nightly backups** | Copies of the order database and the web server's disk | 05.04 |
| **Tax archives** | Kept seven years; almost never read | 05.02 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **05.01a** Choose block, file or object storage for an access pattern | 05.01 |
| **05.02a** Explain how Block Public Access, versioning and default encryption each protect data in S3 | 05.02 |
| **05.03a** Choose an S3 storage class and a lifecycle rule | 05.02 |
| **05.04a** Match a hybrid storage or backup need to an AWS service | 05.04 |
| **05.05a** Choose between a self-managed and a managed database, and between high availability and read scaling | 05.05 |
| **05.06a** Pick a database for a shape of data | 05.05 |

## What this covers on the exam

Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6), storage services (lessons 05.01 to 05.04), and task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4), database services (05.05). It also touches tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) (storage pricing) and [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) (shared responsibility). Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (20 to 25 minutes each):

1. [Block, file and object storage](01-block-file-object.md)
2. [S3 protection, storage classes and lifecycle](02-s3-in-practice.md)
3. [Hybrid storage and backup](04-hybrid-storage-and-backup.md)
4. [Managed databases and choosing one](05-managed-or-self-managed-databases.md)

**Practice:**

- [Lab 05: versions and lifecycle](07-lab-05-versions-and-lifecycle.md), after lesson 05.02, in your own account; nothing is billed on the Free plan.
- [Simulation S6: Multi-AZ vs read replica](10-sim-multi-az-vs-read-replica.md), after lesson 05.05, on paper, because a real database bills by the hour.
- [Optional lab 06: a DynamoDB table](08-lab-06-a-dynamodb-table.md), if you want to try DynamoDB; the exam doesn't need it.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md), [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md) and [Block Public Access for your account](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md).

**Mastery check:** the module ends with [a mastery check](11-check.md); you pass at 80%. A mixed practice set on Modules 02 to 05 follows. **Beyond the exam:** [what this module left out](12-beyond-the-exam.md), with the AWS pages to read.

---

"Module 05: Storing data: storage and databases" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
