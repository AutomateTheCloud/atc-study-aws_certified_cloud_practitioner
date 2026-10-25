---
type: check
id: clf-90-02
title: "Optional mixed set 1: Modules 02 to 05"
tasks: ["1.1", "1.2", "1.4", "2.1", "2.3", "3.1", "3.2", "3.4", "3.6", "4.1"]
objectives: []
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 05; about 45 minutes"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://aws.amazon.com/rds/faqs/"
---

# Optional mixed set 1: thirty questions across Modules 02 to 05, shuffled together

These thirty questions in the exam's style mix everything from the first four teaching modules, so each question makes you work out first what it's about. Mixing topics feels harder than a module's own check, but that harder practice is the kind that sticks.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): tasks [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1), [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2) and [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) and [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1), [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2), [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4) and [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

**For:** an adult studying alone, possibly new to IT, who has finished Modules 02 to 05. **Time:** about 45 minutes, plus time to go through the answer key.

> **Note:** This mixed set is optional practice for learners who want more questions before the practice exams; the main path and its hours leave it out.

## What this set assumes

You've finished [Module 02: Why organizations use the cloud](../02-why-the-cloud/00-brief.md), [Module 03: AWS around the world](../03-aws-around-the-world/00-brief.md), [Module 04: Who secures what](../04-shared-responsibility-and-access/00-brief.md) and [Module 05: Storing data](../05-storing-data/00-brief.md), and passed or retaken their mastery checks. Nothing here needs a later module; where a wrong choice names a service you haven't met yet, the right answer doesn't depend on it.

The set follows the tasks those four modules teach, in proportion to their weight on the exam: 9 questions on Domain 1 (Cloud Concepts), 9 on Domain 2 (Security and Compliance), 10 on Domain 3 (Cloud Technology and Services) and 2 on Domain 4 (Billing, Pricing, and Support), where these modules teach only storage pricing. Domain 4 gets its full share in [Mixed set 2](03-mixed-set-2.md) and [Mixed set 3](04-mixed-set-3.md). [How to use the exam preparation](01-how-to-use-exam-prep.md) explains where this set fits.

## How to take it

- **Closed book.** No lessons, notes or searching. The exam allows none of them.
- **Time yourself:** about 45 minutes for all 30, close to the exam's pace of 90 minutes for 65 questions.
- **Answer every question before you open the answer key.** On the exam there is no penalty for a wrong guess, so never leave one blank. Write your answers on paper as you go.
- **"(Select TWO.)"** means exactly two choices are right. As on the exam, the question scores only if you choose both.
- **Then score it by domain** with the table at the end, and reread the linked section for every question you missed or guessed.

## Questions

**1.** A natural history museum runs its collection catalog on Amazon EC2 instances with a Linux operating system, its ticket-booking code on AWS Lambda, and its donor database on Amazon RDS for PostgreSQL. A serious flaw is announced in the Linux kernel. Where must the museum's own staff install the fix?

- A. On the EC2 instances only
- B. On the EC2 instances and on the servers under the RDS database
- C. On the EC2 instances, the RDS database servers and the servers that run the Lambda code
- D. Nowhere, because AWS patches the operating system under every service

**2.** A puzzle-game studio in Canada sees its new game take off in Southeast Asia, where players complain of slow responses. Within a day, the studio is running a copy of its game servers in an AWS Region in that part of the world, without leasing space or shipping hardware. Which benefit of the AWS Cloud does this show most directly?

- A. Elasticity
- B. Durability
- C. Global reach
- D. Economies of scale

**3.** A transcription agency's servers save each finished transcript as a separate file. Customers download their own files through a web link from anywhere, the collection grows every day, and the agency doesn't want to plan or resize any storage capacity. Which AWS storage service fits best?

- A. Amazon EBS
- B. Amazon EFS
- C. EC2 instance store
- D. Amazon S3

**4.** An administrator at a climbing gym signs in as an IAM user with the AWS managed policy `AdministratorAccess`. The gym has one standalone AWS account. Which task will still require her to sign in as the account's root user?

- A. Moving the account from Basic Support to a paid Support plan
- B. Closing the account when the gym stops using AWS
- C. Creating an IAM role for the gym's booking application
- D. Setting a password policy for the gym's IAM users

**5.** A sensor-data startup stores 50 million small readings files of about 20 KB each in S3 Intelligent-Tiering, expecting the rarely read ones to move to cheaper tiers automatically. A year later, its storage cost per gigabyte hasn't fallen. What explains this?

- A. Intelligent-Tiering moves objects only when a lifecycle rule tells it to
- B. Intelligent-Tiering charges a retrieval fee every time a file is read
- C. Intelligent-Tiering keeps every object in a single Availability Zone
- D. Objects smaller than 128 KB are never moved to Intelligent-Tiering's cheaper access tiers, so they stay at the frequent-access rate

**6.** An esports league runs its tournament app in one AWS Region, spread across three Availability Zones. Which new requirement is the strongest reason to add a second Region?

- A. The app must keep running if one data center in the Region loses power
- B. The app must handle ten times its usual traffic during the finals
- C. The app's database must survive the loss of one Availability Zone
- D. A large new audience on another continent needs fast live scores

**7.** A courier startup moved all its systems to AWS a year ago and has kept every server at the size its busiest week needs, all year round. Its AWS bill is now higher than its old data center costs. Which change best fixes this while it stays on AWS?

- A. Scale capacity down outside the busy week, and resize servers to their measured use
- B. Keep peak capacity running, because cloud costs fall on their own after the first year
- C. Move every server to the Region closest to the startup's head office
- D. Run a second copy of each server in another Availability Zone

**8.** A seed bank that runs entirely on AWS sorts three items on its auditor's checklist: (1) badge readers and guards at the doors of the data center halls; (2) applying security patches; (3) keeping donor records only in an encrypted, restricted area that the seed bank designed. Under the AWS shared responsibility model, which kinds of control are these, in that order?

- A. Shared, shared, inherited
- B. Inherited, shared, customer-specific
- C. Inherited, customer-specific, shared
- D. Customer-specific, inherited, shared

**9.** A chain of board-game cafés is choosing databases for its new systems. Which TWO pairings of data and AWS database fit? (Select TWO.)

- A. A graph of which members play with which others, for game suggestions: Amazon Redshift
- B. Members, visits and payments in linked tables that need transactions: Amazon RDS
- C. Ten years of sales for complex analytical reports: Amazon ElastiCache
- D. The same menu page, read thousands of times a minute, in microseconds: Amazon Neptune
- E. Session data for millions of app users, always looked up by session ID: Amazon DynamoDB

**10.** A charity's IT team keeps its operating procedures as scripts in version control, makes small changes that are easy to undo, and holds a review after every incident to improve how it works. Which pillar of the AWS Well-Architected Framework do these practices belong to?

- A. Reliability
- B. Security
- C. Operational excellence
- D. Performance efficiency

**11.** A developer's IAM user has an identity-based policy that allows `s3:*` on all resources. The bucket `payroll-exports` has a bucket policy that explicitly denies `s3:DeleteObject` to every principal in the account. What happens when the developer tries to delete an object in that bucket?

- A. The delete succeeds, because the identity-based policy is broader
- B. The delete fails, because a bucket policy replaces the user's identity-based policies
- C. The delete succeeds, because bucket policies apply only to other accounts
- D. The delete fails, because an explicit deny overrides any allow

**12.** A broadcaster runs all its systems on servers in its own building. Virtualization software there lets its teams create virtual machines for themselves in minutes, and the vendor calls the setup a "private cloud". In the deployment models that AWS uses, what is this setup?

- A. Cloud
- B. Hybrid
- C. On-premises
- D. Community cloud

**13.** A satellite operator is writing requirements for the archive of its raw telemetry files. Which TWO requirements are about durability rather than availability? (Select TWO.)

- A. No file may be lost, even if several disks fail at once
- B. Engineers must be able to open any file at any hour of the day
- C. The archive must keep answering requests while one Availability Zone is down
- D. Every file must survive for fifteen years, through all the hardware failures in that time
- E. Downloads must start quickly for engineers on every continent

**14.** A dance school moves its MySQL database from an EC2 instance, where staff ran their own backup scripts, to Amazon RDS for MySQL. Which statement about backups after the move is accurate?

- A. AWS takes automated backups, and the school chooses how long to keep them
- B. Backups are no longer needed, because RDS stores data durably
- C. The school must still install backup software on the database server's operating system
- D. AWS keeps every automated backup for as long as the database exists

**15.** An engineering consultancy's design software, on computers in its office, saves drawings to a shared network folder. The consultancy wants the drawings stored durably in Amazon S3, recently used files to open quickly from a cache in the office, and no change to the software or to how staff save files. Which service fits?

- A. Amazon S3 File Gateway, part of AWS Storage Gateway
- B. AWS Elastic Disaster Recovery
- C. Amazon EBS volumes attached to the office computers
- D. AWS DataSync, run once to copy the folder

**16.** A finance student is summarizing why AWS can offer low pay-as-you-go prices. Which TWO statements about AWS's economies of scale are accurate? (Select TWO.)

- A. They remove a customer's need to match capacity to demand
- B. AWS combines the usage of a very large number of customers, so it buys and runs equipment at a scale no single customer could
- C. They lower the price of each unit of capacity, without changing the shape of a customer's demand curve
- D. They mean that a customer's total bill falls as its own usage grows
- E. They are the reason a customer can release servers after a seasonal peak

**17.** An outside auditing firm has its own AWS account. For two weeks, its staff must read log files kept in a ferry company's AWS account. The ferry company doesn't want to create or manage any passwords or long-term keys for them. What should the ferry company set up?

- A. An IAM user for each auditor, with a password and MFA
- B. An IAM role in its account that the auditing firm's account may assume, with read-only access to the logs
- C. One IAM user whose access keys all the auditors share
- D. Access to the root user for the two weeks, with MFA turned on

**18.** A craft brewery's order database is backed up to another AWS Region once a night, at 02:00, and the brewery keeps no other copy outside its main Region. The main Region fails at 18:00. In this failure, how much order data is lost, and which recovery measure describes that loss?

- A. About 16 hours of orders, a loss measured by the recovery time objective (RTO)
- B. No orders, because the backups copy every change as it happens
- C. About 16 hours of orders, a loss measured against the recovery point objective (RPO)
- D. About 2 hours of orders, a loss measured against the recovery point objective (RPO)

**19.** A wildlife charity's donation site normally runs on two servers. On the night of its yearly telethon it needs about forty for six hours, and then two again. The charity wants servers added and removed automatically as donations rise and fall. Which benefit of the AWS Cloud is it relying on?

- A. Elasticity
- B. Agility
- C. High availability
- D. Global reach

**20.** An architecture practice moves its shared project folders from a file server it ran in its own office to Amazon EFS. Under the AWS shared responsibility model, which TWO tasks move from the practice to AWS? (Select TWO.)

- A. Deciding which servers and staff may reach the file system
- B. Replacing failed disks in the storage hardware
- C. Classifying which project files hold clients' personal data
- D. Choosing whether the file system is encrypted
- E. Keeping copies of the data in several Availability Zones for a Regional file system

**21.** A laboratory's instrument software needs a relational database engine version that Amazon RDS doesn't offer, and the vendor's support contract requires a monitoring agent installed on the database server's own operating system. Which way of running the database fits?

- A. Amazon RDS with a Multi-AZ deployment
- B. Amazon Aurora
- C. Amazon DynamoDB
- D. The engine installed on an Amazon EC2 instance that the laboratory manages

**22.** A small design studio is moving its files to AWS and wants to forecast its storage bill. Which TWO statements about how these services charge are accurate? (Select TWO.)

- A. S3 Standard is billed for the space the bucket could hold, reserved in advance
- B. S3 Glacier Deep Archive has no minimum storage duration
- C. Reading data from S3 Standard-IA adds a charge for each gigabyte retrieved
- D. An EFS file system is billed for the capacity chosen when it was created
- E. An EBS volume is billed for its provisioned size, however much of it holds data

**23.** A furniture maker compares the cost of its own servers with AWS. It counts only the servers' purchase price, spread over five years. What should it add to make the comparison fair?

- A. The charge AWS makes for data transferred in from the internet
- B. The power, cooling, space, network and staff time its own servers need
- C. Nothing, because the purchase price is the whole cost of owning a server
- D. Only the hardware refresh, because running costs are the same in both places

**24.** A food bank's donation app on Amazon EC2 has its database password written into its source code, which several volunteers can read in a shared repository. Which change follows AWS's guidance?

- A. Store the password in AWS Secrets Manager, and let the app fetch it at run time through its IAM role
- B. Encrypt the source code file with S3 default encryption
- C. Replace the password with an IAM user's access keys written into the code
- D. Email the password to the app's maintainers and delete it from the code

**25.** A podcast network serves the same audio files to listeners around the world from an S3 bucket in one Region. Listeners far from that Region wait several seconds before playback starts. Which service uses edge locations to fix this?

- A. Amazon Route 53
- B. A copy of the bucket in a second Availability Zone
- C. An S3 Lifecycle rule that moves the files to a faster storage class
- D. Amazon CloudFront

**26.** A team lead wants to review one of her team's workloads against the AWS Well-Architected Framework. She wants an AWS service in the console that walks the team through each pillar's questions, records their answers, and lists the risks found with an improvement plan. Which service is that?

- A. AWS Trusted Advisor
- B. AWS Well-Architected Tool
- C. AWS Config
- D. AWS Artifact

**27.** A hiking club serves its trail maps from a web server that it runs on an EC2 instance. It moves the maps into an Amazon S3 bucket that its website reads from, and deletes the instance. Which task does the club no longer have?

- A. Deciding who may read the maps
- B. Keeping Block Public Access and the bucket policy set correctly
- C. Patching the web server's operating system
- D. Deciding which maps to publish, and keeping them accurate

**28.** A ticket marketplace's Amazon RDS database is overloaded by read-only queries, many of them for the same event listings, requested again and again. Which TWO changes take read work off the primary database? (Select TWO.)

- A. Add an Amazon ElastiCache cache in front of the database for the repeated listings
- B. Turn on a Multi-AZ DB instance deployment and send the reads to its standby
- C. Move the database into Amazon Redshift
- D. Add a read replica and point the read-only queries at it
- E. Increase the automated backup retention period

**29.** A small travel startup used to wait six weeks for each new server to be ordered and installed. On AWS it gets servers in minutes, so it now tries a new feature idea every week and deletes the ones that fail. Which benefit of the AWS Cloud does this describe?

- A. Elasticity
- B. High availability
- C. Economies of scale
- D. Agility

**30.** A game studio's build servers, all in one Availability Zone, share a folder of intermediate build files over NFS. If the files are lost, they can be rebuilt from source in an hour. The studio wants the lowest-cost managed option. Which storage fits?

- A. Amazon EFS with One Zone storage
- B. Amazon EFS with Regional storage
- C. Amazon FSx for Windows File Server
- D. S3 Glacier Deep Archive

## Answer key

Open the key only when you've answered every question.

<details><summary>Answer key</summary>

**1. A** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). On EC2 the guest operating system is the customer's, so the museum patches it. On RDS, AWS patches the operating system and the database software, and on Lambda AWS patches the servers and the managed runtimes, so B and C hand the museum work that is AWS's. D forgets that EC2 leaves the guest operating system with the customer. Reread: [Lesson 04.01, Security of the cloud vs security in the cloud, "The line moves with the service: EC2, RDS, Lambda and S3"](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3).

**2. C** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). What changed is the place: in a day, the studio runs close to its new players. Elasticity changes capacity with demand in the same place, durability is about not losing stored data, and economies of scale lower the price of each unit, so none of them describes moving closer to users. Reread: [Lesson 02.03, Telling the benefits apart, "Global reach: run close to users anywhere, in minutes"](../02-why-the-cloud/03-telling-the-benefits-apart.md#global-reach-run-close-to-users-anywhere-in-minutes).

**3. D** · Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). Whole files fetched over the web, growing with no capacity to plan, is the pattern for object storage, and S3 is AWS's object store. EFS also grows on its own, but servers mount it as a shared folder over NFS; customers don't download from it through a web link. EBS is a disk sized in advance for one server, and instance store is temporary. Reread: [Lesson 05.01, Block, file and object storage, "Object storage: whole objects in a bucket, reached over the web"](../05-storing-data/01-block-file-object.md#object-storage-whole-objects-in-a-bucket-reached-over-the-web).

**4. B** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Closing the account changes the account itself, which is the pattern of root-only tasks. Changing the Support plan is the familiar trap: AWS's current list of root-only tasks doesn't include it (checked 2026-10-23). Creating roles and setting the password policy are ordinary IAM work that `AdministratorAccess` allows. Reread: [Lesson 04.03, Identities, "Only the root user can do a short list of tasks"](../04-shared-responsibility-and-access/03-identities.md#only-the-root-user-can-do-a-short-list-of-tasks).

**5. D** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). Intelligent-Tiering moves objects between tiers by how often they are read, but objects under 128 KB are never moved to the cheaper tiers, so millions of tiny files see no saving (checked 2026-10-23). It charges no retrieval fee, keeps data in three or more Availability Zones, and moves objects on its own, without lifecycle rules. Reread: [Lesson 05.02, S3 protection, storage classes and lifecycle, "Storage classes: how often, how fast, how replaceable"](../05-storing-data/02-s3-in-practice.md#storage-classes-how-often-how-fast-how-replaceable).

**6. D** · Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). Low latency for users far from the current Region is one of the reasons the exam guide gives for using more than one Region, with disaster recovery, business continuity and data sovereignty. Losing a data center or an Availability Zone is already covered by running in three Availability Zones, and a traffic spike is a job for scaling inside the Region. Reread: [Lesson 03.02, Choosing a Region, "Use more than one Region only when you have a reason"](../03-aws-around-the-world/02-choosing-a-region.md#use-more-than-one-region-only-when-you-have-a-reason).

**7. A** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). The cloud turns fixed costs into variable ones, but the bill falls only when capacity follows demand and unused capacity is removed; rightsizing to measured use does the rest. Costs don't fall on their own (B). Moving Regions removes no idle capacity, and a second copy in another Availability Zone adds cost to buy high availability. Reread: [Lesson 02.04, What a data center really costs, "Moving to the cloud doesn't automatically lower costs"](../02-why-the-cloud/04-what-a-data-center-really-costs.md#moving-to-the-cloud-doesnt-automatically-lower-costs).

**8. B** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). Physical security of AWS's buildings is an inherited control: AWS does all of it, and the seed bank shows AWS's audit reports as evidence. Patch management is a shared control: AWS patches its infrastructure and the seed bank patches what it runs. A protected area that the customer designed for its own data is customer-specific, because only what the seed bank builds can provide it. Reread: [Lesson 04.02, Shared, inherited and customer-specific controls, "The big picture: three kinds of control"](../04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md#the-big-picture-three-kinds-of-control).

**9. B and E** · Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). Linked tables with transactions are the shape for a relational database such as RDS, and items fetched by key at any scale are DynamoDB's. The other three are swapped: relationships fit Neptune, years of analytical reports fit the Redshift data warehouse, and repeated reads in microseconds fit the ElastiCache in-memory cache. Reread: [Lesson 05.05, Managed databases and choosing one, "The database services side by side"](../05-storing-data/05-managed-or-self-managed-databases.md#the-database-services-side-by-side).

**10. C** · Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Running the workload well and improving how the team works, through operations as code, small reversible changes and learning from incidents, is the operational excellence pillar's question. Reliability is tempting because incidents are involved, but it asks whether the workload works and recovers from failure, not how the team runs and improves its procedures. Reread: [Lesson 02.05, The Well-Architected Framework, "Six pillars, six questions"](../02-why-the-cloud/05-the-well-architected-framework.md#six-pillars-six-questions).

**11. D** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). AWS evaluates identity-based and resource-based policies together, and an explicit deny in any of them wins over every allow. B has the right outcome for the wrong reason: a bucket policy doesn't replace identity-based policies; both count. Bucket policies apply to principals in the same account as well as in other accounts, so C is wrong. Reread: [Lesson 04.04, Policies and least privilege, "How AWS decides: default deny, then allows, then an explicit deny wins"](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md#how-aws-decides-default-deny-then-allows-then-an-explicit-deny-wins).

**12. C** · Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). AWS names three deployment models, cloud, hybrid and on-premises, and you classify a setup by where each part runs. Everything here runs in the broadcaster's own building, so it is on-premises, whatever the vendor calls it. Hybrid would need some parts in the cloud, and "community" (like "private") belongs to a different vocabulary that AWS doesn't use. Reread: [Lesson 02.01, What cloud computing is, "The three deployment models are cloud, hybrid and on-premises"](../02-why-the-cloud/01-what-cloud-computing-is.md#the-three-deployment-models-are-cloud-hybrid-and-on-premises).

**13. A and D** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Durability asks whether stored data is ever lost, now or years from now, so A and D are about it. Opening files at any hour and staying up through an Availability Zone outage are availability: the data can be safe yet briefly out of reach. Fast downloads everywhere are about global reach and performance. Reread: [Lesson 02.03, Telling the benefits apart, "Durability: stored data isn't lost"](../02-why-the-cloud/03-telling-the-benefits-apart.md#durability-stored-data-isnt-lost).

**14. A** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). With RDS, AWS runs the backup machinery: automated backups that allow a restore to any second in the retention period, which the school sets. Durable storage doesn't undo a wrong delete, so backups are still needed (B). The school has no access to the operating system under RDS (C), and automated backups are kept only for the retention period (D). Reread: [Lesson 05.05, Managed databases and choosing one, "Backups and snapshots take you back in time"](../05-storing-data/05-managed-or-self-managed-databases.md#backups-and-snapshots-take-you-back-in-time).

**15. A** · Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). S3 File Gateway presents a shared folder on the office network, keeps a local cache of recent files, and stores each file as an object in S3, so the software keeps working unchanged. Elastic Disaster Recovery keeps whole servers ready to launch, EBS volumes attach only to EC2 instances in AWS, and DataSync moves data once (or on a schedule) rather than serving a folder people keep working in. Reread: [Lesson 05.04, Hybrid storage and backup, "Storage Gateway lets on-premises software use AWS storage without changing"](../05-storing-data/04-hybrid-storage-and-backup.md#storage-gateway-lets-on-premises-software-use-aws-storage-without-changing).

**16. B and C** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Combining the usage of many customers lowers AWS's cost of each unit, and AWS says this leads to lower pay-as-you-go prices. Scale changes the price per unit, not the curve: following demand and releasing servers after a peak come from paying by use and elasticity (A, E). A customer's bill still grows with its usage, even where some rates fall with volume (D). Reread: [Lesson 02.02, Before and after: the demand curve, "Economies of scale: a very large provider can charge less per unit"](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#economies-of-scale-a-very-large-provider-can-charge-less-per-unit).

**17. B** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). A cross-account IAM role gives the auditors temporary credentials, issued only when they assume the role from their own account, and the ferry company removes the trust when the work ends. IAM users mean long-term passwords or keys to manage, and shared keys also lose track of who did what. The root user is never handed out. Reread: [Lesson 04.05, Credentials and federation, "Federation: sign in once, elsewhere, and receive temporary access"](../04-shared-responsibility-and-access/05-credentials-and-federation.md#federation-sign-in-once-elsewhere-and-receive-temporary-access).

**18. C** · Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). RPO is about data loss: the most data you accept losing, measured back from the failure to the last good copy. Here everything written since the 02:00 backup is gone, about 16 hours, and with nightly backups a failure just before 02:00 could cost almost a day. RTO is a different measure: how long the brewery can be down. A nightly backup is a point-in-time copy, not continuous replication, so B is wrong. Reread: [Lesson 03.03, Surviving failure, "RTO and RPO: how long you can be down, and how much you can lose"](../03-aws-around-the-world/03-surviving-failure.md#rto-and-rpo-how-long-you-can-be-down-and-how-much-you-can-lose).

**19. A** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Capacity that grows and shrinks with demand, automatically, is elasticity. Agility is about how fast you can get something new and try ideas, high availability is about surviving a failure, and global reach is about running close to users in other places. Reread: [Lesson 02.03, Telling the benefits apart, "Elasticity: capacity grows and shrinks with demand"](../02-why-the-cloud/03-telling-the-benefits-apart.md#elasticity-capacity-grows-and-shrinks-with-demand).

**20. B and E** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). AWS runs the storage hardware, replaces failed disks and, for a Regional file system, keeps the data in several Availability Zones. Who may reach the file system, which data is sensitive and whether it is encrypted are settings and data, and those stay with the customer on every service. Reread: [Lesson 05.01, Block, file and object storage, "Your side of the line"](../05-storing-data/01-block-file-object.md#your-side-of-the-line).

**21. D** · Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). AWS recommends a managed database unless there is a real reason not to, and an engine version RDS doesn't offer, plus a need for the operating system itself, are such reasons. On EC2 the operating system, patches, backups and failover then become the laboratory's. RDS and Aurora give no access to the server's operating system, and DynamoDB isn't relational. Reread: [Lesson 05.05, Managed databases and choosing one, "AWS recommends a managed database unless you have a reason not to"](../05-storing-data/05-managed-or-self-managed-databases.md#aws-recommends-a-managed-database-unless-you-have-a-reason-not-to).

**22. C and E** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). EBS bills the size you provision, full or empty, so it behaves like a small fixed cost, and the infrequent-access classes add a per-gigabyte retrieval fee. S3 and EFS bill for what you actually store, with no capacity chosen in advance, and Deep Archive bills a minimum stay of 180 days (checked 2026-10-23). Reread: [Lesson 05.01, Block, file and object storage, "What you pay for"](../05-storing-data/01-block-file-object.md#what-you-pay-for).

**23. B** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Owning servers costs far more than their price: hardware and its refresh, space, power, cooling, network, staff and licenses, most of them fixed. Data transfer in from the internet is free on AWS (A), and running costs such as power and staff are exactly what differs between the two (D). Reread: [Lesson 02.04, What a data center really costs, "On-premises costs come in seven groups"](../02-why-the-cloud/04-what-a-data-center-really-costs.md#on-premises-costs-come-in-seven-groups).

**24. A** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Application secrets belong in a store such as Secrets Manager, which can also rotate them, and the app reaches the store with temporary credentials from its IAM role. Encryption at rest doesn't stop people who can read the repository from seeing the password (B), and access keys in code are a long-term secret in the same wrong place (C). Reread: [Lesson 04.05, Credentials and federation, "Your application's secrets belong in a store, not in the code"](../04-shared-responsibility-and-access/05-credentials-and-federation.md#your-applications-secrets-belong-in-a-store-not-in-the-code).

**25. D** · Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). CloudFront caches copies of content at edge locations near listeners, so most requests are answered nearby instead of from the faraway Region. Route 53 tells users where to go but delivers no content; it isn't a content delivery network. Availability Zones and storage classes are all inside the same faraway Region, so they bring nothing closer. Reread: [Lesson 03.04, The edge, "Three services use the edge, each in its own way"](../03-aws-around-the-world/04-the-edge.md#three-services-use-the-edge-each-in-its-own-way).

**26. B** · Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). The Well-Architected Tool is the service that applies the Framework to one workload: a guided review of each pillar's questions that records risks and an improvement plan. Trusted Advisor runs automated checks of your account's settings, a different service; Config records how resources are set, and Artifact provides AWS's audit reports. Reread: [Lesson 02.05, The Well-Architected Framework, "The Framework is guidance; the Well-Architected Tool applies it"](../02-why-the-cloud/05-the-well-architected-framework.md#the-framework-is-guidance-the-well-architected-tool-applies-it).

**27. C** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). With S3, AWS runs everything under the data, including the servers and their operating systems, so the patching the club did on EC2 is gone. The data, and who can reach it, stay with the customer on every service, so A, B and D are still the club's. Reread: [Lesson 04.01, Security of the cloud vs security in the cloud, "Your data, and who can reach it, are always yours"](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#your-data-and-who-can-reach-it-are-always-yours).

**28. A and D** · Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). A cache answers the repeated reads from memory, and a read replica serves read-only queries from its own copy, so both relieve the primary. The standby of a Multi-AZ DB instance deployment serves no queries; it exists only to take over. Redshift is a warehouse for analysis, not a site's working database, and backups don't answer queries. Reread: [Lesson 05.05, Managed databases and choosing one, "A read replica takes read-only work off the primary"](../05-storing-data/05-managed-or-self-managed-databases.md#a-read-replica-takes-read-only-work-off-the-primary).

**29. D** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Getting something new in minutes instead of weeks, and so being able to try ideas cheaply, is agility. Elasticity is capacity following demand, high availability is surviving failure, and economies of scale lower the price per unit; none of them is about how fast you can try something new. Reread: [Lesson 02.03, Telling the benefits apart, "Agility: getting something new takes minutes, not weeks"](../02-why-the-cloud/03-telling-the-benefits-apart.md#agility-getting-something-new-takes-minutes-not-weeks).

**30. A** · Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). EFS is AWS's shared NFS file system, and One Zone storage keeps the data in a single Availability Zone for less, a fair trade for files that can be rebuilt. Regional storage pays for copies in other Availability Zones that the studio doesn't need, FSx for Windows File Server is the Windows and SMB answer, and Deep Archive is an archive, not a shared folder. Reread: [Lesson 05.01, Block, file and object storage, "File storage: one folder tree that many servers share"](../05-storing-data/01-block-file-object.md#file-storage-one-folder-tree-that-many-servers-share).

</details>

## Score by domain

Count your correct answers in each domain and find your band. The bands say what to do next, not how you'd do on the exam.

| Domain | Share of the exam | Questions in this set | Restudy (below 60%) | Review the linked sections (60–79%) | Ready on this domain (80% or more) |
|---|---|---|---|---|---|
| 1 Cloud Concepts | 24% | 9: 2, 7, 10, 13, 16, 19, 23, 26, 29 | 0 to 5 | 6 to 7 | 8 to 9 |
| 2 Security and Compliance | 30% | 9: 1, 4, 8, 11, 14, 17, 20, 24, 27 | 0 to 5 | 6 to 7 | 8 to 9 |
| 3 Cloud Technology and Services | 34% | 10: 3, 6, 9, 12, 15, 18, 21, 25, 28, 30 | 0 to 5 | 6 to 7 | 8 to 10 |
| 4 Billing, Pricing, and Support | 12% | 2: 5, 22 | 0 to 1 | (none) | 2 |

**With so few questions, read the bands as pointers.** One miss in Domain 4 moves you from 100% to 50%. A domain in the restudy band means: reread the lessons the answer key links to, then retake that module's mastery check, before you go on to Module 06. In the review band, reread only the linked sections for the questions you missed.

**A practice score is not a prediction of an exam score.** This set is a learning tool: it shows which ideas you can tell apart today. The real exam reports a scaled score from 100 to 1,000 on questions you haven't seen, and its mix of questions differs from form to form ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md)). Readiness is judged later, on the two practice exams, taken unseen.

Next: [Module 06: Running applications](../06-running-applications/00-brief.md).

---

"Optional mixed set 1: Modules 02 to 05" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
