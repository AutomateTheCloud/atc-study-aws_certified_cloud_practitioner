---
type: lesson
id: clf-11-03
title: "Estimate, watch, analyze"
tasks: ["4.2"]
objectives: ["11.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 10 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [guardrails-05, clf-10-01, clf-02-02]
terms_introduced: [AWS Pricing Calculator, estimate, AWS Budgets, budget threshold, forecasted cost, budget action, AWS Cost Anomaly Detection, AWS Cost Explorer, forecast, line item, AWS Data Exports, AWS Cost and Usage Report, CUR 2.0]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html"
  - "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html"
  - "https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html"
  - "https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html"
---

# Estimate before you build, watch while it runs, analyze after the fact: each stage has its own cost tool

AWS has a different cost tool for each job: AWS Pricing Calculator estimates, AWS Budgets alerts, AWS Cost Explorer analyzes and forecasts, and the Cost and Usage Report holds every line item. None of them stops spending on its own, and that's the point most people get wrong.

**Exam guide:** [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** on [primer page 05](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md) you created two budgets and set up anomaly alerts; this lesson explains the tools behind them.

## Warm-up: what you remember

1. From lesson 10.01: the bakery keeps a year of website logs as files in S3. Which service runs SQL on those files where they sit?

<details><summary>Feedback</summary>

1. **Amazon Athena.** You'll meet it again here: AWS's most detailed billing data arrives as files in S3, ready for Athena.

</details>

## What you'll learn

By the end of this lesson, you can pick the cost tool for each stage, estimate, watch, analyze or dig into raw detail, and say what question it answers (objective 11.03a).

Try this before you read on, and guess if you're unsure: your monthly budget's 100% alert arrives by email. What happens to the resources that caused it?

## The big picture: pick the tool by the question it answers

![A grid of five cost tools with the stage each serves, the question it answers, and whether it acts on its own; only AWS Budgets can act, and only through a budget action you add.](../../images/11-03-tools-compared.svg)

*Notice the highlighted cell: only one tool can act, and only when you configure it to.*

**Long description.** A grid with five rows and three columns after the tool name: stage, the question it answers, and whether it acts on its own. AWS Pricing Calculator: before you build; what will this design cost a month; no, an estimate only. AWS Budgets: while it runs; are we heading past our limit, tell me; emails only, unless you add a budget action (highlighted). AWS Cost Anomaly Detection: while it runs; is spending unusual for us, tell me; no, alerts only. AWS Cost Explorer: after the fact; where did the money go, and where is it heading; no, charts, forecasts and recommendations. Cost and Usage Report (CUR 2.0) in Data Exports: raw detail; every line item, to query my own way; no, files in your S3 bucket.

The exam's task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2) names all of these except Cost Anomaly Detection (checked 2026-10-24).

## AWS Pricing Calculator estimates a design before it exists

An **estimate** is a cost worked out from assumptions about something that doesn't exist yet. **AWS Pricing Calculator** is a free web tool, at [calculator.aws](https://calculator.aws/), that makes one ([What is AWS Pricing Calculator?](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html), checked 2026-10-24). You pick services and describe how you'll use them (hours, GB, requests), and it shows the monthly, upfront and yearly cost; groups price two designs side by side. A saved estimate is a link on AWS's public servers, so leave out names and secrets. It leaves out tax, and it's only as good as your guesses.

Older material may send you to the **TCO Calculator** or the **Simple Monthly Calculator**. Both are gone; their addresses now lead to the Pricing Calculator.

## AWS Budgets tells you when you pass a limit; it stops nothing unless you add an action

**AWS Budgets** tracks your cost or usage against a target you set and alerts you when it crosses a **budget threshold**, such as 85% of $150 ([Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), checked 2026-10-24):

- **Budget types:** cost, usage, and the utilization and coverage of Reserved Instances and Savings Plans, which tell you whether a commitment is going unused.
- **Actual and forecasted alerts.** An alert can fire when actual cost passes a threshold, or when the **forecasted cost** for the period will pass it, which warns you before the money is spent.
- **Email or Amazon SNS,** and through SNS, chat tools.
- **Delay.** Budgets data updates up to three times a day, so spending can pass a threshold hours before the alert.

### "A budget caps your spending" is wrong

Many people expect a budget to stop spending at its amount. It doesn't: a budget on its own only sends alerts, and resources keep running and billing. It's tempting because in everyday speech a budget is a limit, and prepaid services elsewhere stop when the money runs out.

What you *can* add is a **budget action**: something Budgets does when a threshold is crossed, automatically or after someone approves it ([Configuring budget actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html), checked 2026-10-24). It can **apply an IAM policy**, such as one that denies new EC2 launches; **attach a service control policy** (lesson 09.05) from a management account; or **stop chosen EC2 or RDS instances**. Even then a budget isn't a cap: actions block new work or stop the instances you named, hours after the spending, and everything else keeps billing. Nothing is deleted. For "alert me when costs exceed a limit", the exam expects Budgets.

> **Your turn:** Answer the prequestion. The bakery's $150 budget sends its 100% alert on January 29, and no budget action is set. A forgotten test instance caused it. What happens to the instance, and what would have blocked new launches automatically?

<details><summary>Model answer</summary>

**Nothing happens to it:** it keeps running and billing until someone stops or terminates it. A budget action that applies an IAM policy denying new launches would have blocked *new* instances, but even that leaves running ones alone; only an action naming that instance in advance would stop it.

</details>

## Cost Anomaly Detection tells you when spending is unusual

**AWS Cost Anomaly Detection** uses machine learning to learn your normal spending pattern and alerts you when spending departs from it ([Detecting unusual spend](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html), checked 2026-10-24). A budget compares cost with a number *you* chose; anomaly detection compares it with what's *normal for you*. It costs nothing and, like Budgets, never stops anything.

## Cost Explorer shows where the money went, and forecasts what comes next

**AWS Cost Explorer** shows your costs and usage as charts and tables that you filter and group by service, account, Region, instance type, cost allocation tag and more ([Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), checked 2026-10-24). It's the tool for "where did the money go?" It also gives a **forecast**, a prediction of future cost from your past usage, and recommends Reserved Instances and Savings Plans from your history.

### Older figures for Cost Explorer's history and forecast are out of date

You may have read that Cost Explorer shows the last 12 months and forecasts the next 12. As of 2026-10-24, AWS's guide says it shows up to the previous **13 months** and forecasts up to **18 months** ahead ([Forecasting with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html)). It's tempting because older wording and many practice questions still say 12 and 12. On the exam, look for "visualize, analyze, forecast", not a number.

## The Cost and Usage Report holds every line item, delivered through Data Exports

A **line item** is one row of a bill: one product, one kind of usage, for one period. The **AWS Cost and Usage Report (CUR)** is the most detailed cost and usage data AWS provides: every line item, by hour, day or month, optionally with resource IDs and a column for each cost allocation tag ([What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), checked 2026-10-24). AWS delivers it as files to an S3 bucket you choose, where you can query it with Athena or chart it in Amazon Quick Sight.

The exam guide says "AWS Cost and Usage Report". Today you create it in **AWS Data Exports**, a page of the Billing and Cost Management console, where AWS calls **CUR 2.0** "the new and recommended way" to get this data ([What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), checked 2026-10-24).

> **Example:** January's bill reaches $165.98 against a $150 budget. Cost Anomaly Detection flagged a new daily EC2 cost around January 12; Cost Explorer, grouped by service and then by instance type, shows one forgotten `r7g.large`. Terminated after that alert, it would have cost about $5 instead of $54.

On the exam, name the stage, then the question: "estimate" points to the calculator, "alert" to Budgets, "unusual" to anomaly detection, "visualize, analyze, forecast" to Cost Explorer, and "most detailed" or "line items in S3" to the CUR.

## Summary

- **Pricing Calculator estimates before you build,** from your assumptions. It's free, leaves out tax, and replaced the TCO and Simple Monthly calculators.
- **Budgets alert** on actual or forecasted cost or usage, hours after the spending. **A budget doesn't cap spending;** only a budget action does anything, and only what you set.
- **Cost Anomaly Detection** alerts on spending that's unusual for you, at no charge.
- **Cost Explorer analyzes after the fact** and forecasts up to 18 months, not 12.
- **The CUR holds every line item,** now created as CUR 2.0 in AWS Data Exports and delivered to your S3 bucket.

## Practice

1. **A startup wants an email when its forecasted monthly cost will exceed $1,000. Which tool should it use?**

   A. AWS Cost Explorer\
   B. AWS Budgets\
   C. AWS Pricing Calculator\
   D. The Cost and Usage Report

   <details><summary>Feedback</summary>

   **B is right.** Budgets alerts on actual or forecasted cost against a limit you set.

   - **A is wrong.** Cost Explorer shows a forecast, but it doesn't alert you on a limit.
   - **C is wrong.** The calculator estimates designs you haven't built; it doesn't watch real spending.
   - **D is wrong.** The CUR delivers raw data; it sends no alerts.

   </details>

2. **Which statement about budget actions is correct?**

   A. Every budget stops resources when it reaches 100%\
   B. A budget action can apply an IAM policy or SCP, or stop chosen EC2 or RDS instances, automatically or after approval\
   C. A budget action deletes the resources that caused the overspend\
   D. Budget actions act the moment a charge occurs

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** A budget without an action only alerts.
   - **C is wrong.** Actions block or stop; they never delete.
   - **D is wrong.** Budgets data updates up to three times a day, so actions run hours after the spending.

   </details>

3. **A finance analyst needs hourly cost for every resource, with each team's tag, to load into the company's own reporting database. Which should she use?**

   A. AWS Cost Explorer's charts\
   B. The AWS Cost and Usage Report, created in AWS Data Exports\
   C. An AWS Budgets alert\
   D. AWS Pricing Calculator

   <details><summary>Feedback</summary>

   **B is right.** The CUR holds every line item, with resource IDs and tag columns, as files in an S3 bucket.

   - **A is wrong.** Cost Explorer's charts aren't line-item files to load elsewhere.
   - **C is wrong.** A budget alert holds no line items.
   - **D is wrong.** The calculator estimates; it records no real usage.

   </details>

**Next:** [Many accounts, one bill](04-many-accounts-one-bill.md). To price a design yourself, do [Lab 15](05-lab-15-pricing-calculator.md).

## Where to check the current details

- [What is AWS Pricing Calculator?](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) (checked 2026-10-24)
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and [Configuring budget actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) (checked 2026-10-24)
- [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) and [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) (checked 2026-10-24)

---

"Estimate, watch, analyze" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
