---
type: lesson
id: clf-06-03
title: "Containers and serverless"
tasks: ["3.3", "2.1"]
objectives: ["06.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 05, the guardrails primer and lessons 06.01 and 06.02; about 20 minutes; works on a phone"
prerequisites: [clf-06-01, clf-06-02, clf-04-01, clf-05-01]
terms_introduced: [container, container image, container registry, orchestration, Amazon ECR, Amazon ECS, Amazon EKS, Kubernetes, task, AWS Fargate, serverless, AWS Lambda, function, event, trigger, invocation, GB-second]
pillars: [performance-efficiency, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html"
  - "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html"
  - "https://aws.amazon.com/ecs/faqs/"
  - "https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html"
  - "https://aws.amazon.com/eks/faqs/"
  - "https://aws.amazon.com/fargate/faqs/"
  - "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"
  - "https://aws.amazon.com/lambda/faqs/"
  - "https://aws.amazon.com/lambda/pricing/"
  - "https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
  - "https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html"
---

# Containers package your app; ECS or EKS runs them; Fargate and Lambda take the servers off your list

Containers package an app to run the same anywhere; Amazon ECS or Amazon EKS keeps them running; AWS Fargate and AWS Lambda take servers off your list. The exam asks which of these fits a job, and what you still manage on it.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on lessons [06.01](01-ec2.md) and [06.02](02-auto-scaling-and-load-balancers.md), and on [Security of vs in the cloud](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md).

## Warm-up: what you remember

1. From lesson 04.01: the bakery's order functions run on AWS Lambda. A security flaw is found in a library their code uses. Who updates the library?

<details><summary>Feedback</summary>

1. **The bakery.** AWS patches the servers and managed runtime under Lambda; the code and its libraries are the customer's.

</details>

## What you'll learn

By the end, you can say what Amazon ECR, Amazon ECS, Amazon EKS and AWS Fargate each do, and pick EC2, Fargate or Lambda for a job and say what you still manage on each (objective 06.03a).

Guess before you read on: a teammate says, "We'll use Fargate to decide where our containers run and how many copies we need." What's wrong?

## The big picture: the further right, the less you manage

![A grid of who manages what on Amazon EC2, ECS or EKS on EC2, ECS or EKS on Fargate, and AWS Lambda: the rows that are yours fall from 5 of 6 to 1 of 6.](../../images/06-03-what-you-manage.svg)

*Notice how the cells marked AWS spread from the bottom right. On Fargate you stop choosing and patching servers; on Lambda you also stop packaging the language runtime. The top row is yours everywhere.*

**Long description.** Columns: EC2; ECS or EKS on EC2; ECS or EKS on Fargate; Lambda. Your code, libraries, data and permissions: you on all four. Language runtime: you on the first three; AWS on Lambda, while you move off retired runtimes. Starting and spreading copies: you on EC2 (with Auto Scaling); ECS, EKS or Lambda on the others. Choosing servers: you on the first two; AWS on Fargate (you set CPU and memory per task) and Lambda (you set memory). Server operating system and patches: you on the first two; AWS on the others. Hardware: AWS on all four. Rows yours: 5, 4, 2 and 1 of 6. A note: ECS Managed Instances and EKS Auto Mode are middle options where AWS also patches and scales the EC2 instances.

## Four names, four jobs: ECR stores, ECS and EKS orchestrate, Fargate supplies the computers

A **container** is a standard package of software that holds an application's code and everything it depends on ([AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html)). Every container started from one **container image** is identical, so an app that works on a laptop works the same on AWS. A **container registry** stores images. **Orchestration** decides where containers run and how many, and replaces failed ones. The bakery's inventory app arrived from its supplier as a container image, and it needs all four of the exam's container names:

| | Amazon ECR | Amazon ECS | Amazon EKS | AWS Fargate |
|---|---|---|---|---|
| **Job** | Stores container images | Orchestrates containers, AWS's own way | Orchestrates containers with Kubernetes | Supplies serverless compute for containers |
| **Pick it when** | You need somewhere to keep images | You want the simplest AWS-native choice | You already use Kubernetes | You don't want to manage servers under ECS or EKS |
| **Charge** | Storage and data transfer | None for ECS itself | Per cluster, per hour | vCPU, memory and storage per second |

**Amazon Elastic Container Registry (Amazon ECR)** can also scan images for known flaws ([What is Amazon ECR?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)). **Amazon Elastic Container Service (Amazon ECS)** starts **tasks**, its name for running copies of your containers, and keeps the number you asked for running ([What is Amazon ECS?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)). **Amazon Elastic Kubernetes Service (Amazon EKS)** runs **Kubernetes**, a widely used open-source orchestrator, managed by AWS, so existing Kubernetes tools work ([What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)).

### "Fargate orchestrates containers" is wrong

A common belief is that Fargate is an orchestrator, an alternative to ECS or EKS. It isn't. ECS or EKS decides where containers run and how many, and schedules them onto Fargate ([AWS Fargate FAQs](https://aws.amazon.com/fargate/faqs/)), which ECS lists as a **capacity** option beside EC2 instances. It's tempting because you rarely see Fargate alone ("ECS on Fargate"), and with no servers to look at, Fargate seems to do everything. A setup often uses three at once: ECR, ECS and Fargate.

## Fargate runs containers without servers to manage

**AWS Fargate** is **serverless** compute for containers, for both ECS and EKS: AWS runs, scales and patches the servers out of your sight, and you pay for what you use. You say how much CPU and memory each task needs; you don't choose, add or patch servers ([AWS Fargate FAQs](https://aws.amazon.com/fargate/faqs/), checked 2026-10-23). It suits apps that keep running, such as a web API, and jobs that run for a while and stop. AWS says to use EC2 for GPU work, or for more control of the instances.

## Lambda runs your code only when an event triggers it

**AWS Lambda** runs your code with no servers to provision or manage. You upload a **function**, connect a **trigger**, and Lambda runs it each time an **event** arrives; each run is an **invocation** ([What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), checked 2026-10-23). Triggers include a file landing in Amazon S3, a web request through Amazon API Gateway, a message in a queue, or a schedule in Amazon EventBridge. For the bakery, each new cake photo saved to S3 can trigger a resize function.

Facts that decide whether a job fits, from the [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) page (checked 2026-10-23):

- **At most 15 minutes per invocation.** Longer jobs don't fit a standard function.
- **Automatic scaling:** 300 photos at once means many copies side by side.
- **No state you can count on between runs:** anything to keep goes to S3 or a database.
- **Availability built in,** with no maintenance windows ([AWS Lambda FAQs](https://aws.amazon.com/lambda/faqs/)); you don't spread it across Availability Zones yourself as you do with EC2.
- **Billed per request plus GB-seconds:** a **GB-second** is memory in GB times seconds of run time ([AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/)). Nothing is billed while no events arrive.

> **Dated (checked 2026-10-24):** AWS now calls classic functions **Lambda Event Functions** and has added longer-running forms ([What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)). For CLF-C02, use the classic rule: event-driven functions, at most 15 minutes per invocation.

## Lambda or Fargate: short event-driven work, or containers that keep running

Lambda and Fargate are the two serverless compute options the exam names, so questions often put them side by side.

![Two panels comparing AWS Lambda and AWS Fargate: what you hand over, what starts it, how long it runs, how you size it, how it bills, and what it isn't for.](../../images/06-03-lambda-vs-fargate.svg)

*Notice the "What starts it" and "How long it runs" rows. They decide most questions. Packaging as a container image doesn't decide it, because Lambda can run a container image too.*

**Long description.** Both: no servers to manage, AWS scales them, you pay for what runs. Lambda: function code, as a .zip file or container image; started by an event; up to 15 minutes per invocation; memory from 128 MB to 10,240 MB, CPU growing with it; billed per request plus GB-seconds; not for long or always-on work or full OS control. Fargate: a container image through ECS or EKS, which starts a task or keeps a service running; runs as long as the task, minutes or months; vCPU and memory set per task; billed per second for vCPU, memory and storage, 1-minute minimum; not for GPU work, which needs EC2. Sources: Lambda and Fargate pricing and quota pages, checked 2026-10-23.

Start from the shape of the work. An event and a short job: Lambda. An app in a container that keeps running: Fargate. Full control of the operating system, GPUs, or software that can't be containerized: EC2. So the bakery's photo resize moves to Lambda, and the inventory app to ECS on Fargate with its image in ECR.

> **Your turn:** For each job, choose Lambda, Fargate or EC2, and give the deciding fact.
>
> a) A web API packaged as a container that must answer requests around the clock\
> b) Sending a confirmation email each time an order is saved\
> c) Training a machine learning model on GPUs for six hours\
> d) A nightly report that takes 40 minutes and is already packaged as a container

<details><summary>Model answer</summary>

a) **Fargate:** a container that keeps running. b) **Lambda:** a short, event-triggered job. c) **EC2:** Fargate has no GPUs, and six hours is far past Lambda's 15 minutes. d) **Fargate:** 40 minutes is too long for Lambda, and the container can run as a task and stop.

</details>

## Your side of the line

On every option, your code and its libraries, your data, and your app's IAM permissions are yours. On ECS or EKS on EC2, so are the instances' operating system, patches and count. On Fargate, everything inside your image stays yours: a flawed library stays until you rebuild. On Lambda, you also move off a runtime before AWS retires it ([Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)). "With serverless, AWS handles the security" is still wrong (lesson 04.01): serverless removes servers from your list, not your code, images or permissions.

## Summary

- **ECR stores images, ECS and EKS orchestrate, Fargate supplies serverless compute.** Fargate is not an orchestrator. EKS is for teams that use Kubernetes.
- **Lambda runs code when an event triggers it,** at most 15 minutes per invocation, billed per request and GB-second.
- **Lambda for short event-driven work, Fargate for containers that keep running, EC2 for GPUs or full control.**
- **Your code, images, libraries and permissions stay yours** on every option.

## Practice

1. **Which AWS service stores container images?**

   A. Amazon ECS\
   B. Amazon ECR\
   C. AWS Fargate\
   D. Amazon EKS

   <details><summary>Feedback</summary>

   **B is right.** Amazon Elastic Container Registry is the registry.

   - **A is wrong.** ECS orchestrates containers; it pulls images from a registry.
   - **C is wrong.** Fargate runs containers as serverless capacity.
   - **D is wrong.** EKS runs Kubernetes to orchestrate containers.

   </details>

2. **A job processes a file each time one is uploaded, and each run takes about 30 seconds. The company wants no servers to manage and to pay nothing when no files arrive. Which service fits best?**

   A. Amazon EC2 with Auto Scaling\
   B. AWS Lambda\
   C. Amazon ECS on EC2 instances\
   D. Amazon EKS

   <details><summary>Feedback</summary>

   **B is right.** An upload is an event, 30 seconds is well under 15 minutes, and Lambda bills only for runs.

   - **A and C are wrong.** The company would manage EC2 instances, which bill while idle.
   - **D is wrong.** EKS charges per cluster-hour even when idle, and it needs capacity underneath.

   </details>

3. **Explain in two sentences why "we moved to Fargate, so patching is AWS's problem now" is only half true.**

   <details><summary>Feedback</summary>

   **Model answer:** AWS now patches the servers and operating system under the containers. But the libraries inside the company's images are still the company's, and stay flawed until it rebuilds and redeploys them.

   </details>

**Next:** [Simpler paths](04-simpler-paths.md). If you want to run a function yourself, [Optional lab 07: a Lambda function](05-lab-07-a-lambda-function.md) shows one.

## Where to check the current details

- [What is Amazon ECS?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) and [AWS Fargate FAQs](https://aws.amazon.com/fargate/faqs/) (checked 2026-10-23)
- [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) (checked 2026-10-23)
- [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (checked 2026-10-23)

---

"Containers and serverless" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
