---
type: lesson
id: clf-09-03
title: "Finding threats and weaknesses"
tasks: ["2.2", "2.4"]
objectives: ["09.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-07-02, clf-04-01, clf-09-01, clf-09-02]
terms_introduced: [threat, vulnerability, finding, CVE, security standard, Amazon GuardDuty, AWS Security Hub CSPM, AWS Security Hub, Amazon Detective, AWS Trusted Advisor, AWS Marketplace]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"
  - "https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"
  - "https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"
  - "https://aws.amazon.com/security-hub/faqs/"
  - "https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html"
---

# Each detection service watches something different, and none of them blocks anything: match the finding to the service

Each security service in this lesson reads something different: activity, installed software, settings or a past finding. Ask what a service looked at, and you can name the one that raised a finding.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Filtering traffic](../07-connecting-it/02-filtering-traffic.md) (Inspector, VPC Flow Logs) and lesson 09.01, [Who did what](01-who-did-what.md) (CloudTrail).

## Warm-up: what you remember

1. From lesson 07.02: Amazon Inspector reports that the web server is reachable from the internet on port 22. Does Inspector close the port?
2. From lesson 04.01: the bakery's web server runs on EC2. Who patches its operating system and the software installed on it?

<details><summary>Feedback</summary>

1. **No.** Inspector finds and reports; the bakery fixes the security group or network ACL rule. Every service in this lesson works the same way.
2. **The bakery.** On EC2, the guest operating system and everything installed on it are the customer's, which is why a scanner that finds missing patches is useful.

</details>

## What you'll learn

By the end of this lesson, you can say what GuardDuty, Inspector, Security Hub, Detective and Trusted Advisor each look at and report, match a finding to the service that raised it (objective 09.03a), and say what AWS Marketplace adds for security.

Try this before you read on, and guess if you're unsure: a report says the web server's credentials were just used from an address outside AWS. Which service raised it?

## The big picture: weaknesses before, threats during, investigation after

A **threat** is someone or something actively trying to cause harm. A **vulnerability** is a weakness an attacker could use, such as an unpatched flaw or an open port. A **finding** is a service's report of one possible problem, naming the resource and how severe the service thinks it is.

![A time line in three columns. Before an attack, is there a hole: Trusted Advisor's best-practice checks and Amazon Inspector's software flaws and network exposure. During, is someone at it now: Amazon GuardDuty's suspicious activity in CloudTrail events, VPC Flow Logs and DNS logs. After, how did it happen: Amazon Detective investigates a finding. Inspector and GuardDuty send findings down to a highlighted band, AWS Security Hub, where the findings meet.](../../images/09-03-before-during-after.svg)

*Notice the subtitle: all of these services report and none of them blocks. Blocking belongs to the filters in lesson 07.02 and the front door in lesson 09.04.*

**Long description.** A time line in three columns. Before an attack, "is there a hole?": AWS Trusted Advisor runs best-practice checks on the account (a few security checks free on Basic Support; results stay in its own console), and Amazon Inspector finds known software flaws and unintended network exposure in EC2 instances, Lambda functions and container images. During, "is someone at it now?": Amazon GuardDuty finds suspicious activity in CloudTrail events, VPC Flow Logs and DNS logs, such as stolen credentials, crypto mining and calls from known bad addresses. After, "how did it happen?": Amazon Detective starts from a GuardDuty finding and investigates it with up to a year of history. Arrows labeled "findings" run from Inspector and GuardDuty to a highlighted band, AWS Security Hub: Security Hub CSPM, the original, checks your settings against standards such as CIS and PCI DSS, collects the other services' findings and scores you; the newer, unified Security Hub correlates them into exposures. A note adds that Macie's findings about sensitive data in S3 arrive there too.

## GuardDuty watches activity and reports threats happening now

**Amazon GuardDuty** is a threat detection service. It reads activity continuously and compares it with threat intelligence (lists of known malicious addresses and domains) and with machine-learning models of normal behavior ([What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), checked 2026-10-24). It starts from three sources as soon as you turn it on, with nothing else to set up: **CloudTrail management events**, **VPC Flow Logs** and **DNS logs**. It catches things like stolen credentials, crypto mining and SSH password guessing. It works per Region.

GuardDuty reports; it doesn't stop anything. You can build an automatic response through Amazon EventBridge, and it sends its findings to Security Hub and Detective.

### Detective explains what happened after a finding

**Amazon Detective** is for the investigation that follows a finding. It collects CloudTrail events and VPC Flow Logs, takes in GuardDuty findings, and links them into a picture of which identities, addresses and resources did what, with up to a year of history ([What is Amazon Detective?](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html), checked 2026-10-24). GuardDuty *detects*; Detective *investigates* the root cause and scope.

## Inspector scans workloads and reports weaknesses before an attacker finds them

**Amazon Inspector** is a vulnerability management service. It finds EC2 instances, Lambda functions and container images in Amazon ECR on its own, and scans them for known software flaws (**CVEs**, the public, numbered entries for known flaws) and for unintended network paths from the internet ([What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html), checked 2026-10-24). It rescans whenever software changes or a new CVE is published; you never schedule a scan.

Both Inspector and GuardDuty raise findings about EC2 instances. Inspector reads what is *installed and reachable* and says "this could be attacked". GuardDuty reads what is *happening* and says "this looks like an attack".

### "Create an assessment template and install the Inspector agent" is out of date

You may read that you use Inspector by choosing an **assessment template**, installing the Inspector agent and scheduling runs. That describes **Amazon Inspector Classic**, which AWS shut down on 2026-05-20 ([Services in full shutdown](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html), checked 2026-10-24). Today's Inspector discovers and scans resources with no templates or schedules, and has no separate agent. The old wording is tempting because much study material predates the rebuild, and the service kept its name.

## Security Hub gathers every finding and checks your settings, and the name now covers two products

In exam terms, **AWS Security Hub** is "one place for all security findings, plus automatic checks of your settings against standards". A **security standard** is a published list of recommended settings, such as the [CIS AWS Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services) or PCI DSS for card payments. The product that does this job is now called **AWS Security Hub CSPM** (cloud security posture management) ([Introduction to AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), checked 2026-10-24):

- **It checks your settings** against standards such as AWS Foundational Security Best Practices, CIS, PCI DSS and NIST, and scores the results.
- **It collects findings** from GuardDuty, Inspector, Macie and partner products into one format, across accounts.
- **It needs AWS Config** recording, because most of its checks run as Config rules.

### "Security Hub is one product" is no longer right

You may read that Security Hub is a single service. It isn't any more: the original is now Security Hub CSPM, and the name **AWS Security Hub** belongs to a newer, unified product that correlates signals from Security Hub CSPM, GuardDuty, Inspector and Macie into combined risks ([Security Hub FAQs](https://aws.amazon.com/security-hub/faqs/), checked 2026-10-24). It's tempting because the exam guide still says only "AWS Security Hub". For the exam, "one place for findings" or "check against CIS or PCI DSS" means Security Hub.

## Trusted Advisor is a first look at your settings, with a few security checks free

**AWS Trusted Advisor** inspects your account and recommends changes against AWS's best practices, in six categories: cost optimization, performance, security, fault tolerance, service limits and operational excellence ([check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html), checked 2026-10-24). You may read that it has five; that's wrong now, and it's tempting because much study material still lists five. **Basic Support** gets all service limit checks and selected security checks, such as MFA on the root user and security groups with ports open to everyone; Business Support+, Enterprise and Unified Operations get all checks ([AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)). Module 12 covers it in full.

Trusted Advisor, Security Hub CSPM and Inspector all "check", which makes them easy to confuse. What separates them is what they compare against: AWS's own best practices, named standards, or published CVEs and open paths.

### AWS Marketplace sells third-party security products, billed through AWS

**AWS Marketplace** is a curated catalog where you find, buy and deploy software from other companies, including security products such as firewalls and ready-made rule groups for AWS WAF. Charges appear on your AWS bill ([What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html), checked 2026-10-24). A product bought there is still yours to configure and run.

## Match a finding to its service by asking what it looked at

| Service | Looks at | Reports | Exam clue |
|---|---|---|---|
| **GuardDuty** | Activity: CloudTrail events, VPC Flow Logs, DNS logs | Threats happening now | "malicious activity", "compromised credentials" |
| **Inspector** | Installed software and network paths of EC2, Lambda and container images | Vulnerabilities and exposure | "CVE", "unpatched" |
| **Macie** (09.02) | Contents and settings of S3 buckets | Sensitive data; risky bucket settings | "personal data in S3" |
| **Security Hub (CSPM)** | Your settings, plus everyone's findings | Failed controls; all findings in one place | "single place", "CIS", "PCI DSS" |
| **Detective** | A year of activity linked to a finding | Root cause and scope | "investigate", "root cause" |
| **Trusted Advisor** | Your account against AWS best practices | Recommendations in six categories | "best-practice checks", "Support plan" |

> **Your turn:** Answer the prequestion, then this. GuardDuty reports that the web server's credentials were used outside AWS. The owner asks: "How did they get the credentials, and what else did they do?" and "Was there a known hole in the server?" Name the service for each.

<details><summary>Model answer</summary>

The prequestion's finding came from **GuardDuty**: it's activity, seen in CloudTrail events. "How, and what else?" is **Detective**, which links the finding to a year of CloudTrail and flow-log activity. "Was there a known hole?" is **Inspector**, whose findings would show an unpatched package or an open path on the server.

</details>

## Summary

- **GuardDuty reports threats happening now,** from CloudTrail events, VPC Flow Logs and DNS logs; **Detective** investigates a finding's root cause.
- **Inspector reports weaknesses:** CVEs and open network paths on EC2, Lambda and container images, scanned continuously. Assessment templates belong to Inspector Classic, shut down on 2026-05-20.
- **Security Hub** (today's Security Hub CSPM) checks settings against standards and collects every service's findings; it needs AWS Config.
- **Trusted Advisor** checks your account against AWS best practices in six categories; **AWS Marketplace** sells third-party security products. None of these services blocks anything.

## Practice

1. **Which service continuously scans EC2 instances and container images for software vulnerabilities?**

   A. Amazon GuardDuty\
   B. Amazon Inspector\
   C. Amazon Detective\
   D. AWS Shield

   <details><summary>Feedback</summary>

   **B is right.** Inspector discovers workloads and rescans them as software and published CVEs change.

   - **A is wrong.** GuardDuty watches activity for threats; it doesn't inventory installed software.
   - **C is wrong.** Detective investigates findings after the fact.
   - **D is wrong.** Shield protects against DDoS attacks (lesson 09.04).

   </details>

2. **A company wants to check all of its accounts' settings against the [CIS AWS Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services) and see a score. Which service fits?**

   A. AWS Security Hub\
   B. Amazon GuardDuty\
   C. AWS Audit Manager\
   D. Amazon Macie

   <details><summary>Feedback</summary>

   **A is right.** Security Hub, specifically Security Hub CSPM today, runs a CIS standard and scores the results.

   - **B is wrong.** GuardDuty finds threats in activity, not settings that fail a standard.
   - **C is wrong.** Audit Manager is closed to new customers; treat it as a distractor.
   - **D is wrong.** Macie finds sensitive data in S3.

   </details>

3. **GuardDuty raised a high-severity finding about an IAM role. The security lead wants to see everything that role did over the past month and what it touched. Which service is built for this?**

   A. Amazon Detective\
   B. Amazon Inspector\
   C. AWS Trusted Advisor\
   D. AWS Marketplace

   <details><summary>Feedback</summary>

   **A is right.** Detective links the finding to CloudTrail and flow-log activity, with up to a year of history.

   - **B is wrong.** Inspector scans software and network paths; it doesn't trace a role's activity.
   - **C is wrong.** Trusted Advisor checks settings against best practices.
   - **D is wrong.** Marketplace is a catalog of third-party products.

   </details>

**Next:** [The front door](04-the-front-door.md), where you choose the protections that do block. To practice matching findings, try [Simulation S9](08-sim-security-findings-tour.md).

## Where to check the current details

- [What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) and [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) (checked 2026-10-24)
- [Security Hub FAQs](https://aws.amazon.com/security-hub/faqs/) (checked 2026-10-24)
- [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) (checked 2026-10-24)

---

"Finding threats and weaknesses" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
