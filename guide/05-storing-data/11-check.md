---
type: check
id: clf-05-11
title: "Module 05 mastery check"
tasks: ["3.6", "3.4", "4.1", "2.1"]
objectives: ["05.01a", "05.02a", "05.03a", "05.04a", "05.05a", "05.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 05 lessons; about 30 minutes for each check; works on a phone"
prerequisites: [clf-05-01, clf-05-02, clf-05-03, clf-05-04, clf-05-05, clf-05-06]
pillars: [reliability, security, cost-optimization, performance-efficiency]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html"
  - "https://aws.amazon.com/ebs/faqs/"
  - "https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html"
  - "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"
  - "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html"
  - "https://aws.amazon.com/storagegateway/faqs/"
  - "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"
  - "https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html"
  - "https://aws.amazon.com/rds/faqs/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"
  - "https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html"
  - "https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html"
---

# Module 05 mastery check: place each kind of data, protect it, and keep it affordable

This check shows whether you can do what Module 05 set out to teach: choose block, file or object storage, explain what each S3 protection does, pick a storage class and a lifecycle rule without falling into the cost traps, match a hybrid or backup need to a service, choose how a database is hosted and protected, and pick a database for a shape of data.

**For:** an adult studying alone, possibly new to IT, who has finished lessons [05.01](01-block-file-object.md) to [05.06](06-choosing-a-database.md). **Time:** about 30 minutes for each check. No AWS account needed.

## How to use this check

Take **Check A** closed-book: no lessons, notes or searching. Answer all 15 questions, then open the answers. A "(Select TWO.)" question counts as right only if you chose both correct options. Where a question needs a number that changes, such as a minimum storage duration, the question gives it to you.

- **12 or more right (80%):** you have mastered the module. Go on to the [enrichment tasks](#enrichment-for-learners-who-pass), then to Module 06.
- **Fewer than 12:** for each question you missed, use the [correction map](#correction-map) to reread the named section and redo the linked practice. Then take **Check B**, a parallel retest: new questions on the same objectives. Don't retake Check A; you have seen its answers.

## Check A

### Question A1

A weather-modeling team runs a nightly job on one Amazon EC2 instance. The job needs a fast area for intermediate files, which it can rebuild if they vanish. The instance also boots from a disk that holds the team's software, and that disk must keep its data when the instance is stopped each morning. Where should each go?

- A. The intermediate files on an EBS volume, and the boot disk on instance store
- B. Both on instance store, because it is the fastest disk
- C. The intermediate files on instance store, and the boot disk on an EBS volume
- D. Both in Amazon S3, because it has no capacity to plan

<details><summary>Answer</summary>

**C is right.** Instance store is temporary block storage on the physical computer, which suits scratch data you can rebuild. A stop erases it, so the boot disk goes on an EBS volume, which exists apart from the instance and keeps its data through a stop.

- **A is wrong.** It reverses the two: the software on instance store would be erased at the first stop.
- **B is wrong.** Speed doesn't help if the boot disk is erased every morning.
- **D is wrong.** S3 isn't a disk: programs put and get whole objects through a web API, and a server can't boot from it or use it as a working drive.

</details>

### Question A2

A city's transport department collects millions of small GPS files from its buses every day, keeps them for analysis by several different tools, and publishes the bus timetables as files that its website and mobile app download. Which storage fits this data best?

- A. Amazon EBS volumes attached to an analysis server
- B. Amazon S3 buckets, reached through a web API
- C. EC2 instance store on the web servers
- D. An Amazon EFS One Zone file system

<details><summary>Answer</summary>

**B is right.** Whole files, written once and read by many programs and devices, are object storage. S3 has no capacity to plan, any allowed program reaches it over HTTPS, and AWS lists data lakes and website files among its uses.

- **A is wrong.** A volume attaches to one server in one AZ, so the other tools, the website and the app couldn't all reach the files, and you would have to size the volumes as the data grows.
- **C is wrong.** Instance store is temporary and belongs to one instance; a stop erases it.
- **D is wrong.** EFS is a shared folder that servers mount over NFS, not files a phone app downloads, and One Zone keeps the data in a single AZ.

</details>

### Question A3

A startup's mobile app lets users upload photos. Today the only copy sits on an EBS volume attached to one EC2 instance. The startup wants the photos to survive the loss of a whole Availability Zone, and to be fetched over HTTPS by many servers and by phones. Which change fits best?

- A. Attach a second EBS volume in the same AZ as a mirror
- B. Move the photos to the instance's instance store
- C. Move the photos to an Amazon EFS One Zone file system
- D. Store the photos as objects in Amazon S3

<details><summary>Answer</summary>

**D is right.** S3 Standard keeps copies across several Availability Zones, and any allowed program, on a server or a phone, reaches the objects through a web API over HTTPS.

- **A is wrong.** Both volumes would be in the same AZ, so losing the AZ would take both.
- **B is wrong.** Instance store is temporary and lives on one physical host.
- **C is wrong.** One Zone keeps data in a single AZ, and EFS is mounted as a folder over NFS, not fetched by phones over HTTPS.

</details>

### Question A4

A charity creates a new S3 bucket, keeps every default setting, and turns on versioning. Which TWO of these events do those settings protect it against? (Select TWO.)

- A. A contractor whose IAM policy allows reading downloads every file
- B. A script uploads a corrupt file under the same name as a good one
- C. Someone with permission deletes specific old versions by their version IDs
- D. A developer adds an ACL that would let anyone read one object
- E. The Region that holds the bucket is unavailable for a day

<details><summary>Answer</summary>

**B and D are right.** With versioning on, the good file stays as a noncurrent version that you can restore. Block Public Access, on by default for a new bucket, overrides ACLs and policies that would grant public access.

- **A is wrong.** The contractor was allowed to read. None of these settings stops a permitted reader; least privilege does.
- **C is wrong.** Deleting a specific version is permanent. Only MFA Delete or S3 Object Lock would stop it.
- **E is wrong.** Versions live in the same bucket and Region. Surviving a Regional outage needs a copy elsewhere, such as replication or a backup.

</details>

### Question A5

Which pairing of an S3 protection and the question it answers is correct?

- A. Default encryption: can the stored bytes be read without the key?
- B. Block Public Access: which IAM users in the account may read the data?
- C. Versioning: will the data survive the loss of the whole Region?
- D. Default encryption: may a user with read permission see the files?

<details><summary>Answer</summary>

**A is right.** Encryption at rest protects the stored bytes, for example on a disk that leaves a data center.

- **B is wrong.** Block Public Access stops grants to everyone. Which identities inside the account may read is decided by IAM and bucket policies.
- **C is wrong.** Versions live in the same bucket, account and Region. A copy somewhere else protects against losing those.
- **D is wrong.** S3 decrypts objects automatically for any request its policies allow, so encryption doesn't decide who may read.

</details>

### Question A6

A physiotherapy clinic keeps X-ray images in Amazon S3 and has no other copy of them. Each image is opened about once a month, and when a therapist opens one it must appear in milliseconds. Which storage class is designed for this pattern?

- A. S3 One Zone-IA
- B. S3 Glacier Flexible Retrieval
- C. S3 Standard-IA
- D. S3 Glacier Deep Archive

<details><summary>Answer</summary>

**C is right.** Standard-IA is for data read about once a month that must still come back in milliseconds, and it keeps copies in several Availability Zones, which matters because the images exist nowhere else.

- **A is wrong.** One Zone-IA fits the reading pattern, but it stores data in one AZ, where it can be lost with the AZ. Use it only for data you can recreate.
- **B is wrong.** Flexible Retrieval needs a restore before an object can be read, which takes minutes at best.
- **D is wrong.** Deep Archive needs a restore that takes hours.

</details>

### Question A7

A lifecycle rule moves a team's project files to S3 Glacier Flexible Retrieval at day 60 and expires them at day 120. Glacier Flexible Retrieval bills a minimum storage duration of 90 days (as of 2026-10-23). The files must still be deleted at day 120, and after day 30 a wait of hours to read one is fine. Which change removes the extra charge?

- A. Transition the files at day 30 instead of day 60
- B. Transition the files at day 90 instead of day 60
- C. Keep the rule, because minimums don't apply to lifecycle deletes
- D. Turn on versioning, so that the expired files are kept as old versions

<details><summary>Answer</summary>

**A is right.** From day 30 to day 120 is 90 days in the class, which meets the minimum, so no extra days are billed. Each file is still deleted at day 120.

- **B is wrong.** That leaves only 30 days in the class, so each file is billed for 60 days it never used, more than now.
- **C is wrong.** The minimum applies however an object leaves the class, including by a lifecycle rule.
- **D is wrong.** In a versioned bucket, expiring a file only adds a delete marker, and every old version is billed in full, so it adds cost instead.

</details>

### Question A8

A team reviews five proposed lifecycle rules. As of 2026-10-23, S3 Standard-IA has a 30-day minimum storage duration and bills objects under 128 KB as 128 KB; S3 Glacier Flexible Retrieval has a 90-day minimum; S3 Glacier Deep Archive has a 180-day minimum. Which TWO rules avoid the minimum-duration, minimum-size and reading-cost traps? (Select TWO.)

- A. 2 GB video masters, rarely read: to Deep Archive at day 30, expire at day 400
- B. 20 KB icons that the website reads all day long: to Standard-IA at day 30, expire at day 400
- C. 1 GB nightly backups, rarely read: to Flexible Retrieval at day 1, expire at day 30
- D. 500 MB reports, read twice a year: to Flexible Retrieval at day 30, expire at day 365
- E. 5 GB log bundles, read only after an outage: to Deep Archive at day 7, expire at day 60

<details><summary>Answer</summary>

**A and D are right.** Rule A leaves each video 370 days in Deep Archive, past its 180-day minimum; Rule D leaves each report 335 days in Flexible Retrieval, past its 90-day minimum. Both are large files that are rarely read.

- **B is wrong.** It springs two traps: each 20 KB icon is billed as 128 KB, and every read from Standard-IA adds a fee per GB.
- **C is wrong.** 29 days in Flexible Retrieval are billed as 90.
- **E is wrong.** 53 days in Deep Archive are billed as 180.

</details>

### Question A9

An engineering firm's on-premises application servers need disks over iSCSI. The firm wants the full data kept in AWS, with only frequently used data kept in the office. Its licensing server must also be running in AWS within minutes if the office is lost. Which pairing fits?

- A. Volume Gateway in stored mode; AWS Backup with a nightly plan
- B. Volume Gateway in cached mode; Elastic Disaster Recovery
- C. Amazon S3 File Gateway; AWS Elastic Disaster Recovery
- D. Volume Gateway in cached mode; nightly EBS snapshots

<details><summary>Answer</summary>

**B is right.** Volume Gateway presents disks over iSCSI; in cached mode the full data lives in AWS and only the busy part is kept on premises. Elastic Disaster Recovery copies a server continuously and launches it in AWS within minutes.

- **A is wrong.** Stored mode keeps the full data in the office, the opposite of what the firm wants, and AWS Backup gives back data, not a running server within minutes.
- **C is wrong.** S3 File Gateway presents a shared folder, not disks.
- **D is wrong.** EBS snapshots copy volumes already in AWS, and they don't launch a running server.

</details>

### Question A10

Which TWO needs does AWS Elastic Disaster Recovery meet, rather than AWS Backup? (Select TWO.)

- A. Keep a year of daily backups of RDS databases and EBS volumes under one plan
- B. Stop anyone, even an administrator, from deleting backups before their retention ends
- C. Launch running copies of on-premises servers in AWS within minutes
- D. Present a shared folder to office PCs while storing the files in S3
- E. Run a failover drill that launches recovery servers without disturbing the source servers

<details><summary>Answer</summary>

**C and E are right.** Elastic Disaster Recovery keeps whole servers copied continuously, launches them in minutes, and supports drills that don't disturb the servers it protects. Backups bring back data; disaster recovery brings back servers.

- **A is wrong.** One plan across services, with a set retention, is AWS Backup's job.
- **B is wrong.** That is AWS Backup Vault Lock, in compliance mode.
- **D is wrong.** That is Amazon S3 File Gateway, a type of AWS Storage Gateway.

</details>

### Question A11

A research group uses a specialist open-source database engine that Amazon RDS doesn't offer. A second team in the same company runs a PostgreSQL database with no special needs. Both teams want as little patching work as possible. Which plan fits?

- A. Both on Amazon RDS, which runs any engine you install
- B. Both on EC2, since running your own is always cheaper
- C. The specialist engine on RDS, and PostgreSQL on EC2
- D. The specialist engine on EC2, and PostgreSQL on Amazon RDS

<details><summary>Answer</summary>

**D is right.** RDS can't run an engine it doesn't offer, so that one must be self-managed on EC2, with its patching and backups. PostgreSQL has no special needs, so it goes on RDS, as AWS recommends for most relational databases, and AWS does the patching and backups.

- **A is wrong.** RDS runs only the engines it offers; you can't install your own.
- **B is wrong.** Running your own isn't always cheaper: it adds patching, backups and failover work, and a mistake there can stop the application.
- **C is wrong.** It reverses the two.

</details>

### Question A12

An exam board's results site runs on Amazon RDS for MySQL in one Availability Zone. On results day, reads jump to many times their normal level and pages slow down. The board also wants the database to keep running, losing no committed results, if its Availability Zone fails. Which plan meets both needs?

- A. Read replicas for the reads, and Multi-AZ for the failure
- B. A Multi-AZ DB instance deployment alone, sending reads to its standby
- C. Read replicas alone, one taking over if the AZ fails
- D. Hourly snapshots, restored to a new database if the AZ fails

<details><summary>Answer</summary>

**A is right.** Each need gets its own copy: read replicas answer read-only queries, and a Multi-AZ standby, updated synchronously, takes over automatically when the Availability Zone fails.

- **B is wrong.** In a Multi-AZ DB instance deployment, the standby serves no queries. (A Multi-AZ DB cluster has readable standbys, but that isn't what this option describes.)
- **C is wrong.** A read replica doesn't take over by itself; someone must promote it, and because it is copied asynchronously, the latest results may be missing.
- **D is wrong.** A restore creates a new database and takes time, and anything written since the last snapshot is lost.

</details>

### Question A13

A travel app has three kinds of data: itineraries, always fetched by trip ID, whose traffic jumps tenfold in holiday seasons; a "travelers who went here also went there" feature over millions of trips; and five years of bookings from several systems, analyzed by month and route. Which set of databases fits, in that order?

- A. Amazon RDS; Amazon DocumentDB; Amazon ElastiCache
- B. Amazon DynamoDB; Amazon Neptune; Amazon Redshift
- C. Amazon DynamoDB; Amazon Redshift; Amazon Neptune
- D. Amazon ElastiCache; Amazon Neptune; Amazon RDS

<details><summary>Answer</summary>

**B is right.** Items fetched by one key at any scale fit DynamoDB; relationships across many links fit Neptune, a graph database; analysis of years of data from many sources fits Redshift, a data warehouse.

- **A is wrong.** None of the three matches its shape: no joins are needed for itineraries, the feature is about relationships, not documents, and ElastiCache is a cache, not a warehouse.
- **C is wrong.** It swaps the last two: Redshift is for analysis, and Neptune is for relationships.
- **D is wrong.** ElastiCache sits in front of a main store rather than replacing one, and RDS runs the business rather than studying years of it.

</details>

### Question A14

A company is moving an on-premises Oracle database to Amazon RDS for PostgreSQL, and the database must keep taking orders during the move. The team ran AWS SCT. It converted most of the schema and listed some stored procedures it couldn't convert. What happens next?

- A. AWS DMS converts the rest of them while it copies the data
- B. AWS SCT copies the data across once the team has fixed them
- C. The move stops, because SCT couldn't convert all of them
- D. The team converts them by hand; then DMS moves the data

<details><summary>Answer</summary>

**D is right.** SCT converts what it can and lists what you must convert by hand. Then AWS DMS copies the data while the source keeps running, and keeps copying each new change until the switch-over.

- **A is wrong.** DMS moves data; converting the schema and code is the job of SCT or DMS Schema Conversion, before the data moves.
- **B is wrong.** SCT converts the schema; it doesn't move any data.
- **C is wrong.** A list of items to convert by hand is a normal result, not a reason to stop.

</details>

### Question A15

A new startup with no existing database code is building a fitness app. Each user's profile has different fields, and the app always fetches a profile by user ID. Traffic is unpredictable, and the founders want no servers to size and to pay per request. Which database fits best?

- A. Amazon DocumentDB
- B. Amazon Neptune
- C. Amazon DynamoDB
- D. Amazon Redshift

<details><summary>Answer</summary>

**C is right.** DynamoDB is serverless, supports key-value and document data whose fields vary, gives fast responses at any scale, and in on-demand mode bills per request.

- **A is wrong.** DocumentDB also stores documents, but what points to it is existing MongoDB code, which this startup doesn't have, and it bills by instance hours much like RDS.
- **B is wrong.** Neptune is for relationships many links deep, not profiles fetched by ID.
- **D is wrong.** Redshift is a warehouse for analysis, not the store an app reads and writes all day.

</details>

## Correction map

For each question you missed, reread the section, then try the "another way to see it" line before you redo the practice. Lessons are in this module.

| Question | Objective | Reread | Another way to see it | Practice |
|---|---|---|---|---|
| A1 | 05.01a Choose block, file or object storage | 05.01, [Block storage: a disk attached to one server](01-block-file-object.md#block-storage-a-disk-attached-to-one-server) | Instance store is part of the physical computer, and a stop hands that computer back. An EBS volume is a separate device that waits for the instance to return. | 05.01, [Practice](01-block-file-object.md#practice) |
| A2 | 05.01a | 05.01, [Object storage: whole objects in a bucket, reached over the web](01-block-file-object.md#object-storage-whole-objects-in-a-bucket-reached-over-the-web) | Ask what the program expects to see: a disk, a shared folder, or whole files over the web. Many programs and devices fetching whole files means object storage. | 05.01, [Worked example: placing the bakery's data](01-block-file-object.md#worked-example-placing-the-bakerys-data) |
| A3 | 05.01a | 05.01, [Where the copies live decides what a failure can take](01-block-file-object.md#where-the-copies-live-decides-what-a-failure-can-take) | Count the Availability Zones each option uses. Anything in one AZ needs a copy somewhere else. | 05.01, [Block, file and object side by side](01-block-file-object.md#block-file-and-object-side-by-side) |
| A4 | 05.02a Explain how each S3 protection works | 05.02, [The big picture: five layers](02-s3-in-practice.md#the-big-picture-five-layers-three-of-them-already-on) | For each event, ask which of the five layers would have said no. If the person was allowed to do it, none of them would. | [Lab 05](07-lab-05-versions-and-lifecycle.md), Part C |
| A5 | 05.02a | 05.02, ["Encrypted means safe from everyone" is wrong](02-s3-in-practice.md#encrypted-means-safe-from-everyone-is-wrong) | Encryption answers "can the stored bytes be read without the key?". Policies and Block Public Access answer "who may ask?". | 05.02, [Worked example: protecting two buckets](02-s3-in-practice.md#worked-example-protecting-two-buckets) |
| A6 | 05.03a Choose a class and a lifecycle rule | 05.03, [Three questions pick a class](03-storage-classes-and-lifecycle.md#three-questions-pick-a-class-how-often-how-fast-how-replaceable) | Ask the three questions in order: how often is it read, how fast must it come back, could you recreate it? | [Sim S5](09-sim-lifecycle-cost-timeline.md), Part 1 |
| A7 | 05.03a | 05.03, [Three cost traps](03-storage-classes-and-lifecycle.md#three-cost-traps) | Days in a class are the expiration day minus the transition day. Compare that with the class's minimum before you save a rule. | [Sim S5](09-sim-lifecycle-cost-timeline.md), Part 2 |
| A8 | 05.03a | 05.03, [Three cost traps](03-storage-classes-and-lifecycle.md#three-cost-traps) and [The numbers in one place](03-storage-classes-and-lifecycle.md#the-numbers-in-one-place) | Check every rule for three things: the object's size, its days in each class, and how often it is read. | [Sim S5](09-sim-lifecycle-cost-timeline.md), Part 2 |
| A9 | 05.04a Match a hybrid or backup need to a service | 05.04, [Storage Gateway](04-hybrid-storage-and-backup.md#storage-gateway-lets-on-premises-software-use-aws-storage-without-changing) and [Elastic Disaster Recovery](04-hybrid-storage-and-backup.md#elastic-disaster-recovery-keeps-whole-servers-ready-to-launch) | For Volume Gateway, ask where the full dataset lives: in AWS (cached) or in the office (stored). Then ask whether you need data back or a running server. | 05.04, [Worked example](04-hybrid-storage-and-backup.md#worked-example-matching-the-bakerys-needs-to-services) |
| A10 | 05.04a | 05.04, [A snapshot, AWS Backup and Elastic Disaster Recovery side by side](04-hybrid-storage-and-backup.md#a-snapshot-aws-backup-and-elastic-disaster-recovery-side-by-side) | Look at what you get back: a snapshot and AWS Backup give you data to restore; only Elastic Disaster Recovery gives you running servers. | 05.04, [Practice](04-hybrid-storage-and-backup.md#practice) |
| A11 | 05.05a Choose hosting, and high availability or read scaling | 05.05, [AWS recommends a managed database](05-managed-or-self-managed-databases.md#aws-recommends-a-managed-database-unless-you-have-a-reason-not-to) | Self-manage only for a real reason, such as an engine RDS doesn't offer. Then every chore RDS would do is yours. | 05.05, [Worked example](05-managed-or-self-managed-databases.md#worked-example-setting-up-the-bakerys-order-database) |
| A12 | 05.05a | 05.05, [Multi-AZ](05-managed-or-self-managed-databases.md#a-multi-az-deployment-keeps-the-database-running-when-an-availability-zone-fails) and [read replicas](05-managed-or-self-managed-databases.md#a-read-replica-takes-read-only-work-off-the-primary) | Name each failure first. A broken AZ needs a standby; too many reads need a replica; damaged data needs a backup. One copy rarely does two jobs. | [Sim S6](10-sim-multi-az-vs-read-replica.md), Part 1 |
| A13 | 05.06a Pick a database for a shape of data | 05.06, [The database services side by side](06-choosing-a-database.md#the-database-services-side-by-side) | First ask whether the data runs the business or studies it. Then ask its shape: key, tables, documents, relationships, or hot reads. | 05.06, [Worked example](06-choosing-a-database.md#worked-example-the-bakerys-databases) |
| A14 | 05.06a | 05.06, [DMS moves the data, SCT converts the schema](06-choosing-a-database.md#moving-a-database-in-dms-moves-the-data-sct-converts-the-schema) | SCT translates the structure; DMS carries the contents. Translation comes first, and only when the engine changes. | 05.06, [Practice](06-choosing-a-database.md#practice) |
| A15 | 05.06a | 05.06, [DynamoDB](06-choosing-a-database.md#dynamodb-stores-items-by-key-at-any-scale-with-no-servers-to-run) and [DocumentDB](06-choosing-a-database.md#documentdb-fits-documents-neptune-fits-relationships) | Fields that vary don't decide between the two: both store documents. Existing MongoDB code points to DocumentDB; fetching by one key with no servers points to DynamoDB. | [Lab 06](08-lab-06-a-dynamodb-table.md) |

## Check B: parallel retest

Take Check B after you have worked through the correction map. Question B1 tests the same objective as A1, and so on. The pass mark is the same: 12 of 15.

### Question B1

An analyst keeps a working dataset on a disk attached to an EC2 instance. Next month the team will delete that instance and attach the same disk to a new instance in the same Availability Zone, without losing the data. Which choice fits?

- A. An EBS volume whose Delete on termination setting is No
- B. An instance store volume on the current instance
- C. An EBS volume whose Delete on termination setting is Yes
- D. An S3 bucket attached to the instance as its disk

<details><summary>Answer</summary>

**A is right.** An EBS volume exists apart from its instance. With Delete on termination set to No, it is kept when the instance is deleted, and it can be attached to a new instance in the same AZ.

- **B is wrong.** Instance store is erased when the instance is stopped or terminated.
- **C is wrong.** With that setting, the volume is deleted along with the instance.
- **D is wrong.** S3 isn't attached as a disk; programs reach it through a web API.

</details>

### Question B2

A school district is moving its storage to AWS. Which pairing of a need and a storage service fits?

- A. The boot disk of a web server on EC2: Amazon S3
- B. Linux servers in three AZs that share the same lesson files: one EBS volume
- C. Videos streamed to students' tablets over HTTPS: EC2 instance store
- D. A Windows staff drive using Active Directory: FSx for Windows File Server

<details><summary>Answer</summary>

**D is right.** Amazon FSx for Windows File Server provides Windows file shares over SMB, joined to Microsoft Active Directory, so the drive and its permissions work as before.

- **A is wrong.** A server boots from block storage, an EBS volume. S3 isn't a disk.
- **B is wrong.** An EBS volume attaches to one server in one AZ. Shared files for Linux servers fit Amazon EFS.
- **C is wrong.** Instance store is temporary and belongs to one instance. Files streamed to many devices fit Amazon S3.

</details>

### Question B3

A media company's Linux transcoding servers run in three Availability Zones. All of them must read and write the same working files through a mounted folder, and the files must stay available if one AZ fails. Which option fits?

- A. An Amazon EFS One Zone file system
- B. An Amazon EFS Regional file system
- C. An Amazon EBS volume in the first AZ
- D. EC2 instance store on each server

<details><summary>Answer</summary>

**B is right.** A Regional EFS file system is shared by many Linux servers at once over NFS, and it stores data across several AZs, so it keeps working if one fails.

- **A is wrong.** One Zone keeps the data in a single AZ, where it can be lost with the AZ.
- **C is wrong.** An EBS volume attaches to one server, and only in its own AZ.
- **D is wrong.** Each server's instance store is its own temporary disk; the servers couldn't share it.

</details>

### Question B4

A bookshop creates a new S3 bucket and changes none of its settings. Which TWO risks do the bucket's default settings already reduce? (Select TWO.)

- A. A bucket policy is written that would let anyone read the files
- B. A teammate overwrites a good price list with last year's old one
- C. A clerk deletes last year's invoices from the bucket by mistake
- D. A manager with read permission forwards the files to a competitor
- E. A disk holding the bucket's data is read outside the data center

<details><summary>Answer</summary>

**A and E are right.** Block Public Access, on for new buckets, overrides a policy that would grant public access. Default encryption (SSE-S3) protects the stored bytes, so a disk read outside S3 gives nothing readable.

- **B is wrong.** Versioning would keep the good version, but it is off until you turn it on.
- **C is wrong.** Without versioning, a delete is final, and AWS can't recover it however durable S3 is.
- **D is wrong.** The manager was allowed to read. Only least privilege limits what a permitted reader can take.

</details>

### Question B5

A florist says, "Our S3 bucket encrypts everything, so it doesn't matter if we switch off Block Public Access." Which reply is accurate?

- A. She's right: members of the public would see only scrambled bytes
- B. She's right: with SSE-S3, only she holds the key that decrypts them
- C. She's wrong: S3 decrypts for anyone allowed to read, public or not
- D. She's wrong: new objects aren't encrypted unless she turns it on

<details><summary>Answer</summary>

**C is right.** Encryption at rest protects the stored bytes. Any request that the bucket's permissions allow gets the objects decrypted, so a public bucket would serve readable files to everyone.

- **A is wrong.** S3 decrypts automatically for allowed requests, public ones included.
- **B is wrong.** With SSE-S3, S3 manages the key and uses it for every allowed request.
- **D is wrong.** S3 has encrypted every new object by default since January 5, 2023.

</details>

### Question B6

An online store's product photos are shown on its home page and read thousands of times a day. To cut costs, a developer wants to move them from S3 Standard to S3 Standard-IA. What should the team do?

- A. Keep them in Standard, because Standard-IA charges for each read
- B. Move them to Standard-IA, which is cheaper for any data
- C. Move them to One Zone-IA, which is cheaper still
- D. Move them to Glacier Instant Retrieval, which is just as fast

<details><summary>Answer</summary>

**A is right.** S3 Standard is for data read often, with no retrieval fee. The colder classes charge for each GB read, so moving busy data there can cost more than leaving it in Standard.

- **B is wrong.** Standard-IA is cheaper to store, but not to read. It suits data read about once a month.
- **C is wrong.** It has the same reading fee, and it keeps data in one AZ.
- **D is wrong.** It reads in milliseconds, but it is built for data read about once a quarter, and it charges for each GB read too.

</details>

### Question B7

A lifecycle rule moves a firm's case files to S3 Glacier Deep Archive at day 30 and expires them at day 120. As of 2026-10-23, Deep Archive bills a minimum storage duration of 180 days, and Glacier Flexible Retrieval a minimum of 90 days. The files must still be deleted at day 120, and after day 30 a wait of hours to read one is fine. Which change avoids the extra charge?

- A. Move them to Deep Archive at day 1 instead
- B. Move them to Glacier Flexible Retrieval at day 30 instead
- C. Keep the rule, because S3 waives minimums for lifecycle expirations
- D. Expire them at day 150 instead, to use more of the minimum

<details><summary>Answer</summary>

**B is right.** From day 30 to day 120 is 90 days, which meets Flexible Retrieval's minimum, and a wait of hours to read is acceptable after day 30.

- **A is wrong.** 119 days in Deep Archive are still billed as 180.
- **C is wrong.** The minimum applies however the object leaves, including by a lifecycle rule.
- **D is wrong.** It breaks the requirement to delete the files at day 120, and 120 days in Deep Archive are still under its minimum.

</details>

### Question B8

A team reviews five proposed lifecycle rules. As of 2026-10-23, S3 Standard-IA has a 30-day minimum storage duration and bills objects under 128 KB as 128 KB; S3 Glacier Flexible Retrieval has a 90-day minimum; S3 Glacier Deep Archive has a 180-day minimum. Which TWO rules avoid the minimum-duration, minimum-size and reading-cost traps? (Select TWO.)

- A. 10 KB sensor readings, checked every week: to Standard-IA at day 30, expire at day 400
- B. 4 GB database dumps, rarely read: to Flexible Retrieval at day 30, expire at day 150
- C. 800 MB invoices, read a few times a year: to Standard-IA at day 30, expire at day 400
- D. 3 GB daily exports, rarely read: to Deep Archive at day 1, expire at day 90
- E. 2 GB banner images that the website reads every hour: to Standard-IA at day 7

<details><summary>Answer</summary>

**B and C are right.** Rule B leaves each dump 120 days in Flexible Retrieval, past its 90-day minimum. Rule C leaves each invoice 370 days in Standard-IA, past its 30-day minimum, and occasional reading is what Standard-IA is for.

- **A is wrong.** Each 10 KB file is billed as 128 KB.
- **D is wrong.** 89 days in Deep Archive are billed as 180.
- **E is wrong.** Hourly reads from Standard-IA add a fee for every GB read, which can cost more than Standard.

</details>

### Question B9

A school district's backup software writes weekly backups to physical tapes, and staff want to stop handling tapes without changing the backup jobs. Separately, its EBS volumes and RDS databases in two AWS accounts need one backup schedule, with copies in a second Region. Which pairing fits?

- A. Amazon S3 File Gateway; AWS Elastic Disaster Recovery
- B. Tape Gateway; AWS Elastic Disaster Recovery
- C. Volume Gateway in stored mode; snapshots taken by each team
- D. Tape Gateway; AWS Backup

<details><summary>Answer</summary>

**D is right.** Tape Gateway looks like a tape library to the existing backup software and stores the virtual tapes in AWS. AWS Backup runs one plan across services and accounts and copies backups to another Region.

- **A is wrong.** S3 File Gateway presents a shared folder, not tapes, and Elastic Disaster Recovery keeps servers ready to launch rather than running a backup schedule.
- **B is wrong.** The first half fits, but Elastic Disaster Recovery isn't a backup schedule with retention across services.
- **C is wrong.** Volume Gateway presents disks, not tapes, and snapshots taken by each team are what AWS Backup replaces with one plan.

</details>

### Question B10

An IT lead writes notes on AWS's recovery services for a new colleague. Which TWO notes are correct? (Select TWO.)

- A. An EBS snapshot copies a whole server, ready to launch within minutes
- B. AWS Backup restores data from recovery points taken on a schedule
- C. Elastic Disaster Recovery is a cheaper storage tier inside AWS Backup
- D. AWS Backup can present a tape library to on-premises backup software
- E. Elastic Disaster Recovery copies server changes to a staging area

<details><summary>Answer</summary>

**B and E are right.** AWS Backup keeps recovery points on a schedule and gives back data. Elastic Disaster Recovery copies every change to a low-cost staging area in AWS, and launches running servers from it when needed.

- **A is wrong.** An EBS snapshot is a point-in-time copy of one volume, not a server ready to launch.
- **C is wrong.** They are separate services for different jobs, which AWS designs to be used together.
- **D is wrong.** That is Tape Gateway, a type of AWS Storage Gateway.

</details>

### Question B11

A warehouse company buys stock-control software that works only with a database engine Amazon RDS doesn't offer. The IT manager decides to run that database on an EC2 instance and asks what this means for her small team. Which statement is accurate?

- A. AWS patches the database engine, because the instance runs on AWS
- B. Turning on a Multi-AZ deployment for the instance gives it automatic failover
- C. The team patches, backs up and builds failover for it, the jobs RDS would do
- D. Nothing changes compared with RDS, apart from the hourly price

<details><summary>Answer</summary>

**C is right.** A self-managed database on EC2 leaves the operating system, the database software, backups, replication and failover with the customer. AWS runs only the hardware underneath. That is the price of needing an engine RDS doesn't offer.

- **A is wrong.** On EC2, AWS's line sits below the guest operating system; the database engine is the customer's to install and patch.
- **B is wrong.** Multi-AZ deployments are an RDS feature. On EC2, the team would have to build its own standby and failover.
- **D is wrong.** Everything RDS does for you, from patching to backups, becomes the team's work.

</details>

### Question B12

A company's RDS for PostgreSQL database has one read replica in a second Availability Zone, and no Multi-AZ deployment. The primary's Availability Zone fails. What happens?

- A. RDS fails over to the replica by itself in a minute or two
- B. Someone must promote the replica, and recent writes may be lost
- C. The replica starts accepting writes in the failed primary's place
- D. Nothing is lost, because the replica is copied synchronously

<details><summary>Answer</summary>

**B is right.** For RDS engines other than Aurora, a read replica doesn't take over by itself: someone promotes it and points the application at it. It is copied asynchronously, so changes it hadn't received yet are lost.

- **A is wrong.** Automatic failover is what a Multi-AZ standby does, and this database has none.
- **C is wrong.** A read replica accepts no writes until it is promoted.
- **D is wrong.** Replicas are copied asynchronously and can lag; the Multi-AZ standby is the synchronous copy.

</details>

### Question B13

A food-delivery company has three kinds of data: restaurant menus stored as JSON documents by an app already written with MongoDB drivers; live rider locations, read thousands of times a second, which must be answered in microseconds in front of the main store; and orders that link customers, restaurants and dishes and must be saved whole. Which set of databases fits, in that order?

- A. Amazon DynamoDB; Amazon Neptune; Amazon Redshift
- B. Amazon DocumentDB; Amazon Redshift; Amazon Aurora
- C. Amazon Neptune; Amazon ElastiCache; Amazon DynamoDB
- D. Amazon DocumentDB; Amazon ElastiCache; Amazon Aurora

<details><summary>Answer</summary>

**D is right.** JSON documents with existing MongoDB code point to DocumentDB; microsecond reads in front of a main store point to ElastiCache, a cache in memory; linked tables saved in one transaction point to a relational database such as Aurora.

- **A is wrong.** DynamoDB lacks the MongoDB compatibility, Neptune is for relationships rather than hot reads, and Redshift is for analysis, not taking orders.
- **B is wrong.** Redshift runs large analytical queries; it doesn't answer in microseconds.
- **C is wrong.** Menus aren't a graph, and orders that must be saved across linked tables are relational, not key-value.

</details>

### Question B14

A company plans to move an on-premises Microsoft SQL Server database to Amazon RDS for PostgreSQL while the business keeps using it. Which order of steps is right?

- A. AWS DMS copies the data first; then AWS SCT converts the schema in the target
- B. AWS SCT copies the schema and the data together, so DMS isn't needed
- C. AWS SCT converts the schema; then AWS DMS copies the data and each new change
- D. AWS Backup backs up the database, and the backup is restored into RDS for PostgreSQL

<details><summary>Answer</summary>

**C is right.** The engine changes, so this is a heterogeneous migration: convert the schema first, with SCT or DMS Schema Conversion, then let DMS copy the data and keep copying changes until the switch-over.

- **A is wrong.** The target needs a converted schema before the data can go into it.
- **B is wrong.** SCT converts the schema only; DMS moves the data.
- **D is wrong.** A backup of one engine can't be restored into a different engine, and it wouldn't keep up with new orders during the move.

</details>

### Question B15

A team's product-review app is already written with MongoDB drivers and queries, and each review has different fields. The team is choosing between Amazon DocumentDB and Amazon DynamoDB. Which fact most favors DocumentDB here?

- A. DocumentDB works with the app's MongoDB code
- B. Only DocumentDB can store records whose fields vary
- C. DocumentDB answers queries from memory in microseconds
- D. DocumentDB bills per request, with no servers to size

<details><summary>Answer</summary>

**A is right.** DocumentDB is compatible with MongoDB's drivers and tools, so the app works with few changes. That is what tips the choice.

- **B is wrong.** DynamoDB also stores documents whose fields vary.
- **C is wrong.** Microsecond answers from memory describe ElastiCache.
- **D is wrong.** Per-request billing with no servers describes DynamoDB's on-demand mode; DocumentDB bills by instance hours, much like RDS.

</details>

## Enrichment for learners who pass

These are harder than the checks: there is more than one good answer. Write your answer before you open the model.

### Task 1: plan a second shop's data

The bakery opens a second shop. The shop has a Windows PC that staff use to save supplier invoices in a shared folder, a till server that must run again within minutes if the shop floods, ten years of sales records to keep, and a loyalty app whose members' profiles are always fetched by member ID. Write the one-page data plan: where each kind of data lives, any lifecycle rule, how it is backed up or recovered, and one setting on your side of the line for each. Name the Well-Architected best practice behind two of your choices.

<details><summary>Model answer</summary>

| Data | Where it lives | Rule, backup or recovery | Your side of the line |
|---|---|---|---|
| Supplier invoices | S3 File Gateway over SMB, storing each file in an S3 bucket | Versioning on, with a rule that deletes noncurrent versions after an agreed window | Keep Block Public Access on, and decide who may read the bucket |
| Till server | Stays in the shop | Elastic Disaster Recovery, with a drill to prove the minutes; a nightly backup as well, for mistakes | Run the drills, and decide which Region recovers it |
| Ten years of sales records | An S3 bucket: Standard for a month, then Glacier Deep Archive, expiring after ten years | Consider Object Lock so nobody deletes them early; replicate or back up to a second Region | The retention period itself, which comes from the accountant, not AWS |
| Loyalty profiles | DynamoDB, on demand | Point-in-time recovery, or AWS Backup | IAM permissions for who can read and write the table |

Two best practices: matching each kind of data to its store is [PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html); putting the ten-year rule in a lifecycle rule is [COST04-BP05 Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html). A good answer also says what it would not add yet, for example a cache or a graph database, until the shop's size calls for one.

</details>

### Task 2: prove that a restore works

The owner says, "We have backups, so we're fine." Design a restore test for the order database (RDS) and the photo bucket (S3, versioned) that you would run every quarter. Say what you restore, where to, what you check, how you would know the test met the time and data-loss targets from lesson 03.03, and how you clean up so the test doesn't keep costing money.

<details><summary>Model answer</summary>

- **Order database:** restore the automated backups to a new database at a point in time an hour ago. Check that the latest orders are there, that the application can connect to it, and how long the restore took. Compare the time with the recovery time objective and the gap in orders with the recovery point objective. Delete the restored database when you finish, because it bills by the hour.
- **Photo bucket:** pick a photo, overwrite it on purpose, then restore the earlier version; delete a test file and remove its delete marker. Check that the right version comes back.
- **Record it:** write down the date, the time taken and anything that failed. A test that finds a problem is a success.

This is [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html) and the reliability design principle "[Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)": until you have restored from a backup, you only hope it works.

</details>

### Task 3: audit the safe settings that start off

Make a table of storage and database settings in this module that start off, or start short, in a new account or a new resource. For each, say what risk it leaves open and who must change it. Then pick the two you would fix first, and say why.

<details><summary>Model answer</summary>

| Setting | Starts as | Risk left open | Who changes it |
|---|---|---|---|
| Account-level S3 Block Public Access | Off in the new account we created on 2026-10-23 | A bucket whose own setting is turned off could be made public | You |
| EBS encryption by default | Off in that account until we turned it on | New volumes and their snapshots unencrypted | You, once per Region |
| Block Public Access for EBS snapshots | Off in that account | A snapshot shared publicly by mistake | You |
| S3 Versioning | Off for each new bucket | An overwrite or delete can't be undone | You, per bucket |
| RDS automated backup retention | The default number of days, which may be shorter than your checking routine | A mistake found too late to restore | You choose the period; AWS takes the backups |
| RDS Multi-AZ | Off unless you choose it | An AZ failure stops the database | You choose; AWS runs the standby |

Which two first: account-level Block Public Access, because a public leak is immediate and hard to undo; and versioning (or backups) on the buckets that hold data you can't recreate, because durability doesn't undo deletes. The pattern behind the table: AWS makes many defaults safe, but every row is a decision on your side of the line. Encryption by default supports [SEC08-BP02 Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html); turning backups on and keeping them long enough supports [REL09-BP03 Perform data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html).

</details>

---

"Module 05 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
