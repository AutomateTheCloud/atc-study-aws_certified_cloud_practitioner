---
type: sim
id: clf-09-08
title: "Simulation S9: Match security findings to the service that raised them"
tasks: ["2.2", "2.4"]
objectives: ["09.03a"]
reader: "Adult studying alone, possibly new to IT, who has read lesson 09.03; about 20 minutes"
prerequisites: ["clf-09-03", "clf-07-02", "clf-05-02"]
terms_introduced: [finding type, severity]
pillars: [security]
lab: "S9"
rung: L2
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "20 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"
  - "https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html"
  - "https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"
  - "https://docs.aws.amazon.com/inspector/latest/user/findings-types.html"
  - "https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html"
  - "https://docs.aws.amazon.com/macie/latest/user/findings-types.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html"
  - "https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html"
  - "https://aws.amazon.com/security-hub/faqs/"
  - "https://aws.amazon.com/free/security/"
---

# Simulation S9: A morning of security findings: match each one to the service that raised it

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4).

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [09.03 Finding threats and weaknesses](03-finding-threats-and-weaknesses.md). **Time:** about 20 minutes. **Cost:** $0; no AWS account is used.

**Why a simulation:** in our Free plan test account on 2026-10-23, Amazon GuardDuty and AWS Security Hub CSPM each opened a page headed "Free account plan access limitations" with an **Upgrade plan** button, and no trial. Amazon Inspector and Amazon Macie have free trials, but AWS lists them as Paid plan offers, and after a trial each service bills (as of 2026-10-24, [free security trials](https://aws.amazon.com/free/security/)).

**Goal:** overnight, the bakery's security services raised eight findings. You name the service behind each and answer two questions from the owner. **End state:** eight matches and two short answers in your notes.

## The rules of this simulation

A **finding** is a service's report of one possible problem. Each has a **finding type**, a name for the kind of problem, and a **severity**, the service's estimate of how urgent it is, such as Low, Medium, High or Critical. The four services look at different things:

| Service | Reads | Reports | On our Free plan account (2026-10-23) |
|---|---|---|---|
| Amazon GuardDuty | CloudTrail management events, VPC Flow Logs, DNS logs | Threats: malicious or suspicious activity | Blocked |
| Amazon Inspector | Software packages and network paths of EC2 instances, container images in Amazon ECR, Lambda functions | Vulnerabilities and network exposure | Trial not included |
| Amazon Macie | Objects and settings in S3 buckets | Sensitive data; bucket settings that weaken security | Trial not included |
| AWS Security Hub CSPM | Your account's settings, using AWS Config rules | Failed checks against standards such as CIS and AWS Foundational Security Best Practices | Blocked |

A **CVE** (Common Vulnerabilities and Exposures) is a public, numbered entry for a known software flaw; Inspector's package findings name them.

> **Dated (checked 2026-10-24):** the product the exam calls "AWS Security Hub" is now **AWS Security Hub CSPM**; the name **AWS Security Hub** now belongs to a newer product that correlates findings ([Security Hub FAQs](https://aws.amazon.com/security-hub/faqs/)).

## Part 1: match the findings

### Decision 1: name the service that raised each finding

The resources are the bakery's: the web server, its role, the photo bucket `bakery-cake-photos` and the account. Finding types are real AWS names; the details are made up.

| # | Finding | Resource | Severity | Detail |
|---|---|---|---|---|
| A | `CryptoCurrency:EC2/BitcoinTool.B!DNS` | Web server | High | The server is looking up a domain linked to cryptocurrency mining |
| B | Package vulnerability, CVE in `openssl` | Web server | High | An installed package has a published flaw; a fixed version exists |
| C | `SensitiveData:S3Object/Personal` | `bakery-cake-photos/exports/orders-2026-10.csv` | High | The file holds names and phone numbers |
| D | `[EC2.13] Security groups should not allow ingress from 0.0.0.0/0 or ::/0 to port 22`: FAILED | `web-sg` | High | A rule allows SSH from anywhere |
| E | `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS` | The web server's role | High | The server's temporary credentials were used from an address outside AWS |
| F | Network reachability, port 22 | Web server | Medium | An open path runs from the internet gateway to port 22 |
| G | `Policy:IAMUser/S3BlockPublicAccessDisabled` | `bakery-cake-photos` | High | Someone turned off the bucket's Block Public Access settings |
| H | `[IAM.9] MFA should be enabled for the root user`: FAILED | The account | Critical | The root user has no MFA device |

<details><summary>Model answer</summary>

![A grid of the eight findings against the four services, with one marked cell per row: A and E GuardDuty, B and F Inspector, C and G Macie, D and H Security Hub CSPM.](../../images/09-08-finding-grid.svg)

*Notice the two pairs that look alike: D and F are both about port 22, and C and G are both about the photo bucket, yet each pair comes from two different services.*

**Long description.** A grid with eight rows, A to H, and four columns: GuardDuty, Inspector, Macie, Security Hub CSPM. One cell per row is marked, with a word saying what the service read. A: GuardDuty, from DNS logs. B: Inspector, from software packages. C: Macie, from object contents. D: Security Hub CSPM, from a standards check. E: GuardDuty, from CloudTrail. F: Inspector, from network paths. G: Macie, from bucket settings. H: Security Hub CSPM, from a standards check.

- **A, GuardDuty.** Behavior seen in DNS logs: something is happening now. Inspector looks for weaknesses, not activity.
- **B, Inspector.** A known flaw in installed software. GuardDuty would only notice if someone exploited it and the behavior showed in its logs.
- **C, Macie.** Only Macie reads what's *inside* S3 objects. Worse, order exports with personal data sit in a bucket meant for cake photos.
- **D, Security Hub CSPM.** `EC2.13` is a control: a check of a setting against a standard, here using the AWS Config rule `restricted-ssh`.
- **E, GuardDuty.** Credentials used where they shouldn't be, seen in CloudTrail events.
- **F, Inspector.** A network reachability finding: Inspector worked out an actual path from the internet to the port. D says "the rule breaks a standard"; F says "the server is reachable". Both point to the same fix.
- **G, Macie.** A policy finding about the bucket's settings. GuardDuty has a similar S3 finding type, so on a real account you might see both; Macie's name format, `Policy:IAMUser/S3…`, gives it away here.
- **H, Security Hub CSPM.** A control against standards such as CIS. Trusted Advisor's free checks also flag root MFA, which is why you met it in the primer.

</details>

## Part 2: answer the owner

### Decision 2: the owner asks, "Do I really have to open four consoles every morning?"

<details><summary>Model answer</summary>

No. GuardDuty, Inspector and Macie send their findings to Security Hub CSPM, which shows them in one place, scores the account against standards and can pass findings to Amazon EventBridge to start automatic responses. Security Hub CSPM needs AWS Config turned on and recording, because most of its checks are Config rules ([What is Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)). The newer unified Security Hub goes further: it correlates signals into *exposure findings*, so a flawed package on a server that is reachable from the internet, like B and F together, can be raised as one combined risk ([What is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html)).

</details>

### Decision 3: the owner asks, "Will GuardDuty stop the attacker?"

<details><summary>Model answer</summary>

No. All four services report; none of them blocks traffic or deletes anything on its own. You act on the finding, by hand or with automation you build. To work out what the attacker did and how far it spread, Amazon Detective builds a picture from logs and GuardDuty findings ([What is Amazon Detective?](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)). Blocking belongs to other tools: a security group, a network ACL or AWS WAF, from lesson [09.04](04-the-front-door.md).

</details>

## Recap

Ask what the service reads. Activity logs mean GuardDuty, a threat happening now. Software and network paths mean Inspector, a weakness to fix. What's inside S3 means Macie. A setting checked against a standard means Security Hub CSPM, which also collects everyone's findings. None of them blocks anything.

**Next:** [Simulation S11](10-sim-organizations-and-scps.md), where many accounts are governed together.

---

"Simulation S9: Match security findings to the service that raised them" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
