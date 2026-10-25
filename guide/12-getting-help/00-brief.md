---
type: brief
id: clf-12-00
title: "Module 12: Getting help"
tasks: ["4.3", "3.8", "2.4"]
objectives: ["12.01a", "12.02a", "12.03a", "12.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 11 and the guardrails primer; about 2 hours in total"
prerequisites: [clf-11-00, clf-09-00, clf-04-00, guardrails-00]
pillars: [operational-excellence, security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html"
---

# Module 12: Recommend a Support plan for the bakery, and send five problems to the right place

This module teaches where help with AWS comes from: Support plans, the tools that watch your account, free sources of answers, and people you can hire. The exam asks which one fits a need.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished [Module 11](../11-paying-for-aws/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 2 hours.

## The scenario

The bakery's online orders are now most of its sales, and its AWS bill has grown to about $1,200 a month (made up). The owner asks: **"Do we need to pay AWS for support, and which plan?"** Then five problems arrive in one week:

| # | The problem | Lesson |
|---|---|---|
| 1 | "There's a charge on our bill we don't recognize." | 12.02 |
| 2 | "How do we make the photo bucket delete old versions?" | 12.03 |
| 3 | "Before our busiest week, can someone check that our design will hold up?" | 12.03 |
| 4 | "Something on an AWS IP address keeps hammering our login page." | 12.03 |
| 5 | "The site is slow, and we think AWS may be having an outage." | 12.02 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **12.01a** Choose the cheapest Support plan that fits a need | 12.01 |
| **12.02a** Say what Trusted Advisor, AWS Health and Support Center each show, and who gets them | 12.02 |
| **12.03a** Route a question to the right place | 12.03 |
| **12.04a** Choose the right kind of paid help: a solutions architect, AWS Professional Services, a partner or AWS Marketplace | 12.03 |

## What this covers on the exam

Task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3), AWS technical resources and Support options. It also covers the customer enablement part of task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8) and the security resources of task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (15 to 20 minutes each):

1. [Support plans](01-support-plans.md)
2. [Tools that watch your account](02-tools-that-watch-your-account.md)
3. [Where to find answers and who can help](03-where-to-find-answers.md)

**Practice:**

- [Lab 17: tour the help every AWS account gets](05-lab-17-support-center-tour.md), after lesson 12.03, in your own account. You open no case and change no plan, so it costs $0.
- [Simulation S15: choose the cheapest Support plan that fits](06-sim-support-plan-chooser.md), on paper, because a paid Support plan can't be tried for free.

**Before the lab:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

**Mastery check:** the module ends with [a mastery check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md), with the AWS pages to read.

> **Dated (checked 2026-10-24):** AWS replaced its Support plans on 2025-12-02, and the old ones end on 2027-01-01 ([end of support notice](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html)). Lesson 12.01 teaches the current plans and translates the old names.

---

"Module 12: Getting help" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
