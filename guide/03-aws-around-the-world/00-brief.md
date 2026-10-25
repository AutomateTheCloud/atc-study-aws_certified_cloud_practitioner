---
type: brief
id: clf-03-00
title: "Module 03: AWS around the world"
tasks: ["3.2", "1.1"]
objectives: ["03.01a", "03.02a", "03.03a", "03.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 1 hour 30 minutes in total"
prerequisites: [clf-02-00, guardrails-00]
pillars: [reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/"
---

# Module 03: Decide where in the world the bakery's site runs, and how it survives a failure

This module teaches how AWS spreads its infrastructure around the world: Regions, Availability Zones and edge locations. The exam asks how they relate and which one fits a need: keeping a site close to its customers, within the rules, and running when something breaks.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished [Module 02](../02-why-the-cloud/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 1 hour 30 minutes.

## The scenario

The bakery's ordering site runs in one AWS Region, US East (N. Virginia): a web server in Amazon EC2, an order database in Amazon RDS with no standby, functions in AWS Lambda, and cake photos in Amazon S3. The owner has opened a second shop in Germany (made-up details) and wants three things: a fast site for customers in both countries, German customers' data kept in the European Union, and a site that survives losing a data center.

## You'll be able to

| Objective | Lesson |
|---|---|
| **03.01a** Explain how Regions, Availability Zones and data centers nest, and how that gives high availability | 03.01 |
| **03.02a** Choose a Region for a workload and justify the choice | 03.02 |
| **03.03a** Choose a way to survive failure from how long you can be down, how much data you can lose, and the budget | 03.03 |
| **03.04a** Say where each kind of edge site runs and what it's for | 03.04 |

## What this covers on the exam

Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2), the AWS global infrastructure (all four lessons). It also finishes the global-infrastructure part of task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1), which [lesson 02.03](../02-why-the-cloud/03-telling-the-benefits-apart.md) began. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (12 to 15 minutes each):

1. [Regions, Availability Zones and data centers](01-regions-availability-zones-data-centers.md)
2. [Choosing a Region](02-choosing-a-region.md)
3. [Surviving failure](03-surviving-failure.md)
4. [The edge](04-the-edge.md)

**Practice:**

- [Lab 02: see the global infrastructure](05-lab-02-see-the-global-infrastructure.md), after the lessons, in your own account. It only looks; it creates nothing.
- [Simulation S2: the blast radius](06-sim-blast-radius.md), after Lab 02, on paper: you can't fail a Region for real.

**Before Lab 02:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md). The lessons need no AWS account.

**Mastery check:** the module ends with [a mastery check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md), with the AWS pages to read.

**Numbers that change:** Region and AZ counts change every year. Learn how the pieces relate, not how many there are.

---

"Module 03: AWS around the world" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
