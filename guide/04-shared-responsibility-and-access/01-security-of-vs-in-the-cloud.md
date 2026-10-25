---
type: lesson
id: clf-04-01
title: "Security of the cloud vs security in the cloud"
tasks: ["2.1"]
objectives: ["04.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-02-01, clf-02-05, guardrails-02, guardrails-06]
terms_introduced: [shared responsibility model, security of the cloud, security in the cloud, infrastructure, virtualization, host operating system, guest operating system, patch, security group, managed service, abstracted service]
pillars: [security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html"
  - "https://aws.amazon.com/lambda/faqs/"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-08.html"
---

# AWS secures the cloud itself; you secure what you put in it, and the line between moves with the service

AWS is responsible for security **of** the cloud: the buildings, machines and software that run its services. You are responsible for security **in** the cloud: what you build, configure and store there, and how much that includes depends on the service you choose.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [What cloud computing is](../02-why-the-cloud/01-what-cloud-computing-is.md) and pages [02](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md) and [06](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md) of the guardrails primer. The bakery's parts are in the [module brief](00-brief.md).

## Warm-up: what you remember

1. The bakery runs its ordering website on AWS and keeps its till system in the shop, with orders flowing between them. Which deployment model is that?
2. In the guardrails primer, you protected your account's root user with MFA. Who did that: you or AWS?

<details><summary>Feedback</summary>

1. **Hybrid.** Some parts run at AWS and some in the bakery's own building, connected (lesson 02.01).
2. **You did.** AWS provides MFA as a feature, but only you can choose and register your sign-in device. This lesson explains why that is your share of the work.

</details>

## What you'll learn

By the end of this lesson, you can say whether AWS or you does a given security task on Amazon EC2, Amazon RDS, AWS Lambda or Amazon S3, and give the reason (objective 04.01a).

Try this before you read on, and guess if you're unsure: the bakery's website runs on a virtual server in Amazon EC2. Who installs the security updates for that server's operating system?

## The big picture: two parts of one job

![A stack of six layers split by a dashed line. Above the line, security in the cloud, done by you: your data and who can reach it; your settings and encryption choices; the operating system and software you install on services such as EC2. Below the line, security of the cloud, done by AWS: the software that runs AWS's services; the host operating system and virtualization; hardware and the global infrastructure. Each layer has a bakery example beside it.](../../images/04-01-of-and-in.svg)

*Notice the label on the dashed line: "where it sits depends on the service". For services where AWS runs more for you, the line moves up, and you have fewer layers to look after.*

**Long description.** Six layers split by a dashed line. Above it, "Security in the cloud: you": your data and who can reach it (the bakery's orders and cake photos); your settings and encryption choices (firewall rules, storage settings, MFA); the operating system and software you install on services such as EC2 (the web server's operating system and website software). Below it, "Security of the cloud: AWS": the software that runs AWS's services; the host operating system and virtualization, which splits one physical machine into many virtual servers; hardware and the global infrastructure of Regions, Availability Zones and edge locations (buildings, machines, power, cooling). A note says the stack is drawn for EC2, and the line sits higher on RDS, Lambda and S3.

## AWS is responsible for security of the cloud

The **shared responsibility model** is AWS's description of which security work AWS does and which you do ([Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)). AWS protects the **infrastructure** that runs every AWS service: the hardware, software, networks and buildings. In AWS's words, that's everything "from the host operating system and virtualization layer down to the physical security of the facilities". **Virtualization** is the software that splits one physical computer into several virtual servers; the **host operating system** runs on the physical machine.

So you never guard a data center door, replace a failed disk or update the virtualization software; you couldn't if you wanted to. Independent auditors test AWS's controls, and AWS shares their reports (Module 09).

## You are responsible for security in the cloud, and how much depends on the service

Your share is everything you put into the cloud and every setting you choose there. AWS says it depends on the services you select, how they connect to your other systems, and the laws that apply to you. AWS gives two examples at opposite ends.

**Amazon EC2** rents you virtual servers, infrastructure as a service. On EC2, you're responsible for:

- the **guest operating system**, such as Linux or Windows inside your virtual server, including its updates and security **patches** (software updates that fix flaws);
- any software you install on the server;
- the rules of its **security group**, the firewall AWS provides for each EC2 server.

**Abstracted services, such as Amazon S3,** are the most managed kind: AWS also runs the operating system and platform, and you work only with your data through the service. On S3, you're responsible for your data, including which encryption options to use; classifying it (deciding what is sensitive); and using AWS Identity and Access Management (IAM) to say who can do what.

Between the two sit other **managed services**, such as Amazon RDS, where AWS runs the servers and software underneath and you use the service through its settings. The more AWS runs for you, the less you secure yourself.

## The line moves with the service: EC2, RDS, Lambda and S3

The exam guide names EC2, RDS and Lambda as examples of how responsibility shifts (task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1)). The graphic uses only what AWS publishes for each service.

![A grid of six layers by four services, with a dashed line separating your layers from AWS's. On EC2 the line sits below the operating system. On RDS, Lambda and S3 it sits below your code. The top row, your data and who can access it, is yours on all four.](../../images/04-01-the-line-moves.svg)

*Notice two things. The line sits lowest on EC2, where you run the operating system yourself. And whatever the service, the top row is yours: your data, and who can access it.*

| Layer | Amazon EC2 | Amazon RDS | AWS Lambda | Amazon S3 |
|---|---|---|---|---|
| Your data, and who can access it | You | You | You | You |
| Your code, and how well it runs | You: software you install | You: query tuning | You: function code and its libraries | None: no code of yours runs in S3 |
| Platform software (database engine, language runtime) | You | AWS | AWS, for supported runtimes; you move off old ones | AWS |
| Operating system | You: the guest OS | AWS | AWS | AWS |
| Servers, hardware, buildings | AWS | AWS | AWS | AWS |

**Amazon RDS**, AWS's managed relational database service, takes over the operating system and database software patching, backups, high availability and scaling ([What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)). Two things stay yours: **query tuning** (adjusting your database requests so they run well) and who can reach the database, which you control with IAM and security groups. "AWS does the backups" means AWS does the work, not that you have nothing to decide: you still choose whether to run a Multi-AZ deployment and how long automated backups are kept ([Introduction to backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)).

**AWS Lambda** runs small programs, called functions, when something triggers them; AWS manages "server maintenance, capacity provisioning, scaling, and patching" ([What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)). People often oversimplify it. A **runtime** is the language software that runs your code, such as a version of Python, and Lambda's runtime documentation splits the work this way ([Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)):

- **AWS** publishes security updates for the runtimes it manages and, by default, applies them automatically.
- **You** update your function's code, **including the libraries it depends on**, when they have security flaws.
- **You** move your functions to a supported runtime before the old one is retired.

You also choose, through the function's IAM role, which other AWS resources it may use, and you stay responsible for how sensitive your data is ([Security in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)). So "serverless" takes the servers off your list, not your code, its libraries or its permissions.

> **Your turn:** For each task, say who does it, AWS or the bakery, and name the fact that decides it.
>
> a) Installing a new version of the database software for the order database on RDS\
> b) Fixing a security flaw in a library the order functions use on Lambda\
> c) Replacing a failed power supply in the machine under the EC2 web server\
> d) Writing the security group rules for the EC2 web server

<details><summary>Model answer</summary>

a) **AWS.** The RDS User Guide puts database software install and patching on AWS.\
b) **The bakery.** Lambda's runtime documentation puts your code's dependencies on you.\
c) **AWS.** Hardware is infrastructure, on every service.\
d) **The bakery.** AWS puts security group configuration on EC2 customers.

</details>

## Your data, and who can reach it, are always yours

One row never moves: on every service, you decide what data you put in AWS and who can reach it. AWS gives you tools and safe defaults. S3's **Block Public Access** is on by default for buckets created on or after 2023-04-28 ([ACCT.08](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-08.html)), and S3 has encrypted every new upload automatically since 2023-01-05 ([Default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html)), both checked 2026-10-24.

But a safe default helps only until someone changes it. If someone at the bakery makes the photo bucket public, that's the bakery's responsibility: AWS's side worked perfectly. Turning on Block Public Access for your account (primer page 06) and adding root MFA (page 02) were your side of the line.

> **Example:** the owner asks, "Do I still have to install security updates?" **The web server (EC2):** yes, the guest OS and the website software. **The order database (RDS):** no; AWS patches the OS and database software, and the bakery tunes queries and decides who may connect. **The order functions (Lambda):** AWS patches the servers and managed runtime; the bakery updates its code and libraries and moves off a retired runtime. **The photos (S3):** nothing to patch, but the bakery keeps the bucket private.

## Summary

- **AWS secures the cloud itself:** buildings, hardware, networks, the host operating system and virtualization.
- **You secure what you put in the cloud:** your data, your settings, and any software you run. How much that includes depends on the service.
- **The line moves with the service.** EC2: you run the guest operating system. RDS: AWS also patches the operating system and database software. Lambda: AWS patches the servers and managed runtimes; you keep your code, its libraries and runtime upgrades. S3: AWS runs everything under your data.
- **Your data, and who can reach it, are always yours.** Safe defaults help only until someone changes them.

## Practice

1. **A company moves its database from an EC2 virtual server to Amazon RDS. Which task moves from the company to AWS?**

   A. Deciding which employees can read the data\
   B. Installing operating system patches\
   C. Replacing failed server hardware\
   D. Tuning the company's database queries

   <details><summary>Feedback</summary>

   **B is right.** On EC2 the customer patches the operating system; on RDS, AWS does.

   - **A is wrong.** Access to your data stays yours on every service.
   - **C is wrong.** Hardware was already AWS's on EC2.
   - **D is wrong.** Query tuning stays with you on RDS.

   </details>

2. **Which task is the customer's when using AWS Lambda?**

   A. Patching the operating system of the servers that run the functions\
   B. Applying security updates to a supported managed runtime\
   C. Moving a function to a supported runtime before its runtime is retired\
   D. Adding servers when traffic grows

   <details><summary>Feedback</summary>

   **C is right.** Lambda's runtime documentation puts that upgrade on you.

   - **A is wrong.** Lambda manages server maintenance and patching.
   - **B is wrong.** AWS publishes these updates and, by default, applies them automatically.
   - **D is wrong.** Lambda manages capacity and scaling.

   </details>

3. **A company stores customer files only in Amazon S3. Which is the company's responsibility?**

   A. Patching the operating system of S3's storage servers\
   B. Deciding who can read the files\
   C. Physical security of the data centers\
   D. Replacing failed disks

   <details><summary>Feedback</summary>

   **B is right.** Your data and who can access it are yours on every service.

   - **A is wrong.** On abstracted services such as S3, AWS runs the operating system and platform.
   - **C is wrong.** Physical security is security of the cloud: AWS's.
   - **D is wrong.** Hardware is AWS's on every service.

   </details>

**Next:** [Shared, inherited and customer-specific controls](02-shared-inherited-customer-specific.md).

## Where to check the current details

- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS (checked 2026-10-24)
- [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), Amazon RDS User Guide (checked 2026-10-24)
- [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html), AWS Lambda Developer Guide (checked 2026-10-24)

---

"Security of the cloud vs security in the cloud" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
