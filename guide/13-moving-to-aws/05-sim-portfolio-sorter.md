---
type: sim
id: clf-13-05
title: "Simulation S16: Sort the chain's ten applications into the 7 Rs"
tasks: ["1.3", "1.4"]
objectives: ["13.02a", "13.01a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 13.01 to 13.04; about 20 minutes"
prerequisites: ["clf-13-01", "clf-13-02", "clf-13-03", "clf-13-04"]
terms_introduced: []
pillars: [cost-optimization, operational-excellence]
lab: "S16"
rung: L2-L3
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "20 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html"
  - "https://aws.amazon.com/migration-evaluator/"
  - "https://aws.amazon.com/tco-calculator/"
  - "https://aws.amazon.com/snowball/"
  - "https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html"
---

# Simulation S16: Choose a migration strategy for each of the chain's ten applications, and name who worries about what

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read lessons [13.01](01-the-cloud-adoption-framework.md) to [13.04](04-the-business-case.md). **Time:** about 20 minutes. **Cost:** $0; no AWS account is used.

**Goal:** give each of the chain's ten applications one of the 7 Rs, match managers' worries to perspectives of the AWS Cloud Adoption Framework (AWS CAF), and spot the out-of-date claims in a consultant's slide.

## The chain's portfolio

The ten applications from the [module brief](00-brief.md), made up for teaching. The data center lease ends in 18 months.

| # | Application | What you know about it |
|---|---|---|
| 1 | **Recipe archive** | No sign-ins for over a year; operating system out of support; old recipes must be kept |
| 2 | **Oven control** | Talks directly to the controllers on the central bakery's ovens |
| 3 | **Accounting** | New servers and license eight months ago |
| 4 | **Email and calendars** | Its own mail servers take two staff much of their week |
| 5 | **Payroll** | A vendor's package; the vendor now sells it as a service |
| 6 | **Stock and ordering** | Custom, on Linux servers; works well; no time to change it before the lease ends |
| 7 | **Loyalty database** | Microsoft SQL Server; days each month go on patches and backups |
| 8 | **Shop tools** | About 30 small internal apps on a VMware cluster; the team knows VMware well |
| 9 | **Wholesale portal** | One large program; each release takes a month; the business wants five times the café customers |
| 10 | **Chain website** | Two servers that slow down every December; the bakery's AWS site does much the same job |

## Decision 1: a strategy for each application

**Worked example, the recipe archive.** No sign-ins for a year is well past the 90 days without connections that AWS treats as a sign to retire, and its operating system gets no security updates. The recipes have value; the application doesn't. So **retire** it: export the recipes to an archive storage class (Module 05), then shut the servers down.

Now give each of the other nine a strategy and a one-line reason. Use the question order from [lesson 13.02](02-seven-migration-strategies.md#rehost-relocate-replatform-refactor-side-by-side): no business value, retire; a reason to stay, retain; a product exists, repurchase; demand the design blocks, refactor; a small change pays off, replatform; a whole platform moves, relocate; otherwise, rehost.

<details><summary>Model answer</summary>

![The ten applications placed under the seven strategies, from no move on the left to the most change on the right.](../../images/13-05-strategy-map.svg)

*Notice that three applications don't move at all, and only one is redesigned.*

**Long description.** Seven columns in three groups. Doesn't move to AWS: Retire (recipe archive), Retain (oven control, accounting). Moves as it is: Rehost (stock and ordering), Relocate (shop tools). Changes on the way: Replatform (loyalty database, chain website), Repurchase (email and calendars, payroll), Refactor (wholesale portal, rehosted first).

| # | Application | Strategy | Why |
|---|---|---|---|
| 2 | Oven control | **Retain** | It depends on hardware with no cloud equivalent. |
| 3 | Accounting | **Retain** | It was just upgraded; move it at its next refresh. |
| 4 | Email and calendars | **Repurchase** | A subscription service ends the mail-server work. |
| 5 | Payroll | **Repurchase** | The vendor's service replaces the package; only the data moves. |
| 6 | Stock and ordering | **Rehost** | It works, and there's no time to change it. AWS Application Migration Service (now AWS Transform MGN) copies the servers to EC2. |
| 7 | Loyalty database | **Replatform** | SQL Server to Amazon RDS for SQL Server ends the patching; AWS DMS copies the data while the old database runs (database replication). |
| 8 | Shop tools | **Relocate** | All 30 apps move at once to a VMware-based service on AWS, and the team keeps its tools. |
| 9 | Wholesale portal | **Refactor**, probably after a rehost | Strong demand to scale and release faster; with the deadline, move it first and refactor on AWS. |
| 10 | Chain website | **Replatform** | The bakery's pattern: a managed database, and servers that scale out for December. **Retire** is also fair if the board folds it into the bakery's site. |

Rehost isn't "wrong but quick", and refactor isn't "best": AWS calls it the most complex and costly strategy.

</details>

## Decision 2: who worries about what

During the Align phase, managers raise these concerns. Match each to Business, People, Governance, Platform, Security or Operations.

| | Who | Concern |
|---|---|---|
| a | Finance director | "How will we know the move paid off, and who watches the monthly bill?" |
| b | Office manager | "Staff have used the old email for years. Who trains them on the new service?" |
| c | Chief executive | "Which of these projects helps us win five times the café customers?" |
| d | Security lead | "The loyalty database holds customers' contact details. Who can read it, and is it encrypted?" |
| e | Operations lead | "When the overnight ordering run fails at 2 a.m., who gets the alert?" |
| f | Lead architect | "How do we build every new environment the same way each time?" |
| g | Program manager | "Eighteen months, ten applications. How do we track the schedule and the risks?" |

<details><summary>Model answer</summary>

- **a Governance:** benefits management and cloud financial management.
- **b People:** training staff through change.
- **c Business:** which investments serve the strategy.
- **d Security:** who can reach data, and protecting it.
- **e Operations:** alerts and incident management.
- **f Platform:** architecture and repeatable environments.
- **g Governance:** program management and risk. Note that c and g both mention projects: Business picks which to fund; Governance keeps them on track.

</details>

## Decision 3: find the five errors in a consultant's slide

> "The six Rs are rehost, replatform, repurchase, refactor, retire and retain. Our assessment covers the six CAF perspectives: business, process, people, platform, operations and security. We will inventory the servers with AWS Application Discovery Service, prove the savings with the TCO Calculator, and ship the archived files on an AWS Snowball device."

<details><summary>Model answer</summary>

1. **Seven Rs, not six:** **relocate** is missing, and the shop tools need it.
2. **"Process" is a transformation domain, not a perspective.** The missing perspective is **Governance**.
3. **Application Discovery Service** has been closed to new customers since 2025-11-07, like AWS Migration Hub; AWS points to AWS Transform.
4. **The TCO Calculator** address now leads to the AWS Pricing Calculator. Use **Migration Evaluator** for a business case.
5. **Snowball** has been closed to new customers since 2025-11-07, and support ends on 2026-12-31. AWS points new customers to AWS DataSync, or to AWS Data Transfer Terminal or a Partner for physical transfers.

> **Dated (checked 2026-10-24):** closures and names change; check AWS's pages, cited in this page's sources.

</details>

## Recap

Retire what nobody needs, retain what can't move yet, repurchase when a product exists, refactor only for real business demand, replatform when a small change pays off, relocate whole platforms, and rehost the rest. In the CAF, Business chooses what to fund and Governance keeps it on track.

**Next:** [the Module 13 mastery check](07-check.md).

---

"Simulation S16: Sort the chain's ten applications into the 7 Rs" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
