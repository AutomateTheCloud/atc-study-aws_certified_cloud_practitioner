---
type: lesson
id: clf-11-01
title: "How AWS charges"
tasks: ["4.1", "4.2", "1.4"]
objectives: ["11.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 07 and the guardrails primer; about 35 minutes; works on a phone"
prerequisites: [clf-02-02, clf-06-01, clf-07-04, guardrails-05]
terms_introduced: [rate, cost driver, time-based charge, storage charge, request charge, data transfer out, idle cost, AWS Free Tier, credits, Free plan, Paid plan, Always Free offer, short-term trial, legacy Free Tier]
pillars: [cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/pricing/"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/s3/pricing/"
  - "https://aws.amazon.com/lambda/pricing/"
  - "https://aws.amazon.com/vpc/pricing/"
  - "https://aws.amazon.com/elasticloadbalancing/pricing/"
  - "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json"
  - "https://aws.amazon.com/free/"
  - "https://aws.amazon.com/free/free-tier-faqs/"
  - "https://aws.amazon.com/free/terms/"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html"
---

# An AWS bill is quantities times rates: read it by its four meters, and know the Free Tier's two clocks

Every charge on an AWS bill is something you used, counted, times a price per unit. Most charges count one of four things: time, storage, requests or data moved. Once you can sort a bill by those four, you can say why it grew. This lesson also explains what "free" means on AWS today, because it changed in 2025 and much older study material is out of date.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 35 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Before and after: the demand curve](../02-why-the-cloud/02-before-and-after-the-demand-curve.md) (fixed and variable expenses), [Amazon EC2](../06-running-applications/01-ec2.md) (what a stopped instance still costs), [Connecting networks and offices](../07-connecting-it/04-connecting-networks-and-offices.md) (data transfer by direction) and [primer page 05](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md) (your money alarms). Each idea you need is restated here in a sentence, so you can follow without them. The bakery's scenario is in the [module brief](00-brief.md).

## Warm-up: what you remember

Answer from memory before you look anything up.

1. From Module 10, "Data, AI and the rest of the catalog": Amazon Athena charges by the data each query scans. Name one way to make the same query cost less.
2. From lesson 06.01: the bakery stops a test server for a month instead of terminating it. What does it still pay for?
3. From lesson 02.02: is an On-Demand server a fixed or a variable expense? Why?

<details><summary>Feedback</summary>

1. **Scan less data.** Compressing the files, partitioning them, or converting them to a columnar format such as Parquet means each query reads less, and so costs less. The price per TB stays the same; the quantity drops.
2. **Its EBS volume, and any Elastic IP address it keeps.** Stopping ends the instance-hour charge, but the disk is still stored for you, and an Elastic IP bills until you release it.
3. **Variable.** You pay only for the time it runs, so the cost follows use. That's the pattern this whole lesson builds on.

</details>

## What you'll learn

By the end of this lesson, you can:

- sort any line on a bill onto one of four meters: time, storage, requests or data transfer;
- say which charges continue when nobody uses a resource;
- say which directions of data transfer are free and which are charged;
- explain why a bill grew, from its line items (objective 11.01a);
- describe the Free Tier as it works today: two plans, credits, two clocks.

Try these before you read on. Guess if you're unsure; the answers are in the lesson.

1. The bakery's bill nearly tripled between November and December. Is that bad news?
2. True or false: a new AWS account gets 12 months of free usage.

## The big picture: four meters

![Four columns, each a meter. Time: EC2 web servers, load balancer, NAT gateway, RDS database, public IPv4 addresses; bills while it exists, busy or idle. Storage: S3 photo bucket, EBS disks, RDS storage and backups, snapshots; bills for what you keep. Requests: S3 GET and PUT, Lambda invocations and GB-seconds, Athena data scanned; bills only when used. Data transfer: out to the internet, across AZs, to another Region, in from the internet at $0; bills for where data goes.](../../images/11-01-four-meters.svg)

*Notice the bottom line of each column. Only the time meter runs when nobody is using anything.*

**Long description.** Four columns. Time, measured in the hours or seconds a resource exists or runs: EC2 web servers, the load balancer, a NAT gateway, the RDS database and public IPv4 addresses; it bills while the resource exists, busy or idle. Storage, measured in GB kept per month: the S3 photo bucket, EBS disks billed at the size you set, RDS storage and backups, and snapshots; it bills for what you keep until it's deleted. Requests, measured by the count: S3 GET and PUT requests, Lambda invocations and GB-seconds, and Athena's data scanned; it bills only when someone uses it. Data transfer, measured in GB moved by direction: out to the internet, across Availability Zones and to another Region, while data in from the internet costs $0; it bills for where data goes.

## Key terms (skip if you know them)

- **Rate:** the price of one unit, such as $0.0208 per instance-hour. Rates differ by Region and change over time.
- **Cost driver:** the quantity that makes a charge go up, such as hours run, GB stored or GB sent out. In this lesson we group drivers onto four meters.
- **Time-based charge:** a charge for each second or hour a resource exists or runs.
- **Storage charge:** a charge per GB kept per month (a **GB-month**).
- **Request charge:** a charge per call or per run, such as per thousand S3 reads.
- **Data transfer out:** data leaving AWS for the internet, or leaving one Availability Zone or Region for another. "Out" is the direction that usually costs.

## Pay as you go means every charge is a quantity times a rate

AWS prices most services by use, with no long-term contract unless you choose one ([AWS pricing](https://aws.amazon.com/pricing/)). So each line on a bill has two parts: how much you used, and the rate for one unit. The Well-Architected Framework's cost optimization design principle "[Adopt a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)" is this idea seen from the customer's side: pay for what you consume, and cut what you don't need.

Lesson 02.02 called this a variable expense. The four meters show what varies:

| Meter | Unit | Bakery example (US East (N. Virginia), as of 2026-10-24) |
|---|---|---|
| Time | instance-hour, hour | A `t3.small` web server: $0.0208 an hour |
| Storage | GB-month | S3 Standard: $0.023 per GB-month for the first 50 TB |
| Requests | per request, per GB-second | S3 GET requests: $0.0004 per 1,000 |
| Data transfer | GB | Out to the internet: $0.09 per GB for the first 10 TB a month, after 100 GB free |

Prices are from AWS's published price lists, retrieved 2026-10-24 (data transfer published 2026-09-16); see the [EC2 On-Demand](https://aws.amazon.com/ec2/pricing/on-demand/) and [S3](https://aws.amazon.com/s3/pricing/) pricing pages for current ones.

Three details make the arithmetic honest:

- **The clock is fine-grained.** On-Demand Linux instances bill by the second with a 60-second minimum; RDS bills by the second with a 10-minute minimum (lessons 06.01 and 05.05).
- **Some rates fall with volume.** S3 Standard costs less per GB after the first 50 TB a month, and data out to the internet gets cheaper after 10 TB. This is economies of scale (task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4)) passed on per customer.
- **The same thing costs different amounts in different Regions.** Lesson 03.02 made price one of the four reasons to choose a Region.

> **Your turn:** Sort these bakery charges onto the four meters: (a) the RDS order database's hourly charge; (b) 50 GB of nightly database snapshots; (c) 200,000 Lambda invocations; (d) 300 GB of backups copied to another Region.

<details><summary>Model answer</summary>

(a) **Time:** RDS bills for every hour (in seconds) the database exists. (b) **Storage:** snapshots bill per GB-month for as long as you keep them. (c) **Requests:** Lambda charges per request and per GB-second of run time. (d) **Data transfer:** copying between Regions is charged per GB.

</details>

## Time-based charges run whether or not anyone uses the resource

A time-based charge counts the hours a resource exists, not the work it does. A web server that served no customers at 3 a.m. still bills for 3 a.m. That's **idle cost**: money for capacity nobody used.

You met the biggest examples in earlier modules:

- **EC2 instances** bill while running. Stopped, they still pay for their EBS volumes (lesson 06.01).
- **A NAT gateway** bills every hour it exists, plus every GB it processes (lesson 07.01).
- **An Application Load Balancer** bills each hour or partial hour, with or without customers (lesson 06.02).
- **Public IPv4 addresses** bill by the hour, in use or idle (lesson 06.01).
- **An RDS database** bills by the hour, and a stopped one restarts by itself after seven days (lesson 05.05).

Time-based charges are why every lab in this guide ends with "find, delete, confirm". They are also what Auto Scaling attacks: lesson 06.02 cut the bakery's year from 72 server-months to 29 by running only the servers each month needed.

> **Check:** Which of these keeps billing if the bakery's site gets no visitors for a whole day?
>
> A. S3 GET requests on the photo bucket
> B. The NAT gateway's hourly charge
> C. Data out to the internet
> D. Lambda invocations

<details><summary>Feedback</summary>

**B is right.** A NAT gateway bills for every hour it exists, whatever passes through it.

- **A is wrong.** No visitors means no photo downloads, so no GET requests.
- **C is wrong.** Nothing is sent out to customers, so nothing is charged for it.
- **D is wrong.** A function that isn't triggered doesn't run and isn't charged.

</details>

## Storage bills for what you keep; requests bill for what's used

**Storage** is charged per GB per month, prorated for the time the data was kept. Two habits from Module 05 change the total:

- **EBS bills the size you set,** not the data you wrote. An 8 GB disk holding 1 GB bills for 8.
- **Colder S3 classes are cheaper per GB** but add retrieval fees, minimum storage durations (30, 90 or 180 days) and a minimum billable object size of 128 KB (lesson 05.03). Moving data to the wrong class can cost more, not less.

**Requests** are charged per call, so they follow customers exactly. In US East (N. Virginia), as of 2026-10-24, S3 Standard charges $0.0004 per 1,000 GET requests and $0.005 per 1,000 PUT, COPY, POST or LIST requests ([Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)). Lambda charges $0.20 per million requests plus a rate per GB-second of run time ([AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/)).

Some services include a monthly free allowance. Lambda's, as of 2026-10-23, covers 1 million requests and 400,000 GB-seconds each month, which is why the bakery's photo resizing costs $0.00 in the worked example below.

> **Your turn:** The bakery keeps 260 GB of photos in S3 Standard and customers download 6 million of them a month. Which costs more at the rates above: keeping the photos, or serving the downloads (requests only, not data transfer)?

<details><summary>Model answer</summary>

**Keeping them:** 260 × $0.023 = **$5.98**. **The requests:** 6,000,000 ÷ 1,000 × $0.0004 = **$2.40**. Storage costs more here, but neither is large. The data those downloads send to the internet is the big one, in the next section.

</details>

## Data transfer is priced by direction: in is free, but out, across and between usually cost

Lesson 07.04 gave you the rates. Here is the same pattern drawn on the bakery's setup, so you can price any arrow on a bill:

![A map of the bakery's setup with seven numbered arrows. 1, in from the internet: free. 2, out to the internet: $0.09 per GB after 100 GB free a month. 3, between two instances in the same Availability Zone: free. 4, web server in AZ a to database in AZ b: $0.01 per GB, charged in each direction. 5, EC2 to S3 in the same Region: free. 6, to another Region: $0.02 per GB to most Regions, $0.01 to US East (Ohio). 7, S3 to CloudFront: free.](../../images/11-01-transfer-map.svg)

*Notice that every free arrow either comes in from the internet or stays close: one AZ, or a service in the same Region. The charged arrows leave: to the internet, to another AZ, to another Region.*

**Long description.** A map. On the left, the internet with customers. In the middle, the US East (N. Virginia) Region holding Availability Zone a (a web server and another instance), Availability Zone b (the database) and the S3 photo bucket. On the right, another Region for backup copies, and CloudFront edge locations. Seven arrows: 1, internet to web server, free; 2, web server to internet, $0.09 per GB after 100 GB free a month; 3, web server to the other instance in the same AZ, free; 4, web server to database across AZs, $0.01 per GB charged in each direction; 5, EC2 to S3 in the same Region, free; 6, database backups to another Region, $0.02 per GB to most Regions and $0.01 to US East (Ohio); 7, S3 to CloudFront, free. Free arrows are solid green and labeled "free"; charged arrows are dashed orange and labeled with the rate.

| Direction, from US East (N. Virginia) | Per GB | Note |
|---|---|---|
| In from the internet | $0.00 | Every Region |
| Within one AZ, private addresses | $0.00 | |
| EC2 to S3, DynamoDB, SQS and similar services in the same Region | $0.00 | Services in the path, such as a NAT gateway, still charge their own fees |
| S3 to CloudFront | $0.00 | |
| Across AZs in the Region | $0.01 each way | So $0.02 per GB for one round trip of the same data |
| To another Region | $0.02 to most; $0.01 to US East (Ohio) | Depends on source and destination |
| Out to the internet | $0.09 for the first 10 TB a month | After 100 GB a month free, counted across all services and Regions |

> **Dated (checked 2026-10-23):** rates from AWS's data transfer price list ([AWSDataTransfer offer file](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json), published 2026-09-16); free cases and the 100 GB allowance from the [EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) and [S3 pricing](https://aws.amazon.com/s3/pricing/) pages. Rates differ by Region and fall as volume grows.

### "In is free, out is charged" is only half the rule

You may have read that only data going out to the internet costs money. That's not right. Data **across Availability Zones** and **between Regions** is charged too, even though it never leaves AWS. A design with servers in two AZs pays a little for every GB they exchange, and a backup copied to a second Region pays per GB copied.

It's tempting because "out to the internet" is usually the biggest transfer line, and many notes stop there. Exam task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) names transfer "from one Region to another" and "within the same Region" on purpose.

> **Your turn:** The bakery's web server in AZ a sends 300 GB a month to the database in AZ b. A colleague says, "That's inside AWS, so it's free." What does it cost at the rates above, and what would make it free?

<details><summary>Model answer</summary>

**About $6.00:** 300 GB × $0.01 on each side = 300 × $0.02. It would be free only if both were in the same AZ, which would give up the high availability that two AZs buy (lesson 03.01). Most teams keep the two AZs and pay the small charge: a trade-off, not a mistake.

</details>

## Worked example: why did the bakery's bill nearly triple?

The owner forwards two monthly bills, November and December, and asks: "What happened, and is something wrong?" The order database is left out, because its charge was the same in both months, and so are the web servers' public IPv4 addresses (lesson 07.01), to keep the table short.

![Waterfall chart. November total $73.48. Then NAT gateway, new, hours and data: plus $39.60. Data out to the internet: plus $54.00. More web server hours: plus $30.37. Web server to database across AZs: plus $4.00. Disks, photo storage and requests: plus $4.26. December total $205.71.](../../images/11-01-bill-waterfall.svg)

*Notice the orange bar. Everything else grew because customers did; the NAT gateway grew because someone added it.*

**Long description.** A waterfall chart in US dollars. It starts with November's total, $73.48. Five increases follow: the new NAT gateway, hours and data processed, plus $39.60 (orange, a new resource, not caused by customers); data out to the internet plus $54.00; more web server hours plus $30.37; web server to database across AZs plus $4.00; disks, photo storage and requests plus $4.26 (all yellow, grew with customers). It ends with December's total, $205.71.

| Line item | Meter | November | December |
|---|---|---|---|
| Web servers, `t3.small` (2 then an average of 4, 730 hours) | Time | $30.37 | $60.74 |
| Load balancer hours | Time | $16.43 | $16.43 |
| NAT gateway hours (new on 1 December) | Time | $0.00 | $32.85 |
| Server disks, EBS gp3, 8 GB each | Storage | $1.28 | $2.56 |
| Photo bucket, S3 Standard (200 then 260 GB) | Storage | $4.60 | $5.98 |
| Photo downloads, S3 GET (2 then 6 million) | Requests | $0.80 | $2.40 |
| Photo resizing, Lambda (inside the free allowance) | Requests | $0.00 | $0.00 |
| Data out to the internet (300 then 900 GB, 100 GB free) | Data transfer | $18.00 | $72.00 |
| Web server to database across AZs (100 then 300 GB) | Data transfer | $2.00 | $6.00 |
| Data processed by the NAT gateway (150 GB of updates) | Data transfer | $0.00 | $6.75 |
| **Total** | | **$73.48** | **$205.71** |

Quantities are made up for teaching; rates are US East (N. Virginia), from AWS's price lists as of 2026-10-24 (data transfer published 2026-09-16, S3 published 2026-10-15). Our arithmetic.

An expert reads it in four steps:

1. **Sort by meter.** Time went from $46.80 to $110.02, data transfer from $20.00 to $84.75. Storage and requests barely moved.
2. **Ask whether each increase followed customers.** December is the bakery's peak (Module 02). More orders mean more servers (Auto Scaling at work), more photos sent out, and more traffic to the database. Those increases are the business growing, and per order they're cheap.
3. **Find what didn't follow customers.** The NAT gateway is new, and its $32.85 of hours would bill even in a quiet January. Someone added it so servers in private subnets could download updates (lesson 07.01). That's a decision to review: is it needed all month, every month?
4. **Answer the owner.** "Most of the increase is December's customers, and it will fall in January. One new item, a NAT gateway at about $40 a month, is a fixed cost we should review."

That's objective 11.01a. Cutting the steady part of the bill with commitments is lesson 11.02. Seeing these lines yourself, and setting alerts on them, is lesson 11.03, "Estimate, watch, analyze".

> **Your turn:** In January the bakery's customers drop back to November's level, and the NAT gateway stays. Without calculating every line, roughly what will January's bill be, and which line stops it falling all the way back to November's total?

<details><summary>Model answer</summary>

**About $110 to $115.** The customer-driven lines (servers, data out, requests, cross-AZ traffic) fall back towards November's $73.48. The NAT gateway's $32.85 of hours stays, plus a few dollars for the GB it processes, and the photo bucket keeps its extra 60 GB. Time-based charges don't fall when customers leave; that's why the expert flagged it.

</details>

## The Free Tier now: two plans, credits and two clocks

The **AWS Free Tier** is AWS's offer for trying services without paying. Since 15 July 2025 it works through **credits** and a choice of plan. As of 2026-10-24 ([AWS Free Tier](https://aws.amazon.com/free/); Billing User Guide, [Explore AWS services with AWS Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html) and [Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html)):

- **Credits:** a new customer gets USD $100 in credits at sign-up, on either plan, and can earn up to $100 more by completing short activities (the primer's budget earned $20). Usage beyond the always-free allowances comes out of the credits. AWS's Free Tier page sums it up as up to $200 over 6 months on the Free plan.
- **The Free plan** never charges you. It offers only selected services, and none that could use up the credits quickly or buy hardware: no Savings Plans and no Reserved Instances, which lesson 11.02 teaches. It ends after six months or when the credits run out, whichever comes first. Then the account closes. AWS keeps your content for 90 days, and upgrading in that time restores access; leftover credits then apply to later bills.
- **The Paid plan** gives access to every service. Usage beyond the credits is billed at normal rates, and the account doesn't close when the credits run out.
- **Always Free offers** are monthly allowances on more than 30 services, such as Lambda's, on both plans. **Short-term trials** start when you activate a service and are available on the Paid plan only.
- **Upgrading is one way.** You can't move from the Paid plan back to the Free plan. Some actions upgrade a Free plan account automatically, such as joining AWS Organizations, which lesson 11.04, "Many accounts, one bill", relies on.

A Free plan account runs on **two clocks**: the calendar, which stops it six months after sign-up, and the credit balance, which stops it when the credits are spent. Whichever runs out first ends the plan.

![Timeline from sign-up to 12 months. Free plan: a bar to 6 months; it ends then, or sooner if the credits run out, and the account closes. Credits, $100 plus up to $100 more: a solid bar to 6 months, up to $200 over 6 months on the Free plan; a dashed extension to 12 months for leftover credits after an upgrade, whose expiry AWS gives as 6 or 12 months. Paid plan: a bar across all 12 months; it never closes for lack of credits. Always Free: monthly allowances on both plans, with no end date.](../../images/11-01-two-clocks.svg)

*Notice the first two bars. On the Free plan, the calendar and the credits are the two clocks, and both stop by six months. Only after an upgrade can leftover credits outlast the plan, and that part is dashed because AWS's pages disagree on how long.*

**Long description.** A timeline from 0 to 12 months after sign-up, as of 2026-10-24. Free plan: a bar from 0 to 6 months; it ends at 6 months, or sooner if the credits run out, and the account then closes. Credits, $100 plus up to $100 more: a solid bar from 0 to 6 months, which AWS's Free Tier page describes as up to $200 over 6 months on the Free plan; then a dashed bar from 6 to 12 months, labeled as leftover credits after an upgrade, which apply to later bills until they expire, at 6 or 12 months after sign-up depending on which AWS page you read. Paid plan: a bar across all 12 months and beyond; it never closes for lack of credits, and usage beyond the credits is billed. Always Free: monthly allowances on both plans, with no end date. Notes: after the Free plan closes the account, AWS keeps content for 90 days; upgrading in that time restores access, and remaining credits apply to later bills.

> **Dated (checked 2026-10-24):** the [AWS Free Tier](https://aws.amazon.com/free/) page says up to $200 in credits over 6 months on the Free plan, and that the account closes 6 months after sign-up or when the credits run out, whichever comes first. AWS's pages disagree on when leftover credits expire after an upgrade: two answers in the [Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/) say 6 months after sign-up and two say 12, and the [Free Tier terms](https://aws.amazon.com/free/terms/) say 12. The Free plan account we opened on 2026-10-23 showed its credits expiring 12 months after sign-up on its **Credits** page. Check your own Credits page; AWS may change these terms at any time.

| | Free plan | Paid plan |
|---|---|---|
| Credits at sign-up, plus activities | $100, plus up to $100 | $100, plus up to $100 |
| Can you be charged? | No | Yes, beyond the credits |
| Services | Selected ones | All |
| Savings Plans, Reserved Instances | Not available | Available |
| Short-term trials | No | Yes |
| When credits run out | The account closes | You pay normal rates |

> **Misconception:** "A new AWS account is free for 12 months." That was the **legacy Free Tier**: before 15 July 2025, new accounts got 12 months of free usage on many services. Accounts created before that date stay on it; new accounts get credits and a plan instead. Old courses, practice questions and even one AWS page about Regions still say "12 months". It's tempting because it was true for years, and "12 months" still appears in some of AWS's answers about when credits expire. If a question says "12 months free", read it as describing the old program, and answer with the current one where you can.

> **Your turn:** A friend opened a Free plan account three months ago and has $40 of credits left. They want to buy a one-year Reserved Instance "to make the credits last". What actually happens, and when does their account close if they change nothing?

<details><summary>Model answer</summary>

**They can't buy it on the Free plan.** Reserved Instances and Savings Plans aren't available until they upgrade, and upgrading is one way: from then on, anything beyond the credits is billed to their card. If they change nothing, the account closes at six months after sign-up, three months from now, or sooner if the $40 runs out first.

</details>

## In real work: explain the bill before you cut it

Teams that manage cloud costs well read the bill as data about the business. The Well-Architected Framework names the habits:

- The cost optimization design principle "[Analyze and attribute expenditure](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)": know which workload, and which team, each charge belongs to. Lesson 11.04 and Lab 16 do this with cost allocation tags.
- [COST05-BP02 Analyze all components of the workload](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_analyze_all.html): every component bills, including the ones nobody thinks about, such as a NAT gateway.
- [COST08-BP01 Perform data transfer modeling](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_modeling.html): know where your data moves before the bill tells you.

The four-meter habit also tells you which tool to reach for. Time-based charges are cut by turning things off, rightsizing or committing (lesson 11.02); request and transfer charges by design; surprises by alerts (lesson 11.03).

## Summary

- **Every charge is a quantity times a rate.** Most charges run on one of four meters: time, storage, requests or data transfer. Rates differ by Region, change over time, and sometimes fall with volume.
- **Time-based charges bill while a resource exists,** busy or idle: instances, NAT gateways, load balancers, public IPv4 addresses, databases.
- **Storage bills for what you keep; requests bill for what's used.** EBS bills the size you set; some services have monthly free allowances.
- **Data transfer depends on direction.** In from the internet is free, and so is staying within one AZ or reaching a service in the same Region; data out to the internet, across AZs and between Regions is charged.
- **To explain a bill, sort it by meter** and ask which increases followed customers and which didn't.
- **The Free Tier is credit-based.** $100 plus up to $100 in credits; a Free plan with two clocks, which ends at six months or when the credits run out; a Paid plan that bills beyond them; Always Free allowances on both. "12 months free" describes the legacy Free Tier.

## Practice

1. **Which of these is charged, at the US East (N. Virginia) rates in this lesson?**

   A. 50 GB uploaded from customers' browsers to the bakery's web server
   B. 50 GB sent from an EC2 instance to an S3 bucket in the same Region
   C. 50 GB sent from the web server to the database in another Availability Zone
   D. 50 GB sent from S3 to CloudFront

   <details><summary>Feedback</summary>

   **C is right.** Traffic across AZs is charged on each side, $0.01 per GB each way as of 2026-10-23.

   - **A is wrong.** Data in from the internet is free.
   - **B is wrong.** EC2 to S3 in the same Region has no transfer charge.
   - **D is wrong.** S3 to CloudFront is free; CloudFront then charges for what it delivers.

   </details>

2. **A team deletes every test server on Friday afternoon but leaves a NAT gateway and an idle load balancer. On Monday the bill shows charges for the weekend. Which meter explains them, and why didn't deleting the servers stop them?**

   <details><summary>Feedback</summary>

   **The time meter.** A NAT gateway and a load balancer bill for every hour they exist, whether or not traffic passes. Deleting the servers ended their instance hours, but the other resources kept their own clocks running.

   </details>

3. **Which statement describes the AWS Free Tier for an account opened today, as of 2026-10-24?**

   A. Twelve months of free usage on many services, then normal rates
   B. Credits and a choice of plan; the Free plan ends after six months or when the credits run out
   C. Unlimited free usage of every service on the Free plan
   D. Credits that can buy Reserved Instances on the Free plan

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** That's the legacy Free Tier, for accounts created before 15 July 2025.
   - **C is wrong.** The Free plan offers selected services, and usage beyond the always-free allowances comes out of the credits.
   - **D is wrong.** Reserved Instances and Savings Plans aren't available on the Free plan.

   </details>

4. **The bakery's December bill shows $72 for data out to the internet and $32.85 for NAT gateway hours. The owner asks which one to worry about. Answer in two sentences.**

   <details><summary>Feedback</summary>

   **Model answer:** The $72 grew because December's customers downloaded more pages and photos; it will shrink when they do. The NAT gateway's $32.85 bills every hour whether or not anyone orders, so it's the one to question: is it needed all the time?

   </details>

5. **(From lesson 06.01.) Is a stopped EC2 instance free? Name the charges that continue.**

   <details><summary>Feedback</summary>

   **No.** Its EBS volumes keep billing per GB-month, and an Elastic IP address bills until released. Only the instance-hour charge stops.

   </details>

6. **(From lesson 05.03.) Moving photos that customers view every day from S3 Standard to S3 Glacier Instant Retrieval cuts the storage rate. Why might the bill go up anyway?**

   <details><summary>Feedback</summary>

   **Retrieval fees.** Colder classes charge per GB retrieved and have minimum storage durations, so data read every day costs more to serve from them. The cheaper storage rate is paid for with request and retrieval charges.

   </details>

**Next:** [Purchasing options](02-purchasing-options.md), where the bakery cuts the steady part of its bill.

## Where to check the current details

- [AWS pricing](https://aws.amazon.com/pricing/) and each service's pricing page: [EC2 On-Demand](https://aws.amazon.com/ec2/pricing/on-demand/), [S3](https://aws.amazon.com/s3/pricing/), [Lambda](https://aws.amazon.com/lambda/pricing/), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/pricing/), [Amazon VPC](https://aws.amazon.com/vpc/pricing/) (checked 2026-10-23 and 2026-10-24)
- AWS's machine-readable [data transfer price list](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json) (published 2026-09-16)
- [AWS Free Tier](https://aws.amazon.com/free/), the [Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/), and the Billing User Guide's [Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html) and [Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html) pages (checked 2026-10-24); your own account's **Credits** page for your dates
- [Cost optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html), AWS Well-Architected Framework
- [AWS Certified Cloud Practitioner (CLF-C02) exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) and [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2) (checked 2026-10-24)

---

"How AWS charges" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
