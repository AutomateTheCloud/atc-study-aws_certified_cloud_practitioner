---
type: check
id: clf-90-04
title: "Mixed set 3: Modules 02 to 13"
tasks: ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "4.1", "4.2", "4.3"]
objectives: []
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 13; about 45 minutes"
prerequisites: [clf-02-00, clf-03-00, clf-04-00, clf-05-00, clf-06-00, clf-07-00, clf-08-00, clf-09-00, clf-10-00, clf-11-00, clf-12-00, clf-13-00]
pillars: [security, reliability, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html"
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://aws.amazon.com/savingsplans/faq/"
---

# Mixed set 3: thirty questions across all the teaching modules, shuffled together

This set has thirty questions in the exam's style, drawn from every teaching module, Modules 02 to 13, and weighted like the exam. It's the last mixed set before the practice exams, and the first that can ask about anything the exam covers.

**For:** an adult studying alone, possibly new to IT, who has finished Modules 02 to 13. **Time:** about 45 minutes, plus time to go through the answer key.

## What this set assumes

You've finished Modules 02 to 13 and their mastery checks, up to [Module 10: Data, AI and the rest of the catalog](../10-data-ai-and-more/00-brief.md), [Module 11: Paying for AWS](../11-paying-for-aws/00-brief.md), [Module 12: Getting help](../12-getting-help/00-brief.md) and [Module 13: Moving to AWS](../13-moving-to-aws/00-brief.md). [Mixed set 1](02-mixed-set-1.md) and [Mixed set 2](03-mixed-set-2.md) covered Modules 02 to 09; this set leans on Modules 10 to 13 (analytics and AI, paying for AWS, getting help, and moving to AWS), which no mixed set has asked about yet, and keeps the earlier modules in play. The capstone, Module 14, adds no new exam content, so you can take this set before or after it.

The set is weighted like the exam's domains, 24/30/34/12: 7 questions on Domain 1 (Cloud Concepts), 9 on Domain 2 (Security and Compliance), 10 on Domain 3 (Cloud Technology and Services) and 4 on Domain 4 (Billing, Pricing, and Support). [How to use the exam preparation](01-how-to-use-exam-prep.md) explains where this set fits.

## How to take it

- **Closed book.** No lessons, notes or searching.
- **Time yourself:** about 45 minutes for all 30, close to the exam's pace of 90 minutes for 65 questions.
- **Answer every question before you open the answer key.** There is no penalty for a wrong guess on the exam, so never leave one blank. Write your answers on paper as you go.
- **"(Select TWO.)"** means exactly two choices are right. As on the exam, the question scores only if you choose both.
- **Then score it by domain** with the table at the end, and reread the linked section for every question you missed or guessed.

## Questions

**1.** A public broadcaster has started a cloud adoption program. Its program office must track the program's benefits and spending against the plan, manage the risks, and keep software license use within its contracts. Which perspective of the AWS Cloud Adoption Framework (AWS CAF) covers these concerns?

- A. Business
- B. Governance
- C. Operations
- D. Platform

**2.** A city's open-data team keeps years of bus-ridership records as CSV files in Amazon S3. A few times a month, analysts want to run SQL queries on the files where they are, without loading them into a database or running any servers. Which service fits?

- A. Amazon Redshift
- B. AWS Glue
- C. Amazon Quick Sight
- D. Amazon Athena

**3.** A company suspects that someone downloaded objects from one of its S3 buckets last week. Its security lead searches CloudTrail event history and finds the bucket's creation and policy changes, but no record of any object being read. What explains this?

- A. CloudTrail doesn't record anything about Amazon S3
- B. Object reads are data events, which CloudTrail records only in a trail set up to log them; event history shows management events
- C. Object reads appear only in Amazon CloudWatch metrics, never in CloudTrail
- D. Event history keeps records for one day only

**4.** A startup set an AWS budget of $500 a month with an email alert at 100%. A forgotten test cluster pushed the month's spending to $900. The founder asks why AWS didn't stop at $500. Which answer is accurate?

- A. Budgets cap spending only on the Free plan, so the startup must open a support case
- B. The budget failed, because AWS Budgets always shuts down resources at the limit
- C. A budget only alerts; it stops nothing unless a budget action was set up, such as applying a restrictive policy or stopping chosen EC2 or RDS instances
- D. AWS Budgets can only forecast spending; it can't send alerts on actual costs

**5.** A pharmaceutical research group must run about 20,000 independent simulation jobs every weekend. It wants to submit them to a queue and have compute launched to run them and removed when they finish, without building that scheduling itself. Which service fits?

- A. AWS Batch
- B. AWS Elastic Beanstalk
- C. Amazon Lightsail
- D. AWS Outposts

**6.** A second-hand clothing marketplace uses Amazon Rekognition to label the photos that sellers upload. Under the AWS shared responsibility model, which TWO tasks belong to the marketplace? (Select TWO.)

- A. Training the model that recognizes the objects in images
- B. Deciding which people and programs may call Rekognition, through IAM policies
- C. Patching the servers that run Rekognition
- D. Protecting the uploaded photos and the labels, for example in private, encrypted S3 buckets
- E. Adding servers when the number of requests grows

**7.** A news website's traffic jumps whenever a big story breaks, and nobody can predict when that will be. The publisher doesn't want to keep extra servers idle all year "just in case". Which of AWS's advantages of cloud computing addresses this most directly?

- A. Go global in minutes
- B. Benefit from massive economies of scale
- C. Stop guessing capacity
- D. Stop spending money running and maintaining data centers

**8.** A tour operator hires 150 seasonal booking agents each summer. Each agent needs a full Windows desktop with the company's applications, reached from their own laptop at home, and the company wants to pay by the hour only while agents use them. Which service fits?

- A. Amazon Connect
- B. Amazon WorkSpaces Secure Browser
- C. Amazon WorkSpaces
- D. Amazon EC2 instances with a public IPv4 address for each agent

**9.** An online game publisher has suffered large DDoS attacks, including floods of web requests. It is considering a subscription to AWS Shield Advanced. Which TWO things does Shield Advanced add to the free AWS Shield Standard? (Select TWO.)

- A. Access to the Shield Response Team during an attack
- B. Blocking SQL injection in individual web requests without any AWS WAF rules
- C. Protection for the first time against common network floods
- D. Encryption of the traffic between players and the game servers
- E. DDoS cost protection against charges from scaling during an attack

**10.** A company moving its Windows Server and SQL Server workloads to Amazon EC2 owns no licenses it can bring along. It wants to pay for the software by the hour as part of the instance price, with no license tracking of its own. Which option fits?

- A. Bring your own license (BYOL) on Dedicated Hosts
- B. A Capacity Reservation
- C. Spot Instances
- D. License-included instances

**11.** A Canadian health insurer must keep its members' data in Canada under its regulator's rules. Its members live mostly in Toronto and Vancouver. When it chooses an AWS Region, which factor rules Regions out first?

- A. The Region with the lowest prices
- B. The Region with the most Availability Zones
- C. The rules on where the data may be stored
- D. The Region closest to the insurer's head office

**12.** An access review finds two IAM user access keys: one that hasn't been used for 200 days, and one that a developer uses every day from her laptop and hasn't changed in two years. Which TWO actions follow AWS's guidance? (Select TWO.)

- A. Delete the access key that hasn't been used
- B. Copy the developer's key to the rest of her team so they can work the same way
- C. Move the developer to temporary credentials for the command line, such as signing in through IAM Identity Center, and remove her long-term key
- D. Save both keys in the application's source code so they can't be lost
- E. Attach `AdministratorAccess` to both users so the keys never fail

**13.** A regional bank is sorting its applications into AWS's seven migration strategies. Which TWO pairings of strategy and plan are correct? (Select TWO.)

- A. Retire: switch off an old reporting tool that nobody has used for a year
- B. Rehost: rewrite the loans application as serverless functions
- C. Relocate: rebuild the payments system as microservices
- D. Repurchase: replace the in-house staff-rota application with a SaaS product
- E. Refactor: move the branch servers to EC2 without changing them

**14.** A ticketing company expects one very busy fortnight for a festival. It must be certain that a set number of a particular EC2 instance type will be available to it in one Availability Zone for those two weeks, and it won't sign a one-year or three-year commitment. Which option fits?

- A. Spot Instances
- B. An On-Demand Capacity Reservation
- C. A Compute Savings Plan
- D. Dedicated Instances

**15.** A growing software company wants to set up a new multi-account AWS environment that follows AWS's best practices from the start: separate accounts for logs and security, preventive and detective controls applied automatically, and a standard way to create each new account. Which service fits?

- A. AWS Control Tower
- B. AWS Service Catalog
- C. AWS Config
- D. AWS Artifact

**16.** A ticketing company must move its MySQL database from its own data center to Amazon RDS for MySQL. Customers keep buying tickets during the weeks the copy takes, and the switch-over may cause only a few minutes of downtime. Which approach fits?

- A. AWS Schema Conversion Tool (AWS SCT) alone, because it converts and copies the data
- B. A full load followed by ongoing replication with AWS Database Migration Service (AWS DMS), then a short cutover
- C. A nightly backup restored into RDS on the night of the switch-over
- D. AWS Snowball, to ship the database files

**17.** A software company turns on Amazon Inspector for its EC2 instances, AWS Lambda functions and container images. Which TWO of these findings would Inspector raise? (Select TWO.)

- A. A Lambda function packages a library version with a published CVE
- B. An IAM user is calling AWS APIs from a country the company never works in
- C. An S3 bucket holds a spreadsheet of customers' card numbers
- D. An EC2 instance can be reached from the internet on a port nobody meant to open
- E. The root user has no MFA

**18.** To save money, a team runs its test environment on a single instance in one Availability Zone, while production runs across three Availability Zones. Which pillar is the team trading away in the test environment, and does this fit the Well-Architected Framework's guidance?

- A. Reliability, and it is an acceptable trade-off for a test environment
- B. Security, and it is an acceptable trade-off for a test environment
- C. Reliability, and the Framework never allows a pillar to be traded
- D. Operational excellence, and it is an acceptable trade-off for a test environment

**19.** A travel site runs French and Spanish versions of its application in separate deployments. Visitors located in France must be sent to the French version and visitors in Spain to the Spanish one, based on where each visitor is. Which Amazon Route 53 routing policy fits?

- A. Latency routing
- B. Weighted routing
- C. Failover routing
- D. Geolocation routing

**20.** A company runs one application's data on Amazon RDS for PostgreSQL and another's on Amazon DynamoDB. Which task does the company have on RDS but not on DynamoDB?

- A. Choosing the database instance class and its storage size
- B. Deciding which people and programs may read the data
- C. Deciding what data to store and how sensitive it is
- D. Replacing failed hardware under the database

**21.** A manufacturer wants to move 40 servers from its data center to Amazon EC2 as they are, without changing the applications. It wants continuous block-level copying, test launches before the move, and a short cutover. Which service is built for this?

- A. AWS Database Migration Service (AWS DMS)
- B. AWS DataSync
- C. Migration Evaluator
- D. AWS Application Migration Service

**22.** A city council receives thousands of written comments on a new transport plan. It wants each comment marked as positive, negative or neutral automatically, and the streets and neighborhoods each one names picked out, without building a machine learning model. Which service fits?

- A. Amazon Translate
- B. Amazon Textract
- C. Amazon Transcribe
- D. Amazon Comprehend

**23.** A company is moving Windows servers that depend on Microsoft Active Directory to Amazon EC2. It wants the servers to join a managed Active Directory that runs in AWS, without running domain controllers itself. Which service fits?

- A. Amazon Cognito
- B. AWS Directory Service
- C. AWS IAM Identity Center
- D. IAM user groups

**24.** Six weeks ago, a team added the tag `project` to every resource in its standalone AWS account. In Cost Explorer, it still can't group its costs by `project`. What is missing?

- A. Tags take three months to reach cost reports
- B. Tags never appear in Cost Explorer; only the Cost and Usage Report can use them
- C. The tag must be activated as a cost allocation tag in the Billing console; it then appears in cost reports from then on
- D. The tag must be renamed to start with `aws:`

**25.** An administrator must add the same tag to 300 existing EC2 instances, once, this afternoon. The instances weren't created by any template. Which way of working fits best?

- A. Click through the AWS Management Console for each instance
- B. Write an AWS CloudFormation template that creates the 300 instances again with the tag
- C. Run AWS CLI commands, or a short script of them
- D. Build an application with an AWS SDK and deploy it to production

**26.** A company is planning service control policies (SCPs) for its accounts in AWS Organizations. Which TWO statements about SCPs are accurate? (Select TWO.)

- A. An SCP grants permissions to the users and roles in a member account
- B. An SCP sets the most that users and roles in a member account can do, including the account's root user
- C. SCPs don't apply to users and roles in the management account
- D. An SCP replaces the IAM policies in the accounts it is attached to
- E. SCPs apply to IAM users but not to IAM roles

**27.** Three months after moving its servers to Amazon EC2, a company wants recommendations, based on the measured use of each instance, for smaller or better-fitting instance types. It wants the recommendations only; it will make the changes itself. Which service fits?

- A. AWS Pricing Calculator
- B. Migration Evaluator
- C. AWS Compute Optimizer
- D. AWS Budgets

**28.** A vineyard installs 500 soil-moisture sensors that send readings over MQTT every few minutes. It wants a managed service that connects the devices securely and routes their messages, by rules, to other AWS services for storage and alerts. Which service fits?

- A. Amazon Kinesis Data Streams
- B. AWS IoT Core
- C. AWS Amplify
- D. Amazon SNS

**29.** A small company's web server logs show repeated login attacks coming from IP addresses that belong to AWS, apparently from another customer's EC2 instances. The company is on Basic Support. Where should it report the attacks?

- A. On the AWS Health Dashboard
- B. In a technical support case, which Basic Support doesn't allow, so it must upgrade first
- C. On AWS re:Post, so the instances' owner sees the post
- D. To AWS Trust & Safety, through AWS's abuse report form

**30.** A company is moving most of its servers with AWS Application Migration Service. One server must stay in its own data center for two more years under a contract, but the company wants it copied to AWS continuously, so that it can be launched there within minutes whenever that site fails. Which service fits that server?

- A. AWS Backup
- B. AWS DataSync
- C. AWS Application Migration Service, left running after a cutover
- D. AWS Elastic Disaster Recovery

## Answer key

Open the key only when you've answered every question.

<details><summary>Answer key</summary>

**1. B** · Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). The Governance perspective oversees how the program goes: benefits, spending and licenses, risk and program management. The Business perspective decides what is worth doing in the first place, Operations runs the services day to day, and Platform builds the technical foundation. Map a concern by what is at stake, not by who raises it. Reread: [Lesson 13.01, The Cloud Adoption Framework, "Business or Governance: deciding what to do, or overseeing how it goes"](../13-moving-to-aws/01-the-cloud-adoption-framework.md#business-or-governance-deciding-what-to-do-or-overseeing-how-it-goes).

**2. D** · Task [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7). Athena runs SQL directly on files in S3, with no servers, and charges for the queries run, which suits occasional questions. Redshift is a warehouse that data is loaded into for complex, repeated reporting. Glue catalogs and prepares data but doesn't answer questions, and Quick Sight draws dashboards from answers that something else produces. Reread: [Lesson 10.01, Analytics in five verbs, "Query: Athena, Redshift and EMR answer questions in three different ways"](../10-data-ai-and-more/01-analytics-in-five-verbs.md#query-athena-redshift-and-emr-answer-questions-in-three-different-ways).

**3. B** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). CloudTrail event history keeps 90 days of management events, such as creating a bucket or changing its policy, for free. Reading an object is a data event, which is off by default and is recorded only by a trail configured for it, so it has to be turned on before it's needed. CloudWatch metrics count activity but don't say who did it. Reread: [Lesson 09.01, Who did what, how it runs, how it was set, "CloudTrail records who did what, when and from where"](../09-protecting-and-governing/01-who-did-what.md#cloudtrail-records-who-did-what-when-and-from-where).

**4. C** · Task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2). AWS Budgets tells you when actual or forecasted cost or usage passes a limit, a few hours after the spending; on its own it caps nothing. Only a budget action does anything, and only what you set: apply an IAM policy or SCP, or stop chosen EC2 or RDS instances. Budgets alert on actual costs as well as forecasts. Reread: [Lesson 11.03, Estimate, watch, analyze, "AWS Budgets tells you when you pass a limit; it stops nothing unless you add an action"](../11-paying-for-aws/03-estimate-watch-analyze.md#aws-budgets-tells-you-when-you-pass-a-limit-it-stops-nothing-unless-you-add-an-action).

**5. A** · Task [3.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.3). Batch runs large numbers of jobs from a queue: it launches the compute they need and removes it afterwards, at no extra charge for Batch itself. Elastic Beanstalk builds and runs the setup for a web application's code, Lightsail sells a simple server as a bundle, and Outposts puts AWS hardware in your own building. Reread: [Lesson 06.04, Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts, "Batch runs large numbers of jobs from a queue"](../06-running-applications/04-simpler-paths.md#batch-runs-large-numbers-of-jobs-from-a-queue).

**6. B and D** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). Ready-made AI services sit far toward AWS's side of the line: AWS trains and runs the models and the servers, and scales them. Who may call the service, and the data sent to it and returned by it, stay with the customer, as on every service. Reread: [Lesson 10.02, AI and machine learning, "Your side of the line"](../10-data-ai-and-more/02-ai-and-ml.md#your-side-of-the-line).

**7. C** · Task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1). "Stop guessing capacity" is the advantage for demand you can't forecast: use what you need when you need it, instead of buying for a guess and leaving it idle. Going global is about place, economies of scale lower the price of each unit, and leaving data centers removes the work of running them, but none of them makes capacity follow the news. Reread: [Lesson 02.02, Before and after: the demand curve, "Six advantages, one picture"](../02-why-the-cloud/02-before-and-after-the-demand-curve.md#six-advantages-one-picture).

**8. C** · Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). WorkSpaces gives each person a whole desktop that runs in AWS and streams to their device, and hourly billing with AutoStop suits part-time and seasonal staff. Secure Browser streams only a web browser, not a desktop, and is closing to new customers (2026-10-29). Connect runs a contact center but provides no desktops, and self-managed EC2 instances would make the company build and secure the desktops itself. Reread: [Lesson 10.03, People, apps and devices, "WorkSpaces gives each person a whole desktop that runs in AWS"](../10-data-ai-and-more/03-people-apps-and-devices.md#workspaces-gives-each-person-a-whole-desktop-that-runs-in-aws).

**9. A and E** · Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Shield Advanced is a paid yearly subscription that adds automatic layer 7 mitigation, the Shield Response Team (which also needs a qualifying Support plan) and DDoS cost protection. Common network floods are already covered free by Shield Standard. Blocking harmful single requests such as SQL injection is AWS WAF's job, and encryption in transit is TLS, not Shield. Reread: [Lesson 09.04, The front door, "Shield Advanced adds detection, people and bill protection, for a price"](../09-protecting-and-governing/04-the-front-door.md#shield-advanced-adds-detection-people-and-bill-protection-for-a-price).

**10. D** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). License-included instances bundle the software license into the pay-as-you-go price, which is simple and keeps compliance with the vendor's terms on AWS's side of the bill. BYOL depends on licenses the company owns and on their terms, and puts license compliance on the company. Spot and Capacity Reservations are about how compute is bought or reserved, not licenses. Reread: [Lesson 13.04, The business case, "License-included or bring your own license: who pays the software vendor"](../13-moving-to-aws/04-the-business-case.md#license-included-or-bring-your-own-license-who-pays-the-software-vendor).

**11. C** · Task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2). Rules come first: a Region outside the allowed country is out, whatever its price or speed, and AWS doesn't move data between Regions on its own, so keeping every copy in Canada is the insurer's job. Services, latency to the members (not to the office) and price then rank the Regions that are left. Reread: [Lesson 03.02, Choosing a Region, "Rules first: decide where the data may live"](../03-aws-around-the-world/02-choosing-a-region.md#rules-first-decide-where-the-data-may-live).

**12. A and C** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Access keys are long-term secrets: AWS's guidance is to use temporary credentials where you can, to rotate any key you must keep, and to delete keys that aren't used. Sharing keys or putting them in code spreads the secret, and broader permissions make a leaked key more dangerous. Reread: [Lesson 04.05, Credentials and federation, "Access keys are long-term secrets: avoid them where you can"](../04-shared-responsibility-and-access/05-credentials-and-federation.md#access-keys-are-long-term-secrets-avoid-them-where-you-can).

**13. A and D** · Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Retire removes what has no value, and repurchase replaces an application with a different product, often SaaS. The others are swapped: rewriting for cloud-native features is refactor, moving servers unchanged onto EC2 is rehost, and relocate moves a whole platform, such as VMware, onto its AWS version without changing the applications. Reread: [Lesson 13.02, Seven migration strategies, "Rehost, relocate, replatform, refactor side by side"](../13-moving-to-aws/02-seven-migration-strategies.md#rehost-relocate-replatform-refactor-side-by-side).

**14. B** · Task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1). A Capacity Reservation guarantees capacity for an instance type in one Availability Zone, for as long as you need it, billed at the On-Demand rate; it gives no discount of its own. Spot capacity can be taken back, a Savings Plan is a one- or three-year commitment that discounts but reserves nothing, and Dedicated Instances are about single-tenant hardware, not guaranteed capacity. Reread: [Lesson 11.02, Purchasing options, "Capacity Reservations: a guarantee, not a discount"](../11-paying-for-aws/02-purchasing-options.md#capacity-reservations-a-guarantee-not-a-discount).

**15. A** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). Control Tower builds and watches a best-practice landing zone on top of AWS Organizations, with preventive, detective and proactive controls and an account factory for new accounts. Service Catalog offers approved products for people to launch, Config records and judges resource settings (Control Tower uses it for detective controls), and Artifact provides AWS's audit reports. Reread: [Lesson 09.05, Compliance and governance, "AWS Control Tower sets up and watches a multi-account environment, on top of Organizations"](../09-protecting-and-governing/05-compliance-and-governance.md#aws-control-tower-sets-up-and-watches-a-multi-account-environment-on-top-of-organizations).

**16. B** · Task [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4). DMS copies the data while the source keeps running, then keeps replicating every change until the cutover, so downtime is only the switch itself. SCT converts schemas between different engines and isn't needed for MySQL to MySQL. A nightly backup loses the day's sales, and Snowball has been closed to new customers since 2025-11-07 and moves files, not a live database. Reread: [Lesson 05.06, Choosing a database, "Moving a database in: DMS moves the data, SCT converts the schema"](../05-storing-data/06-choosing-a-database.md#moving-a-database-in-dms-moves-the-data-sct-converts-the-schema).

**17. A and D** · Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4). Inspector scans workloads continuously for weaknesses: known vulnerabilities in installed software and unintended network exposure. Unusual API activity is a threat for GuardDuty to report, sensitive data in S3 is Macie's job, and a root user without MFA is a settings check for Security Hub or Trusted Advisor. Reread: [Lesson 09.03, Finding threats and weaknesses, "Inspector scans workloads and reports weaknesses before an attacker finds them"](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md#inspector-scans-workloads-and-reports-weaknesses-before-an-attacker-finds-them).

**18. A** · Task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2). Running in one Availability Zone gives up reliability, and the Framework expects trade-offs like this one, such as less reliability in a test environment to save cost. What it generally doesn't trade away are security and operational excellence, so B and D trade the wrong pillars, and C is wrong because trade-offs between the other pillars are normal. Reread: [Lesson 02.05, The Well-Architected Framework, "The pillars can be traded against each other, but not all of them"](../02-why-the-cloud/05-the-well-architected-framework.md#the-pillars-can-be-traded-against-each-other-but-not-all-of-them).

**19. D** · Task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5). Geolocation routing answers by where the user is, so it sends each country to its own version. Latency routing picks whichever Region answers fastest, which may not match the language, weighted routing splits traffic by percentages, and failover routing switches to a standby when health checks fail. Reread: [Lesson 07.03, Names and the edge, "Route 53 answers "where is it?", and it can choose the answer"](../07-connecting-it/03-names-and-the-edge.md#route-53-answers-where-is-it-and-it-can-choose-the-answer).

**20. A** · Task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1). RDS runs on DB instances that the customer sizes, so choosing the instance class and storage is the customer's job; DynamoDB is serverless, with no instances to choose. Who may read the data and what data is stored are the customer's on both, and failed hardware is AWS's on both. Reread: [Lesson 04.01, Security of the cloud vs security in the cloud, "The line moves with the service: EC2, RDS, Lambda and S3"](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3).

**21. D** · Task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3). Application Migration Service, now called AWS Transform MGN, rehosts whole servers onto EC2 by block-level replication, with test launches and a short cutover. DMS moves the data inside databases, DataSync moves files, and Migration Evaluator builds the cost case before the move but moves nothing. Reread: [Lesson 13.03, Migration tools, "Application Migration Service, now AWS Transform MGN, rehosts whole servers"](../13-moving-to-aws/03-migration-tools.md#application-migration-service-now-aws-transform-mgn-rehosts-whole-servers).

**22. D** · Task [3.7](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.7). Comprehend takes text in and finds meaning: sentiment, and entities such as places, people and organizations. Translate changes the language without judging it, Textract reads text out of scanned documents and forms, and Transcribe turns speech into text. Reread: [Lesson 10.02, AI and machine learning, "Text in: Comprehend finds meaning, Translate changes the language"](../10-data-ai-and-more/02-ai-and-ml.md#text-in-comprehend-finds-meaning-translate-changes-the-language).

**23. B** · Task [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3). Directory Service is AWS's answer for Active Directory, including a managed Microsoft AD that servers can join. Cognito handles sign-in for an application's customers, Identity Center gives the workforce one sign-in to AWS accounts and applications (it can use a directory as its identity source, but isn't one), and IAM groups hold policies for IAM users. Reread: [Lesson 04.05, Credentials and federation, "Federation: sign in once, elsewhere, and receive temporary access"](../04-shared-responsibility-and-access/05-credentials-and-federation.md#federation-sign-in-once-elsewhere-and-receive-temporary-access).

**24. C** · Task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2). A tag reaches cost reports only after someone activates it as a cost allocation tag, the management account in an organization or the account itself when it stands alone; costs are tagged from activation on, with a backfill possible only where the tag was already on the resource. The `aws:` prefix belongs to AWS-generated tags, which users can't create. Reread: [Lesson 11.04, Many accounts, one bill, "A tag reaches your cost reports only after you activate it"](../11-paying-for-aws/04-many-accounts-one-bill.md#a-tag-reaches-your-cost-reports-only-after-you-activate-it).

**25. C** · Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1). The CLI turns an action into a command you can run in bulk or save as a script, which fits a quick one-time change to many existing resources. Clicking 300 times invites mistakes, CloudFormation manages resources a stack created rather than retagging others in bulk, and an SDK is for calls inside a program you are building. Reread: [Lesson 08.01, Four ways in, "The CLI turns each action into a command you can save and run again"](../08-building-and-operating/01-four-ways-in.md#the-cli-turns-each-action-into-a-command-you-can-save-and-run-again).

**26. B and C** · Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2). An SCP is a ceiling: it limits every user and role in a member account, root included, and grants nothing, so an action needs both an IAM allow and the SCP's permission. SCPs don't apply to the management account. IAM policies still do the granting inside the ceiling, and roles are limited just as users are. Reread: [Lesson 09.05, Compliance and governance, "An SCP is a ceiling: it limits everyone in a member account, and grants nothing"](../09-protecting-and-governing/05-compliance-and-governance.md#an-scp-is-a-ceiling-it-limits-everyone-in-a-member-account-and-grants-nothing).

**27. C** · Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4). Compute Optimizer recommends better-fitting resources from measured use and changes nothing itself: the second round of rightsizing, after the move. Migration Evaluator builds the case before a migration, the Pricing Calculator estimates a design from your own assumptions, and Budgets alerts on spending. Reread: [Lesson 13.04, The business case, "Rightsize twice: before the move from measured data, and after it with Compute Optimizer"](../13-moving-to-aws/04-the-business-case.md#rightsize-twice-before-the-move-from-measured-data-and-after-it-with-compute-optimizer).

**28. B** · Task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8). IoT Core connects devices, typically over MQTT, and its rules route their messages to other AWS services. Kinesis Data Streams holds streaming records for your own programs but doesn't connect or manage devices, Amplify builds web and mobile front ends, and SNS pushes messages to subscribers. Reread: [Lesson 10.03, People, apps and devices, "IoT Core connects devices and routes what they send"](../10-data-ai-and-more/03-people-apps-and-devices.md#iot-core-connects-devices-and-routes-what-they-send).

**29. D** · Task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3). Abuse coming from AWS resources, such as attacks, spam or malware from an AWS address, goes to the AWS Trust & Safety team through the abuse form, whatever the reporter's Support plan. It isn't a support case, re:Post is a public question-and-answer site, and the Health Dashboard reports problems with AWS services. An intruder in your own account is a different matter: an urgent security case. Reread: [Lesson 12.03, Where to find answers, "Abuse from an AWS address goes to AWS Trust & Safety, not to Support"](../12-getting-help/03-where-to-find-answers.md#abuse-from-an-aws-address-goes-to-aws-trust--safety-not-to-support).

**30. D** · Task [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6). Elastic Disaster Recovery uses the same kind of continuous copying as Application Migration Service, but it keeps copying so the server can be recovered in AWS whenever needed; Application Migration Service ends at a planned cutover. AWS Backup brings back data from the last backup rather than a running server in minutes, and DataSync moves files. Reread: [Lesson 13.03, Migration tools, "MGN or Elastic Disaster Recovery: same copying, different ending"](../13-moving-to-aws/03-migration-tools.md#mgn-or-elastic-disaster-recovery-same-copying-different-ending).

</details>

## Score by domain

Count your correct answers in each domain and find your band. The bands say what to study next, not how you'd do on the exam.

| Domain | Share of the exam | Questions in this set | Restudy (below 60%) | Review the linked sections (60–79%) | Ready on this domain (80% or more) |
|---|---|---|---|---|---|
| 1 Cloud Concepts | 24% | 7: 1, 7, 10, 13, 18, 21, 27 | 0 to 4 | 5 | 6 to 7 |
| 2 Security and Compliance | 30% | 9: 3, 6, 9, 12, 15, 17, 20, 23, 26 | 0 to 5 | 6 to 7 | 8 to 9 |
| 3 Cloud Technology and Services | 34% | 10: 2, 5, 8, 11, 16, 19, 22, 25, 28, 30 | 0 to 5 | 6 to 7 | 8 to 10 |
| 4 Billing, Pricing, and Support | 12% | 4: 4, 14, 24, 29 | 0 to 2 | 3 | 4 |

**Read the bands as pointers, not verdicts.** With 4 questions in Domain 4, one miss moves you from 100% to 75%. For a domain in the restudy band, reread the lessons the answer key links to, use the [blueprint map](../99-reference/06-blueprint-map.md) to find every page on that domain's tasks, and retake the mastery checks of the modules involved. In the review band, reread only the linked sections for your misses.

**A practice score is not a prediction of an exam score.** This set shows which ideas you can tell apart today, on questions you have now seen. The real exam reports a scaled score from 100 to 1,000 on questions you haven't seen, with a different mix on each form ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md)). When every domain is at least in the review band, go on to the practice exams, described in [How to use the exam preparation](01-how-to-use-exam-prep.md).

---

"Mixed set 3: Modules 02 to 13" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
