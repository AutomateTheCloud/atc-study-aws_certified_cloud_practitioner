---
type: lesson
id: clf-06-02
title: "Auto Scaling and load balancers"
tasks: ["3.3", "1.1", "2.1"]
objectives: ["06.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 05, the guardrails primer and lesson 06.01; about 20 minutes; works on a phone"
prerequisites: [clf-06-01, clf-05-05, clf-03-01, clf-02-03]
terms_introduced: [Amazon EC2 Auto Scaling, Auto Scaling group, launch template, minimum capacity, maximum capacity, desired capacity, scaling policy, target tracking, scheduled scaling, predictive scaling, health check, Elastic Load Balancing, load balancer, target, Application Load Balancer, Network Load Balancer, Gateway Load Balancer, Classic Load Balancer, AWS Auto Scaling]
pillars: [reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html"
  - "https://aws.amazon.com/ec2/autoscaling/faqs/"
  - "https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html"
  - "https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html"
  - "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html"
  - "https://aws.amazon.com/elasticloadbalancing/features/"
  - "https://aws.amazon.com/elasticloadbalancing/pricing/"
---

# Auto Scaling decides how many servers run; a load balancer decides which one gets each request

Amazon EC2 Auto Scaling changes the number of instances to follow demand: elasticity. A load balancer gives customers one address and sends each request to a healthy instance; with instances in several Availability Zones, that gives high availability.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** read [Amazon EC2](01-ec2.md) first. This lesson also builds on [Telling the benefits apart](../02-why-the-cloud/03-telling-the-benefits-apart.md) (elasticity) and [Regions, Availability Zones and data centers](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md) (high availability).

## Warm-up: what you remember

1. What is the smallest number of Availability Zones a highly available web tier needs, and why?

<details><summary>Feedback</summary>

1. **Two.** With every server in one AZ, losing that AZ stops the site (lesson 03.01).

</details>

## What you'll learn

By the end, you can explain how Auto Scaling and a load balancer together give a site elasticity and high availability (objective 06.02a), tell the two services apart, and pick a load balancer type.

Guess before you read on: which service adds servers when orders rise, the load balancer or Auto Scaling?

## An Auto Scaling group keeps the right number of instances running

**Amazon EC2 Auto Scaling** manages an **Auto Scaling group**, a set of identical EC2 instances. It keeps the group between a **minimum capacity** and a **maximum capacity** you set, at the **desired capacity** in between ([What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)). New instances come from a **launch template**, the recipe of AMI, instance type and security group from lesson 06.01. The group does three jobs:

- **Follows demand.** A **scaling policy** raises or lowers the desired capacity with load, and the group launches or terminates instances to match. This is elasticity, the skill task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3) asks you to recognize.
- **Heals itself.** It replaces any instance that is terminated or impaired, to keep the desired capacity.
- **Balances across AZs.** It spreads instances evenly across the Availability Zones you choose, so one AZ's failure leaves the others running.

You choose how it decides ([Amazon EC2 Auto Scaling FAQs](https://aws.amazon.com/ec2/autoscaling/faqs/), checked 2026-10-23): **target tracking** keeps a measure, such as average processor use, near a value you set; **scheduled scaling** changes capacity at times you set; **predictive scaling** forecasts traffic from past patterns and adds capacity before it arrives. Auto Scaling itself has no extra charge; you pay for the instances.

> **Note:** the exam guide lists **AWS Auto Scaling**, a separate service that sets up scaling for several resource types at once, such as EC2 groups and DynamoDB tables ([What is a scaling plan?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)). For "auto scaling provides elasticity", either name points to the same idea.

> **Your turn:** The bakery sets its group to minimum 2, maximum 8. Explain in one sentence each why the minimum isn't 1, and why there is a maximum at all.

<details><summary>Model answer</summary>

**Minimum 2:** with one instance per AZ, losing an AZ or a server still leaves one taking orders. **Maximum 8:** it caps the cost if a fault or a flood of bots drives the measure up.

</details>

## A load balancer sends each request to a healthy instance

**Elastic Load Balancing** spreads incoming traffic across **targets**, such as EC2 instances, containers and IP addresses, in one or more Availability Zones ([What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)). A **load balancer** gives you:

- **One front door:** one address, however many servers sit behind it.
- **Only healthy targets:** it runs **health checks**, regular tests of whether each target answers correctly, and sends requests only to targets that pass.
- **Its own scaling:** AWS grows the load balancer's capacity as traffic changes.
- **HTTPS for the servers:** it can decrypt HTTPS using a certificate from AWS Certificate Manager.

The two services work as a team: when Auto Scaling launches an instance, it registers it with the load balancer; when it terminates one, it deregisters it.

![Three numbered frames. 1: both instances healthy, the load balancer splits requests between AZ a and AZ b. 2: instance 1 fails its health check and gets no requests; instance 2 carries the site. 3: Auto Scaling launches instance 3 in AZ a, which registers and takes requests again.](../../images/06-02-health-frames.svg)

*Notice who acts: in frame 2 the load balancer stops the damage; in frame 3 Auto Scaling repairs it. (By default Auto Scaling uses only EC2's own status checks, so it replaces a failed application only if the group also uses the load balancer's [health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).)*

**Long description.** Three frames, each with a load balancer above two Availability Zones. Frame 1: requests go to instance 1 in AZ a and instance 2 in AZ b. Frame 2: instance 1 fails its health check, marked with a cross, and gets no requests; instance 2 carries the site. Frame 3: Auto Scaling has launched instance 3 in AZ a, highlighted; it registers with the load balancer and takes requests again alongside instance 2.

## Auto Scaling changes how many; the load balancer chooses which

Many people think Auto Scaling spreads traffic across instances. It doesn't. Auto Scaling changes the number of instances and replaces failed ones; the load balancer spreads the requests. The two are easy to confuse because they're almost always used together.

| | Amazon EC2 Auto Scaling | Elastic Load Balancing |
|---|---|---|
| Question it answers | How many instances should run, and where? | Which healthy instance gets this request? |
| Benefit it gives | **Elasticity**, plus self-healing and balance across AZs | One front door; traffic only to healthy targets across AZs |

Elasticity comes from Auto Scaling. High availability comes from running in several AZs, which Auto Scaling keeps balanced and the load balancer makes reachable through one address.

## Choose ALB, NLB or GWLB; Classic is the previous generation

Elastic Load Balancing has three current types, chosen by the traffic they handle ([Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/), checked 2026-10-23):

| Type | Handles | Choose it when |
|---|---|---|
| **Application Load Balancer (ALB)** | Web requests: HTTP, HTTPS, gRPC | A website or web API, perhaps routed by page address, such as `/orders` |
| **Network Load Balancer (NLB)** | Connections: TCP, UDP, TLS | Very high volume with very low delay, or a fixed IP address |
| **Gateway Load Balancer (GWLB)** | Traffic passed through appliances | Third-party virtual appliances, such as firewalls, that must scale |

You may have read that the **Classic Load Balancer** is a current option alongside ALB and NLB. That's out of date: AWS calls it the previous generation and recommends moving to a current type ([What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)). It's tempting because older courses list four equal types.

> **Example:** the owner wants two things: "Don't crash in December" and "Don't pay for six servers in January." So the group spans two AZs with a **minimum of 2** and a **maximum of 8**, target tracking follows the orders, and an **Application Load Balancer** serves the HTTPS site in both AZs. With lesson 02.02's made-up demand, the group runs 29 server-months a year instead of the 72 a fixed December-sized fleet would: elastic and highly available. The load balancer bills for every hour or partial hour, with or without customers ([Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/), checked 2026-10-24), so [Simulation S7](07-sim-elasticity-with-auto-scaling.md) practices this on paper.

## Summary

- **Two jobs:** Auto Scaling decides how many instances run, between a minimum and a maximum, and replaces unhealthy ones: elasticity. A load balancer decides which healthy instance gets each request.
- **High availability** comes from several AZs, kept balanced by Auto Scaling and reached through the load balancer, which sends requests only to healthy targets.
- **ALB** for web traffic, **NLB** for TCP and UDP at high speed or a fixed IP, **GWLB** for appliances. **Classic** is the previous generation.
- **Your side of the line:** AWS runs both services and scales the load balancer itself; the AZs, the limits, the patched AMI and the health checks are your settings.

## Practice

1. **Which statement about Amazon EC2 Auto Scaling is true?**

   A. It distributes incoming requests across instances.\
   B. It keeps the number of instances between a minimum and a maximum, and replaces unhealthy ones.\
   C. It recommends better instance sizes but doesn't change anything.\
   D. It charges a fee per scaling action.

   <details><summary>Feedback</summary>

   **B is right.** That is its job: the right number of healthy instances.

   - **A is wrong.** Spreading requests is the load balancer's job.
   - **C is wrong.** That describes AWS Compute Optimizer, which recommends; Auto Scaling acts.
   - **D is wrong.** Auto Scaling has no extra charge; you pay for the resources.

   </details>

2. **A company routes requests to different servers depending on the web address, such as `/orders` or `/photos`. Which load balancer fits?**

   A. Network Load Balancer\
   B. Gateway Load Balancer\
   C. Application Load Balancer\
   D. Classic Load Balancer

   <details><summary>Feedback</summary>

   **C is right.** It handles HTTP and HTTPS and can route by the page address.

   - **A is wrong.** An NLB works with connections, not web addresses.
   - **B is wrong.** A GWLB is for passing traffic through appliances.
   - **D is wrong.** Classic is the previous generation; AWS recommends a current type.

   </details>

3. **The bakery's group has a minimum of 2 in two AZs, behind a load balancer. AZ a fails at noon in December. Describe what each service does in the next few minutes.**

   <details><summary>Feedback</summary>

   **The load balancer** stops sending requests to AZ a's instances when they fail their health checks, so AZ b's take every order. **Auto Scaling** launches replacements in the AZ that still works until the group is back at its desired capacity.

   </details>

**Next:** [Containers and serverless](03-containers-and-serverless.md), where you run code without managing servers at all. To practice this lesson, work through [Simulation S7](07-sim-elasticity-with-auto-scaling.md).

## Where to check the current details

- [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) (checked 2026-10-23)
- [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) and [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/) (checked 2026-10-23)
- [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/) (checked 2026-10-24)

---

"Auto Scaling and load balancers" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
