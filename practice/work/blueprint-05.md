# Blueprint: Module 05, Storing data: storage and databases

Items file: `practice/items/05-storing-data.yaml`. Targets from the brief: about 85 questions (about
17 "Select TWO") and 22 concept cards. Exam tasks: 3.6 (storage), 3.4 (databases), the storage-cost
part of 4.1, and 2.1 where a page's "your side of the line" section is tested. No prices are
tested.

The course plan gives Module 05 six objectives, one per lesson. Each is central, so each gets
more than the minimum; the rows under each objective show how its questions spread over the
sections that teach it. Levels in brackets are the course plan's (C concept, J judgment; Un
understand, Ap apply).

Counts are the actual counts in the items file (updated at the end).

## Objectives

| Objective | Wording (course plan) | Level | Taught on | Questions | Multi | Cards |
|---|---|---|---|---|---|---|
| 05.01a | Choose block, file or object storage for an access pattern | C·Ap | 05.01 | 14 | 3 | 4 |
| 05.02a | Explain how Block Public Access, versioning and default encryption each protect data in S3 | C·Un | 05.02 | 14 | 3 | 3 |
| 05.03a | Choose an S3 storage class and a lifecycle rule, avoiding the cost traps | J·Ap | 05.03, Lab 05, Sim S5 | 16 | 3 | 5 |
| 05.04a | Match a hybrid storage or backup need to an AWS service | C·Ap | 05.04 | 13 | 3 | 3 |
| 05.05a | Choose between a self-managed and a managed database, and between high availability and read scaling | J·Ap | 05.05, Sim S6 | 15 | 2 | 4 |
| 05.06a | Pick a database for a shape of data | J·Ap | 05.06, Lab 06 | 17 | 3 | 3 |
| **Total** | | | | **89** | **17** | **22** |

## Spread by section (actual)

Generated from the items file. Levels: r recall, u understanding, a application.


### 05.01a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 01 | Block storage: a disk attached to one server | 3 | 0 | a2 u1 | 1 |
| 01 | "Instance store survives a stop" is wrong | 1 | 0 | u1 | 0 |
| 01 | File storage: one folder tree that many servers share | 4 | 0 | a2 r1 u1 | 0 |
| 01 | Object storage: whole objects in a bucket, reached over the web | 2 | 1 | r1 u1 | 0 |
| 01 | Where the copies live decides what a failure can take | 2 | 1 | a1 u1 | 1 |
| 01 | What you pay for | 1 | 0 | u1 | 1 |
| 01 | Your side of the line | 1 | 1 | u1 | 0 |
| 01 | Worked example: placing the bakery's data | 0 | 0 |  | 1 |

### 05.02a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 02 | Private by default, and Block Public Access keeps it that way | 2 | 0 | a1 u1 | 1 |
| 02 | The big picture: five layers, three of them already on | 1 | 1 | r1 | 1 |
| 02 | "Encrypted means safe from everyone" is wrong | 1 | 0 | u1 | 0 |
| 02 | Encryption at rest is automatic; you choose who holds the keys | 1 | 0 | u1 | 0 |
| 02 | Versioning lets you undo an overwrite or a delete | 6 | 1 | a1 r2 u3 | 0 |
| 02 | "S3 is so durable that AWS can always get my file back" is wrong | 1 | 0 | u1 | 1 |
| 02 | A copy somewhere else: replication and backups | 1 | 0 | r1 | 0 |
| 02 | Your side of the line for S3 | 1 | 1 | u1 | 0 |

### 05.03a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 03 | Three questions pick a class: how often, how fast, how replaceable | 2 | 0 | a2 | 1 |
| 03 | "Standard-IA is as available as Standard" is wrong | 1 | 0 | u1 | 0 |
| 03 | Three Glacier classes: archive by how fast you need it back | 3 | 0 | a3 | 0 |
| 03 | The big picture: from hot to cold | 1 | 1 | r1 | 0 |
| 03 | "Glacier vaults are the S3 Glacier classes" is wrong | 1 | 0 | u1 | 0 |
| 03 | Lifecycle rules move and delete objects for you | 3 | 2 | r1 u2 | 0 |
| 03 | Three cost traps | 3 | 0 | a1 u2 | 2 |
| 03 | Your side of the line | 0 | 0 |  | 1 |
| 07 | Part B: finish a lifecycle rule (completion) | 1 | 0 | a1 | 0 |
| 09 | Part 1: one month of backups, four plans | 1 | 0 | a1 | 0 |
| 09 | Decision 3: the owner asks why Plan B, with more steps, costs more | 0 | 0 |  | 1 |

### 05.04a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 04 | Storage Gateway lets on-premises software use AWS storage without changing | 4 | 0 | a3 u1 | 1 |
| 04 | AWS Backup runs backups for many services from one set of rules | 2 | 0 | a1 r1 | 0 |
| 04 | "Elastic Disaster Recovery is a backup service" is wrong | 1 | 0 | u1 | 0 |
| 04 | Elastic Disaster Recovery keeps whole servers ready to launch | 1 | 0 | a1 | 0 |
| 04 | Snapshots are point-in-time copies of one disk or one database | 2 | 1 | a1 r1 | 0 |
| 04 | "Snowball is the answer for moving lots of data" is wrong | 1 | 0 | u1 | 1 |
| 04 | A snapshot, AWS Backup and Elastic Disaster Recovery side by side | 1 | 1 | u1 | 0 |
| 04 | Your side of the line | 1 | 1 | u1 | 0 |
| 04 | Worked example: matching the bakery's needs to services | 0 | 0 |  | 1 |

### 05.05a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 05 | AWS recommends a managed database unless you have a reason not to | 2 | 0 | a1 u1 | 0 |
| 05 | Your side of the line | 1 | 1 | u1 | 0 |
| 05 | A Multi-AZ deployment keeps the database running when an Availability Zone fails | 3 | 0 | a1 u2 | 1 |
| 05 | A read replica takes read-only work off the primary | 1 | 0 | a1 | 0 |
| 05 | "A read replica gives you high availability" is wrong | 1 | 0 | u1 | 1 |
| 05 | Backups and snapshots take you back in time | 1 | 1 | u1 | 1 |
| 05 | Amazon Aurora is AWS's own relational engine in the RDS family | 2 | 0 | r1 u1 | 0 |
| 05 | What you pay for | 1 | 0 | u1 | 0 |
| 10 | Decision 1: for each event, which copy keeps the bakery going or gets its data back? | 1 | 0 | a1 | 0 |
| 10 | Decision 5 (challenge): losing the whole Region | 1 | 0 | a1 | 1 |
| 10 | Decision 4: "Backups are automatic, so we're covered for mistakes." | 1 | 0 | a1 | 0 |

### 05.06a

| Page | Section | Q | Multi | Levels | Cards |
|---|---|---|---|---|---|
| 06 | DynamoDB stores items by key, at any scale, with no servers to run | 5 | 1 | a2 r1 u2 | 0 |
| 06 | Relational databases fit structured data that links together | 1 | 0 | a1 | 1 |
| 06 | ElastiCache answers from memory in microseconds | 1 | 0 | a1 | 0 |
| 06 | DocumentDB fits documents; Neptune fits relationships | 2 | 0 | a1 u1 | 0 |
| 06 | Redshift studies the business; it doesn't run the shop | 2 | 1 | r1 u1 | 0 |
| 06 | Moving a database in: DMS moves the data, SCT converts the schema | 4 | 1 | a1 r1 u2 | 0 |
| 06 | Your side of the line | 1 | 0 | u1 | 0 |
| 06 | Worked example: the bakery's databases | 0 | 0 |  | 1 |
| 06 | In real work: purpose-built, but no more than you need | 0 | 0 |  | 1 |
| 08 | Get one item, then query one cart | 1 | 0 | u1 | 0 |

## Levels

Target: about 20% recall, 50% understanding, 30% application. Actual: 14 recall, 42 understanding, 33 application (of 89).

## Left out on purpose

- Prices, Free Tier amounts, and limits such as the 50 TB object size, 15 read replicas or 35 days
  of retention: volatile, and the guide says not to memorize them.
- FSx for Lustre, MemoryDB and S3 Express One Zone: out of scope or only to be recognized.
- Designed availability and durability percentages: tested as "lower" or "the same", with the
  dated figures only in explanations.
