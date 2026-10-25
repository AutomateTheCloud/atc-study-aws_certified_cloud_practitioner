---
type: brief
id: clf-10-00
title: "Module 10: Data, AI and the rest of the catalog"
tasks: ["3.7", "3.8"]
objectives: ["10.01a", "10.02a", "10.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 09 and the guardrails primer; about 1 hour 15 minutes in total"
prerequisites: [clf-09-00, clf-08-00, clf-07-00, clf-05-00, guardrails-00]
pillars: [performance-efficiency, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 10: Match six of the bakery owner's requests to the AWS service built for each

The rest of the exam's catalog: analytics, AI and machine learning, desktops and apps for people, and connected devices. The exam asks which service fits a need, so learn each one's job and the look-alike it's confused with.

**Exam guide:** [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7) and [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished Modules 02 to 09 and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 1 hour 15 minutes, plus 20 minutes for the optional simulation and the time for the optional labs.

## The scenario: six requests from the owner

The growing bakery brings six requests (made-up details):

| # | The owner wants | Lesson |
|---|---|---|
| 1 | A morning dashboard of sales, and of which cake pages people view before they order | 10.01 |
| 2 | A bot that answers the phone and takes simple orders | 10.02, 10.03 |
| 3 | Each cake's description read aloud on the website | 10.02 |
| 4 | Suppliers' paper receipts turned into searchable text | 10.02 |
| 5 | Work desktops for December's temporary staff, reached from their own laptops | 10.03 |
| 6 | Freezer temperature readings collected, with a warning before the dough thaws | 10.03 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **10.01a** Place each analytics service on its job: ingest, catalog, query, search or visualize | 10.01 |
| **10.02a** Choose an AI service by what goes in and what must come out | 10.02 |
| **10.03a** Match a need from staff, customers, app users or devices to its service | 10.03 |

## What this covers on the exam

Task [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7), AI/ML and analytics, and the end-user computing, business application, front-end and IoT parts of task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8); Modules 08 and 12 cover the rest of 3.8. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (about 20 minutes each):

1. [Analytics in five verbs](01-analytics-in-five-verbs.md)
2. [AI and machine learning](02-ai-and-ml.md)
3. [People, apps and devices](03-people-apps-and-devices.md)

**Practice:**

- [Optional simulation S12: the input and output matcher](06-sim-input-output-matcher.md), after lesson 10.03, on paper, if you want more decisions to make; the main path doesn't need it.
- Two optional labs, which the exam doesn't need: [Optional lab 13: query a sales file with Athena](04-lab-13-athena-query.md), after lesson 10.01, and [Optional lab 14: have Polly read a description aloud](05-lab-14-polly-text-to-speech.md), after lesson 10.02.

**Before a lab:** check you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md). The lessons need no AWS account.

**Mastery check:** [the module's mastery check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md).

> **Dated (checked 2026-10-24):** names move fast here, and questions may use old or new ones: QuickSight is now Quick Sight, Kinesis Data Firehose is Amazon Data Firehose, AppStream 2.0 is WorkSpaces Applications, and Amazon Connect is Connect Customer. Amazon Q Business and Amazon Kendra are closed to new customers, and WorkSpaces Secure Browser closes to them on 2026-10-29.

---

"Module 10: Data, AI and the rest of the catalog" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
