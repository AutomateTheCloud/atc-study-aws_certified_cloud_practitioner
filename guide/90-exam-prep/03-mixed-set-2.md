---
type: check
id: clf-90-03
title: "Mixed set 2: Modules 02 to 09"
tasks: ["1.1", "1.2", "1.4", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.8", "4.1"]
objectives: []
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 09; about 45 minutes"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html"
  - "https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
---

# Mixed set 2: thirty questions across Modules 02 to 09, shuffled together

These thirty questions in the exam's style draw on everything up to the end of Module 09 and are mixed so that no two questions in a row come from the same place. Each one makes you decide first what it's about, and on the real exam that's most of the work.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): tasks [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1), [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2) and [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4); [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1), [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2), [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1), [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2), [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3), [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4), [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5), [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6) and [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

**For:** an adult studying alone, possibly new to IT, who has finished Modules 02 to 09. **Time:** about 45 minutes, plus time to go through the answer key.

## What this set assumes

You've finished Modules [02](../02-why-the-cloud/00-brief.md), [03](../03-aws-around-the-world/00-brief.md), [04](../04-shared-responsibility-and-access/00-brief.md), [05](../05-storing-data/00-brief.md), [06](../06-running-applications/00-brief.md), [07](../07-connecting-it/00-brief.md), [08](../08-building-and-operating/00-brief.md) and [09](../09-protecting-and-governing/00-brief.md), and their mastery checks. [Mixed set 1](02-mixed-set-1.md) covered Modules 02 to 05; this set leans on Modules 06 to 09 but keeps the earlier ones in play, because the exam does.

The set is weighted by the exam's domains: 7 questions on Domain 1 (Cloud Concepts), 9 on Domain 2 (Security and Compliance), 10 on Domain 3 (Cloud Technology and Services) and 4 on Domain 4 (Billing, Pricing, and Support). Modules 02 to 09 teach only the pricing part of Domain 4, so its 4 questions are all about how storage, compute and networking are charged; billing tools and Support plans come in Modules 11 and 12, and in [Mixed set 3](04-mixed-set-3.md). Analytics, AI and migration are left for Mixed set 3 too. [How to use the exam preparation](01-how-to-use-exam-prep.md) explains where this set fits.

## How to take it

- **Closed book.** No lessons, notes or searching.
- **Time yourself:** about 45 minutes for all 30, close to the exam's pace of 90 minutes for 65 questions.
- **Answer every question before you open the answer key.** There is no penalty for a wrong guess on the exam, so never leave one blank. Write your answers on paper as you go.
- **"(Select TWO.)"** means exactly two choices are right. As on the exam, the question scores only if you choose both.
- **Then score it by domain** with the table at the end, and reread the linked section for every question you missed or guessed.

## Questions

**1.** Before an audit, a regional airline's security officer needs one list of every IAM user in the account, showing whether each user has MFA turned on and when each password and access key was last used. Which AWS feature produces it?

- A. AWS CloudTrail event history
- B. AWS Config rules
- C. Amazon Inspector
- D. The IAM credential report

**2.** A traffic-camera company runs a containerized program that reads a live video stream and must keep running for hours at a time. The team doesn't want to manage any servers, and the program needs no GPU. Which option fits?

- A. AWS Lambda
- B. Amazon ECR
- C. Amazon EC2 instances that the team manages
- D. Amazon ECS on AWS Fargate

**3.** A logistics company builds the same environment for each of its regional offices. It moves from building each one by hand in the console to one AWS CloudFormation template kept in version control. Which TWO benefits can it expect? (Select TWO.)

- A. Each office's environment comes out identical, with fewer manual mistakes
- B. The template also copies each environment's data to the new offices
- C. Nobody can change a resource by hand once a template has created it
- D. Every resource that a template creates is free of charge
- E. Staff spend less time on each new environment, and a whole environment can be deleted in one step

**4.** A retail group has more than forty AWS accounts in AWS Organizations and opens new accounts every month. Its security team wants the same AWS WAF rules and security group policies applied in every account, including the new ones, from one place. Which service fits?

- A. AWS Shield Advanced
- B. AWS Firewall Manager
- C. Amazon GuardDuty
- D. AWS Config

**5.** A university runs 15 VPCs, one for each faculty, and adds more every year. Every VPC must reach a shared services VPC, several must reach each other, and all must reach the campus network through one VPN. The team finds that pairwise connections have become impossible to manage. Which service fits?

- A. VPC peering between every pair of VPCs
- B. AWS PrivateLink
- C. AWS Transit Gateway
- D. AWS Client VPN

**6.** A concert promoter's ticket site uses an EC2 Auto Scaling group with a target tracking policy that keeps average processor use near 50%. When a famous band's tickets go on sale, the group grows from 4 instances to 30, then shrinks back to 4 by evening. Which benefit does this show, and which part provides it?

- A. High availability, provided by the load balancer
- B. Elasticity, provided by EC2 Auto Scaling
- C. Agility, provided by AWS CloudFormation
- D. Elasticity, provided by Elastic Load Balancing

**7.** A freelance designer runs her portfolio site on an Amazon Lightsail instance. She stops the instance for a two-month break, expecting the charges to stop too. What happens to the charge, and how does she end it?

- A. The plan price stops while the instance is stopped, as for EC2 instance hours
- B. Lightsail charges only for the days on which the site has visitors
- C. Only the data transfer allowance is charged while the instance is stopped
- D. The plan price keeps running while the instance exists; she ends it by deleting the instance, after taking a snapshot if she needs it

**8.** A bike-share company has three sign-in needs: its 30 staff must sign in once and reach five AWS accounts; riders must sign in to its mobile app; and a nightly program on an EC2 instance must write to an Amazon DynamoDB table. Which choice matches the three needs, in that order?

- A. IAM users in each account; Amazon Cognito; access keys stored on the instance
- B. Amazon Cognito; AWS IAM Identity Center; an IAM role for the instance
- C. AWS IAM Identity Center; Amazon Cognito; an IAM role for the instance
- D. AWS IAM Identity Center; an IAM user for each rider; the root user's access keys

**9.** When a customer books a ride with a regional coach company, three things must happen at once: a message goes into the dispatch team's work queue, a function updates the seat map, and the duty manager gets an email alert. The booking code should send just one message. Which service should receive it?

- A. An Amazon SNS topic with three subscriptions
- B. One Amazon SQS queue
- C. Amazon SES
- D. AWS Step Functions

**10.** A software company tags every resource with the team that owns it, shows each team its own monthly spending, and asks each team to explain any increase in its costs. Which pillar of the AWS Well-Architected Framework do these practices serve most directly?

- A. Reliability
- B. Sustainability
- C. Performance efficiency
- D. Cost optimization

**11.** An auditor finds that a clinic's patient portal sends patient details between browsers and its Application Load Balancer as plain HTTP. The portal's database is already encrypted at rest with an AWS KMS key. Which change fixes the finding?

- A. Add an HTTPS listener with a certificate from AWS Certificate Manager, and redirect HTTP to HTTPS
- B. Switch the database to a customer managed KMS key
- C. Turn on Amazon Macie for the portal's S3 buckets
- D. Move the encryption keys into AWS CloudHSM

**12.** An engineer is deciding what may live on the instance store volumes of an EC2 instance. Which TWO kinds of data are safe to keep there? (Select TWO.)

- A. The only copy of files that customers upload
- B. A cache of images that can be rebuilt from Amazon S3 if it is lost
- C. The files of a database that must survive a stop and a start
- D. The operating system of a server that is stopped every night
- E. Temporary working files of a batch job that is simply rerun if it fails

**13.** A language-learning company moves its app from containers on EC2 instances it managed to Amazon ECS on AWS Fargate. Which TWO tasks are still the company's? (Select TWO.)

- A. Patching the operating system of the servers that run the containers
- B. Rebuilding its container images when a library inside them has a security flaw
- C. Choosing how many servers the cluster needs
- D. Granting the app only the permissions it needs through its IAM task role
- E. Maintaining the physical hosts in AWS data centers

**14.** A university's teaching labs use 60 EC2 instances, but only during class hours on weekdays in term time. The instances run around the clock all year. Which change cuts the cost most while keeping the labs ready for classes?

- A. Move the instances to a Region with more Availability Zones
- B. Automate stopping the instances outside class hours, and starting them before classes
- C. Replace the instances with larger ones so fewer are needed
- D. Keep them running, because an idle instance isn't billed

**15.** A video-tutorial company's monthly AWS bill shows its data transfer charges doubling since spring, although its storage and instance costs are flat. Which change in its business would most likely explain this?

- A. Instructors are uploading twice as many new videos from the internet
- B. Its web servers now read video files from an S3 bucket in the same Region twice as often
- C. Twice as many viewers are streaming its videos from its servers over the internet
- D. Its EC2 instances now exchange twice as much data within one Availability Zone, over private addresses

**16.** A parcel-tracking service keeps a smaller copy of its whole application running at all times in a second AWS Region, with its data copied there continuously. If the main Region fails, the service scales that copy up and moves traffic to it within minutes. Which disaster recovery strategy is this?

- A. Backup and restore
- B. Pilot light
- C. Warm standby
- D. Multi-site active/active

**17.** A newly hired cloud administrator keeps running into common how-to questions, such as how to find out who deleted a resource or how to rotate an access key. She wants AWS's own step-by-step articles that answer frequent questions like these. Where should she look?

- A. The AWS Knowledge Center, on AWS re:Post
- B. AWS Artifact
- C. AWS Security Hub
- D. The AWS Health Dashboard

**18.** An events company's ticket site now runs on two EC2 instances in two Availability Zones behind a load balancer. Its manager says, "Now we're elastic." Which reply is accurate?

- A. Yes: running in two Availability Zones is what elasticity means
- B. No: two Availability Zones give durability, which protects only stored data
- C. Not yet: two Availability Zones give high availability; elasticity needs capacity that grows and shrinks with demand, for example through Auto Scaling
- D. No: elasticity is possible only across two or more Regions

**19.** A health-tech startup's compliance officer is learning what AWS Artifact offers. Which TWO statements are accurate? (Select TWO.)

- A. It checks the startup's resources against a compliance standard and marks each one pass or fail
- B. It provides AWS's own audit reports, such as SOC reports, at no cost
- C. It certifies the startup's own workload as compliant
- D. It records every API call made in the startup's account
- E. It lets the startup review and accept agreements with AWS, such as the Business Associate Addendum

**20.** Instances in a private subnet send several terabytes a month to an S3 bucket in the same Region through a NAT gateway, and the NAT gateway's per-gigabyte charges now dominate the network bill. The instances must stay private. Which change removes those charges for the S3 traffic?

- A. Move the instances to a public subnet with an internet gateway
- B. Replace the NAT gateway with an interface VPC endpoint for every AWS service
- C. Add a gateway VPC endpoint for S3 and a route to it in the private route table
- D. Give each instance an Elastic IP address

**21.** A team builds a full-size copy of its production environment for one day of load testing, then deletes it. Which general design principle of the AWS Well-Architected Framework does this follow?

- A. Test systems at production scale
- B. Design for failure
- C. Think parallel
- D. Geographic diversity

**22.** A sports club's new treasurer finds that the root user of the club's AWS account has an access key, has no MFA, and is used every week to read the bills. Which TWO changes should come first? (Select TWO.)

- A. Turn on MFA for the root user
- B. Attach an IAM policy to the root user that limits what it can do
- C. Delete the root user's access key
- D. Keep reading the bills as root, but change the root password every month
- E. Rename the root user so that attackers can't guess it

**23.** A grocery chain wants to run complex SQL reports across ten years of sales from all its stores, joined with its loyalty-card data, without slowing the database that runs its checkout systems. Which service fits?

- A. Amazon DynamoDB
- B. Amazon ElastiCache
- C. Amazon Neptune
- D. Amazon Redshift

**24.** A small archive's nightly job resizes new scans and runs for about two minutes a night. Today it runs on an EC2 instance that is on around the clock. Why would AWS Lambda probably cost less for this job?

- A. Lambda bills per request and for the time the code runs, so nothing is charged while the job is idle
- B. Lambda is free for every workload that runs less than an hour a day
- C. Lambda functions run on reserved hardware at a fixed monthly price
- D. Lambda includes the EC2 instance's hours at a discount

**25.** An online bookshop's website sits behind Amazon CloudFront. Which statement correctly divides the work of protecting it between AWS and the bookshop?

- A. AWS turns on AWS WAF rules against SQL injection for every CloudFront site; the bookshop handles network floods
- B. AWS protects it against common network floods with AWS Shield Standard, at no charge; writing AWS WAF rules against harmful requests, such as SQL injection, is the bookshop's job
- C. AWS Shield Advanced is included with CloudFront, so the bookshop has nothing to configure
- D. The bookshop must subscribe to AWS Shield before any DDoS protection applies

**26.** A quiz app gets bursts of traffic during live TV shows and almost none at other times. Its team wants the database bill to follow use, paying per request rather than for capacity set in advance, with no servers to manage. Which choice fits?

- A. Amazon DynamoDB in on-demand capacity mode
- B. Amazon RDS on a DB instance sized for the busiest show
- C. A database installed on an EC2 instance that runs all the time
- D. Amazon Redshift

**27.** Customers of an online plant nursery report that checkout is sometimes slow. A checkout request passes through Amazon API Gateway, three AWS Lambda functions and an Amazon DynamoDB table. The team wants to follow single slow requests through every part to see which one causes the delay. Which service fits?

- A. AWS CloudTrail
- B. AWS Config
- C. Amazon CloudWatch alarms
- D. AWS X-Ray

**28.** To be ready "just in case", a team gives a public IPv4 address to each of its database instances in private subnets, whose route tables have no route to an internet gateway. What is the effect?

- A. The databases become reachable from the internet
- B. The addresses do nothing useful, but each one is billed by the hour
- C. The subnets become public subnets
- D. The addresses cost nothing, because no traffic uses them

**29.** A web application runs on EC2 instances in an Auto Scaling group across two Availability Zones, behind an Application Load Balancer. Which TWO are jobs of the load balancer rather than of Auto Scaling? (Select TWO.)

- A. Launching new instances from a launch template when demand rises
- B. Replacing an instance that fails its health checks
- C. Sending each incoming request to a healthy instance
- D. Keeping the number of instances between a minimum and a maximum
- E. Giving users one address that spreads their requests across both Availability Zones

**30.** A developer is writing an order-tracking application. Each time a customer uploads a delivery photo, the application itself must store the photo in Amazon S3. Which way of working with AWS fits?

- A. The AWS Management Console
- B. An AWS SDK called from the application's code
- C. An AWS CloudFormation template
- D. The AWS CLI, run by hand when photos arrive

## Answer key

Open the key only when you've answered every question.

<details><summary>Answer key</summary>

**1. D** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). The credential report is one of IAM's access reports: a list of the account's users with the state of their passwords, access keys and MFA, including when each credential was last used. CloudTrail event history shows individual actions, not a summary of each user's credentials, Config judges resource settings against rules, and Inspector scans workloads for software flaws and network exposure. Reread: [Lesson 09.01, Who did what, how it runs, how it was set, "Access reports show who can do what, and whether they still use it"](../09-protecting-and-governing/01-who-did-what.md#access-reports-show-who-can-do-what-and-whether-they-still-use-it).

**2. D** · Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). Fargate runs containers without servers to manage, for as long as a task keeps running, so it suits a container that runs for hours. Lambda is for short, event-driven work, with a limit of 15 minutes per invocation. EC2 instances would work but leave the servers with the team, and ECR only stores container images. Reread: [Lesson 06.03, Containers and serverless, "Lambda or Fargate: short event-driven work, or containers that keep running"](../06-running-applications/03-containers-and-serverless.md#lambda-or-fargate-short-event-driven-work-or-containers-that-keep-running).

**3. A and E** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Automation makes the work repeatable and cheaper: identical copies, fewer mistakes, less staff time and clean deletion of a whole stack. A template rebuilds resources, not their data, which travels by backups or replication. People can still change resources by hand, which drift detection reports, and the resources a stack creates are billed as usual. Reread: [Lesson 08.01, Four ways in, and infrastructure as code, "Automation makes work repeatable and cheaper"](../08-building-and-operating/01-four-ways-in.md#automation-makes-work-repeatable-and-cheaper).

**4. B** · Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Firewall Manager applies WAF rules, Shield Advanced protections and security group policies across the accounts of an organization, and covers new accounts as they join. Shield Advanced protects against DDoS attacks but doesn't spread rules across accounts, GuardDuty detects threats, and Config records and judges settings rather than applying firewall rules. Reread: [Lesson 09.04, The front door, "Firewall Manager applies the same protections in every account"](../09-protecting-and-governing/04-the-front-door.md#firewall-manager-applies-the-same-protections-in-every-account).

**5. C** · Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). Transit Gateway is a hub: each VPC and the VPN attach to it once, and its route tables decide which networks reach which. Peering joins exactly two VPCs and isn't transitive, so a mesh of them grows with every new VPC. PrivateLink exposes one service rather than joining networks, and Client VPN connects individual people's devices. Reread: [Lesson 07.04, Connecting networks and offices, "Peering, Transit Gateway and PrivateLink connect networks inside AWS"](../07-connecting-it/04-connecting-networks-and-offices.md#peering-transit-gateway-and-privatelink-connect-networks-inside-aws).

**6. B** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Capacity that follows demand up and down, automatically, is elasticity, and the Auto Scaling group is what changes the number of instances. The load balancer spreads requests across the healthy instances, however many there are, which supports high availability; it doesn't add or remove instances, so D names the wrong part. Reread: [Lesson 06.02, Auto Scaling and load balancers, "Auto Scaling changes how many; the load balancer chooses which"](../06-running-applications/02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which).

**7. D** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). Lightsail charges an instance's plan price while it is running or stopped; only deleting the instance ends the charge, so she should keep a snapshot first if she wants to restore the site later. This differs from EC2, where a stopped instance doesn't bill instance hours, though its disk and public IPv4 address still do. Reread: [Lesson 06.04, Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts, "Lightsail sells a simple server as a bundle with a predictable price"](../06-running-applications/04-simpler-paths.md#lightsail-sells-a-simple-server-as-a-bundle-with-a-predictable-price).

**8. C** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Identity Center gives a workforce one sign-in across many accounts, Cognito handles sign-in for an application's own customers, and a role gives a program on EC2 temporary credentials with no keys to store. B swaps the first two, and A and D rely on long-term credentials where AWS recommends temporary ones. Reread: [Lesson 04.05, Credentials and federation, "Federation: sign in once, elsewhere, and receive temporary access"](../04-shared-responsibility-and-access/05-credentials-and-federation.md#federation-sign-in-once-elsewhere-and-receive-temporary-access).

**9. A** · Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). SNS pushes each message published to a topic to every subscriber at once, and its subscribers can be an SQS queue, a Lambda function and an email address, so one publish reaches all three. A single SQS queue holds each message for one worker to pull, SES sends an application's own mail rather than fanning a message out, and Step Functions runs steps in order rather than at once. Reread: [Lesson 08.04, Connecting parts, shipping software, "SNS pushes one message to every subscriber of a topic"](../08-building-and-operating/04-connecting-parts-shipping-software.md#sns-pushes-one-message-to-every-subscriber-of-a-topic).

**10. D** · Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Knowing where the money goes, and who is responsible for it, serves the cost optimization pillar, which asks whether the workload delivers its value at the lowest cost. Sustainability measures resources and energy rather than money, reliability is about working and recovering from failure, and performance efficiency is about using the right kind and amount of resources. Reread: [Lesson 02.05, The Well-Architected Framework, "Pillars that sound alike, side by side"](../02-why-the-cloud/05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side).

**11. A** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Data moving over the network needs encryption in transit: a TLS certificate from ACM on the load balancer gives HTTPS, and the redirect makes HTTPS required rather than merely available. The other choices concern data at rest or finding sensitive data, and none protects the patient details on their way to the load balancer. Reread: [Lesson 09.02, Encryption, "TLS certificates from ACM protect data in transit"](../09-protecting-and-governing/02-encryption.md#tls-certificates-from-acm-protect-data-in-transit).

**12. B and E** · Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). Instance store is temporary disk on the physical host: it survives a reboot, but its data is lost when the instance stops, hibernates or terminates. That suits data you can rebuild or redo, such as a cache whose originals are in S3 or a rerunnable job's working files. Uploads, database files and a disk that must survive nightly stops belong on EBS or in S3. Reread: [Lesson 05.01, Block, file and object storage, "Block storage: a disk attached to one server"](../05-storing-data/01-block-file-object.md#block-storage-a-disk-attached-to-one-server).

**13. B and D** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). On Fargate, AWS runs and patches the servers and decides how many there are, so A and C leave the customer's list, and E was always AWS's. What runs inside the image, including its libraries, and the permissions the app gets through its role stay with the customer on every compute option. Reread: [Lesson 06.03, Containers and serverless, "Your side of the line"](../06-running-applications/03-containers-and-serverless.md#your-side-of-the-line).

**14. B** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Paying by use saves money only when unused capacity is switched off, and automation does it reliably without anyone having to remember. Instance hours bill whether or not anyone uses them (D); a stopped instance still pays for its EBS volumes, but far less. Larger instances don't remove idle hours, and Availability Zones don't affect them. Reread: [Lesson 02.04, What a data center really costs, "Rightsizing and automation keep the variable bill small"](../02-why-the-cloud/04-what-a-data-center-really-costs.md#rightsizing-and-automation-keep-the-variable-bill-small).

**15. C** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). Data transfer is priced by direction: data out to the internet is charged, so more viewers streaming out raises the bill. Uploads in from the internet are free, and so are reads by EC2 from S3 in the same Region and traffic within one Availability Zone over private addresses. Traffic across Availability Zones and between Regions would also be charged. Reread: [Lesson 07.04, Connecting networks and offices, "Data in is free; across, between and out usually costs"](../07-connecting-it/04-connecting-networks-and-offices.md#data-in-is-free-across-between-and-out-usually-costs).

**16. C** · Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). A scaled-down but fully working copy that takes traffic once it scales up is a warm standby, recovering in minutes. A pilot light keeps only the core, such as the copied data, switched on and must start the rest, which takes longer. Multi-site active/active serves traffic from both Regions all the time, and backup and restore rebuilds from backups, in hours. Reread: [Lesson 03.03, Surviving failure, "Four strategies, from cheap and slow to costly and fast"](../03-aws-around-the-world/03-surviving-failure.md#four-strategies-from-cheap-and-slow-to-costly-and-fast).

**17. A** · Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). The Knowledge Center is AWS's collection of official articles for common questions and problems, published inside re:Post. Artifact holds AWS's audit reports and agreements, Security Hub collects security findings about your own account, and the Health Dashboard reports problems on AWS's side; none of them is a library of how-to answers. Reread: [Lesson 09.05, Compliance and governance, "Where AWS publishes security information"](../09-protecting-and-governing/05-compliance-and-governance.md#where-aws-publishes-security-information).

**18. C** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). The two Availability Zones keep the site working if one fails, which is high availability. Elasticity is a different benefit: capacity that follows demand, which two fixed instances don't do until something such as an Auto Scaling group adds and removes them. Durability concerns stored data, and elasticity needs no second Region. Reread: [Lesson 02.03, Telling the benefits apart, "All five side by side"](../02-why-the-cloud/03-telling-the-benefits-apart.md#all-five-side-by-side).

**19. B and E** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Artifact hands out AWS's own reports and agreements: free evidence about AWS's controls, and contracts such as the BAA that a United States healthcare business may need. It doesn't judge the startup's resources (Config rules and Security Hub checks do that), it certifies nothing about the customer's workload, and API calls are CloudTrail's record. Reread: [Lesson 09.05, Compliance and governance, "AWS Artifact hands you AWS's audit reports, not a verdict on you"](../09-protecting-and-governing/05-compliance-and-governance.md#aws-artifact-hands-you-awss-audit-reports-not-a-verdict-on-you).

**20. C** · Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). A gateway endpoint gives the private subnet its own route to S3 (or DynamoDB), off the internet and with no charge for the endpoint, so the S3 traffic no longer passes through the NAT gateway. Moving to a public subnet or adding Elastic IP addresses gives up privacy, and interface endpoints are private too but bill by the hour and per gigabyte. Reread: [Lesson 07.01, Your own network, "VPC endpoints reach AWS services without the internet, and one kind is free"](../07-connecting-it/01-your-own-network.md#vpc-endpoints-reach-aws-services-without-the-internet-and-one-kind-is-free).

**21. A** · Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Building a full-size test copy and removing it afterwards is "Test systems at production scale", one of the Framework's six general design principles; the cloud makes the copy affordable because you pay only while it exists. "Design for failure", "think parallel" and "geographic diversity" are slogans from older study material, not Framework principles. Reread: [Lesson 02.05, The Well-Architected Framework, "Real design principles, and slogans that only sound like them"](../02-why-the-cloud/05-the-well-architected-framework.md#real-design-principles-and-slogans-that-only-sound-like-them).

**22. A and C** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Protecting the root user means MFA, no access keys and no everyday work as root; reading bills belongs to an IAM identity with billing access. IAM policies don't limit the root user (B), a new password doesn't end routine use of the most powerful identity (D), and the root user has no name to change: it signs in with the account's email address (E). Reread: [Lesson 04.03, Identities, "Protecting the root user is your job, and you've already done it"](../04-shared-responsibility-and-access/03-identities.md#protecting-the-root-user-is-your-job-and-youve-already-done-it).

**23. D** · Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). Redshift is a data warehouse, built for complex analytical queries over years of history from many sources, apart from the systems that run the business. DynamoDB answers lookups by key, ElastiCache serves repeated reads from memory, and Neptune follows relationships between items; none of them is built for years of analytical reporting. Reread: [Lesson 05.05, Managed databases and choosing one, "The database services side by side"](../05-storing-data/05-managed-or-self-managed-databases.md#the-database-services-side-by-side).

**24. A** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). Lambda charges for requests and for compute time while the code runs, in GB-seconds, so a job that runs two minutes a night pays for two minutes. The EC2 instance bills for every hour it runs, busy or idle. Lambda has a monthly free allowance, but short workloads aren't free by rule, and it has no fixed monthly price. Reread: [Lesson 06.03, Containers and serverless, "Lambda runs your code only when an event triggers it"](../06-running-applications/03-containers-and-serverless.md#lambda-runs-your-code-only-when-an-event-triggers-it).

**25. B** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). Shield Standard protects every AWS customer automatically and free against common network floods, and it is strongest with CloudFront in front. AWS WAF is a tool AWS provides, but choosing and configuring its rules for the shop's own requests is the customer's side of the line. Shield Advanced is a paid subscription, not something CloudFront includes. Reread: [Lesson 09.04, The front door, "AWS Shield Standard is already protecting every AWS account"](../09-protecting-and-governing/04-the-front-door.md#aws-shield-standard-is-already-protecting-every-aws-account).

**26. A** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). DynamoDB's on-demand mode bills per request, so its cost is purely variable and follows the bursts, with no servers or capacity to plan. A DB instance or an EC2 server sized for the peak bills every hour whether anyone is playing or not, which makes it a fixed cost, and Redshift is a warehouse for analysis. Reread: [Lesson 05.05, Managed databases and choosing one, "DynamoDB stores items by key, at any scale, with no servers to run"](../05-storing-data/05-managed-or-self-managed-databases.md#dynamodb-stores-items-by-key-at-any-scale-with-no-servers-to-run).

**27. D** · Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). X-Ray traces one request across every part it touches and shows where the time goes; AWS now presents it as part of CloudWatch, but request tracing still means X-Ray on the exam. CloudTrail records who did what to the account, Config records resource settings, and an alarm watches one metric rather than following a request. Reread: [Lesson 08.03, Watching workloads, "X-Ray follows one request through every part it touches"](../08-building-and-operating/03-watching-workloads.md#x-ray-follows-one-request-through-every-part-it-touches).

**28. B** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). A subnet is public only if its route table points to an internet gateway, so these databases still can't reach the internet or be reached from it. AWS charges for every public IPv4 address by the hour, used or not, so the addresses add cost and nothing else. Reread: [Lesson 07.01, Your own network, "A subnet is public because of its route, not because of its addresses"](../07-connecting-it/01-your-own-network.md#a-subnet-is-public-because-of-its-route-not-because-of-its-addresses).

**29. C and E** · Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). The load balancer is the single front door: it spreads requests across Availability Zones and sends each one only to a healthy target. Auto Scaling decides how many instances run: it launches them from the launch template, keeps the count between its limits and replaces unhealthy ones. Reread: [Lesson 06.02, Auto Scaling and load balancers, "Auto Scaling changes how many; the load balancer chooses which"](../06-running-applications/02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which).

**30. B** · Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). An SDK puts AWS calls inside your own program, signing each request with the application's role credentials, so the application stores each photo as part of its normal work. The console and the CLI are for people, and a CloudFormation template describes resources to create, not work an application does each time it runs. Reread: [Lesson 08.01, Four ways in, and infrastructure as code, "An SDK puts AWS calls inside your own program"](../08-building-and-operating/01-four-ways-in.md#an-sdk-puts-aws-calls-inside-your-own-program).

</details>

## Score by domain

Count your correct answers in each domain and find your band. The bands say what to study next, not how you'd do on the exam.

| Domain | Share of the exam | Questions in this set | Restudy (below 60%) | Review the linked sections (60–79%) | Ready on this domain (80% or more) |
|---|---|---|---|---|---|
| 1 Cloud Concepts | 24% | 7: 3, 6, 10, 14, 18, 21, 26 | 0 to 4 | 5 | 6 to 7 |
| 2 Security and Compliance | 30% | 9: 1, 4, 8, 11, 13, 17, 19, 22, 25 | 0 to 5 | 6 to 7 | 8 to 9 |
| 3 Cloud Technology and Services | 34% | 10: 2, 5, 9, 12, 16, 20, 23, 27, 29, 30 | 0 to 5 | 6 to 7 | 8 to 10 |
| 4 Billing, Pricing, and Support | 12% | 4: 7, 15, 24, 28 | 0 to 2 | 3 | 4 |

**Read the bands as pointers, not verdicts.** With 4 questions in Domain 4, one miss moves you from 100% to 75%. For a domain in the restudy band, reread the lessons the answer key links to and retake the mastery check of the module they belong to, before Module 10. In the review band, reread only the linked sections for your misses. The [blueprint map](../99-reference/06-blueprint-map.md) lists every page that teaches each task, if you want a second explanation.

**A practice score is not a prediction of an exam score.** This set shows which ideas you can tell apart today. The real exam reports a scaled score from 100 to 1,000 on questions you haven't seen, with a different mix on each form ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md)). Readiness is judged later, on the two practice exams, taken unseen.

Next: [Module 10: Data, AI and the rest of the catalog](../10-data-ai-and-more/00-brief.md).

---

"Mixed set 2: Modules 02 to 09" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
