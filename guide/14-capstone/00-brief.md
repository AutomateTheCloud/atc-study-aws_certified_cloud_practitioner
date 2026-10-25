---
type: brief
id: clf-14-00
title: "Module 14: Capstone: a Well-Architected review"
tasks: ["1.2", "4.2"]
objectives: ["14.01a", "14.02a", "14.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 13; about 1 hour for Lab 19, plus about 3 hours if you take the optional review"
prerequisites: [clf-13-00, clf-12-00, clf-11-00, clf-02-05]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html"
---

# Module 14: Close out your course account safely, and, if you want more practice, review the bakery's workload against all six pillars

This module has one step everyone who used an AWS account must take, and optional practice beyond the exam.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished Modules 02 to 13. **Time:** about 1 hour for Lab 19 over two days, plus about 3 hours if you do the optional review.

## What you must do, and what's optional

**Everyone who ran a lab: do Lab 19.** It sweeps every Region for anything the labs left behind, reads the bill, keeps your guardrails and checks again the next day. A forgotten resource keeps billing whether or not you study, so don't skip it. If you never used an AWS account for the course, you can skip this module.

**Optional: the capstone review and Lab 18.** The CLF-C02 exam only asks you to recognize the six pillars of the Well-Architected Framework ([lesson 02.05](../02-why-the-cloud/05-the-well-architected-framework.md)) and tell them apart. Doing a full review of a workload, pricing the fixes and choosing a Support plan is real practitioner work, well beyond that. Take it if you want to pull the whole course together; skip it if you're preparing for the exam on a tight schedule.

## You'll be able to

| Objective | Lesson or lab |
|---|---|
| **14.03a** Close out an AWS account safely: find every leftover, check the bill and keep the guardrails [P·Ap] | Lab 19 |
| **14.01a** (optional) Assemble a pillar-by-pillar review of a workload, price the fixes and recommend a Support plan, justifying each choice [J·Ev] | 14.01 |
| **14.02a** (optional) Record a review in the Well-Architected Tool and read its risks [P·Ap] | Optional lab 18 |

## What this covers on the exam

Lab 19 practices task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2), resources for billing, budgets and cost management. The optional review applies task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2), the Well-Architected Framework, with what you learned for the other tasks. We checked the exam guide on 2026-10-24.

## How the module is laid out

1. [Lab 19: close out the account you used for the course](03-lab-19-close-out.md), about 45 minutes, plus 10 the next day. Nothing is billed.
2. Optional: [the capstone review](01-the-capstone-review.md), about 20 minutes to read and 90 minutes for your own review of the bakery's workload as Labs 05 to 11 built it. You work from an inventory, so you don't need to have run those labs. It's scored with a rubric, not a mastery check.
3. [Optional lab 18: record the bakery's review in the AWS Well-Architected Tool](02-lab-18-well-architected-tool-review.md), about 50 minutes; the Tool has no charge. If you do it, do it before Lab 19, so the close-out sweep also checks that its workload is gone.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

---

"Module 14: Capstone: a Well-Architected review" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
