---
type: lesson
id: clf-00-04
title: "AWS changes fast"
tasks: []
objectives: ["00.04a"]
reader: "Adult studying alone, possibly new to IT; about 10 minutes; works on a phone"
prerequisites: ["clf-00-01"]
terms_introduced: [closed to new customers, end of support, shut down, exam name, current name]
pillars: []
facts_checked: 2026-10-23
sources:
  - "https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html"
  - "https://aws.amazon.com/free/"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# AWS is a moving target, so this guide dates its facts and teaches both old and new names

AWS renames services, closes some, and changes its plans and console all the time. This guide dates every fact that changes and gives both the exam's name and today's name. By the end of this page you can recognize out-of-date material and know where to check (objective 00.04a).

**For:** an adult studying alone, possibly new to IT. **Time:** about 10 minutes. Don't worry if most service names below mean nothing yet; the modules teach them. Here, notice the pattern.

## Three words for a service on its way out

AWS lists the services and features it is retiring on [AWS lifecycle changes](https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html), in three stages:

- **Closed to new customers:** existing customers keep using it; a new account can't sign up. The guide teaches it while the exam lists it, but never uses it in a lab.
- **End of support:** a date is set, often about a year ahead.
- **Shut down:** the service is gone. The guide mentions it only so you can reject it as a wrong answer.

## The exam's name and today's name

AWS revised the CLF-C02 exam guide in 2026 without changing the exam code, and we can't confirm from which date live questions use the new wording ([exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), compared with archived copies, 2026-10-23). So at its first mention in each module, a service gets its **exam name**, then its **current name**: "Amazon AppStream 2.0 (now Amazon WorkSpaces Applications)". Questions use the exam's name; labs use today's, as the console does.

## Changes you'll meet in older material

The most common, as of 2026-10-23. [Exam names and current names](../99-reference/02-names-exam-vs-current.md) has the full list, including renames such as AWS Single Sign-On to IAM Identity Center.

| Older material says | Today |
|---|---|
| Support plans: Basic, Developer, Business, Enterprise On-Ramp, Enterprise | [Basic, Business Support+, Enterprise and Unified Operations](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html), since 2025-12-02. Developer and Business take no new customers; all three old paid plans end on 2027-01-01 |
| The Free Tier: 12 months free | [Credits](https://aws.amazon.com/free/) ($100, plus up to $100 more) and a Free plan lasting up to 6 months or until the credits run out, or a Paid plan |
| Changing your Support plan needs the root user | No longer a [root-only task](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) |
| Amazon AppStream 2.0, Amazon Connect, AWS Application Migration Service (still the exam's names) | [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html), [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html), [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) |
| AWS Snowball for moving large amounts of data | [Closed to new customers](https://aws.amazon.com/snowball/) since 2025-11-07; support ends 2026-12-31; removed from the exam guide |
| AWS OpsWorks, AWS CodeStar, AWS Snowmobile, AWS Cloud9, AWS IQ | [Shut down](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) in 2024 (Snowmobile on 2024-03-14, CodeStar on 2024-07-25); Cloud9 closed to new customers; [AWS IQ](https://aws.amazon.com/iq/) discontinued on 2026-05-28 (AWS's lifecycle list says 2026-05-20) |

When a fact might have changed, check the service's "What is …?" page, the lifecycle list, the exam guide and [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/). If a screen or price differs from this guide, trust the live AWS page.

> **Your turn:** A practice question asks which Support plan a small company should choose, and its four answer choices are Basic, Developer, Business and Enterprise On-Ramp. Using the table, say what is wrong with the question.

<details><summary>Model answer</summary>

Three of the four choices are retiring plans: Developer and Business take no new customers, and all three end on 2027-01-01. Today's plans are Basic, Business Support+, Enterprise and Unified Operations, so treat the question as out of date. Module 12 teaches the current plans.

</details>

**Next:** [Before your first lab](05-before-your-first-lab.md).

---

"AWS changes fast" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
