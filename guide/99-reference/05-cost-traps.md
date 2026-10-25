---
type: reference
id: clf-99-05
title: "Cost traps"
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; a page to check before and after every lab"
tasks: []
objectives: []
pillars: [cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/vpc/pricing/"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/ebs/pricing/"
  - "https://aws.amazon.com/rds/pricing/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html"
  - "https://aws.amazon.com/ec2/faqs/"
  - "https://aws.amazon.com/s3/pricing/"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json"
  - "https://aws.amazon.com/cloudwatch/pricing/"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html"
  - "https://aws.amazon.com/cloudtrail/pricing/"
  - "https://aws.amazon.com/config/pricing/"
  - "https://aws.amazon.com/free/security/"
  - "https://aws.amazon.com/kms/pricing/"
  - "https://aws.amazon.com/cloudhsm/pricing/"
  - "https://aws.amazon.com/shield/pricing/"
  - "https://aws.amazon.com/firewall-manager/pricing/"
  - "https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-pricing.html"
  - "https://aws.amazon.com/athena/pricing/"
  - "https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/"
  - "https://aws.amazon.com/premiumsupport/pricing/"
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
  - "https://aws.amazon.com/free/terms/"
  - "https://aws.amazon.com/application-migration-service/faqs/"
  - "https://aws.amazon.com/ec2/dedicated-hosts/pricing/"
---

# Cost traps: what keeps billing when nobody is using it

Most surprise AWS bills come from a short list of habits: something left running, something stopped that still bills, data kept or moved without thinking, and commitments signed to try a feature. This page collects the traps the guide's lessons and labs teach, each with why it costs, how to avoid it, and the page that teaches it.

**How to use it:** read it once before your first lab, then use it as a checklist when you clean up. If a charge on your bill puzzles you, start here.

> **Dated (checked 2026-10-24):** prices are AWS's list prices in US East (N. Virginia) on the dates the lessons checked them, and they change. Use them for the size of the trap, not for budgeting; check the pricing page linked from each lesson before you rely on a figure. On the Free plan, charges come out of your credits, so these traps spend credits first.

## The traps at a glance

| Trap | Roughly, if forgotten for a month | Section |
|---|---|---|
| NAT gateway left in place | About $33, plus $0.045 per GB | [NAT gateways bill every hour they exist](#nat-gateways-bill-every-hour-they-exist) |
| Idle Elastic IP or other public IPv4 address | About $3.65 each | [Every public IPv4 address bills, used or idle](#every-public-ipv4-address-bills-used-or-idle) |
| Stopped EC2 instance | Its disks, about $0.64 for 8 GiB | [A stopped instance still pays for its disks](#a-stopped-instance-still-pays-for-its-disks) |
| Stopped Lightsail instance | The full plan price | [Lightsail bills while stopped](#lightsail-bills-while-stopped) |
| Stopped RDS database | Storage and backups, then the instance again after seven days | [A stopped database starts itself again](#a-stopped-database-starts-itself-again) |
| Object deleted early from an infrequent-access or archive class | The rest of its minimum stay | [S3's colder classes have minimum stays, sizes and retrieval fees](#s3s-colder-classes-have-minimum-stays-sizes-and-retrieval-fees) |
| Data sent to the internet | $0.09 per GB after the first 100 GB | [Data going out costs; data coming in doesn't](#data-going-out-costs-data-coming-in-doesnt) |
| Logs with no retention set | Grows every month | [Logs are kept forever unless you say otherwise](#logs-are-kept-forever-unless-you-say-otherwise) |
| Shield Advanced, to try it | $3,000 a month for a year | [Shield Advanced commits you to a year](#shield-advanced-commits-you-to-a-year) |
| Support plan upgrade, to look | At least $29 for the first month | [Paid Support plans have a minimum](#paid-support-plans-have-a-minimum) |

## Things that bill by the hour while they exist

These are on AWS's "time" meter: they bill every hour they exist, busy or idle ([How AWS charges](../11-paying-for-aws/01-how-aws-charges.md)). The cure is always the same: delete what you don't use, and check the next day that it's gone.

### NAT gateways bill every hour they exist

**Why it costs:** a NAT gateway charges $0.045 an hour (about $32.85 for a 730-hour month) plus $0.045 per GB it processes, and it needs a public IPv4 address that bills too. One per Availability Zone, as resilience suggests, doubles it. A month with one gateway and 10 GB came to about $36.95 in the lesson's example (as of 2026-10-24).

**How to avoid it:** don't create one to learn; the guide's VPC lab doesn't. For traffic to S3 or DynamoDB, a gateway endpoint does the job at no charge. Delete NAT gateways, and release their addresses, when a test ends.

**Taught in:** [Your own network](../07-connecting-it/01-your-own-network.md); [Lab 09: Build a small network with a public and a private subnet, then take it apart](../07-connecting-it/05-lab-09-build-a-small-vpc.md)

### Every public IPv4 address bills, used or idle

**Why it costs:** each public IPv4 address, including an Elastic IP address, costs $0.005 an hour, about $3.65 a month, whether it's attached to a running server or sitting unused (as of 2026-10-24). An Elastic IP you keep after terminating its instance goes on billing.

**How to avoid it:** release Elastic IPs you no longer need. Don't give servers public addresses they don't need; put them in private subnets.

**Taught in:** [Your own network](../07-connecting-it/01-your-own-network.md); [Amazon EC2: instances, images and instance types](../06-running-applications/01-ec2.md)

### A stopped instance still pays for its disks

**Why it costs:** stopping an EC2 instance ends its instance-hour charge, but its EBS volumes, and any Elastic IP you keep, still bill. In Lab 08's example, a forgotten `t3.micro` costs about $11.88 a month running, $0.64 stopped (the 8 GiB volume) and $0 only when terminated (as of 2026-10-24).

**How to avoid it:** terminate what you don't need, and check that its volumes went with it. Stop only what you'll start again soon.

**Taught in:** [Amazon EC2: instances, images and instance types](../06-running-applications/01-ec2.md); [Lab 08: Launch a virtual server, stop it, terminate it, and prove nothing is left](../06-running-applications/06-lab-08-launch-and-terminate-an-instance.md)

### Lightsail bills while stopped

**Why it costs:** a Lightsail instance is charged by the hour up to its plan's monthly price whether it's running or stopped. This differs from EC2: only deleting the Lightsail instance ends the charge.

**How to avoid it:** delete Lightsail instances you've finished with, rather than stopping them.

**Taught in:** [Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts](../06-running-applications/04-simpler-paths.md)

### A stopped database starts itself again

**Why it costs:** a stopped RDS database still pays for its storage and backups, and RDS starts it again on its own after seven days, when instance hours resume.

**How to avoid it:** delete databases you don't need rather than stopping them. The guide teaches Multi-AZ and read replicas in a simulation for this reason.

**Taught in:** [Managed or self-managed databases](../05-storing-data/05-managed-or-self-managed-databases.md)

### Some network links bill hourly too

**Why it costs:** several connections have an hourly charge before any data moves: a Site-to-Site VPN connection $0.05 an hour (about $36.50 a month), a Transit Gateway attachment $0.05 an hour, an interface endpoint $0.01 an hour in each Availability Zone, and a Client VPN subnet association $0.10 an hour (as of 2026-10-24). A Global Accelerator accelerator bills a fixed hourly fee even when disabled.

**How to avoid it:** price links before you create them, and delete accelerators, endpoints and VPN connections you don't use.

**Taught in:** [Connecting networks and offices](../07-connecting-it/04-connecting-networks-and-offices.md); [Names and the edge](../07-connecting-it/03-names-and-the-edge.md)

### High availability means paying for the spare

**Why it costs:** a second web server runs and bills all the time; a standby database is a whole database server that serves no orders; a load balancer bills by the hour; data between EC2 and RDS in different Availability Zones costs $0.01 per GB each way (as of 2026-10-23).

**How to avoid it:** it's often worth paying, but decide from what an outage costs the business, and price the design first.

**Taught in:** [Regions, Availability Zones and data centers](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md)

## Storage that keeps billing

### Snapshots outlive the volume

**Why it costs:** EBS snapshots are billed on their own, and deleting a volume doesn't delete its snapshots.

**How to avoid it:** after a cleanup, look for snapshots left behind, and set a backup plan's retention so old ones expire.

**Taught in:** [Hybrid storage and backup](../05-storing-data/04-hybrid-storage-and-backup.md)

### S3's colder classes have minimum stays, sizes and retrieval fees

**Why it costs:** the infrequent-access and archive classes are cheap to keep data in, but a file deleted, overwritten or moved early is billed for the rest of its minimum stay; small files are billed as larger ones; and reading data back adds a per-GB retrieval fee. As checked on 2026-10-23:

| Class | Minimum stay | Minimum billed size | Retrieval fee |
|---|---|---|---|
| S3 Standard-IA and S3 One Zone-IA | 30 days | 128 KB | Per GB |
| S3 Glacier Instant Retrieval | 90 days | 128 KB | Per GB |
| S3 Glacier Flexible Retrieval | 90 days | About 40 KB of metadata added to each object | Per GB; bulk free |
| S3 Glacier Deep Archive | 180 days | About 40 KB of metadata added to each object | Per GB |

**How to avoid it:** choose a class by how long data stays and how often it's read, not by the storage price alone. Don't move lots of tiny files to archive classes. S3 Intelligent-Tiering avoids retrieval fees for unpredictable access, for a monitoring fee.

**Taught in:** [Storage classes and lifecycle](../05-storing-data/03-storage-classes-and-lifecycle.md); [Simulation S5: Run a year of lifecycle rules forward and find the cost traps](../05-storing-data/09-sim-lifecycle-cost-timeline.md)

### Old versions are billed in full

**Why it costs:** with versioning on, every overwritten or deleted object stays as a noncurrent version, and each is billed as a whole object. A bucket whose files change weekly grows every week.

**How to avoid it:** pair versioning with a lifecycle rule that deletes noncurrent versions after a safety window, such as 30 days.

**Taught in:** [Storage classes and lifecycle](../05-storing-data/03-storage-classes-and-lifecycle.md); [Lab 05: Keep every version, add a lifecycle rule, and set up an archive bucket](../05-storing-data/07-lab-05-versions-and-lifecycle.md)

### Logs are kept forever unless you say otherwise

**Why it costs:** a new CloudWatch Logs log group is set to keep its data forever, so stored logs, and their storage charge, grow every month. Log data ingested beyond the free 5 GB a month costs $0.50 per GB (as of 2026-10-24).

**How to avoid it:** set a retention period on every log group, as Lab 07 does with one week.

**Taught in:** [Lab 07: Run a Lambda function, read its logs, and stop them piling up](../06-running-applications/05-lab-07-a-lambda-function.md); [Watching workloads](../08-building-and-operating/03-watching-workloads.md)

## Moving data

### Data going out costs; data coming in doesn't

**Why it costs:** data in from the internet is free, but data out is not. The first 100 GB a month sent to the internet is free across all Regions, then it costs $0.09 per GB for the first 10 TB; sending to another Region costs $0.02 per GB to most Regions; between Availability Zones, $0.01 each way; and a NAT gateway adds $0.045 per GB on top (US East (N. Virginia), as of 2026-10-23 and 2026-10-24).

**How to avoid it:** keep data close to where it's used, serve popular content through CloudFront (which pulls from S3 at no transfer charge), and estimate transfer before you design across Regions.

**Taught in:** [Connecting networks and offices](../07-connecting-it/04-connecting-networks-and-offices.md); [Choosing a Region](../03-aws-around-the-world/02-choosing-a-region.md); [How AWS charges](../11-paying-for-aws/01-how-aws-charges.md)

### Queries are billed by the data they scan

**Why it costs:** Athena charges by the data each query reads; the pricing page's examples use $5 per TB scanned (as of 2026-10-24). A query over a large, uncompressed folder reads all of it.

**How to avoid it:** compress, partition or convert data to a columnar format such as Parquet, and query only the columns and folders you need.

**Taught in:** [Analytics in five verbs](../10-data-ai-and-more/01-analytics-in-five-verbs.md); [Lab 13: Query a small sales file in S3 with Athena, then delete everything](../10-data-ai-and-more/04-lab-13-athena-query.md)

## Watching and protecting

### CloudWatch is free only up to a point

**Why it costs:** the free tier covers basic metrics, 10 custom or detailed-monitoring metrics, 10 alarm metrics, 5 GB of log data and 3 dashboards a month. Beyond that: $0.10 per alarm metric a month, $0.30 per custom metric a month and $0.50 per GB of logs ingested (as of 2026-10-24).

**How to avoid it:** turn on detailed monitoring and custom metrics only where you'll use them, and delete alarms and dashboards from finished tests.

**Taught in:** [Watching workloads](../08-building-and-operating/03-watching-workloads.md); [Lab 11: Email the owner when the order function fails](../08-building-and-operating/06-lab-11-alarm-on-errors.md)

### Extra trails and recorders bill per event

**Why it costs:** CloudTrail's event history and one trail's copy of management events are free, apart from the S3 storage; extra copies cost $2.00 per 100,000 events and data events $0.10 per 100,000. AWS Config bills $0.003 per configuration item recorded and $0.001 per rule evaluation, and Security Hub CSPM needs Config (as of 2026-10-24).

**How to avoid it:** keep one trail; turn on data events and Config only with a reason and a budget.

**Taught in:** [Who did what, how it runs, how it was set](../09-protecting-and-governing/01-who-did-what.md)

### Security services bill after their free trial

**Why it costs:** GuardDuty, Inspector, Security Hub CSPM, Detective and Macie start with a free trial (30, 15, 30, 30 and 30 days) and then bill by what they process. On a new Free plan account, some of them asked to upgrade the plan (2026-10-23).

**How to avoid it:** the guide shows their findings in a simulation instead. If you turn one on, note the trial's end date and turn it off before then if you don't want to pay.

**Taught in:** [Finding threats and weaknesses](../09-protecting-and-governing/03-finding-threats-and-weaknesses.md); [Encryption](../09-protecting-and-governing/02-encryption.md)

### Keys and HSMs bill monthly or hourly

**Why it costs:** each customer managed KMS key costs $1 a month, prorated hourly, with $1 more for each of its first two rotations; requests beyond 20,000 a month cost $0.03 per 10,000 (as of 2026-10-24). A CloudHSM HSM bills every hour until you delete it.

**How to avoid it:** use SSE-S3 or an AWS managed key unless you need control of the key yourself, and don't create customer managed keys just to look.

**Taught in:** [Encryption](../09-protecting-and-governing/02-encryption.md)

### Shield Advanced commits you to a year

**Why it costs:** Shield Advanced is $3,000 a month with a one-year commitment, plus data transfer fees. Firewall Manager costs $100 per policy per Region a month, plus the services it uses (as of 2026-10-24). Shield Standard is free and already on.

**How to avoid it:** never subscribe to Shield Advanced to see what it does; learn it from the lesson.

**Taught in:** [The front door](../09-protecting-and-governing/04-the-front-door.md)

## Commitments and minimums

### Paid Support plans have a minimum

**Why it costs:** Business Support+ costs $29 a month or a share of the account's AWS charges, whichever is greater, and it's charged per account; once you sign up, you pay for at least a month. Enterprise Support starts at $5,000 a month and Unified Operations at $50,000 (as of 2026-10-24). Changing the plan doesn't need the root user, so an admin user can do it by accident.

**How to avoid it:** never choose an upgrade button in a lab; the Basic plan covers everything the guide does.

**Taught in:** [Support plans](../12-getting-help/01-support-plans.md); [Lab 17: Tour the help every AWS account gets, on the Basic plan](../12-getting-help/05-lab-17-support-center-tour.md)

### Commitments bill whether you use them or not

**Why it costs:** a Reserved Instance is charged every hour of its term, and Savings Plans commitment unused in an hour is lost. In an organization, sharing decides who gets the discount, not whether you pay. A Dedicated Host bills per host-hour however many instances run on it.

**How to avoid it:** commit only to the baseline you run every hour, after watching real usage, and buy Spot or On-Demand for the rest.

**Taught in:** [Purchasing options](../11-paying-for-aws/02-purchasing-options.md); [Many accounts, one bill](../11-paying-for-aws/04-many-accounts-one-bill.md); [The business case](../13-moving-to-aws/04-the-business-case.md)

### Migration tools bill while they run

**Why it costs:** AWS Transform MGN (the exam's AWS Application Migration Service) gives each source server 2,160 free hours of replication, about 90 days, then charges hourly per server, and you pay for the replication servers, EC2 and EBS it uses throughout. AWS DMS bills for its replication capacity while it runs (as of 2026-10-24).

**How to avoid it:** stop replication and delete the replication resources once a server has cut over.

**Taught in:** [Migration tools](../13-moving-to-aws/03-migration-tools.md)

### Marketplace subscriptions add the seller's charges

**Why it costs:** subscribing to a product in AWS Marketplace adds the seller's charges to your AWS bill.

**How to avoid it:** browse, but don't choose Subscribe or Request Offer from a lab account.

**Taught in:** [Lab 17: Tour the help every AWS account gets, on the Basic plan](../12-getting-help/05-lab-17-support-center-tour.md); [Partners and paid help](../12-getting-help/04-partners-and-paid-help.md)

## Watching doesn't stop spending

### A budget alerts; it doesn't cap

**Why it costs:** an AWS budget sends alerts, and its data updates up to three times a day, so an alert arrives hours after the money is spent. Nothing stops unless you set a budget action, and only what that action covers. The first two action-enabled budgets are free, then each costs $0.10 a day (as of 2026-10-24).

**How to avoid it:** set budgets and alerts anyway (the guardrails primer does), and add cleanup habits: they're what actually stop a runaway cost.

**Taught in:** [Estimate, watch, analyze](../11-paying-for-aws/03-estimate-watch-analyze.md); [Simulation S14: Follow a runaway cost and see which guardrails alert and which stop it](../11-paying-for-aws/08-sim-guardrail-timeline.md)

### Some actions move a Free plan account to the Paid plan

**Why it costs:** on the Free plan, creating or joining an organization, setting up a Control Tower landing zone, accepting an AWS Artifact agreement that designates the account for regulated data, creating a Professional Services contract or joining the AWS Partner Network upgrades the account to the Paid plan, and AWS says a Paid plan can't go back (as of 2026-10-24). An account in an organization can't use or earn Free Tier credits.

**How to avoid it:** practice those in the guide's simulations, and choose an upgrade only when you've decided to pay.

**Taught in:** [Compliance and governance](../09-protecting-and-governing/05-compliance-and-governance.md); [Many accounts, one bill](../11-paying-for-aws/04-many-accounts-one-bill.md); [Partners and paid help](../12-getting-help/04-partners-and-paid-help.md)

## After every lab

- Delete what the lab created, in the order its cleanup gives, and check the console shows nothing left.
- The next day, check the Bills page and Cost Explorer for charges by service; billing data arrives hours late.
- Look for leftovers this page names: NAT gateways, Elastic IPs, volumes and snapshots, log groups without retention, stopped Lightsail instances and databases.

The guardrails primer's [habits for every lab](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md) give the full routine.

---

"Cost traps" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
