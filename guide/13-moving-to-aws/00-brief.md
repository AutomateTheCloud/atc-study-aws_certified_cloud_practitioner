---
type: brief
id: clf-13-00
title: "Module 13: Moving to AWS"
tasks: ["1.3", "1.4"]
objectives: ["13.01a", "13.02a", "13.03a", "13.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 12; about 2 hours in total"
prerequisites: [clf-12-00, clf-11-00, clf-04-00, clf-02-00]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
---

# Module 13: Build the case for moving a bakery chain's ten applications to AWS

This module teaches how an organization decides to move to the cloud, how it moves each application, and what it costs.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely, and who has finished Modules 02 to 12. **Time:** about 2 hours; no AWS account needed.

## The scenario: a chain buys the bakery

A larger bakery chain has bought the bakery, whose site runs on AWS. **The chain** runs its own systems in a rented data center whose lease ends in 18 months, and its board asks: **should we move too, and how?** Its ten applications (made up):

| # | Application | What you know about it |
|---|---|---|
| 1 | Recipe archive | No sign-ins for a year; unsupported operating system; recipes must be kept |
| 2 | Oven control | Talks directly to the ovens' controllers |
| 3 | Accounting | New servers and license eight months ago |
| 4 | Email and calendars | Its mail servers take two staff much of their week |
| 5 | Payroll | A vendor's package; the vendor now sells it as a service |
| 6 | Stock and ordering | Custom, on Linux; works well; no time to change it |
| 7 | Loyalty database | SQL Server; days each month go on patches and backups |
| 8 | Shop tools | About 30 small apps on VMware; the team knows VMware well |
| 9 | Wholesale portal | One large program; monthly releases; the business wants five times the café customers |
| 10 | Chain website | Two servers that slow every December; the bakery's AWS site does a similar job |

## You'll be able to

| Objective | Lesson |
|---|---|
| **13.01a** Map a concern to an AWS Cloud Adoption Framework perspective | 13.01 |
| **13.02a** Assign and justify a migration strategy | 13.02 |
| **13.03a** Choose a migration tool for a job | 13.03 |
| **13.04a** Build a cost comparison and make a licensing decision | 13.04 |

## What this covers on the exam

Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3), the AWS CAF and migration strategies, and task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4), cloud economics: on-premises costs, licensing and rightsizing. Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons**, about 20 minutes each:

1. [The Cloud Adoption Framework](01-the-cloud-adoption-framework.md)
2. [Seven migration strategies](02-seven-migration-strategies.md)
3. [Migration tools](03-migration-tools.md)
4. [The business case](04-the-business-case.md)

**Practice:** [Simulation S16: the portfolio sorter](05-sim-portfolio-sorter.md), on paper. There's no lab: the migration services bill while they run, and two planning tools are closed to new customers.

> **Dated (checked 2026-10-24):** the exam's AWS Application Migration Service is now AWS Transform MGN, and AWS Application Discovery Service and AWS Migration Hub closed to new customers on 2025-11-07.

**Mastery check:** [the module check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md), with the AWS pages to read.

---

"Module 13: Moving to AWS" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
