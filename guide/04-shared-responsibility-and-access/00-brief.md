---
type: brief
id: clf-04-00
title: "Module 04: Who secures what: shared responsibility and access"
tasks: ["2.1", "2.3"]
objectives: ["04.01a", "04.02a", "04.03a", "04.03b", "04.04a", "04.05a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 2.5 hours in total"
prerequisites: [clf-02-00, guardrails-00]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
---

# Module 04: Give a new teammate access to the cake photos and nothing else, then explain who patches what

This module teaches how security work is split between AWS and you, and how you decide who can do what in your account. The exam asks who is responsible for a task and which identity, policy or sign-in fits a need.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) and [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished [Module 02](../02-why-the-cloud/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 2.5 hours, plus 20 minutes for the optional simulation and 50 for the optional lab.

## The scenario

The bakery's ordering site now runs on AWS (made-up details), and the owner has two requests: "Give our new teammate access to the cake photos, **and nothing else**," and "Do I still have to install security updates? For which parts?"

| Part of the site | AWS service | Used in |
|---|---|---|
| The web server | Amazon EC2 | 04.01, 04.02 |
| The order database | Amazon RDS | 04.01, 04.02 |
| The order functions | AWS Lambda | 04.01 |
| The cake photos | A bucket in Amazon S3 | 04.01, 04.03 to 04.05, Lab 03 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **04.01a** Say whether AWS or you does a security task on EC2, RDS, Lambda or S3, and why | 04.01 |
| **04.02a** Explain what "shared" means, with examples of inherited, shared and customer-specific controls | 04.02 |
| **04.03a** Pick the right kind of identity for a case | 04.03 |
| **04.03b** Recognize the tasks only the root user can do | 04.03 |
| **04.04a** Choose a kind of policy, apply least privilege, and predict allow or deny in simple cases | 04.04 |
| **04.05a** Choose a way to store credentials and a way to manage identities | 04.05 |

## What this covers on the exam

Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1), the AWS shared responsibility model (lessons 04.01 and 04.02), and task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3), access management (04.03 to 04.05). Domain 2, Security and Compliance, is 30% of the exam, the largest share. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (about 20 minutes each):

1. [Security of the cloud vs security in the cloud](01-security-of-vs-in-the-cloud.md)
2. [Shared, inherited and customer-specific controls](02-shared-inherited-customer-specific.md)
3. [Identities](03-identities.md)
4. [Policies and least privilege](04-policies-and-least-privilege.md)
5. [Credentials and federation](05-credentials-and-federation.md)

**Practice:**

- [Optional simulation S3: the responsibility slider](08-sim-responsibility-slider.md), after 04.02, on paper, if you want more decisions to make; the main path doesn't need it.
- [Lab 03: a group and a policy](06-lab-03-a-group-and-a-policy.md), after lesson 04.04, in your own account; $0 on the Free plan (as of 2026-10-24).
- [Optional lab 04: finish and fix a policy](07-lab-04-finish-and-fix-a-policy.md), if you want more practice writing policies; the exam doesn't need it.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

**Mastery check:** the module ends with [a mastery check](10-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](11-beyond-the-exam.md), with the AWS pages to read.

---

"Module 04: Who secures what: shared responsibility and access" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
