---
type: brief
id: clf-07-00
title: "Module 07: Connecting it: networks and the edge"
tasks: ["3.5", "3.2", "4.1", "2.1", "2.4"]
objectives: ["07.01a", "07.02a", "07.03a", "07.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 06 and the guardrails primer; about 1 hour 15 minutes in total"
prerequisites: [clf-06-00, clf-05-00, clf-03-00, guardrails-00]
pillars: [security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 07: Give the bakery's site a network: private where it must be, fast near customers, and linked to head office

This module teaches what each piece of an AWS network is for: your own network and its filters, the services at the edge near customers, and the links to your offices and other networks. The exam asks which piece fits a need, not how to build it.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2) and [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. You have done Modules 02 to 06 and the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md). **Time:** about 1 hour 15 minutes, plus 50 minutes for the optional lab.

## The scenario

The bakery's site runs in US East (N. Virginia): web servers on EC2, the order database on Amazon RDS, functions in AWS Lambda, cake photos in S3. So far it lives in the default VPC, where every subnet is public. The owner has four requests (made-up details):

| The owner's request | Answered in |
|---|---|
| "Customers reach the website; nobody on the internet reaches the order database." | 07.01 |
| "Someone keeps hammering our order page from one block of addresses. Block them." | 07.02 |
| "Customers far away say the cake photos load slowly." | 07.03 |
| "Our head office needs a secure link to the systems on AWS." | 07.04 |

## You'll be able to

| Objective | Lesson |
|---|---|
| **07.01a** Explain what makes a subnet public | 07.01 |
| **07.02a** Predict whether traffic passes a security group and a network ACL | 07.02 |
| **07.03a** Choose Route 53, CloudFront, Global Accelerator or API Gateway for a need | 07.03 |
| **07.04a** Choose a link by whether it's private, encrypted and quick to set up | 07.04 |

## What this covers on the exam

Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5), network services, in every lesson. It also touches task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2) (edge locations), [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) (data transfer costs), [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) (shared responsibility) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4) (Shield and WAF at the edge). Exam guide checked 2026-10-24.

## How the module is laid out

**Lessons** (about 15 minutes each):

1. [Your own network](01-your-own-network.md)
2. [Filtering traffic](02-filtering-traffic.md)
3. [Names and the edge](03-names-and-the-edge.md)
4. [Connecting networks and offices](04-connecting-networks-and-offices.md)

**Practice:** [Optional lab 09: build a small VPC](05-lab-09-build-a-small-vpc.md), after lesson 07.02, if you want to see a VPC for yourself; the exam doesn't need it. It creates no NAT gateway and no public IPv4 address, so it costs $0. Before it, check that you still have [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md), [your IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md) and [money alarms](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md). The lessons need no AWS account.

**Mastery check:** the module ends with [a mastery check](07-check.md); you pass at 80%. **Beyond the exam:** [what this module left out](08-beyond-the-exam.md), such as address planning and packet tracing, with the AWS pages to read.

**Numbers that change:** NAT gateway, public IPv4 address and data transfer prices appear with the date they were checked.

---

"Module 07: Connecting it: networks and the edge" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
