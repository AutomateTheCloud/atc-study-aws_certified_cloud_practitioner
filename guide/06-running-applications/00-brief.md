---
type: brief
id: clf-06-00
title: "Module 06: Running applications: compute"
tasks: ["3.3", "1.1", "2.1", "3.1"]
objectives: ["06.01a", "06.02a", "06.03a", "06.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 05 and the guardrails primer; about 2.5 hours in total"
prerequisites: [clf-05-00, clf-04-00, clf-02-00, guardrails-00]
pillars: [performance-efficiency, reliability, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 06: Choose where each of the bakery's programs runs, how it grows, and who patches it

This module teaches the ways AWS runs your code: virtual servers, containers and functions. The exam asks which compute option fits a need, and so do you.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1) and [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have finished Modules [02](../02-why-the-cloud/00-brief.md) to [05](../05-storing-data/00-brief.md) and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 2.5 hours, plus 30 minutes for the optional lab.

## The scenario

The owner asks where the bakery's programs should run (made-up details).

| Program | What its load looks like | Placed in |
|---|---|---|
| **The order site** | Quiet at night, a lunch rush every day, six times busier in December | 06.01, 06.02 |
| **The photo resize** | Seconds of work per new cake photo | 06.03 |
| **The inventory app** | Runs all day; it came from its supplier as a container image | 06.03 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **06.01a** Choose an EC2 instance family from a workload's bottleneck | 06.01 |
| **06.02a** Explain how Auto Scaling and load balancers together give elasticity and high availability | 06.02 |
| **06.03a** Pick EC2, Fargate or Lambda for a workload, and say what you manage on each | 06.03 |
| **06.04a** Match Elastic Beanstalk, Lightsail, Batch and Outposts to their uses | 06.04 |

## What this covers on the exam

Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3), compute services, in every lesson. Lesson 06.02 adds the elasticity and high availability of task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1); each lesson says who manages what, task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); and lesson 06.04 places Outposts in hybrid deployments, task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (15 to 20 minutes each):

1. [Amazon EC2](01-ec2.md)
2. [Auto Scaling and load balancers](02-auto-scaling-and-load-balancers.md)
3. [Containers and serverless](03-containers-and-serverless.md)
4. [Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts](04-simpler-paths.md)

**Practice:**

- [Lab 08: launch and terminate an instance](06-lab-08-launch-and-terminate-an-instance.md), after lesson 06.01 or at the end of the module, in your own account. It's time-boxed to 30 minutes, because a server bills by the hour, and costs under 2 cents of Free plan credits.
- [Simulation S7: elasticity with Auto Scaling](07-sim-elasticity-with-auto-scaling.md), after lesson 06.02, on paper, because a load balancer bills by the hour.
- [Optional lab 07: a Lambda function](05-lab-07-a-lambda-function.md), if you want to run a function yourself; the exam doesn't need it.

**Before the labs:** check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md), [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md) and the [EC2 safe defaults](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md) in `us-east-1`. The lessons need no AWS account.

**Mastery check:** the module ends with [a mastery check](08-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](09-beyond-the-exam.md), with the AWS pages to read.

---

"Module 06: Running applications: compute" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
