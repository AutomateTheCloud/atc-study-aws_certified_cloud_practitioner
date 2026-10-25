---
type: check
id: clf-90-05
title: "Practice exam 1"
tasks: ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "4.1", "4.2", "4.3"]
objectives: []
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 13; 90 minutes for the exam and about an hour to review it"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00, clf-10-00, clf-11-00, clf-12-00, clf-13-00]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html"
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://aws.amazon.com/cloud-adoption-framework/"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://aws.amazon.com/compliance/programs/"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html"
  - "https://aws.amazon.com/premiumsupport/plans/"
---

# Practice exam 1: a full 65-question form, timed and weighted like the CLF-C02 exam

Sixty-five questions in 90 minutes, spread across all four domains and all 19 task statements in the same proportions as the real exam. Take it in one sitting, closed book, then score each domain separately to see where you're ready and what to restudy.

**For:** an adult studying alone, possibly new to IT, who has finished Modules 02 to 13 of this guide (start from the [Module 02 brief](../02-why-the-cloud/00-brief.md) if you haven't). **Time:** 90 minutes for the questions, and about an hour to go through the answer key. No AWS account is needed.

## How to take it

- **Set a timer for 90 minutes** and work in one sitting, as on exam day. Closed book: no notes, no guide pages, no searching. If you will take the exam in English as a non-native speaker with the extra 30 minutes, set 120.
- **Write your answers down** as you go (question number and letter), and don't open the answer key until you have answered all 65. Answer every question: on the real exam a blank counts as wrong and a wrong guess costs nothing.
- **Two question types**, as on the exam. Most questions have one correct answer out of four. 13 questions end with "(Select TWO.)" and have two correct answers out of five; they count only if both of your choices are right.
- **Score it by domain** with the table under the answer key. A domain score tells you what to do next; it doesn't predict your exam score.
- **Count it only once.** A form shows your readiness only the first time you take it. When you come back to it after restudying, treat it as practice, not as a readiness check.

Where the exam guide uses an older name for a service or plan, the questions use the exam's name and the answer key gives today's name. No question needs a price or a count. Facts were checked on 2026-10-24. The real exam has 65 questions too, but 15 of them are unscored trial questions that you can't identify ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md)); on this form, all 65 count.

## Questions

**1.** Four organizations are each considering moving one system from servers they own to pay-as-you-go cloud resources. For which system would trading fixed expense for variable expense most likely save the most money?

- A. A hospital's patient records system that runs at the same load around the clock, on servers bought last year
- B. A bank's internal ledger that processes about the same volume of transactions every night
- C. A factory's control system that runs at full capacity every hour of every day
- D. A tax-preparation website that is very busy for ten weeks a year and nearly idle the rest of the time

**2.** An online marketplace's website runs on EC2 instances in a public subnet, behind an Application Load Balancer. One block of IP addresses keeps sending abusive requests. Which two controls can block that address range? (Select TWO.)

- A. A deny rule for the range in the instances' security group
- B. AWS Shield Standard, with the range added to it
- C. A finding from Amazon Inspector about the range
- D. A deny rule for the range in the network ACL of the load balancer's subnets
- E. A rule in AWS WAF, on the load balancer, that blocks an IP set holding the range

**3.** A university's IT director wants to read AWS's own in-depth papers on disaster recovery approaches that span several services, before a planning workshop. Where should she look?

- A. AWS Support Center
- B. AWS Marketplace
- C. AWS whitepapers and guides
- D. AWS re:Post

**4.** An online newspaper's article search runs on a server type the team chose five years ago. The team now wants to test newer instance types, and managed and serverless options, as AWS releases them, and to move the search to whichever does the job best for its readers. Which pillar of the AWS Well-Architected Framework is this goal part of?

- A. Operational excellence
- B. Performance efficiency
- C. Reliability
- D. Sustainability

**5.** A bank's security team has used one vendor's intrusion prevention product for years. It wants to run the same product in front of its AWS workloads, with the charges on its AWS bill. Where should it look?

- A. AWS Trusted Advisor
- B. AWS Security Hub
- C. AWS Artifact
- D. AWS Marketplace

**6.** A veterinary clinic keeps its appointments in a PostgreSQL database on a server in its office. It wants to move the database to AWS and stop doing the operating system patches, database upgrades and backups itself, while its staff keep the same PostgreSQL queries and tools. Which option fits?

- A. Amazon ElastiCache
- B. Amazon DocumentDB
- C. Amazon RDS
- D. Amazon EC2, with PostgreSQL installed and run by the clinic

**7.** A sports-league startup has two jobs to run without provisioning or managing any servers: a short piece of code that runs each time a new score file lands in an Amazon S3 bucket, and a containerized web API that must answer requests all day. Which two services fit these jobs? (Select TWO.)

- A. AWS Lambda
- B. Amazon EC2
- C. Amazon ECR
- D. AWS Fargate
- E. AWS Outposts

**8.** A company's security team works from a dedicated security account. Its compliance tool, running in that account, must read resource settings in each of the company's other AWS accounts, and the company wants no IAM users or long-term keys in those accounts. Which approach fits?

- A. Add the security account to an IAM group in each of the other accounts
- B. Create an IAM user with an access key in each account and store the keys in the tool
- C. Give the tool the access keys of each account's root user
- D. Create a role in each account with read permissions, whose trust policy names the security account

**9.** A hotel group runs dozens of AWS accounts in AWS Organizations. Its security team wants one central policy that no security group in any account may allow SSH from anywhere on the internet, applied to accounts created later too, with a report of anything that doesn't comply. Which service fits?

- A. AWS Firewall Manager
- B. Amazon Inspector
- C. AWS WAF
- D. AWS Shield Advanced

**10.** A market research firm needs Microsoft SQL Server on Amazon EC2 for a six-week project. It owns no SQL Server licenses it could move, and it will delete the servers when the project ends. Which licensing approach fits best?

- A. Run SQL Server unlicensed, because AWS covers licensing for all software on EC2
- B. Use license-included instances, paying for SQL Server by the hour in the instance price
- C. Buy new licenses from Microsoft and run them on Dedicated Hosts
- D. Bring its own licenses to shared EC2 instances under License Mobility

**11.** A market-data company serves a trading API from two AWS Regions. Its clients only allow traffic to a short list of fixed IP addresses in their firewalls. The company wants each client's traffic to enter AWS's network at the edge location nearest the client and then reach the closest healthy Region, with no change to client settings if one Region fails. Which service fits?

- A. AWS Transit Gateway
- B. Amazon API Gateway
- C. AWS Global Accelerator
- D. An Application Load Balancer in each Region

**12.** A recruiting firm keeps thousands of uploaded résumés and identity documents in many Amazon S3 buckets. It wants to find out which buckets hold personal data, such as passport numbers, so that it knows what to protect first. Which service fits?

- A. Amazon Detective
- B. Amazon Inspector
- C. Amazon Macie
- D. AWS Shield

**13.** A startup is designing a new application that will use Amazon EC2, Amazon RDS and Amazon S3. Before it builds anything, it wants an estimate of the monthly cost to share with its investors. Which tool fits?

- A. AWS Budgets
- B. AWS Cost Explorer
- C. AWS Cost and Usage Report
- D. AWS Pricing Calculator

**14.** A fitness-tracking startup in Australia wants to find out whether people in Canada would pay for its app. Its point is that trying the idea is quick and cheap: a new setup on AWS running by the end of the week for a three-month trial, deleted with nothing left to pay for if few people sign up. Demand during the trial is expected to be small and steady. Which benefit is the team relying on most?

- A. Elasticity
- B. Economies of scale
- C. Agility
- D. Durability

**15.** A smart-thermostat maker stores each device's latest settings and readings, always fetched by device ID. Traffic swings from a few thousand to millions of requests an hour, and the team wants no database servers to size or patch. Which database fits?

- A. Amazon RDS for MySQL
- B. Amazon Redshift
- C. Amazon Neptune
- D. Amazon DynamoDB

**16.** A meal-planning app's backend runs on AWS Lambda. Every time a user saves a weekly plan, the backend must write it to an Amazon DynamoDB table. How should the backend's code make that request?

- A. With an AWS SDK for the language the backend is written in
- B. Through the AWS Management Console
- C. With an AWS CloudFormation template that creates the item
- D. With an AWS CLI script that a developer runs each evening

**17.** A car parts distributor plans to move 40 databases to AWS over the next year. Its architects want AWS-vetted guides and step-by-step patterns for planning and carrying out the work. Where should they look?

- A. AWS Prescriptive Guidance
- B. AWS Knowledge Center
- C. AWS Health Dashboard
- D. AWS Trusted Advisor

**18.** An import company receives scanned paper invoices from suppliers in France. It wants the text and fields pulled out of each scan automatically, and then the French text turned into English for its accounts team. Which two services should it use? (Select TWO.)

- A. Amazon Translate
- B. Amazon Polly
- C. Amazon Comprehend
- D. Amazon Rekognition
- E. Amazon Textract

**19.** A biotech company stores research files in Amazon S3. Some of the files contain volunteers' personal details. Under the AWS shared responsibility model, which task is the company's?

- A. Securing the network that links AWS's data centers
- B. Deciding which files are sensitive, and which encryption option protects them
- C. Keeping the S3 storage servers patched
- D. Making sure stored objects survive the failure of a storage device

**20.** A company's auditor wants a continuously updated score showing how the company's own AWS account settings measure up against AWS Foundational Security Best Practices, across all of its accounts. Which service provides this?

- A. Amazon Macie
- B. AWS Security Hub
- C. Amazon Inspector
- D. AWS Artifact

**21.** A new cloud team is writing onboarding notes about the AWS global infrastructure. Which two statements are correct? (Select TWO.)

- A. An Availability Zone is always exactly one data center building
- B. Customers can launch EC2 instances in edge locations to run servers close to users
- C. Each Region has at least three Availability Zones, which are physically separate from each other
- D. Edge locations are separate from Regions, sit in many more cities, and run services such as Amazon CloudFront
- E. AWS copies each resource to a second Region automatically, for safety

**22.** A bank's auditors require that every change to its AWS network and firewall settings is written down, reviewed by a second engineer and approved before it is applied, and that the whole setup can be rebuilt exactly after a disaster. Which approach fits?

- A. Describe the setup in AWS CloudFormation templates kept in version control
- B. Make changes in the AWS Management Console and record them in a change log afterwards
- C. Keep a set of AWS CLI commands that engineers run in order
- D. Have the bank's customer-facing app create the settings through an AWS SDK

**23.** A contractor will upload survey files into one folder (prefix) of one Amazon S3 bucket for three months. She needs to do nothing else in the account. Which permissions follow the principle of least privilege?

- A. The AWS managed policy PowerUserAccess
- B. Permission to upload objects, only under that prefix of that bucket
- C. Every S3 action, but only on that one bucket
- D. The AWS managed policy AmazonS3FullAccess, removed after three months

**24.** A ride-hailing company's trip-history service runs on EC2 instances in private subnets and writes every trip to an Amazon DynamoDB table in the same Region. The company wants that traffic to stay off the internet, with no NAT gateway, and with no extra charge for the connection itself. What should it add to the VPC?

- A. An AWS Site-to-Site VPN connection to DynamoDB
- B. A gateway VPC endpoint for DynamoDB, with a route to it in the private subnets' route table
- C. An interface VPC endpoint for DynamoDB in each Availability Zone, reached through private IP addresses
- D. An internet gateway, and public IP addresses on the instances

**25.** A music festival sells tickets online during a two-week window each spring. Two years ago it bought too few servers, and the ticket site crashed. Last year it bought too many, and most of them sat unused for the rest of the year. Which advantage of cloud computing addresses this problem most directly?

- A. Benefit from massive economies of scale
- B. Go global in minutes
- C. Stop guessing capacity
- D. Stop spending money running and maintaining data centers

**26.** A travel-booking company wants two things on AWS: continual scanning of its EC2 instances and container images for known software vulnerabilities, and alerts when activity in its account looks malicious, such as API calls from addresses known to be used by attackers. Which two services should it turn on? (Select TWO.)

- A. AWS Artifact
- B. Amazon Inspector
- C. Amazon Macie
- D. AWS Shield Standard
- E. Amazon GuardDuty

**27.** A retail group's leaders want an AWS framework to help them find the gaps in their organization's skills, governance and ways of working before they adopt the cloud, with guidance grouped by the stakeholders who own each area. Which AWS resource fits?

- A. AWS Pricing Calculator
- B. The AWS Well-Architected Framework
- C. The AWS Cloud Adoption Framework (AWS CAF)
- D. Migration Evaluator

**28.** A crop-insurance company wants its data scientists to build, train and deploy their own model that predicts hail-damage claims from its weather and claims history. No ready-made AI service answers this question. Which service fits?

- A. Amazon Polly
- B. Amazon Textract
- C. Amazon Rekognition
- D. Amazon SageMaker AI

**29.** A small software company is on Basic Support. It wants its own operations tool to read AWS Health events through the AWS Health API, and it wants to see every AWS Trusted Advisor check, not only some of them. What is the lowest-cost way to get both?

- A. Upgrade to AWS Enterprise Support
- B. Buy a Trusted Advisor subscription separately from its Support plan
- C. Turn on AWS Health separately in each Region it uses
- D. Upgrade to AWS Business Support+

**30.** An insurance company's leaders list what they expect from moving to AWS: less risk of the claims system failing or being breached during the busy season, and reliable energy and carbon figures they can publish for investors. Which two business outcomes of the AWS Cloud Adoption Framework (AWS CAF) match these expectations? (Select TWO.)

- A. Reduced business risk
- B. Improved environmental, social, and governance (ESG) performance
- C. Increased operational efficiency
- D. Reduced regulatory obligations
- E. Increased revenue

**31.** A dental imaging practice keeps patients' X-ray images for years. Each image is looked at about once a quarter, usually during a check-up, and must appear on screen within milliseconds. The images can't be recreated, so they must survive the loss of an Availability Zone. Which S3 storage class is the most cost-effective fit?

- A. S3 Glacier Instant Retrieval
- B. S3 Standard
- C. S3 Express One Zone
- D. S3 Glacier Deep Archive

**32.** A chain of veterinary clinics learns about problems with its appointment system only when receptionists phone the IT team. Nothing records how the system is behaving, so nobody can see a slowdown coming or tell afterwards what went wrong. The team lead wants the system to report its health continuously, with alerts the team can act on. Which pillar of the AWS Well-Architected Framework does this goal belong to?

- A. Reliability
- B. Performance efficiency
- C. Security
- D. Operational excellence

**33.** A regional newspaper's publisher has two reasons for moving its website to AWS. She has read that AWS can charge less per unit of computing than the paper could ever pay buying its own hardware, because AWS buys and runs equipment at enormous volume. And she wants a second site, close to readers in another country, running within the month. Which two advantages of cloud computing match her reasons? (Select TWO.)

- A. Stop spending money running and maintaining data centers
- B. Go global in minutes
- C. Benefit from massive economies of scale
- D. Trade fixed expense for variable expense
- E. Stop guessing capacity

**34.** A developer discovers that an IAM user's access key was pasted into a public code repository an hour ago. What should the team do right away?

- A. Make the repository private, so that the key stops working for anyone who copied it
- B. Deactivate and delete the access key, then check AWS CloudTrail for its use
- C. Change the IAM user's console password
- D. Turn on MFA for the account's root user

**35.** An online grocery serves customers only in Canada. Its website runs behind an Application Load Balancer. The company wants to block requests from other countries and to limit how many requests any single IP address can send in a short time. Which service should it use?

- A. A network ACL on the load balancer's subnets
- B. Amazon GuardDuty
- C. AWS Shield Standard
- D. AWS WAF

**36.** An animation studio's render servers write temporary scratch files to EC2 instance store volumes. Which two statements about instance store are correct? (Select TWO.)

- A. It is backed up with EBS snapshots
- B. It keeps its data when the instance is stopped and started again
- C. It sits on disks physically attached to the computer that runs the instance
- D. It can be detached from one instance and attached to another
- E. Its data survives a reboot, but is lost when the instance is stopped or terminated

**37.** A software company is bidding for a German public-sector contract. The buyer asks for proof that the company's cloud provider holds Germany's C5 attestation. Where does the company get AWS's C5 report?

- A. AWS Artifact
- B. AWS Security Hub
- C. Amazon Inspector
- D. AWS Config

**38.** A photo-sharing startup holds a design review of its AWS workload. Which two findings belong to the security pillar of the AWS Well-Architected Framework? (Select TWO.)

- A. Photos travel from the mobile app to the servers without encryption
- B. The whole service runs in a single Availability Zone
- C. All the engineers sign in with one shared administrator password
- D. The thumbnail service runs on an instance type too slow for its work
- E. Most servers sit idle overnight but keep running

**39.** An online marketplace startup stores its transaction records in Amazon DynamoDB, a service with no servers for customers to manage. Under the AWS shared responsibility model, which task is still the startup's?

- A. Upgrading the DynamoDB database software to new versions
- B. Replacing failed storage devices that hold the table's data
- C. Choosing which IAM roles and users may read and write the table
- D. Patching the operating systems of the servers that run DynamoDB

**40.** A craft brewery is comparing the cost of running its ordering system on its own servers with running it on AWS. Its draft counts only the purchase price of the servers on the on-premises side. Which two costs are missing from the on-premises side? (Select TWO.)

- A. Charges for data sent out from AWS to the internet
- B. Staff time to install, patch and repair the hardware
- C. An AWS Support plan fee
- D. Electricity and cooling for the server room
- E. A Savings Plans commitment

**41.** A software company's developers use the AWS CLI on their laptops with long-term access keys for their IAM users. The security team wants to stop giving people long-term keys, while keeping CLI access to the company's several AWS accounts. What should the company do?

- A. Store the access keys in Parameter Store and let developers fetch them when needed
- B. Have developers sign in through AWS IAM Identity Center and use the temporary credentials it provides for the CLI
- C. Create access keys for each account's root user and give them to team leads
- D. Keep the access keys, but rotate each one once a year and keep them in an encrypted file

**42.** A company bought a Regional Reserved Instance for a Linux EC2 instance type. Later it moves its matching instance from one Availability Zone to another in the same Region, keeping the same instance type. What happens to the discount?

- A. It stops applying, because every Reserved Instance's discount is tied to one Availability Zone
- B. It applies only after the company exchanges the Reserved Instance for a new one
- C. It keeps applying: a Regional Reserved Instance covers matching usage in any Availability Zone
- D. The Reserved Instance moves the instance back to the original Availability Zone

**43.** A nonprofit wants an email as soon as its projected AWS spending for the month is on track to pass the amount its board approved, before the money is actually spent. Which tool fits?

- A. AWS Cost Explorer, with its spending forecast
- B. AWS Budgets, with an alert on forecasted cost
- C. AWS Pricing Calculator, with a monthly estimate
- D. AWS Cost and Usage Report, delivered to S3

**44.** An online print shop's website hands each new order to a group of workers that prepare the print files. Workers are sometimes slow or offline; orders must wait until a worker is free, and each order must be prepared by only one worker. Which service fits?

- A. Amazon SES
- B. Amazon EventBridge
- C. Amazon SNS
- D. Amazon SQS

**45.** A card-payment processor and a hospital both run workloads on AWS. Which statement about their compliance needs is correct?

- A. Because AWS holds many certifications, both organizations are compliant as soon as their workloads run on AWS
- B. Compliance programs cover only data kept on premises, not data stored in AWS
- C. Different programs apply to each, such as PCI DSS for card data and HIPAA for health data, and each stays responsible for its own compliance
- D. Both follow one single AWS compliance program, so their obligations on AWS are identical, whatever data they hold

**46.** A city transit app runs on one large server. When that server fails, the whole app is down until someone rebuilds it. The team wants to run the app on several smaller servers instead, so that losing one doesn't stop it, and to rehearse recovering from failures regularly. Which pillar of the AWS Well-Architected Framework addresses these goals?

- A. Cost optimization
- B. Performance efficiency
- C. Reliability
- D. Operational excellence

**47.** A pension fund's auditor asks how the physical and environmental controls of the data centers that run its AWS workloads are carried out, such as who may enter the buildings and how power and cooling are kept running. How should the fund answer?

- A. They are inherited controls: AWS carries them out, and the fund gives the auditor AWS's third-party audit reports
- B. They don't apply in the cloud, so the auditor needs no evidence for them
- C. They are shared controls: the fund must inspect the data centers each year alongside AWS
- D. They are customer-specific controls: the fund must write its own procedures for the buildings

**48.** A property management firm's employees sign in to the AWS Management Console as IAM users. The firm wants to make those sign-ins harder to break into. Which two actions should it take? (Select TWO.)

- A. Turn on the password policy's setting that locks a user out after five wrong attempts
- B. Give each user an access key to use alongside the password
- C. Extend the IAM password policy so it also applies to the root user's password
- D. Set a custom IAM password policy that requires long passwords and blocks reuse of recent ones
- E. Require each user to register an MFA device, preferably a passkey or security key

**49.** A pet-supplies retailer is replacing its old office phone system. Its customer service staff should answer customer calls and chats from a web browser wherever they work, with each contact sent to the right queue, and with no telephone hardware for the company to buy or maintain. Which service fits?

- A. Amazon Connect
- B. Amazon SNS
- C. Amazon WorkSpaces
- D. Amazon Lex

**50.** A company wants to cut its EC2 costs with Spot Instances. Which two workloads are good fits? (Select TWO.)

- A. A fleet of test runners whose tests can be interrupted and run again
- B. Licensed software that must run on a physical server dedicated to the company
- C. A payment API that must answer every request without interruption
- D. Overnight image-rendering jobs that save their progress and can restart where they stopped
- E. The company's only production database server

**51.** A meditation app stores millions of short audio clips. The app on users' phones downloads whole clips over HTTPS, and the company doesn't want to plan or manage storage capacity. Which storage service fits?

- A. Amazon EFS
- B. Amazon S3
- C. EC2 instance store
- D. Amazon EBS

**52.** An operations engineer wants to stop every development EC2 instance on Friday evening and start them again on Monday morning, every week, using the tags that mark them as development instances. Which way of working with AWS fits this routine task best?

- A. An AWS SDK call added to the company's customer-facing website
- B. Clicking through the AWS Management Console each Friday and Monday
- C. An AWS CLI script, run on a schedule
- D. A new AWS CloudFormation template each week

**53.** Amazon GuardDuty raises a finding that one of a company's EC2 instances is looking up domain names linked to cryptocurrency mining. What does GuardDuty itself do about it?

- A. It tells AWS Shield to block those domain names for every resource in the account
- B. Nothing, until the company has turned on VPC Flow Logs and DNS logging itself
- C. It stops the instance automatically and keeps it stopped until an administrator reviews the finding
- D. It reports the finding; stopping or isolating the instance needs a response the company builds, for example with an Amazon EventBridge rule

**54.** A small accounting firm will run Windows Server on a few Amazon EC2 instances that it resizes often. It doesn't want to buy, track or prove compliance for Windows Server licenses itself, or to buy client access licenses. Which licensing approach fits?

- A. Its own Windows Server licenses on Dedicated Hosts, tracked with AWS License Manager
- B. Its own Windows Server licenses on shared instances, under License Mobility
- C. License-included Windows Server instances, paying for the license in the hourly price
- D. Unlicensed Windows Server, since AWS licenses all software on EC2

**55.** A packaging company's PostgreSQL database must run a vendor's monitoring agent that installs directly on the database server's operating system. Which option meets this requirement?

- A. Amazon Aurora PostgreSQL-Compatible Edition
- B. PostgreSQL installed and managed by the company on Amazon EC2
- C. Amazon RDS for PostgreSQL, with automated backups turned on
- D. Amazon DynamoDB

**56.** A national lottery's results website was knocked offline by a DDoS attack last year. For the next draw, the operator wants DDoS specialists at AWS it can call during an attack, detailed reports on attacks against its protected resources, and credits if an attack forces its servers to scale up. What should it subscribe to?

- A. AWS Shield Advanced
- B. AWS Firewall Manager
- C. AWS Shield Standard
- D. Amazon GuardDuty

**57.** A team new to containers has packaged its web services as container images. It doesn't use Kubernetes and doesn't want to learn it. It wants AWS's own service to start the containers, keep the right number running and replace any that fail. Which service fits?

- A. Amazon ECR
- B. AWS Batch
- C. Amazon ECS
- D. Amazon EKS

**58.** A logistics company moved one application to AWS as a pilot. It has served real customers for three months, and the company has measured the results. Leaders now want to extend the move to the rest of the business and make sure the expected benefits are realized and kept. Which phase of the cloud transformation journey in the AWS Cloud Adoption Framework (AWS CAF) is the company entering?

- A. Envision
- B. Align
- C. Launch
- D. Scale

**59.** A company wants to know which of its EC2 instances can actually be reached from the internet on an open port, worked out from its route tables, network ACLs and security groups. It wants findings, without any change to its traffic. Which service fits?

- A. Amazon Inspector
- B. AWS WAF
- C. AWS Shield Standard
- D. Amazon GuardDuty

**60.** A hotel-booking website based in Mexico runs in an AWS Region in North America. It is signing up many customers in Europe, who find the site slow because every request crosses the Atlantic. Which change uses the AWS Cloud's global reach to fix this?

- A. Run a copy of the site in an AWS Region in Europe
- B. Spread the site across more Availability Zones in its current Region
- C. Add Auto Scaling to the site in its current Region
- D. Move the site to a larger instance type in its current Region

**61.** A hospital network is planning its move to AWS. Its internal audit team asks who will make sure patient data is encrypted, that access to it is controlled, and that security incidents are detected and handled. Which perspective of the AWS Cloud Adoption Framework (AWS CAF) covers these capabilities?

- A. Governance
- B. Platform
- C. Operations
- D. Security

**62.** An airline's pricing engine keeps a very large in-memory database of fares and seat availability. Its servers run out of memory long before their processors get busy. Which EC2 instance family fits best?

- A. Accelerated computing
- B. Memory optimized
- C. Compute optimized
- D. Storage optimized

**63.** A translation agency keeps its client database in Amazon RDS and clients' documents in Amazon S3. Under the AWS shared responsibility model, which two tasks belong to AWS? (Select TWO.)

- A. Installing patches on the operating system that runs the RDS database
- B. Deciding which users and applications may read the documents in the bucket
- C. Choosing whether the documents are encrypted with a key the agency manages
- D. Configuring the database's security group to accept only the agency's application servers
- E. Replacing failed drives in the servers that store S3 data

**64.** A city's permit-application website runs on one EC2 instance and an Amazon RDS database, both in the same Availability Zone. The city wants the site to keep accepting applications if that Availability Zone fails. What should it do?

- A. Run instances in two Availability Zones behind a load balancer, and turn on a Multi-AZ deployment for the database
- B. Move the website to a larger instance type with more memory and faster processors
- C. Put Amazon CloudFront in front of the website
- D. Keep the single instance, and add an RDS read replica of the database in another Availability Zone

**65.** A shipping company's new security manager drafts a one-line summary of the AWS shared responsibility model for staff. Which summary is accurate?

- A. AWS and the company carry out every security task together, so neither of them owns any task on its own
- B. AWS secures the infrastructure that runs its services; the company secures what it puts on that infrastructure and how it configures it
- C. AWS becomes responsible for who can access the company's data once that data is stored in an AWS service
- D. The company secures the physical sites of the Availability Zones it chooses, and AWS secures everything else in the cloud

## Answer key

Open it only after you have answered all 65 questions. Each answer names its task statement in the exam guide, explains why the answer is right and why the most tempting wrong choice is wrong, and links to the section that teaches it.

<details><summary>Answer key</summary>

**1. D** ([Task 1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4))

Variable expense saves money when use varies and you give capacity back when demand falls. The tax site would otherwise own enough servers for its peak and leave them idle most of the year. The other three run at steady, predictable loads, so they have little idle capacity to give back; paying by use changes the shape of their bills more than the total. **Reread:** [Fixed expense becomes variable expense, which isn't the same as cheaper](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#fixed-expense-becomes-variable-expense-which-isnt-the-same-as-cheaper).

**2. D and E** ([Task 3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5))

A network ACL has allow and deny rules, so it can refuse a range at the subnet's edge, and AWS WAF can block requests from an IP set before they reach the instances. Security groups have allow rules only, Inspector reports exposure without blocking anything, and Shield Standard works automatically without customer rules. **Reread:** [A network ACL checks every packet entering or leaving a subnet, in number order](../07-connecting-it/02-filtering-traffic.md#a-network-acl-checks-every-packet-entering-or-leaving-a-subnet-in-number-order); [AWS WAF reads each web request and allows, blocks or challenges it](../09-protecting-and-governing/04-the-front-door.md#aws-waf-reads-each-web-request-and-allows-blocks-or-challenges-it).

**3. C** ([Task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3))

AWS's whitepapers and guides are longer papers on one topic across services, such as disaster recovery or the Well-Architected Framework. re:Post is a community question-and-answer site, Support Center is for cases about your own account, and Marketplace sells other companies' products. **Reread:** [AWS's free pages answer "how does this work?"](../12-getting-help/03-where-to-find-answers.md#awss-free-pages-answer-how-does-this-work).

**4. B** ([Task 1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2))

Performance efficiency asks whether you use the right kind and amount of resources as demand and technology change; [Experiment more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) and [Use serverless architectures](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) are two of its design principles. Reliability is about surviving failures, which the scenario doesn't mention, and sustainability measures energy and resources used, not how well the work is done. **Reread:** [Pillars that sound alike, side by side](../02-why-the-cloud/05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side).

**5. D** ([Task 2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4))

AWS Marketplace is a curated catalog of other companies' software, including security products such as firewalls and intrusion prevention, billed through your AWS bill. The bank still configures and runs the product itself. Artifact holds AWS's compliance reports, and Security Hub and Trusted Advisor report on your setup; none of them sells third-party products. **Reread:** [AWS Marketplace sells third-party security products, billed through AWS](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#aws-marketplace-sells-third-party-security-products-billed-through-aws).

**6. C** ([Task 3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4))

Amazon RDS runs PostgreSQL, and other relational engines, as a managed service: AWS patches the operating system and the database and takes the backups, and the clinic's queries keep working. EC2 is tempting because PostgreSQL runs there too, but then the clinic still patches, upgrades and backs up the database itself. ElastiCache is an in-memory cache, not the main database, and DocumentDB stores JSON documents, not PostgreSQL tables. **Reread:** [AWS recommends a managed database unless you have a reason not to](../05-storing-data/05-managed-or-self-managed-databases.md#aws-recommends-a-managed-database-unless-you-have-a-reason-not-to); [The database services side by side](../05-storing-data/05-managed-or-self-managed-databases.md#the-database-services-side-by-side).

**7. A and D** ([Task 3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3))

Lambda runs code when an event, such as a new S3 object, triggers it; Fargate, with Amazon ECS or EKS, runs containers that keep running, with no servers to manage. EC2 gives you servers to look after, Outposts puts AWS hardware in your own building, and ECR stores container images but runs nothing. **Reread:** [Lambda or Fargate: short event-driven work, or containers that keep running](../06-running-applications/03-containers-and-serverless.md#lambda-or-fargate-short-event-driven-work-or-containers-that-keep-running).

**8. D** ([Task 2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3))

A cross-account role lets an identity from another account assume it and receive temporary credentials, so the tool needs no users or keys in the other accounts; the security account must also allow the tool to assume the roles. An IAM group can contain only users of its own account, and root user keys should never exist. **Reread:** [Cross-account roles let another account in without new users](../04-shared-responsibility-and-access/05-credentials-and-federation.md#cross-account-roles-let-another-account-in-without-new-users).

**9. A** ([Task 2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4))

Firewall Manager applies policies for security groups, AWS WAF and Shield Advanced across every account in an organization, including new ones, and reports what doesn't comply. It needs AWS Organizations and AWS Config. WAF filters web requests, Shield Advanced adds DDoS protection, and Inspector reports open paths but enforces no policy. **Reread:** [Firewall Manager applies the same protections in every account](../09-protecting-and-governing/04-the-front-door.md#firewall-manager-applies-the-same-protections-in-every-account).

**10. B** ([Task 1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4))

License-included instances add the license to the hourly price, with no long-term commitment, and AWS handles the license compliance; that suits short, changing work. Bringing your own license needs licenses you already own (and, for shared instances, active Software Assurance), which the firm doesn't have. Buying licenses and dedicated hardware for six weeks costs far more, and AWS doesn't license software you install yourself. **Reread:** [License-included or bring your own license: who pays the software vendor](../13-moving-to-aws/04-the-business-case.md#license-included-or-bring-your-own-license-who-pays-the-software-vendor).

**11. C** ([Task 3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2))

Global Accelerator gives an application fixed IP addresses announced from AWS's edge locations, then carries the traffic over AWS's network to the best healthy endpoint, switching Regions without new addresses. A load balancer works inside one Region and its addresses aren't a fixed pair you can hand out; API Gateway is a managed entrance to your code in a Region, and Transit Gateway connects networks to each other, not users to an application. **Reread:** [Three services use the edge, each in its own way](../03-aws-around-the-world/04-the-edge.md#three-services-use-the-edge-each-in-its-own-way); [Global Accelerator gives fixed addresses and a fast path, but keeps no copies](../07-connecting-it/03-names-and-the-edge.md#global-accelerator-gives-fixed-addresses-and-a-fast-path-but-keeps-no-copies).

**12. C** ([Task 2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2))

Macie finds sensitive data, such as personal details, in S3, so you know what to protect. Inspector looks for software vulnerabilities and network exposure, Shield defends against DDoS attacks, and Detective helps investigate what happened after a security finding. **Reread:** [Macie finds sensitive data in S3, so you know what to protect](../09-protecting-and-governing/02-encryption.md#macie-finds-sensitive-data-in-s3-so-you-know-what-to-protect).

**13. D** ([Task 4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2))

The AWS Pricing Calculator estimates the cost of a design before it exists, from the usage you describe, and an estimate can be shared as a link or exported. Cost Explorer, Budgets and the Cost and Usage Report all work from spending that has already happened, so they have nothing to show for an application that doesn't exist yet. **Reread:** [AWS Pricing Calculator estimates a design before it exists](../11-paying-for-aws/03-estimate-watch-analyze.md#aws-pricing-calculator-estimates-a-design-before-it-exists).

**14. C** ([Task 1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1))

Agility is getting something new quickly and cheaply, and being free to throw it away if the idea fails. Elasticity is tempting because both happen fast, but elasticity changes the amount of the same thing as demand rises and falls; here the team is creating something new to test an idea. **Reread:** [Agility: getting something new takes minutes, not weeks](../02-why-the-cloud/03-telling-the-benefits-apart.md#agility-getting-something-new-takes-minutes-not-weeks).

**15. D** ([Task 3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4))

DynamoDB stores items by key, answers in single-digit milliseconds at any scale, and is serverless, with on-demand capacity for traffic that swings. RDS needs instances sized for the load, Neptune is a graph database for relationships, and Redshift is a data warehouse for analysis, not for an application's live reads and writes. **Reread:** [DynamoDB stores items by key, at any scale, with no servers to run](../05-storing-data/05-managed-or-self-managed-databases.md#dynamodb-stores-items-by-key-at-any-scale-with-no-servers-to-run).

**16. A** ([Task 3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1))

When a program calls AWS while it runs, it uses an SDK, which signs each request, picks up the function's role credentials and retries brief failures. The console and a CLI script need a person, and a CloudFormation template builds infrastructure, not the data an application writes. **Reread:** [An SDK puts AWS calls inside your own program](../08-building-and-operating/01-four-ways-in.md#an-sdk-puts-aws-calls-inside-your-own-program).

**17. A** ([Task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3))

Prescriptive Guidance collects guides and patterns from AWS experts for larger jobs such as migrations and modernization. The Knowledge Center answers common single problems ("How do I…?"), the Health Dashboard reports events on AWS's side, and Trusted Advisor checks your account's setup. **Reread:** [AWS's free pages answer "how does this work?"](../12-getting-help/03-where-to-find-answers.md#awss-free-pages-answer-how-does-this-work).

**18. A and E** ([Task 3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7))

Textract reads printed and handwritten text, forms and tables from scanned documents, and Translate changes text from one language to another. Rekognition can spot words in a picture, which makes it look like a fit, but it doesn't return a document's fields and structure. Comprehend finds meaning in text, and Polly turns text into speech. **Reread:** [Pictures and documents: Rekognition sees, Textract reads](../10-data-ai-and-more/02-ai-and-ml.md#pictures-and-documents-rekognition-sees-textract-reads); [Text in: Comprehend finds meaning, Translate changes the language](../10-data-ai-and-more/02-ai-and-ml.md#text-in-comprehend-finds-meaning-translate-changes-the-language).

**19. B** ([Task 2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1))

On S3, AWS names three customer jobs: the data, including which encryption options to use; classifying that data; and IAM permissions. Patching S3's servers, surviving device failures and the network between data centers are part of the infrastructure AWS runs. **Reread:** [You are responsible for security in the cloud, and how much depends on the service](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#you-are-responsible-for-security-in-the-cloud-and-how-much-depends-on-the-service).

**20. B** ([Task 2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2))

Security Hub (the exam's name; today this job is AWS Security Hub CSPM) checks your settings against standards such as AWS Foundational Security Best Practices, CIS and PCI DSS, turns the results into a security score, and works across accounts; it needs AWS Config recording. Artifact is tempting because it is about compliance, but its reports describe AWS's controls, not your settings. Inspector scans for vulnerabilities, and Macie finds sensitive data. **Reread:** [Security Hub gathers every finding and checks your settings, and the name now covers two products](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#security-hub-gathers-every-finding-and-checks-your-settings-and-the-name-now-covers-two-products).

**21. C and D** ([Task 3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2))

AWS states that every Region has at least three isolated, physically separate Availability Zones, and edge locations sit outside the Regions in many more cities, running CloudFront, Route 53 and Global Accelerator. An Availability Zone is one *or more* data centers; resources stay in their Region unless you copy them; and you can't run EC2 servers in an edge location. **Reread:** [A Region is at least three Availability Zones in one area](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md#a-region-is-at-least-three-availability-zones-in-one-area); [Edge locations deliver and answer close to users; they don't run your servers](../03-aws-around-the-world/04-the-edge.md#edge-locations-deliver-and-answer-close-to-users-they-dont-run-your-servers).

**22. A** ([Task 3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1))

Infrastructure as code describes the end result in files that can be reviewed before a change and deployed again to rebuild the same setup. A CLI command list is tempting because it is written down, but it repeats steps, not the end state, and may fail or duplicate resources on a second run. Console changes leave only the result behind. **Reread:** [Infrastructure as code describes the end result in a file](../08-building-and-operating/01-four-ways-in.md#infrastructure-as-code-describes-the-end-result-in-a-file).

**23. B** ([Task 2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3))

Least privilege grants only the actions the task needs (uploading), only on the resources it touches (that prefix), ideally with conditions too. Full S3 access and PowerUserAccess reach far beyond one folder, and all S3 actions on the bucket would also let her read, delete or change settings she doesn't need. **Reread:** [Least privilege: grant only what the task needs, then keep trimming](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md#least-privilege-grant-only-what-the-task-needs-then-keep-trimming).

**24. B** ([Task 3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5))

A gateway endpoint gives a VPC a private path to S3 or DynamoDB through a route-table entry, and it has no charge. An interface endpoint also keeps traffic private, but it bills by the hour in each Availability Zone and per GB. An internet gateway with public addresses would send the traffic over the internet path, and a Site-to-Site VPN links an office network, not a VPC to an AWS service. **Reread:** [VPC endpoints reach AWS services without the internet, and one kind is free](../07-connecting-it/01-your-own-network.md#vpc-endpoints-reach-aws-services-without-the-internet-and-one-kind-is-free).

**25. C** ([Task 1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1))

Both mistakes came from having to guess in advance how many servers the busiest days would need. In the cloud there is no fixed amount to choose: capacity can follow the demand. The other advantages are about location, price per unit and data-center chores, none of which caused either year's problem. **Reread:** [Six advantages, one picture](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#six-advantages-one-picture).

**26. B and E** ([Task 2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2))

Inspector scans EC2 instances, Lambda functions and container images in Amazon ECR for known vulnerabilities, continuously. GuardDuty reads account activity, network flows and DNS lookups and reports threats such as calls from known malicious addresses. Shield Standard absorbs network floods, Artifact holds AWS's audit reports, and Macie finds sensitive data in S3. **Reread:** [GuardDuty watches activity and reports threats happening now](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#guardduty-watches-activity-and-reports-threats-happening-now); [Inspector scans workloads and reports weaknesses before an attacker finds them](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#inspector-scans-workloads-and-reports-weaknesses-before-an-attacker-finds-them).

**27. C** ([Task 1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3))

The AWS CAF lists the capabilities an organization needs for cloud adoption, grouped into six perspectives, each owned by a set of stakeholders. It's easy to pick the Well-Architected Framework because it's also a framework, but it reviews the design of a workload, not the organization's readiness. Migration Evaluator builds a cost case, and the Pricing Calculator estimates a design. **Reread:** [Six perspectives group the capabilities, each owned by different people](../13-moving-to-aws/01-the-cloud-adoption-framework.md#six-perspectives-group-the-capabilities-each-owned-by-different-people); [The CAF and the 7 Rs work at different levels](../13-moving-to-aws/01-the-cloud-adoption-framework.md#the-caf-and-the-7-rs-work-at-different-levels).

**28. D** ([Task 3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7))

When no ready-made service fits, SageMaker AI (formerly Amazon SageMaker) is where you build, train and deploy your own models. Textract reads documents, Polly speaks text aloud and Rekognition analyzes images; each does one ready-made job. **Reread:** [When nothing ready-made fits, SageMaker AI builds your own model](../10-data-ai-and-more/02-ai-and-ml.md#when-nothing-ready-made-fits-sagemaker-ai-builds-your-own-model).

**29. D** ([Task 4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3))

The AWS Health API and the full set of Trusted Advisor checks come with Business Support+ and the plans above it; on Basic, the Health API refuses the call and only some checks show. Enterprise Support also includes both but costs far more, adding a designated Technical Account Manager the company didn't ask for. AWS Health needs no switching on, and Trusted Advisor has no price of its own: what you see depends on your Support plan. **Reread:** [Trusted Advisor checks your setup in six categories, and your plan sets how much you see](../12-getting-help/02-tools-that-watch-your-account.md#trusted-advisor-checks-your-setup-in-six-categories-and-your-plan-sets-how-much-you-see); [AWS Health reports problems on AWS's side, in one dashboard with two views](../12-getting-help/02-tools-that-watch-your-account.md#aws-health-reports-problems-on-awss-side-in-one-dashboard-with-two-views).

**30. A and B** ([Task 1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3))

Less risk of failure or a breach is reduced business risk, which the CAF describes as better reliability, performance and security, and published energy and carbon figures are ESG performance. Increased revenue and operational efficiency are the CAF's other two outcomes, but nothing in the list is about new sales or lower running costs. Reduced regulatory obligations isn't a CAF outcome: moving to AWS doesn't remove the laws that apply to the company. **Reread:** [The CAF aims at four business outcomes](../13-moving-to-aws/01-the-cloud-adoption-framework.md#the-caf-aims-at-four-business-outcomes).

**31. A** ([Task 3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6))

Glacier Instant Retrieval is the archive class for data read about once a quarter that must still come back in milliseconds, with copies in several Availability Zones; AWS gives medical images as a typical use. S3 Standard would work but charges more to store data read so rarely. Deep Archive needs a restore that takes hours, and Express One Zone keeps data in a single zone. **Reread:** [Storage classes: how often, how fast, how replaceable](../05-storing-data/02-s3-in-practice.md#storage-classes-how-often-how-fast-how-replaceable).

**32. D** ([Task 1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2))

Operational excellence asks whether you can run a workload well, see what it is doing and keep improving; [Implement observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) is one of its design principles. Reliability is tempting because unnoticed problems can become outages, but the gap here is being able to see and act on how the system behaves, which is operations. **Reread:** [Six pillars, six questions](../02-why-the-cloud/05-the-well-architected-framework.md#six-pillars-six-questions).

**33. B and C** ([Task 1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1))

Lower prices per unit because the provider operates at huge scale is the economies-of-scale advantage, and a site near foreign readers within a month is going global in minutes. The other three are real advantages, but her reasons say nothing about data-center chores, sizing capacity in advance or paying as you go. **Reread:** [Six advantages, one picture](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#six-advantages-one-picture); [Economies of scale: a very large provider can charge less per unit](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#economies-of-scale-a-very-large-provider-can-charge-less-per-unit).

**34. B** ([Task 2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3))

An access key keeps working until someone deactivates or deletes it, so a leaked key must be switched off at once, and CloudTrail shows what was done with it. Hiding the repository doesn't stop a copied key, and the console password and root MFA protect other credentials, not this key. **Reread:** [Access keys are long-term secrets: avoid them where you can](../04-shared-responsibility-and-access/05-credentials-and-federation.md#access-keys-are-long-term-secrets-avoid-them-where-you-can); [CloudTrail records who did what, when and from where](../09-protecting-and-governing/01-who-did-what.md#cloudtrail-records-who-did-what-when-and-from-where).

**35. D** ([Task 2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4))

AWS WAF attaches to an Application Load Balancer and applies rules to each web request, including rules that match the country a request comes from and rate-based rules that limit requests per address. A network ACL sees only addresses, ports and protocols. Shield Standard absorbs network-level floods without applying your rules, and GuardDuty reports threats but blocks nothing. **Reread:** [AWS WAF reads each web request and allows, blocks or challenges it](../09-protecting-and-governing/04-the-front-door.md#aws-waf-reads-each-web-request-and-allows-blocks-or-challenges-it).

**36. C and E** ([Task 3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6))

Instance store is temporary block storage on the host computer's own disks: a reboot keeps its data, but a stop, hibernation or termination erases it, which is fine for scratch files. Detaching and reattaching a volume, and backing it up with snapshots, are features of Amazon EBS. **Reread:** [Block storage: a disk attached to one server](../05-storing-data/01-block-file-object.md#block-storage-a-disk-attached-to-one-server).

**37. A** ([Task 2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2))

AWS Artifact gives you AWS's own security and compliance documents on demand, including country-specific ones such as Germany's C5 alongside SOC, ISO and PCI reports. Config, Security Hub and Inspector all report on *your* resources; none of them holds AWS's audit reports. **Reread:** [AWS Artifact hands you AWS's audit reports, not a verdict on you](../09-protecting-and-governing/05-compliance-and-governance.md#aws-artifact-hands-you-awss-audit-reports-not-a-verdict-on-you); [AWS lists its compliance programs, and which services each one covers](../09-protecting-and-governing/05-compliance-and-governance.md#aws-lists-its-compliance-programs-and-which-services-each-one-covers).

**38. A and C** ([Task 1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2))

A shared administrator password breaks [Implement a strong identity foundation](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html), and unencrypted uploads break [Protect data in transit and at rest](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html): both are security. A too-slow instance type is performance efficiency, a single Availability Zone is reliability, and idle servers are cost optimization and sustainability. **Reread:** [Six pillars, six questions](../02-why-the-cloud/05-the-well-architected-framework.md#six-pillars-six-questions).

**39. C** ([Task 2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1))

However much AWS runs, who can reach your data stays yours: the startup grants access to its table through IAM. Servers, storage hardware and the database software under a managed service like DynamoDB are AWS's to patch, replace and upgrade. **Reread:** [Your data, and who can reach it, are always yours](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#your-data-and-who-can-reach-it-are-always-yours).

**40. B and D** ([Task 1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4))

Owning servers brings power, cooling and the people who look after the hardware, along with space, network, licenses and the next hardware refresh. Data transfer out, a Savings Plans commitment and a Support plan are costs of the AWS side of the comparison, not of staying on premises. **Reread:** [On-premises costs come in seven groups](../02-why-the-cloud/04-what-a-data-center-really-costs.md#on-premises-costs-come-in-seven-groups).

**41. B** ([Task 2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3))

IAM Identity Center gives people one sign-in, with MFA, to many accounts, and hands out temporary credentials through roles, so nobody holds a long-term key. Rotating or storing the keys elsewhere leaves long-term keys in people's hands, and root user access keys are the most dangerous credential an account can have. **Reread:** [Access keys are long-term secrets: avoid them where you can](../04-shared-responsibility-and-access/05-credentials-and-federation.md#access-keys-are-long-term-secrets-avoid-them-where-you-can); [Federation: sign in once, elsewhere, and receive temporary access](../04-shared-responsibility-and-access/05-credentials-and-federation.md#federation-sign-in-once-elsewhere-and-receive-temporary-access).

**42. C** ([Task 4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1))

A Reserved Instance is a billing discount on matching running usage, not a machine. Regional scope means the discount follows matching instances to any Availability Zone in the Region (and, for Linux on shared tenancy, to other sizes in the family); only a zonal Reserved Instance is tied to one zone, in exchange for reserving capacity there. **Reread:** [Reserved Instances: a billing discount on a matching configuration](../11-paying-for-aws/02-purchasing-options.md#reserved-instances-a-billing-discount-on-a-matching-configuration).

**43. B** ([Task 4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2))

AWS Budgets can alert when its forecast for the period will pass a threshold, warning before the money is spent; it sends alerts and stops nothing unless you add a budget action. Cost Explorer forecasts and analyzes spending but doesn't send threshold alerts, the Pricing Calculator estimates a design before it exists, and the Cost and Usage Report delivers line items. **Reread:** [AWS Budgets tells you when you pass a limit; it stops nothing unless you add an action](../11-paying-for-aws/03-estimate-watch-analyze.md#aws-budgets-tells-you-when-you-pass-a-limit-it-stops-nothing-unless-you-add-an-action).

**44. D** ([Task 3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8))

SQS holds messages in a queue until a worker pulls one, so work waits safely while workers are busy, and while one worker handles a message SQS hides it from the others. SNS pushes each message to every subscriber at once, SES sends email, and EventBridge routes events by rules rather than holding work for a pool of workers. **Reread:** [SQS holds work in a queue until a worker pulls it](../08-building-and-operating/04-connecting-parts-shipping-software.md#sqs-holds-work-in-a-queue-until-a-worker-pulls-it); [Choose by the shape of the message](../08-building-and-operating/04-connecting-parts-shipping-software.md#choose-by-the-shape-of-the-message).

**45. C** ([Task 2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2))

Compliance needs differ by industry and by country, and AWS's Compliance Programs page says customers remain responsible for the laws and regulations that apply to them. AWS's certifications cover AWS's side; each customer still configures its own workloads correctly and keeps its own evidence. **Reread:** [AWS lists its compliance programs, and which services each one covers](../09-protecting-and-governing/05-compliance-and-governance.md#aws-lists-its-compliance-programs-and-which-services-each-one-covers).

**46. C** ([Task 1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2))

Reliability asks whether a workload keeps doing its job and recovers when something fails; [Scale horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) and [Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) are two of its design principles. You might pick performance efficiency because the change is about servers, but the app isn't too slow; the risk is that it stops working. **Reread:** [Pillars that sound alike, side by side](../02-why-the-cloud/05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side).

**47. A** ([Task 2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1))

Physical and environmental controls are AWS's example of inherited controls: AWS does all of the work, and customers can't enter its buildings. Inheriting a control doesn't remove the need for evidence; AWS's independent audit reports, from AWS Artifact, are that evidence. **Reread:** [Inherited controls: AWS does all of it](../04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md#inherited-controls-aws-does-all-of-it).

**48. D and E** ([Task 2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3))

A strong password policy and MFA together protect a person's sign-in, and passkeys and security keys also resist phishing. The IAM password policy has no lockout setting, and it doesn't cover the root user. An access key is an extra long-term secret, not a sign-in protection. **Reread:** [Passwords and MFA protect a person's sign-in](../04-shared-responsibility-and-access/05-credentials-and-federation.md#passwords-and-mfa-protect-a-persons-sign-in).

**49. A** ([Task 3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8))

Amazon Connect (now named Amazon Connect Customer) runs a cloud contact center: phone numbers, queues and routing, and a browser workspace for agents, with no telephone hardware. Lex is tempting because it can be the bot inside Connect, but it doesn't run a contact center. SNS sends notifications, and WorkSpaces gives people a whole cloud desktop. **Reread:** [Connect runs the contact center; Lex is the bot inside it](../10-data-ai-and-more/03-people-apps-and-devices.md#connect-runs-the-contact-center-lex-is-the-bot-inside-it).

**50. A and D** ([Task 4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1))

Spot Instances use spare capacity at a deep discount, but EC2 can interrupt them with a two-minute notice, so they suit work that can stop and pick up again. A sole production database and a payment API can't tolerate interruption, and software that needs a dedicated physical server points to Dedicated Hosts. **Reread:** [Spot Instances: deep discounts for work that can stop](../11-paying-for-aws/02-purchasing-options.md#spot-instances-deep-discounts-for-work-that-can-stop).

**51. B** ([Task 3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6))

S3 is object storage: whole files in a bucket, read through a web API by any program with permission, with no capacity to plan. EBS and instance store are block storage attached to one server, and EFS is a shared file system that servers mount; none of them serves files straight to apps over the web. **Reread:** [Object storage: whole objects in a bucket, reached over the web](../05-storing-data/01-block-file-object.md#object-storage-whole-objects-in-a-bucket-reached-over-the-web).

**52. C** ([Task 3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1))

A routine task on resources that already exist suits a saved CLI script: written once, run the same way every week. The console means repeating the same clicks by hand, CloudFormation builds and changes whole setups rather than stopping and starting instances on a timetable, and an SDK belongs in a program that uses AWS as part of its own work. **Reread:** [One-time or repeatable: the question that picks the way in](../08-building-and-operating/01-four-ways-in.md#one-time-or-repeatable-the-question-that-picks-the-way-in).

**53. D** ([Task 2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4))

GuardDuty detects and reports; it doesn't stop anything. An automatic response, such as isolating the instance, is something you build, typically an EventBridge rule that reacts to the finding. GuardDuty reads DNS logs and flow logs on its own as soon as it is turned on, so no extra logging setup is needed for this finding. **Reread:** [GuardDuty watches activity and reports threats happening now](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#guardduty-watches-activity-and-reports-threats-happening-now).

**54. C** ([Task 1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4))

With license-included instances the hourly price covers Windows Server, AWS handles license compliance, no client access licenses are needed, and the firm can resize or stop at any time. Bringing its own licenses would make compliance the firm's job; Windows Server also isn't eligible for License Mobility, so its own licenses would need Dedicated Hosts. **Reread:** [License-included or bring your own license: who pays the software vendor](../13-moving-to-aws/04-the-business-case.md#license-included-or-bring-your-own-license-who-pays-the-software-vendor).

**55. B** ([Task 3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4))

AWS recommends a managed database by default, but RDS and Aurora don't give you the database server's operating system, because AWS runs that layer. Software that needs the operating system is one of the few reasons to run the database yourself on EC2, accepting the patching, backups and failover work that comes with it. DynamoDB isn't PostgreSQL at all. **Reread:** [AWS recommends a managed database unless you have a reason not to](../05-storing-data/05-managed-or-self-managed-databases.md#aws-recommends-a-managed-database-unless-you-have-a-reason-not-to).

**56. A** ([Task 2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4))

Shield Advanced is the paid tier that adds the Shield Response Team, attack visibility and DDoS cost protection for the resources you choose. Shield Standard already protects every account at no extra charge, but has no one to call and no cost protection. AWS's page also says the Shield Response Team needs a Business or Enterprise Support plan (checked 2026-10-24). **Reread:** [Shield Advanced adds detection, people and bill protection, for a price](../09-protecting-and-governing/04-the-front-door.md#shield-advanced-adds-detection-people-and-bill-protection-for-a-price).

**57. C** ([Task 3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3))

Amazon ECS is AWS's own container orchestrator: it starts tasks, keeps services at the right count and replaces failed copies. EKS also orchestrates, but with Kubernetes, which the team wants to avoid. ECR only stores images, and AWS Batch runs large numbers of jobs from a queue rather than keeping services running. **Reread:** [Four names, four jobs: ECR stores, ECS and EKS orchestrate, Fargate supplies the computers](../06-running-applications/03-containers-and-serverless.md#four-names-four-jobs-ecr-stores-ecs-and-eks-orchestrate-fargate-supplies-the-computers).

**58. D** ([Task 1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3))

Scale expands the pilots to the size the business needs and makes sure the benefits are realized and sustained. Launch is the phase the company has just finished: delivering pilots in production. Envision chooses the outcomes, and Align finds the gaps in capabilities across the six perspectives. **Reread:** [Four phases, repeated: Envision, Align, Launch, Scale](../13-moving-to-aws/01-the-cloud-adoption-framework.md#four-phases-repeated-envision-align-launch-scale).

**59. A** ([Task 3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5))

Inspector reports unintended network exposure: a real path from the internet to a port, worked out from routes, network ACLs and security groups. It finds open paths and blocks nothing. WAF and Shield act on traffic, and GuardDuty reports suspicious activity, not which paths are open. **Reread:** [Amazon Inspector finds open paths; it doesn't block anything](../07-connecting-it/02-filtering-traffic.md#amazon-inspector-finds-open-paths-it-doesnt-block-anything).

**60. A** ([Task 1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1))

Global reach means running in Regions close to your users, so their requests travel a short distance; a copy in a European Region shortens the trip for European customers. A larger instance, Auto Scaling and more Availability Zones all add capacity or resilience in the same place, so every European request still crosses the ocean. **Reread:** [Global reach: run close to users anywhere, in minutes](../02-why-the-cloud/03-telling-the-benefits-apart.md#global-reach-run-close-to-users-anywhere-in-minutes).

**61. D** ([Task 1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3))

Data protection, identity and access management, threat detection and incident response are capabilities of the Security perspective, whose stakeholders include internal audit. Governance is tempting because of the words "audit" and "oversight", but it oversees the transformation program itself: projects, benefits, risk and cloud spending. Ask what is at stake (protecting data and systems), not who is asking. **Reread:** [Six perspectives group the capabilities, each owned by different people](../13-moving-to-aws/01-the-cloud-adoption-framework.md#six-perspectives-group-the-capabilities-each-owned-by-different-people); [Map a concern by asking what is at stake, not who is asking](../13-moving-to-aws/01-the-cloud-adoption-framework.md#map-a-concern-by-asking-what-is-at-stake-not-who-is-asking).

**62. B** ([Task 3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3))

Choose the family by what runs out first: memory points to memory optimized, which AWS lists for in-memory databases. Compute optimized is for processor-bound work, storage optimized for fast reads and writes to local disks, and accelerated computing for work on GPUs or other special chips. **Reread:** [Choose the family from the bottleneck](../06-running-applications/01-ec2.md#choose-the-family-from-the-bottleneck).

**63. A and E** ([Task 2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1))

AWS secures the infrastructure under its services, and on a managed service such as RDS that includes the operating system and database software. Who may read the documents, which network sources can reach the database, and which encryption key option to use are the agency's settings, because they concern its data and who can reach it. **Reread:** [AWS is responsible for security of the cloud](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#aws-is-responsible-for-security-of-the-cloud); [Your data, and who can reach it, are always yours](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#your-data-and-who-can-reach-it-are-always-yours).

**64. A** ([Task 3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2))

High availability means no zonal part exists in only one Availability Zone: a second web server in another zone with a load balancer sending users to healthy ones, and a Multi-AZ standby that takes over for the database. A read replica takes read-only work off the database and doesn't keep it running, and the single web server would still fail with its zone. A bigger instance and CloudFront leave the single points of failure in place. **Reread:** [High availability means running in more than one Availability Zone](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md#high-availability-means-running-in-more-than-one-availability-zone).

**65. B** ([Task 2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1))

That is the split AWS calls security *of* the cloud and security *in* the cloud. Access to the data stays with the customer wherever it is stored, AWS alone secures its physical sites, and "shared" means each side does its own part, not that both do every task together. **Reread:** [AWS is responsible for security of the cloud](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#aws-is-responsible-for-security-of-the-cloud); ["Shared" doesn't mean both sides do the same task](../04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md#shared-doesnt-mean-both-sides-do-the-same-task).

</details>

## Score by domain

Count your correct answers in each domain. A "(Select TWO.)" question counts only if both choices are right. Then find your band.

| Domain | Share of the exam | Questions on this form | Below 60%: restudy | 60% to 79%: review the linked sections | 80% or more: ready on this domain |
|---|---|---|---|---|---|
| Domain 1: Cloud Concepts | 24% | 16 | 0 to 9 | 10 to 12 | 13 to 16 |
| Domain 2: Security and Compliance | 30% | 20 | 0 to 11 | 12 to 15 | 16 to 20 |
| Domain 3: Cloud Technology and Services | 34% | 22 | 0 to 13 | 14 to 17 | 18 to 22 |
| Domain 4: Billing, Pricing, and Support | 12% | 7 | 0 to 4 | 5 | 6 to 7 |

Which questions belong to which domain:

- **Domain 1: Cloud Concepts:** questions 1, 4, 10, 14, 25, 27, 30, 32, 33, 38, 40, 46, 54, 58, 60, 61.
- **Domain 2: Security and Compliance:** questions 5, 8, 9, 12, 19, 20, 23, 26, 34, 35, 37, 39, 41, 45, 47, 48, 53, 56, 63, 65.
- **Domain 3: Cloud Technology and Services:** questions 2, 6, 7, 11, 15, 16, 18, 21, 22, 24, 28, 31, 36, 44, 49, 51, 52, 55, 57, 59, 62, 64.
- **Domain 4: Billing, Pricing, and Support:** questions 3, 13, 17, 29, 42, 43, 50.

What to do with each band:

- **Restudy:** go back to the module lessons for that domain, redo their labs or simulations, and take the module mastery checks again before another full form.
- **Review the linked sections:** reread the section linked beside each question you missed, and write one sentence on why the right answer beats the choice you picked.
- **Ready on this domain:** keep it fresh with short mixed practice, and spend most of your time on the domains below 80%.

For an overall figure, weight each domain's percentage by its share of the exam: 0.24 × Domain 1 + 0.30 × Domain 2 + 0.34 × Domain 3 + 0.12 × Domain 4. Read every result as a range, not a point. On 65 questions, three or four lucky or unlucky answers move the total by about five points, and Domain 4 has only seven questions, so one answer moves it by about fourteen.

**A practice score is not a prediction of your exam score.** The real exam reports a scaled score from 100 to 1,000 with a pass mark of 700, uses different questions, and includes unscored ones. What this form can tell you is which domains need more study. Before booking, take a second form you haven't seen, and check that your weaker domains have moved up.

---

"Practice exam 1" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
