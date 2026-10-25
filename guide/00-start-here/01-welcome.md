---
type: lesson
id: clf-00-01
title: "Welcome"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT; the first page of the guide; about 10 minutes; works on a phone"
prerequisites: []
terms_introduced: [AWS, CLF-C02, module, path, guardrails primer, lab, simulation, mastery check]
pillars: []
facts_checked: 2026-10-23
sources:
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
  - "https://aws.amazon.com/certification/policies/before-testing/"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/free/"
---

# This guide teaches you to understand AWS and use it safely; the exam follows from that

## Before anything else: two notices

**Your account, your responsibility.** This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Trademarks.** Automate the Cloud is not affiliated with, endorsed by, or sponsored by Amazon Web Services. AWS, Amazon Web Services, and AWS Certified Cloud Practitioner are trademarks of Amazon.com, Inc. or its affiliates. They are used here only to identify the exam this guide prepares you for.

## Who this guide is for

This is Automate the Cloud's study guide for the AWS Certified Cloud Practitioner exam, version **CLF-C02**. **AWS** (Amazon Web Services) rents computing power, storage and many other services over the internet; the exam checks that you understand what AWS offers, what it costs, and who keeps it secure. The guide is for an adult studying alone, possibly new to IT, so it explains every term the first time it appears. No honest guide can promise you a pass, and we don't.

## How the guide is organized

A **module** is built around one realistic task: short lessons, then a **mastery check** (pass at 80%, or reread what it points to and take a second check). Many add a **lab** in your own AWS account, or a **simulation**: a decision exercise on paper, for things that would cost money or carry risk. Before the first lab you set up a safe account with the separate **guardrails primer**.

### The modules, by exam domain

The exam has four **domains** (subject areas), each with a share of the scored questions. The table groups the modules by the domain they mainly teach ([more in The exam at a glance](03-the-exam-at-a-glance.md#what-the-exam-tests-and-where-this-guide-covers-it)); you study them in number order.

| # | Module | Hours |
|---|---|---|
| 00 | Start here | 1 |
| 01 | [On-ramp: IT foundations](../01-on-ramp/00-brief.md) (optional) | 1.5 |
| — | [Guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md) (separate) | 3–4 |
| | **Domain 1: Cloud Concepts, 24% of the exam** | **4.5** |
| 02 | [Why organizations use the cloud](../02-why-the-cloud/00-brief.md) | 2.75 |
| 13 | [Moving to AWS](../13-moving-to-aws/00-brief.md) | 1.75 |
| | **Domain 2: Security and Compliance, 30%** | **5.5** |
| 04 | [Who secures what](../04-shared-responsibility-and-access/00-brief.md) | 2.5 |
| 09 | [Protecting, governing and proving compliance](../09-protecting-and-governing/00-brief.md) | 3 |
| | **Domain 3: Cloud Technology and Services, 34%** | **10.5** |
| 03 | [AWS around the world](../03-aws-around-the-world/00-brief.md) | 1.5 |
| 05 | [Storing data: storage and databases](../05-storing-data/00-brief.md) | 3 |
| 06 | [Running applications: compute](../06-running-applications/00-brief.md) | 2.25 |
| 07 | [Connecting it: networks and the edge](../07-connecting-it/00-brief.md) | 1.25 |
| 08 | [Building and operating](../08-building-and-operating/00-brief.md) | 1.25 |
| 10 | [Data, AI and the rest of the catalog](../10-data-ai-and-more/00-brief.md) | 1.25 |
| | **Domain 4: Billing, Pricing, and Support, 12%** | **4.5** |
| 11 | [Paying for AWS](../11-paying-for-aws/00-brief.md) | 2.5 |
| 12 | [Getting help](../12-getting-help/00-brief.md) | 2 |
| | **All domains** | |
| 14 | [Close-out (optional capstone)](../14-capstone/00-brief.md) | 1, plus 3 optional |
| 90 | [Exam preparation](../90-exam-prep/01-how-to-use-exam-prep.md) | 5 |

### What's on the main path, and what's optional

The exam asks which service or idea fits a situation, not how to build it, so the main path keeps what prepares you for that:

- **Main path:** each module's lessons and mastery check; nine core labs (01, 02, 03, 05, 08, 12, 15, 17 and 19, which closes out your account); and two practice exams with their review.
- **Optional:** ten simulations (about 3.5 hours), three mixed practice sets (about 2.5 hours), Optional labs 04 to 16 (about 6 hours), the capstone review with Optional lab 18 (about 3 hours), and the Beyond the exam pages. Each says so in its title.

## Three paths, one destination

What helps a newcomer slows down someone who already knows it, so there are three paths:

| Path | Who it's for | What changes | Estimated time |
|---|---|---|---|
| **On-ramp** | You are weak on IT basics: servers, networks, data, APIs | Module 01 first; pass a lesson's test-out to skip it | About 33.5 hours, or 7–8 weeks |
| **Standard** (the main path) | Most learners | Modules 02 to 14 in order, then exam preparation | About 32 hours, or about 7 weeks |
| **Fast** | You already work in IT or with AWS | Take each module's mastery check first; pass it and skip the lessons, but still do the core labs and exam preparation | About 16 hours, or about 4 weeks, plus lessons for any check you don't pass |

**How the hours add up.** A module's hours are the times its pages state for its lessons, core labs (with next-day checks) and one mastery check, rounded to the quarter hour. The main path is Start here, 1; modules 02 to 13, 25; Lab 19, 1; and exam preparation, 5 (two 90-minute practice exams and their review). The fast path counts Start here, one check per module (about 4 hours), the core labs (about 6.25) and exam preparation. Hours leave out optional pages and the primer; weeks include the primer, at 5 hours a week. All are estimates until we test the guide with learners.

![Horizontal bar chart of estimated study hours before the guardrails primer: fast path about 16, standard path about 32, on-ramp path about 33.5.](../../images/00-01-path-hours.svg)

*Notice that the on-ramp adds only an hour and a half, while the fast path halves the time. The table above has the same data.*

**Choosing your path.** The [diagnostic](06-diagnostic.md) at the end of this module (about 20 minutes) points you to one. Without it: if you couldn't explain what a server, an IP address and a database are, start with the on-ramp; if you work with IT or AWS every week, try the fast path. You can switch at any time.

> **Your turn:** Write down which path you'll start on, and one sentence on why. Look at it again after your first module.

## What you need

- **Time and a device:** about 5 hours a week, and a laptop or desktop for the labs. Reading works on a phone.
- **For the labs, an AWS account of your own,** opened when you reach the primer, not before, because AWS's **Free plan** lasts up to 6 months. You need an email address and a payment card. On the Free plan you expect to pay $0: usage comes out of free credits ($100, plus up to $100 more for short activities), and the plan can't bill you unless you upgrade (as of 2026-10-23; check [AWS Free Tier](https://aws.amazon.com/free/)).

**Next:** [How to study with this guide](02-how-to-study-with-this-guide.md).

---

"Welcome" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
