---
type: check
id: clf-09-11
title: "Module 09 mastery check"
tasks: ["2.2", "2.4", "2.3", "2.1"]
objectives: ["09.01a", "09.02a", "09.03a", "09.04a", "09.05a", "09.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 09 lessons; about 30 minutes for each check; works on a phone"
prerequisites: [clf-09-01, clf-09-02, clf-09-03, clf-09-04, clf-09-05, clf-09-06]
pillars: [security]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html"
  - "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html"
  - "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"
  - "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html"
  - "https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html"
  - "https://aws.amazon.com/compliance/services-in-scope/"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
  - "https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html"
---

# Module 09 mastery check

This check tells you whether you can do what Module 09 set out to teach: answer an audit question from the right record, choose how data is encrypted and who holds the key, name the service behind a finding, choose a protection for an attack, say which compliance work stays yours and what an SCP does, and judge a layered security plan. Every question is a short scenario, like the exam's.

**For:** an adult studying alone, possibly new to IT, who has finished the six Module 09 lessons. **Time:** about 30 minutes for each check. Reading works on a phone.

## How to use this check

Take Check A closed-book, without the lessons open, and write down your answers before you open any of them. Count your score: 15 of 18 (80%) or better is a pass. If you score below that, use the correction map to reread the sections behind each miss, then take Check B, the parallel retest, on another day if you can. If you pass, go on to the enrichment tasks.

Questions marked "(Select TWO.)" have two right answers; you need both for the point, as on the exam.

## Check A

**A1.** An online bookshop created a multi-Region CloudTrail trail on its first day, two years ago, and has kept every log file. It turned on AWS Config only last month. An auditor asks: "Between January and March last year, was remote desktop (port 3389) open to the internet on the office security group, and if so, who opened it?" What can the bookshop produce?

- A. The trail's events: each change to the rules, who made it and when
- B. Config's history for those months, with the CloudTrail events it links to
- C. Nothing, because CloudTrail keeps only the last 90 days of events
- D. IAM last accessed information, showing who used EC2 in those months

<details><summary>Answer</summary>

**A is right.** Config records only from the day recording starts, so it has nothing from last year. The trail, though, has kept every management event since day one: each change to the security group's rules, with who made it and when. From those changes the bookshop can work out what the group allowed between January and March, and name the person.

- **B is wrong.** Config would be the easier source for "what did it allow?", but its history begins last month.
- **C is wrong.** The 90-day limit belongs to Event history. A trail keeps its files in S3 for as long as you keep them.
- **D is wrong.** Last accessed information says when an identity last tried a service, not which change it made to which security group.

</details>

**A2.** An auditor sends a payroll company five questions. Which TWO can IAM's access reports answer? (Select TWO.)

- A. Which roles may use DynamoDB but haven't tried to in the past year?
- B. Who deleted the payroll DynamoDB table last week?
- C. Was the payroll database's storage encrypted on 1 May?
- D. Which IAM users have a console password but no MFA device?
- E. How many read requests did the payroll table serve on Friday?

<details><summary>Answer</summary>

**A and D are right.** Last accessed information shows, for each role, which allowed services it last tried and when, so it finds permissions nobody uses. The credential report lists every IAM user with their password, MFA and access key status.

- **B is wrong.** Deleting a table is an action on the account: CloudTrail records who did it.
- **C is wrong.** A resource's settings on a past date are AWS Config's history, if it was recording then.
- **E is wrong.** Request counts over time are a CloudWatch metric.

</details>

**A3.** A shop's order database was slow on Friday from 18:00 to 19:00. The owner suspects that someone changed the database's instance class that afternoon. She wants to know (1) whether the database was overloaded during that hour, and (2) whether its instance class was changed, and by whom. Which pair of records answers both?

- A. (1) AWS CloudTrail; (2) AWS Config
- B. (1) AWS Config; (2) CloudWatch Logs
- C. (1) CloudWatch metrics; (2) AWS CloudTrail
- D. (1) CloudWatch metrics; (2) IAM last accessed information

<details><summary>Answer</summary>

**C is right.** How busy the database was is a question about how it ran: its CPU and connections are CloudWatch metrics. A change to its instance class is an action on the account, and CloudTrail records who made it and when.

- **A is wrong.** CloudTrail records actions, not load. Config could show that the instance class changed, but it describes states, not people, so it can't name who did it.
- **B is wrong.** Config shows settings, not load, and CloudWatch Logs holds lines that software writes, not a record of who changed a setting.
- **D is wrong.** Last accessed information shows when an identity last tried a service, not which change it made to which database.

</details>

**A4.** A recruitment agency stores candidates' CVs in Amazon S3. Its contract with a large client says the agency must be able to show who is allowed to decrypt the CVs, and must be able to cut off all access to them at once in an emergency by turning off the key. Nothing in the contract mentions dedicated hardware. Which approach fits best?

- A. SSE-S3, the bucket's default encryption
- B. SSE-KMS with the AWS managed key `aws/s3`
- C. SSE-KMS with a customer managed key in AWS KMS
- D. Keys held in an AWS CloudHSM cluster

<details><summary>Answer</summary>

**C is right.** With a customer managed key, the agency writes the key policy that says who may decrypt, and it can disable the key, which stops every decryption at once, then enable it again later. Each use of the key is also recorded in CloudTrail.

- **A is wrong.** With SSE-S3, S3 manages the keys; the agency can neither show who may use them nor turn them off.
- **B is wrong.** An AWS managed key lives in the agency's account and its use shows in CloudTrail, but AWS controls it: the agency can't change its policy or disable it.
- **D is wrong.** CloudHSM would work, but nothing requires single-tenant hardware, so it adds cost and work for no gain.

</details>

**A5.** A mobile-banking startup serves its app through an Amazon API Gateway API and stores each transaction in a database. Its auditor requires encryption for the app's traffic to the API and for the stored transactions. Which TWO should the startup use? (Select TWO.)

- A. A certificate from AWS Certificate Manager, so the API serves HTTPS
- B. An AWS CloudHSM cluster, so the app's traffic stays off the internet
- C. Amazon Macie, so the transactions it finds are encrypted
- D. Encryption at rest on the database, with a key from AWS KMS
- E. A KMS key attached to the API, so the traffic is encrypted

<details><summary>Answer</summary>

**A and D are right.** Data moving between the app and the API needs encryption in transit: TLS, with a certificate from ACM. Stored transactions need encryption at rest, which the database does with a KMS key.

- **B is wrong.** CloudHSM holds keys in dedicated hardware; it doesn't change the path that traffic takes, and encrypted traffic still crosses the internet.
- **C is wrong.** Macie finds sensitive data in S3; it encrypts nothing.
- **E is wrong.** KMS keys protect data at rest. Encrypting a website's or an API's traffic is a job for a TLS certificate from ACM.

</details>

**A6.** A physiotherapy clinic created its Amazon RDS database a year ago without encryption. Its new auditor requires the patient data to be encrypted at rest. What must the clinic do?

- A. Turn on encryption in the running database's settings
- B. Attach an ACM certificate to the database's endpoint
- C. Turn on Amazon Macie for the database's storage
- D. Copy a snapshot with encryption turned on, and restore from the copy

<details><summary>Answer</summary>

**D is right.** An RDS database is encrypted, or not, when it's created, and that can't be switched on in place. The clinic copies a snapshot with encryption on, restores a new, encrypted database from the copy, and moves its application to it.

- **A is wrong.** There is no such switch for an existing RDS database; that is why the choice at creation matters.
- **B is wrong.** A TLS certificate protects connections to the database, which is encryption in transit, not the stored data.
- **C is wrong.** Macie finds sensitive data in S3; it doesn't encrypt RDS storage.

</details>

**A7.** A finding reports that an Amazon EC2 instance is sending traffic to an IP address on a list of known malicious servers that attackers use to control hijacked machines. Which service raised it?

- A. Amazon Inspector
- B. Amazon GuardDuty
- C. Amazon Macie
- D. AWS Trusted Advisor

<details><summary>Answer</summary>

**B is right.** GuardDuty reads activity, such as VPC Flow Logs and DNS logs, and compares it with threat intelligence: lists of known malicious addresses and domains. Traffic to such an address is activity happening now, a threat.

- **A is wrong.** Inspector finds weaknesses in installed software and open network paths, not who a server is talking to.
- **C is wrong.** Macie looks inside S3 buckets for sensitive data.
- **D is wrong.** Trusted Advisor checks settings against AWS's best practices; it doesn't watch traffic.

</details>

**A8.** A security team matches five findings to the services that raised them. Which TWO matches are right? (Select TWO.)

- A. A Lambda function's code uses a library with a published CVE: Amazon Inspector
- B. A spreadsheet in an S3 bucket holds staff bank details: Amazon GuardDuty
- C. Three controls of the PCI DSS standard fail for the account's settings: AWS Security Hub
- D. The root user has no MFA, flagged by a free check on Basic Support: Amazon Detective
- E. An IAM user is calling AWS APIs from a country the company never works in: Amazon Inspector

<details><summary>Answer</summary>

**A and C are right.** Inspector scans the software in EC2 instances, container images and Lambda functions for known flaws, continuously and with no assessment templates (those belonged to Inspector Classic, shut down on 2026-05-20). A setting that fails a named standard's control is Security Hub: today the product called Security Hub CSPM, which the exam calls AWS Security Hub.

- **B is wrong.** Only Amazon Macie reads what's inside S3 objects. GuardDuty watches activity.
- **D is wrong.** A free best-practice check on Basic Support is AWS Trusted Advisor. Detective investigates a finding after it's raised.
- **E is wrong.** Unusual API activity is a threat, seen in CloudTrail events, so GuardDuty raises it. Inspector looks at software and network paths.

</details>

**A9.** A cloud team's morning report includes this finding: a control in the AWS Foundational Security Best Practices standard, "EBS default encryption should be enabled", is marked FAILED for the account. Which service raised it?

- A. AWS Trusted Advisor
- B. Amazon Detective
- C. Amazon GuardDuty
- D. AWS Security Hub

<details><summary>Answer</summary>

**D is right.** Checking settings against a named standard and marking each control passed or failed is what Security Hub does; the product is now called Security Hub CSPM, and most of its controls run as AWS Config rules.

- **A is wrong.** Trusted Advisor checks the account against AWS's own best practices in six categories; it doesn't report controls of a named standard such as AWS Foundational Security Best Practices.
- **B is wrong.** Detective investigates a finding after another service raised it; it runs no checks of settings.
- **C is wrong.** GuardDuty reports suspicious activity, not settings.

</details>

**A10.** A ticket seller lists five attacks and the protection it plans for each. Which TWO plans are right? (Select TWO.)

- A. A flood of half-opened connections (a SYN flood): an AWS WAF rate-based rule
- B. Search requests containing `' OR 1=1 --`: an AWS WAF managed rule group for SQL injection
- C. One address range keeps trying SSH passwords on a server: an AWS WAF IP set rule
- D. All 40 of its accounts, including new ones, must get the same web ACL: AWS Firewall Manager
- E. A flood of page requests on the checkout page: a security group rule

<details><summary>Answer</summary>

**B and D are right.** SQL injection hides in the content of a web request, which only WAF reads. Applying the same WAF rules to every account in an organization, including accounts created later, is Firewall Manager's job.

- **A is wrong.** A SYN flood is a network flood, below the level of web requests; AWS Shield Standard absorbs it automatically.
- **C is wrong.** SSH isn't a web request, so WAF never sees it. Block the range with a network ACL deny rule, and don't open SSH to the internet at all.
- **E is wrong.** A security group sees only addresses and ports. A page request flood arrives on port 443 like real customers; a WAF rate-based rule limits it.

</details>

**A11.** A small charity's donation page, behind an Application Load Balancer, is hit by a flood of page requests from about 200 addresses, each sending far more requests than any donor would. The charity can't afford a yearly security subscription. What should it add?

- A. An AWS WAF rate-based rule on the load balancer
- B. Nothing; AWS Shield Standard, already on, blocks request floods
- C. An AWS Shield Advanced subscription for the load balancer
- D. A security group rule that limits requests per address

<details><summary>Answer</summary>

**A is right.** A rate-based rule caps how many requests one address may send in a time window, which is the usual answer to a small HTTP flood, and WAF costs a few dollars a month for a site this size.

- **B is wrong.** Shield Standard absorbs common network floods, but it doesn't read web requests, so a flood of normal-looking page requests gets through.
- **C is wrong.** Shield Advanced would add automatic mitigation, but it's a yearly commitment the charity has ruled out, and WAF alone handles this attack.
- **D is wrong.** Security groups allow or deny by address, port and protocol; they can't count requests.

</details>

**A12.** An online brokerage loses more in an hour offline than any AWS protection costs in a year. For its CloudFront distributions and Application Load Balancers, it wants automatic mitigation of request floods, detailed reports on each attack, and credits for the scaling charges an attack causes. Which choice fits?

- A. AWS Shield Standard, with CloudFront in front of the site
- B. AWS WAF rules alone, with a rate-based rule
- C. AWS Firewall Manager across the brokerage's accounts
- D. AWS Shield Advanced on those distributions and load balancers

<details><summary>Answer</summary>

**D is right.** Shield Advanced adds automatic layer 7 mitigation (it writes WAF rules for you), detailed attack metrics and reports, and DDoS cost protection, on the resources you choose. For a business this size, the cost is justified. It also brings the Shield Response Team (SRT), though AWS's page says using the SRT needs a Business or Enterprise Support plan as well (checked 2026-10-24; Business Support is being replaced, so check the page).

- **A is wrong.** Shield Standard and CloudFront are a strong base, but they bring no attack reports, no automatic layer 7 mitigation and no bill protection.
- **B is wrong.** WAF handles request floods, but it brings no attack reports and no cost protection.
- **C is wrong.** Firewall Manager applies policies across accounts; it adds no protection of its own.

</details>

**A13.** An e-learning company is filling in a customer's security questionnaire. Which question can it answer with a document from AWS Artifact?

- A. "Do all your IAM users sign in with MFA?"
- B. "Are the data centers that host your systems audited for physical security?"
- C. "Do your S3 buckets block public access?"
- D. "Do your staff complete security training every year?"

<details><summary>Answer</summary>

**B is right.** Data center security is AWS's control, security of the cloud, and Artifact holds AWS's independent audit reports, such as SOC 2, that cover it.

- **A is wrong.** Who has MFA is the company's own control; its evidence is the IAM credential report.
- **C is wrong.** Bucket settings are the company's configuration; its evidence comes from its own account, such as the Block Public Access settings or AWS Config results.
- **D is wrong.** Staff training is the company's job, and its evidence is its own training records. No AWS document covers it.

</details>

**A14.** An SCP attached to a company's Analytics OU denies `s3:DeleteBucket`. In a member account under that OU, an engineer's IAM policy explicitly allows `s3:DeleteBucket`. She tries to delete a bucket. What happens?

- A. It works, because an explicit allow in her IAM policy overrides the SCP
- B. It works, because SCPs apply only to the account's root user
- C. It's denied, because the SCP sets a ceiling that her IAM policy can't raise
- D. It's denied only if the bucket also has a bucket policy that denies it

<details><summary>Answer</summary>

**C is right.** An SCP sets the maximum for every user and role in the member account. A request must be allowed by every SCP above the account and by her own policies; the SCP's deny holds whatever her IAM policy says.

- **A is wrong.** An IAM allow can never lift a request above the SCP.
- **B is wrong.** SCPs limit every IAM user and role in a member account, and its root user as well.
- **D is wrong.** The SCP's deny is enough on its own; no bucket policy is needed.

</details>

**A15.** A company's Sandbox OU has an SCP that allows only Amazon S3 and AWS Lambda actions. A new IAM user in a sandbox account has no IAM policies at all. She tries to create a Lambda function. What happens?

- A. It works, because the SCP allows Lambda actions in the account
- B. It's denied, because an SCP grants nothing and she has no IAM policy that allows it
- C. It works, because a new user gets Lambda access by default in a sandbox
- D. It's denied, because SCPs deny every Lambda action by default

<details><summary>Answer</summary>

**B is right.** An SCP only sets the ceiling. What a person can do is the overlap of what the SCPs allow and what their own policies allow, and with no IAM policy, the overlap is empty.

- **A is wrong.** That treats the SCP as a grant. It allows Lambda only as far as an IAM policy also does.
- **C is wrong.** New IAM users start with no permissions anywhere; nothing is granted by default.
- **D is wrong.** This SCP allows Lambda, and the default SCP, FullAWSAccess, allows everything; SCPs don't deny by default.

</details>

**A16.** A growing design agency has five AWS accounts. It wants one bill for all of them and to write its own service control policies. It doesn't want a ready-made landing zone or pre-built controls. Which service fits?

- A. AWS Organizations
- B. AWS Control Tower
- C. AWS Artifact
- D. AWS Firewall Manager

<details><summary>Answer</summary>

**A is right.** Organizations groups accounts under a management account, with OUs, consolidated billing and SCPs that you design yourself.

- **B is wrong.** Control Tower is built on Organizations, but its whole job is the ready-made landing zone and controls that the agency has said it doesn't want.
- **C is wrong.** Artifact gives you AWS's audit reports and agreements; it doesn't group accounts or bill them.
- **D is wrong.** Firewall Manager applies firewall policies across an organization that already exists; it doesn't create one or handle billing.

</details>

**A17.** A consultant's security plan for a photo-sharing startup lists: CloudFront in front of the site, AWS WAF managed rules, AWS Shield Advanced, private subnets, tight security groups, Amazon GuardDuty and a multi-Region CloudTrail trail. The startup's developers sign in to the AWS CLI with long-term access keys stored on their laptops, and their IAM users have no MFA. What is the strongest criticism of the plan?

- A. It has no detective controls, so an attack in progress would go unnoticed
- B. It guards the edge and network, while long-term keys leave identity open
- C. It needs AWS CloudHSM, because users' photos count as regulated data
- D. It should drop AWS WAF, because Shield Advanced reads every web request

<details><summary>Answer</summary>

**B is right.** A stolen access key is used through ordinary calls to AWS's APIs, which never pass the edge or the network filters, so the plan's strongest layers don't touch the likeliest threat. Roles or temporary credentials and MFA would prevent it. GuardDuty and CloudTrail would reveal it, but only after the damage starts. Shield Advanced's yearly cost also needs a business case for a startup.

- **A is wrong.** GuardDuty and CloudTrail are detective controls, and both are in the plan.
- **C is wrong.** Nothing here requires single-tenant hardware; KMS keys already sit in validated HSMs.
- **D is wrong.** Shield doesn't read requests on its own; Shield Advanced's request-flood mitigation works by writing WAF rules, and WAF's managed rules stop attacks such as SQL injection that aren't floods at all.

</details>

**A18.** For the threat "someone switches off CloudTrail to hide what they're doing", which pair gives one preventive control and one detective control?

- A. An AWS Config rule that flags a stopped trail, and Amazon GuardDuty
- B. A security group that blocks the console, and VPC Flow Logs
- C. An SCP that denies stopping or deleting trails, and CloudTrail's record of the attempt
- D. An IAM policy on each administrator denying it, and S3 Block Public Access

<details><summary>Answer</summary>

**C is right.** In member accounts, the SCP stops anyone, the root user included, from stopping or deleting a trail. The attempt itself is an API call, which CloudTrail records, so the layer that watches shows who tried.

- **A is wrong.** Both are detective: they notice the trail is off after it happened, and neither stops it.
- **B is wrong.** Security groups filter network traffic to your resources; they don't control calls to AWS's own APIs, and Flow Logs record traffic, not API calls.
- **D is wrong.** Both halves are preventive, and the first is weak: an IAM policy prevents it only for the identities it's attached to, an administrator can remove it, and it never limits the account's root user. Block Public Access guards buckets, not trails.

</details>

## Correction map

Find each item you missed, reread the section, then try the angle in the fourth column: it explains the same idea a different way from the lesson. The practice column names the lab or simulation that exercises it.

| Item | Objective | Reread | A different way to see it | Practice |
|---|---|---|---|---|
| A1 | 09.01a | [AWS Config records how each resource was set](01-who-did-what.md#aws-config-records-how-each-resource-was-set-and-judges-it-against-your-rules); ["CloudTrail records everything, forever" is wrong](01-who-did-what.md#cloudtrail-records-everything-forever-is-wrong) | Every record starts the day it's switched on. Ask two things of each source: does it hold this kind of fact, and was it running back then? | [Simulation S10](09-sim-config-timeline.md), Part 3 |
| A2 | 09.01a | [Access reports show who can do what, and whether they still use it](01-who-did-what.md#access-reports-show-who-can-do-what-and-whether-they-still-use-it) | Access reports describe people's permissions and credentials, not their actions or resources' settings | [Lab 12](07-lab-12-answer-the-auditor.md), Part C |
| A3 | 09.01a | [CloudWatch shows how things are running, not who changed them](01-who-did-what.md#cloudwatch-shows-how-things-are-running-not-who-changed-them) | Split a two-part question first. "How busy" is a gauge on the dashboard; "who changed it" is a name in the visitors' book | [Lab 12](07-lab-12-answer-the-auditor.md), Parts A and B |
| A4 | 09.02a | [KMS holds the keys for data at rest, and records every use](02-encryption.md#kms-holds-the-keys-for-data-at-rest-and-records-every-use) | Move along the key line only as far as the requirement pushes you: "show who" and "switch it off" both need a key whose policy and life are yours | [Lab 12](07-lab-12-answer-the-auditor.md), Part D |
| A5 | 09.02a | [At rest and in transit are two protections against two different threats](02-encryption.md#at-rest-and-in-transit-are-two-protections-against-two-different-threats); [TLS certificates from ACM protect data in transit](02-encryption.md#tls-certificates-from-acm-protect-data-in-transit) | Ask "moving or stored?" before naming a service. Moving means a certificate (ACM); stored means a key (KMS) | The lesson's worked example |
| A6 | 09.02a | [KMS holds the keys for data at rest, and records every use](02-encryption.md#kms-holds-the-keys-for-data-at-rest-and-records-every-use) (the last paragraph) | Some choices are made when a resource is born. To change them, you make a new copy that was born right | The lesson's worked example |
| A7 | 09.03a | [GuardDuty watches activity and reports threats happening now](03-finding-threats-and-weaknesses.md#guardduty-watches-activity-and-reports-threats-happening-now) | If the finding describes something a server *did*, it came from a service that reads activity: GuardDuty | [Simulation S9](08-sim-security-findings-tour.md), Decision 1 |
| A8 | 09.03a | [Match a finding to its service by asking what it looked at](03-finding-threats-and-weaknesses.md#match-a-finding-to-its-service-by-asking-what-it-looked-at) | Name the evidence in each finding: installed software, data in S3, a setting against a standard, activity, or an investigation. The service follows | [Simulation S9](08-sim-security-findings-tour.md), Decision 1 |
| A9 | 09.03a | [Security Hub gathers every finding and checks your settings](03-finding-threats-and-weaknesses.md#security-hub-gathers-every-finding-and-checks-your-settings-and-the-name-now-covers-two-products) | The words "standard" and "control" are the signature of Security Hub CSPM | [Simulation S9](08-sim-security-findings-tour.md), findings D and H |
| A10 | 09.04a | [Choose the protection by the attack, then check the cost](04-the-front-door.md#choose-the-protection-by-the-attack-then-check-the-cost); [AWS WAF reads each web request](04-the-front-door.md#aws-waf-reads-each-web-request-and-allows-blocks-or-challenges-it) | Sort by what the attack is made of: raw packets (Shield), web requests (WAF), other ports (network ACL), many accounts (Firewall Manager) | The lesson's attack grid |
| A11 | 09.04a | [AWS WAF reads each web request](04-the-front-door.md#aws-waf-reads-each-web-request-and-allows-blocks-or-challenges-it) | Shield is the flood barrier that never reads the letters; a rate-based rule is the attendant who notices one visitor knocking 500 times a minute | The lesson's cost chart |
| A12 | 09.04a | [Shield Advanced adds detection, people and bill protection, for a price](04-the-front-door.md#shield-advanced-adds-detection-people-and-bill-protection-for-a-price) | List what the business asked for: attack reports, automatic request-flood mitigation and bill credits appear together only in Shield Advanced's column | The lesson's worked example |
| A13 | 09.05a | [AWS Artifact hands you AWS's audit reports, not a verdict on you](05-compliance-and-governance.md#aws-artifact-hands-you-awss-audit-reports-not-a-verdict-on-you) | Ask whose hands touch it. If only AWS staff can touch it (buildings, hardware), Artifact has the proof; if your people configure it, the proof is yours | [Lab 12](07-lab-12-answer-the-auditor.md), Part E |
| A14 | 09.05a | [An SCP is a ceiling](05-compliance-and-governance.md#an-scp-is-a-ceiling-it-limits-everyone-in-a-member-account-and-grants-nothing) | Picture two gates in a row: the SCP and the IAM policy. A request must pass both, and a locked first gate can't be opened from the second | [Simulation S11](10-sim-organizations-and-scps.md), Decision 1 |
| A15 | 09.05a | [SCP or IAM policy: a ceiling or a key](05-compliance-and-governance.md#scp-or-iam-policy-a-ceiling-or-a-key) | A high ceiling doesn't lift anyone off the floor. Only an IAM policy lifts | [Simulation S11](10-sim-organizations-and-scps.md), Decision 1 |
| A16 | 09.05a | [AWS Control Tower sets up and watches a multi-account environment, on top of Organizations](05-compliance-and-governance.md#aws-control-tower-sets-up-and-watches-a-multi-account-environment-on-top-of-organizations) | Organizations is the building's frame; Control Tower is a contractor who fits it out to a standard plan. Choose by who should design the rooms | [Simulation S11](10-sim-organizations-and-scps.md), Decision 3 |
| A17 | 09.06a | [Cover every threat with at least two layers](06-a-defense-map.md#cover-every-threat-with-at-least-two-layers-one-that-stops-it-and-one-that-finds-it) | Walk the threat grid row by row and put a finger on the plan's control for each. The row with no finger is the gap | The lesson's threat grid |
| A18 | 09.06a | [Each layer stops different attacks](06-a-defense-map.md#each-layer-stops-different-attacks) | For each pair, label each half "stops" or "notices". A good pair has one of each | The lesson's threat grid |

## Check B: parallel retest

Take this after you have worked through the correction map. Each item tests the same objective as the Check A item with the same number, with a new scenario.

**B1.** A clinic turned on AWS Config three years ago but has never created a CloudTrail trail. An auditor says: "Eight months ago, the policy on your patient-records bucket briefly allowed public reads. When did that start, and who changed the policy?" What can the clinic show?

- A. Both: Config shows when it started, and Event history names who did it
- B. When, from Config's history; but not who, with no trail and Event history's 90 days
- C. Who, from IAM last accessed information; but not when it started
- D. Neither, because Config keeps only the last 90 days of history

<details><summary>Answer</summary>

**B is right.** Config has been recording for three years and keeps seven years by default, so it shows when the bucket's policy changed and what it said. But Config describes states, not people. The person is in CloudTrail, and without a trail, nothing older than Event history's 90 days was kept.

- **A is wrong.** Event history can't reach back eight months.
- **C is wrong.** Last accessed information shows when an identity last tried a service, not which change it made.
- **D is wrong.** The 90-day window is CloudTrail Event history's. Config's history is seven years by default.

</details>

**B2.** An auditor asks a logistics firm two questions: (1) "Which of your staff accounts have a password but no MFA?" and (2) "Which permissions has your deployment role never used this year?" Which pair of IAM reports answers them?

- A. (1) The credential report; (2) last accessed information
- B. (1) Last accessed information; (2) the credential report
- C. (1) CloudTrail Event history; (2) the AWS Config history
- D. (1) The Organizations access report; (2) CloudWatch Logs Insights

<details><summary>Answer</summary>

**A is right.** The credential report lists every IAM user with their password and MFA status. The role's Last Accessed tab shows which allowed services it tried, and when, so the ones never tried are permissions it doesn't use.

- **B is wrong.** It swaps them: last accessed information is about services used, and the credential report about users' credentials.
- **C is wrong.** CloudTrail records actions and Config records resource settings; neither is a list of who lacks MFA or which permissions go unused.
- **D is wrong.** The Organizations access report covers services used per account under SCPs, and Logs Insights searches log lines; neither answers either question directly.

</details>

**B3.** For a week last month, a web shop's load balancer had a listener that accepted plain HTTP, until someone noticed. AWS Config was recording, and the load balancer sends its metrics to CloudWatch. The auditor asks (1) what the load balancer's listeners were set to on each day of that week, and (2) how many requests the site served that week. Which pair of records answers both?

- A. (1) AWS CloudTrail; (2) AWS Config
- B. (1) Amazon CloudWatch; (2) AWS CloudTrail
- C. (1) AWS Config; (2) AWS CloudTrail
- D. (1) AWS Config; (2) Amazon CloudWatch

<details><summary>Answer</summary>

**D is right.** A resource's settings on a given day are Config's configuration history. The number of requests served is a load balancer metric in CloudWatch.

- **A is wrong.** CloudTrail lists the changes to the listeners, not the state each day, and Config doesn't count requests.
- **B is wrong.** CloudWatch measures traffic, not settings, and CloudTrail records actions on the account, not the site's request count.
- **C is wrong.** The first half is right, but CloudTrail records management actions, not customers' requests to the site.

</details>

**B4.** A pharmacy's prescription archive is in Amazon S3. Its security rules say the pharmacy must decide itself how often the key's material is rotated, and that the people who manage the key must not be able to use it to decrypt. No rule mentions dedicated hardware. Which approach fits best?

- A. SSE-S3, the bucket's default encryption
- B. SSE-KMS with the AWS managed key `aws/s3`
- C. SSE-KMS with a customer managed key in AWS KMS
- D. SSE-KMS with an AWS owned key

<details><summary>Answer</summary>

**C is right.** A customer managed key's policy is the pharmacy's to write, so it can let one role administer the key and a different role decrypt with it, and it chooses the key's rotation.

- **A is wrong.** S3 manages SSE-S3's keys; the pharmacy can't set who uses them or how they rotate.
- **B is wrong.** AWS rotates an AWS managed key every year on its own schedule, and its policy can't be changed.
- **D is wrong.** AWS owned keys live in AWS's accounts; customers can't see, control or audit them.

</details>

**B5.** A tutoring platform must encrypt (1) students' live sessions between their browsers and its Amazon CloudFront distribution, and (2) the session recordings it stores in S3, with access to the recordings' key controlled by the company. Which TWO should it use? (Select TWO.)

- A. A public certificate from ACM on the distribution, with HTTPS required
- B. A KMS key attached to the distribution to encrypt the live sessions
- C. An ACM certificate attached to the bucket to encrypt the stored recordings
- D. AWS CloudHSM, so the sessions travel off the internet
- E. SSE-KMS with a customer managed key on the recordings bucket

<details><summary>Answer</summary>

**A and E are right.** The live sessions are data in transit, protected by TLS with an ACM certificate on CloudFront; requiring HTTPS, not just offering it, closes the plain-HTTP door. The recordings are data at rest, and a customer managed key lets the company write the key policy.

- **B is wrong.** KMS keys protect stored data; a website's traffic is encrypted with TLS.
- **C is wrong.** Certificates protect connections, not stored objects.
- **D is wrong.** CloudHSM holds keys in dedicated hardware; it doesn't move traffic off the internet.

</details>

**B6.** A travel company's Amazon RDS database is encrypted with the AWS managed key `aws/rds`. A new company rule says the database must use a customer managed key that the company controls. What must it do?

- A. Edit the running database and choose the new key in its settings
- B. Change the policy of the `aws/rds` key to match the new rule
- C. Turn on automatic rotation, which converts `aws/rds` into a customer managed key
- D. Copy a snapshot encrypted with the new key, and restore a new database from it

<details><summary>Answer</summary>

**D is right.** An RDS database's key is chosen when it's created and can't be changed afterward. The way to a different key is a snapshot copy encrypted with that key, restored as a new database.

- **A is wrong.** The key of an existing RDS database can't be changed in place.
- **B is wrong.** AWS controls AWS managed keys; customers can't change their policies.
- **C is wrong.** Rotation makes new key material for the same key; it never changes the kind of key.

</details>

**B7.** A finding reports that an Amazon EC2 instance is making repeated attempts to guess SSH passwords on other servers. Which service raised it?

- A. Amazon Inspector
- B. Amazon Macie
- C. Amazon GuardDuty
- D. AWS Trusted Advisor

<details><summary>Answer</summary>

**C is right.** Repeated sign-in attempts are activity, which GuardDuty spots in VPC Flow Logs; its finding type for this is `UnauthorizedAccess:EC2/SSHBruteForce`.

- **A is wrong.** Inspector would report that port 22 is reachable or that software is unpatched, not that the instance is attacking others.
- **B is wrong.** Macie looks inside S3 buckets, not at network activity.
- **D is wrong.** Trusted Advisor checks settings against best practices; it doesn't watch what servers do.

</details>

**B8.** A university's security team matches five findings to services. Which TWO matches are right? (Select TWO.)

- A. A container image in Amazon ECR has a package with a known flaw: Amazon GuardDuty
- B. Files in a research bucket contain passport numbers: Amazon Macie
- C. The account's settings fail controls in the CIS benchmark: Amazon Inspector
- D. A server keeps looking up domains linked to cryptocurrency mining: Amazon GuardDuty
- E. Find the root cause and the scope of a GuardDuty finding: AWS Trusted Advisor

<details><summary>Answer</summary>

**B and D are right.** Macie finds sensitive data, such as passport numbers, inside S3 objects. Lookups of mining domains are activity seen in DNS logs, which GuardDuty reads.

- **A is wrong.** Known flaws in container images are Amazon Inspector's findings.
- **C is wrong.** Settings checked against a named standard such as CIS are AWS Security Hub's (Security Hub CSPM's) controls.
- **E is wrong.** Investigating a finding's root cause and scope is Amazon Detective's job, with up to a year of linked activity.

</details>

**B9.** The owner of a new account on Basic Support, with no security services turned on, opens a page of checks grouped as cost optimization, performance, security, fault tolerance, service limits and operational excellence. A security check warns that a security group allows unrestricted access to specific ports. Which service is she looking at?

- A. AWS Trusted Advisor
- B. AWS Security Hub
- C. Amazon Inspector
- D. Amazon Detective

<details><summary>Answer</summary>

**A is right.** Trusted Advisor groups its best-practice checks into those six categories, and Basic Support includes a few security checks, such as security groups with specific ports open to everyone, refreshed by hand.

- **B is wrong.** Security Hub must be turned on, and it reports controls against standards, not those six categories.
- **C is wrong.** Inspector must be turned on, and it reports software flaws and network paths on workloads.
- **D is wrong.** Detective investigates findings that other services raised; it runs no checks of its own.

</details>

**B10.** An online shop lists five attacks and the protection it plans for each. Which TWO plans are right? (Select TWO.)

- A. Product reviews carry scripts that run in other visitors' browsers: an AWS WAF cross-site scripting rule
- B. Most bad traffic comes from one country the shop doesn't serve: a network ACL rule for that country
- C. A UDP reflection flood against the site: AWS Shield Standard, already on
- D. Every account in the organization needs the same WAF rules: AWS Shield Standard
- E. A flood of page requests from hundreds of addresses: the web servers' security groups

<details><summary>Answer</summary>

**A and C are right.** Cross-site scripting is in the content of a request, which only WAF reads. UDP reflection is a network flood, which Shield Standard absorbs for every customer automatically.

- **B is wrong.** A network ACL knows addresses and ports, not countries. A WAF rule can match requests by country.
- **D is wrong.** Shield Standard applies no rules of yours. Copying the same WAF rules to every account is AWS Firewall Manager's job.
- **E is wrong.** Security groups can't count or read requests; a WAF rate-based rule handles a request flood.

</details>

**B11.** Attackers are trying thousands of stolen username and password pairs on a gym's sign-in page, which runs behind an Application Load Balancer. Each attacking address sends hundreds of attempts a minute, far more than a member would. What should the gym add first?

- A. Nothing; AWS Shield Standard already blocks this attack
- B. An AWS WAF rate-based rule on the load balancer
- C. Amazon Inspector scans of the sign-in servers
- D. Amazon GuardDuty in the load balancer's Region

<details><summary>Answer</summary>

**B is right.** The attempts are ordinary web requests, so only WAF sees them, and a rate-based rule caps how many requests each address may send in a time window.

- **A is wrong.** Shield Standard absorbs network floods; it doesn't read or count web requests.
- **C is wrong.** Inspector finds software flaws and open paths; it blocks nothing.
- **D is wrong.** GuardDuty reports threats it sees in logs; it doesn't stop requests to the site.

</details>

**B12.** An online exam provider holds national exams twice a year and can't afford its site to fail during exam week. It wants DDoS experts on call during an attack and credits for the scaling charges an attack causes. Which choice fits?

- A. AWS Shield Standard, plus CloudFront in front of the site
- B. AWS WAF, plus managed rule groups and rate-based rules
- C. AWS Shield Advanced, plus the Support plan its response team requires
- D. An Enterprise Support plan alone, which includes the Shield Response Team

<details><summary>Answer</summary>

**C is right.** Shield Advanced brings the Shield Response Team (SRT) and DDoS cost protection, plus automatic mitigation of request floods, and AWS's page says using the SRT also needs a Business or Enterprise Support plan (checked 2026-10-24; Business Support is being replaced by Business Support+, and AWS hasn't yet said whether that qualifies).

- **A is wrong.** Shield Standard is automatic and free, but it brings no experts and no bill protection.
- **B is wrong.** WAF filters requests, but brings no experts and no cost protection.
- **D is wrong.** The SRT is a Shield Advanced feature. A Support plan, of any level, doesn't bring it on its own.

</details>

**B13.** A health insurer has accepted the BAA with AWS and wants to use a service that isn't listed under HIPAA on AWS's Services in Scope page. The service would process members' claims, which are protected health information. Which statement is correct?

- A. AWS blocks unlisted services in accounts that have accepted a BAA
- B. The service may never be used anywhere in the insurer's company
- C. Accepting the BAA brings every AWS service into HIPAA scope
- D. It isn't forbidden; the insurer must decide, with its auditor, before relying on it

<details><summary>Answer</summary>

**D is right.** AWS says a service missing from the list isn't forbidden. Whether it can hold regulated data is the insurer's decision, part of its share of the responsibility, and because claims are protected health information, it should check with its auditor or AWS account team first.

- **A is wrong.** AWS doesn't block services by compliance program.
- **B is wrong.** The service can be used, at least outside the regulated part of the insurer's setup.
- **C is wrong.** The BAA is a contract about how regulated data is handled; it doesn't change which services were assessed.

</details>

**B14.** An SCP attached to an organization's root denies leaving the organization. The root user of a member account signs in and tries to remove the account from the organization. What happens?

- A. It's denied, because SCPs limit a member account's root user too
- B. It works, because the root user is outside every policy
- C. It works, because the root user needs no IAM policy to act
- D. It's denied only if the root user signed in without MFA

<details><summary>Answer</summary>

**A is right.** An SCP sets the ceiling for everyone in a member account, the root user included, which no IAM policy inside the account can do. Only the management account is outside SCPs.

- **B is wrong.** In a member account, SCPs reach the root user as well.
- **C is wrong.** It's true that root needs no IAM policy, but the SCP's ceiling still applies.
- **D is wrong.** MFA proves who signed in; it doesn't change what an SCP allows.

</details>

**B15.** A member account still has the default SCP, FullAWSAccess, which allows every action. A contractor's role in that account has a permissions policy that allows only `s3:GetObject`. The contractor tries to delete an object. What happens?

- A. It works, because FullAWSAccess allows every action in the account
- B. It works, because the SCP overrides the role's narrower policy
- C. It's denied, because the SCP allows it but the role's policy doesn't
- D. It's denied, because FullAWSAccess denies deletes by default

<details><summary>Answer</summary>

**C is right.** The contractor can do only what both the SCP and the role's policy allow. FullAWSAccess sets a high ceiling, but the role's policy allows only reading, so the delete is refused.

- **A is wrong.** FullAWSAccess grants nothing; it only leaves the ceiling at "everything".
- **B is wrong.** An SCP never adds permissions to a role.
- **D is wrong.** FullAWSAccess allows every action; the denial comes from the role's policy, which doesn't allow deleting.

</details>

**B16.** A university's central IT team wants each research group's new AWS account to arrive already set up with logging, single sign-on and ready-made rules applied to whole groups of accounts, plus a dashboard of accounts that break them. It has no staff to design the OUs and policies itself. Which service fits best?

- A. AWS Organizations alone, with OUs and SCPs the team writes
- B. AWS Control Tower
- C. AWS Audit Manager, with a framework assessment
- D. AWS Config alone, recording in each account

<details><summary>Answer</summary>

**B is right.** Control Tower builds a landing zone on top of Organizations, applies ready-made preventive, detective and proactive controls to whole OUs, creates new accounts through Account Factory, and shows a dashboard of resources that break the controls.

- **A is wrong.** Organizations gives the parts, but the team would have to design and build all of it, which it can't.
- **C is wrong.** Audit Manager can't be set up in new accounts since 2026-04-30, and it never created or governed accounts.
- **D is wrong.** Config records and checks settings in one account at a time; it doesn't create accounts, sign-in or a landing zone.

</details>

**B17.** A recruiting firm's security plan lists: private subnets, tight security groups, KMS encryption, S3 Block Public Access, MFA and roles for everyone, an SCP that protects CloudTrail, GuardDuty, a CloudTrail trail and AWS Config rules. Its job application form is served straight from an Application Load Balancer. What is the most important gap?

- A. No control reads the form's requests, so SQL injection would reach the servers
- B. No detective controls, so a stolen key would go unnoticed
- C. No DDoS protection at all, because nothing was bought for it
- D. No CloudHSM cluster, so the KMS keys are too weak for personal data

<details><summary>Answer</summary>

**A is right.** Every layer except the edge has controls. A malicious form entry arrives on port 443 like any honest one, passes the security groups, and only a WAF web ACL, on the load balancer or on CloudFront in front of it, would stop it.

- **B is wrong.** GuardDuty, CloudTrail and Config are all detective controls, and all are in the plan.
- **C is wrong.** Shield Standard protects every AWS customer automatically. Moving the front door to CloudFront would strengthen it, but some protection is there.
- **D is wrong.** KMS keys sit in validated hardware security modules; nothing here requires single-tenant HSMs.

</details>

**B18.** For the threat "a web server runs software with a known, published flaw", which pair gives one preventive control and one detective control?

- A. AWS WAF rules, and Amazon Detective
- B. AWS Shield Advanced, and CloudWatch metrics
- C. An SCP that denies changes to EC2, and AWS Trusted Advisor
- D. Regular patching from updated images, and Amazon Inspector findings

<details><summary>Answer</summary>

**D is right.** Patching removes the flaw, which prevents it from being used, and Inspector rescans when a new CVE is published, so it reveals any server still carrying it. On EC2, patching the guest operating system is the customer's job.

- **A is wrong.** WAF reads web requests and can block some attacks, but it doesn't fix the software, and Detective investigates findings rather than finding flaws.
- **B is wrong.** Shield Advanced protects against DDoS floods, and metrics don't know which software is installed.
- **C is wrong.** Blocking changes to EC2 would also block the patching, and Trusted Advisor's best-practice checks don't list software flaws.

</details>

## Enrichment

For learners who passed Check A. Each task has no single right answer; compare yours with the model answer.

> **Your turn:** **Evidence that survives next year's audit.** The bakery grows to three accounts: production, test and the German business. Design the setup that lets it answer the auditor's five questions again next year, for every account, with records that nobody in a member account can switch off or change. Name at least five pieces, and connect your design to [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html).

<details><summary>Model answer</summary>

1. **An organization trail** from the management account, covering every account and Region, delivering to an S3 bucket in a separate log account, with **log file integrity validation** on, so the bakery can prove the files weren't changed. Member accounts can't change or delete it.
2. **An SCP on the root** that denies stopping or deleting trails and stopping the Config recorder, so even a member account's root user can't switch off the evidence.
3. **AWS Config recording in every account**, with a conformance pack of the rules the auditor cares about (for example `restricted-ssh` and `encrypted-volumes`), so "how was it set on 1 March?" has an answer, starting now.
4. **CloudTrail data events on the few buckets that hold sensitive data**, such as the tax archive, if the auditor will ask who read what; they cost extra, so only where needed.
5. **Access reports on a schedule:** the credential report and last accessed information in each account, and the Organizations access report from the management account.
6. **AWS's side from Artifact**, downloaded fresh for each audit.

SEC04-BP02 asks for logs and findings in one protected, standard place rather than one per team or account: here, the log account, which day-to-day users can't change. The honest gap to state: nothing before today can be recovered, so the date the setup was finished goes in the memo.

</details>

> **Your turn:** **The Region rule that broke everything.** The security lead wants to attach an SCP to the organization root that denies every action outside two European Regions. Explain what could go wrong for the member accounts, what the SCP can't stop, and how you would roll it out safely. Connect your answer to [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html).

<details><summary>Model answer</summary>

**What could go wrong:** global services, such as IAM, answer from outside those Regions, so the SCP must exempt them, as AWS's example does; without that, people in member accounts can't manage IAM. Anyone who "tidies up" by detaching FullAWSAccess at the same time leaves a deny-only policy, so every action below that level fails.

**What it can't stop:** SCPs don't apply to the management account, so a server launched there in another Region is still allowed; keep the management account empty of workloads. Service-linked roles are also outside SCPs, which is what keeps AWS services such as GuardDuty working.

**A safe rollout:** attach it first to a test OU holding one or two accounts, and check the Organizations access report and last accessed information for what those accounts really use. Then attach it to one OU at a time, and only at the end to the root. SEC03-BP05 describes exactly this: guardrails set centrally as a ceiling for whole accounts, while IAM policies inside each account still grant only what each job needs.

</details>

> **Your turn:** **The first hour after a finding.** On Saturday night GuardDuty reports that the web server's role credentials are being used from an address outside AWS. Write the bakery's first-hour plan: who is told and how, what to do first, which services answer "how did they get in?" and "what else did they do?", and what changes on Monday so it doesn't happen again. Connect it to [SEC10-BP04 Develop and test security incident response playbooks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html).

<details><summary>Model answer</summary>

1. **Told:** an EventBridge rule that matches high-severity GuardDuty findings sends them to an SNS topic, which texts or emails the owner. That has to be built before Saturday; GuardDuty itself tells nobody.
2. **Contain first:** revoke the role's active sessions and cut the server off from the network (a security group that allows nothing), keeping the server for investigation rather than deleting it.
3. **What else did they do?** CloudTrail shows every API call made with those credentials; Amazon Detective links the finding to up to a year of activity, to show what the role and the address touched.
4. **How did they get in?** Amazon Inspector findings on the server, such as an unpatched package or an open path, and AWS Config's history of the server's security group, with CloudTrail naming who opened anything.
5. **Monday:** patch or rebuild the server from an updated image, close any open port, check that the role has only the permissions it needs (last accessed information), and write down what happened.

SEC10-BP04 asks for this as a written playbook, practiced before it's needed, so that on Saturday night nobody is deciding the steps for the first time. Primer page 08 is the small version for a lab account.

</details>

---

"Module 09 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
