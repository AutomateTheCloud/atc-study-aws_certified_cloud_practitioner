---
type: brief
id: clf-09-00
title: "Module 09: Protecting, governing and proving compliance"
tasks: ["2.2", "2.4", "2.3", "2.1"]
objectives: ["09.01a", "09.02a", "09.03a", "09.04a", "09.05a", "09.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08 and the guardrails primer; about 4 hours in total"
prerequisites: [clf-08-00, clf-07-00, clf-04-00, guardrails-00]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 09: Answer an auditor's five questions with evidence, and put layered protection in front of the bakery's site

This module teaches the services that protect an AWS account, watch it, and prove what happened in it. The exam asks which one fits a need.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1), [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2), [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished [Module 08](../08-building-and-operating/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 4 hours.

## The scenario

Before signing a contract, a large customer's auditor sends the bakery five questions (made-up details):

| # | The auditor asks | Answered in |
|---|---|---|
| 1 | Who changed your systems recently? | 09.01 |
| 2 | Does anyone use the account's root user? | 09.01 |
| 3 | Does anyone have permissions they don't use? | 09.01 |
| 4 | Is the stored data encrypted, and who holds the keys? | 09.02 |
| 5 | How do you know AWS protects its data centers? | 09.05 |

The same week, a flood of traffic knocks a competitor's site offline, and the owner asks what protects the bakery (09.03 and 09.04).

## You'll be able to

| Objective | Lesson |
|---|---|
| **09.01a** Choose the service that answers an audit question | 09.01 |
| **09.02a** Choose an encryption and key approach | 09.02 |
| **09.03a** Match a security finding to the service that raised it | 09.03 |
| **09.04a** Choose protections for an attack type | 09.04 |
| **09.05a** State the compliance work that stays yours, and explain a service control policy as a ceiling | 09.05 |
| **09.06a** Assemble and justify layered controls | 09.06 |

## What this covers on the exam

Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2), security, governance and compliance concepts, and task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4), security services and resources. It also touches tasks [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3) (access across many accounts) and [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) (shared responsibility, 09.06). Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (15 to 20 minutes each):

1. [Who did what, how it runs, how it was set](01-who-did-what.md): CloudTrail, CloudWatch, Config, access reports
2. [Encryption](02-encryption.md): ACM, KMS, CloudHSM, Macie
3. [Finding threats and weaknesses](03-finding-threats-and-weaknesses.md): GuardDuty, Inspector, Security Hub, Detective, Trusted Advisor
4. [The front door](04-the-front-door.md): Shield, WAF, Firewall Manager
5. [Compliance and governance](05-compliance-and-governance.md): Artifact, Organizations, SCPs, Control Tower
6. [A defense map](06-a-defense-map.md): layers, and who does what

**Practice:**

- [Lab 12: answer the auditor](07-lab-12-answer-the-auditor.md), after lesson 09.05, in your own account; $0 on the Free plan (as of 2026-10-24).
- [Simulation S9: security findings](08-sim-security-findings-tour.md) and [Simulation S11: organizations and SCPs](10-sim-organizations-and-scps.md), on paper: GuardDuty and Security Hub CSPM were blocked on the Free plan (checked 2026-10-23), and an organization would upgrade the account.

**Before the lab:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md).

**Mastery check:** the module ends with [a mastery check](11-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](12-beyond-the-exam.md), with the AWS pages to read.

---

"Module 09: Protecting, governing and proving compliance" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
