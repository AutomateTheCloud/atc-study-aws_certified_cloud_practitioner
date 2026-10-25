---
type: brief
id: clf-08-00
title: "Module 08: Building and operating"
tasks: ["3.1", "3.8", "2.2", "1.4"]
objectives: ["08.01a", "08.02a", "08.03a", "08.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 07 and the guardrails primer; about 1.5 hours in total"
prerequisites: [clf-07-00, clf-06-00, clf-04-00, guardrails-00]
pillars: [operational-excellence, reliability, security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 08: Rebuild the bakery's setup identically in a second Region, and email the owner when orders fail

How you give AWS instructions, how a template rebuilds a whole setup, how you watch it, and how its parts pass work to each other. The exam asks which tool or service fits a need, and so do you.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have done Modules [02](../02-why-the-cloud/00-brief.md) to [07](../07-connecting-it/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 1.5 hours, plus about 50 minutes for each optional lab.

## The scenario

The site runs in US East (N. Virginia), set up by hand in the console. The owner (made-up details) asks for four things:

| The owner's request | Lesson |
|---|---|
| "If N. Virginia goes down, I want the same setup ready in US East (Ohio). Exactly the same." | 08.01 |
| "Our new developer needs a test copy every week, without touching the real one." | 08.01 |
| "When orders start failing, email me." | 08.03, 08.04 |
| "One slow part shouldn't stall the whole order. And test code changes before they go live." | 08.04 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **08.01a** Choose the console, the CLI, an SDK or infrastructure as code for a task | 08.01 |
| **08.02a** Explain how infrastructure as code makes work repeatable and cheaper | 08.01 |
| **08.03a** Pick the tool for an operations question: CloudWatch, X-Ray or CloudTrail | 08.03 |
| **08.04a** Choose a messaging service by the shape of the message, and name the build or release tool | 08.04 |

## What this covers on the exam

Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1), deploying and operating (lesson 08.01), and task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8), other service categories (08.03 and 08.04). It also touches monitoring and auditing from task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) (08.03) and the benefits of automation from task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4) (08.01). AWS CloudShell and AWS CodeDeploy are out of scope; the lessons treat them as likely wrong answers. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (15 to 20 minutes each):

1. [Four ways in, and infrastructure as code](01-four-ways-in.md)
2. [Watching workloads](03-watching-workloads.md): CloudWatch, X-Ray and CloudTrail
3. [Connecting parts, shipping software](04-connecting-parts-shipping-software.md): messaging, email, build and release

**Optional labs:** this module has no core lab, because the exam asks which service fits, not how to set it up. Both run in US East (N. Virginia) and cost nothing on the Free plan.

- [Optional lab 10: the same bucket three ways](05-lab-10-same-bucket-three-ways.md), after lesson 08.01: console, CLI and a template.
- [Optional lab 11: an alarm on errors](06-lab-11-alarm-on-errors.md), after lesson 08.04: a CloudWatch alarm that emails you.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md), [CloudShell without access keys](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

**Mastery check:** the module ends with [a mastery check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md), with the AWS pages to read.

---

"Module 08: Building and operating" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
