---
type: lesson
id: clf-09-01
title: "Who did what, how it runs, how it was set"
tasks: ["2.2"]
objectives: ["09.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-08-03, clf-04-04, clf-07-02, clf-02-06]
terms_introduced: [CloudTrail event, multi-Region trail, AWS Config, configuration item, Config rule, noncompliant, conformance pack, access reports, last accessed information, credential report, AWS Audit Manager]
pillars: [security, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/delete-config-data-with-retention-period.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html"
  - "https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html"
---

# CloudTrail says who did what, CloudWatch how it runs, Config how it was set: answer each audit question from the record that holds the answer

AWS keeps several records of your account, and each answers a different kind of question. Name the kind of question first, and the service follows.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Watching workloads](../08-building-and-operating/03-watching-workloads.md) (CloudWatch, CloudTrail's management and data events) and [Policies and least privilege](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md). The auditor's visit is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From lesson 08.03: the bakery's owner was emailed when order functions started failing. Which service watched the error count and raised the alarm?
2. From lesson 04.03: how did you check whether anyone had used your root user recently, and how far back could you look?

<details><summary>Feedback</summary>

1. **Amazon CloudWatch.** An alarm watched the functions' error metric and, through an Amazon SNS topic, sent the email. CloudWatch watches how things run.
2. **CloudTrail Event history, filtered by user name `root`.** It shows the last 90 days of activity, one Region at a time.

</details>

## What you'll learn

By the end of this lesson, you can say what CloudTrail, CloudWatch, AWS Config and IAM's access reports each record, say where AWS's security logs are kept, and choose the record that answers an audit question (objective 09.01a).

Try this before you read on, and guess if you're unsure: the auditor asks, "Was SSH open to the internet on your web server on March 1?" CloudTrail, CloudWatch or Config?

## The big picture: four records, four questions

Most wrong answers on this topic come from asking the right question of the wrong record.

| Record | Question it answers | On from day one? |
|---|---|---|
| **AWS CloudTrail** | Who did what, when, and from where? | Event history: 90 days, per Region, free |
| **Amazon CloudWatch** | How is it running? | Basic metrics from AWS services |
| **AWS Config** | How was it set up, then and now, and is that allowed? | No: you turn on recording, and pay per item |
| **IAM access reports** | Who can do what, and do they still use it? | Yes, free in the IAM console |

## CloudTrail records who did what, when and from where

**AWS CloudTrail** records the actions taken in your account, by people, by roles and by AWS services acting for you, whether they came from the console, the CLI, an SDK or an API call. Each **CloudTrail event** says who acted, which action, on which resource, when, and from which IP address ([How CloudTrail works](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html), checked 2026-10-24).

- **Event history** is on in every account from the day it's created. It holds the last **90 days** of management events, **per Region**, can't be edited, and costs nothing to view.
- **A trail** delivers events as log files to an S3 bucket, and the files stay as long as you keep them, so a trail is how you keep more than 90 days. AWS recommends a **multi-Region trail**, which covers every Region enabled in your account. Your first copy of management events costs nothing from CloudTrail; you pay for the S3 storage.
- **Data events**, such as reading an object in S3, aren't recorded by default. You turn them on per resource, for a charge.

So CloudTrail isn't a complete, permanent record. With no trail, nothing older than 90 days exists, and by default it shows who *changed* the photo bucket's settings but not who *downloaded* each photo.

## AWS Config records how each resource was set, and judges it against your rules

**AWS Config** keeps an inventory of your resources and a history of their settings. Each time a resource changes, Config records a **configuration item**: a snapshot of its settings at that moment, linked to the CloudTrail event that caused the change ([What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), checked 2026-10-24).

- **Recording is off until you turn it on,** and you pay per item recorded.
- **Config rules** check each resource against a setting you want, such as the AWS managed rule `restricted-ssh`, which fails any security group that lets SSH in from anywhere. A resource that fails is marked **noncompliant**. Config reports; it fixes nothing unless you attach a fix.
- **Conformance packs** bundle many rules into one unit you deploy and report on together.
- **History is kept for 7 years by default** (2,557 days), but only from the day recording started.

That answers the prequestion: "was SSH open on March 1?" asks about a state, so it's **Config**, if it was recording then. "Who opened it?" would be CloudTrail, which Config links to.

### CloudWatch shows how things are running, not who changed them

**Amazon CloudWatch** (Module 08) collects **metrics**, **logs** and **alarms**. It can show *that* the web server was overloaded at 6 p.m.; it can't show *who* changed a setting. Its log groups keep logs indefinitely until you set a retention period.

The figure follows one change through all three services:

![One security group change at 14:02 seen three ways: CloudTrail names the user, time and address; Config shows web-sg's settings before and after and the restricted-ssh rule turning noncompliant; CloudWatch shows failed SSH sign-ins rising afterward.](../../images/09-01-one-change-three-views.svg)

*Notice that no single row tells the whole story. CloudTrail names the person, Config shows the before and after and flags the breach, and CloudWatch shows the consequence.*

**Long description.** A time line for Tuesday from 12:00 to 17:00, with a dashed marker at 14:02, when someone adds a rule to the security group `web-sg` allowing SSH, port 22, from anywhere. Three rows. CloudTrail, which answers who, what, when and where: one event, `AuthorizeSecurityGroupIngress`, by user `sam-dev` at 14:02:11 UTC, from address 198.51.100.23, on `web-sg`, port 22, from `0.0.0.0/0`. Config, which answers what it looked like and whether it's allowed: before 14:02, `web-sg` allowed 443 from anywhere and the rule `restricted-ssh` was compliant; from 14:02, it allows 443 and 22 from anywhere, and the rule is noncompliant. CloudWatch, which answers how it's behaving: a bar chart of failed SSH sign-ins on the web server per 15 minutes, from the server's own log sent to CloudWatch Logs by the agent; zero before the change, then rising to about 40 per 15 minutes within an hour. A note says the failed sign-ins appear only if the bakery sends the server's log to CloudWatch.

### "Audit Manager is the compliance answer" is out of date

Older material names **AWS Audit Manager**, a service that gathers evidence against frameworks such as PCI DSS, as the answer for audits. Since 2026-04-30 it can't be set up in new accounts, and AWS points to Config conformance packs instead ([Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html), checked 2026-10-24). It's tempting because the name says "audit"; treat it as a wrong answer. Lesson 09.05 covers where compliance reports come from.

> **Your turn:** Name the record for each question. (a) Which user deleted the old photo bucket last month? (b) Are any EBS volumes unencrypted right now? (c) Email the owner when the database's storage is nearly full. (d) What did the database's security group allow on September 1? (e) Who downloaded `lemon-tart.jpg` from the photo bucket yesterday?

<details><summary>Model answer</summary>

(a) **CloudTrail**: deleting a bucket is a management event, in Event history if it's within 90 days. (b) **AWS Config**, with a rule that checks volume encryption. (c) **CloudWatch**: a metric and an alarm. (d) **AWS Config**, if it was recording on that date; CloudTrail shows changes, not the state. (e) **None by default.** A download is a data event, which a trail records only if you turned data events on *before* the download; S3 server access logs are the other way. Evidence you didn't collect doesn't exist.

</details>

## Access reports show who can do what, and whether they still use it

Task [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) names **access reports** for reporting. They're IAM's reports on who can use what, and whether they have:

- **Last accessed information:** on the **Last Accessed** tab of any IAM user, group, role or policy, which services it's allowed to use and when it last tried each one. Service information covers at least the last 400 days ([Refine permissions using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html), checked 2026-10-24). Use it to remove permissions nobody uses. It reports attempts, not successes, and covers identity-based policies only.
- **The credential report:** a CSV file listing every IAM user and the state of their credentials: password and its last use, whether MFA is on, and when each access key was last rotated and used ([Generate credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)).
- **The AWS Organizations access report:** the same idea for each account in an organization (lesson 09.05).

### Security logs end up in an S3 bucket or CloudWatch Logs

The exam asks where security logs are captured and kept. Nearly all of them land in one of two places, and several are off until you turn them on:

| Log | Lands in | On by default? |
|---|---|---|
| CloudTrail trail | S3 bucket (optionally CloudWatch Logs too) | No; Event history's 90 days are |
| VPC Flow Logs | CloudWatch Logs or S3 | No |
| Lambda function logs | CloudWatch Logs | Yes |
| EC2 operating system and app logs | CloudWatch Logs, through the CloudWatch agent | No |
| S3 server access logs, load balancer access logs | S3 bucket | No |
| AWS Config history | Config itself, with snapshots to S3 | No |

## Summary

- **Four records, four questions.** CloudTrail: who did what, when, from where. CloudWatch: how it's running. Config: how it was set, and is that allowed. IAM access reports: who can do what, and do they use it.
- **CloudTrail** keeps 90 days of management events per Region for free; a trail keeps more, in S3. Data events are off by default.
- **AWS Config** records settings over time and marks resources noncompliant against rules. It's off until you turn it on. Audit Manager is closed to new customers.
- **Security logs end up in S3 or CloudWatch Logs.** AWS runs these services; turning them on, and keeping the logs, is your side of the line.

## Practice

1. **An auditor asks which IAM user deleted a security group three weeks ago. Which service answers this?**

   A. Amazon CloudWatch\
   B. AWS CloudTrail\
   C. AWS Config\
   D. IAM last accessed information

   <details><summary>Feedback</summary>

   **B is right.** Deleting a security group is an action, and three weeks is inside Event history's 90 days.

   - **A is wrong.** CloudWatch measures how resources run; it doesn't name who acted.
   - **C is wrong.** Config records that the group disappeared and links to the CloudTrail event, but the name comes from CloudTrail.
   - **D is wrong.** It shows when an identity last used a service, not which action it took on which resource.

   </details>

2. **A company must show, at any moment, which of its resources break its internal rules, such as "no unencrypted disks". Which service fits best?**

   A. AWS Config, with rules\
   B. AWS CloudTrail, with a trail\
   C. Amazon CloudWatch dashboards\
   D. AWS Audit Manager

   <details><summary>Feedback</summary>

   **A is right.** Config rules mark each resource compliant or noncompliant as its settings change.

   - **B is wrong.** CloudTrail records actions, not whether today's settings follow a rule.
   - **C is wrong.** Dashboards show metrics and logs, not configuration compliance.
   - **D is wrong.** Audit Manager has been closed to new customers since 2026-04-30; AWS points to Config conformance packs.

   </details>

3. **The auditor asks which staff accounts have a password but no MFA. Which report answers this?**

   A. The IAM credential report\
   B. CloudTrail Event history\
   C. AWS Config's configuration history\
   D. CloudWatch Logs

   <details><summary>Feedback</summary>

   **A is right.** It lists every IAM user with password and MFA status in one file.

   - **B is wrong.** Event history lists actions, not each user's credential settings.
   - **C is wrong.** Config records resource settings, not a report of every user's credentials.
   - **D is wrong.** Log groups hold lines that software writes, not credential status.

   </details>

**Next:** [Encryption](02-encryption.md). To answer the auditor in your own account, do [Lab 12](07-lab-12-answer-the-auditor.md).

## Where to check the current details

- [How CloudTrail works](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html) (checked 2026-10-24)
- [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) (checked 2026-10-24)
- [Refine permissions using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) (checked 2026-10-24)

---

"Who did what, how it runs, how it was set" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
