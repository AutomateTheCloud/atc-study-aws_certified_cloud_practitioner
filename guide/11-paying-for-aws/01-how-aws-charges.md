---
type: lesson
id: clf-11-01
title: "How AWS charges"
tasks: ["4.1", "4.2", "1.4"]
objectives: ["11.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 07 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-02-02, clf-06-01, clf-07-04, guardrails-05]
terms_introduced: [rate, cost driver, time-based charge, storage charge, request charge, data transfer out, idle cost, AWS Free Tier, credits, Free plan, Paid plan, Always Free offer, short-term trial, legacy Free Tier]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/pricing/"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/s3/pricing/"
  - "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json"
  - "https://aws.amazon.com/free/"
  - "https://aws.amazon.com/free/free-tier-faqs/"
  - "https://aws.amazon.com/free/terms/"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
---

# An AWS bill is quantities times rates: know the four meters, which transfers cost, and how today's Free Tier works

Every charge on an AWS bill is something you used, counted, times a price per unit, and time and storage keep billing when nobody uses anything. "Free" changed in 2025: new accounts get credits and a choice of two plans, not 12 free months.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** lessons [02.02](../02-why-the-cloud/02-before-and-after-the-demand-curve.md), [06.01](../06-running-applications/01-ec2.md) and [07.04](../07-connecting-it/04-connecting-networks-and-offices.md) help; each idea you need is restated here.

## Warm-up: what you remember

1. From Module 10: Amazon Athena charges by the data each query scans. Name one way to make the same query cost less.
2. From lesson 02.02: is an On-Demand server a fixed or a variable expense?

<details><summary>Feedback</summary>

1. **Scan less data:** compress, partition or convert the files to a columnar format. The price per TB stays the same; the quantity drops.
2. **Variable.** You pay only for the time it runs, so the cost follows use. This lesson builds on that.

</details>

## What you'll learn

By the end of this lesson, you can sort a bill's charges by what drives them and say which directions of data transfer are charged (objective 11.01a), and describe the Free Tier as it works today.

Try this before you read on, and guess if you're unsure: true or false, a new AWS account gets 12 months of free usage?

## The big picture: four meters

![Four meters, each a column: time, storage, requests and data transfer, with the bakery's charges under each and when each one bills.](../../images/11-01-four-meters.svg)

*Notice the bottom line of each column. The time and storage meters keep running when nobody is using anything; requests and data transfer stop.*

**Long description.** Four columns. Time, measured in the hours or seconds a resource exists or runs: EC2 web servers, the load balancer, a NAT gateway, the RDS database and public IPv4 addresses; it bills while the resource exists, busy or idle. Storage, measured in GB kept per month: the S3 photo bucket, EBS disks billed at the size you set, RDS storage and backups, and snapshots; it bills for what you keep until it's deleted. Requests, measured by the count: S3 GET and PUT requests, Lambda invocations and GB-seconds, and Athena's data scanned; it bills only when someone uses it. Data transfer, measured in GB moved by direction: out to the internet, across Availability Zones and to another Region, while data in from the internet costs $0; it bills for where data goes.

## Every charge is a quantity times a rate

AWS prices most services by use, with no long-term contract unless you choose one ([AWS pricing](https://aws.amazon.com/pricing/)). So each line on a bill is how much you used times a **rate**, the price of one unit, such as an hourly price for a web server. The quantity that makes a charge go up is its **cost driver**, and most drivers fall on one of four meters: a **time-based charge** per second or hour a resource exists or runs; a **storage charge** per GB kept per month (a GB-month); a **request charge** per call or per run; and data transfer, per GB moved.

Rates differ by Region and change over time. Some also fall with volume, such as S3 Standard's after the first 50 TB a month: economies of scale (task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4)) passed on to each customer.

**Time-based charges run whether or not anyone uses the resource.** A web server that served nobody at 3 a.m. still bills for 3 a.m.: that's **idle cost**. EC2 instances, NAT gateways, load balancers, public IPv4 addresses and RDS databases all bill by the hour, and a stopped instance still pays for its EBS disks. That's why every lab ends with "find, delete, confirm".

**Storage bills for what you keep, and requests for what's used.** EBS bills the size you set, not the data you wrote. Colder S3 classes cost less per GB but add retrieval fees and minimum stays (lesson 05.02). Requests follow customers, and some services include a monthly free allowance, such as Lambda's 1 million requests (as of 2026-10-23).

> **Your turn:** Sort these bakery charges onto the four meters: (a) the RDS order database's hourly charge; (b) 50 GB of nightly database snapshots; (c) 200,000 Lambda invocations; (d) 300 GB of backups copied to another Region.

<details><summary>Model answer</summary>

(a) **Time:** RDS bills for every hour the database exists. (b) **Storage:** snapshots bill per GB-month for as long as you keep them. (c) **Requests:** Lambda charges per request and per GB-second of run time. (d) **Data transfer:** copying between Regions is charged per GB.

</details>

## Data transfer is priced by direction: in is free, but out, across and between usually cost

**Data transfer out**, data leaving AWS for the internet or leaving one Availability Zone or Region for another, is the direction that usually costs (lesson 07.04):

![A map of the bakery's setup with seven numbered data flows, each labeled free or with its rate per GB.](../../images/11-01-transfer-map.svg)

*Notice that every free arrow either comes in from the internet or stays close: one AZ, or a service in the same Region. The charged arrows leave: to the internet, to another AZ, to another Region.*

**Long description.** A map of the internet, the US East (N. Virginia) Region with two Availability Zones and the S3 photo bucket, another Region and CloudFront edge locations. Seven arrows: 1, internet to web server, free; 2, web server to internet, $0.09 per GB after 100 GB free a month; 3, web server to the other instance in the same AZ, free; 4, web server to database across AZs, $0.01 per GB charged in each direction; 5, EC2 to S3 in the same Region, free; 6, database backups to another Region, $0.02 per GB to most Regions and $0.01 to US East (Ohio); 7, S3 to CloudFront, free. Free arrows are solid green and labeled "free"; charged arrows are dashed orange and labeled with the rate.

> **Dated (checked 2026-10-23):** rates from AWS's data transfer price list ([AWSDataTransfer offer file](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json), published 2026-09-16) and the [EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) page. Services in the path, such as a NAT gateway, still charge their own fees.

### "In is free, out is charged" is only half the rule

A common belief is that only data going out to the internet costs money. That's wrong: data **across Availability Zones** and **between Regions** is charged too, even though it never leaves AWS, so servers in two AZs pay for every GB they exchange. The belief is tempting because "out to the internet" is usually the biggest transfer line on a bill. Exam task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) names transfer "from one Region to another" and "within the same Region" on purpose.

> **Example:** the bakery's December bill is nearly three times November's. Sorted by meter, most of the growth is data out and extra server hours, which followed December's customers and will shrink in January. One new line didn't: a NAT gateway, which bills every hour whether anyone orders or not. That's the line to question.

## The Free Tier now: two plans, credits and two clocks

The **AWS Free Tier** is AWS's offer for trying services without paying. Since 2025-07-15 it works through credits and a choice of plan. As of 2026-10-24 ([AWS Free Tier](https://aws.amazon.com/free/); [Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html)):

- **Credits:** a new customer gets USD $100 in **credits** at sign-up, on either plan, and can earn up to $100 more through short activities. Usage beyond the always-free allowances comes out of the credits.
- **The Free plan** never charges you. It offers selected services, with no Savings Plans or Reserved Instances. It ends after six months or when the credits run out, whichever comes first, and the account closes; upgrading within 90 days restores access.
- **The Paid plan** gives access to every service and bills usage beyond the credits at normal rates.
- **Always Free offers** are monthly allowances on more than 30 services, such as Lambda's, on both plans. **Short-term trials** start when you activate a service, on the Paid plan only.
- **Upgrading is one way.** You can't move from the Paid plan back to the Free plan. Joining AWS Organizations upgrades a Free plan account automatically (lesson 11.04).

So a Free plan account runs on two clocks, the calendar and the credit balance, and whichever runs out first ends it.

> **Misconception:** "A new AWS account is free for 12 months." That's wrong today: it was the **legacy Free Tier**, for accounts created before 2025-07-15, which stay on it. New accounts get credits and a plan instead. It's tempting because it was true for years and old practice questions still say it; read "12 months free" as the old program.

> **Your turn:** A friend opened a Free plan account three months ago and has $40 of credits left. They want to buy a one-year Reserved Instance "to make the credits last". What happens, and when does the account close if they change nothing?

<details><summary>Model answer</summary>

**They can't buy it on the Free plan.** Reserved Instances and Savings Plans need the Paid plan, and upgrading is one way: from then on, anything beyond the credits is billed. If they change nothing, the account closes six months after sign-up, three months from now, or sooner if the $40 runs out first.

</details>

## Summary

- **Every charge is a quantity times a rate,** and most fall on four meters: time, storage, requests or data transfer. Rates differ by Region and some fall with volume.
- **Time-based charges bill while a resource exists,** busy or idle: instances, NAT gateways, load balancers, public IPv4 addresses, databases. EBS bills the size you set.
- **Data transfer depends on direction.** In from the internet is free, and so is staying in one AZ or reaching a service in the same Region; out to the internet, across AZs and between Regions is charged.
- **The Free Tier is credit-based:** $100 plus up to $100 in credits; a Free plan that ends at six months or when the credits run out; a Paid plan that bills beyond them; Always Free allowances on both. "12 months free" is the legacy Free Tier.

## Practice

1. **Which of these is charged, at the US East (N. Virginia) rates in this lesson?**

   A. 50 GB uploaded from customers' browsers to the bakery's web server\
   B. 50 GB sent from an EC2 instance to an S3 bucket in the same Region\
   C. 50 GB sent from the web server to the database in another Availability Zone\
   D. 50 GB sent from S3 to CloudFront

   <details><summary>Feedback</summary>

   **C is right.** Traffic across AZs is charged on each side, $0.01 per GB each way as of 2026-10-23.

   - **A is wrong.** Data in from the internet is free.
   - **B is wrong.** EC2 to S3 in the same Region has no transfer charge.
   - **D is wrong.** S3 to CloudFront is free; CloudFront then charges for what it delivers.

   </details>

2. **A team deletes every test server on Friday but leaves a NAT gateway and an idle load balancer. Which charges appear for the weekend?**

   A. None, because no servers were running\
   B. Hourly charges for the NAT gateway and the load balancer\
   C. Data transfer out for the traffic they would have carried\
   D. Request charges for each hour they existed

   <details><summary>Feedback</summary>

   **B is right.** A NAT gateway and a load balancer bill for every hour they exist, with or without traffic.

   - **A is wrong.** Deleting the servers ended only their own instance hours.
   - **C is wrong.** With no traffic, no data was sent out.
   - **D is wrong.** Request charges count calls, not hours.

   </details>

3. **Which statement describes the AWS Free Tier for an account opened today, as of 2026-10-24?**

   A. Twelve months of free usage on many services, then normal rates\
   B. Credits and a choice of plan; the Free plan ends after six months or when the credits run out\
   C. Unlimited free usage of every service on the Free plan\
   D. Credits that can buy Reserved Instances on the Free plan

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** That's the legacy Free Tier, for accounts created before 2025-07-15.
   - **C is wrong.** The Free plan offers selected services, and usage beyond the always-free allowances comes out of the credits.
   - **D is wrong.** Reserved Instances and Savings Plans aren't available on the Free plan.

   </details>

**Next:** [Purchasing options](02-purchasing-options.md), where the bakery cuts the steady part of its bill.

## Where to check the current details

- [AWS pricing](https://aws.amazon.com/pricing/) and each service's pricing page, such as [EC2 On-Demand](https://aws.amazon.com/ec2/pricing/on-demand/) (checked 2026-10-24)
- AWS's machine-readable [data transfer price list](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json) (published 2026-09-16)
- [AWS Free Tier](https://aws.amazon.com/free/) and [Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html) (checked 2026-10-24); your own account's **Credits** page for your dates

---

"How AWS charges" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
