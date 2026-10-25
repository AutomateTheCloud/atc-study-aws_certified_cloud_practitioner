---
type: check
id: clf-05-11
title: "Module 05 mastery check"
tasks: ["3.6", "3.4", "4.1", "2.1"]
objectives: ["05.01a", "05.02a", "05.03a", "05.04a", "05.05a", "05.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 05 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-05-01, clf-05-02, clf-05-04, clf-05-05]
pillars: [reliability, security, cost-optimization, performance-efficiency]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://aws.amazon.com/storagegateway/faqs/"
  - "https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html"
  - "https://aws.amazon.com/rds/faqs/"
  - "https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html"
---

# Module 05 mastery check: place each kind of data, protect it, and keep it affordable

**For:** an adult studying alone, possibly new to IT, who has finished lessons [05.01](01-block-file-object.md) to [05.05](05-managed-or-self-managed-databases.md). **Time:** about 20 minutes per check.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.4) and [3.6](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.6); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 06.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

### Question A1

A nightly job on one EC2 instance needs a fast area for files it can rebuild. The instance's boot disk must keep its data when the instance is stopped each morning. Where should each go?

- A. The rebuildable files on EBS; the boot disk on instance store
- B. Both on instance store, because it is the fastest disk
- C. The rebuildable files on instance store; the boot disk on EBS
- D. Both in Amazon S3, because it has no capacity to plan

<details><summary>Answer</summary>

**C is right.** Instance store suits scratch data, but a stop erases it; an EBS volume keeps its data through a stop.

- **A is wrong.** It reverses the two.
- **B is wrong.** The boot disk would be erased every morning.
- **D is wrong.** S3 isn't a disk a server boots from.

</details>

### Question A2

A transport department collects millions of GPS files a day for several analysis tools, and publishes timetables that its website and mobile app download. Which storage fits best?

- A. Amazon EBS volumes attached to an analysis server
- B. Amazon S3 buckets, reached through a web API
- C. EC2 instance store on the web servers
- D. An Amazon EFS One Zone file system

<details><summary>Answer</summary>

**B is right.** Whole files read by many programs and devices are object storage, reached over HTTPS.

- **A is wrong.** A volume attaches to one server.
- **C is wrong.** Instance store is temporary and belongs to one instance.
- **D is wrong.** EFS is a folder servers mount, not files an app downloads.

</details>

### Question A3

A charity creates an S3 bucket, keeps every default, and turns on versioning. Which TWO events do those settings protect against? (Select TWO.)

- A. A contractor allowed to read downloads every file
- B. A script uploads a corrupt file over a good one
- C. Someone with permission deletes old versions by version ID
- D. A developer adds an ACL that would let anyone read an object
- E. The bucket's Region is unavailable for a day

<details><summary>Answer</summary>

**B and D are right.** Versioning keeps the good file as a noncurrent version, and Block Public Access, on for new buckets, overrides a public ACL.

- **A is wrong.** The contractor was allowed to read.
- **C is wrong.** Deleting a specific version is permanent.
- **E is wrong.** Versions live in the same Region; a copy elsewhere is needed.

</details>

### Question A4

A clinic's only copy of its X-ray images is in S3. Each is opened about once a month and must appear in milliseconds. Which storage class fits?

- A. S3 One Zone-IA
- B. S3 Glacier Flexible Retrieval
- C. S3 Standard-IA
- D. S3 Glacier Deep Archive

<details><summary>Answer</summary>

**C is right.** It suits monthly reads in milliseconds, with copies in several AZs.

- **A is wrong.** One AZ only: for data you can recreate.
- **B is wrong.** It needs a restore first, minutes at best.
- **D is wrong.** Its restore takes hours.

</details>

### Question A5

A law firm keeps closed case files for ten years, then deletes them. They're almost never read, and delivering one within three days is fine. Which approach costs least?

- A. A lifecycle rule: Glacier Deep Archive after 30 days, expire at ten years
- B. A vault in the Amazon Glacier service
- C. S3 Standard-IA, deleting files by hand
- D. A lifecycle rule: One Zone-IA after 30 days, expire at ten years

<details><summary>Answer</summary>

**A is right.** Deep Archive is S3's cheapest class, and a restore within 48 hours fits.

- **B is wrong.** The vault service no longer accepts new customers.
- **C is wrong.** It costs far more to store.
- **D is wrong.** It costs more and keeps the only copy in one AZ.

</details>

### Question A6

A clinic wants to stop handling the physical tapes its backup software writes, without changing the jobs. Its appointment server must also run in AWS within minutes if the building is lost. Which pairing fits?

- A. Tape Gateway; AWS Elastic Disaster Recovery
- B. Tape Gateway; AWS Backup with a nightly plan
- C. Amazon S3 File Gateway; AWS Elastic Disaster Recovery
- D. Volume Gateway; nightly EBS snapshots

<details><summary>Answer</summary>

**A is right.** Tape Gateway looks like a tape library to the software; Elastic Disaster Recovery launches a continuously copied server in minutes.

- **B is wrong.** AWS Backup gives back data, not a running server.
- **C is wrong.** S3 File Gateway presents a shared folder, not tapes.
- **D is wrong.** Volume Gateway presents disks, and snapshots don't launch servers.

</details>

### Question A7

One team needs a database engine Amazon RDS doesn't offer; another runs plain PostgreSQL. Both want as little patching work as possible. Which plan fits?

- A. Both on Amazon RDS, which runs any engine you install
- B. Both on EC2, since running your own is always cheaper
- C. The specialist engine on RDS, and PostgreSQL on EC2
- D. The specialist engine on EC2, and PostgreSQL on Amazon RDS

<details><summary>Answer</summary>

**D is right.** RDS can't run an engine it doesn't offer, so that one is self-managed. PostgreSQL goes on RDS, where AWS patches it.

- **A is wrong.** RDS runs only its own engines.
- **B is wrong.** Running your own adds patching, backups and failover work.
- **C is wrong.** It reverses the two.

</details>

### Question A8

A results site on RDS for MySQL slows when reads jump on results day. The database must also keep running, losing no committed results, if its AZ fails. Which plan meets both needs?

- A. Read replicas for the reads; Multi-AZ for the failure
- B. A Multi-AZ DB instance deployment, sending reads to its standby
- C. Read replicas alone, one taking over if the AZ fails
- D. Hourly snapshots, restored if the AZ fails

<details><summary>Answer</summary>

**A is right.** Replicas answer read-only queries; the synchronous standby takes over automatically.

- **B is wrong.** In a Multi-AZ DB instance deployment, the standby serves no queries.
- **C is wrong.** A replica must be promoted by hand and may miss the latest writes.
- **D is wrong.** A restore is slow and loses recent writes.

</details>

### Question A9

A travel app has itineraries fetched by trip ID, with traffic that jumps tenfold in holidays; a "travelers who went here also went there" feature; and five years of bookings from several systems to analyze. Which databases fit, in that order?

- A. Amazon RDS; Amazon DocumentDB; Amazon ElastiCache
- B. Amazon DynamoDB; Amazon Neptune; Amazon Redshift
- C. Amazon DynamoDB; Amazon Redshift; Amazon Neptune
- D. Amazon ElastiCache; Amazon Neptune; Amazon RDS

<details><summary>Answer</summary>

**B is right.** Items by one key at any scale fit DynamoDB; relationships fit Neptune, a graph database; analysis of years of data from many sources fits Redshift.

- **A is wrong.** None matches its shape.
- **C is wrong.** It swaps the last two.
- **D is wrong.** ElastiCache is a cache, and RDS runs the business.

</details>

### Question A10

A company is moving an Oracle database to RDS for PostgreSQL while it keeps taking orders. AWS SCT converted most of the schema and listed some stored procedures it couldn't. What happens next?

- A. AWS DMS converts them while it copies the data
- B. AWS SCT copies the data once they're fixed
- C. The move stops, because SCT couldn't convert everything
- D. The team converts them by hand; then AWS DMS moves the data

<details><summary>Answer</summary>

**D is right.** SCT converts what it can and lists the rest for you to convert. Then DMS copies the data while the source keeps running.

- **A is wrong.** DMS moves data; it doesn't convert schemas.
- **B is wrong.** SCT doesn't move data.
- **C is wrong.** A list to convert by hand is a normal result.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 05.01a | [Block storage](01-block-file-object.md#block-storage-a-disk-attached-to-one-server) |
| A2, B2 | 05.01a | [Side by side](01-block-file-object.md#block-file-and-object-side-by-side) |
| A3, B3 | 05.02a | [Five layers](02-s3-in-practice.md#the-big-picture-five-layers-three-of-them-already-on) |
| A4, B4 | 05.03a | [Storage classes](02-s3-in-practice.md#storage-classes-how-often-how-fast-how-replaceable) |
| A5, B5 | 05.03a | [Lifecycle rules](02-s3-in-practice.md#lifecycle-rules-move-and-delete-objects-for-you) |
| A6, B6 | 05.04a | [Storage Gateway](04-hybrid-storage-and-backup.md#storage-gateway-lets-on-premises-software-use-aws-storage-without-changing) and [Elastic Disaster Recovery](04-hybrid-storage-and-backup.md#elastic-disaster-recovery-keeps-whole-servers-ready-to-launch) |
| A7, B7 | 05.05a | [Managed by default](05-managed-or-self-managed-databases.md#aws-recommends-a-managed-database-unless-you-have-a-reason-not-to) |
| A8, B8 | 05.05a | [One copy, one job](05-managed-or-self-managed-databases.md#each-copy-of-the-database-has-one-job) |
| A9, B9 | 05.06a | [Side by side](05-managed-or-self-managed-databases.md#the-database-services-side-by-side) |
| A10, B10 | 05.06a | [DMS and SCT](05-managed-or-self-managed-databases.md#moving-a-database-in-dms-moves-the-data-sct-converts-the-schema) |

## Check B: parallel retest

Question B1 tests the same objective as A1, and so on. The pass mark is the same: 8 of 10.

### Question B1

A team will delete an EC2 instance next month and attach its data disk to a new instance in the same AZ, keeping the data. Which choice fits?

- A. An EBS volume whose Delete on termination setting is No
- B. An instance store volume on the current instance
- C. An EBS volume whose Delete on termination setting is Yes
- D. An S3 bucket attached to the instance as its disk

<details><summary>Answer</summary>

**A is right.** With Delete on termination set to No, the volume survives the instance and can be attached again.

- **B is wrong.** Instance store is erased when the instance stops or terminates.
- **C is wrong.** The volume would be deleted with the instance.
- **D is wrong.** S3 isn't attached as a disk.

</details>

### Question B2

A school district is moving its storage to AWS. Which pairing of a need and a service fits?

- A. A web server's boot disk: Amazon S3
- B. Linux servers in three AZs sharing lesson files: one EBS volume
- C. Videos streamed to tablets over HTTPS: EC2 instance store
- D. A Windows staff drive using Active Directory: FSx for Windows File Server

<details><summary>Answer</summary>

**D is right.** FSx for Windows File Server provides SMB shares joined to Active Directory.

- **A is wrong.** A server boots from block storage, such as EBS.
- **B is wrong.** A volume attaches to one server; shared Linux files fit EFS.
- **C is wrong.** Instance store is temporary; files streamed to many devices fit S3.

</details>

### Question B3

A bookshop creates a new S3 bucket and changes none of its settings. Which TWO risks do the defaults already reduce? (Select TWO.)

- A. A bucket policy that would let anyone read the files
- B. A teammate overwrites a good price list with an old one
- C. A clerk deletes last year's invoices by mistake
- D. A manager allowed to read forwards the files to a competitor
- E. A disk holding the data is read outside the data center

<details><summary>Answer</summary>

**A and E are right.** Block Public Access overrides a public policy, and SSE-S3 encryption protects the stored bytes.

- **B and C are wrong.** Versioning would help, but it starts off.
- **D is wrong.** The manager was allowed to read.

</details>

### Question B4

A store's product photos are read thousands of times a day. To cut costs, a developer wants to move them from S3 Standard to Standard-IA. What should the team do?

- A. Keep them in Standard: Standard-IA charges for each GB read
- B. Move them to Standard-IA, which is cheaper for any data
- C. Move them to One Zone-IA, which is cheaper still
- D. Move them to Glacier Instant Retrieval, just as fast

<details><summary>Answer</summary>

**A is right.** Standard has no retrieval fee; moving busy data to a class that charges per GB read can cost more.

- **B is wrong.** Standard-IA is cheaper to store, not to read.
- **C is wrong.** Same reading fee, and only one AZ.
- **D is wrong.** It also charges per GB read.

</details>

### Question B5

A hospital's scans are viewed often for 90 days, then rarely, but must always open in milliseconds. They're kept eight years, then deleted. Which lifecycle rule fits?

- A. Standard, then Glacier Instant Retrieval at day 90; expire at eight years
- B. Standard, then Glacier Deep Archive at day 90; expire at eight years
- C. Standard throughout, deleted by hand at eight years
- D. Standard, then Glacier Flexible Retrieval at day 90; expire at eight years

<details><summary>Answer</summary>

**A is right.** Glacier Instant Retrieval is the archive class that still answers in milliseconds.

- **B is wrong.** Deep Archive restores take hours.
- **C is wrong.** It pays Standard's price for years of rarely read data.
- **D is wrong.** Flexible Retrieval needs a restore first.

</details>

### Question B6

A school district wants to stop handling the physical tapes its backup software writes, without changing the jobs. Its EBS volumes and RDS databases in two accounts also need one backup schedule, copied to a second Region. Which pairing fits?

- A. Amazon S3 File Gateway; AWS Elastic Disaster Recovery
- B. Tape Gateway; AWS Elastic Disaster Recovery
- C. Volume Gateway; snapshots taken by each team
- D. Tape Gateway; AWS Backup

<details><summary>Answer</summary>

**D is right.** Tape Gateway looks like a tape library to the software; AWS Backup runs one plan across services and accounts, with cross-Region copies.

- **A is wrong.** A folder, and no backup schedule.
- **B is wrong.** The second half doesn't fit.
- **C is wrong.** Volume Gateway presents disks, not tapes.

</details>

### Question B7

Stock-control software works only with a database engine RDS doesn't offer, so the IT manager runs it on an EC2 instance. Which statement is accurate?

- A. AWS patches the engine, because the instance runs on AWS
- B. Turning on Multi-AZ for the instance gives it automatic failover
- C. The team patches, backs up and builds failover for it
- D. Nothing changes compared with RDS but the price

<details><summary>Answer</summary>

**C is right.** A self-managed database leaves the operating system, the database software, backups and failover with the customer.

- **A is wrong.** On EC2, the engine is the customer's to patch.
- **B is wrong.** Multi-AZ deployments are an RDS feature.
- **D is wrong.** Everything RDS does becomes the team's work.

</details>

### Question B8

An RDS for PostgreSQL database has one read replica in a second AZ, and no Multi-AZ deployment. The primary's AZ fails. What happens?

- A. RDS fails over to the replica by itself in a minute or two
- B. Someone must promote the replica, and recent writes may be lost
- C. The replica starts accepting writes in the primary's place
- D. Nothing is lost: the replica is copied synchronously

<details><summary>Answer</summary>

**B is right.** Outside Aurora, a replica doesn't take over by itself, and it's copied asynchronously.

- **A is wrong.** Automatic failover is what a Multi-AZ standby does.
- **C is wrong.** A replica accepts no writes until promoted.
- **D is wrong.** Replicas are asynchronous; the standby is the synchronous copy.

</details>

### Question B9

A delivery company has menus stored as JSON by an app written with MongoDB drivers; rider locations read thousands of times a second, answered in microseconds; and orders that link customers, restaurants and dishes and must be saved whole. Which databases fit, in that order?

- A. Amazon DynamoDB; Amazon Neptune; Amazon Redshift
- B. Amazon DocumentDB; Amazon Redshift; Amazon Aurora
- C. Amazon Neptune; Amazon ElastiCache; Amazon DynamoDB
- D. Amazon DocumentDB; Amazon ElastiCache; Amazon Aurora

<details><summary>Answer</summary>

**D is right.** MongoDB documents: DocumentDB. Microsecond reads: ElastiCache. Linked tables saved whole: a relational database such as Aurora.

- **A is wrong.** No MongoDB compatibility, and Redshift is for analysis.
- **B is wrong.** Redshift doesn't answer in microseconds.
- **C is wrong.** Menus aren't a graph, and linked orders are relational.

</details>

### Question B10

A company is moving a SQL Server database to RDS for PostgreSQL while the business keeps using it. Which order of steps is right?

- A. AWS DMS copies the data; then AWS SCT converts the schema
- B. AWS SCT copies the schema and the data together
- C. AWS SCT converts the schema; then AWS DMS copies the data and each change
- D. AWS Backup restores a backup of it into RDS for PostgreSQL

<details><summary>Answer</summary>

**C is right.** The engine changes, so convert the schema first; then DMS copies the data and each change until the switch-over.

- **A is wrong.** The target needs a converted schema first.
- **B is wrong.** SCT converts the schema only.
- **D is wrong.** A backup of one engine can't be restored into another.

</details>

---

"Module 05 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
