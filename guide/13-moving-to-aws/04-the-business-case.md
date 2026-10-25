---
type: lesson
id: clf-13-04
title: "The business case"
tasks: ["1.4", "1.3"]
objectives: ["13.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 12 and lessons 13.01 to 13.03; about 20 minutes; works on a phone"
prerequisites: [clf-13-03, clf-02-04]
terms_introduced: [business case, one-time migration cost, license-included, bring your own license, AWS Compute Optimizer]
pillars: [cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/economics/"
  - "https://aws.amazon.com/migration-evaluator/faqs/"
  - "https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html"
  - "https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html"
  - "https://aws.amazon.com/windows/resources/licensing/"
  - "https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
---

# A business case weighs the whole cost of staying against the whole cost of moving, and rightsizing and licensing often decide it

A **business case** compares every cost of staying, every cost of moving (including the move itself) and the value money doesn't capture. The exam asks about the ideas behind it: on-premises costs, fixed and variable costs, rightsizing, and the difference between license-included and bring-your-own-license.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): tasks [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3) and [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [What a data center really costs](../02-why-the-cloud/04-what-a-data-center-really-costs.md) (lesson 02.04) and on Migration Evaluator from [lesson 13.03](03-migration-tools.md).

## Warm-up: what you remember

1. From Module 12, "Getting help": AWS Trusted Advisor has a cost optimization category. What kind of thing do its checks point out?

<details><summary>Feedback</summary>

1. **Resources you pay for but barely use**, such as underused instances, and other ways to cut waste. This lesson adds a tool that goes deeper on size: Compute Optimizer.

</details>

## What you'll learn

By the end of this lesson, you can build a cost comparison between staying on-premises and moving to AWS, and choose between license-included and bring-your-own-license for a workload (objective 13.04a).

Try this before you read on, and guess if you're unsure: which AWS tool would you use today for a total cost of ownership comparison?

## The big picture: three ways to spend the next three years

A business case compares options, not just "cloud or not". Here are the chain's three, over three years, with made-up numbers for teaching.

![Stacked columns of three-year costs, made-up figures: stay on-premises $930,000; move as it is $1,070,000; move, rightsized and relicensed $750,000. The table below gives every segment.](../../images/13-04-big-picture.svg)

*Notice that moving everything at its current size and licensing costs more than staying. The same move, with servers rightsized and licenses chosen with care, costs the least. The move didn't save the money; the two decisions did.*

| Cost (made-up, three years) | Stay | Move as it is | Move, rightsized and relicensed |
|---|---|---|---|
| Hardware and its refresh | $240,000 | — | — |
| Facilities: space, power, cooling, network | $180,000 | — | — |
| Staff | $300,000 | $210,000 | $210,000 |
| Licenses (from AWS or from vendors) | $210,000 | $260,000 | $140,000 |
| AWS usage: compute, storage, data transfer | — | $450,000 | $250,000 |
| One-time migration costs | — | $150,000 | $150,000 |
| **Total** | **$930,000** | **$1,070,000** | **$750,000** |

## Count every cost on both sides, including the move itself

Lesson 02.04 listed the on-premises costs: hardware and its refresh, space, power, cooling, network, staff and licenses. Most of them are **fixed**: you pay for the capacity whether you use it or not. On AWS most costs become **variable**: you pay for what you use, at prices AWS keeps low through its **economies of scale** (lesson 02.02). Variable doesn't mean smaller, though. The bill falls only if what you run matches what you need.

Three things to check in a table like the one above:

- **The one-time costs are there:** planning, tools, people's time, training, and running both environments during the move. A **one-time migration cost** is money spent once to move, and leaving it out flatters the move.
- **Licenses are their own line,** whether AWS bills them or a vendor does.
- **Staff doesn't drop to zero.** Managed services such as Amazon RDS take over patching and backups, and **automation** (scheduling, Auto Scaling, infrastructure as code) removes repetitive manual work and its mistakes, but people still run, secure and improve what's in AWS.

Money isn't the whole case. AWS's Cloud Economics Center describes cloud value in five dimensions: Cost Savings (TCO), Staff Productivity, Operational Resilience, Business Agility and Sustainability ([Cloud Economics Center](https://aws.amazon.com/economics/), checked 2026-10-24). They line up with the CAF's business outcomes from lesson 13.01.

### "Use the AWS TCO Calculator" is out of date

Older courses send you to the AWS TCO Calculator to compare on-premises and AWS costs. That tool no longer exists: its old address now opens the AWS Pricing Calculator (checked 2026-10-24; we found no retirement notice with a date). Today a migration cost case comes from **Migration Evaluator**, which projects what the servers you run would cost on AWS, and the **AWS Pricing Calculator** (Module 11), which prices an AWS setup you describe; the on-premises side is your finance team's numbers. The mistake is tempting because total cost of ownership (TCO) is still the right idea. The idea lives on; that tool doesn't. That answers the prequestion.

## Rightsize twice: before the move from measured data, and after it with Compute Optimizer

On-premises servers are bought for a guess about the future, so many are far bigger than their work needs. Copy them at the same size and you pay for that guess every hour. **Rightsizing** means matching each resource's type and size to its measured needs, and it isn't only "smaller": a server that runs flat out should get bigger.

Rightsize **before** the move from measured on-premises use (Migration Evaluator does this), and **after** it with **AWS Compute Optimizer**. After you opt in, Compute Optimizer analyzes the CloudWatch metrics of resources such as EC2 instances, Auto Scaling groups, EBS volumes, Lambda functions and RDS databases, and reports each as over-provisioned, under-provisioned, optimized or idle, with better options ([What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html), checked 2026-10-24). It recommends; you make the change, apart from a few EBS volume actions it can apply if you set up its [automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html).

Keep it apart from its neighbors: **Auto Scaling** changes how *many* instances run; **Trusted Advisor** runs broad checks across several categories; **Compute Optimizer** gives metric-based advice on the *size and type* of each resource. And rightsize before you buy a Savings Plan or Reserved Instance: a commitment bought for an oversized server locks the waste in for one or three years.

## License-included or bring your own license: who pays the software vendor

For software such as Windows Server and SQL Server, AWS offers two routes ([Microsoft licensing on AWS](https://aws.amazon.com/windows/resources/licensing/), checked 2026-10-24):

- **License-included:** the hourly price of the EC2 instance or RDS database covers the software license. You pay as you go with no long-term commitment, and AWS handles license compliance.
- **Bring your own license (BYOL):** you use licenses you already own, and AWS charges only for the infrastructure. The license terms decide where and how you may run them; some need extra rights from the vendor, such as Microsoft's Software Assurance, and some can run only on Dedicated Hosts. **Compliance is yours:** AWS's licensing page says you're responsible for following your license terms. **AWS License Manager** helps you track the licenses you bring and can stop a launch that would take you over what you own ([What is AWS License Manager?](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)).

How much of a license-included price is the license? For SQL Server, most of it:

![Stacked bars for one hour of an m7i.xlarge instance: Linux $0.2016; Windows Server $0.3856; Windows with SQL Server Standard $0.8656; Windows with SQL Server Enterprise $1.8856. The table below gives each part.](../../images/13-04-license-share.svg)

*Notice the last bar: on license-included SQL Server Enterprise, nearly 90 cents of every dollar pays for software licenses.*

| m7i.xlarge, per hour | Instance | Windows license | SQL Server license | Total |
|---|---|---|---|---|
| Linux | $0.2016 | — | — | $0.2016 |
| Windows Server, license-included | $0.2016 | $0.1840 | — | $0.3856 |
| Windows + SQL Server Standard, license-included | $0.2016 | $0.1840 | $0.4800 | $0.8656 |
| Windows + SQL Server Enterprise, license-included | $0.2016 | $0.1840 | $1.5000 | $1.8856 |

> **Dated (checked 2026-10-24):** On-Demand prices for US East (N. Virginia), from AWS's EC2 price list published 2026-10-23, compute and licenses only. Check [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) for today's figures.

BYOL isn't always cheaper. It saves money when you own eligible licenses that you'd be paying for anyway and can use fully. License-included usually wins for small, short-lived or changing workloads, or when your licenses aren't eligible.

> **Your turn:** Decide each case. (a) A web server peaks at 18% CPU over a month. (b) The overnight ordering batch runs its server at 97% CPU every night, and the shops wait for it. (c) A four-month project needs SQL Server; the company's licenses would need a Software Assurance renewal paid only for this project.

<details><summary>Model answer</summary>

(a) **Downsize** it: it uses a fraction of what it pays for. (b) **Upsize** it: rightsizing means the right size, and a struggling server costs the business more than a bigger instance. (c) **License-included:** pay by the hour and stop when the project ends; renewing Software Assurance for four months of use adds a cost, and BYOL would make compliance the company's job.

</details>

## Summary

- **Count every cost on both sides:** hardware, facilities, staff and licenses for staying; AWS usage, licenses, staff and one-time migration costs for moving. Add the value beyond cost.
- **Fixed becomes variable,** at prices lowered by AWS's economies of scale; managed services and automation cut the staff work.
- **There is no TCO Calculator.** Use Migration Evaluator for a migration cost case, and the AWS Pricing Calculator to estimate an AWS setup.
- **Rightsize twice,** before the move from measured use and after it with AWS Compute Optimizer, and before you commit to a discount.
- **License-included** is pay-as-you-go with compliance handled by AWS; **BYOL** reuses licenses you own, within their terms, and makes compliance yours.

## Practice

1. **A company asks for the AWS tool that builds a data-driven business case for migrating its on-premises servers, including license options. What do you recommend?**

   A. The AWS TCO Calculator\
   B. Migration Evaluator\
   C. AWS Compute Optimizer\
   D. AWS License Manager

   <details><summary>Feedback</summary>

   **B is right.** It starts from data about the servers you run and projects their AWS cost, including bringing your own licenses.

   - **A is wrong.** It no longer exists; its address opens the AWS Pricing Calculator.
   - **C is wrong.** Compute Optimizer analyzes resources already running in AWS.
   - **D is wrong.** License Manager tracks licenses; it doesn't price a migration.

   </details>

2. **Which statement about license-included instances is correct?**

   A. You must own the licenses before you launch them\
   B. They always need a Dedicated Host\
   C. The hourly price covers the software license, and AWS handles license compliance\
   D. They cost the same per hour as Linux instances

   <details><summary>Feedback</summary>

   **C is right.**

   - **A is wrong.** That describes bringing your own license.
   - **B is wrong.** They run on ordinary shared instances.
   - **D is wrong.** The license adds to the hourly price.

   </details>

3. **Six weeks after a move, a company wants to know which of its EC2 instances are bigger than their work needs. What should it use?**

   A. EC2 Auto Scaling\
   B. AWS Compute Optimizer, after opting in\
   C. AWS License Manager\
   D. AWS Cost Explorer's forecast

   <details><summary>Feedback</summary>

   **B is right.** It reads the instances' metrics and reports which are over-provisioned, with a suggested size.

   - **A is wrong.** Auto Scaling changes the number of instances, not their size.
   - **C is wrong.** License Manager tracks licenses, not instance sizes.
   - **D is wrong.** A forecast projects spend; it doesn't judge each instance's size.

   </details>

**Next:** [Simulation S16: the portfolio sorter](05-sim-portfolio-sorter.md), then the [Module 13 mastery check](07-check.md).

## Where to check the current details

- [Cloud Economics Center](https://aws.amazon.com/economics/) (checked 2026-10-24)
- [What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) (checked 2026-10-24)
- [Microsoft licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) (checked 2026-10-24)

---

"The business case" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
