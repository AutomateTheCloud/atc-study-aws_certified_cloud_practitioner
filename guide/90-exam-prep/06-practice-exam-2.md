---
type: check
id: clf-90-06
title: "Practice exam 2"
tasks: ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "4.1", "4.2", "4.3"]
objectives: []
reader: "Adult studying alone who has finished Modules 02 to 13 and wants a full timed rehearsal; 90 minutes, then about 45 minutes to score and review"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00, clf-10-00, clf-11-00, clf-12-00, clf-13-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
---

# Practice exam 2: a second full rehearsal in exam format

This is a second complete practice exam: 65 questions in 90 minutes, spread across the four domains in the same proportions as the real CLF-C02 exam, and across all 19 task statements. None of its questions appears anywhere else in this guide, so it measures what you can do with situations you haven't seen.

**For:** an adult studying alone who has finished Modules 02 to 13 and wants a timed rehearsal before booking or sitting the exam. **Time:** 90 minutes for the questions, then about 45 minutes to score them and read the explanations.

## How to take it

- **Set a timer for 90 minutes** and take the whole exam in one sitting, as you will on the day. That's a little under a minute and a half per question.
- **Closed book.** No lessons, notes, AWS pages or search. Answer from what you know.
- **Answer every question.** On the real exam a blank counts as wrong and a wrong guess costs nothing more, so guess when you must and flag the question to come back to.
- **Don't open the answer key until you've finished** all 65. Looking early turns the rest of the exam into practice, not a measure.
- **Score it:** one point per question. A "(Select TWO.)" question scores only if you chose both correct answers and nothing else, as on the exam. Then count your points per domain and use the [score table](#score-by-domain) to find what to do next.
- **Use it once as a measure.** Your first attempt is the readiness signal. After you've read the key, a retake shows that you remember these questions, not that you're ready for new ones. Take [Practice exam 1](05-practice-exam-1.md) on a different day for a second measure.

The real exam has 65 questions too, but 15 of them are unscored trials you can't identify, and it reports a scaled score. Here every question counts and you get a raw count, so the two aren't directly comparable. The questions use the exam's names for services; where AWS has renamed something, the explanation gives today's name.

## The questions

**1.** A concert-ticket reseller's site gets about ten times its usual traffic in the first hour after a popular tour goes on sale, then returns to normal. On AWS, the site adds servers automatically as the rush builds and removes them as it fades, so the company pays for the extra servers only while they run. Which benefit of the AWS Cloud does this show?

- **A.** Agility
- **B.** Global reach
- **C.** Elasticity
- **D.** High availability

**2.** A credit union is moving its loan-processing servers to Amazon EC2. Its auditor asks which security work AWS, not the credit union, will do for those instances. Which task belongs to AWS?

- **A.** Patching the guest operating system on each instance
- **B.** Setting the security group rules that allow traffic to the instances
- **C.** Deciding whether the instances' EBS volumes are encrypted
- **D.** Maintaining the physical hosts and the virtualization layer that the instances run on

**3.** A parcel-delivery company records the latest status of every parcel and looks each one up by its tracking number. Volume jumps unpredictably during holiday sales, responses must stay in single-digit milliseconds, and the team doesn't want to manage any database servers. Which AWS database fits best?

- **A.** Amazon DynamoDB
- **B.** Amazon Redshift
- **C.** Amazon RDS for MySQL on a large instance
- **D.** Amazon Neptune

**4.** A regional TV broadcaster must leave its data center in ten weeks, when the lease ends. It runs 60 Linux servers whose applications work well, and its team has no time to change any of them before the deadline. Which migration strategy fits these servers best?

- **A.** Refactor
- **B.** Replatform
- **C.** Repurchase
- **D.** Rehost

**5.** At a design agency, an IAM administrator saved a bucket policy on a critical Amazon S3 bucket that denies every principal every action, which locks out her and every other administrator. How can the agency regain control of the bucket?

- **A.** Wait for the bucket policy to expire after 24 hours
- **B.** Create a new IAM user with the AdministratorAccess policy and use it to edit the bucket policy
- **C.** Sign in as the account's root user and fix or delete the bucket policy
- **D.** Ask AWS Support to delete the bucket policy for the agency

**6.** A bank runs its payment service in two Availability Zones in one AWS Region. A manager asks why a fire or a power cut in one building wouldn't stop the service. Which statement best explains it?

- **A.** Each Availability Zone is in a different country, far from the others
- **B.** AWS automatically copies every resource to every Availability Zone in the Region
- **C.** The Availability Zones share one power supply but use separate networks
- **D.** Each Availability Zone has its own power, cooling and networking, physically separate from the other zones in the Region

**7.** An online insurance broker's quote service never goes down and its data is well protected. But it runs on general purpose instances while its pricing engine is limited by CPU, so each quote takes several seconds. A Well-Architected review flags this. Which pillar does the concern belong to?

- **A.** Reliability
- **B.** Performance efficiency
- **C.** Operational excellence
- **D.** Security

**8.** A video production agency's IT lead lists four kinds of data transfer the agency uses. Which one carries no data transfer charge?

- **A.** Uploading raw footage from the office over the internet into an Amazon S3 bucket
- **B.** Copying finished films from that bucket to a bucket in another AWS Region
- **C.** Clients downloading the films from S3 over the internet, beyond the monthly free allowance
- **D.** Sending files between two EC2 instances in different Availability Zones

**9.** A shipping company's auditor asks two questions about one security group: what its inbound rules were on a date three weeks ago, and whether at that time it broke the company's rule against allowing SSH from anywhere. Which AWS service answers both?

- **A.** Amazon CloudWatch
- **B.** AWS CloudTrail
- **C.** Amazon GuardDuty
- **D.** AWS Config

**10.** A film-editing studio's workstations save project files to an NFS share in its office. The studio wants every file stored in Amazon S3, so render jobs in AWS can read the files as objects, while the editors keep using the share as they do today and recently used files stay quick to open. Which solution fits?

- **A.** Amazon S3 File Gateway
- **B.** Volume Gateway in stored mode
- **C.** Tape Gateway
- **D.** AWS Elastic Disaster Recovery

**11.** Two months after moving to AWS, an engineering firm's monitoring shows that most of its EC2 instances average under 10% CPU use and never pass 30%, even at month-end. Which action is rightsizing?

- **A.** Buy three-year Reserved Instances for the instances at their current sizes
- **B.** Raise the maximum size of each Auto Scaling group
- **C.** Move the instances to Dedicated Hosts
- **D.** Move each instance to a smaller instance type that still covers its measured peak

**12.** A cloud engineer at an online retailer wants to keep up with new AWS security features as they are released, and to read walkthroughs from AWS that show how to set them up. Where should she look?

- **A.** AWS Security Bulletins
- **B.** AWS Artifact
- **C.** AWS Security Blog
- **D.** The AWS Trust and Safety team

**13.** A travel company packages its booking API as containers and wants to run them as always-on services on Amazon ECS. The team doesn't want to choose, patch or scale any EC2 instances for the containers. Which option meets this?

- **A.** AWS Fargate
- **B.** Amazon EC2 Dedicated Instances
- **C.** Amazon EKS with self-managed worker nodes
- **D.** Amazon EC2 Auto Scaling

**14.** A newspaper's data team wants to find out whether a new article-recommendation feature keeps readers on the site longer. On AWS, they build a full trial version in an afternoon, run it for two weeks, and delete it when the results disappoint, leaving nothing to pay for. Which benefit of the AWS Cloud does this show best?

- **A.** High availability
- **B.** Agility
- **C.** Elasticity
- **D.** Durability

**15.** A genomics institute sends several terabytes of sequencing data to AWS every day. Over its internet connection, the transfers slow down unpredictably at busy times of day. It wants a link to its VPCs with steady bandwidth and delay, and it can wait several weeks for the link to be installed. Which option fits?

- **A.** AWS DataSync over the existing internet connection
- **B.** A Site-to-Site VPN over the existing internet connection
- **C.** AWS Direct Connect
- **D.** Amazon CloudFront

**16.** A city government wants a company outside AWS to design its new permit system on AWS, build it, and migrate the old system's data, under a contract. In the exam's terms, which kind of AWS Partner does the city need?

- **A.** An independent software vendor (ISV)
- **B.** A training partner
- **C.** AWS Professional Services
- **D.** A system integrator

**17.** An online pharmacy wants customers' prescription details protected while they travel between customers' browsers and the Application Load Balancer in front of its site. Which approach does this?

- **A.** Turn on default encryption for the S3 bucket that stores the prescriptions
- **B.** Encrypt the web servers' EBS volumes with an AWS KMS key
- **C.** Serve the site over HTTPS, with a TLS certificate from AWS Certificate Manager (ACM) on the load balancer
- **D.** Run Amazon Macie on the prescription data

**18.** A development team has two problems. Some checkout requests are slow, and nobody can tell which of the services each request passes through adds the delay. And every code change should be compiled and unit-tested automatically, without the team running build servers. Which TWO AWS services address these problems? (Select TWO.)

- **A.** AWS CloudTrail
- **B.** AWS X-Ray
- **C.** Amazon Inspector
- **D.** AWS CodeBuild
- **E.** AWS Config

**19.** At a logistics company, changes to the parcel-tracking site are made by hand on the live servers late at night. Nobody writes down the steps or what changed, and after a bad change nobody looks into why it happened. Which Well-Architected pillar's practices are most clearly missing?

- **A.** Reliability
- **B.** Security
- **C.** Operational excellence
- **D.** Cost optimization

**20.** A consulting firm with 300 employees already manages their sign-ins in its corporate identity provider. It wants staff to sign in once with those corporate credentials and reach the AWS accounts their jobs need, without anyone getting an IAM user. Which approach fits?

- **A.** Create an IAM user with MFA for each employee in every account
- **B.** Use AWS IAM Identity Center, connected to the corporate identity provider
- **C.** Create one shared IAM user per team and change its password every month
- **D.** Use an Amazon Cognito user pool for the employees

**21.** A retail chain must build the same network, servers and database for each of the 30 new stores it opens this year, identically each time, and keep a reviewable record of every change to the setup. Which approach fits best?

- **A.** Follow a written checklist in the AWS Management Console for each store
- **B.** Ask AWS Support to build each store's resources
- **C.** Type the AWS CLI commands by hand at a prompt for each store
- **D.** Describe the setup once in an AWS CloudFormation template, and create a stack from it for each store

**22.** A media company's finance team wants its cost reports to show which IAM user or role created each resource, without asking engineers to tag anything themselves. What should the organization's management account do?

- **A.** Activate the AWS-generated cost allocation tag aws:createdBy
- **B.** Create a user-defined tag named createdBy and ask every engineer to apply it
- **C.** Turn on AWS Config recording in every account
- **D.** Create an AWS Budgets budget for each IAM user

**23.** A ride-hailing company wants its stream of trip events delivered into Amazon S3 continuously, without writing or running its own delivery code. It then wants the structure of that data recorded in a central catalog, so analysts can query it. Which TWO services fit these two jobs? (Select TWO.)

- **A.** Amazon EMR
- **B.** Amazon Data Firehose, part of Amazon Kinesis
- **C.** Amazon Quick Sight
- **D.** Amazon OpenSearch Service
- **E.** AWS Glue

**24.** A food-delivery startup runs its order-validation code as AWS Lambda functions. Under the AWS shared responsibility model, which TWO tasks remain the startup's? (Select TWO.)

- **A.** Securing the function code and the libraries packaged with it
- **B.** Patching the operating system of the servers that run the functions
- **C.** Writing the permissions in the functions' execution role
- **D.** Planning server capacity for traffic peaks
- **E.** Physical security of the data centers

**25.** An online travel agency is moving its booking database to AWS, keeping the same database engine. Bookings arrive around the clock, and the business can accept only a few minutes of downtime at the switch-over. Which approach best meets this?

- **A.** Take a full backup on Friday night, copy it to AWS, and restore it before Monday
- **B.** Use AWS DMS to copy the database while it keeps running, keep replicating new changes, and switch over once the copy has caught up
- **C.** Rebuild the bookings as items in Amazon DynamoDB, then switch over
- **D.** Pause bookings and copy the database files with AWS DataSync

**26.** A video-streaming company runs everything in one AWS Region, across three Availability Zones. Which TWO new requirements would justify adding a second Region? (Select TWO.)

- **A.** Keep running if one data center in the current Region loses power
- **B.** Add servers automatically during the evening peak
- **C.** Keep serving customers even if the whole current Region becomes unavailable
- **D.** Encrypt the video files stored in Amazon S3
- **E.** Store subscribers' personal data inside their own country, as a new law there requires, when the current Region is in another country

**27.** A small cloud consulting firm is deciding whether to join the AWS Partner Network. Which TWO are benefits AWS offers its partners? (Select TWO.)

- **A.** Unlimited AWS usage at no charge for the firm's own workloads
- **B.** Partner-only training that helps the firm's staff earn AWS certifications
- **C.** Permission to take over AWS's side of the shared responsibility model for its clients
- **D.** Partner events, and the chance to list in AWS Marketplace and sell together with AWS
- **E.** An AWS employee assigned to carry out the firm's client projects

**28.** A small charity's AWS account is on Basic Support. Its volunteer administrator wants a free, quick look at common security gaps, such as a root user without MFA or security groups that leave certain ports open to everyone. Which service should she use?

- **A.** AWS Trusted Advisor
- **B.** Amazon Detective
- **C.** AWS Shield Advanced
- **D.** Amazon Macie

**29.** An online exam platform's load rises sharply during exam weeks and drops between them. Which feature adds EC2 instances automatically when the load rises and removes them when it falls?

- **A.** Elastic Load Balancing
- **B.** Amazon CloudFront
- **C.** Amazon EC2 Auto Scaling
- **D.** AWS Batch

**30.** The finance director of a small accounting firm asks why AWS can charge less per hour for a server than it would cost the firm to buy, power and run the same server itself. Which explanation reflects AWS's economies of scale?

- **A.** AWS requires every customer to commit to three years of use
- **B.** AWS doesn't charge for data transferred out to the internet
- **C.** AWS customers maintain the physical hardware themselves
- **D.** AWS combines the usage of a very large number of customers, so it buys and runs equipment at a scale no single customer can

**31.** An online quiz game shows a live leaderboard that is updated and read thousands of times a second during each round, and needs responses in well under a millisecond. The scores can be rebuilt from the main database if they are lost. Which service fits the leaderboard best?

- **A.** Amazon Redshift
- **B.** Amazon ElastiCache
- **C.** Amazon RDS with a Multi-AZ deployment
- **D.** Amazon S3 Standard

**32.** A payroll company must show auditors that the data it stores in Amazon S3 and on Amazon EBS volumes is encrypted under keys the company controls, and that every use of those keys is recorded. Which TWO actions meet these requirements? (Select TWO.)

- **A.** Encrypt the S3 buckets and EBS volumes with AWS KMS customer managed keys
- **B.** Require TLS on every connection between clients and the servers
- **C.** Turn on Amazon GuardDuty in every Region
- **D.** Store the encryption keys in the application's configuration file
- **E.** Review the KMS key-use events that AWS CloudTrail records

**33.** An insurance company stores scanned claim forms in Amazon S3. Its data manager has read that S3 Lifecycle rules could cut storage costs and enforce the company's retention schedule. Which TWO jobs can a lifecycle rule do? (Select TWO.)

- **A.** Encrypt each new object with an AWS KMS key
- **B.** Move objects to a cheaper storage class once they reach a set age
- **C.** Block public access to the bucket
- **D.** Delete objects, or their older versions, once they reach a set age
- **E.** Make each object available in a second AWS Region

**34.** A chain of veterinary clinics runs its appointment-booking system on servers in two Availability Zones. One morning, a power problem takes one zone offline, and pet owners keep booking appointments without noticing anything. Which benefit of the AWS Cloud does this show?

- **A.** Durability
- **B.** Elasticity
- **C.** High availability
- **D.** Agility

**35.** A ski resort's mobile app needs sign-up and sign-in for hundreds of thousands of visitors, including sign-in with their Facebook accounts. After signing in, the app uploads each visitor's photos to Amazon S3, and it must never contain long-term AWS credentials. Which approach fits?

- **A.** Build the app with one IAM user's access keys inside it
- **B.** Store an IAM user's access keys in AWS Secrets Manager and have every copy of the app read them
- **C.** Use Amazon Cognito: a user pool to sign visitors in, and an identity pool to give the app temporary, limited AWS credentials
- **D.** Create a member account in AWS Organizations for each visitor

**36.** A tax-preparation firm hires seasonal staff each spring, who work from their own computers. The firm wants them to use only its licensed Windows tax application, streamed from AWS, with nothing installed on their computers and no whole desktop for each person. Which service fits?

- **A.** Amazon WorkSpaces
- **B.** Amazon AppStream 2.0
- **C.** AWS Amplify
- **D.** Amazon Lightsail

**37.** An analytics team creates a 2 TiB Amazon EBS volume for a database that holds only 200 GiB of data so far. It also keeps 200 GiB of files in Amazon S3 Standard. How is each one billed for storage?

- **A.** Both are billed for the 200 GiB actually stored
- **B.** The EBS volume for the data stored on it; S3 for a fixed bucket size chosen at creation
- **C.** The EBS volume for its full 2 TiB, whether or not it is filled; S3 for the 200 GiB stored
- **D.** Neither is billed for storage while nobody reads the data

**38.** A recipe website runs a copy of its application in two AWS Regions. The owners want visitors' DNS lookups to send them to the primary Region, and to send them to the second Region automatically if health checks show the primary is down. Which service does this?

- **A.** Amazon Route 53
- **B.** Amazon CloudFront
- **C.** AWS Direct Connect
- **D.** AWS Transit Gateway

**39.** A Well-Architected review at a car-rental company lists four findings, each tagged with a pillar. Which finding is tagged with the right pillar?

- **A.** A single database server whose failure stops all bookings: performance efficiency
- **B.** Pages that load slowly for customers on another continent: reliability
- **C.** Servers left mostly idle all year, using electricity whatever they cost: sustainability
- **D.** One administrator password shared by the whole team: operational excellence

**40.** A newly hired security analyst at an e-commerce company wants one AWS starting point that describes the security services AWS offers and how AWS approaches security. Where should she start?

- **A.** AWS Security Center
- **B.** AWS Security Bulletins
- **C.** AWS Knowledge Center
- **D.** AWS Health Dashboard

**41.** A pharmaceutical manufacturer keeps the systems that control its production lines on servers inside its factories. Those systems connect to AWS, where the company runs its analytics and its customer portal. Which deployment model is this?

- **A.** Cloud
- **B.** On-premises
- **C.** Hybrid
- **D.** Multi-Region

**42.** An insurance company's migration team is matching strategies to its applications. Which TWO statements about migration strategies are correct? (Select TWO.)

- **A.** Rehost moves servers onto Amazon EC2 without changing the application
- **B.** Replatform redesigns the application into many small services
- **C.** Refactor is usually the quickest and cheapest strategy
- **D.** Retain keeps an application where it is for now, for a reason such as a recent upgrade or a compliance need
- **E.** Retire means replacing the application with a software-as-a-service product

**43.** A city's IT department is preparing for an audit of its systems on AWS. Which of these is a shared control, where AWS and the city each do their own part in their own context?

- **A.** Physical access to the data center buildings
- **B.** Patch management
- **C.** Fire suppression and power in the data centers
- **D.** Deciding which staff may read residents' records

**44.** A tutoring company replaces its single EC2 web server with four instances spread across two Availability Zones. Students must keep reaching the site at one address, requests must be shared among the instances, and an instance that stops responding must stop receiving requests. Which component provides this?

- **A.** An Elastic IP address, moved to a working instance by a script
- **B.** An AWS Transit Gateway
- **C.** A NAT gateway
- **D.** An Elastic Load Balancing load balancer

**45.** A school district's security lead wants to find IAM roles that are allowed to use services they haven't used in months, so she can remove those permissions. Which feature shows this?

- **A.** IAM last accessed information, among the IAM console's access reports
- **B.** AWS Artifact reports
- **C.** Amazon CloudWatch metrics for each role
- **D.** AWS Shield Standard

**46.** An engineering firm's new branch office needs an encrypted link from its office network to the firm's VPC, working by tomorrow, over the branch's existing internet connection. Which option fits?

- **A.** AWS Direct Connect
- **B.** AWS Site-to-Site VPN
- **C.** AWS Client VPN
- **D.** Amazon CloudFront

**47.** A marketing agency's engineers build a test environment by hand for each client campaign. It takes most of a day, the copies often differ, and some are left running for months after a campaign ends. Which TWO benefits would building them from infrastructure as code most directly bring? (Select TWO.)

- **A.** AWS takes over patching the servers in the environments
- **B.** Every environment is built the same way, with fewer configuration mistakes
- **C.** The resources in the environments are billed at a lower hourly rate
- **D.** The environments no longer need security groups
- **E.** Deleting an environment's stack removes its resources, so nothing is left running by accident

**48.** A family-owned winery learns that the email address of its AWS account's root user is the personal mailbox of an employee who left last year, and that the root user's only MFA device was that employee's phone. Which TWO actions best restore the winery's protection of the root user? (Select TWO.)

- **A.** Give the former employee an IAM user so she can pass on any root user emails
- **B.** Change the root user's email address to a mailbox the winery controls
- **C.** Register a new MFA device for the root user, such as a security key or passkey kept by the winery
- **D.** Create an IAM user named root with the AdministratorAccess policy
- **E.** Rely on AWS Shield Standard, which protects every account's sign-in

**49.** A media group has 12 AWS accounts in one organization in AWS Organizations, with consolidated billing. What does consolidated billing do for the group's pricing?

- **A.** It combines usage across the accounts, so volume pricing tiers and shared Reserved Instance and Savings Plans discounts apply to the organization as a whole
- **B.** It gives every member account a paid Support plan at no charge
- **C.** It makes data transfer between the accounts' instances in different Regions free
- **D.** It fixes the group's AWS prices for three years

**50.** A property-management company runs EC2 instances, RDS databases, EFS file systems and DynamoDB tables in several accounts. It must apply one backup schedule and retention period to all of them, copy the backups to another Region, and show auditors that the backups ran. Which service fits?

- **A.** Amazon S3 Lifecycle rules
- **B.** AWS Storage Gateway
- **C.** AWS Elastic Disaster Recovery
- **D.** AWS Backup

**51.** A security engineer at a car-parts distributor is writing a one-page guide for her team on where to find each kind of AWS security information. Which pairing should she write down?

- **A.** New security features, with walkthroughs: AWS Security Bulletins
- **B.** AWS's own step-by-step article for fixing a common error: AWS Knowledge Center
- **C.** Notices of vulnerabilities that may affect AWS services: AWS Security Blog
- **D.** AWS's audit reports, such as SOC reports: AWS Security Center

**52.** A language-learning startup moves its app to AWS. Afterwards, its engineers launch a test copy of each new feature within minutes, and the app keeps working when one of its servers fails. Which TWO benefits of the AWS Cloud do these outcomes show? (Select TWO.)

- **A.** Economies of scale
- **B.** Elasticity
- **C.** Agility
- **D.** Global reach
- **E.** High availability

**53.** A game company's multiplayer servers run only in a European AWS Region. Players in East Asia complain of lag, because every move travels to Europe and back to be processed. Which change most directly reduces their lag?

- **A.** Add a second Availability Zone in the European Region
- **B.** Run game servers in an AWS Region in East Asia as well
- **C.** Move the game servers to larger instance types
- **D.** Store the game's assets in S3 Glacier Instant Retrieval

**54.** A retail group with 20 accounts in one organization buys third-party software through AWS Marketplace. The cloud team wants staff to subscribe only to products it has approved, and finance wants one view of Marketplace spending and agreements across all the accounts. Which TWO features meet these needs? (Select TWO.)

- **A.** Private Marketplace
- **B.** AWS Artifact
- **C.** The Procurement insights dashboard
- **D.** AWS License Manager
- **E.** AWS Trusted Advisor

**55.** A company runs one workload on Amazon EC2, one on Amazon RDS and one on AWS Lambda. For which of them does the company patch the operating system itself?

- **A.** Only the EC2 workload
- **B.** The EC2 and RDS workloads
- **C.** All three workloads
- **D.** Only the Lambda workload

**56.** A hotel chain's regional managers want interactive dashboards of occupancy and revenue, built from data its analysts already query with Amazon Athena and Amazon Redshift, and shared with managers in their web browsers. Which service fits?

- **A.** AWS Glue
- **B.** Amazon Kinesis Data Streams
- **C.** Amazon EMR
- **D.** Amazon Quick Sight

**57.** A game studio runs a short-lived load-test environment. To save money, the team proposes two changes: run it in one Availability Zone with no standby, and turn off MFA for the engineers who use it. According to the Well-Architected Framework, how should the team judge these proposals?

- **A.** Both are acceptable, because a test environment can relax every pillar
- **B.** One Availability Zone is a reasonable trade for a test environment, but turning off MFA is not, because security is generally not traded against the other pillars
- **C.** Turning off MFA is acceptable, but one Availability Zone is not, because reliability is never traded for cost
- **D.** Neither is acceptable, because every pillar must be maximized in every environment

**58.** A company that runs 5,000 vending machines wants each machine to report its stock levels securely to AWS several times an hour, and to route those messages to other AWS services for processing. Which service connects the machines?

- **A.** Amazon Connect
- **B.** AWS Amplify
- **C.** AWS IoT Core
- **D.** Amazon SES

**59.** A manufacturer has a Standard Reserved Instance with two years left that it no longer needs, and wants to sell the rest of the term to another AWS customer. The company's IAM administrator, who has full permissions, can't complete the first step. Why?

- **A.** Registering as a seller in the Reserved Instance Marketplace requires the account's root user
- **B.** Reserved Instances can't be resold under any circumstances
- **C.** Selling Reserved Instances requires the AWS Enterprise Support plan
- **D.** Only AWS Professional Services can list Reserved Instances for sale

**60.** A payments company checks AWS's Services in Scope by Compliance Program page and finds that a service it wants to use isn't listed under PCI DSS. What does this mean?

- **A.** The company may not use the service in any AWS account
- **B.** The service wasn't part of that assessment, so the company must decide whether card data will touch it and, if so, how that use will meet PCI DSS
- **C.** AWS will add the service to the company's own PCI DSS certification on request
- **D.** The service isn't available in the company's Region

**61.** A garden-supply wholesaler plans two database moves to AWS: its Microsoft SQL Server database to Amazon RDS for SQL Server, and its Oracle database to Amazon Aurora MySQL. Both databases must stay in use during their moves. Which plan fits?

- **A.** AWS DMS for both moves, with the Oracle schema converted first by AWS SCT, because only that move changes the engine
- **B.** AWS SCT for both moves, then AWS Application Migration Service to copy the data
- **C.** AWS DMS for the SQL Server move only, with the Oracle database shut down while its files are copied
- **D.** AWS Application Migration Service for both moves, because it copies whole servers

**62.** A regional law firm runs its own customer-relationship software on servers it maintains. As part of its move to the cloud, it decides to stop running that software and switch to a different vendor's customer-relationship product, sold as a subscription service that the vendor hosts. Which migration strategy is this?

- **A.** Rehost
- **B.** Retire
- **C.** Relocate
- **D.** Repurchase

**63.** An IT lead at a furniture retailer opens AWS Trusted Advisor to look for security issues. Which TWO issues can Trusted Advisor's checks point out? (Select TWO.)

- **A.** Malware on an EC2 instance's disk
- **B.** A SQL injection attack in progress against the retailer's website
- **C.** Customers' card numbers stored in an S3 object
- **D.** Security groups that allow unrestricted access to specific ports
- **E.** A root user without MFA turned on

**64.** A design studio's development servers on EC2 run around the clock, but its developers use them only during office hours on weekdays. The studio wants to stop paying for the hours when nobody uses them, with no daily manual work. What should it do?

- **A.** Buy three-year Reserved Instances for the servers
- **B.** Stop the servers automatically each evening and at weekends, and start them each weekday morning
- **C.** Move the servers to a Region with lower prices
- **D.** Switch the servers to Dedicated Instances

**65.** A museum stores high-resolution scans of its collection in Amazon S3. Which security task does AWS carry out for this storage?

- **A.** Deciding who may read the scans
- **B.** Choosing whether Block Public Access stays on for the bucket
- **C.** Choosing who holds the encryption keys for the scans
- **D.** Maintaining and securing the servers and disks that S3 runs on

## Answer key

Score yourself before you read this. Each entry gives the answer, the task statement it tests, why the answer is right and why the most tempting wrong choice is wrong, and the section of the guide that teaches it.

<details><summary>Answer key</summary>

**1. C.** Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Elasticity is capacity that grows and shrinks with demand: the same site gets more servers during the rush and fewer after it. Agility can look right because the servers arrive quickly, but agility is about how fast you can get something new or try an idea, not about following demand. High availability is about staying up when a part fails, which the scenario doesn't mention. *Reread:* [Elasticity: capacity grows and shrinks with demand](../02-why-the-cloud/03-telling-the-benefits-apart.md#elasticity-capacity-grows-and-shrinks-with-demand).

**2. D.** Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). AWS is responsible for security of the cloud: the facilities, the hardware and the virtualization layer under every instance. On EC2 the customer's share is large: the guest operating system, the security groups and the choice to encrypt volumes are all the credit union's. Patching is tempting because AWS patches its own infrastructure, but the operating system inside an EC2 instance is the customer's to patch. *Reread:* [AWS is responsible for security of the cloud](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#aws-is-responsible-for-security-of-the-cloud).

**3. A.** Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). DynamoDB stores items by key, scales with demand with no servers to manage, and answers in single-digit milliseconds, which fits lookups by tracking number. RDS for MySQL could hold the same records, which makes it look like a fit, but it's a relational database on an instance size you choose and must size for the spikes. Redshift is a data warehouse for analysis, and Neptune is a graph database for data about relationships. *Reread:* [DynamoDB stores items by key, at any scale, with no servers to run](../05-storing-data/06-choosing-a-database.md#dynamodb-stores-items-by-key-at-any-scale-with-no-servers-to-run).

**4. D.** Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Rehost (lift and shift) moves each server to Amazon EC2 without changing the application, the quickest way to meet a hard deadline; AWS's tool for it is AWS Application Migration Service, now named AWS Transform MGN. Replatform is tempting because it also moves the application, but it changes some parts on the way, such as the database host, and the team has no time for changes. Refactor redesigns the application and is the slowest and most costly strategy. *Reread:* [Rehost and relocate: move without changing the application](../13-moving-to-aws/02-seven-migration-strategies.md#rehost-and-relocate-move-without-changing-the-application).

**5. C.** Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Fixing an S3 bucket policy that denies everyone is one of the few tasks only the root user can do. A new administrator is tempting, but an explicit deny in the bucket policy beats any allow, so every IAM identity, however powerful, stays locked out. Bucket policies don't expire, and AWS Support doesn't edit a customer's resource policies. *Reread:* [Only the root user can do a short list of tasks](../04-shared-responsibility-and-access/03-identities.md#only-the-root-user-can-do-a-short-list-of-tasks).

**6. D.** Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). Availability Zones are built not to share single points of failure: each has its own power, cooling and networking, and they are physically apart, yet close enough for fast links between them. The zones of a Region are in one geographic area, not in different countries. AWS doesn't copy every resource across zones for you; running in two zones is a design choice the bank made. *Reread:* [Availability Zones don't share a single point of failure](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md#availability-zones-dont-share-a-single-point-of-failure).

**7. B.** Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Performance efficiency asks whether you use the right kind and amount of resources for the job; a CPU-bound engine on general purpose instances is the wrong kind, and a compute optimized family would likely fit better. You might reach for reliability because it also involves capacity, but it is about working correctly and recovering from failure, and this service never fails. Nothing here concerns day-to-day operations or protection. *Reread:* [Pillars that sound alike, side by side](../02-why-the-cloud/05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side).

**8. A.** Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). Data coming into AWS from the internet is free in every Region. Transfer out to the internet, between Regions and across Availability Zones is usually charged, even though the last two never leave AWS. The tempting idea that only internet-bound traffic costs money is half the rule: cross-Region and cross-zone transfer appear on the bill too. *Reread:* [Data transfer is priced by direction: in is free, but out, across and between usually cost](../11-paying-for-aws/01-how-aws-charges.md#data-transfer-is-priced-by-direction-in-is-free-but-out-across-and-between-usually-cost).

**9. D.** Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). AWS Config records how each resource was configured over time and evaluates those configurations against rules, so it shows the group's rules on that date and whether they were compliant. CloudTrail is tempting because it records who called the API that changed the group, but it doesn't show the resource's whole state at a point in time or judge it against a rule. CloudWatch shows how things are running, and GuardDuty reports threats. *Reread:* [AWS Config records how each resource was set, and judges it against your rules](../09-protecting-and-governing/01-who-did-what.md#aws-config-records-how-each-resource-was-set-and-judges-it-against-your-rules).

**10. A.** Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). S3 File Gateway appears to the workstations as a file share over NFS or SMB, stores each file as an object in S3, and keeps recently used files in a local cache, which is why the exam calls Storage Gateway a cached file system. Volume Gateway looks close because it's another Storage Gateway type, but it presents disks over iSCSI, not a file share, and in stored mode the full data stays in the office. Tape Gateway serves backup software, and Elastic Disaster Recovery keeps servers ready for recovery. *Reread:* [Storage Gateway lets on-premises software use AWS storage without changing](../05-storing-data/04-hybrid-storage-and-backup.md#storage-gateway-lets-on-premises-software-use-aws-storage-without-changing).

**11. D.** Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Rightsizing means choosing the type, size and number of resources that meet measured needs at the lowest cost; AWS Compute Optimizer can recommend sizes from the same data. Reserved Instances are tempting because they lower the rate, but committing at today's oversized types locks in the waste, so rightsize first and commit afterwards. A larger Auto Scaling maximum and Dedicated Hosts add capacity or cost rather than trimming them. *Reread:* [Rightsizing and automation keep the variable bill small](../02-why-the-cloud/04-what-a-data-center-really-costs.md#rightsizing-and-automation-keep-the-variable-bill-small); [Rightsize twice: before the move from measured data, and after it with Compute Optimizer](../13-moving-to-aws/04-the-business-case.md#rightsize-twice-before-the-move-from-measured-data-and-after-it-with-compute-optimizer).

**12. C.** Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). The AWS Security Blog is where AWS writes about new security features and how to use them, often step by step. Security Bulletins are easy to confuse with it because they're also AWS security news, but they report vulnerabilities that may affect AWS services and say whether customers must act. Artifact holds AWS's audit reports and agreements, and the Trust and Safety team (today written AWS Trust & Safety) handles reports of abuse from AWS resources. *Reread:* [Where AWS publishes security information](../09-protecting-and-governing/05-compliance-and-governance.md#where-aws-publishes-security-information).

**13. A.** Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). Fargate is serverless compute for containers: ECS runs each task on capacity AWS provides, so there are no instances to choose, patch or scale. EKS is tempting because it also runs containers, but with self-managed nodes the team would still run and patch EC2 instances. Dedicated Instances and EC2 Auto Scaling are both ways of working with EC2 instances, which the team wants to avoid. *Reread:* [Fargate runs containers without servers to manage](../06-running-applications/03-containers-and-serverless.md#fargate-runs-containers-without-servers-to-manage).

**14. B.** Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Agility is the speed of getting something new, and the freedom to experiment cheaply: a trial built in an afternoon and removed when it fails. Resources come and go here, which makes elasticity look right, but elasticity is the same system growing and shrinking with demand, and here a person's idea drove the change. Nothing in the scenario is about surviving a failure or keeping stored data safe. *Reread:* [Agility: getting something new takes minutes, not weeks](../02-why-the-cloud/03-telling-the-benefits-apart.md#agility-getting-something-new-takes-minutes-not-weeks).

**15. C.** Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). Direct Connect is a dedicated line from your network to AWS that bypasses the internet, which is what gives it steady bandwidth and delay; it needs physical setup, which the institute can wait for. DataSync is tempting because it's built to move large amounts of data, but it moves files over whatever network path you give it, so on the internet the slowdowns remain; a Site-to-Site VPN crosses the internet too. CloudFront delivers content to users from edge locations; it isn't a link from a data center. *Reread:* [Direct Connect is a dedicated line that bypasses the internet](../07-connecting-it/04-connecting-networks-and-offices.md#direct-connect-is-a-dedicated-line-that-bypasses-the-internet).

**16. D.** Task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3). System integrators are services partners: they design, build, migrate and connect systems for customers (some also run systems day to day, as managed service providers). An ISV is the other kind of partner the exam names, so it's an easy pick, but ISVs make and sell software products rather than delivering projects. A training partner teaches AWS skills rather than building systems, and Professional Services is part of AWS, while the city wants a company outside AWS. *Reread:* [AWS Partners are other companies: software vendors and services firms](../12-getting-help/04-partners-and-paid-help.md#aws-partners-are-other-companies-software-vendors-and-services-firms).

**17. C.** Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Data moving across a network is protected by encryption in transit, which for a website means HTTPS with a TLS certificate; ACM provides and renews certificates for load balancers. S3 default encryption and EBS encryption with KMS are tempting because they are encryption too, but they protect data at rest, once it's stored. Macie finds sensitive data in S3; it doesn't encrypt anything. *Reread:* [TLS certificates from ACM protect data in transit](../09-protecting-and-governing/02-encryption.md#tls-certificates-from-acm-protect-data-in-transit).

**18. B and D.** Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). X-Ray traces each request through the parts it touches and shows where the time goes; its tracing now appears in CloudWatch, and AWS recommends OpenTelemetry for new instrumentation. CodeBuild compiles code and runs tests on demand, with no build servers to manage. CloudTrail also records activity, which makes it a likely wrong pick, but it records actions on the AWS account, not how a request moves through the application. Inspector scans for vulnerabilities, and Config records resource settings. *Reread:* [X-Ray follows one request through every part it touches](../08-building-and-operating/03-watching-workloads.md#x-ray-follows-one-request-through-every-part-it-touches); [Shipping software: CodeBuild builds and tests, CodePipeline runs the release](../08-building-and-operating/04-connecting-parts-shipping-software.md#shipping-software-codebuild-builds-and-tests-codepipeline-runs-the-release).

**19. C.** Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Operational excellence is about running a workload well day to day and improving how the team works, with practices such as small, reversible changes, written procedures and learning from failures. Reliability is tempting because bad changes can cause outages, but the gap described is in how the team operates and learns, not in whether the design recovers from failure. Nothing here concerns protection or spending. *Reread:* [Six pillars, six questions](../02-why-the-cloud/05-the-well-architected-framework.md#six-pillars-six-questions).

**20. B.** Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). IAM Identity Center (formerly AWS Single Sign-On) federates a workforce: people sign in with their existing corporate identity and get temporary credentials in the accounts they may use, through permission sets. Cognito catches people out because it also signs people in, but it's built for the customers of your web and mobile apps, not your employees. IAM users per employee, or shared ones, are the long-term credentials federation is meant to avoid. *Reread:* [Federation: sign in once, elsewhere, and receive temporary access](../04-shared-responsibility-and-access/05-credentials-and-federation.md#federation-sign-in-once-elsewhere-and-receive-temporary-access).

**21. D.** Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). Work that repeats, and must come out identical every time, is what infrastructure as code is for: one template makes many identical stacks, and the template's version history records each change. The console is tempting because it's the easiest way to start, but it suits exploring and one-time actions, and 30 hand-built copies invite missed settings. CLI commands typed fresh each time are no more repeatable than clicks unless they're saved as a script, and AWS Support doesn't build customers' resources. *Reread:* [One-time or repeatable: the question that picks the way in](../08-building-and-operating/01-four-ways-in.md#one-time-or-repeatable-the-question-that-picks-the-way-in).

**22. A.** Task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2). aws:createdBy is an AWS-generated cost allocation tag: once the management account activates it, AWS applies it to supported resources created afterwards, and it appears in Cost Explorer and as a column in the Cost and Usage Report. A user-defined tag is tempting, but engineers would have to apply it, which the team wants to avoid, and it would need activating too. Config records resource settings and Budgets alerts on spending; neither labels costs by creator. *Reread:* [A tag reaches your cost reports only after you activate it](../11-paying-for-aws/04-many-accounts-one-bill.md#a-tag-reaches-your-cost-reports-only-after-you-activate-it).

**23. B and E.** Task [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7). Firehose (formerly Amazon Kinesis Data Firehose) is the ingest service that delivers streaming data to destinations such as S3 for you, with no consumer code to write. Glue crawls the stored data and records its schema in the Glue Data Catalog, which query services such as Athena then use. EMR looks right because it processes big data, but it runs frameworks such as Apache Spark on clusters; it isn't the catalog. Quick Sight draws dashboards, and OpenSearch Service searches text and logs. *Reread:* [Ingest: Data Streams holds records for your programs; Firehose delivers them for you](../10-data-ai-and-more/01-analytics-in-five-verbs.md#ingest-data-streams-holds-records-for-your-programs-firehose-delivers-them-for-you); [Catalog: Glue records what your data looks like and gets it ready](../10-data-ai-and-more/01-analytics-in-five-verbs.md#catalog-glue-records-what-your-data-looks-like-and-gets-it-ready).

**24. A and C.** Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). With Lambda, AWS runs and patches the servers, the operating system and, by default, the managed runtime, and supplies capacity as events arrive. The startup still owns its code and libraries, and the IAM permissions its functions use, because data and access always stay with the customer. Patching is the tempting wrong choice: it is the customer's job on EC2, but on Lambda the operating system is AWS's. *Reread:* [The line moves with the service: EC2, RDS, Lambda and S3](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3).

**25. B.** Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Database replication is the migration approach for minimal downtime: DMS copies the data while the source stays in use, then keeps applying new changes until the switch-over, so customers keep booking. A backup and restore appeals because it's simple, but bookings made after the backup would be missing unless the site closed during the copy. Rebuilding on DynamoDB is a redesign, and DataSync moves files, not a live database's changes. *Reread:* [Database replication is a technique, used inside a strategy](../13-moving-to-aws/02-seven-migration-strategies.md#database-replication-is-a-technique-used-inside-a-strategy).

**26. C and E.** Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). A second Region needs a reason, such as disaster recovery from a Region-wide failure, or data sovereignty, where a law requires data to stay in a country the current Region isn't in. Surviving the loss of a data center is tempting, but running across Availability Zones already covers it. Scaling for peaks and encrypting data both work within one Region. *Reread:* [Use more than one Region only when you have a reason](../03-aws-around-the-world/02-choosing-a-region.md#use-more-than-one-region-only-when-you-have-a-reason).

**27. B and D.** Task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3). AWS offers its partners training and certification, events, and ways to sell with AWS such as Marketplace listings and co-selling, along with funding and reseller programs. Free unlimited usage isn't a partner benefit, and no partner takes over AWS's responsibilities. Joining doesn't bring AWS staff to do the partner's work: delivering client projects is the consulting firm's own business. *Reread:* [What partners get from joining](../12-getting-help/04-partners-and-paid-help.md#what-partners-get-from-joining).

**28. A.** Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Trusted Advisor compares an account's settings with AWS best practices, and every account, including Basic Support, gets selected security checks such as root MFA and security groups with specific ports open to everyone. Detective sounds right because it's a security service, but it investigates what happened after a finding; it doesn't check settings. Shield Advanced is a paid DDoS protection subscription, and Macie finds sensitive data in S3. *Reread:* [Trusted Advisor is a first look at your settings, with a few security checks free](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#trusted-advisor-is-a-first-look-at-your-settings-with-a-few-security-checks-free).

**29. C.** Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). An Auto Scaling group changes how many instances run, launching them as load rises and terminating them as it falls, which is what makes the platform elastic. A load balancer usually works alongside Auto Scaling, so it's an easy mistake here, but it chooses which healthy instance gets each request; it doesn't change how many there are. CloudFront caches content at edge locations, and Batch runs queued batch jobs, not a website. *Reread:* [Auto Scaling changes how many; the load balancer chooses which](../06-running-applications/02-auto-scaling-and-load-balancers.md#auto-scaling-changes-how-many-the-load-balancer-chooses-which).

**30. D.** Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Economies of scale come from aggregation: AWS combines the usage of very many customers, which lowers its cost per unit and, AWS says, leads to lower pay-as-you-go prices. A commitment is tempting because Savings Plans and Reserved Instances do lower rates, but they are optional pricing choices, not the economies-of-scale benefit. Data out to the internet is usually charged, and AWS, not the customer, maintains the hardware. *Reread:* [Economies of scale: a very large provider can charge less per unit](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#economies-of-scale-a-very-large-provider-can-charge-less-per-unit).

**31. B.** Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). ElastiCache keeps data in memory, so it answers in microseconds, and it often holds fast-changing, short-lived data such as leaderboards and sessions; the exam calls it a memory-based database. RDS Multi-AZ looks attractive because it's a solid database choice, but its standby adds availability, not speed, and a disk-based database won't match in-memory response times. Redshift is for analysis, and S3 is object storage. *Reread:* [ElastiCache answers from memory in microseconds](../05-storing-data/06-choosing-a-database.md#elasticache-answers-from-memory-in-microseconds).

**32. A and E.** Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). KMS customer managed keys are keys the company creates and controls, including who may use them, and they encrypt S3 and EBS data at rest. CloudTrail records every use of a KMS key, which gives auditors the record. TLS is tempting because it's encryption, but it protects data in transit, not stored data. GuardDuty detects threats, and keys in a configuration file are neither well controlled nor recorded. *Reread:* [KMS holds the keys for data at rest, and records every use](../09-protecting-and-governing/02-encryption.md#kms-holds-the-keys-for-data-at-rest-and-records-every-use).

**33. B and D.** Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). Lifecycle rules do two kinds of thing: transitions, which move objects to a cheaper class as they age, and expirations, which delete objects or noncurrent versions at the age you set, for example at the end of a retention period. Encryption seems to belong here because it's also a bucket-wide setting, but it comes from default encryption, not a lifecycle rule. Block Public Access is its own setting, and copies in another Region come from replication. *Reread:* [Lifecycle rules move and delete objects for you](../05-storing-data/03-storage-classes-and-lifecycle.md#lifecycle-rules-move-and-delete-objects-for-you).

**34. C.** Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). High availability means the system keeps working when a part fails; running in two Availability Zones let bookings continue through the loss of one. Durability is tempting because both concern failures, but durability means stored data isn't lost, not that the system stays reachable. Nothing changed with demand, and nothing new was created. *Reread:* [High availability: the system keeps working when a part fails](../02-why-the-cloud/03-telling-the-benefits-apart.md#high-availability-the-system-keeps-working-when-a-part-fails).

**35. C.** Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Cognito is the identity service for the customers of your apps: user pools sign them in, including through social identity providers such as Facebook, and identity pools exchange that sign-in for temporary, limited AWS credentials, so the app holds no long-term keys. Secrets Manager is tempting because it stores secrets safely, but every copy of the app would still share the same long-term keys. An account per visitor is a misuse of Organizations. *Reread:* [Four identity services, side by side](../04-shared-responsibility-and-access/05-credentials-and-federation.md#four-identity-services-side-by-side).

**36. B.** Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). AppStream 2.0, now named Amazon WorkSpaces Applications, streams individual desktop applications from AWS to a user's browser or client, so nothing is installed locally. WorkSpaces is in the same family, which makes it the likely wrong pick, but it gives each person a whole desktop, which the firm doesn't want. Amplify builds and hosts web and mobile front ends, and Lightsail offers simple servers. *Reread:* [WorkSpaces Applications streams single apps; Secure Browser streams one web browser](../10-data-ai-and-more/03-people-apps-and-devices.md#workspaces-applications-streams-single-apps-secure-browser-streams-one-web-browser).

**37. C.** Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). EBS bills for what you provision, the volume's size, however much of it you fill, so it behaves like a small fixed cost; S3 bills for what you store, plus requests and data transferred out. Billing both for the data stored is tempting because that's how S3 and EFS work, but an EBS volume is reserved capacity. S3 buckets have no size to choose, and stored data is billed whether or not anyone reads it. *Reread:* [What you pay for](../05-storing-data/01-block-file-object.md#what-you-pay-for).

**38. A.** Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). Route 53 is AWS's DNS service; with failover routing and health checks it answers with the primary Region's address while it is healthy and with the second Region's when it isn't. CloudFront can look right because it's global and sits in front of websites, but it caches and delivers content from edge locations; answering DNS lookups is Route 53's job. Direct Connect and Transit Gateway connect networks. *Reread:* [Route 53 answers "where is it?", and it can choose the answer](../07-connecting-it/03-names-and-the-edge.md#route-53-answers-where-is-it-and-it-can-choose-the-answer).

**39. C.** Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Sustainability is about using as few resources and as little energy as the work needs, so idle servers wasting electricity belong there, as well as under cost optimization. A single server whose failure stops everything is a reliability concern, not performance efficiency, which is tempting because both deal with capacity. Slow pages for distant users are performance efficiency, and a shared password is security. *Reread:* [Pillars that sound alike, side by side](../02-why-the-cloud/05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side).

**40. A.** Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). AWS Security Center, the exam guide's name for AWS's security home page at aws.amazon.com/security, introduces AWS's security services and its approach to security. The Knowledge Center is tempting because it's also AWS's own content, but it holds step-by-step articles for fixing common problems. Security Bulletins report vulnerabilities that may affect AWS services, and the AWS Health Dashboard reports events affecting AWS services and your account. *Reread:* [Where AWS publishes security information](../09-protecting-and-governing/05-compliance-and-governance.md#where-aws-publishes-security-information).

**41. C.** Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). Hybrid means some parts run in the organization's own facilities and some in the cloud, connected so they work together, as here. On-premises might seem right because the factory systems stay in the company's buildings, but the analytics and portal run on AWS. Cloud would mean everything runs at the provider, and multi-Region describes where cloud resources run, not a deployment model. *Reread:* [The three deployment models are cloud, hybrid and on-premises](../02-why-the-cloud/01-what-cloud-computing-is.md#the-three-deployment-models-are-cloud-hybrid-and-on-premises).

**42. A and D.** Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Rehost (lift and shift) moves each server onto EC2 as it is, and retain leaves an application in place for now when there's a reason to stay. Replatform is tempting to call a redesign, but it changes only a few parts, such as moving to a managed database; redesign is refactor, which is the slowest and most costly strategy. Replacing an application with a SaaS product is repurchase; retire means switching it off. *Reread:* [Rehost, relocate, replatform, refactor side by side](../13-moving-to-aws/02-seven-migration-strategies.md#rehost-relocate-replatform-refactor-side-by-side); [Retire and retain: decide first what doesn't move](../13-moving-to-aws/02-seven-migration-strategies.md#retire-and-retain-decide-first-what-doesnt-move).

**43. B.** Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). Patch management is a shared control: AWS patches its infrastructure, and the city patches the guest operating systems and applications it runs. Physical access, fire suppression and power are inherited controls, done entirely by AWS. Deciding who reads residents' records is tempting because the city does it, but it is customer-specific: only the city does it, with no AWS half. *Reread:* [Shared controls: each side does its own half](../04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md#shared-controls-each-side-does-its-own-half).

**44. D.** Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). A load balancer gives the site one entry point, spreads requests across instances in several Availability Zones, and uses health checks to stop sending requests to instances that fail. An Elastic IP address is tempting because it's a fixed address, but it points at one instance at a time, so it can't share requests, and a script that moves it is a fragile stand-in for health checks. Transit Gateway connects networks, and a NAT gateway handles outbound traffic from private subnets. *Reread:* [A load balancer sends each request to a healthy instance](../06-running-applications/02-auto-scaling-and-load-balancers.md#a-load-balancer-sends-each-request-to-a-healthy-instance).

**45. A.** Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Last accessed information shows, for an IAM user, group, role or policy, which services it is allowed to use and when it last tried each one, so unused permissions stand out. CloudWatch metrics can seem to fit because they track activity over time, but they measure how resources perform, not which permissions identities use. Artifact holds AWS's audit reports, and Shield Standard protects against DDoS attacks. *Reread:* [Access reports show who can do what, and whether they still use it](../09-protecting-and-governing/01-who-did-what.md#access-reports-show-who-can-do-what-and-whether-they-still-use-it).

**46. B.** Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). Site-to-Site VPN joins an office network to a VPC through encrypted tunnels over the internet, and can be set up quickly on the existing connection. Direct Connect is tempting because it's the other office-to-AWS link, but it needs physical work at a Direct Connect location, which takes far longer, and it isn't encrypted unless you add encryption. Client VPN connects individual people's devices, not a whole office network. *Reread:* [A Site-to-Site VPN links an office network over the internet, encrypted](../07-connecting-it/04-connecting-networks-and-offices.md#a-site-to-site-vpn-links-an-office-network-over-the-internet-encrypted).

**47. B and E.** Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Automation repeats the same steps every time, so copies match and mistakes drop, and deleting a stack deletes what it created, so forgotten resources stop billing. A lower rate is tempting, but AWS charges the same for a resource however it was created: the savings come from staff time, fewer errors and fewer idle resources. Automation doesn't move the shared responsibility line or remove the need for security settings. *Reread:* [Automation makes work repeatable and cheaper](../08-building-and-operating/02-iac-and-automation.md#automation-makes-work-repeatable-and-cheaper).

**48. B and C.** Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Root protection includes keeping the account's recovery paths, such as its email address, under the company's control, and having working MFA on the root user; changing the root email is itself a root-only task. Giving the former employee an IAM user is tempting as a quick fix, but it leaves the account's recovery in the hands of someone who has left. An IAM user named root is just another IAM user, and Shield Standard protects against DDoS attacks, not sign-ins. *Reread:* [Protecting the root user is your job, and you've already done it](../04-shared-responsibility-and-access/03-identities.md#protecting-the-root-user-is-your-job-and-youve-already-done-it).

**49. A.** Task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2). For pricing, consolidated billing treats the organization as one account: usage is combined for volume tiers, and Reserved Instance and Savings Plans discounts can be shared, all on one bill paid by the management account at no extra fee. Free Support and free cross-Region transfer are tempting extras, but consolidated billing changes how usage is combined and billed, not what is included: data transfer is charged as usual. Prices aren't fixed by joining an organization. *Reread:* [Consolidated billing combines usage and sends one bill](../11-paying-for-aws/04-many-accounts-one-bill.md#consolidated-billing-combines-usage-and-sends-one-bill).

**50. D.** Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). AWS Backup runs backups for many AWS services from one backup plan, with the schedule, the retention and copies to another Region or account, and audit reports that show the backups happened. Elastic Disaster Recovery sounds close because it's also about recovery, but it keeps whole servers replicated and ready to launch; it doesn't manage backups across services. Lifecycle rules move and delete S3 objects, and Storage Gateway connects on-premises software to AWS storage. *Reread:* [AWS Backup runs backups for many services from one set of rules](../05-storing-data/04-hybrid-storage-and-backup.md#aws-backup-runs-backups-for-many-services-from-one-set-of-rules).

**51. B.** Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). The Knowledge Center, part of AWS re:Post, holds AWS's own articles that walk through common problems and their fixes. The other three swap their sources: new features and walkthroughs are on the Security Blog, vulnerability notices are Security Bulletins, and audit reports come from AWS Artifact. The Security Center is tempting for audit reports because it's AWS's security home page, but it introduces AWS's security services rather than handing out reports. *Reread:* [Where AWS publishes security information](../09-protecting-and-governing/05-compliance-and-governance.md#where-aws-publishes-security-information).

**52. C and E.** Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). Launching a test copy in minutes is agility: getting something new fast. Working through the loss of a server is high availability: the system keeps working when a part fails. Elasticity is tempting, but nothing here grows or shrinks with demand; economies of scale are about AWS's lower unit prices, and global reach about running close to users in other parts of the world. *Reread:* [All five side by side](../02-why-the-cloud/03-telling-the-benefits-apart.md#all-five-side-by-side).

**53. B.** Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). Low latency for distant users is one of the reasons to use more than one Region: servers in an East Asian Region process players' moves close to them. A second Availability Zone is tempting because it's the usual next step in a design, but it adds availability within Europe and does nothing about the distance. Larger instances speed up processing, not the trip around the world, and a storage class doesn't affect game moves. *Reread:* [Use more than one Region only when you have a reason](../03-aws-around-the-world/02-choosing-a-region.md#use-more-than-one-region-only-when-you-have-a-reason).

**54. A and C.** Task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3). Private Marketplace is the governance feature: administrators give each part of the organization a catalog of approved products, and new subscriptions to anything else are blocked. Procurement insights is the cost management feature: it shows Marketplace costs and agreements for all the accounts in the organization. License Manager is tempting because it's Marketplace's third buyer feature, entitlement, but it shares and tracks licenses already bought; it doesn't limit what staff may buy or report spending. *Reread:* [AWS Marketplace sells partners' products, with three services for the buyer](../12-getting-help/04-partners-and-paid-help.md#aws-marketplace-sells-partners-products-with-three-services-for-the-buyer).

**55. A.** Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). On EC2, the guest operating system is the customer's to patch. On RDS, AWS patches the operating system and the database software, and on Lambda AWS runs and patches the servers and their operating system. RDS is the tempting extra: the customer still manages database users, access and settings there, but not its operating system. *Reread:* [The line moves with the service: EC2, RDS, Lambda and S3](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3).

**56. D.** Task [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7). Quick Sight (written QuickSight in older material, now part of Amazon Quick) is the visualize step: it builds interactive dashboards from sources such as Athena and Redshift and shares them in a browser. Glue prepares data for analytics, which draws some people to it, but it catalogs and transforms data rather than presenting it. Kinesis Data Streams ingests streaming records, and EMR runs big-data frameworks on clusters. *Reread:* [Visualize: Quick Sight turns answers into dashboards](../10-data-ai-and-more/01-analytics-in-five-verbs.md#visualize-quick-sight-turns-answers-into-dashboards).

**57. B.** Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). The Framework expects pillars to be weighed against business need, so a test environment can accept lower reliability to save cost. It also says security and operational excellence are generally not traded against the other pillars, and a weakly protected test environment can still give an attacker a way into the account. Maximizing every pillar everywhere isn't the Framework's view. *Reread:* [The pillars can be traded against each other, but not all of them](../02-why-the-cloud/05-the-well-architected-framework.md#the-pillars-can-be-traded-against-each-other-but-not-all-of-them).

**58. C.** Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). IoT Core connects devices to AWS securely and uses rules to route their messages to other services. Amplify is tempting because it's also about apps on devices, but it builds and hosts web and mobile front ends for people to use. Connect runs contact centers, and SES sends email. *Reread:* [IoT Core connects devices and routes what they send](../10-data-ai-and-more/03-people-apps-and-devices.md#iot-core-connects-devices-and-routes-what-they-send).

**59. A.** Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Registering as a seller in the Reserved Instance Marketplace is on AWS's list of tasks only the root user can do, so even a full IAM administrator can't do it. The tempting reasoning is that full permissions allow everything, but root-only tasks are the exceptions, and they mostly change or rescue the account itself. Standard Reserved Instances can be sold once the account is registered; no Support plan or AWS team is needed. *Reread:* [Only the root user can do a short list of tasks](../04-shared-responsibility-and-access/03-identities.md#only-the-root-user-can-do-a-short-list-of-tasks).

**60. B.** Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Compliance coverage varies among AWS services: the page lists which services were included in each program's assessment. A missing service isn't forbidden; deciding whether regulated data will reach it is part of the company's share of the responsibility. The tempting reading is that "not in scope" means "not allowed", which AWS says it doesn't, and Regional availability is a separate question. *Reread:* [AWS lists its compliance programs, and which services each one covers](../09-protecting-and-governing/05-compliance-and-governance.md#aws-lists-its-compliance-programs-and-which-services-each-one-covers).

**61. A.** Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). DMS moves the data in both cases while the sources stay in use. Only the Oracle move is heterogeneous, so only it needs its schema converted first, with SCT or DMS Schema Conversion; SQL Server to RDS for SQL Server keeps the same engine. You might choose Application Migration Service (now AWS Transform MGN) because it moves whole servers, but a copied server keeps its old engine and doesn't land in RDS or Aurora. *Reread:* [Moving a database in: DMS moves the data, SCT converts the schema](../05-storing-data/06-choosing-a-database.md#moving-a-database-in-dms-moves-the-data-sct-converts-the-schema).

**62. D.** Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Repurchase means replacing an application with a different product, usually software as a service. Retire is tempting because the old software is switched off, but retire is for applications with no business value left; here the firm still needs the function and buys it as a service. Rehost and relocate both move the existing application unchanged. *Reread:* [Replatform and repurchase: change something on the way](../13-moving-to-aws/02-seven-migration-strategies.md#replatform-and-repurchase-change-something-on-the-way).

**63. D and E.** Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Trusted Advisor checks the account's settings against AWS best practices, and its security checks include security groups with specific ports open to everyone and MFA on the root user; every account gets both. Card numbers in S3 are tempting as a "security check", but finding sensitive data in S3 is Amazon Macie's job. Finding malware is a GuardDuty job, and blocking SQL injection is AWS WAF's. *Reread:* [Trusted Advisor is a first look at your settings, with a few security checks free](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#trusted-advisor-is-a-first-look-at-your-settings-with-a-few-security-checks-free).

**64. B.** Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Automation such as a schedule that stops the servers outside working hours removes the idle hours from the bill: AWS's own example cuts a week's running time from 168 hours to 40. Reserved Instances look attractive because they lower the rate, but they are a commitment billed for every hour of the term, used or not. A cheaper Region lowers the rate yet still bills the idle hours, and Dedicated Instances cost more. *Reread:* [Rightsizing and automation keep the variable bill small](../02-why-the-cloud/04-what-a-data-center-really-costs.md#rightsizing-and-automation-keep-the-variable-bill-small).

**65. D.** Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). For S3, AWS runs and secures everything under the stored data: the facilities, servers, disks and the service software. Choosing the encryption keys is tempting because S3 now encrypts new objects automatically, but who holds the keys is still the museum's choice. Who can read the data, and whether the bucket stays private, are always the customer's. *Reread:* [The line moves with the service: EC2, RDS, Lambda and S3](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3).

</details>

## Score by domain

Count your correct answers in each domain. The questions belong to these domains:

- **Domain 1: Cloud Concepts:** questions 1, 4, 7, 11, 14, 19, 25, 30, 34, 39, 42, 47, 52, 57, 62, 64.
- **Domain 2: Security and Compliance:** questions 2, 5, 9, 12, 17, 20, 24, 28, 32, 35, 40, 43, 45, 48, 51, 55, 59, 60, 63, 65.
- **Domain 3: Cloud Technology and Services:** questions 3, 6, 10, 13, 15, 18, 21, 23, 26, 29, 31, 33, 36, 38, 41, 44, 46, 50, 53, 56, 58, 61.
- **Domain 4: Billing, Pricing, and Support:** questions 8, 16, 22, 27, 37, 49, 54.

Then find your count in the table. The bands are percentages of each domain's questions: below 60%, from 60% to 79%, and 80% or more.

| Domain | Share of the exam | Questions here | Restudy the domain (below 60%) | Review the linked sections (60% to 79%) | Ready on this domain (80% or more) |
|---|---|---|---|---|---|
| Domain 1: Cloud Concepts | 24% | 16 | 0 to 9 | 10 to 12 | 13 to 16 |
| Domain 2: Security and Compliance | 30% | 20 | 0 to 11 | 12 to 15 | 16 to 20 |
| Domain 3: Cloud Technology and Services | 34% | 22 | 0 to 13 | 14 to 17 | 18 to 22 |
| Domain 4: Billing, Pricing, and Support | 12% | 7 | 0 to 4 | 5 | 6 to 7 |
| **Whole exam** | 100% | 65 | 0 to 38 | 39 to 51 | 52 to 65 |

What each band means:

- **Restudy the domain:** go back through the modules behind it (the [blueprint map](../99-reference/06-blueprint-map.md) lists them by task statement), redo their mastery checks, then come back to Practice exam 1 if you haven't taken it.
- **Review the linked sections:** for every question you missed, reread the section its answer links to, and write one sentence on why the right answer beats the one you chose.
- **Ready on this domain:** read the explanations of anything you missed, then spend your study time on your weakest domain.

Read your result as a range, not a point. A domain with few questions moves a whole band with one answer: Domain 4 has only 7 questions here, so a single miss or lucky guess changes its percentage by about 14 points. Two practice exams on different days, each taken once and unseen, give a steadier picture than one.

> **Note:** a practice score is not a prediction of your exam score. These are our questions, written from AWS's public exam guide; they aren't AWS's, they aren't scaled the way the exam is, and real exam forms differ from each other. Use the result to decide what to study next, not whether you'll pass.

---

"Practice exam 2" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
