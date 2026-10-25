---
type: check
id: clf-00-06
title: "Diagnostic: choose your path"
tasks: ["1.3", "1.4", "2.2", "2.3", "3.2", "3.3", "3.4", "3.5", "3.7", "4.1", "4.3"]
objectives: ["01.01a", "01.02a", "01.03a", "01.04a", "01.05a", "01.05b", "01.06a", "02.04a", "03.02a", "04.04a", "05.05a", "06.03a", "07.01a", "08.03a", "09.01a", "10.02a", "11.02a", "12.02a", "13.01a"]
reader: "Adult studying alone, possibly new to IT, choosing a path through the guide; about 20 minutes; works on a phone"
prerequisites: [clf-00-01]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/virtualization/"
  - "https://aws.amazon.com/route53/what-is-dns/"
  - "https://aws.amazon.com/rds/what-is-a-relational-database/"
  - "https://www.rfc-editor.org/rfc/rfc8259"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html"
  - "https://aws.amazon.com/fargate/faqs/"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html"
  - "https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html"
  - "https://docs.aws.amazon.com/textract/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html"
  - "https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html"
---

# Seventeen questions point you to the path through the guide that fits what you already know

Part 1 checks the IT basics the AWS modules take for granted; Part 2 asks one question from each AWS module. Your two scores pick a path from [Welcome](01-welcome.md#three-paths-one-destination).

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): tasks [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3) and [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) and [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2), [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3), [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4), [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5) and [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) and [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3).

**For:** an adult studying alone, possibly new to IT, who has read [Welcome](01-welcome.md). **Time:** about 20 minutes, with no time limit. Reading works on a phone.

## How to take the diagnostic

Answer every question before opening any answer, with no notes, search or AWS account. **Mark every guess** and count it as wrong. Each question is worth one point; a "(Select TWO.)" question scores only if both choices are right. A low Part 2 score is normal: it means the lessons are for you.

## Part 1: IT basics

These five questions come from the optional on-ramp, Module 01.

**1.** A small firm rents a virtual server from a cloud provider: 2 processor cores (vCPUs) and 8 GiB of memory. Its monthly report now needs about 12 GiB of data in memory at once. While the report runs, the server slows to a crawl, the processor is 30% busy and the disk is half empty. What should the firm change, and why can the change take minutes rather than weeks?

- A. More storage; the provider attaches a bigger disk while the server keeps running
- B. More memory; the provider restarts it with a bigger share of hardware already running
- C. More processor cores; the provider adds virtual cores without any restart
- D. More memory; the provider buys a new physical server for each customer who resizes

<details><summary>Answer</summary>

**B is right.** Memory is the **bottleneck** (12 GiB needed, 8 available), and a virtual server can be restarted with more memory on hardware already running.

**Taught in:** [Computers and servers](../01-on-ramp/01-computers-and-servers.md) and [Data centers and virtualization](../01-on-ramp/04-data-centers-and-virtualization.md).

</details>

**2.** Customers type `cakes.example` into their browsers and get a message that the site can't be found. A technician confirms that the shop's web server is running, and that it answers requests sent from the internet straight to its IP address, `203.0.113.25`, on port 443. Which step of the journey has most likely failed?

- A. Securing the line: the server's certificate has expired
- B. Answering: the server's processor is too busy to reply
- C. Looking up the name: DNS isn't giving out the server's address
- D. Traveling: a firewall on the way blocks traffic to port 443

<details><summary>Answer</summary>

**C is right.** The server answers when reached by its IP address, so the failing step is the one before: DNS turning the name into that address.

**Taught in:** [Networks, IP addresses, DNS and HTTPS](../01-on-ramp/02-networks-ip-dns-https.md).

</details>

**3.** A gift shop's program saves each sale in two steps: first the order, then its payment. One day the power fails between the two steps. If the sales were kept in a spreadsheet file, part of the file might be saved and part not. But the shop keeps its sales in a database, and its program makes the two steps one transaction. What does the database keep from that sale?

- A. Neither step: a transaction is saved whole or not at all
- B. The order but not the payment, because the order was sent first
- C. Both steps, because the database holds them in memory until the power returns
- D. A damaged copy of both steps, which staff must repair by hand

<details><summary>Answer</summary>

**A is right.** A **transaction** is saved whole or not at all, even if the power fails halfway.

**Taught in:** [Files vs databases](../01-on-ramp/03-files-vs-databases.md).

</details>

**4.** A delivery company's API sends back this JSON about one van:

```json
{"van": "V2", "stops": [{"shop": "North", "boxes": 12}, {"shop": "Harbor", "boxes": 5}], "driver": {"name": "Kim", "start": "06:30"}}
```

Which statement is correct?

- A. The van makes three stops: North, Harbor and Kim
- B. The van makes two stops, and 12 boxes go to Harbor
- C. `driver` is a list of two drivers, Kim and 06:30
- D. The van makes two stops, and 5 boxes go to Harbor

<details><summary>Answer</summary>

**D is right.** `stops` is a list (square brackets) of two objects, and the second pairs `"shop": "Harbor"` with `"boxes": 5`; Kim is in the separate `driver` object.

**Taught in:** [APIs, the command line and JSON](../01-on-ramp/05-apis-command-line-and-json.md).

</details>

**5.** A bookkeeper used the same password for a hobby forum and for her firm's accounting app. The forum is broken into, and its list of email addresses and passwords is published. Which two habits would have stopped an attacker from signing in to the accounting app with that password? (Select TWO.)

- A. HTTPS on the accounting app's website
- B. A different password for every account
- C. Encryption of the accounting app's stored data
- D. A longer version of the same shared password
- E. MFA on the accounting app

<details><summary>Answer</summary>

**B and E are right.** A different password per account means the leak opens only the forum, and MFA demands a second proof the leak didn't contain. HTTPS, encryption and length don't stop a valid password.

**Taught in:** [Everyday security](../01-on-ramp/06-everyday-security.md).

</details>

## Part 2: one question from each AWS module

These twelve questions follow Modules 02 to 13 in order. If you have never used AWS, answer what you can and mark your guesses.

**6.** A pumpkin farm's booking website needs 1 server for ten months of the year and 4 servers in September and October. If the farm owns its servers, it must keep 4 all year, at $100 per server-month for everything owning costs. Renting cloud servers costs $150 per server-month, paid only for the servers it runs. All the numbers are made up. If the farm rents exactly what it needs each month, which is cheaper over a year?

- A. Owning, by about $2,400, because renting 4 servers all year costs more than owning them
- B. Renting, by about $2,100, because it pays for 18 server-months instead of 48
- C. Neither, because both options must pay for the four-server peak
- D. Owning, because its price per server-month is lower

<details><summary>Answer</summary>

**B is right.** Owning pays for 48 server-months ($4,800); renting pays for 18 ($2,700). A lower rate (D) doesn't help when you pay for idle servers.

**Taught in:** [What a data center really costs](../02-why-the-cloud/04-what-a-data-center-really-costs.md), Module 02.

</details>

**7.** An online shop's contract says its customers' data must stay inside the European Union (EU). Most of its customers are in Sweden. In this made-up case, Europe (Stockholm) doesn't offer one service the shop depends on. Europe (Frankfurt), Europe (Ireland) and Europe (London) all offer it; the shop's tests show Frankfurt answers Swedish customers fastest of the three, and its estimate for London is the cheapest. Which Region should the shop choose?

- A. Europe (Stockholm), because it is the Region nearest to the shop's customers
- B. Europe (London), because it offers the service at the lowest price of the three
- C. Europe (Frankfurt), because it is the fastest EU Region that offers the service
- D. Europe (Ireland), because any EU Region that offers the service will do equally well

<details><summary>Answer</summary>

**C is right.** Rules first (London is outside the EU), then services (Stockholm lacks one), then closeness: Frankfurt is faster than Ireland.

**Taught in:** [Choosing a Region](../03-aws-around-the-world/02-choosing-a-region.md), Module 03.

</details>

**8.** An IAM user, Priya, is in a user group whose policy allows `s3:GetObject` and `s3:PutObject` on the bucket `menu-photos`, which means reading and uploading its files. A policy attached to Priya herself denies `s3:PutObject` on that bucket. The bucket's own policy also allows Priya to upload. What can Priya do in the bucket?

- A. Read and upload files, because the group's policy and the bucket's policy both allow uploading
- B. Nothing, because one deny on the bucket blocks every action on it
- C. Read files only, because the explicit deny on uploading overrides both allows
- D. Upload files only, because a policy attached to the user replaces the group's policy

<details><summary>Answer</summary>

**C is right.** An explicit deny always wins over any number of allows, and it covers only the action it names, so reading still works.

**Taught in:** [Policies and least privilege](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md), Module 04.

</details>

**9.** A research lab's analysis tool runs inside its PostgreSQL database server, and the tool's vendor requires it to have access to that server's operating system. Which way of running the database fits, and what does the lab take on?

- A. PostgreSQL on Amazon EC2; the lab patches the server and database and runs its own backups
- B. Amazon RDS for PostgreSQL; AWS patches the operating system, and the lab installs the tool on it
- C. Amazon Aurora PostgreSQL; a Multi-AZ deployment gives the lab access to the operating system
- D. Amazon RDS for PostgreSQL with a read replica; the lab installs the tool on the replica's server

<details><summary>Answer</summary>

**A is right.** Operating system access is a reason to run your own database, on EC2, where the lab also takes on patching and backups. RDS, Aurora and replicas give no OS access.

**Taught in:** [Managed or self-managed databases](../05-storing-data/05-managed-or-self-managed-databases.md), Module 05.

</details>

**10.** A team wants as little as possible to manage. Which pairing of workload and compute service is the best fit?

- A. A data import that runs for about two hours once a night: AWS Lambda
- B. A web API, packaged as a container image, that answers requests all day: Amazon ECS on AWS Fargate
- C. A tool that needs changes to the operating system of the server it runs on: AWS Fargate
- D. Resizing each uploaded photo, about two seconds of work each: an EC2 instance that runs all day

<details><summary>Answer</summary>

**B is right.** A container that runs all day suits ECS on Fargate. Lambda stops at 15 minutes (A), and Fargate gives no OS access (C).

**Taught in:** [Containers and serverless](../06-running-applications/03-containers-and-serverless.md), Module 06.

</details>

**11.** A shop's web servers sit in a public subnet and its database in a private subnet of the same VPC. Which two settings keep people on the internet from reaching the database directly? (Select TWO.)

- A. The private subnet's route table has no route to an internet gateway
- B. The web servers in the public subnet have their own public IPv4 addresses
- C. An internet gateway is attached to the VPC and used by the public subnet
- D. The database's security group accepts its port only from the web servers' group
- E. The database's storage is encrypted at rest with a key from AWS KMS

<details><summary>Answer</summary>

**A and D are right.** No route to an internet gateway means no internet path, and the security group accepts the database port only from the web servers.

**Taught in:** [Your own network](../07-connecting-it/01-your-own-network.md) and [Filtering traffic](../07-connecting-it/02-filtering-traffic.md), Module 07.

</details>

**12.** A café's online ordering runs on an AWS Lambda function. The owner wants an email whenever the function reports more than five errors in five minutes. Which two pieces together do this? (Select TWO.)

- A. An AWS CloudTrail trail that records each error the function raises
- B. AWS X-Ray tracing on the function, set to email failed requests
- C. An Amazon CloudWatch alarm on the function's `Errors` metric
- D. An Amazon SES identity verified for the café's email domain
- E. An Amazon SNS topic with the owner's email subscribed and confirmed

<details><summary>Answer</summary>

**C and E are right.** A CloudWatch alarm watches Lambda's `Errors` metric and notifies an SNS topic, which emails confirmed subscribers. SES (D) sends a business's own mail, not alerts.

**Taught in:** [Watching workloads](../08-building-and-operating/03-watching-workloads.md), Module 08.

</details>

**13.** An auditor asks a bakery chain to show what its payment server's security group allowed on each day of the last three months, and to flag any day on which it allowed SSH from anywhere on the internet. A year ago, the chain turned on recording of its resources' settings and of the activity in its account. Which service answers both parts of the question?

- A. AWS Config
- B. AWS CloudTrail
- C. Amazon CloudWatch
- D. AWS Artifact

<details><summary>Answer</summary>

**A is right.** AWS Config records each resource's settings over time and flags rule breaks. CloudTrail (B) records who changed the group, not its settings day by day.

**Taught in:** [Who did what](../09-protecting-and-governing/01-who-did-what.md), Module 09.

</details>

**14.** A city council receives thousands of scanned letters from residents. It wants the text of each letter pulled out, and then each letter tagged with the places and organizations it mentions, so that it reaches the right department. The council has no machine learning staff. Which two services, used one after the other, do this? (Select TWO.)

- A. Amazon Rekognition
- B. Amazon Textract
- C. Amazon Translate
- D. Amazon Comprehend
- E. Amazon Polly

<details><summary>Answer</summary>

**B and D are right.** Textract turns the scans into text; Comprehend finds the places and organizations in it. Rekognition sees images, Translate changes language, and Polly speaks.

**Taught in:** [AI and machine learning](../10-data-ai-and-more/02-ai-and-ml.md), Module 10.

</details>

**15.** Which pairing of workload and Amazon EC2 purchasing option is the best fit?

- A. A web tier that runs all year at the same size: Spot Instances
- B. A two-week trial whose running hours can't be predicted: a three-year Reserved Instance
- C. Overnight test runs that simply start again if a server is taken away: Spot Instances
- D. A database that runs all year, to get a lower rate: an On-Demand Capacity Reservation

<details><summary>Answer</summary>

**C is right.** Spot is the cheapest but can be taken back with two minutes' warning, so it suits work that can start again. A Capacity Reservation (D) gives no discount of its own.

**Taught in:** [Purchasing options](../11-paying-for-aws/02-purchasing-options.md), Module 11.

</details>

**16.** Which pairing of question and AWS tool is right?

- A. "Is AWS planning maintenance on the hardware under our instances?": AWS Trusted Advisor
- B. "Is Amazon S3 having trouble in our Region right now?": AWS Support Center
- C. "Who deleted our photo bucket last night?": the AWS Health Dashboard
- D. "Do any of our security groups leave a port open to everyone?": AWS Trusted Advisor

<details><summary>Answer</summary>

**D is right.** Trusted Advisor checks your own setup, including ports open to everyone. AWS Health covers AWS's side (A, B); CloudTrail answers who deleted what (C).

**Taught in:** [Tools that watch your account](../12-getting-help/02-tools-that-watch-your-account.md), Module 12.

</details>

**17.** A museum group is planning its move to AWS. Its marketing director insists that visitors' email addresses be encrypted, and readable only by the newsletter team. In the AWS Cloud Adoption Framework (AWS CAF), which perspective does this concern belong to?

- A. Business
- B. Security
- C. People
- D. Platform

<details><summary>Answer</summary>

**B is right.** Map a concern by what is at stake, not who raises it: protecting data and deciding who reads it is Security, even when marketing asks.

**Taught in:** [The Cloud Adoption Framework](../13-moving-to-aws/01-the-cloud-adoption-framework.md), Module 13.

</details>

## Score yourself, then choose your path

Write down two scores: **Part 1** (questions 1 to 5, out of 5) and **Part 2** (questions 6 to 17, out of 12).

| Part 1 (of 5) | Part 2 (of 12) | Your path | Start here |
|---|---|---|---|
| 0 to 3 | Any | **On-ramp** | [Module 01: On-ramp](../01-on-ramp/00-brief.md). Each lesson opens with a test-out, so you skip what you already know |
| 4 or 5 | 0 to 9 | **Standard** | [Module 02: Why organizations use the cloud](../02-why-the-cloud/00-brief.md), then every module in order |
| 4 or 5 | 10 to 12 | **Fast** | The fast path in [Welcome](01-welcome.md#three-paths-one-destination): take each module's mastery check first, as a pretest |

**If Part 1 was 4,** take the test-out of the on-ramp lesson your missed question names under "Taught in", and read that lesson if the test-out shows a gap.

**On the fast path,** each module's mastery check decides for that module: pass it and skip the lessons (but still do its core lab), or score below 80% and work through them. The diagnostic is a starting point, not a verdict; you can switch paths at any time.

> **Your turn:** Write down your two scores, the path they point to, and the first page you will open.

Whichever path you take, you set up a safe AWS account with the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md) before Lab 01, in Module 02. [Before your first lab](05-before-your-first-lab.md) says what to have ready.

---

"Diagnostic: choose your path" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
