---
type: lab
id: clf-11-05
title: "Lab 15: Price the bakery's setup in the AWS Pricing Calculator"
tasks: ["4.1", "4.2", "1.4"]
objectives: ["11.03a", "11.02a", "11.01a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 06.01 and 06.02; about 45 minutes; a laptop or desktop with a web browser"
prerequisites: ["clf-06-01", "clf-06-07"]
terms_introduced: [hourly item, estimate link]
pillars: [cost-optimization]
lab: "15"
rung: L1-L3
mode: real
free_plan: "not needed"
signup_path: none
time: "45 minutes"
cost: "$0: a free web tool, and no AWS account is used (as of 2026-10-24)"
worst_case: "$0. Nothing is created in AWS. The estimate link you share stays readable by anyone who has it for one year, so keep personal details out of the estimate"
needs: []
last_run_pass: "2026-10-25, standalone Free plan account, advanced sign-up, us-east-1"
recorded: 2026-10-25
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"
  - "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/vpc/pricing/"
  - "https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
---

# Lab 15: Price the bakery's setup in the AWS Pricing Calculator, then cut what it doesn't need

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) and [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2).

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [06.01 Amazon EC2](../06-running-applications/01-ec2.md) and [06.02 Auto Scaling and load balancers](../06-running-applications/02-auto-scaling-and-load-balancers.md); lessons [11.02](02-purchasing-options.md) and [11.03](03-estimate-watch-analyze.md) help. **Time:** about 45 minutes.

**Goal:** you price the bakery's web tier, find the lines that charge by the hour, trim a test copy for a new cake designer feature, compare ways to pay for the web servers, and share the estimate. **End state:** your lab log holds the estimate, the test copy, a table of purchasing options and a working link.

**What it creates:** nothing in AWS. The public **AWS Pricing Calculator** website needs no AWS account ([What is AWS Pricing Calculator?](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)).

**What it costs:** $0. **Worst case:** still $0. Watch privacy instead: anyone with a shared estimate's link can open it, so never put names, addresses or account IDs in it.

**Before you start:** no guardrails are needed, because you don't sign in to AWS. You need a browser and your lab log ([primer page 07](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md)).

> **New sign-up path:** AWS lists the Pricing Calculator as not supported in that experience (as of 2026-10-23). We read that as the version inside the console; the public website needs no account, so it should work the same for you.

**About the screens:** labels in **bold** and the figures quoted are what we saw when we ran this lab end to end on 2026-10-25. The calculator changes often; if a label differs, look for the option with the same meaning.

> **Dated (checked 2026-10-24):** the prices in this lab are On-Demand, Linux, US East (N. Virginia), from AWS's Price List files: `t3.small` $0.0208 an hour; Application Load Balancer $0.0225 an hour plus capacity units; public IPv4 address $0.005 an hour; gp3 disk $0.08 per GB-month; S3 Standard $0.023 per GB-month. The calculator counts 730 hours in a month. Your calculator shows today's prices; trust it over this box.

## Steps

### Get ready

1. In your lab log, write today's date, `Lab 15`, and this table. You'll fill in the last column. The settings are round numbers for practice.

   | Line | Service to search for | Settings | Monthly cost |
   |---|---|---|---|
   | Web servers | Amazon EC2 | 2 × `t3.small`, Linux, shared tenancy, always on, On-Demand, 20 GB gp3 disk each | |
   | Load balancer | Elastic Load Balancing | 1 Application Load Balancer, very little traffic | |
   | Public addresses | Amazon VPC | 2 public IPv4 addresses, in use all month | |
   | Cake photos | Amazon S3 | 50 GB in S3 Standard | |

2. Open `https://calculator.aws/` in your browser. Don't sign in to anything.
   **You should see:** a page with a **Create estimate** button.

### Part 1: price the live web tier

3. Choose **Create estimate**.
   **You should see:** the **Add service** page, with a search box.
4. Search for `Amazon EC2` and choose **Configure** on its card.
5. In **Description**, type `Bakery live - web servers`. Keep the location type **Region** and choose **US East (N. Virginia)**. Check it: our calculator started on US East (Ohio).
6. In the instance section, keep the tenancy as shared and the operating system as Linux. Choose the workload for constant usage, and set the number of instances to `2`. Search for `t3.small` and select it.
7. Under **Payment options**, choose **On-Demand**. The page starts on **Compute Savings Plans** with a 3-year term (as of 2026-10-25), which would make your figure far lower than this lab's. Keep **Expected utilization** at `100` percent, **Utilization percent per month**.
8. Open the collapsed **Amazon Elastic Block Store (EBS) - optional** section, keep **General Purpose SSD (gp3)**, and type `20` in **Storage amount** (GB). Leave snapshots, monitoring and data transfer empty or at zero.
   **You should see:** a monthly cost near $33.57 (two servers at $15.18, two disks at $1.60). **Show calculations** opens the working behind the figure; the calculator counts 730 hours a month.
   > **If something went wrong:** a much larger figure usually means a different Region, Windows, or a larger instance type. Check all three against step 6.
9. Choose **Save and add service**.
10. Search for `Elastic Load Balancing` and choose **Configure**. Choose the Application Load Balancer, the same Region, and `1` load balancer. Where it asks about traffic, under processed bytes for EC2 instances, change the unit from **GB per hour** to **GB per month** and enter `1`. Save the service.
    **You should see:** about $16.43 for the hours, plus a little for **capacity units** (load balancer capacity units, which grow with traffic).
11. Search for `Amazon VPC` and choose **Configure**. Its features are checkboxes: tick **Public IPv4 Address** (leave **NAT Gateway** cleared; **VPN Connection** was ticked by default for us and adds nothing while its numbers are zero), enter `2` in **Number of In-use public IPv4 addresses**, and save.
    **You should see:** $7.30 (2 × $0.005 × 730).
    > **If something went wrong:** if your calculator has no public IPv4 section, cancel this service and write $7.30 in your log by hand. AWS bills public IPv4 addresses by the hour either way ([Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)).
12. Search for `Amazon S3` and choose **Configure**. In S3 Standard, enter `50` GB of storage, leave requests at zero, and save.
    **You should see:** about $1.15.
13. Open the summary (the **My Estimate** page). Write each line's monthly cost in your log.
    **You should see:** four or five lines and a monthly total near $58.

### Part 2: find the hourly items, and trim the test copy

An **hourly item** is a line made of a time-based charge ([lesson 11.01](01-how-aws-charges.md)): it bills for every hour the resource exists, whether it does any work or not.

14. Next to each line in your log, write **H** if it bills by the hour, **S** if it bills for a size you set, or **U** if it bills only for what you use.

> **Your turn:** which lines are hourly, and what share of the total are they? What would make the photo line grow?

<details><summary>Model answer</summary>

**H:** the servers ($30.37), the load balancer ($16.43) and the public addresses ($7.30): $54.10 of about $58.45, about 93%. **S:** the disks, which bill for 20 GB whether they hold 1 GB or 20. **U:** the photos, which grow only when the bakery stores more.

</details>

15. The owner's nephew wants a test copy of the site for the cake designer. His draft copies Part 1 without the photos: two servers, a load balancer and two public addresses, all month. Add up his draft's monthly cost from your log, without building it.
16. Testing happens only in working hours, about 40 of the week's 168 hours, and one tester at a time. Decide which of the draft's hourly items the test copy can drop.
17. Add a new **Amazon EC2** service with the description `Test copy - cake designer`, the same Region, `1` × `t3.small`, On-Demand, and a 20 GB gp3 disk. In the utilization or usage field, enter about `24` percent (40 ÷ 168), or 40 hours a week if it asks for hours. Save it.
    **You should see:** about $3.62 for the server, but only about $0.38 for the disk, $4.00 in all. The calculator explains why in a note under the usage field: for usage below 100%, it "assumes that the attached EBS volume is deleted while the instance is not running". Your plan only stops the server, and a disk is billed for as long as it exists, so the real cost of this line is $3.62 + $1.60 = $5.22. Write both figures in your log.
    > **If something went wrong:** if you find no utilization or hours field, look for a workload option based on a usage pattern, such as a daily spike, and choose one that runs about 8 hours a day.

> **Your turn:** what did you remove, and why can't fewer hours shrink the disk's cost?

<details><summary>Model answer</summary>

The draft costs $57.30 a month; the trimmed copy $5.22. Remove the **load balancer** (one server has nothing to balance) and the **second server** and its address (one tester needs one), and run the remaining server **only in working hours**. Most of the saving comes from removing whole hourly items. The **disk** bills for its size for as long as it exists, even while the server is stopped (lesson 06.01), which is why the calculator's $4.00 understates this plan.

</details>

### Part 3 (challenge): compare ways to pay for the web servers

18. The two live web servers run all year. On the **My Estimate** page, choose the **Edit** icon next to `Bakery live - web servers`. Try each payment option the calculator offers, choosing a **1-year** term and **no upfront** payment wherever it asks: On-Demand, Compute Savings Plans, EC2 Instance Savings Plans, Standard Reserved Instances, and Spot. Reserved Instances are in a collapsed section, **Other purchasing options**, which also offers Convertible Reserved Instances. The total includes the two disks ($3.20); subtract them to compare the servers. For each, write the monthly cost and any upfront cost. Then set the line back to the option you would choose, and save.

> **Your turn:** fill in a table like this, choose an option for the two always-on servers, and say which you would refuse.

<details><summary>Model answer</summary>

| Option, 1 year, no upfront | Monthly, 2 × `t3.small` | Commitment |
|---|---|---|
| On-Demand | $30.37 | None |
| Standard Reserved Instances | $18.98 ($0.013 an hour each) | This instance type |
| Convertible Reserved Instances | $21.90 | Exchangeable for other types |
| EC2 Instance Savings Plans | $18.98 | Dollars per hour, one family, one Region |
| Compute Savings Plans | $21.90 | Dollars per hour, any EC2, Lambda or Fargate |
| Spot | $11.54 (the calculator's 62% average discount) | None, but interruptible with two minutes' warning |

On-Demand and Reserved prices: AWS Price List, US East (N. Virginia), as of 2026-10-24. The other figures are the calculator's on 2026-10-25; yours may differ.

**A good choice:** a 1-year **Savings Plan** sized to the two servers, which run every hour. **Compute** keeps working if the bakery moves to another family or onto Lambda; **EC2 Instance** or a **Reserved Instance** can save more but ties you to `t3` in one Region. **Refuse Spot:** these servers are the site's only floor, and losing both with two minutes' warning would take orders offline.

</details>

> **Note:** the Free plan leaves out Savings Plans and Reserved Instances ([Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), checked 2026-10-24), so you compare them here, on paper.

### Part 4: share the estimate

19. On the **My Estimate** page, check that no description contains a name, an address or an account ID. Then choose **Share**.
20. Read the **Public server acknowledgment** and choose **Agree and continue**. Then choose **Copy public link**.
    **You should see:** a link copied to your clipboard. This **estimate link** is the public address that reopens the saved estimate. Paste it into your lab log, with one line saying what the estimate shows.
21. Open the link in a private browser window.
    **You should see:** the same estimate, with all its lines.
    > **If something went wrong:** an older version of the estimate means you changed something after sharing. The calculator never updates a saved link; choose **Share** again for a new one ([Sharing your estimate](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html)).

Estimate links made since 2023-05-31 stay valid for one year (checked 2026-10-24).

## Check your work

- [ ] Your lab log lists four lines of the live web tier, each marked H, S or U, with a total near $58.
- [ ] The test copy line is near $5, and you can say why the load balancer went.
- [ ] Your table compares at least four payment options, with one choice and your reasons.
- [ ] Your estimate link opens in a private window.

## Clean up

22. Nothing was created in AWS, so there is nothing to delete. Close the calculator tab.
23. **Confirm:** you never signed in to AWS during this lab. The shared link stays readable for a year; AWS's guide describes no way to withdraw it, which is why step 19 checked it for personal details.

## Recap

You priced a setup before building it, saw that hourly items make up almost all of its bill, cut a test copy by removing them, and compared paying by the hour with committing for a year.

> **Reflect:** the owner asks, "Is $58 a month what we'll pay?" Write two sentences on what your estimate leaves out and how you would check it once the site runs.
>
> <details><summary>Model answer</summary>
>
> No: it leaves out data transfer to customers, requests, the database, tax and price changes. Once the site runs, compare it with Cost Explorer monthly, and set a budget a little above it.
>
> </details>

**Next:** [Many accounts, one bill](04-many-accounts-one-bill.md).

## Where to check the current details

- [What is AWS Pricing Calculator?](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) (checked 2026-10-24)
- [Sharing your estimate](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html) (checked 2026-10-24)
- [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) (prices as of 2026-10-24)

---

"Lab 15: Price the bakery's setup in the AWS Pricing Calculator" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
