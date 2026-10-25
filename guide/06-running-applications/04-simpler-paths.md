---
type: lesson
id: clf-06-04
title: "Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts"
tasks: ["3.3", "3.1", "2.1"]
objectives: ["06.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 05, the guardrails primer and lessons 06.01 to 06.03; about 15 minutes; works on a phone"
prerequisites: [clf-06-01, clf-06-02, clf-06-03, clf-03-04, clf-05-05]
terms_introduced: [AWS Elastic Beanstalk, Amazon Lightsail, AWS Batch, job queue, AWS Outposts]
pillars: [operational-excellence, cost-optimization, performance-efficiency, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html"
  - "https://aws.amazon.com/elasticbeanstalk/faqs/"
  - "https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html"
  - "https://aws.amazon.com/lightsail/faq/"
  - "https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html"
  - "https://aws.amazon.com/batch/faqs/"
  - "https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"
  - "https://aws.amazon.com/outposts/rack/faqs/"
---

# Beanstalk assembles the setup for your code, Lightsail bundles a server, Batch runs job queues, and Outposts brings AWS on site

Lessons 06.01 to 06.03 had you assemble compute from parts. Four more services do the assembling, or the housing, for you, and the exam asks you to match a need to the right one.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on lessons [06.01](01-ec2.md) to [06.03](03-containers-and-serverless.md) and on [The edge](../03-aws-around-the-world/04-the-edge.md), where Outposts first appeared.

## Warm-up: what you remember

1. From lesson 05.05: when the bakery moves its database from an EC2 server to Amazon RDS, name two chores that disappear.

<details><summary>Feedback</summary>

1. **Operating system and database patches, and running backups.** This lesson applies the same idea to whole applications.

</details>

## What you'll learn

By the end, you can match Elastic Beanstalk, Lightsail, Batch and Outposts to their uses (objective 06.04a), and tell EC2, Elastic Beanstalk and Lightsail apart for a web application.

Guess before you read on: the owner's sister wants a WordPress site for her flower shop with a bill she can predict. Which service fits?

## The big picture: four services that assemble or house compute for you

![Four cards for AWS Elastic Beanstalk, Amazon Lightsail, AWS Batch and AWS Outposts, each showing what you bring, what AWS sets up, what you pay and when to pick it.](../../images/06-04-four-paths.svg)

*Notice the "You pay" rows. Beanstalk and Batch cost nothing themselves; you pay for the resources they create. Lightsail is the only one sold as a fixed monthly price.*

**Long description.** Each card: you bring; AWS sets up; you pay; pick it when. Elastic Beanstalk: your code; EC2 or EKS, load balancing, scaling and health monitoring in your account; nothing extra beyond those resources; to deploy code without building the setup. Lightsail: a small site, often from an image such as WordPress; a server, storage, static IP and data transfer as one bundle; a fixed monthly plan, charged hourly up to that price; for something simple and predictable. Batch: many container jobs; a queue and compute that is removed when they finish; nothing extra beyond the EC2 or Fargate capacity; for lots of jobs, often too long for Lambda. Outposts: a site with space, power and a network link to a Region; AWS hardware that AWS maintains; a term of years; when work or data must stay in your building. A note: the servers under Beanstalk, Batch and Lightsail still exist; you just don't assemble them.

## Elastic Beanstalk builds and runs the setup for your code

With **AWS Elastic Beanstalk**, you upload your application's code and Beanstalk creates what it needs to run: EC2 instances (or an EKS cluster), load balancing, Auto Scaling and health monitoring ([What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html), checked 2026-10-23). AWS's product page calls it Platform as a Service. There's no extra charge: you pay for the resources it creates. AWS says developers keep full control of those resources ([Elastic Beanstalk FAQs](https://aws.amazon.com/elasticbeanstalk/faqs/)), so you can still choose the instance type and run in more than one Availability Zone.

Beanstalk isn't serverless. It feels that way because you only upload code, but the instances are real, sit in your account and bill while they run.

## Lightsail sells a simple server as a bundle with a predictable price

**Amazon Lightsail** is AWS's simplest way to get a website or small application online. Its plans bundle a virtual server, SSD storage, a static IP address and a data transfer allowance into one monthly price, and you can start from ready-made images such as WordPress ([Amazon Lightsail FAQs](https://aws.amazon.com/lightsail/faq/); [What is Amazon Lightsail?](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html), checked 2026-10-23). AWS recommends EC2 for steady high CPU work. Plans are charged by the hour, up to the plan's monthly price, while the instance is running **or stopped**; only deleting it ends the charge. When you outgrow it, Upgrade to EC2 copies an instance into EC2.

## EC2, Elastic Beanstalk or Lightsail: three ways to run a web app

All three can run the same website, so the exam likes to set them side by side. The servers underneath are similar; what differs is who assembles the setup and how you pay.

| | Amazon EC2 | AWS Elastic Beanstalk | Amazon Lightsail |
|---|---|---|---|
| **You bring** | Everything: instances, scaling, load balancing | Your code | A website, often from a ready-made image |
| **Who builds the setup** | You | Beanstalk, in your account | Lightsail, as a bundle |
| **Price** | Each part, by use | No extra charge; the parts it creates | Fixed monthly plan |
| **Pick it when** | You need full control or special hardware | You want to deploy code and skip the assembly | You want simple and predictable |

## Batch runs large numbers of jobs from a queue

**AWS Batch** runs batch computing work at any scale. You package each job as a container and submit it to a **job queue**. Batch decides where to run each job, launches compute when it's needed, and removes it when it's no longer needed ([What is AWS Batch?](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html); [AWS Batch FAQs](https://aws.amazon.com/batch/faqs/), checked 2026-10-23). There's no additional charge; you pay for the EC2 or Fargate capacity the jobs use, and Spot Instances suit jobs that can be retried. Lambda runs short, event-triggered functions of up to 15 minutes; Batch runs queued jobs of any length.

## Outposts brings AWS hardware into your own building

Lesson [03.04](../03-aws-around-the-world/04-the-edge.md) placed **AWS Outposts** on the map: AWS racks or servers in your own data center or site. They run services such as EC2, EBS, ECS, RDS and S3 on Outposts, with the same APIs, console and tools as in the Region ([What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html), checked 2026-10-23). Use it for low latency to systems on site, local data processing, and data that must stay on premises. It's AWS's way to build a **hybrid deployment** (task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1)), sold for a term of years.

It moves the line of responsibility: AWS maintains and patches the Outpost, while you provide the space, power and network, and physical security around it ([Outposts racks FAQs](https://aws.amazon.com/outposts/rack/faqs/)).

> **Your turn:** Match each request to Outposts, Batch, Lightsail, Elastic Beanstalk or EC2 with Auto Scaling and a load balancer.
>
> a) The nephew's test copy of the site, updated by uploading code\
> b) The sister's WordPress site with a predictable bill\
> c) The flour supplier's 2,000 nightly price models, about an hour each\
> d) The supplier's mill, whose control systems need millisecond responses on site\
> e) The bakery's spiky order site, which needs exact control of instance types and scaling rules

<details><summary>Model answer</summary>

a) **Elastic Beanstalk:** upload code and AWS assembles the setup. b) **Lightsail:** a simple site at a fixed price. c) **Batch:** a queue of unattended jobs, each far past Lambda's 15 minutes. d) **Outposts:** it must run in the mill's own building. e) **EC2 with Auto Scaling and a load balancer**, as in lesson 06.02.

</details>

## Summary

- **Elastic Beanstalk builds and runs the setup for your code** in your account, at no extra charge. It isn't serverless.
- **Lightsail sells a simple server as a bundle with a predictable price,** billed while the instance exists, even when stopped.
- **EC2, Beanstalk and Lightsail differ in who assembles the setup and how you pay,** not in the servers underneath.
- **Batch runs large numbers of jobs from a queue,** launching compute for them and removing it afterwards.
- **Outposts brings AWS hardware into your own building;** AWS maintains it, and you secure the site.

## Practice

1. **Which AWS service lets a developer upload application code and have AWS provision the EC2 instances, load balancing, scaling and health monitoring?**

   A. Amazon Lightsail\
   B. AWS Elastic Beanstalk\
   C. AWS Batch\
   D. AWS Outposts

   <details><summary>Feedback</summary>

   **B is right.** That is Elastic Beanstalk's job, at no extra charge beyond the resources.

   - **A is wrong.** Lightsail sells bundled servers at a fixed price.
   - **C is wrong.** Batch runs queued jobs, not web applications.
   - **D is wrong.** Outposts puts AWS hardware on your premises.

   </details>

2. **Which statement about AWS Batch is correct?**

   A. Batch charges a fee per job on top of the compute used\
   B. Batch runs each job for at most 15 minutes\
   C. Batch launches compute for queued jobs and removes it when it's no longer needed\
   D. Batch requires you to install scheduling software on EC2

   <details><summary>Feedback</summary>

   **C is right.** Batch provisions compute in response to jobs and removes it afterwards.

   - **A is wrong.** Batch has no additional charge.
   - **B is wrong.** That's Lambda's limit per invocation.
   - **D is wrong.** Batch is fully managed.

   </details>

3. **A hospital's imaging systems need answers within milliseconds, and its patient data must stay in its own building. It wants to run EC2 instances with the same tools it uses in the AWS Region. Which service fits?**

   A. AWS Outposts\
   B. Amazon Lightsail\
   C. A Local Zone in the nearest city\
   D. AWS Batch

   <details><summary>Feedback</summary>

   **A is right.** Outposts puts AWS-managed hardware inside the hospital, with the same APIs and tools.

   - **B and D are wrong.** Lightsail and Batch run in AWS Regions.
   - **C is wrong.** A Local Zone is AWS's site in a city, not the hospital's building (lesson 03.04).

   </details>

**Next:** [Lab 08: launch and terminate an instance](06-lab-08-launch-and-terminate-an-instance.md), then the [mastery check](08-check.md).

## Where to check the current details

- [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) (checked 2026-10-23)
- [Amazon Lightsail FAQs](https://aws.amazon.com/lightsail/faq/) (checked 2026-10-23)
- [What is AWS Batch?](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) and [What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) (checked 2026-10-23)

---

"Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
