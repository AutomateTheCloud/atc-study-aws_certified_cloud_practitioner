---
type: lesson
id: clf-11-04
title: "Many accounts, one bill"
tasks: ["4.2", "4.1"]
objectives: ["11.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 10, the guardrails primer, Simulation S11 and lesson 11.03; about 20 minutes; works on a phone"
prerequisites: [clf-09-10, clf-11-02, clf-11-03, clf-02-06]
terms_introduced: [purchasing account, discount sharing, cost allocation tag, AWS-generated tag, user-defined tag, tag activation, tag backfill]
pillars: [cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
---

# In one organization, a commitment discount follows matching usage across accounts, and a tag reaches your cost reports only after you activate it

An organization gets one bill, priced as if it were one account, so a commitment bought in one account can lower another account's costs. To split that bill by team, you tag resources, and the tags reach cost reports only after someone activates them.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** [Simulation S11](../09-protecting-and-governing/10-sim-organizations-and-scps.md) introduced the chain's organization (the bakery grown into a small chain) and [lesson 11.02](02-purchasing-options.md) the commitments; the ideas you need are restated here.

## Warm-up: what you remember

1. From lesson 11.02: is a Reserved Instance a server you launch?

<details><summary>Feedback</summary>

1. **No.** It's a billing discount applied to matching instances you run. That's why it can move between accounts, as this lesson shows.

</details>

## What you'll learn

By the end of this lesson, you can explain which account receives a Reserved Instance or Savings Plans discount in an organization, and how a tag reaches Cost Explorer, Budgets and the Cost and Usage Report (objective 11.04a).

Try this before you read on, and guess if you're unsure: you tag a bucket `team=kitchen` today. Will Cost Explorer show last month's cost for that bucket under `team=kitchen`?

## Consolidated billing combines usage and sends one bill

**Consolidated billing**, a feature of AWS Organizations, works like this ([Consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html), checked 2026-10-24):

- **The management account pays for every member account,** on one bill, at no extra fee.
- **For pricing, the organization counts as one account.** Volume tiers, such as S3's cheaper rate above 50 TB, apply to combined usage, and Reserved Instance and Savings Plans discounts are shared.
- **Each member account's own bill is for information.** The management account sees every account's costs.

AWS Billing Conductor, which builds a second, custom-priced version of the bill for AWS partners and internal chargeback, is out of the exam's scope; for "one bill for many accounts", the answer is consolidated billing.

> **Warning:** creating or joining an organization moves a Free plan account to the Paid plan ([Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), checked 2026-10-24). Learn this part from Simulation S11 and this lesson, not in your own account.

## A commitment discount goes to its owner first, then to matching usage anywhere in the organization

A Reserved Instance or Savings Plan is a billing discount, not a machine, so each hour AWS applies it to usage it can cover ([How Reserved Instance discounts are applied](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html); [Reserved Instances](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html); both checked 2026-10-24):

- **The purchasing account comes first.** The account that bought the commitment gets the discount on its own matching usage before any other account.
- **Then any matching usage in the organization.** This **discount sharing** is how consolidated billing works by default: an unused Reserved Instance in `shop-prod` can cover a matching instance in `shop-dev`.
- **The management account can turn sharing off** for any account ([Reserved Instances and Savings Plans discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html)); both accounts must have it on for a discount to pass between them.
- **The discount travels; the capacity doesn't.** A zonal Reserved Instance reserves capacity only for its own account.

> **Your turn:** Sharing is on everywhere. `shop-prod` owns two Regional `m7g.large` Reserved Instances but runs only one matching instance this hour; `shop-dev` runs two. How many instances get the discount, and whose?

<details><summary>Model answer</summary>

**Two:** `shop-prod`'s own instance first, then one of `shop-dev`'s. Two reservations can't cover three instances, so the third pays On-Demand. With sharing off for `shop-dev`, the second reservation would go unused but still be paid for.

</details>

## A tag reaches your cost reports only after you activate it

To split `shop-prod`'s costs among teams, you label each resource with a tag, such as `team=kitchen`. A **cost allocation tag** is a tag that billing tools use to organize costs, and there are two types ([Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html), checked 2026-10-24):

- **AWS-generated tags** are created and applied by AWS. The main one, `aws:createdBy`, records who created a resource. Only the management account can activate it, and AWS applies it only to supported resources created after activation ([Using AWS-generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html)).
- **User-defined tags** are tags you create and apply yourself. Reports show them with the prefix `user:`, and keys are case-sensitive: `team` and `Team` are two keys ([Using user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html)).

![A grid comparing AWS-generated and user-defined cost allocation tags: who applies them, an example key, the prefix in reports, who activates them and which costs carry them; the highlighted row says both must be activated before reports show them.](../../images/11-04-tag-types.svg)

*Notice the highlighted row. Whichever kind you use, nothing reaches a report until someone activates the key.*

**Long description.** Six rows comparing AWS-generated and user-defined tags. Who puts it on: AWS (and some Marketplace sellers); you, with Tag Editor, the console or the API. Example key: `aws:createdBy`; `team`, `project` or `cost-center`. In reports: `aws:` prefix; `user:` prefix. Who activates: the management account, once, for all member accounts; the management account or a standalone account. Highlighted, the same for both: must be activated before reports show it. Which costs carry it: only resources created after activation; usage from activation on, while the resource carries the tag. A note: up to 24 hours to appear after activation.

**Tag activation** is the step people miss. In the Billing and Cost Management console, the management account (or a standalone account) chooses which tag keys billing should use. Only those keys appear in Cost Explorer, Budgets and the Cost and Usage Report, where each becomes a column, and activation can take up to 24 hours.

### "A tag shows costs" is wrong

It's easy to assume that tagging a resource is enough to see its costs by tag. It isn't: a tag is invisible to billing until its key is activated, and then it labels usage **from activation onward**. A management account can request a **tag backfill** for up to twelve earlier months, but only where the resource carried the tag at the time ([Backfill cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html), checked 2026-10-24). It's tempting because Tag Editor finds tagged resources at once (Lab 01), but finding resources and grouping costs are separate systems.

> **Example:** the chain's shop, kitchen and delivery teams want their own costs. Accounts already split costs with no work, so `shop-dev` belongs to the shop team as it is. Only `shop-prod` holds all three teams' work, so its resources get `team=shop`, `team=kitchen` or `team=delivery`, and the management account activates the key `team` on day one, because costs from before activation won't carry it.

## Summary

- **Consolidated billing** sends every account's charges to one bill, paid by the management account at no extra fee, and prices the organization as one account.
- **A commitment discount serves its purchasing account first,** then matching usage in other accounts, unless the management account turns sharing off. The discount travels; a zonal reservation's capacity doesn't.
- **Two cost allocation tag types:** AWS-generated (`aws:createdBy`) and user-defined (`user:` in reports). Both must be **activated** before Cost Explorer, Budgets or the CUR show them, and they label usage only from then on.

## Practice

1. **A company has three accounts in one organization. Account A bought Reserved Instances it no longer fully uses; account C runs matching instances. Nobody has changed the billing preferences. Who benefits from A's unused Reserved Instances?**

   A. Nobody: unused Reserved Instances are wasted\
   B. Account C, because consolidated billing shares discounts unless the management account turns sharing off\
   C. Only the management account\
   D. Account C, but only if C pays A

   <details><summary>Feedback</summary>

   **B is right.** For billing, the organization counts as one account.

   - **A is wrong.** That happens only if sharing is off or no account has matching usage.
   - **C is wrong.** The management account pays the bill; the discount follows matching usage.
   - **D is wrong.** No payment between accounts is needed.

   </details>

2. **A team tagged its EC2 instances `project=atlas` two weeks ago, but Cost Explorer shows no `project` tag. What is the most likely cause?**

   A. EC2 instances can't carry cost allocation tags\
   B. The `project` key was never activated as a cost allocation tag\
   C. Cost Explorer only shows AWS-generated tags\
   D. Tags appear only in the CUR, never in Cost Explorer

   <details><summary>Feedback</summary>

   **B is right.** A tag reaches billing tools only after its key is activated.

   - **A is wrong.** EC2 instances can be tagged, and those tags used for cost allocation.
   - **C is wrong.** Cost Explorer shows both types once they're activated.
   - **D is wrong.** Activated tags appear in Cost Explorer, Budgets and the CUR.

   </details>

3. **Which pair names the two types of cost allocation tag?**

   A. Public and private\
   B. AWS-generated and user-defined\
   C. Account and resource\
   D. Active and backfilled

   <details><summary>Feedback</summary>

   **B is right.** AWS applies the first kind, such as `aws:createdBy`; you apply the second. Both must be activated.

   - **A is wrong.** Tags have no public or private type.
   - **C is wrong.** Those are things you can tag, not tag types.
   - **D is wrong.** Those describe a tag's status, not its type.

   </details>

**Next:** activate tags yourself in [Optional lab 16](06-lab-16-cost-allocation-tags.md), or go on to [Simulation S13](07-sim-purchasing-option-tree.md).

## Where to check the current details

- [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) (checked 2026-10-24)
- [Reserved Instances and Savings Plans discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) (checked 2026-10-24)
- [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) (checked 2026-10-24)

---

"Many accounts, one bill" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
