---
type: lesson
id: clf-12-03
title: "Where to find answers and who can help"
tasks: ["4.3", "2.4", "3.8"]
objectives: ["12.03a", "12.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 11, the guardrails primer and lessons 12.01 and 12.02; about 20 minutes; works on a phone"
prerequisites: [clf-12-01, clf-12-02, clf-09-00]
terms_introduced: [AWS documentation, AWS whitepapers, AWS blogs, AWS re:Post, AWS Knowledge Center, AWS Prescriptive Guidance, abuse, AWS Trust & Safety team, AWS solutions architect, AWS Professional Services, AWS Partner, AWS Partner Network (APN), independent software vendor (ISV), system integrator, private offer, Private Marketplace, entitlement, AWS License Manager]
pillars: [operational-excellence, security, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/"
  - "https://aws.amazon.com/whitepapers/"
  - "https://repost.aws/knowledge-center"
  - "https://aws.amazon.com/prescriptive-guidance/"
  - "https://repost.aws/knowledge-center/report-aws-abuse"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html"
  - "https://aws.amazon.com/blogs/training-and-certification/engaging-a-solutions-architect/"
  - "https://aws.amazon.com/professional-services/"
  - "https://aws.amazon.com/partners/"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-marketplace-current.html"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/managing-licenses.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
---

# Send each question where it can be answered, and pay people only for work you can't do yourself

AWS's free pages answer most questions, abuse goes to AWS Trust & Safety, and only questions about your own account need a support case. When you need people, solutions architects advise for free, while AWS Professional Services and AWS Partners do the work for a fee; AWS Marketplace sells partners' products on your AWS bill.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** read [Support plans](01-support-plans.md) and [Tools that watch your account](02-tools-that-watch-your-account.md) first. [Module 09](../09-protecting-and-governing/00-brief.md) introduced AWS Marketplace and AWS's security pages.

## Warm-up: what you remember

1. From Module 09: the bakery buys a firewall product through AWS Marketplace. Who configures it?

<details><summary>Feedback</summary>

1. **The bakery.** Buying through Marketplace changes whom you pay, not who configures the product. The same holds for every kind of paid help in this lesson: hiring someone changes who does a task, not whose responsibility it is.

</details>

## What you'll learn

By the end of this lesson, you can route a question to the source that can answer it (objective 12.03a), and choose the right kind of paid help: a solutions architect, AWS Professional Services, an AWS Partner or AWS Marketplace (objective 12.04a).

Try this before you read on, and guess if you're unsure: a server at an address that belongs to AWS keeps trying passwords on the bakery's order page. Should the bakery open a support case?

## AWS's free pages answer "how does this work?"

These sources are public and the same for every customer, so they answer general questions, never "what's wrong with *my* account?":

| Source | What you find there | Use it for |
|---|---|---|
| [AWS documentation](https://docs.aws.amazon.com/) | User guides, API and CLI references, tutorials for each service | How a service behaves, its limits, exact steps |
| [AWS whitepapers](https://aws.amazon.com/whitepapers/) | Longer papers on one topic, such as the Well-Architected Framework | Concepts and best practice across services |
| **AWS blogs**, such as the AWS News Blog and AWS Security Blog | Dated posts | What's new, and walk-throughs of a feature |
| **AWS re:Post** | AWS's public question-and-answer site: anyone asks, and the community, AWS staff and experts answer | An unusual problem nobody has written up |
| [AWS Knowledge Center](https://repost.aws/knowledge-center) | AWS's own articles on the questions customers ask most, published on re:Post | A common problem, fixed step by step |
| [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) | Guides for planning and patterns with hands-on steps, from AWS experts | A bigger job: a migration, a modernization, a security setup |

Module 09 added the security sources: the AWS Security Center for AWS's security services and approach, and the Security Blog and Knowledge Center for how-to.

The **Knowledge Center is part of re:Post**, not a separate site: AWS writes its articles, while community answers vary in quality. **Prescriptive Guidance** is for "we want to…" jobs across several services, while the documentation answers "how do I…?" for one service. All of it is free on every plan, Basic included; paid plans only get prioritized responses on re:Post ([Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/), checked 2026-10-24). re:Post is public, so never post keys, passwords or customer details there.

**Check the date on everything.** Some whitepapers that study material still quotes, such as *How AWS Pricing Works*, now carry AWS's banner "for historical reference only" (checked 2026-10-23). When a whitepaper or blog post disagrees with the current documentation, trust the documentation.

## Abuse from an AWS address goes to AWS Trust & Safety, not to Support

**Abuse** here means someone using an AWS resource to harm others: spam, port scans, login floods, denial-of-service attacks, or hosting illegal or copied content. The **AWS Trust & Safety team** handles reports of it. You report through AWS's abuse form, with evidence: the address that was attacked, the time with its time zone, and log lines; for content, its URL ([Report abuse of AWS resources](https://repost.aws/knowledge-center/report-aws-abuse), checked 2026-10-24). Trust & Safety deals with the resource's owner, and shares details about it only with the owner's permission. AWS publishes its IP address ranges, so you can check that an address is AWS's.

### "Abuse goes to AWS Support" is wrong

It's natural to assume you open a support case to report an attack from an AWS address, because Support is the AWS contact most people know. You don't: AWS's article says AWS Support can't help with abuse reports, on any plan. The difference is whose resource is misbehaving. Someone else's resource harming you goes to Trust & Safety. An intruder inside *your own* account is a support case, opened from that account and marked as an urgent security incident ([Security incident response and resources](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html), checked 2026-10-24). Either way, reporting doesn't protect your site: blocking the traffic stays your job (Module 07 and Module 09). That answers the prequestion: no support case.

## When you need people, ask who does the work

Four kinds of human help are easy to mix up. The question that sorts them is whether you want advice or want the work done:

| | Part of AWS? | What they do | Do the hands-on work? | Cost |
|---|---|---|---|---|
| **AWS Support** | Yes | Fix problems with AWS services and your account (lesson 12.01) | No: they don't write your code or run your systems | Your Support plan |
| **AWS solutions architects** | Yes | Advise on design and run Well-Architected reviews; reached through your account team or AWS's contact form | No: they point you to people who build | No charge |
| **AWS Professional Services** | Yes | AWS's own consulting organization: designs, builds, migrates and manages workloads | Yes, on a project you hire it for | A paid contract |
| **AWS Partners** | No | Other companies in the **AWS Partner Network (APN)** that sell software or services | Yes, for services partners | The partner's prices |

Sources: [Engaging an AWS Solutions Architect](https://aws.amazon.com/blogs/training-and-certification/engaging-a-solutions-architect/) (AWS blog, 2024-12-19) and [AWS Professional Services](https://aws.amazon.com/professional-services/), checked 2026-10-24.

The exam names two kinds of partner: **independent software vendors (ISVs)**, which make software that runs on or works with AWS, and **system integrators**, which design, build and connect systems for customers. Some partners also run a customer's systems day to day.

**What partners get from joining** the APN, which is free ([AWS Partner Network](https://aws.amazon.com/partners/), checked 2026-10-24): partner training and certification, partner events, the chance to sell through AWS Marketplace and alongside AWS's sales teams, and programs and incentives. The exam guide also names partner volume discounts; AWS publishes no discount levels, so learn the idea without a figure. One more name appears as a wrong answer: **AWS Managed Services (AMS)**, which the exam guide lists as out of scope.

> **Warning:** on AWS's Free plan, creating a Professional Services contract or joining the AWS Partner Network upgrades the account to the Paid plan automatically ([Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), checked 2026-10-24). Don't sign up from your lab account.

## AWS Marketplace sells partners' products, with three services for buyers

**AWS Marketplace** is a curated catalog of third-party software, data and services, from ISVs and other partners. Pricing can be free, hourly, monthly, annual or bring your own license (BYOL), and the charges arrive on your AWS bill. A buyer can take the public price or a **private offer** negotiated for that buyer ([What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html), checked 2026-10-24). The exam names three things it does for buyers, which matter most for a company with many accounts:

| Service | What it does |
|---|---|
| **Cost management** | A Procurement insights dashboard shows Marketplace spending across the organization's accounts, and cost allocation tags split it by team in Cost Explorer |
| **Governance** | **Private Marketplace** gives each part of the organization a catalog of approved products. It blocks new subscriptions to anything else, but doesn't control what can be deployed ([Private Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-marketplace-current.html)) |
| **Entitlement** | Your **entitlement** is your right to use what you bought. Subscribing creates licenses, which **AWS License Manager** can share with the organization's other accounts and track ([Managing licenses](https://docs.aws.amazon.com/marketplace/latest/buyerguide/managing-licenses.html)) |

> **Your turn:** route four of the bakery's requests. (a) "How do we make the photo bucket delete old versions?" (b) "Check our design before our busiest week; we have no budget for consultants." (c) "Move the head office's servers to AWS in three months." (d) "Staff may buy only the backup product we approved."

<details><summary>Model answer</summary>

(a) **The S3 documentation and the Knowledge Center**, then re:Post if nothing fits: a general how-to. (b) **A solutions architect**, at no charge, with the free Well-Architected Tool. (c) **AWS Professional Services or a system integrator**, hired for the project. (d) **Private Marketplace**, the governance service; IAM permissions still control what can be deployed.

</details>

## Summary

- **Documentation, whitepapers and blogs** explain how AWS works; check dates. **re:Post** is the public Q&A site, and the **Knowledge Center** is AWS's official articles inside it. **Prescriptive Guidance** is for planning and building bigger jobs.
- **Abuse from an AWS resource goes to AWS Trust & Safety** through the abuse form, not to AWS Support. An intruder in your own account is a support case.
- **Solutions architects advise for free; Professional Services (AWS) and partners (other companies) do the work for a fee.** Support fixes problems with AWS, not your code.
- **ISVs sell software, system integrators sell services;** partners get training, events, selling with AWS, and programs.
- **AWS Marketplace** sells third-party products on your AWS bill, with cost management, governance (Private Marketplace) and entitlement (License Manager).

## Practice

1. **Which source holds AWS's official articles on the questions customers ask most often?**

   A. AWS Prescriptive Guidance\
   B. AWS Knowledge Center\
   C. AWS Support Center\
   D. AWS Trust & Safety

   <details><summary>Feedback</summary>

   **B is right.** The Knowledge Center, on re:Post, collects AWS-written answers to common questions.

   - **A is wrong.** Prescriptive Guidance offers guides and patterns for planning and building.
   - **C is wrong.** Support Center is where you open cases about your own account.
   - **D is wrong.** Trust & Safety handles abuse reports.

   </details>

2. **A website owner's logs show a port scan from an address in AWS's published IP ranges. Which TWO steps are right?**

   A. Report it to AWS Trust & Safety through the abuse form, with timestamps and log samples\
   B. Open an account and billing case in Support Center\
   C. Block the address with the owner's own firewall rules\
   D. Ask on re:Post who owns the address\
   E. Wait for the AWS Health Dashboard to show the event

   <details><summary>Feedback</summary>

   **A and C are right.** Trust & Safety acts on the resource's owner; the website owner protects its own site meanwhile.

   - **B is wrong.** AWS Support can't help with abuse reports.
   - **D is wrong.** re:Post is public, and nobody there can act on another customer's resource.
   - **E is wrong.** AWS Health reports AWS's events, not other customers' attacks.

   </details>

3. **Which option gives a company AWS's own experts to carry out a migration project under a contract?**

   A. AWS Support\
   B. AWS Professional Services\
   C. An AWS solutions architect\
   D. AWS Marketplace

   <details><summary>Feedback</summary>

   **B is right.** Professional Services is AWS's consulting organization.

   - **A is wrong.** Support helps with problems using AWS services; it doesn't run projects.
   - **C is wrong.** A solutions architect advises at no charge but doesn't do the build.
   - **D is wrong.** Marketplace sells products, mostly from other companies.

   </details>

**Next:** see these places for yourself in [Lab 17](05-lab-17-support-center-tour.md), then practice the plan choice in [Simulation S15](06-sim-support-plan-chooser.md).

## Where to check the current details

- [AWS re:Post Knowledge Center](https://repost.aws/knowledge-center) and [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) (checked 2026-10-24)
- [Report abuse of AWS resources](https://repost.aws/knowledge-center/report-aws-abuse) (checked 2026-10-24)
- [What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html), AWS Marketplace Buyer Guide (checked 2026-10-24)

---

"Where to find answers and who can help" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
