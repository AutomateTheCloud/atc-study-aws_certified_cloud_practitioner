---
type: brief
id: clf-02-00
title: "Module 02: Why organizations use the cloud"
tasks: ["1.1", "1.2", "1.4", "3.1"]
objectives: ["02.01a", "02.02a", "02.03a", "02.04a", "02.05a"]
reader: "Adult studying alone, possibly new to IT; first module of the guide; about 3 hours in total"
prerequisites: []
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
---

# Module 02: Advise a small bakery on whether to move to the cloud

This module teaches why organizations move computing to the cloud: what cloud computing is, the benefits the exam names, what owning servers really costs, and the Well-Architected Framework's six pillars.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. This is the first module, so it assumes only everyday computer use. **Time:** about 3 hours, spread over several sessions.

## The scenario

A small bakery takes pickup orders through its own website, which runs on three servers it owns, in a room behind the shop. The site crashes in the busy holiday weeks and sits nearly idle in January. The owner asks: should we move to the cloud, and what would change? The facts are made up for teaching, and later modules reuse the bakery.

| Fact | Value (made up) |
|---|---|
| What one server can handle | About 20 orders an hour |
| Busiest hour in January | About 10 orders |
| Busiest hour in December | About 120 orders |
| Average order | About $20 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **02.01a** Classify a setup as cloud, hybrid or on-premises | 02.01 |
| **02.02a** Explain idle cost and lost sales from a demand curve | 02.02 |
| **02.03a** Name the benefit a scenario shows, and say why it isn't one of the others | 02.03 |
| **02.04a** Compare on-premises and pay-as-you-go costs in plain numbers | 02.04 |
| **02.05a** Match a concern to a Well-Architected pillar, and explain a trade-off | 02.05 |

## What this covers on the exam

The start of Domain 1, Cloud Concepts: task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1), the benefits of the AWS Cloud (lessons 02.01 to 02.03); task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4), cloud economics (02.02 and 02.04); and task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2), the Well-Architected Framework (02.05). It also covers the deployment models in task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1) (02.01). Exam guide checked 2026-10-23.

## How the module is laid out

**Lessons** (about 25 minutes each):

1. [What cloud computing is](01-what-cloud-computing-is.md)
2. [Before and after: the demand curve](02-before-and-after-the-demand-curve.md)
3. [Telling the benefits apart](03-telling-the-benefits-apart.md)
4. [What a data center really costs](04-what-a-data-center-really-costs.md)
5. [The Well-Architected Framework](05-the-well-architected-framework.md)

**Practice:** [Lab 01: your first resource](06-lab-01-first-resource.md), in your own AWS account, any time after lesson 02.03. It costs nothing on the Free plan (as of 2026-10-24). The exam doesn't ask you to build anything, but timing a real resource makes agility concrete.

**Before the lab:** work through the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md), above all [securing the root user](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your everyday admin identity](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md). The lessons need no AWS account.

**Mastery check:** the module ends with [a mastery check](08-check.md); you pass at 80%. From Module 03 on, every lesson's warm-up brings back ideas from this one. **Beyond the exam:** [what this module left out](09-beyond-the-exam.md), with the AWS pages to read.

---

"Module 02: Why organizations use the cloud" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
