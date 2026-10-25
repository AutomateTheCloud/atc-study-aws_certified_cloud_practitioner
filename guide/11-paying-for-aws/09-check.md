---
type: check
id: clf-11-09
title: "Module 11 mastery check"
tasks: ["4.1", "4.2"]
objectives: ["11.01a", "11.02a", "11.03a", "11.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished lessons 11.01 to 11.04; about 20 minutes for each check; works on a phone"
prerequisites: [clf-11-01, clf-11-02, clf-11-03, clf-11-04]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html"
  - "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"
---

# Module 11 mastery check: say what drives a bill, choose how to pay, pick the cost tool, and trace who gets a discount

**For:** an adult studying alone, possibly new to IT, who has finished lessons [11.01](01-how-aws-charges.md) to [11.04](04-many-accounts-one-bill.md). **Time:** about 20 minutes per check. No question needs a price.

**Exam guide:** [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): tasks [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1) and [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2).

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 12.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

**A1.** A team says, "Our data never leaves AWS, so we pay nothing for data transfer." Which two of its flows add a data transfer charge? (Select TWO.)

- A. Users upload photos from their browsers to the web servers
- B. Web servers in two Availability Zones exchange session data
- C. The web servers read and write objects in an S3 bucket in the same Region
- D. Each night, backups are copied to a bucket in a second Region
- E. Objects are served from the S3 bucket to Amazon CloudFront

<details><summary>Answer</summary>

**B and D are right.** Data across Availability Zones and data copied to another Region are charged per GB, even though neither leaves AWS.

- **A is wrong.** Data in from the internet is free.
- **C is wrong.** EC2 to S3 in the same Region has no transfer charge.
- **E is wrong.** S3 to CloudFront is free; CloudFront charges for what it delivers.

</details>

**A2.** Two months into the Free plan, a learner's friend suggests, "Upgrade to the Paid plan to try more services, then switch back." As of 2026-10-24, what is the problem?

- A. Upgrading is one way, and usage beyond her credits will then be billed
- B. Upgrading uses up her remaining credits at once
- C. The Paid plan offers the same services as the Free plan
- D. She can't upgrade until her twelve free months have ended

<details><summary>Answer</summary>

**A is right.** A Free plan account can move to the Paid plan but never back.

- **B is wrong.** Remaining credits apply to later bills after an upgrade.
- **C is wrong.** The Paid plan gives access to every service; the Free plan to selected ones.
- **D is wrong.** "Twelve free months" is the legacy Free Tier, for accounts created before 2025-07-15.

</details>

**A3.** Team 1 is sure its instance family won't change and wants to be able to sell unused reservations; Team 2 expects to move to a newer family. Which Reserved Instances fit?

- A. Convertible for Team 1, and Standard for Team 2
- B. Standard for Team 1, and Convertible for Team 2
- C. Standard for both teams
- D. Convertible for both teams

<details><summary>Answer</summary>

**B is right.** Standard can be sold on the Reserved Instance Marketplace; Convertible can be exchanged for another family.

- **A is wrong.** It's the wrong way around.
- **C is wrong.** Team 2 couldn't move a Standard reservation to the new family.
- **D is wrong.** Team 1 would give up discount and the right to sell.

</details>

**A4.** A health records company must never share hardware with other AWS customers. It has no per-core licensing and wants capacity held in one Availability Zone, simply. Which fits?

- A. Dedicated Hosts
- B. Dedicated Instances, with a Capacity Reservation
- C. Zonal Reserved Instances on shared hardware
- D. Spot Instances

<details><summary>Answer</summary>

**B is right.** Dedicated Instances are single-tenant without managing a server, and support Capacity Reservations.

- **A is wrong.** Dedicated Hosts are for per-core licenses, are more to manage, and don't support Capacity Reservations.
- **C is wrong.** Shared hardware breaks the rule.
- **D is wrong.** Spot can be interrupted and isn't dedicated.

</details>

**A5.** A ticketing company runs a payment service on six instances every hour, as it has for two years; a nightly report that can restart from saved progress; and a one-week sale that needs instances certain to launch in one Availability Zone. Which two pairings fit? (Select TWO.)

- A. Payment service: a Savings Plan covering its six instances
- B. Report generator: Spot Instances
- C. Sale week: Spot Instances, for the lowest price
- D. Payment service: Spot Instances
- E. Sale week: a one-year Compute Savings Plan

<details><summary>Answer</summary>

**A and B are right.** Steady use fits a commitment; restartable work fits Spot.

- **C is wrong.** Spot guarantees no capacity; the sale needs a Capacity Reservation.
- **D is wrong.** A payment service mustn't be interrupted.
- **E is wrong.** A Savings Plan holds no capacity, and a year's commitment for one week would sit idle.

</details>

**A6.** A charity must show its board the monthly cost of two designs for a new website, side by side, before building either. Which tool should it use?

- A. AWS Cost Explorer
- B. A forecasted-cost alert in AWS Budgets
- C. AWS Pricing Calculator
- D. AWS TCO Calculator

<details><summary>Answer</summary>

**C is right.** It estimates designs that don't exist yet, side by side in groups.

- **A is wrong.** Cost Explorer works from usage you already have.
- **B is wrong.** A forecast alert watches real spending; it can't price a design.
- **D is wrong.** The TCO Calculator is gone; its address leads to the Pricing Calculator.

</details>

**A7.** An instructor wants new instance launches blocked automatically in a student's sandbox account once actual cost reaches its monthly budget, without deleting anything. Which setup does this?

- A. The budget's alert alone, because AWS stops spending at the budget amount
- B. A budget action that applies an IAM policy denying new launches
- C. A Cost Anomaly Detection monitor set to stop launches
- D. A Cost Explorer forecast for each student's account

<details><summary>Answer</summary>

**B is right.** A budget action can apply an IAM policy when a threshold is crossed; running instances keep billing.

- **A is wrong.** A budget alone only alerts; it doesn't cap spending.
- **C is wrong.** Anomaly Detection only alerts.
- **D is wrong.** A forecast takes no action.

</details>

**A8.** A finance manager wants to see which services grew most since last quarter and what the coming months will cost, in charts she can filter in a few clicks, with nothing to set up. Which tool fits?

- A. AWS Budgets
- B. AWS Cost and Usage Report
- C. Amazon Quick Sight
- D. AWS Cost Explorer

<details><summary>Answer</summary>

**D is right.** Cost Explorer charts past cost and forecasts from your history.

- **A is wrong.** Budgets alerts on a limit; it isn't for finding what grew.
- **B is wrong.** The CUR (today a CUR 2.0 export in AWS Data Exports) delivers line-item files to query yourself.
- **C is wrong.** Quick Sight needs a data source set up first.

</details>

**A9.** Discount sharing is on everywhere. This hour, `mobile` owns two Regional `c7g.large` Linux Reserved Instances and runs one matching instance; `web` runs two. How is the hour billed?

- A. Both of `web`'s instances are covered first; `mobile`'s pays On-Demand
- B. Only `mobile`'s instance is covered; the second reservation goes unused
- C. `mobile`'s instance and one of `web`'s are covered; `web`'s other pays On-Demand
- D. All three instances are covered, because the organization counts as one account

<details><summary>Answer</summary>

**C is right.** The purchasing account comes first, then matching usage elsewhere.

- **A is wrong.** The purchasing account always comes first.
- **B is wrong.** With sharing on, unused discount passes to other accounts.
- **D is wrong.** Two reservations can't cover three instances.

</details>

**A10.** Resources have carried the user-defined tag key `costcenter` since March. On June 1, the management account activates it. In July, finance groups Cost Explorer by `costcenter`. Which two statements are accurate? (Select TWO.)

- A. Costs from March to May already carry the values, because the resources were tagged
- B. Costs from shortly after June 1 onward carry the `costcenter` values
- C. Each member account must also activate `costcenter`
- D. The key appears in reports as `aws:costcenter`
- E. Costs from March to May carry the values only if the management account requests a tag backfill

<details><summary>Answer</summary>

**B and E are right.** An activated tag labels usage from then on; a backfill can reach earlier months where the tag was already on.

- **A is wrong.** Tagging alone shows no costs.
- **C is wrong.** In an organization, only the management account activates cost allocation tags.
- **D is wrong.** User-defined tags show the `user:` prefix; `aws:` marks AWS-generated tags.

</details>

## Correction map

For each miss, reread the section and redo its practice.

| Question | Objective | Reread |
|---|---|---|
| A1, B1 | 11.01a | [Data transfer is priced by direction](01-how-aws-charges.md#data-transfer-is-priced-by-direction-in-is-free-but-out-across-and-between-usually-cost) |
| A2, B2 | 11.01a | [The Free Tier now](01-how-aws-charges.md#the-free-tier-now-two-plans-credits-and-two-clocks) |
| A3, B3 | 11.02a | [Reserved Instances](02-purchasing-options.md#reserved-instances-a-billing-discount-on-a-matching-configuration) |
| A4, B4 | 11.02a | [Dedicated Hosts and Instances](02-purchasing-options.md#dedicated-hosts-and-dedicated-instances-hardware-with-no-other-customers) |
| A5, B5 | 11.02a | [Choosing an option](02-purchasing-options.md#choosing-an-option-for-a-usage-pattern); [Simulation S13](07-sim-purchasing-option-tree.md) |
| A6, B6 | 11.03a | [AWS Pricing Calculator](03-estimate-watch-analyze.md#aws-pricing-calculator-estimates-a-design-before-it-exists) |
| A7, B7 | 11.03a | [AWS Budgets](03-estimate-watch-analyze.md#aws-budgets-tells-you-when-you-pass-a-limit-it-stops-nothing-unless-you-add-an-action) |
| A8, B8 | 11.03a | [Pick the tool by the question](03-estimate-watch-analyze.md#the-big-picture-pick-the-tool-by-the-question-it-answers) |
| A9, B9 | 11.04a | [Discounts across accounts](04-many-accounts-one-bill.md#a-commitment-discount-goes-to-its-owner-first-then-to-matching-usage-anywhere-in-the-organization) |
| A10, B10 | 11.04a | [Activating tags](04-many-accounts-one-bill.md#a-tag-reaches-your-cost-reports-only-after-you-activate-it) |

## Check B: parallel retest

**B1.** A video company's design runs in one Region. Which two flows add a data transfer charge? (Select TWO.)

- A. Customers upload videos from their browsers to the company's servers
- B. Servers write each video's details to a DynamoDB table in the same Region
- C. Servers in one Availability Zone send finished files to servers in another
- D. Videos are served from an S3 bucket to Amazon CloudFront
- E. Viewers stream videos from the company's EC2 servers over the internet

<details><summary>Answer</summary>

**C and E are right.** Data across Availability Zones and data out to the internet are charged per GB.

- **A is wrong.** Data in from the internet is free.
- **B is wrong.** EC2 to DynamoDB in the same Region has no transfer charge.
- **D is wrong.** S3 to CloudFront is free.

</details>

**B2.** A learner's account has been on the Free plan for four months, and she has used up all her credits. She hasn't changed anything. As of 2026-10-24, what happens?

- A. Her card is charged at normal rates from now on
- B. Her usage stays free until twelve months after sign-up
- C. The plan ends and the account closes; upgrading in time restores access
- D. AWS adds fresh credits each month until the plan's time limit

<details><summary>Answer</summary>

**C is right.** Whichever runs out first, six months or the credits, ends the Free plan.

- **A is wrong.** The Free plan never bills; that's the Paid plan.
- **B is wrong.** "Twelve months free" is the legacy Free Tier.
- **D is wrong.** Credits aren't topped up each month.

</details>

**B3.** A year into a three-year Convertible Reserved Instance, a project ends and the reservation no longer matches any running instance. What can the company do?

- A. Sell it on the Reserved Instance Marketplace
- B. Cancel it for a refund of the remaining term
- C. Ask AWS to convert it into a Compute Savings Plan
- D. Exchange it for another Convertible Reserved Instance of at least equal value

<details><summary>Answer</summary>

**D is right.** A Convertible can be exchanged for one with a different family, operating system or tenancy, of equal or higher value.

- **A is wrong.** Only Standard Reserved Instances can be sold there.
- **B is wrong.** Reserved Instances can't be canceled.
- **C is wrong.** The lessons describe no such conversion.

</details>

**B4.** A vendor licenses software per physical core, audits the server it runs on, and requires instances to stay on that server after a stop and start. Which option fits?

- A. Dedicated Instances
- B. Dedicated Hosts
- C. An On-Demand Capacity Reservation
- D. Spot Instances

<details><summary>Answer</summary>

**B is right.** A Dedicated Host shows its cores and keeps instances on the host you choose.

- **A is wrong.** Dedicated Instances show nothing of the server and may move after a stop and start.
- **C is wrong.** A Capacity Reservation holds capacity; it doesn't make the hardware yours.
- **D is wrong.** Spot is shared spare capacity and can be interrupted.

</details>

**B5.** A delivery app has a weekly training job that saves checkpoints; a launch next month needing 20 instances certain to start in one Availability Zone; and a three-day promotion whose few instances can launch slowly. Which two pairings fit? (Select TWO.)

- A. Training job: Spot Instances
- B. Promotion: a one-year Savings Plan sized to the promotion
- C. Product launch: Spot Instances
- D. Product launch: a Capacity Reservation, billed at the On-Demand rate
- E. Training job: three-year Standard Reserved Instances

<details><summary>Answer</summary>

**A and D are right.** Restartable work fits Spot; only a Capacity Reservation guarantees capacity in one AZ, with no discount of its own.

- **B is wrong.** A year's commitment for three days would sit idle; that's On-Demand.
- **C is wrong.** Spot guarantees nothing.
- **E is wrong.** A weekly job would leave most of the commitment unused.

</details>

**B6.** A school district wants a monthly cost estimate for a new enrollment feature that isn't built yet. Which tool produces it?

- A. AWS Cost Anomaly Detection
- B. AWS Pricing Calculator
- C. AWS Trusted Advisor
- D. AWS Simple Monthly Calculator

<details><summary>Answer</summary>

**B is right.** It estimates a design before anything exists.

- **A is wrong.** It watches real spending.
- **C is wrong.** Trusted Advisor (Module 12) checks resources you already run.
- **D is wrong.** The Simple Monthly Calculator is gone.

</details>

**B7.** A team wants chosen EC2 instances in its test account to stop when cost crosses its budget, but only after a lead confirms. Which setup does this?

- A. A budget action that stops the chosen instances, set to wait for approval
- B. The budget alone, because AWS stops resources at the budget
- C. A Cost Anomaly Detection subscription that stops the instances
- D. A Cost Explorer report with a rule that stops the instances

<details><summary>Answer</summary>

**A is right.** A budget action can stop chosen instances, automatically or after approval.

- **B is wrong.** A budget alone only alerts.
- **C is wrong.** Anomaly Detection never stops anything.
- **D is wrong.** Cost Explorer can't act on resources.

</details>

**B8.** Analysts want to join AWS costs with sales data in Amazon Athena daily, at the finest detail, with each cost's resource ID. Which should they set up?

- A. A saved AWS Cost Explorer report
- B. An AWS Budgets report emailed each day
- C. A bill estimate in AWS Pricing Calculator
- D. An AWS Cost and Usage Report delivered to an S3 bucket

<details><summary>Answer</summary>

**D is right.** The CUR holds every line item, with resource IDs, as files in S3; today it's a CUR 2.0 export in AWS Data Exports.

- **A is wrong.** Cost Explorer's charts aren't line-item files.
- **B is wrong.** A budget report holds no line items.
- **C is wrong.** An estimate isn't a record of real usage.

</details>

**B9.** Discount sharing is off for the `labs` account and on for every other. This hour, `core` owns three Regional `m7g.large` Linux Reserved Instances and runs two matching instances; `labs` and `edge` each run one. How is the hour billed?

- A. `core`'s two and `labs`'s instance are covered; `edge` pays On-Demand
- B. `core`'s two and `edge`'s instance are covered; `labs` pays On-Demand
- C. Only `core`'s two are covered; the third reservation goes unused
- D. `labs`'s and `edge`'s are covered first; one of `core`'s pays On-Demand

<details><summary>Answer</summary>

**B is right.** `core` comes first; the spare reservation passes only where sharing is on for both accounts.

- **A is wrong.** With sharing off, `labs` can't receive the discount.
- **C is wrong.** Sharing is on for `core` and `edge`.
- **D is wrong.** The purchasing account always comes first.

</details>

**B10.** On March 1, a management account activates `aws:createdBy`. One supported resource was created in January, another in April. The user-defined key `project` has been on resources since January but never activated. In May, which two statements are accurate? (Select TWO.)

- A. The April resource's costs can show who created it
- B. The January resource's costs show who created it, because it still exists
- C. Costs grouped by `project` already appear under `user:project`
- D. If `project` is activated now, costs carry it from then on, and earlier months need a backfill
- E. Each member account must activate `aws:createdBy` itself

<details><summary>Answer</summary>

**A and D are right.** `aws:createdBy` applies only to resources created after activation, and a user-defined key labels costs only once activated.

- **B is wrong.** Resources created before activation don't get the tag.
- **C is wrong.** A key never activated reaches no report.
- **E is wrong.** Only the management account activates it, for every account.

</details>

---

"Module 11 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
