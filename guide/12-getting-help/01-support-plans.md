---
type: lesson
id: clf-12-01
title: "Support plans"
tasks: ["4.3", "3.8"]
objectives: ["12.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 11 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-12-00, clf-04-03, clf-00-04]
terms_introduced: [AWS Support, Support plan, support case, Basic Support, AWS Business Support+, AWS Enterprise Support, AWS Unified Operations, case severity, first-response time, Technical Account Manager, Developer Support, Business Support, Enterprise On-Ramp]
pillars: [operational-excellence, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://aws.amazon.com/premiumsupport/pricing/"
  - "https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-intro.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html"
  - "https://aws.amazon.com/premiumsupport/plans/enterprise/"
  - "https://aws.amazon.com/premiumsupport/faqs/"
---

# Choose the cheapest Support plan that covers your worst day: Basic, Business Support+, Enterprise or Unified Operations

AWS sells help with your account in four plans, and each one includes everything in the plan below it. Basic is free but answers no technical questions; each paid step adds faster replies and more people, for a higher monthly fee.

**Exam guide:** [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [AWS changes fast](../00-start-here/04-aws-changes-fast.md), which warned that the Support plans changed. The bakery scenario is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From Module 11: the bakery's costs pass its $300 monthly budget. Does AWS stop its servers?
2. From lesson 04.03: must the owner sign in as the root user to change the account's Support plan?

<details><summary>Feedback</summary>

1. **No.** A budget alerts you; on its own it stops nothing. A Support plan is similar: it gets you help, but doesn't run your systems.
2. **No.** Changing the Support plan needs IAM permissions, not the root user. Much older material says otherwise.

</details>

## What you'll learn

By the end of this lesson, you can choose the cheapest Support plan that fits a business's needs and defend the choice (objective 12.01a), and translate an old plan name into today's lineup.

Try this before you read on, and guess if you're unsure: a plan lists "under 30 minutes" for a business-critical system that is down. Does AWS promise to fix the problem in 30 minutes?

## The big picture: four steps, each including the one before

![Four steps rise from left to right. Basic, free for every account: cases about your account and bill, quota increase requests, docs and re:Post, some Trusted Advisor checks, the AWS Health Dashboard, and no technical cases. Business Support+, highlighted, from $29 a month: technical cases 24/7, under 30 minutes for a business-critical system down, all Trusted Advisor checks, the Health API. Enterprise Support, from $5,000 a month: a designated Technical Account Manager, under 15 minutes, Well-Architected reviews. Unified Operations, from $50,000 a month: domain specialists, under 5 minutes, 24/7 workload monitoring.](../../images/12-01-plan-ladder.svg)

*Notice the highlighted step. The biggest change in the whole ladder is between Basic and Business Support+: that's where technical help from AWS starts.*

**Long description.** Four steps rise from left to right; each includes everything to its left. Basic: free, on every account; cases about your account and bill; service quota increase requests; documentation, whitepapers and re:Post; some Trusted Advisor checks; the AWS Health Dashboard; no technical cases. Business Support+, highlighted: from $29 a month; technical cases 24/7 by phone, web and chat; under 30 minutes for a business-critical system down; all Trusted Advisor checks; the AWS Health API and Support API; AI help that uses your account's context. Enterprise Support: from $5,000 a month; a designated Technical Account Manager (TAM); under 15 minutes for business-critical cases; Well-Architected reviews; Trusted Advisor Priority; Security Incident Response included. Unified Operations: from $50,000 a month; a TAM plus designated domain specialists; under 5 minutes for critical incidents, from an Incident Management Engineer; 24/7 workload monitoring; critical workload reviews. Prices are monthly minimums as of 2026-10-24. Response times are targets for a first reply.

**AWS Support** is AWS's own help service; the exam guide files it under "customer enablement". A **Support plan** is the level of AWS Support an account subscribes to, and a **support case** is one request for help, opened in AWS Support Center and tracked until it's closed.

## Every account starts on Basic, which answers account questions but not technical ones

**Basic Support** is free and included with every AWS account. It gives you, around the clock ([AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html), checked 2026-10-24):

- **Cases about your account and your bill**, answered by AWS customer service.
- **Service quota increase requests.**
- **Documentation, whitepapers and AWS re:Post**, AWS's community question-and-answer site (lesson 12.03).
- **Some AWS Trusted Advisor checks** and the **AWS Health Dashboard** (lesson 12.02).

What Basic can't do is open a **technical** case. "Our database stopped accepting connections" needs a paid plan ([Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html), checked 2026-10-24).

> **Dated (checked 2026-10-25):** on the Free plan you can't buy a paid Support plan at all. Our Free plan test account's Support Plans page said: "Only Basic Support is available to accounts on the AWS Free Tier plan. To upgrade your support, first upgrade to a Paid plan." Basic is your plan for as long as you stay on the Free plan.

One limit applies to every plan, paid ones included: AWS Support doesn't write your code, debug your own software, or administer or log in to your systems ([AWS Support FAQs](https://aws.amazon.com/premiumsupport/faqs/), checked 2026-10-24). Lesson 12.03 covers hiring someone to do that.

## Each paid plan adds speed and people

**AWS Business Support+** is the first paid plan, and the one AWS calls the minimum it recommends for production workloads. It adds technical cases 24/7 by phone, web and chat, a first reply in under 30 minutes when a business-critical system is down, AI help that uses your account's context, all Trusted Advisor checks, and the AWS Health API and Support API so your own tools can read them.

**AWS Enterprise Support** adds a **Technical Account Manager (TAM)**: a named person at AWS assigned to you, who learns your setup, guides your plans and pulls in specialists. It adds a 15-minute target for business-critical cases, Well-Architected reviews, Trusted Advisor Priority and AWS Security Incident Response ([AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/), checked 2026-10-24).

**AWS Unified Operations** is for mission-critical systems where minutes matter. It adds a 5-minute target for critical incidents, answered by an Incident Management Engineer, 24/7 monitoring of your workloads, and designated Domain Specialist Engineers alongside the TAM ([What is AWS Unified Operations](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-intro.html), checked 2026-10-24).

> **Dated (checked 2026-10-24):** from [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/) and [AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/). Each paid plan costs the greater of its monthly minimum and a percentage of your AWS charges, and the percentage falls as the bill grows. Business Support+ is charged per account. Paid plans are billed monthly with a minimum commitment: 30 days, or 90 days for Unified Operations.
>
> | | Basic | Business Support+ | Enterprise Support | Unified Operations |
> |---|---|---|---|---|
> | **Monthly minimum** | Free | $29 per account | $5,000 | $50,000 |
> | **Technical cases** | No | Yes, 24/7 | Yes, 24/7 | Yes, 24/7 |
> | **Fastest target** | None | Under 30 min | Under 15 min | Under 5 min |
> | **A named person** | No | No | A TAM | A TAM and domain specialists |
> | **Trusted Advisor** | Some checks | All checks | All, plus Priority | All, plus Priority |
> | **AWS Health API** | No | Yes | Yes | Yes |
> | **Security Incident Response** | Not included | Extra fee | Included | Included |

> **Your turn:** a company wants a designated Technical Account Manager and has no need for 5-minute responses. Which is the cheapest plan that fits, and why not the plans on either side?

<details><summary>Model answer</summary>

**Enterprise Support**, the first plan with a designated TAM. Business Support+ has 24/7 engineers but no named TAM. Unified Operations includes a TAM too, but it costs far more and adds 5-minute responses the company doesn't need.

</details>

## Response times are targets for a first reply, not guarantees

When you open a technical case you choose its **case severity**, from "general guidance" to "business-critical system down". Each severity has a **first-response time**: how soon AWS aims to reply for the first time.

On every paid plan, the lower severities share the same targets: under 1 hour for a production system down, 4 hours for a production system impaired, 12 hours for a system impaired and 24 hours for general guidance ([Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html), checked 2026-10-24). Only the business-critical target differs between the paid plans.

### "Response times are guaranteed" is wrong

It's easy to read a plan's response time as a promise of a reply, or even a fix, within that time. That's wrong on two counts. AWS says it will make "every reasonable effort" to respond within the stated times ([Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/), checked 2026-10-24), so they are targets. And they measure the first reply: "under 30 minutes" means a person engages with your case, not that the problem is solved. The belief is tempting because the times sit in a neat table that looks like a contract, and some study material calls them "SLAs". That answers the prequestion: no.

## Older material uses plan names that are being retired

> **Dated (checked 2026-10-24):** Three older plans are being retired ([end of support notice](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html); [AWS Support FAQs](https://aws.amazon.com/premiumsupport/faqs/)):
>
> - **Developer Support** and **Business Support** have taken no new subscriptions since 2025-12-02 and end on 2027-01-01. Existing customers can keep them until then or move to Business Support+. AWS doesn't move them automatically: a Developer Support customer who doesn't choose a new plan falls back to Basic.
> - **Enterprise On-Ramp** ends on 2027-01-01. During 2026, AWS is moving its customers to Enterprise Support automatically.
> - All three stay available in the AWS GovCloud (US) Regions.
> - Enterprise Support continues, with its monthly minimum lowered from $15,000 to $5,000.

### "Developer, Business and Enterprise On-Ramp are current plans" is out of date

You may have studied five plans: Basic, Developer, Business, Enterprise On-Ramp and Enterprise. That was right until AWS replaced the lineup on 2025-12-02; the exam guide now lists the four current plans. The old lineup is easy to trust because so much material predates the change, and AWS's own pages lag: the Shield Response Team page still names "Business Support" (checked 2026-10-24). If a practice question lists only the old plans, translate before you answer: "Developer" or "Business" means today's Business Support+, and "Enterprise On-Ramp" means Enterprise Support.

> **Example:** the bakery's bill has grown to about $1,200 a month in one account (made up), and the site is now most of its sales. On its worst day, the site is down in its busiest week, and Basic can't open a technical case. Business Support+ covers that day with 24/7 engineers, at about $108 a month (9% of the bill, as of 2026-10-24). Enterprise's $5,000 minimum is about 46 times that fee, for a TAM the bakery doesn't need. **Answer:** Business Support+ on the production account, revisited when the business changes.

## Summary

- **Basic is free and on every account,** with account and billing cases but no technical cases. On the Free plan, it's the only plan you can have.
- **Business Support+ adds 24/7 technical cases**, all Trusted Advisor checks and the Health API. **Enterprise Support adds a named TAM.** **Unified Operations adds replies in minutes**, domain specialists and workload monitoring.
- **Response times are targets for a first reply,** not guarantees of a fix.
- **Choose the cheapest plan that covers your worst day,** and move up only for something the next plan adds.
- **Old names:** Developer and Business map to Business Support+, and Enterprise On-Ramp to Enterprise Support; all three end on 2027-01-01.

## Practice

1. **Which is the lowest-cost plan that lets a company open technical support cases at any hour?**

   A. Basic\
   B. Business Support+\
   C. Enterprise Support\
   D. Developer Support

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** Basic can't open technical cases.
   - **C is wrong.** Enterprise Support can, but it costs more and adds things the company didn't ask for.
   - **D is wrong.** Developer Support takes no new subscriptions and ends on 2027-01-01 (as of 2026-10-24).

   </details>

2. **A practice question asks for the cheapest plan with technical support, and its choices are Basic, Developer, Business and Enterprise. How do you answer it today?**

   <details><summary>Feedback</summary>

   **Model answer:** The question uses the old lineup, where the answer was Developer. Developer takes no new customers and ends on 2027-01-01 (as of 2026-10-24); it maps to Business Support+, today's cheapest plan with technical cases.

   </details>

3. **A colleague says, "With Enterprise Support, AWS guarantees a critical outage is fixed within 15 minutes." In two sentences, correct them.**

   <details><summary>Feedback</summary>

   **Model answer:** The 15 minutes is a target for AWS's first reply to a business-critical case, not for the fix. AWS says it makes every reasonable effort to meet it, so it isn't a guarantee either.

   </details>

**Next:** [Tools that watch your account](02-tools-that-watch-your-account.md). To practice choosing, try the optional [Simulation S15](06-sim-support-plan-chooser.md).

## Where to check the current details

- [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/): features and response targets (checked 2026-10-24)
- [AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/): minimums, percentages and terms (checked 2026-10-24)
- [Developer, Business, and Enterprise On-Ramp end of support](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html) (checked 2026-10-24)

---

"Support plans" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
