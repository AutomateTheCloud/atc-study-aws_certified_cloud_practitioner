---
type: check
id: clf-06-08
title: "Module 06 mastery check"
tasks: ["3.3", "1.1", "2.1"]
objectives: ["06.01a", "06.02a", "06.03a", "06.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the lessons of Module 06; about 25 minutes for each check"
prerequisites: [clf-06-01, clf-06-02, clf-06-03, clf-06-04]
pillars: [performance-efficiency, reliability, cost-optimization, security]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 06 mastery check: choose the compute, say how it scales, and say who manages it

This check tests the four objectives of Module 06: choosing an EC2 instance family, explaining how Auto Scaling and a load balancer give elasticity and high availability, picking EC2, Fargate or Lambda and saying what you still manage, and matching Elastic Beanstalk, Lightsail, Batch and Outposts to their uses.

**For:** an adult studying alone, possibly new to IT, who has finished the lessons of [Module 06](00-brief.md). **Time:** about 25 minutes for Check A, and the same for Check B if you need it.

## How to use this check

Take **Check A** closed-book: no lessons, no notes, no searching. Answer all 12 items before you open any answer. **The threshold is 80%,** which is 10 of 12.

- **If you score below 10,** use the [correction map](#correction-map) for each item you missed: reread the section it names, try the other way of seeing it, and do the lab or simulation it lists. Then take **Check B**, the parallel retest. It tests the same objectives with new scenarios.
- **If you score 10 or more,** go on to the [enrichment tasks](#enrichment-for-learners-who-passed).

On the exam, a "(Select TWO.)" item scores only if you choose both right answers. Score it the same way here.

## Check A

**A1.** A company lists five workloads it will move to Amazon EC2. Which TWO point to a compute optimized instance family? (Select TWO.)

A. A nightly batch job that compresses millions of log files, with its processors at full speed and little memory in use\
B. An in-memory cache whose data fills the server's RAM while its processors stay mostly idle\
C. A service that converts recorded lectures into several video formats, with its processors busy for hours\
D. A quiet brochure website on which no single resource ever runs out\
E. A database that makes huge numbers of reads and writes to the instance's own local disks

<details><summary>Answer</summary>

**A and C.** Both run out of processor first, and AWS lists batch processing and media transcoding among the compute optimized workloads.

- **B is wrong.** Its bottleneck is memory, so it needs a memory optimized type.
- **D is wrong.** When nothing runs out, a general purpose type fits, often a burstable T type.
- **E is wrong.** Heavy, fast use of local disks is the job of storage optimized types.

</details>

**A2.** A research team runs a large analysis every night. It holds its whole data set in memory, and memory is what keeps running out. If a server is taken away during the run, the job restarts later and loses only time. The team wants the lowest compute cost and won't commit to a term. Which choice fits?

A. A memory optimized instance type, paid for with Reserved Instances\
B. A Spot instance type, which is AWS's memory-heavy family for interruptible work\
C. A compute optimized instance type, paid for as Spot Instances\
D. A memory optimized instance type, paid for as Spot Instances

<details><summary>Answer</summary>

**D is right.** The item asks for two separate choices. The bottleneck, memory, picks the family: memory optimized. Work that can be interrupted, with no commitment and the lowest cost, picks the purchasing option: Spot Instances.

- **A is wrong.** The family is right, but Reserved Instances need a commitment for a term, which the team won't make.
- **B is wrong.** Spot isn't an instance type or a family. It's a way to pay for any instance type.
- **C is wrong.** Spot fits the payment, but the job runs out of memory, not processor.

</details>

**A3.** A development team stops its ten test instances every evening and starts them again each morning. Each instance has an EBS root volume and uses the public IPv4 address that AWS assigned it automatically. Which statement about the hours while they are stopped is correct?

A. Nothing is billed overnight, because a stopped instance is switched off and stores nothing\
B. Instance hours stop, but the EBS volumes still bill, and each gets a new public address on start\
C. Instance hours continue at a lower rate, and each instance keeps its public address for the morning\
D. The EBS volumes are deleted at each stop, so their storage charges end until the morning

<details><summary>Answer</summary>

**B is right.** Stopping ends the charge for instance time, but the EBS volumes still exist and are still billed. An address that AWS assigned automatically is released at a stop, so a new one comes with each start; a fixed address would need an Elastic IP address, which bills until you release it.

- **A is wrong.** "Off" isn't free: the disks are still stored for the team.
- **C is wrong.** A stopped instance bills no instance time at any rate, and it loses an automatically assigned address.
- **D is wrong.** A stop keeps the EBS volumes and their data. Only terminating deletes volumes, and only those set to delete on termination.

</details>

**A4.** A company's website runs on two EC2 instances behind an Application Load Balancer. During a sale, both instances reach full processor use and pages time out, although both still pass their health checks. The team asks what would change if it put the instances in an Amazon EC2 Auto Scaling group, attached to the load balancer, with a target tracking policy on average processor use. Which reply is accurate?

A. Nothing new: the load balancer would already have added servers to the site if it had been allowed to\
B. New instances would start as processor use rises, and the load balancer would send requests to them\
C. Requests would be spread more evenly, because Auto Scaling would take over routing from the load balancer\
D. AWS Compute Optimizer would move both of the instances to a larger instance type until the sale ends

<details><summary>Answer</summary>

**B is right.** Auto Scaling changes how many instances run. It launches them from its launch template when the measure rises and registers them with the load balancer, which then sends requests to the larger set. That is elasticity.

- **A is wrong.** A load balancer never adds instances. It scales its own capacity, not the servers behind it.
- **C is wrong.** Auto Scaling doesn't route requests; the load balancer keeps doing that. With every instance full, spreading alone adds no capacity.
- **D is wrong.** Compute Optimizer only recommends sizes; it changes nothing. Auto Scaling changes the number of instances, not their type.

</details>

**A5.** A company wants its EC2 web tier to keep taking orders if a server or a whole Availability Zone fails. Which TWO design choices give it that high availability? (Select TWO.)

A. Reserved Instances for the group's minimum capacity\
B. Instances spread across at least two Availability Zones\
C. A target tracking policy that follows average processor use\
D. A load balancer that sends requests only to targets that pass health checks\
E. AWS Compute Optimizer, to recommend a better instance size

<details><summary>Answer</summary>

**B and D.** High availability comes from running in more than one AZ, so one failure doesn't take every server with it, and from a load balancer that stops sending requests to failed targets while the healthy ones carry the site.

- **A is wrong.** Reserved Instances change how you pay for the instances, not where they run or whether they survive a failure.
- **C is wrong.** Target tracking gives elasticity: the count follows demand. It doesn't decide where the instances run.
- **E is wrong.** A recommendation about size doesn't keep the site running when an AZ fails.

</details>

**A6.** A farming company runs two applications on EC2. Application 1 receives a very high volume of small readings over UDP from thousands of soil sensors. Application 2 is a web dashboard over HTTPS that sends requests for `/maps` to one group of servers and requests for `/reports` to another. Which pairing of load balancer types fits?

A. Application 1: Application Load Balancer. Application 2: Network Load Balancer\
B. Application 1: Gateway Load Balancer. Application 2: Application Load Balancer\
C. Application 1: Network Load Balancer. Application 2: Application Load Balancer\
D. Application 1: Network Load Balancer. Application 2: Classic Load Balancer

<details><summary>Answer</summary>

**C is right.** The Network Load Balancer handles connections over TCP, UDP and TLS at very high volume with very low delay. The Application Load Balancer handles web requests and can route them by the page address.

- **A is wrong.** It swaps the two: an Application Load Balancer doesn't handle UDP, and a Network Load Balancer works with connections, not page addresses.
- **B is wrong.** A Gateway Load Balancer passes traffic through third-party appliances, such as firewalls; it isn't for receiving sensor readings.
- **D is wrong.** Classic is the previous generation; AWS recommends a current type for new work.

</details>

**A7.** A company still uses an old reporting program that runs only on one specific operating system version, with a driver installed into that operating system. The vendor says the program can't be packaged as a container. Which option fits, and who then patches the operating system it runs on?

A. AWS Fargate, and AWS patches the operating system\
B. Amazon EC2, and AWS patches the guest operating system\
C. AWS Lambda, and AWS patches the operating system\
D. Amazon EC2, and the company patches the guest operating system

<details><summary>Answer</summary>

**D is right.** The work needs full control of the operating system, and it can't be containerized. That is the strongest reason to manage more: EC2. On EC2 the guest operating system is on the customer's side of the line, so the company patches it.

- **A is wrong.** Fargate runs containers, and this program can't be put in one. It also gives no access to the operating system underneath.
- **B is wrong.** EC2 is the right choice, but AWS patches only the host and its virtualization; the guest operating system is the customer's.
- **C is wrong.** Lambda runs your code on a runtime AWS manages; you can't install a driver into its operating system.

</details>

**A8.** A team moving its app to containers draws three boxes on a whiteboard: (1) where the container images are kept, (2) what decides how many copies run and replaces any that fail, and (3) the compute the containers run on, with no servers for the team to manage. Which services fill the boxes, in order?

A. AWS Fargate, Amazon ECS, Amazon ECR\
B. Amazon ECR, AWS Fargate, Amazon EC2 Auto Scaling\
C. Amazon ECR, Amazon ECS, AWS Fargate\
D. Amazon ECS, Amazon ECR, AWS Fargate

<details><summary>Answer</summary>

**C is right.** Amazon ECR stores images, Amazon ECS orchestrates (where containers run, how many, and replacing failed copies), and AWS Fargate is serverless compute that ECS places the containers on.

- **A is wrong.** Fargate stores no images, and ECR runs nothing.
- **B is wrong.** Fargate doesn't orchestrate; ECS or EKS does. EC2 Auto Scaling changes the number of EC2 instances, not of containers.
- **D is wrong.** It swaps the first two jobs: ECR stores, ECS orchestrates.

</details>

**A9.** A company moves a nightly clean-up job from an EC2 instance to an AWS Lambda function that an Amazon EventBridge schedule triggers. Which TWO tasks does the company still own after the move? (Select TWO.)

A. Patching the operating system of the servers that run the function\
B. Choosing an instance type for the function\
C. The function's code and the libraries it uses\
D. Placing copies of the function in two or more Availability Zones\
E. Moving the function to a supported runtime before its current one is retired

<details><summary>Answer</summary>

**C and E.** On Lambda your code and its libraries stay yours, and so does moving off a runtime before AWS retires it. (So do the function's IAM permissions and your data.)

- **A is wrong.** AWS runs and patches the servers and operating system under Lambda.
- **B is wrong.** Lambda has no instance types to choose; you set the function's memory.
- **D is wrong.** Lambda has availability built in; spreading servers across AZs is your job only on EC2.

</details>

**A10.** At each month end, an insurance company recalculates the risk on about 50,000 policies. Each calculation is packaged as a container job that runs unattended for up to an hour. The company wants AWS to queue the jobs, start compute while they wait, remove it when the queue is empty, and use discounted spare capacity, because a stopped job can simply be retried. Which service fits?

A. AWS Elastic Beanstalk\
B. AWS Batch\
C. Amazon Lightsail\
D. AWS Lambda

<details><summary>Answer</summary>

**B is right.** AWS Batch takes container jobs in a job queue, launches compute for them, removes it when it's no longer needed, and can run the jobs on Spot Instances. Batch itself has no extra charge.

- **A is wrong.** Beanstalk builds and runs the setup for a web application, not a queue of unattended jobs.
- **C is wrong.** Lightsail sells a few simple servers at fixed monthly prices, not compute that grows and shrinks with a queue.
- **D is wrong.** Lambda runs short functions when events trigger them. It has no job queue or compute environment for long container jobs, and an hour is longer than the exam's rule for one Lambda invocation allows.

</details>

**A11.** A broadcaster processes raw studio footage on EC2 instances. Its contracts say the raw footage may never leave its own studio building, and its engineers want to use the same AWS APIs, console and tools there as in its AWS Region. Which service fits?

A. AWS Outposts\
B. Amazon Lightsail\
C. AWS Batch\
D. A Local Zone in the city where the studio is

<details><summary>Answer</summary>

**A is right.** AWS Outposts puts AWS-managed racks or servers inside the customer's own building, running services such as EC2 with the same APIs and tools as the Region.

- **B is wrong.** Lightsail servers run in AWS Regions.
- **C is wrong.** Batch schedules jobs in a Region; it doesn't change where the hardware is.
- **D is wrong.** A Local Zone is close to the city's users, but it is AWS's site, not the broadcaster's building, so the footage would leave the studio.

</details>

**A12.** A web agency takes on two new clients. Client 1, a bakery, wants a simple brochure website started from a ready-made image, with one predictable monthly price for the server, storage and data transfer. Client 2's developers want to upload new versions of their app's code and have AWS build the load balancing, Auto Scaling and health monitoring in their own account, while they keep control of the resources. Which pairing fits?

A. Client 1: Amazon Lightsail. Client 2: AWS Elastic Beanstalk\
B. Client 1: AWS Elastic Beanstalk. Client 2: Amazon Lightsail\
C. Client 1: Amazon Lightsail. Client 2: AWS Batch\
D. Client 1: Amazon EC2 with Auto Scaling. Client 2: Amazon Lightsail

<details><summary>Answer</summary>

**A is right.** Lightsail bundles a server, storage, a static IP address and a data transfer allowance into one monthly plan price. Elastic Beanstalk takes uploaded code and builds the EC2 instances, load balancing, scaling and health monitoring in the customer's account, at no extra charge for Beanstalk itself.

- **B is wrong.** It swaps the two: Beanstalk bills for the parts it creates, with no fixed monthly price, and Lightsail doesn't assemble a load-balanced, auto-scaling setup from uploaded code.
- **C is wrong.** Batch runs queues of unattended jobs, not web applications.
- **D is wrong.** EC2 with Auto Scaling means building everything by hand and paying for each part, which Client 1 doesn't want; Lightsail doesn't fit Client 2.

</details>

## Correction map

For each item you missed, reread the section, then try the other way of seeing it. Each of these says the idea differently from the lesson.

| Item | Objective (level) | Reread | Another way to see it | Practice with |
|---|---|---|---|---|
| A1 | 06.01a, choose a family (Ap) | [Choose the family from the bottleneck](01-ec2.md#choose-the-family-from-the-bottleneck) | Watch the server's monitoring, not its job title: whichever gauge sits at the top first names the family. | [Lab 08](06-lab-08-launch-and-terminate-an-instance.md) |
| A2 | 06.01a (Ap) | [Instance types are not purchasing options](01-ec2.md#instance-types-are-not-purchasing-options) | Picture one order form with two fields: "What hardware?" (the type) and "How will you pay?" (On-Demand, Savings Plans, Reserved, Spot). An answer to one field never fills the other. | [Lab 08](06-lab-08-launch-and-terminate-an-instance.md) |
| A3 | 06.01a (Un) | [Stopping pauses the instance bill; terminating ends it](01-ec2.md#stopping-pauses-the-instance-bill-terminating-ends-it) | List the three things that bill for an instance (running hours, a public address, the disk), then cross out what each state stops. Only termination crosses out all three. | [Lab 08](06-lab-08-launch-and-terminate-an-instance.md), Part B |
| A4 | 06.02a, elasticity and high availability (Un) | [Auto Scaling changes how many; the load balancer chooses which](02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which) | Ask what each service takes in. Auto Scaling takes in a measure of demand and puts out a number of servers; the load balancer takes in requests and puts out a choice of server. | [Simulation S7](07-sim-elasticity-with-auto-scaling.md), Decision 3 |
| A5 | 06.02a (Un) | [Auto Scaling changes how many; the load balancer chooses which](02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which), the principle under the table | Sort each setting by the question it answers: "Will the site survive a failure?" (AZs, health checks) or "Will the count follow demand?" (the scaling policy). | [Simulation S7](07-sim-elasticity-with-auto-scaling.md), Decision 4 |
| A6 | 06.02a (Un) | [Choose ALB, NLB or GWLB; Classic is the previous generation](02-auto-scaling-and-load-balancers.md#choose-alb-nlb-or-gwlb-classic-is-the-previous-generation) | Name the traffic before the product: web pages and APIs (ALB), raw TCP or UDP connections (NLB), traffic that must pass through appliances (GWLB). | [Simulation S7](07-sim-elasticity-with-auto-scaling.md) |
| A7 | 06.03a, EC2, Fargate or Lambda (Ap) | [Worked example: compute for the bakery's photo job and inventory app](03-containers-and-serverless.md#worked-example-compute-for-the-bakerys-photo-job-and-inventory-app), the flowchart | Each step toward EC2 needs a reason to manage more. "It can't be containerized" or "it needs the operating system" is the strongest reason there is. | [Lab 07](05-lab-07-a-lambda-function.md) |
| A8 | 06.03a (Ap) | [Four names, four jobs](03-containers-and-serverless.md#four-names-four-jobs-ecr-stores-ecs-and-eks-orchestrate-fargate-supplies-the-computers) and ["Fargate orchestrates containers" is wrong](03-containers-and-serverless.md#fargate-orchestrates-containers-is-wrong) | Think of a shipping port: ECR is the warehouse of images, ECS or EKS is the harbor master deciding where each container goes, and Fargate is the ships, which someone else owns and maintains. | [Lab 07](05-lab-07-a-lambda-function.md) |
| A9 | 06.03a (Ap) | [Your side of the line](03-containers-and-serverless.md#your-side-of-the-line) | Lambda takes away everything below your code. The code itself, its libraries, its runtime version and its permissions are still above the line. | [Lab 07](05-lab-07-a-lambda-function.md), "Look at the role" and the Recap |
| A10 | 06.04a, match the simpler paths (Ap) | [Batch runs large numbers of jobs from a queue](04-simpler-paths.md#batch-runs-large-numbers-of-jobs-from-a-queue) | The word "queue" plus "many unattended jobs" points to Batch, whatever the jobs compute. | [Worked example: matching five requests](04-simpler-paths.md#worked-example-matching-five-requests) |
| A11 | 06.04a (Ap) | [Outposts brings AWS hardware into your own building](04-simpler-paths.md#outposts-brings-aws-hardware-into-your-own-building) | Ask "whose building?" A Region and a Local Zone are AWS's buildings; only an Outpost sits in yours. | [Worked example: matching five requests](04-simpler-paths.md#worked-example-matching-five-requests) |
| A12 | 06.04a (Ap) | [EC2, Elastic Beanstalk or Lightsail: three ways to run a web app](04-simpler-paths.md#ec2-elastic-beanstalk-or-lightsail-three-ways-to-run-a-web-app) | Read each request for two clues: who should assemble the setup, and how the client wants to be billed. A fixed monthly price means Lightsail; "upload code" means Beanstalk. | [Worked example: matching five requests](04-simpler-paths.md#worked-example-matching-five-requests) |

## Check B: parallel retest

Take Check B after you have worked through the correction map. It tests the same objectives as Check A, item for item, with new scenarios. The threshold is again 10 of 12.

**B1.** A company lists five workloads it will move to Amazon EC2. Which TWO point to a memory optimized instance family? (Select TWO.)

A. A media encoder that keeps its processors at full speed for hours\
B. An in-memory database whose whole data set must fit in RAM\
C. A test server that is idle most of the day and busy for a few minutes at a time\
D. Analytics that load a large data set into memory to compare its records\
E. A log search engine slowed by its reads and writes to the instance's local disks

<details><summary>Answer</summary>

**B and D.** Both run out of memory first. AWS lists in-memory databases and analytics on large data sets held in memory among the memory optimized workloads.

- **A is wrong.** A processor bottleneck points to compute optimized.
- **C is wrong.** A mostly idle server with short bursts suits a burstable general purpose type, such as a T type.
- **E is wrong.** Heavy, fast use of local disks points to storage optimized.

</details>

**B2.** A company's order-processing servers have a balanced load: no single resource runs out first. They will run around the clock on the same configuration for the next three years, and must never be taken away at short notice. The company wants a lower rate in return for a commitment. Which choice fits?

A. A general purpose instance type, paid for as Spot Instances\
B. The Reserved instance type, which AWS builds for steady workloads\
C. A general purpose instance type, paid for with Reserved Instances\
D. A compute optimized instance type, paid for On-Demand

<details><summary>Answer</summary>

**C is right.** A balanced load picks the family: general purpose. Steady use of one configuration, with a commitment in return for a lower rate, picks the purchasing option: Reserved Instances. The hardware is the same either way; only the way of paying changes.

- **A is wrong.** Spot Instances can be reclaimed with a two-minute warning, which these servers can't accept.
- **B is wrong.** "Reserved" isn't an instance type; it is a way to pay for one.
- **D is wrong.** Nothing here runs out of processor, and On-Demand gives no discount for the commitment.

</details>

**B3.** A finance manager reviews two test servers that nobody uses any more. Server 1 is stopped; it has an EBS root volume. Server 2 was terminated, and its root volume was set to delete on termination. Which statement about their charges is correct?

A. Neither bills anything, because neither one is running instance hours\
B. Server 1 still bills for its EBS volume; Server 2 bills nothing\
C. Server 2 still bills for its volume for a month; Server 1 bills nothing\
D. Both still bill for instance hours, at a lower rate than while running

<details><summary>Answer</summary>

**B is right.** Stopping ends instance-time charges, but a stopped instance keeps its EBS volume, which bills while it exists (as would any Elastic IP address it kept). Terminating with the volume set to delete removes the volume too, so the charges end. If Server 1 is never needed again, terminating it is the fix.

- **A is wrong.** That is the misconception: "off" isn't free while a disk is still stored.
- **C is wrong.** A volume deleted at termination stops billing; the stopped server is the one still paying.
- **D is wrong.** Neither a stopped nor a terminated instance bills instance time at any rate.

</details>

**B4.** During a load test of a web tier, an engineer watches two graphs. Graph 1 shows the number of running instances rising from 2 to 5 as the test ramps up, then falling back. Graph 2 shows each incoming request being handed to one of the healthy instances, so the 5 share the work. Which service does each graph show?

A. Graph 1: Elastic Load Balancing. Graph 2: Amazon EC2 Auto Scaling\
B. Graph 1: Amazon EC2 Auto Scaling. Graph 2: Amazon CloudFront\
C. Graph 1: AWS Compute Optimizer. Graph 2: Elastic Load Balancing\
D. Graph 1: Amazon EC2 Auto Scaling. Graph 2: Elastic Load Balancing

<details><summary>Answer</summary>

**D is right.** Auto Scaling changes how many instances run, up and down with demand: elasticity. The load balancer decides which healthy instance gets each request. Auto Scaling registers each new instance with the load balancer, so the new ones get work at once.

- **A is wrong.** It swaps the two jobs. A load balancer never adds instances, and Auto Scaling never hands out requests.
- **B is wrong.** CloudFront caches content at edge locations; it doesn't share requests among a Region's instances.
- **C is wrong.** Compute Optimizer recommends instance sizes; it doesn't start or stop instances.

</details>

**B5.** A company's Auto Scaling group spans two Availability Zones, with a minimum of 2, a maximum of 10, and a target tracking policy that keeps average processor use near 50%. Traffic triples at 11:00 and falls back at 14:00. Which TWO things happen with nobody acting? (Select TWO.)

A. The group launches instances from its launch template as processor use rises\
B. The load balancer launches extra instances when requests start to queue\
C. The group replaces its instances with a larger instance type for the rush\
D. The group raises its own maximum above 10 if the rush is bigger than expected\
E. The group terminates spare instances after the rush, but never runs fewer than 2

<details><summary>Answer</summary>

**A and E.** Target tracking raises the desired capacity as the measure rises and lowers it when it falls, so capacity follows demand up and down: elasticity. The group never goes below its minimum or above its maximum.

- **B is wrong.** A load balancer spreads requests; only Auto Scaling adds instances.
- **C is wrong.** Auto Scaling changes the number of instances, not their type.
- **D is wrong.** The maximum is a limit you set, so that an unexpected surge can't run up the bill. Auto Scaling never changes it for you.

</details>

**B6.** A company is replacing the old Classic Load Balancer in front of its HTTPS web store. The new one must send requests for `/checkout` to one group of servers and requests for `/blog` to another. Which choice fits?

A. A Network Load Balancer\
B. A Gateway Load Balancer\
C. Keep the Classic Load Balancer, which AWS still recommends for websites\
D. An Application Load Balancer

<details><summary>Answer</summary>

**D is right.** The Application Load Balancer handles web requests over HTTP and HTTPS and can route them by the page address.

- **A is wrong.** A Network Load Balancer works with connections, not web addresses.
- **B is wrong.** A Gateway Load Balancer passes traffic through third-party appliances.
- **C is wrong.** AWS calls the Classic Load Balancer the previous generation and recommends moving to a current type.

</details>

**B7.** A team runs its containerized order API on Amazon ECS, on EC2 instances that the team launches and patches itself. Patching keeps falling behind. The team wants to keep using ECS and its container images, but stop looking after any servers. What should it change?

A. Run the tasks on AWS Fargate instead of the team's EC2 instances\
B. Rewrite the API as AWS Lambda functions and retire ECS\
C. Move the containers to Amazon EKS on the same EC2 instances\
D. Keep the images in Amazon ECR instead of the current registry

<details><summary>Answer</summary>

**A is right.** ECS lists Fargate as a capacity option beside EC2 instances. On Fargate, AWS chooses, scales and patches the servers under the tasks, while ECS keeps orchestrating as before. The team still owns its images, their libraries and the tasks' permissions.

- **B is wrong.** It could remove servers too, but it throws away ECS, which the team wants to keep, and means rewriting the API.
- **C is wrong.** EKS is another orchestrator; on the same EC2 instances the team would still patch them, and it would add Kubernetes.
- **D is wrong.** ECR only stores images. Where images are kept doesn't change who patches the servers that run them.

</details>

**B8.** A company already runs its containers with Kubernetes in its own data center, and its team wants to keep using the same Kubernetes tools on AWS. The team also wants no worker servers of its own to patch. Which combination fits?

A. Amazon EKS, with the containers running on AWS Fargate\
B. Amazon ECS, with the containers running on AWS Fargate\
C. AWS Fargate alone, acting as the Kubernetes orchestrator\
D. Amazon ECR, with the containers running in AWS Lambda

<details><summary>Answer</summary>

**A is right.** Amazon EKS runs Kubernetes with an AWS-managed control plane, so the team's tools keep working. Fargate supplies serverless compute for EKS as well as ECS, so there are no worker servers to patch.

- **B is wrong.** ECS is AWS's own orchestrator, not Kubernetes, so the team's Kubernetes tools wouldn't work with it.
- **C is wrong.** Fargate doesn't orchestrate; EKS or ECS decides where containers run and places them on Fargate.
- **D is wrong.** ECR only stores images, and Lambda doesn't run Kubernetes workloads.

</details>

**B9.** A company moves its web app from EC2 instances it manages to an Amazon ECS service on AWS Fargate. Which TWO tasks does the company stop doing? (Select TWO.)

A. Patching the operating system of the servers that run the containers\
B. Keeping the libraries inside its container image up to date\
C. Choosing instance types and how many servers to run\
D. Setting the permissions that the app's tasks get through IAM\
E. Protecting the customer data that the app stores

<details><summary>Answer</summary>

**A and C.** With Fargate, AWS chooses, scales and patches the servers under the containers. The company only sets the CPU and memory for each task.

- **B is wrong.** Everything inside the image stays the company's. A flawed library stays until the company rebuilds and redeploys the image.
- **D is wrong.** The permissions an app gets through its IAM role are the customer's on every compute option.
- **E is wrong.** Data is always on the customer's side of the line.

</details>

**B10.** A two-person startup has a Ruby web app. The founders don't want to wire up load balancers and scaling themselves, but they want those parts built in their own account, so that they can later choose instance types and run in more than one Availability Zone. They also want each new version deployed the same way every time by uploading code. Which service fits?

A. Amazon Lightsail\
B. AWS Batch\
C. AWS Elastic Beanstalk\
D. AWS Outposts

<details><summary>Answer</summary>

**C is right.** Elastic Beanstalk takes uploaded code and builds EC2 instances, load balancing, Auto Scaling and health monitoring in the customer's account, and the customer keeps control of those resources. Beanstalk itself costs nothing extra.

- **A is wrong.** Lightsail sells bundled servers at fixed prices; it doesn't build a load-balanced, auto-scaling setup from uploaded code.
- **B is wrong.** Batch runs queued, unattended jobs, not web applications.
- **D is wrong.** Outposts puts AWS hardware in the customer's building; it doesn't deploy code.

</details>

**B11.** A small charity runs its one-page website on a single EC2 instance. Its treasurer complains that the bill has separate lines (the instance, its disk, a public IPv4 address, data transfer) and that the total changes from month to month. The charity wants one predictable monthly price and as little to manage as possible. Which move fits best?

A. Amazon Lightsail\
B. AWS Elastic Beanstalk\
C. A Reserved Instance for the existing EC2 instance\
D. AWS Outposts

<details><summary>Answer</summary>

**A is right.** Lightsail is AWS's simplest way to run a small website, and its plans bundle the server, storage, a static IP address and a data transfer allowance into one monthly price.

- **B is wrong.** Beanstalk builds a load-balanced, auto-scaling setup and bills for each resource it creates, by use, so the bill would still have several changing lines.
- **C is wrong.** A Reserved Instance lowers the rate for the instance itself, but the disk, address and transfer still bill separately.
- **D is wrong.** Outposts puts AWS racks or servers in the customer's own building, for a term of years.

</details>

**B12.** An IT consultancy brings two requests. Request 1: a bank's regulator requires its trade records to stay inside the bank's own data center, and the bank wants to process them there on EC2 instances, using the same console and APIs as in its AWS Region. Request 2: after each day's shoot, a film studio queues thousands of frame-rendering jobs, each packaged as a container, and wants to pay for compute only while there are jobs waiting to run. Which pairing fits?

A. Request 1: AWS Batch. Request 2: AWS Outposts\
B. Request 1: AWS Outposts. Request 2: AWS Batch\
C. Request 1: AWS Outposts. Request 2: Amazon Lightsail\
D. Request 1: Amazon Lightsail. Request 2: AWS Batch

<details><summary>Answer</summary>

**B is right.** Outposts brings AWS-managed hardware into the bank's data center, so the instances and the records stay on site, with the same tools as the Region. Batch queues the container jobs, launches compute for them and removes it afterwards.

- **A is wrong.** It swaps the two services.
- **C is wrong.** Lightsail sells a few fixed-price servers, not compute that grows and shrinks with a queue of jobs.
- **D is wrong.** Lightsail servers run in AWS Regions, not inside the bank's data center.

</details>

## Enrichment for learners who passed

Three harder tasks. Each has no single right answer; compare your reasoning with the model answer, not just your conclusion.

**Task 1: a compute plan to justify.** A ticket-selling startup has three programs. (a) A web store that is quiet for weeks, then gets ten times its usual traffic in the first hour of a big concert sale. (b) A fraud-scoring run each night: about 40,000 independent jobs, each a container, each able to restart if interrupted. (c) A small piece of code that must run each time the payment company calls back to confirm a payment, at random times, a few seconds each. Choose compute for each, say how each grows and shrinks, and name what the startup still patches. Then name the Well-Architected best practice your whole plan applies.

<details><summary>Model answer</summary>

(a) **EC2 instances in an Auto Scaling group across at least two AZs, behind an Application Load Balancer.** Target tracking follows the surge, and a scheduled action or predictive scaling adds instances before a sale opens at a known time, because new instances take minutes to start. The startup patches the AMI in the launch template and the guest operating system. If the store is already a container, ECS on Fargate is a strong alternative that removes the patching of servers.
(b) **AWS Batch on Spot capacity.** The queue drives the compute, which is removed when the jobs finish, and interrupted jobs simply retry. The startup keeps the job images and their libraries up to date.
(c) **AWS Lambda.** It runs only when a callback arrives, scales on its own, and bills nothing between callbacks. The startup owns the code, its libraries, the runtime version and the function's role.
The plan applies [PERF02-BP01 Select the best compute options for your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html): each shape of work gets its own compute choice, rather than one server type for everything.

</details>

**Task 2: a real-world complication.** A company's web tier runs in an Auto Scaling group behind an Application Load Balancer. One night the web application on one instance crashes, but the instance itself keeps running. The load balancer marks it unhealthy and stops sending it requests. By morning the instance is still there, still unhealthy, and the group still counts it. Explain why Auto Scaling didn't replace it, what to change, and which Well-Architected best practice the fix applies.

<details><summary>Model answer</summary>

By default an Auto Scaling group judges health only by EC2's own status checks. The instance's hardware and operating system were fine, so EC2 reported it healthy, and Auto Scaling ignored the load balancer's verdict. The load balancer limited the damage, but nothing repaired it, and the tier ran a server short all night. The fix is to turn on Elastic Load Balancing health checks for the group, so an instance that fails the load balancer's checks is also replaced. That is [REL11-BP03 Automate healing on all layers](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_auto_healing_system.html): healing should react to the application failing, not only to the server failing.

</details>

**Task 3: when pay-per-use stops winning.** A team moved an image-tagging job to Lambda when it handled a few hundred images a day, and the cost was tiny. A year later the job runs on a steady, heavy stream of images every hour of every day. A colleague says, "Serverless is always cheapest, so leave it." Without using any prices, explain when the colleague is right, when not, and what the team should do before deciding.

<details><summary>Model answer</summary>

Lambda's cost follows the work: requests plus memory times run time. For light or irregular work that is far cheaper than a server that bills every hour, used or not. But a server's cost is flat, so once the work is steady and heavy enough, a server, or Fargate, kept busy all the time can cost less, and commitments such as Savings Plans lower both. The colleague is right for spiky or light loads and may be wrong for a constant heavy one. Before deciding, the team should measure a month of real invocations and run time, price both options with the AWS Pricing Calculator, and count the cost of operations too: a server brings back patching and scaling work that Lambda removed. This is the cost optimization design principle "[Adopt a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)" applied with data, as [COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html) asks.

</details>

---

"Module 06 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
