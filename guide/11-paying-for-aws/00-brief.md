---
type: brief
id: clf-11-00
title: "Module 11: Paying for AWS"
tasks: ["4.1", "4.2", "1.4"]
objectives: ["11.01a", "11.02a", "11.03a", "11.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 10 and the guardrails primer; about 2.5 hours in total"
prerequisites: [clf-10-00, clf-06-00, clf-05-00, guardrails-05]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/pricing/"
  - "https://aws.amazon.com/free/"
---

# Module 11: Explain the bakery's growing bill, cut it, price a new feature, and show each team its own costs

This module teaches what drives an AWS bill, the ways to pay for the same servers, the tools that estimate, watch and analyze costs, and how many accounts share one bill. The exam asks which pricing model or tool fits a need, not how to work out a bill.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished Modules 02 to 10 and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 2.5 hours, plus 25 minutes for the optional lab.

## The scenario

The bakery's December bill is nearly three times November's (made-up details). The owner has four requests:

| The owner's request | Lesson |
|---|---|
| **"Explain it."** Which charges grew, and is anything wrong? | 11.01 |
| **"Cut it."** Pay less for what runs all year, without risking December. | 11.02 |
| **"Price it first."** Estimate the next feature, a cake designer, before anyone builds it, and warn us next time. | 11.03 |
| **"Show each team its own costs."** The shop, kitchen and delivery teams each want their own figures. | 11.04 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **11.01a** Identify what drives a bill | 11.01 |
| **11.02a** Choose a purchasing option for a usage pattern | 11.02 |
| **11.03a** Pick the cost tool for each stage: estimate, watch, analyze | 11.03 |
| **11.04a** Explain who gets a discount in an organization, and how tags reach cost reports | 11.04 |

## What this covers on the exam

Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1), pricing models (lessons 11.01 and 11.02), and task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2), billing, budget and cost management (11.03 and 11.04). It also touches task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4), cloud economics. Module 05 covered the storage tiers in 4.1. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (20 to 25 minutes each):

1. [How AWS charges](01-how-aws-charges.md)
2. [Purchasing options](02-purchasing-options.md)
3. [Estimate, watch, analyze](03-estimate-watch-analyze.md)
4. [Many accounts, one bill](04-many-accounts-one-bill.md)

**Practice:**

- [Lab 15: price the bakery's setup in the AWS Pricing Calculator](05-lab-15-pricing-calculator.md), after lesson 11.03; no AWS account needed.
- [Simulation S13: choose how to pay for each workload](07-sim-purchasing-option-tree.md), after lesson 11.02, on paper, because Savings Plans and Reserved Instances aren't available on the Free plan.
- [Optional lab 16: turn on cost allocation tags](06-lab-16-cost-allocation-tags.md), after lesson 11.04, in your own account at $0; the exam doesn't need it.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

> **Dated (checked 2026-10-24):** prices, discount maximums, the number of Savings Plans types (four today) and the Free Tier's terms, which changed in July 2025, all move. Each lesson dates them where they appear.

**Mastery check:** the module ends with [a mastery check](09-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](10-beyond-the-exam.md), with the AWS pages to read.

---

"Module 11: Paying for AWS" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
