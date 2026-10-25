---
type: lesson
id: clf-14-01
title: "Optional: The capstone review"
tasks: ["1.2", "4.1", "4.3"]
objectives: ["14.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 13; optional, beyond the exam; about 20 minutes to read and 90 minutes for the review; a laptop or desktop helps for the write-up"
prerequisites: [clf-14-00, clf-02-05, clf-11-01, clf-12-01]
terms_introduced: [workload inventory, review scope, review question, improvement plan, accepted risk, scoring rubric]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/appendix.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads.html"
  - "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/vpc/pricing/"
  - "https://aws.amazon.com/elasticloadbalancing/pricing/"
  - "https://aws.amazon.com/dynamodb/pricing/on-demand/"
  - "https://aws.amazon.com/premiumsupport/pricing/"
---

# A Well-Architected review asks each pillar's questions of a real workload, rates what it finds by the harm to the business, and prices every fix

This lesson is optional practice beyond the exam, which only asks you to recognize the pillars. A review isn't a pass-or-fail test: it's a short list of what could hurt the business most, what to do about it, and what that costs.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) and [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes to read, then about 90 minutes for your own review.

**Before you start:** you need the pillars from [lesson 02.05](../02-why-the-cloud/05-the-well-architected-framework.md), costing from [lesson 11.01](../11-paying-for-aws/01-how-aws-charges.md) and the Support plans from [lesson 12.01](../12-getting-help/01-support-plans.md). No AWS account is needed.

## Warm-up: what you remember

1. From Module 09: how far back does CloudTrail Event history go, and how do you keep records for longer?
2. From lesson 04.01: on an EC2 web server, who patches the operating system: AWS or the customer?

<details><summary>Feedback</summary>

1. **90 days.** A **trail** delivers events to an S3 bucket, kept as long as you like ([lesson 09.01](../09-protecting-and-governing/01-who-did-what.md)). The bakery has none.
2. **The customer** ([lesson 04.01](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md)). Nobody at the bakery owns that job yet.

</details>

## What you'll learn

By the end, you can assemble a pillar-by-pillar review of a workload and justify each fix you recommend (objective 14.01a).

Guess before you read on: does a Well-Architected review give the workload a score out of 100?

## The workload you're reviewing

Before December, the bakery's owner asks, "Is it built well?" You review what Labs 05 to 11 built, as one workload running all month in `us-east-1`. Each lab deleted what it built, so you work from this **workload inventory**: every part and how it's set up.

| Part | As built |
|---|---|
| Exports and tax archive buckets | S3, versioning on, with lifecycle rules: exports to Standard-IA, archives to Glacier Deep Archive, both deleted later |
| Cart table | DynamoDB, on-demand; point-in-time recovery off |
| Order function | Lambda; its role can only write logs; logs never expire |
| Web server | One `t3.micro`, chosen because it was free-tier eligible; public IPv4 address; encrypted 8 GiB gp3 disk; no key pair |
| Network | One VPC: a public subnet in `us-east-1a`, an empty private subnet in `us-east-1b` |
| Photo bucket | Built from a CloudFormation template: private, encrypted by default, tagged; no versioning, no lifecycle rule |
| Error alarm | Function errors email one address through SNS |
| Account | Root MFA; an IAM admin user with MFA; budgets and alarms; CloudTrail Event history only, no trail |

Everything but the photo bucket was built by hand. **Not there:** a load balancer, Auto Scaling, a second web server, backups, a trail. The RDS order database is outside the review: no lab built it.

## Steps 1 and 2: set the scope, then ask each pillar's question

Read the inventory for what's missing: missing parts are often the findings. Then write the **review scope**, what the review covers and leaves out. Ours: "The bakery's production account in `us-east-1`, as built in Labs 05 to 11. Out of scope: the RDS order database."

Each pillar has five to thirteen numbered **review questions**, such as REL 10, each with its own best practices ([Questions and best practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/appendix.html), checked 2026-10-24). A full review answers every question; start with one per pillar:

| Pillar | Starter question |
|---|---|
| Operational excellence | [OPS 8. How do you utilize workload observability in your organization?](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops-08.html) |
| Security | [SEC 4. How do you detect and investigate security events?](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-04.html) |
| Reliability | [REL 10. How do you use fault isolation to protect your workload?](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-10.html) |
| Performance efficiency | [PERF 2. How do you select and use compute resources in your workload?](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-02.html) |
| Cost optimization | [COST 7. How do you use pricing models to reduce cost?](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-07.html) |
| Sustainability | [SUS 2 How do you align cloud resources to your demand?](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-02.html) |

Note what the workload does well, not only what it lacks. And the answer to the prequestion is no: the Framework calls a review a conversation, not an audit, and its outcome is a set of actions, not a grade ([The review process](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html)). The Well-Architected Tool counts high and medium risks, but nobody passes or fails.

## Step 3: rate each finding by what it would do to the business

In the Well-Architected Tool, a high-risk issue might do a business significant harm, and a medium-risk issue less. Each best practice's page states the level if it's missing, but AWS calls these guidelines: your business's reasons can make a risk lower, if you write them down ([Workloads](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads.html), checked 2026-10-24). So start from the page's level, then ask: what happens to the bakery if this goes wrong, and would anyone notice? A finding that stops orders is high; one that loses a few shopping carts is medium.

> **Your turn:** Which is the better reason for rating "the cart table has no point-in-time recovery" as medium rather than high?
>
> A. DynamoDB copies data across three Availability Zones, so backups aren't needed\
> B. Losing carts annoys some customers, but orders and payments live elsewhere\
> C. Backups are expensive

<details><summary>Feedback</summary>

**B is right.** It rates the finding by its harm to the business.

- **A is wrong.** Copies in three AZs protect against a failed AZ, not against a bad write or a deletion, which reaches every copy.
- **C is wrong.** At the bakery's size it costs about 20 cents a month. Price is a reason for ordering fixes, not for rating risk.

</details>

## Step 4: price each fix with dated rates, and count people's time

Every charge is a quantity times a rate (lesson 11.01). Look first for the hourly lines, which bill all month with or without customers. Count the work too, and compare each cost with the harm it avoids.

| Item | Rate, US East (N. Virginia) |
|---|---|
| `t3.micro` instance, On-Demand | $0.0104 an hour |
| Public IPv4 address, also a load balancer's | $0.005 an hour |
| EBS gp3 disk | $0.08 per GB-month |
| Application Load Balancer | $0.0225 an hour, plus $0.008 per capacity unit-hour |
| DynamoDB point-in-time recovery | $0.20 per GB-month |

> **Dated (checked 2026-10-24):** from AWS's Price List files and the US East example on [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/on-demand/). Check the [EC2](https://aws.amazon.com/ec2/pricing/on-demand/), [VPC](https://aws.amazon.com/vpc/pricing/) and [load balancer](https://aws.amazon.com/elasticloadbalancing/pricing/) pages before you quote a figure.

As built, the workload costs about $13.19 a month: $11.88 for the web server and $1.31 for storage and requests, on made-up usage.

**Example:** the reliability pillar. Under REL 10, most of the workload already survives an Availability Zone failure: Lambda, DynamoDB and S3 are Regional services spread across AZs. The part that doesn't is the one every order passes through, a single web server in `us-east-1a`. If it fails, someone rebuilds it by hand, maybe over a December weekend. **High risk.** The options:

![Horizontal bars of the web tier's monthly cost. A, leave it as built, one server: $11.88. B, a self-healing single server in an Auto Scaling group of one: $11.88. C, outlined as the choice, two servers in two AZs behind a load balancer: $23.76 of servers plus $24.90 of load balancer, $48.66.](../../images/14-01-web-tier-options.svg)

*Notice that option B costs nothing extra but still leaves gaps, and that most of option C's extra cost is hourly: the load balancer and its addresses bill whether or not anyone orders.*

**Long description.** Three bars, dollars per month, On-Demand, US East (N. Virginia), price lists retrieved 2026-10-24, 730 hours. A, as built: one `t3.micro` with its public IPv4 address and 8 GiB gp3 disk, $11.88; down until someone rebuilds it. B, the same server in an Auto Scaling group of one, at no extra charge, $11.88; a replacement in minutes, but with a new public address customers can't find until the site's address is updated. C, outlined: two servers, $23.76, plus an Application Load Balancer, $24.90 (hours $16.43, two public IPv4 addresses $7.30, an assumed 0.2 capacity units $1.17), $48.66; stays up, because the load balancer stops sending orders to a failed server and Auto Scaling replaces it. C adds $36.78 a month.

Say online orders bring in $150 an hour on a December Saturday (made up): three hours of outage cost about a year of the fix, $441. C also needs a second public subnet, because an Application Load Balancer needs subnets in at least two Availability Zones ([Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)). Two servers all night use more energy than one; write that trade-off down for the sustainability finding.

## Steps 5 and 6: recommend a Support plan, and write one page

Start at Basic Support and move up only for a reason the review gives you (lesson 12.01). After the fixes the bill is about $50 a month. Business Support+ costs the greater of $29 or a share of the account's charges, 9% of the first $10,000, so here the fee is **$29 a month**, and once you sign up you pay for at least 30 days ([AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/), as of 2026-10-24). That buys technical cases 24/7 and all Trusted Advisor checks; Basic can't open technical cases, and Enterprise Support's $5,000 minimum is about 99 times the bill. Basic now, with the gap written down as an **accepted risk** (a risk the business decides not to fix, with the reason and who decided), is defensible; so is Business Support+ with a reason.

Then write the **improvement plan**, the list of risks you decided to fix, in order, each with its fix, cost and owner. Give the owner one page: the scope; a summary of the high risks and the change in the bill; the findings, high risks first (among equal risks, quick and cheap fixes first); the Support plan; accepted risks, with who decided; and the next review date.

## The scoring rubric

A **scoring rubric** describes weak, good and strong work for each part of a task. Score each row **1**, **2** or **3**, and **0** if it's missing. You've met the capstone when every row scores at least 2.

| Criterion | 1: Developing | 2: Proficient | 3: Strong |
|---|---|---|---|
| Operational excellence | Mentions monitoring | Nothing watches the web server | Also the hand-built parts |
| Security | Names a service | The 90-day limit of Event history; a trail | Also an owner for patching |
| Reliability | Names one AZ as a problem | The single web server, rated high, options priced | Also backups of carts and photos |
| Performance efficiency | Says "make it faster" | Size chosen by label, not data | Also why there's no high risk here |
| Cost optimization | Says "buy Reserved Instances" | Fixes log retention; commits only after the redesign | Also prices the commitment |
| Sustainability | Says "use less" | Always-on servers for a demand that drops at night, with a fix | Also weighs it against reliability |
| Ratings and costs | Ratings without reasons | A reason for every rating; every fix priced, with hours of work | Also the largest cost against the harm avoided |
| Support plan | Names a plan | The cheapest plan that fits, fee worked out | Also why not the others |
| Write-up | Unordered notes | One page, high risks first | Also an owner per fix, and a next-review date |

## Your review, then the model answer

Do the whole review now for all six pillars, taking the example as given. Write yours before opening the model: reading the answer first feels quicker but teaches much less.

<details><summary>Model answer</summary>

**Summary:** three high-risk issues: one web server in one AZ; nobody told if it stops; only 90 days of who-did-what. The fixes take the bill from about $13.19 to $50.36 a month.

**Strengths to keep:** private, encrypted buckets; lifecycle rules on exports and archives; a function role that can only write logs; Regional services spread across AZs; budgets.

| # | Pillar | Finding | Risk | Fix | Per month | Work |
|---|---|---|---|---|---|---|
| 1 | Reliability | Only web server in one AZ; nothing replaces it | High | Two servers in two AZs, Auto Scaling, load balancer | +$36.78 | 1 day |
| 2 | Operational excellence | Nothing watches the web tier | High | Alarm when healthy servers drop below 2; a second email address | $0 | 1 hour |
| 3 | Security | Only 90 days of Event history | High | A multi-Region trail to a private bucket, logs deleted after a year | About $0.14 after a year | 1 hour |
| 4 | Reliability | Cart table has no point-in-time recovery; photo bucket has no versioning | Medium | Turn on recovery; add versioning and a 30-day rule for old versions | +$0.25 | 1 hour |
| 5 | Operational excellence | Everything but the photo bucket was built by hand | Medium | Templates for the network, web tier, function and alarms | $0 | 1 to 2 days |
| 6 | Security | Nobody owns patching the web servers | Medium | Monthly: newest image in the launch template; replace the servers | $0 | 1 hour a month |
| 7 | Cost optimization | The function's logs never expire, and the photo bucket has no lifecycle rule | Medium | 30-day log retention; fix 4's rule for old photo versions | $0 | 5 minutes |
| 8 | Performance efficiency | `t3.micro` chosen as free-tier eligible, not from data | Medium | After the redesign, read a month of metrics in Compute Optimizer | $0 | 1 hour |

**Later,** after a month of data: test Graviton-based `t4g.micro` instances (sustainability), then commit the floor of two servers for a year (cost). A Standard Reserved Instance is tied to its instance family, so commit after the test (lesson 11.02).

**Support plan:** Basic, recorded as an accepted risk; move to Business Support+ once the site carries much of the bakery's revenue.

**Accepted risks:** a Region-wide outage stops the site (a second Region is out of proportion at this size). **Next review:** before next December, or sooner if the site adds payments.

Findings 4 and 6 are rated below their best practices' high level: carts are low-value, and after fix 1 only the load balancer reaches the servers. Your review can differ and still score 2 or 3, as long as each rating has a reason and each fix a price.

</details>

## Summary

- **Start from the inventory:** read it for what's missing, and write down what's out of scope.
- **Ask each pillar's own question,** such as REL 10, and record strengths as well as gaps.
- **Rate by harm to the business,** starting from the best practice's level, with a reason for every rating.
- **Price every fix** against the harm avoided, and recommend the cheapest Support plan that fits or record an accepted risk.
- **Write one page,** high risks first, and review again when the workload changes.

## Practice

1. **What does a Well-Architected review produce?**

   A. A pass or fail result from AWS\
   B. A list of risks, ordered by business impact, with actions to fix them\
   C. A certificate that the workload is well-architected

   <details><summary>Feedback</summary>

   **B is right.** The Framework calls the outcome a set of actions to improve the workload.

   - **A is wrong.** It's a conversation, not an audit, and nobody passes or fails.
   - **C is wrong.** No such certificate comes from a review.

   </details>

2. **An internal reporting tool, used weekly by two people, runs on one instance in one AZ. Is that a high-risk issue, as it was for the bakery's web server? Explain in two sentences.**

   <details><summary>Feedback</summary>

   **Probably not.** The same gap does less harm: if the tool is down for a few hours, two people wait and no money is lost. It could be medium, or an accepted risk with the reason written down.

   </details>

3. **(From Module 03.) The fixed bakery runs in two Availability Zones. Which event does that still not protect against: a failed server, a failed Availability Zone, or a Region-wide outage?**

   <details><summary>Feedback</summary>

   **A Region-wide outage.** Two AZs give high availability within the Region; surviving a Region's loss needs disaster recovery in a second one (lesson 03.03).

   </details>

**Next:** [Optional lab 18: record the bakery's review in the AWS Well-Architected Tool](02-lab-18-well-architected-tool-review.md), then [Lab 19: close out the account you used for the course](03-lab-19-close-out.md).

## Where to check the current details

- [The review process](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html) and [Questions and best practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/appendix.html), AWS Well-Architected Framework (checked 2026-10-24)
- [Workloads](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads.html), AWS Well-Architected Tool User Guide (checked 2026-10-24)
- [AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/) (checked 2026-10-24)

---

"Optional: The capstone review" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
