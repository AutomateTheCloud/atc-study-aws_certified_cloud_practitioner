---
type: check
id: clf-06-08
title: "Module 06 mastery check"
tasks: ["3.3", "1.1", "2.1", "3.1"]
objectives: ["06.01a", "06.02a", "06.03a", "06.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the lessons of Module 06; about 20 minutes for each check; works on a phone"
prerequisites: [clf-06-01, clf-06-02, clf-06-03, clf-06-04]
pillars: [performance-efficiency, reliability, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/ec2/instance-types/"
  - "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html"
  - "https://aws.amazon.com/fargate/faqs/"
---

# Module 06 mastery check: choose the compute, say how it scales, and say who manages it

**For:** an adult who has finished lessons [06.01](01-ec2.md) to [06.04](04-simpler-paths.md). **Time:** about 20 minutes per check.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1) and [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3).

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 07.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

### Question A1

Which TWO workloads point to a compute optimized instance family? (Select TWO.)

- A. A nightly job compressing millions of log files, processors at full speed
- B. An in-memory cache that fills the server's RAM, processors mostly idle
- C. A service converting recorded lectures into video formats, processors busy for hours
- D. A quiet brochure website on which nothing ever runs out
- E. A database making huge numbers of reads and writes to local disks

<details><summary>Answer</summary>

**A and C.** Both run out of processor first; AWS lists batch processing and media transcoding as compute optimized workloads.

- **B is wrong.** Its bottleneck is memory: memory optimized.
- **D is wrong.** When nothing runs out, general purpose fits.
- **E is wrong.** Heavy use of local disks is storage optimized.

</details>

### Question A2

A nightly analysis keeps running out of memory. If a server is taken away, the job restarts later and loses only time. The team wants the lowest cost with no commitment. Which choice fits?

- A. A memory optimized instance type, paid for with Reserved Instances
- B. A Spot instance type, AWS's memory-heavy family for interruptible work
- C. A compute optimized instance type, paid for as Spot Instances
- D. A memory optimized instance type, paid for as Spot Instances

<details><summary>Answer</summary>

**D is right.** The bottleneck picks the family; interruptible work with no commitment picks Spot.

- **A is wrong.** Reserved Instances need a commitment.
- **B is wrong.** Spot is a way to pay, not an instance type or family.
- **C is wrong.** The job runs out of memory, not processor.

</details>

### Question A3

Two EC2 instances behind an Application Load Balancer reach full processor use during a sale, and pages time out. What changes if they join an Amazon EC2 Auto Scaling group with target tracking on processor use?

- A. Nothing: the load balancer already adds servers when needed
- B. New instances start as processor use rises, and the load balancer sends requests to them
- C. Auto Scaling takes over routing from the load balancer
- D. AWS Compute Optimizer moves both instances to a larger type

<details><summary>Answer</summary>

**B is right.** Auto Scaling changes how many instances run and registers new ones with the load balancer: elasticity.

- **A is wrong.** A load balancer never adds instances.
- **C is wrong.** Auto Scaling doesn't route requests.
- **D is wrong.** Compute Optimizer only recommends.

</details>

### Question A4

Which TWO design choices keep an EC2 web tier taking orders if a server or an Availability Zone fails? (Select TWO.)

- A. Reserved Instances for the minimum capacity
- B. Instances spread across at least two Availability Zones
- C. A target tracking policy on average processor use
- D. A load balancer that sends requests only to healthy targets
- E. AWS Compute Optimizer recommendations

<details><summary>Answer</summary>

**B and D.** High availability comes from more than one AZ and from a load balancer that stops sending requests to failed targets.

- **A is wrong.** Reserved Instances change how you pay.
- **C is wrong.** Target tracking gives elasticity.
- **E is wrong.** A size recommendation doesn't keep a site running.

</details>

### Question A5

Application 1 receives a very high volume of UDP readings from soil sensors. Application 2 is an HTTPS dashboard that sends `/maps` and `/reports` requests to different servers. Which pairing fits?

- A. 1: Application Load Balancer. 2: Network Load Balancer
- B. 1: Gateway Load Balancer. 2: Application Load Balancer
- C. 1: Network Load Balancer. 2: Application Load Balancer
- D. 1: Network Load Balancer. 2: Classic Load Balancer

<details><summary>Answer</summary>

**C is right.** NLB handles TCP and UDP at very high volume; ALB handles web requests and can route by page address.

- **A is wrong.** It swaps the two.
- **B is wrong.** GWLB passes traffic through appliances such as firewalls.
- **D is wrong.** Classic is the previous generation.

</details>

### Question A6

An old reporting program needs one specific operating system version with a driver installed into it, and can't be packaged as a container. Which option fits, and who patches the operating system?

- A. AWS Fargate, and AWS patches the operating system
- B. Amazon EC2, and AWS patches the guest operating system
- C. AWS Lambda, and AWS patches the operating system
- D. Amazon EC2, and the company patches the guest operating system

<details><summary>Answer</summary>

**D is right.** Full control of the operating system and no container point to EC2, where the guest operating system is the customer's.

- **A is wrong.** Fargate gives no access to the operating system.
- **B is wrong.** On EC2, AWS patches only the host and its virtualization.
- **C is wrong.** You can't install a driver into Lambda's operating system.

</details>

### Question A7

A team draws three boxes: (1) where container images are kept, (2) what decides how many copies run, and (3) serverless compute the containers run on. Which services fill the boxes, in order?

- A. AWS Fargate, Amazon ECS, Amazon ECR
- B. Amazon ECR, AWS Fargate, Amazon EC2 Auto Scaling
- C. Amazon ECR, Amazon ECS, AWS Fargate
- D. Amazon ECS, Amazon ECR, AWS Fargate

<details><summary>Answer</summary>

**C is right.** ECR stores images, ECS orchestrates, and Fargate is the serverless compute.

- **A is wrong.** Fargate stores no images, and ECR runs nothing.
- **B is wrong.** Fargate doesn't orchestrate, and EC2 Auto Scaling changes EC2 instances, not containers.
- **D is wrong.** It swaps ECR and ECS.

</details>

### Question A8

A company moves a nightly job from EC2 to an AWS Lambda function on an Amazon EventBridge schedule. Which TWO tasks does it still own? (Select TWO.)

- A. Patching the servers' operating system
- B. Choosing an instance type
- C. The function's code and libraries
- D. Placing copies in two or more Availability Zones
- E. Moving to a supported runtime before the current one is retired

<details><summary>Answer</summary>

**C and E.** On Lambda your code, its libraries and moving off a retiring runtime stay yours.

- **A is wrong.** AWS patches the servers under Lambda.
- **B is wrong.** Lambda has no instance types; you set memory.
- **D is wrong.** Lambda has availability built in.

</details>

### Question A9

Client 1 wants a simple site from a ready-made image, at one predictable monthly price. Client 2's developers want to upload code and have AWS build load balancing, Auto Scaling and health monitoring in their own account. Which pairing fits?

- A. 1: Amazon Lightsail. 2: AWS Elastic Beanstalk
- B. 1: AWS Elastic Beanstalk. 2: Amazon Lightsail
- C. 1: Amazon Lightsail. 2: AWS Batch
- D. 1: Amazon EC2 with Auto Scaling. 2: Amazon Lightsail

<details><summary>Answer</summary>

**A is right.** Lightsail bundles a server, storage and transfer into one monthly price; Beanstalk builds the setup from uploaded code in the customer's account.

- **B is wrong.** It swaps the two.
- **C is wrong.** Batch runs queues of jobs, not web apps.
- **D is wrong.** EC2 means building each part; Lightsail doesn't fit Client 2.

</details>

### Question A10

Request 1: each month an insurer queues about 50,000 container jobs of up to an hour each, and wants compute started while they wait and removed afterwards. Request 2: a broadcaster's footage may never leave its studio, where it wants EC2 with the same APIs as in the Region. Which pairing fits?

- A. 1: AWS Batch. 2: AWS Outposts
- B. 1: AWS Lambda. 2: AWS Outposts
- C. 1: AWS Batch. 2: A Local Zone in the studio's city
- D. 1: Amazon Lightsail. 2: AWS Outposts

<details><summary>Answer</summary>

**A is right.** Batch queues jobs and launches and removes compute; Outposts puts AWS hardware in the customer's building.

- **B is wrong.** An hour is past Lambda's 15 minutes per invocation.
- **C is wrong.** A Local Zone is AWS's site, not the studio's building.
- **D is wrong.** Lightsail sells fixed-price servers, not compute that follows a queue.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 06.01a | [Choose the family from the bottleneck](01-ec2.md#choose-the-family-from-the-bottleneck) |
| A2, B2 | 06.01a | [Instance types are not purchasing options](01-ec2.md#instance-types-are-not-purchasing-options) |
| A3, B3 | 06.02a | [Auto Scaling changes how many](02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which) |
| A4, B4 | 06.02a | [An Auto Scaling group](02-auto-scaling-and-load-balancers.md#an-auto-scaling-group-keeps-the-right-number-of-instances-running) and [Simulation S7](07-sim-elasticity-with-auto-scaling.md) |
| A5, B5 | 06.02a | [Choose ALB, NLB or GWLB](02-auto-scaling-and-load-balancers.md#choose-alb-nlb-or-gwlb-classic-is-the-previous-generation) |
| A6, B6 | 06.03a | [Fargate](03-containers-and-serverless.md#fargate-runs-containers-without-servers-to-manage) and [Lambda or Fargate](03-containers-and-serverless.md#lambda-or-fargate-short-event-driven-work-or-containers-that-keep-running) |
| A7, B7 | 06.03a | [Four names, four jobs](03-containers-and-serverless.md#four-names-four-jobs-ecr-stores-ecs-and-eks-orchestrate-fargate-supplies-the-computers) |
| A8, B8 | 06.03a | [Your side of the line](03-containers-and-serverless.md#your-side-of-the-line) |
| A9, B9 | 06.04a | [EC2, Elastic Beanstalk or Lightsail](04-simpler-paths.md#ec2-elastic-beanstalk-or-lightsail-three-ways-to-run-a-web-app) |
| A10, B10 | 06.04a | [Batch](04-simpler-paths.md#batch-runs-large-numbers-of-jobs-from-a-queue) and [Outposts](04-simpler-paths.md#outposts-brings-aws-hardware-into-your-own-building) |

## Check B: parallel retest

### Question B1

Which TWO workloads point to a memory optimized instance family? (Select TWO.)

- A. A media encoder, processors at full speed for hours
- B. An in-memory database whose whole data set must fit in RAM
- C. A test server, idle most of the day with short bursts
- D. Analytics that load a large data set into memory
- E. A log search engine slowed by reads and writes to local disks

<details><summary>Answer</summary>

**B and D.** Both run out of memory first.

- **A is wrong.** A processor bottleneck: compute optimized.
- **C is wrong.** Mostly idle with short bursts: a burstable general purpose type.
- **E is wrong.** Heavy local disk use: storage optimized.

</details>

### Question B2

Order servers with a balanced load will run around the clock on one configuration for three years, and must never be taken away at short notice. The company wants a lower rate for a commitment. Which choice fits?

- A. A general purpose instance type, paid for as Spot Instances
- B. The Reserved instance type, which AWS builds for steady workloads
- C. A general purpose instance type, paid for with Reserved Instances
- D. A compute optimized instance type, paid for On-Demand

<details><summary>Answer</summary>

**C is right.** A balanced load picks general purpose; steady use with a commitment picks Reserved Instances.

- **A is wrong.** Spot Instances can be reclaimed with a two-minute warning.
- **B is wrong.** "Reserved" is a way to pay, not an instance type.
- **D is wrong.** Nothing runs out of processor, and On-Demand gives no discount.

</details>

### Question B3

In a load test, graph 1 shows running instances rising from 2 to 5, then falling back. Graph 2 shows each request handed to one of the healthy instances. Which service does each graph show?

- A. Graph 1: Elastic Load Balancing. Graph 2: Amazon EC2 Auto Scaling
- B. Graph 1: Amazon EC2 Auto Scaling. Graph 2: Amazon CloudFront
- C. Graph 1: AWS Compute Optimizer. Graph 2: Elastic Load Balancing
- D. Graph 1: Amazon EC2 Auto Scaling. Graph 2: Elastic Load Balancing

<details><summary>Answer</summary>

**D is right.** Auto Scaling changes how many instances run; the load balancer picks which healthy instance gets each request.

- **A is wrong.** It swaps the two jobs.
- **B is wrong.** CloudFront caches content at edge locations.
- **C is wrong.** Compute Optimizer only recommends sizes.

</details>

### Question B4

An Auto Scaling group has a minimum of 2, a maximum of 10, and target tracking on processor use. Traffic triples at 11:00 and falls back at 14:00. Which TWO things happen with nobody acting? (Select TWO.)

- A. The group launches instances from its launch template
- B. The load balancer launches extra instances
- C. The group switches to a larger instance type
- D. The group raises its own maximum above 10
- E. The group terminates spare instances after the rush, keeping at least 2

<details><summary>Answer</summary>

**A and E.** Capacity follows demand up and down, between the minimum and maximum: elasticity.

- **B is wrong.** Only Auto Scaling adds instances.
- **C is wrong.** Auto Scaling changes the number, not the type.
- **D is wrong.** The maximum is a limit you set; Auto Scaling never changes it.

</details>

### Question B5

A company is replacing the Classic Load Balancer in front of its HTTPS store. The new one must send `/checkout` and `/blog` requests to different servers. Which choice fits?

- A. A Network Load Balancer
- B. A Gateway Load Balancer
- C. Keep the Classic Load Balancer, which AWS still recommends for websites
- D. An Application Load Balancer

<details><summary>Answer</summary>

**D is right.** ALB handles HTTP and HTTPS and can route by page address.

- **A is wrong.** NLB works with connections, not web addresses.
- **B is wrong.** GWLB passes traffic through appliances.
- **C is wrong.** AWS calls Classic the previous generation.

</details>

### Question B6

A team runs its API on Amazon ECS, on EC2 instances it patches itself, and patching keeps falling behind. It wants to keep ECS and its images but stop looking after servers. What should it change?

- A. Run the tasks on AWS Fargate instead of the team's EC2 instances
- B. Rewrite the API as AWS Lambda functions and retire ECS
- C. Move the containers to Amazon EKS on the same EC2 instances
- D. Keep the images in Amazon ECR instead of the current registry

<details><summary>Answer</summary>

**A is right.** Fargate is an ECS capacity option where AWS chooses, scales and patches the servers.

- **B is wrong.** It means a rewrite without ECS.
- **C is wrong.** The team would still patch the same instances.
- **D is wrong.** ECR only stores images.

</details>

### Question B7

A company uses Kubernetes on premises and wants the same tools on AWS, with no worker servers to patch. Which combination fits?

- A. Amazon EKS, with the containers running on AWS Fargate
- B. Amazon ECS, with the containers running on AWS Fargate
- C. AWS Fargate alone, acting as the Kubernetes orchestrator
- D. Amazon ECR, with the containers running in AWS Lambda

<details><summary>Answer</summary>

**A is right.** EKS runs Kubernetes, and Fargate supplies serverless compute for EKS as well as ECS.

- **B is wrong.** ECS isn't Kubernetes.
- **C is wrong.** Fargate doesn't orchestrate.
- **D is wrong.** ECR only stores images, and Lambda doesn't run Kubernetes workloads.

</details>

### Question B8

A company moves its web app from EC2 to Amazon ECS on AWS Fargate. Which TWO tasks does it stop doing? (Select TWO.)

- A. Patching the servers' operating system
- B. Updating the libraries inside its container image
- C. Choosing instance types and how many servers to run
- D. Setting the tasks' IAM permissions
- E. Protecting the customer data the app stores

<details><summary>Answer</summary>

**A and C.** With Fargate, AWS chooses, scales and patches the servers.

- **B is wrong.** Everything inside the image stays the company's.
- **D is wrong.** IAM permissions are the customer's on every option.
- **E is wrong.** Data is always the customer's.

</details>

### Question B9

A charity's one-page site runs on one EC2 instance, and its treasurer wants one predictable monthly price and little to manage. A startup wants to upload its code and have AWS build load balancing and scaling in its own account. Which pairing fits?

- A. Charity: AWS Elastic Beanstalk. Startup: Amazon Lightsail
- B. Charity: Amazon Lightsail. Startup: AWS Elastic Beanstalk
- C. Charity: a Reserved Instance. Startup: AWS Batch
- D. Charity: AWS Outposts. Startup: AWS Elastic Beanstalk

<details><summary>Answer</summary>

**B is right.** Lightsail bundles the parts into one monthly price; Beanstalk builds the setup from uploaded code in the customer's account.

- **A is wrong.** It swaps the two.
- **C is wrong.** A Reserved Instance lowers only the instance rate, and Batch runs job queues.
- **D is wrong.** Outposts puts AWS hardware in the customer's building, for a term of years.

</details>

### Question B10

Request 1: a bank's trade records must stay in its own data center, where it wants EC2 with the same APIs as in its Region. Request 2: a film studio queues thousands of container rendering jobs a day and wants to pay for compute only while jobs wait. Which pairing fits?

- A. 1: AWS Batch. 2: AWS Outposts
- B. 1: AWS Outposts. 2: AWS Batch
- C. 1: AWS Outposts. 2: Amazon Lightsail
- D. 1: Amazon Lightsail. 2: AWS Batch

<details><summary>Answer</summary>

**B is right.** Outposts keeps the instances and records on site; Batch launches compute for queued jobs and removes it afterwards.

- **A is wrong.** It swaps the two.
- **C is wrong.** Lightsail sells fixed-price servers, not compute that follows a queue.
- **D is wrong.** Lightsail runs in AWS Regions.

</details>

---

"Module 06 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
