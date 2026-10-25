---
type: check
id: clf-11-09
title: "Module 11 mastery check"
tasks: ["4.1", "4.2", "1.4"]
objectives: ["11.01a", "11.02a", "11.03a", "11.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished lessons 11.01 to 11.04; about 25 minutes for each check"
prerequisites: [clf-11-01, clf-11-02, clf-11-03, clf-11-04]
pillars: [cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html"
  - "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html"
  - "https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html"
---

# Module 11 mastery check: explain a bill, choose how to pay, pick the cost tool, and trace who gets a discount

Twelve questions test whether you can say what drives a bill, choose a purchasing option for a usage pattern, pick the cost tool for each stage, and trace discounts and tags through an organization. A second set of twelve, on the same objectives, is there if you need a retest.

**For:** an adult studying alone, possibly new to IT, who has finished lessons [11.01](01-how-aws-charges.md), [11.02](02-purchasing-options.md), [11.03](03-estimate-watch-analyze.md) and [11.04](04-many-accounts-one-bill.md). **Time:** about 25 minutes for each check. No AWS account is needed.

## How to use this check

Take Check A closed-book, in one sitting, and write down your answers before you open any feedback. The threshold is 80%: 10 of the 12 questions. A "(Select TWO.)" question counts only if both of your choices are right. If you score below 10, use the correction map to reread the section behind each miss and redo its lab or simulation, then take Check B, the parallel retest. If you score 10 or more, go on to the enrichment tasks.

No question needs a price, a percentage or a count. Free Tier terms and service names are as of 2026-10-24; where the exam guide uses an older name, the options use the exam's name and the feedback gives today's.

## Check A

**A1.** A language school's AWS bill for August, when the school is closed and its website gets almost no visitors, is nearly the same as for a busy month. Its setup: EC2 web servers that run all the time, an Application Load Balancer, an RDS database, an S3 bucket of course videos, and Lambda functions triggered when students upload work. Which charges explain why August's bill didn't fall?

- A. The hourly charges for the servers, load balancer and database
- B. The GET request charges for the course videos in S3
- C. The request and run-time charges for the Lambda functions
- D. The charges for data sent out to the internet

<details><summary>Answer</summary>

**A is right.** EC2 instances, a load balancer and an RDS database bill for every hour they exist, busy or idle. That idle cost doesn't fall when visitors stop.

- **B is wrong.** Request charges bill only when someone uses the resource. With almost no visitors, there are almost no GET requests.
- **C is wrong.** A Lambda function that isn't triggered doesn't run and isn't charged.
- **D is wrong.** Data out to the internet follows visitors too: no visitors, little data sent.

</details>

**A2.** A team says, "Our data never leaves AWS, so we pay nothing for data transfer." Its application runs in one Region and has these flows. Which two add a data transfer charge? (Select TWO.)

- A. Users upload photos from their browsers to the web servers
- B. Web servers in two Availability Zones exchange session data with each other
- C. The web servers read and write objects in an S3 bucket in the same Region
- D. Each night, backups are copied to a bucket in a second Region
- E. Objects are served from the S3 bucket to Amazon CloudFront

<details><summary>Answer</summary>

**B and D are right.** Data that crosses Availability Zones is charged per GB, in each direction, and data copied to another Region is charged per GB, even though neither flow leaves AWS. "In is free, out is charged" is only half the rule.

- **A is wrong.** Data in from the internet is free.
- **C is wrong.** EC2 to S3 in the same Region has no transfer charge. (A NAT gateway in the path would add its own processing fee, but none is described.)
- **E is wrong.** S3 to CloudFront is free; CloudFront then charges for what it delivers to viewers.

</details>

**A3.** A learner has had her account on the Free plan for two months. A friend suggests, "Upgrade to the Paid plan to try a few more services, then switch back to the Free plan when the course ends." As of 2026-10-24, what is the problem with that plan?

- A. Upgrading is one way, and usage beyond her credits will then be billed
- B. Upgrading uses up her remaining credits, so everything is billed from that day
- C. The Paid plan offers the same services as the Free plan, so it gains her nothing
- D. She can't upgrade until her twelve free months have ended, so it's blocked

<details><summary>Answer</summary>

**A is right.** A Free plan account can move to the Paid plan, but never back to the Free plan. On the Paid plan, usage beyond the credits is billed at normal rates, and the account doesn't close when the credits run out.

- **B is wrong.** Remaining credits carry on and apply to later bills after an upgrade.
- **C is wrong.** The Free plan offers selected services; the Paid plan gives access to all of them, plus short-term trials.
- **D is wrong.** "Twelve free months" describes the legacy Free Tier, for accounts created before 15 July 2025. Today's accounts get credits and a choice of plan, and can upgrade at any time.

</details>

**A4.** A company will buy a one-year commitment for its steady EC2 fleet in one Region. Its engineers right-size the fleet every few months, and the right size sometimes means a different instance family. It doesn't need any capacity guarantee. Which commitment keeps its discount through those changes?

- A. An EC2 Instance Savings Plan for the fleet's current family
- B. Standard Regional Reserved Instances for the current instance type
- C. A Compute Savings Plan for the fleet's hourly spend
- D. Spot Instances for the whole fleet

<details><summary>Answer</summary>

**C is right.** A Compute Savings Plan commits to dollars per hour and applies to EC2 in any family, size, Region, operating system or tenancy, so a change of family keeps the discount.

- **A is wrong.** An EC2 Instance Savings Plan covers one family in one Region. It gives a deeper maximum discount, but a move to another family leaves the new instances uncovered.
- **B is wrong.** A Regional Reserved Instance is flexible on size within its family (for Linux on shared tenancy), not across families.
- **D is wrong.** Spot isn't a commitment and can be interrupted; a steady fleet that mustn't stop isn't Spot work.

</details>

**A5.** Two teams each want three-year Reserved Instances. Team 1 is sure its instance family won't change, and if a project ends early it wants to be able to sell unused reservations. Team 2 expects to move to a newer instance family halfway through the term. Which pairing fits?

- A. Convertible for Team 1, and Standard for Team 2
- B. Standard for Team 1, and Convertible for Team 2
- C. Standard for both teams
- D. Convertible for both teams

<details><summary>Answer</summary>

**B is right.** Standard Reserved Instances give the larger discount and can be sold on the Reserved Instance Marketplace, which suits a team that won't change. Convertible Reserved Instances give less discount but can be exchanged for another Convertible Reserved Instance of a different family, which suits Team 2.

- **A is wrong.** It's the wrong way around: a Convertible can't be sold, and a Standard can't be exchanged for another family.
- **C is wrong.** Team 2 couldn't move its Standard reservations to the new family.
- **D is wrong.** Team 1 would give up discount it doesn't need to, and lose the right to sell.

</details>

**A6.** A health records company has a rule that its instances must never run on hardware shared with other AWS customers. Its software has no per-socket or per-core licensing. It also wants capacity held for these instances in one Availability Zone, and the simplest option that meets the rule. Which should it use?

- A. Dedicated Hosts
- B. Dedicated Instances, with a Capacity Reservation
- C. Zonal Reserved Instances on shared hardware
- D. Spot Instances

<details><summary>Answer</summary>

**B is right.** Dedicated Instances run on hardware that no other customer uses, without you managing a physical server, and they support Capacity Reservations.

- **A is wrong.** Dedicated Hosts also meet the rule, but they're for licenses counted per socket or core, where you need to see and control the server. They're more to manage, and they don't support Capacity Reservations.
- **C is wrong.** A zonal Reserved Instance holds capacity, but on shared hardware it breaks the rule.
- **D is wrong.** Spot can be interrupted and guarantees no capacity, and it doesn't make the hardware dedicated.

</details>

**A7.** A ticketing company has three workloads. A payment service has run on six instances every hour for two years and will keep running. A nightly report generator saves its progress and can restart from there. A one-week sale next month needs extra instances that are certain to launch in one Availability Zone. Which two pairings of workload and purchasing option fit? (Select TWO.)

- A. Payment service: a Savings Plan covering its six instances' hourly use
- B. Report generator: Spot Instances
- C. Sale week: Spot Instances, for the lowest price
- D. Payment service: Spot Instances
- E. Sale week: a one-year Compute Savings Plan

<details><summary>Answer</summary>

**A and B are right.** Steady, proven use is what a commitment fits, so commit to the baseline of six. Work that can stop and restart is what Spot is priced for.

- **C is wrong.** Spot guarantees nothing: capacity may not be there, and it can be taken back. The sale week needs a Capacity Reservation, which holds capacity in one Availability Zone at the On-Demand rate and gives no discount on its own.
- **D is wrong.** A payment service mustn't be interrupted with a two-minute warning.
- **E is wrong.** A Savings Plan lowers the price but holds no capacity, and a year of commitment for one week's use would sit idle for the rest of the year.

</details>

**A8.** A charity must show its board the monthly cost of two designs for a new donation website, side by side, before it builds either one: one design uses EC2 servers behind a load balancer, the other uses Lambda functions. Which tool should it use?

- A. AWS Cost Explorer
- B. A forecasted-cost alert in AWS Budgets
- C. AWS Pricing Calculator
- D. AWS TCO Calculator

<details><summary>Answer</summary>

**C is right.** AWS Pricing Calculator estimates designs that don't exist yet, from your assumptions, and its groups price two designs side by side. The estimate is only as good as the guesses about hours, requests and data.

- **A is wrong.** Cost Explorer analyzes and forecasts from usage you already have. There's no usage yet.
- **B is wrong.** A forecasted alert predicts real spending against a budget; it can't price a design.
- **D is wrong.** The TCO Calculator is gone; its address now leads to the Pricing Calculator.

</details>

**A9.** A university gives each student a sandbox AWS account with a monthly budget. The instructor wants new instance launches blocked automatically in a student's account once its actual cost reaches the budget, without deleting anything. Which setup does this?

- A. The budget's alert on its own, because AWS stops spending at the budget amount
- B. A budget action that applies an IAM policy denying new launches
- C. A Cost Anomaly Detection monitor set to stop launches
- D. A Cost Explorer forecast for each student's account

<details><summary>Answer</summary>

**B is right.** A budget action can apply an IAM policy (or, from a management account, an SCP) when a threshold is crossed, automatically or after approval. It blocks new launches; instances already running keep running and billing, and nothing is deleted.

- **A is wrong.** A budget on its own only sends alerts. It doesn't cap spending; resources keep billing.
- **C is wrong.** Cost Anomaly Detection alerts on unusual spending; it never stops or blocks anything.
- **D is wrong.** A forecast shows where spending is heading; it takes no action.

</details>

**A10.** A finance manager asks, "Which three services grew most since last quarter, and roughly what will we spend over the coming months?" She wants charts she can filter and group in a few clicks, with no files or data sources to set up. Which tool fits?

- A. AWS Budgets
- B. AWS Cost and Usage Report
- C. Amazon Quick Sight
- D. AWS Cost Explorer

<details><summary>Answer</summary>

**D is right.** Cost Explorer shows past cost and usage as charts you filter and group, by service, account, Region, tag and more, and it forecasts spending from your history.

- **A is wrong.** Budgets compares cost with a limit you set and alerts you when it's crossed; it isn't for finding which services grew.
- **B is wrong.** The Cost and Usage Report, created today as a CUR 2.0 export in AWS Data Exports, delivers every line item as files to an S3 bucket. It's for querying your own way, not for a few clicks.
- **C is wrong.** Quick Sight can chart billing data, but only once you've set up a data source, such as CUR files queried through Athena. That's the setup she wants to avoid.

</details>

**A11.** In one organization, discount sharing is on for every account. This hour, the `mobile` account owns two Regional Reserved Instances for `c7g.large` Linux in one Region, but runs only one matching instance. The `web` account runs two matching instances in the same Region. How is this hour billed?

- A. Both of `web`'s instances are covered first, because `web` uses more; `mobile`'s instance pays On-Demand
- B. Only `mobile`'s instance is covered; the second reservation goes unused because `mobile` bought it
- C. `mobile`'s instance and one of `web`'s are covered; `web`'s other instance pays On-Demand
- D. All three instances are covered, because the organization counts as one account

<details><summary>Answer</summary>

**C is right.** A Reserved Instance covers matching usage in the account that bought it first, then matching usage in other accounts where sharing is on. Two reservations cover two instances; the third instance pays On-Demand.

- **A is wrong.** The purchasing account always comes first.
- **B is wrong.** With sharing on, unused discount passes to matching usage elsewhere in the organization.
- **D is wrong.** The organization counts as one account for billing, but two reservations can't cover three instances.

</details>

**A12.** A company's resources have carried the user-defined tag key `costcenter` since March. On 1 June, the management account activates `costcenter` as a cost allocation tag. In July, finance opens Cost Explorer grouped by `costcenter`. Which two statements are accurate? (Select TWO.)

- A. Costs from March to May already carry the values, because the resources were tagged then
- B. Costs from shortly after 1 June onward carry the `costcenter` values
- C. Each member account must also activate `costcenter` before its own costs show it
- D. The key appears in reports as `aws:costcenter`, because the management account activated it
- E. Costs from March to May carry the values only if the management account requests a tag backfill

<details><summary>Answer</summary>

**B and E are right.** A tag reaches cost reports only after its key is activated, up to 24 hours later, and only for usage from then on. A tag backfill, requested by the management account, re-applies the activation to earlier months (up to twelve back), and it works here because the resources already carried the tag in March.

- **A is wrong.** Tagging alone shows no costs. Without a backfill, months before activation stay without a value.
- **C is wrong.** In an organization, only the management account activates cost allocation tags, once, for every account.
- **D is wrong.** User-defined tags appear with the prefix `user:`. The `aws:` prefix marks AWS-generated tags, such as `aws:createdBy`.

</details>

## Correction map

For each question you missed, reread the section, then redo the practice next to it before you take Check B.

| Question | Objective | Reread | Then practice |
|---|---|---|---|
| A1 | 11.01a | [Time-based charges run whether or not anyone uses the resource](01-how-aws-charges.md#time-based-charges-run-whether-or-not-anyone-uses-the-resource) | [Lab 15](05-lab-15-pricing-calculator.md), Part 2 (the hourly items) |
| A2 | 11.01a | [Data transfer is priced by direction: in is free, but out, across and between usually cost](01-how-aws-charges.md#data-transfer-is-priced-by-direction-in-is-free-but-out-across-and-between-usually-cost) | The lesson's practice question 1 and its cross-AZ "Your turn" |
| A3 | 11.01a | [The Free Tier now: two plans, credits and two clocks](01-how-aws-charges.md#the-free-tier-now-two-plans-credits-and-two-clocks) | The section's "Your turn"; [Simulation S14](08-sim-guardrail-timeline.md), Decision 4 |
| A4 | 11.02a | [Compute or EC2 Instance Savings Plan: flexibility or a deeper discount](02-purchasing-options.md#compute-or-ec2-instance-savings-plan-flexibility-or-a-deeper-discount) | [Simulation S13](07-sim-purchasing-option-tree.md), Decision 1 (workload A) |
| A5 | 11.02a | [Standard or Convertible](02-purchasing-options.md#standard-or-convertible) | [Simulation S13](07-sim-purchasing-option-tree.md), Decision 3 |
| A6 | 11.02a | [Dedicated Hosts and Dedicated Instances: hardware with no other customers](02-purchasing-options.md#dedicated-hosts-and-dedicated-instances-hardware-with-no-other-customers) | [Simulation S13](07-sim-purchasing-option-tree.md), Decision 1 (workload F) |
| A7 | 11.02a | [Choosing an option for a usage pattern](02-purchasing-options.md#choosing-an-option-for-a-usage-pattern), then [Capacity Reservations: a guarantee, not a discount](02-purchasing-options.md#capacity-reservations-a-guarantee-not-a-discount) | [Simulation S13](07-sim-purchasing-option-tree.md), Decisions 1 and 2 |
| A8 | 11.03a | [AWS Pricing Calculator estimates a design before it exists](03-estimate-watch-analyze.md#aws-pricing-calculator-estimates-a-design-before-it-exists) | [Lab 15: price the bakery's setup in the AWS Pricing Calculator](05-lab-15-pricing-calculator.md) |
| A9 | 11.03a | [AWS Budgets tells you when you pass a limit; it stops nothing unless you add an action](03-estimate-watch-analyze.md#aws-budgets-tells-you-when-you-pass-a-limit-it-stops-nothing-unless-you-add-an-action) | [Simulation S14](08-sim-guardrail-timeline.md), Decision 3 |
| A10 | 11.03a | [Pick the tool by the question it answers](03-estimate-watch-analyze.md#pick-the-tool-by-the-question-it-answers) | The lesson's worked example, "One forgotten instance in January" |
| A11 | 11.04a | [A commitment discount goes to its owner first, then to matching usage anywhere in the organization](04-many-accounts-one-bill.md#a-commitment-discount-goes-to-its-owner-first-then-to-matching-usage-anywhere-in-the-organization) | [Simulation S11](../09-protecting-and-governing/10-sim-organizations-and-scps.md), Part 3 |
| A12 | 11.04a | [A tag reaches your cost reports only after you activate it](04-many-accounts-one-bill.md#a-tag-reaches-your-cost-reports-only-after-you-activate-it) | [Lab 16: turn on cost allocation tags](06-lab-16-cost-allocation-tags.md) |

When you reread, use the method the lessons use instead of memorizing figures: sort a bill by its four meters; ask the purchasing questions in order (dedicated hardware, interruptible, guaranteed capacity, steady use); name the stage before the cost tool; and follow a discount or a tag step by step.

## Check B: parallel retest

Take this only after the correction map, and closed-book. The threshold is the same: 10 of 12.

**B1.** A small museum closes for a month of building work. Its website stays up with a "closed" page and gets almost no visitors. The site runs on two EC2 instances behind an Application Load Balancer, with a NAT gateway and an RDS database, and about 40 GB of photos in S3. Which change would cut the closed month's bill the most?

- A. Move the photos to a colder S3 storage class and delete old copies
- B. Cut the number of S3 GET requests the closed page makes
- C. Remove the NAT gateway and load balancer, and keep one small server
- D. Compress the page's images so less data goes out to the internet

<details><summary>Answer</summary>

**C is right.** The NAT gateway, the load balancer and each server bill for every hour they exist, with or without visitors. Removing whole hourly items is what cuts an idle month.

- **A is wrong.** Storage is a small line, and colder classes add retrieval fees and minimum storage durations; it barely touches an idle bill.
- **B is wrong.** With almost no visitors, request charges are already close to zero.
- **D is wrong.** Data out follows visitors, and there are almost none.

</details>

**B2.** A video company's design runs in one Region and has these data flows. Which two add a data transfer charge? (Select TWO.)

- A. Customers upload videos from their browsers to the company's servers
- B. Servers write each video's details to a DynamoDB table in the same Region
- C. Transcoding servers in one Availability Zone send finished files to servers in another Availability Zone
- D. Videos are served from an S3 bucket to Amazon CloudFront
- E. Viewers stream videos from the company's EC2 servers over the internet

<details><summary>Answer</summary>

**C and E are right.** Data that crosses Availability Zones is charged per GB, in each direction, even though it stays inside AWS, and data sent out to the internet is charged per GB.

- **A is wrong.** Data in from the internet is free.
- **B is wrong.** EC2 to DynamoDB in the same Region has no transfer charge, like EC2 to S3 or SQS.
- **D is wrong.** S3 to CloudFront is free; CloudFront then charges for what it delivers to viewers.

</details>

**B3.** A learner's account has been on the Free plan for four months, and she has used up all her credits. She hasn't changed anything. As of 2026-10-24, what happens?

- A. Her card is charged at normal rates for everything she uses from now on
- B. Her usage stays free until twelve months after sign-up, as before
- C. The plan ends and the account closes; upgrading in time restores access
- D. AWS adds fresh credits each month until the plan's time limit is reached

<details><summary>Answer</summary>

**C is right.** A Free plan account runs on two clocks, the calendar and the credit balance; whichever runs out first ends the plan, and the account closes. The Free plan never charges you. AWS keeps the content for a time, and upgrading in that time restores access.

- **A is wrong.** That's what happens on the Paid plan when credits run out; the Free plan never bills.
- **B is wrong.** "Twelve months free" describes the legacy Free Tier, for accounts created before 15 July 2025.
- **D is wrong.** Credits come at sign-up, plus a set amount earned through activities; they aren't topped up each month.

</details>

**B4.** A weather service will run its forecasting models on one compute-optimized instance family in one Region for the next three years. It will move between sizes as the models grow, but it never plans to leave that family or Region, and it uses no Lambda or Fargate. Finance wants the commitment with the deepest discount that still covers the size changes without any exchange or new purchase. Which should it buy?

- A. An EC2 Instance Savings Plan
- B. A Compute Savings Plan
- C. Zonal Standard Reserved Instances for the current size
- D. A Database Savings Plan

<details><summary>Answer</summary>

**A is right.** An EC2 Instance Savings Plan covers one family in one Region, in any size, operating system or tenancy, and gives a deeper maximum discount in return for staying put.

- **B is wrong.** A Compute Savings Plan would work, but its maximum discount is lower, and the service doesn't need its freedom to change family, Region or compute service.
- **C is wrong.** A zonal Reserved Instance applies only to exactly matching instances in one Availability Zone, with no size flexibility, so a resize loses the discount.
- **D is wrong.** A Database Savings Plan covers database services such as RDS and Aurora, not EC2 instances.

</details>

**B5.** A company bought three-year Convertible Reserved Instances. A year later, one project ends, and the company no longer needs that project's reservation for its current instances. What can it do with it?

- A. Sell it to another customer on the Reserved Instance Marketplace
- B. Cancel it and get a refund for the rest of its three-year term
- C. Ask AWS to convert it into a Compute Savings Plan of the same value
- D. Exchange it for another Convertible Reserved Instance of at least equal value

<details><summary>Answer</summary>

**D is right.** A Convertible Reserved Instance can be exchanged for another Convertible Reserved Instance with a different family, operating system or tenancy, of equal or higher value, in the same Region. That's the freedom it trades some discount for.

- **A is wrong.** Only Standard Reserved Instances can be sold on the Reserved Instance Marketplace.
- **B is wrong.** Reserved Instances can't be canceled; the commitment is paid for the whole term.
- **C is wrong.** The lessons describe no such conversion: a Reserved Instance stays a Reserved Instance until its term ends.

</details>

**B6.** A manufacturer is moving a design application to AWS. Its vendor licenses the software per physical core, audits which physical server it runs on, and requires the instances to stay on that same server after a stop and start. Which option fits?

- A. Dedicated Instances
- B. Dedicated Hosts
- C. An On-Demand Capacity Reservation
- D. Spot Instances

<details><summary>Answer</summary>

**B is right.** A Dedicated Host is a whole physical server for your use. You see its sockets, cores and host ID, and you keep instances on the host you choose, which per-core licenses and audits need.

- **A is wrong.** Dedicated Instances also run on hardware no other customer uses, but you see nothing of the server, and an instance may move to other hardware after a stop and start.
- **C is wrong.** A Capacity Reservation holds capacity in one Availability Zone; it doesn't make the hardware yours or show its cores.
- **D is wrong.** Spot runs on shared spare capacity and can be interrupted.

</details>

**B7.** A food delivery app has three workloads. A weekly pricing-model training job saves checkpoints and can be rerun from them. A product launch next month needs 20 extra instances that are certain to launch in one Availability Zone that morning. A three-day promotion adds a few instances, and it doesn't matter if launches are slow. Which two pairings of workload and purchasing option fit? (Select TWO.)

- A. Training job: Spot Instances
- B. Promotion: a one-year Savings Plan sized to the promotion's instances
- C. Product launch: Spot Instances
- D. Product launch: a Capacity Reservation, billed at the On-Demand rate
- E. Training job: three-year Standard Reserved Instances

<details><summary>Answer</summary>

**A and D are right.** Work that can stop and be rerun is what Spot is priced for. Only a Capacity Reservation guarantees capacity in one Availability Zone; it bills at the On-Demand rate, used or not, and gives no discount on its own.

- **B is wrong.** A commitment sized to three days of use would be paid for, idle, the rest of the year. Short, irregular use is On-Demand.
- **C is wrong.** Spot guarantees nothing: capacity may not be there, and it can be taken back.
- **E is wrong.** A weekly job doesn't run every hour, so most of a three-year commitment would go unused.

</details>

**B8.** A school district has designed a new online enrollment feature, but nothing is built yet. The council wants a monthly cost estimate for the design, based on the expected number of students and documents, before it approves the work. Which tool produces it?

- A. AWS Cost Anomaly Detection
- B. AWS Pricing Calculator
- C. AWS Trusted Advisor
- D. AWS Simple Monthly Calculator

<details><summary>Answer</summary>

**B is right.** AWS Pricing Calculator estimates the cost of a design from your assumptions, before anything exists. It leaves out tax, and it's only as good as the guesses you enter.

- **A is wrong.** Cost Anomaly Detection watches real spending for patterns that are unusual for you. A design that isn't built has no spending to watch.
- **C is wrong.** Trusted Advisor, which Module 12 covers, checks resources you already run, for example for idle ones that waste money. It doesn't price a design.
- **D is wrong.** The Simple Monthly Calculator is gone; its address now leads to the Pricing Calculator.

</details>

**B9.** A team wants the chosen EC2 instances in its test account to stop when actual cost crosses its monthly budget, but only after a team lead confirms. Which setup does this?

- A. A budget action that stops the chosen EC2 instances, set to wait for approval
- B. The budget on its own, because AWS stops resources when cost reaches the budget
- C. A Cost Anomaly Detection subscription that stops the instances
- D. A Cost Explorer report with a rule that stops the instances

<details><summary>Answer</summary>

**A is right.** A budget action can stop EC2 or RDS instances chosen when the action is set up, either automatically or after someone approves it. Anything it doesn't name, such as storage or a NAT gateway, keeps billing.

- **B is wrong.** A budget on its own only sends alerts; it never caps spending or stops resources.
- **C is wrong.** Cost Anomaly Detection only tells people; it never stops anything.
- **D is wrong.** Cost Explorer shows and forecasts costs; it can't act on resources.

</details>

**B10.** A retail group's analysts want to join its AWS costs with its sales data in Amazon Athena every day, at the finest detail AWS provides, including the ID of the resource behind each cost. Which should the group set up?

- A. A saved AWS Cost Explorer report
- B. An AWS Budgets report emailed each day
- C. A bill estimate in AWS Pricing Calculator
- D. An AWS Cost and Usage Report delivered to an S3 bucket

<details><summary>Answer</summary>

**D is right.** The Cost and Usage Report holds every line item, optionally with resource IDs and a column per activated tag, delivered as files to your S3 bucket, where Athena can query it. Today you create it as a CUR 2.0 export in AWS Data Exports.

- **A is wrong.** Cost Explorer's charts are for analysis in the console; they aren't line-item files to join with other data.
- **B is wrong.** A budget report summarizes budgets; it doesn't hold line items.
- **C is wrong.** A bill estimate models changes to a bill; it isn't a record of real usage.

</details>

**B11.** In one organization, the management account has turned discount sharing off for the `labs` account; sharing is on for every other account. This hour, the `core` account owns three Regional Reserved Instances for `m7g.large` Linux in one Region and runs two matching instances. `labs` runs one matching instance, and so does the `edge` account. How is this hour billed?

- A. `core`'s two instances and `labs`'s instance are covered; `edge` pays On-Demand
- B. `core`'s two instances and `edge`'s instance are covered; `labs` pays On-Demand
- C. `core`'s two instances are covered; the third reservation goes unused, and `labs` and `edge` pay On-Demand
- D. `labs`'s and `edge`'s instances are covered first; one of `core`'s pays On-Demand

<details><summary>Answer</summary>

**B is right.** The purchasing account comes first, so `core`'s two instances are covered. The third reservation passes to matching usage in another account, but only where sharing is on for both accounts: `edge`, not `labs`.

- **A is wrong.** With sharing off, `labs` can't receive another account's discount.
- **C is wrong.** Sharing is on for both `core` and `edge`, so the spare discount isn't wasted.
- **D is wrong.** A reservation always serves its purchasing account first.

</details>

**B12.** On 1 March, a company's management account activates the AWS-generated tag `aws:createdBy`. One resource of a supported type was created in January, and another in April. The company has also put a user-defined key, `project`, on its resources since January, but has never activated it. In May, which two statements are accurate? (Select TWO.)

- A. The April resource's costs can show who created it
- B. The January resource's costs show who created it, because it still exists after activation
- C. Costs grouped by `project` already appear in Cost Explorer, under `user:project`
- D. If `project` is activated now, costs carry it from then on, and earlier months need a backfill
- E. Each member account must activate `aws:createdBy` for its own resources

<details><summary>Answer</summary>

**A and D are right.** AWS applies `aws:createdBy` only to supported resources created after activation, so the April resource carries it. A user-defined key labels costs only once it's activated, from then on; earlier months can carry it only through a backfill, where the tag was on the resource at the time.

- **B is wrong.** Resources created before activation don't get the `aws:createdBy` tag.
- **C is wrong.** A tag that was never activated reaches no cost report, whatever it's called.
- **E is wrong.** Only the management account can activate `aws:createdBy`, once, for every member account.

</details>

## Enrichment

For learners who reached 10 or more on Check A. Each task has no single right answer; compare yours with the model answer.

**Task 1: write the bakery's commitment plan.** The bakery from the [module brief](00-brief.md) has two web servers that run every hour, extra servers in November and December, an order database on RDS that runs all year, and the accountant's nightly analysis that saves its progress. It now runs in an organization with a `shop-prod` and a `shop-dev` account. Write a short plan: how to pay for each part, how much to commit, and which account should buy the commitments. Link your answer to [COST07-BP05 Perform pricing model analysis at the management account level](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_master_analysis.html).

<details><summary>Model answer</summary>

Commit only to the base: a one-year Compute Savings Plan sized to the two servers that always run, because it keeps applying if the servers change family or move to Lambda. Leave the November and December extras On-Demand, since a commitment sized for the peak would sit idle for ten months. For the database, a Database Savings Plan or an RDS Reserved Instance, because it runs all year. Run the nightly analysis on Spot, since it can restart from its last save. Review the usage of all accounts before buying, and leave discount sharing on, so that a commitment one account can't fully use covers matching usage in the other. That's COST07-BP05: commitments are shared across the organization, so the analysis belongs where the whole picture is, at the management account.

</details>

**Task 2: a real-world complication with guardrails.** The bakery's production account runs the live website and order database; its sandbox account is where staff try tutorials. The owner says, "Set a budget action to stop everything when we pass the budget, in both accounts." Explain what you'd do instead in each account, and why a budget action doesn't make a budget a cap. Link your answer to [COST02-BP05 Implement cost controls](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_controls.html).

<details><summary>Model answer</summary>

In the sandbox, an automatic budget action that applies an IAM policy (or an SCP from the management account) to deny new launches is a fair control: nothing there matters to customers. In production, alerts go to a shared team address or chat channel, any action waits for a person to approve it, and nothing ever stops the web servers or the database automatically, because taking the shop offline costs more than the overspend. Even an automatic action isn't a cap: Budgets data is hours old, a deny policy stops only new launches, a stop action touches only the instances you named, and storage, NAT gateways and everything else keep billing. COST02-BP05 asks for controls that match the risk, which is why the two accounts get different ones.

</details>

**Task 3: split a shared cost fairly.** The chain's `log-archive` and `security-tools` accounts serve the shop, kitchen and delivery teams equally. The kitchen team says it shouldn't pay for them, because "we only have a few sensors". Propose how the cost category should handle the two shared accounts, and say what each team will see. Link your answer to [COST03-BP03 Identify cost attribution categories](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_define_attribution.html).

<details><summary>Model answer</summary>

Map both accounts to a `Shared` value in the `Team` cost category, then add a split charge rule that spreads `Shared` across the three teams in proportion to each team's own costs. The kitchen team, with the smallest costs, then carries the smallest share, which answers its objection without hiding the cost. An even split or fixed percentages are the alternatives if the teams agree to them. Each team's saved Cost Explorer report and budget, filtered to its `Team` value, then shows its own costs plus its share of the shared accounts. COST03-BP03 asks the business to agree on these categories in advance, so the split is settled once instead of argued over each month.

</details>

---

"Module 11 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
