---
type: page
id: clf-11-10
title: "Module 11: beyond the exam"
reader: "Adult who has finished Module 11 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-11-00]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/free/free-tier-faqs/"
  - "https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-multi-year-data.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html"
---

# Module 11: what we left out, and where to read it

The CLF-C02 exam asks which pricing model or billing tool fits a need, not how to work out a bill or configure the tools. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Reading and modeling a bill

- **Working out a bill line by line.** Sorting a month's line items by meter, separating what grew with customers from what was added, and pricing each change. See [AWS pricing](https://aws.amazon.com/pricing/) and each service's pricing page.
- **Data transfer in detail.** Rates per Region pair, volume tiers, the 100 GB monthly allowance and the NAT gateway's per-GB processing charge. See the [EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) page and [COST08-BP01 Perform data transfer modeling](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_modeling.html).
- **Free Tier fine print.** When leftover credits expire after an upgrade (AWS's pages said 6 or 12 months when we checked on 2026-10-24) and the 90 days AWS keeps a closed Free plan account's content. See the [Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/) and your account's **Credits** page.

## Purchasing options

- **How Savings Plans apply each hour.** Commitment unused in one hour is lost, and a small plan can be returned within 7 days. See [How Savings Plans apply](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) and the [Savings Plans FAQ](https://aws.amazon.com/savingsplans/faq/).
- **Instance size flexibility arithmetic.** Normalization factors (small 1, medium 2, large 4) decide how much of a bigger instance a smaller reservation covers. See [How Reserved Instance discounts are applied](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html).
- **Pricing a commitment.** AWS's average discounts (for example 40% for a one-year Standard Reserved Instance against the 72% maximum), payment options, and sizing a commitment to a year of usage. See [Reserved Instances pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/) and [COST07-BP01 Perform pricing model analysis](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_analysis.html).
- **Future-dated Capacity Reservations.** Booked 5 to 120 days ahead, with a minimum commitment and size. See [Capacity Reservation concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html).
- **Dedicated hardware costs.** Dedicated Instances' per-Region hourly fee and Dedicated Host Reservations. See [Dedicated Hosts pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/).

## Cost tools in depth

- **Budgets in practice.** How often data refreshes, verifying email recipients, budget periods, and what action-enabled budgets cost. See [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and [AWS Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/).
- **Spend limits.** On the new sign-up experience's Paid plan, a spend limit pauses a project at the limit. See [Create a spend limit](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html).
- **Cost Anomaly Detection setup.** Cost monitors, alert subscriptions, and the history a new service needs before anomalies are detected. See [Detecting unusual spend](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html).
- **Cost Explorer options.** Multi-year data up to 38 months, hourly data, the forecast's prediction interval and the charged API. See [Multi-year data](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-multi-year-data.html) and [Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/).
- **Pricing Calculator in the console.** Workload estimates and bill estimates that use your own discounts. See [Pricing Calculator concepts](https://docs.aws.amazon.com/cost-management/latest/userguide/pc-concepts.html).
- **Querying the CUR.** CUR 2.0 columns, Parquet files, Athena and a ready-made Quick Sight dashboard. See [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)

## Many accounts

- **The order discounts apply in.** Reserved Instances before Savings Plans, EC2 Instance before Compute Savings Plans. See [How Savings Plans apply](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html).
- **Group sharing.** Prioritized and restricted sharing, and the month-end settings the bill uses. See [Reserved Instances and Savings Plans discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html).
- **Cost categories, split charges and account tags.** Rules that name groups of costs, spread shared costs across teams, and tag whole accounts. See [Creating cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html) and [Using account tags for cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/account-tags-cost-allocation.html).
- **AWS Billing Conductor.** A second, custom-priced version of the bill for AWS partners and internal chargeback; out of the exam's scope. See [What is AWS Billing Conductor?](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html)

## Well-Architected practices for cost

Budgets and forecasts ([COST01-BP03 Establish cloud budgets and forecasts](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_budget_forecast.html)), watching spend before the bill arrives ([COST01-BP06 Monitor cost proactively](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_proactive_process.html)) and tagging for cost ([COST03-BP02 Add organization information to cost and usage](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_org_information.html)) belong to running a cost practice, not to this exam.

---

"Module 11: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
