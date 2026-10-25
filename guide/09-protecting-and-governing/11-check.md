---
type: check
id: clf-09-11
title: "Module 09 mastery check"
tasks: ["2.2", "2.4", "2.3", "2.1"]
objectives: ["09.01a", "09.02a", "09.03a", "09.04a", "09.05a", "09.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 09 lessons; about 15 minutes for each check; works on a phone"
prerequisites: [clf-09-01, clf-09-02, clf-09-03, clf-09-04, clf-09-05, clf-09-06]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html"
  - "https://aws.amazon.com/compliance/services-in-scope/"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
---

# Module 09 mastery check

**For:** an adult studying alone, possibly new to IT, who has finished the Module 09 lessons. **Time:** about 15 minutes per check.

## How to use this check

Take Check A closed-book; 8 of 10 (80%) is a pass. Below that, reread the sections the correction map names for your misses, then take Check B, the parallel retest. A "(Select TWO.)" question counts only if both choices are right.

## Check A

**A1.** A shop's database was slow on Friday evening. The owner asks (1) whether it was overloaded, and (2) whether someone changed its instance class that afternoon, and who. Which pair of records answers both?

- A. (1) AWS CloudTrail; (2) AWS Config
- B. (1) AWS Config; (2) CloudWatch Logs
- C. (1) CloudWatch metrics; (2) AWS CloudTrail
- D. (1) CloudWatch metrics; (2) IAM last accessed information

<details><summary>Answer</summary>

**C is right.** Load over time is a CloudWatch metric; a change to the instance class is an action, which CloudTrail records with who and when.

- **A is wrong.** CloudTrail records actions, not load.
- **B is wrong.** Config shows settings, not load.
- **D is wrong.** Last accessed information doesn't name changes.

</details>

**A2.** An agency stores CVs in Amazon S3. A contract says it must show who may decrypt them and be able to cut off all access at once by turning off the key. Nothing mentions dedicated hardware. Which fits best?

- A. SSE-S3, the bucket's default encryption
- B. SSE-KMS with the AWS managed key `aws/s3`
- C. SSE-KMS with a customer managed key in AWS KMS
- D. Keys held in an AWS CloudHSM cluster

<details><summary>Answer</summary>

**C is right.** The agency writes the key policy that says who may decrypt, and it can disable the key, which stops every decryption at once.

- **A is wrong.** S3 manages SSE-S3's keys.
- **B is wrong.** AWS controls an AWS managed key.
- **D is wrong.** It works, but nothing requires single-tenant hardware.

</details>

**A3.** A banking app talks to an Amazon API Gateway API and stores transactions in a database. Both the traffic and the stored data must be encrypted. Which TWO should it use? (Select TWO.)

- A. A certificate from AWS Certificate Manager, so the API serves HTTPS
- B. An AWS CloudHSM cluster, so the app's traffic stays off the internet
- C. Amazon Macie, so the transactions it finds are encrypted
- D. Encryption at rest on the database, with a key from AWS KMS
- E. A KMS key attached to the API, so the traffic is encrypted

<details><summary>Answer</summary>

**A and D are right.** Data moving to the API needs TLS, with a certificate from ACM; stored data needs encryption at rest with a KMS key.

- **B is wrong.** CloudHSM doesn't change the path traffic takes.
- **C is wrong.** Macie finds sensitive data; it encrypts nothing.
- **E is wrong.** Traffic needs a TLS certificate, not a KMS key.

</details>

**A4.** Which TWO matches of a finding to its service are right? (Select TWO.)

- A. A Lambda function's code uses a library with a published CVE: Amazon Inspector
- B. A spreadsheet in an S3 bucket holds staff bank details: Amazon GuardDuty
- C. Three controls of the PCI DSS standard fail for the account's settings: AWS Security Hub
- D. The root user has no MFA, flagged by a free check on Basic Support: Amazon Detective
- E. An IAM user is calling AWS APIs from a country the company never works in: Amazon Inspector

<details><summary>Answer</summary>

**A and C are right.** Inspector scans software for known flaws; a failed control of a named standard is Security Hub (today's Security Hub CSPM).

- **B is wrong.** That's Amazon Macie.
- **D is wrong.** That's AWS Trusted Advisor.
- **E is wrong.** That's GuardDuty: activity, not software.

</details>

**A5.** Which TWO plans match the attack to the right protection? (Select TWO.)

- A. A flood of half-opened connections (a SYN flood): an AWS WAF rate-based rule
- B. Search requests containing `' OR 1=1 --`: an AWS WAF managed rule group for SQL injection
- C. One address range keeps trying SSH passwords on a server: an AWS WAF IP set rule
- D. All 40 of its accounts, including new ones, must get the same web ACL: AWS Firewall Manager
- E. A flood of page requests on the checkout page: a security group rule

<details><summary>Answer</summary>

**B and D are right.** Only WAF reads request content; Firewall Manager copies WAF rules to every account.

- **A is wrong.** A SYN flood is a network flood for Shield Standard.
- **C is wrong.** WAF never sees SSH; use a network ACL.
- **E is wrong.** A security group can't count requests.

</details>

**A6.** A brokerage loses more in an hour offline than any protection costs in a year. It wants automatic mitigation of request floods, attack reports, and credits for scaling charges an attack causes. Which fits?

- A. AWS Shield Standard, with CloudFront in front of the site
- B. AWS WAF rules alone, with a rate-based rule
- C. AWS Firewall Manager across the brokerage's accounts
- D. AWS Shield Advanced on those distributions and load balancers

<details><summary>Answer</summary>

**D is right.** Shield Advanced adds all three.

- **A is wrong.** No reports, layer 7 mitigation or bill protection.
- **B is wrong.** No reports or cost protection.
- **C is wrong.** It applies policies; it adds no protection of its own.

</details>

**A7.** Which questionnaire item can a company answer with a document from AWS Artifact?

- A. "Do all your IAM users sign in with MFA?"
- B. "Are the data centers that host your systems audited for physical security?"
- C. "Do your S3 buckets block public access?"
- D. "Do your staff complete security training every year?"

<details><summary>Answer</summary>

**B is right.** Data center security is AWS's control, and Artifact holds AWS's audit reports, such as SOC 2, that cover it.

- **A, C and D are wrong.** MFA, bucket settings and training are the company's controls, proved by its own records.

</details>

**A8.** An SCP on an OU denies `s3:DeleteBucket`. In a member account below it, an engineer's IAM policy allows `s3:DeleteBucket`. She tries to delete a bucket. What happens?

- A. It works, because an explicit allow in her IAM policy overrides the SCP
- B. It works, because SCPs apply only to the account's root user
- C. It's denied, because the SCP sets a ceiling that her IAM policy can't raise
- D. It's denied only if the bucket also has a bucket policy that denies it

<details><summary>Answer</summary>

**C is right.** A request must be allowed by every SCP above the account and by her own policies.

- **A is wrong.** An IAM allow can't lift a request above the SCP.
- **B is wrong.** SCPs limit every user and role, and root.
- **D is wrong.** The SCP's deny is enough.

</details>

**A9.** An agency with five accounts wants one bill and to write its own SCPs, without a ready-made landing zone. Which service fits?

- A. AWS Organizations
- B. AWS Control Tower
- C. AWS Artifact
- D. AWS Firewall Manager

<details><summary>Answer</summary>

**A is right.** Organizations groups accounts under a management account, with consolidated billing and SCPs you design yourself.

- **B is wrong.** Its job is the landing zone the agency doesn't want.
- **C is wrong.** Artifact holds AWS's reports.
- **D is wrong.** It applies firewall policies; it doesn't create an organization.

</details>

**A10.** For the threat "someone switches off CloudTrail to hide what they're doing", which pair gives one preventive control and one detective control?

- A. An AWS Config rule that flags a stopped trail, and Amazon GuardDuty
- B. A security group that blocks the console, and VPC Flow Logs
- C. An SCP that denies stopping or deleting trails, and CloudTrail's record of the attempt
- D. An IAM policy on each administrator denying it, and S3 Block Public Access

<details><summary>Answer</summary>

**C is right.** The SCP stops anyone in a member account, root included; CloudTrail records the attempt.

- **A is wrong.** Both are detective.
- **B is wrong.** Neither sees calls to AWS's APIs.
- **D is wrong.** Both are preventive, and Block Public Access guards buckets.

</details>

## Correction map

Reread the section for each item you missed.

| Items | Objective | Reread |
|---|---|---|
| A1, B1 | 09.01a | [AWS Config records how each resource was set](01-who-did-what.md#aws-config-records-how-each-resource-was-set-and-judges-it-against-your-rules) |
| A2, B2 | 09.02a | [KMS holds the keys for data at rest, and records every use](02-encryption.md#kms-holds-the-keys-for-data-at-rest-and-records-every-use) |
| A3, B3 | 09.02a | [At rest and in transit are two protections](02-encryption.md#at-rest-and-in-transit-are-two-protections-against-two-different-threats) |
| A4, B4 | 09.03a | [Match a finding to its service by asking what it looked at](03-finding-threats-and-weaknesses.md#match-a-finding-to-its-service-by-asking-what-it-looked-at) |
| A5, B5 | 09.04a | [Choose the protection by the attack](04-the-front-door.md#choose-the-protection-by-the-attack-then-check-the-cost) |
| A6, B6 | 09.04a | [Shield Advanced adds detection, people and bill protection](04-the-front-door.md#shield-advanced-adds-detection-people-and-bill-protection-for-a-price) |
| A7, B7 | 09.05a | [AWS Artifact hands you AWS's audit reports](05-compliance-and-governance.md#aws-artifact-hands-you-awss-audit-reports-not-a-verdict-on-you); [compliance programs](05-compliance-and-governance.md#aws-lists-its-compliance-programs-and-which-services-each-one-covers) |
| A8, B8 | 09.05a | [An SCP is a ceiling](05-compliance-and-governance.md#an-scp-is-a-ceiling-it-limits-everyone-in-a-member-account-and-grants-nothing) |
| A9, B9 | 09.05a | [AWS Control Tower](05-compliance-and-governance.md#aws-control-tower-sets-up-and-watches-a-multi-account-environment-on-top-of-organizations) |
| A10, B10 | 09.06a | [Cover every threat with at least two layers](06-a-defense-map.md#cover-every-threat-with-at-least-two-layers-one-that-stops-it-and-one-that-finds-it) |

## Check B: parallel retest

**B1.** A load balancer accepted plain HTTP for a week. Config was recording. The auditor asks (1) what its listeners were set to each day, and (2) how many requests the site served that week. Which pair answers both?

- A. (1) AWS CloudTrail; (2) AWS Config
- B. (1) Amazon CloudWatch; (2) AWS CloudTrail
- C. (1) AWS Config; (2) AWS CloudTrail
- D. (1) AWS Config; (2) Amazon CloudWatch

<details><summary>Answer</summary>

**D is right.** Settings on a given day are Config's history; requests served are a CloudWatch metric.

- **A is wrong.** CloudTrail lists changes, not daily state.
- **B is wrong.** CloudWatch doesn't hold settings.
- **C is wrong.** CloudTrail doesn't count site requests.

</details>

**B2.** A pharmacy's archive is in Amazon S3. It must choose the key's rotation itself, and the key's managers must not be able to decrypt. Nothing mentions dedicated hardware. Which fits best?

- A. SSE-S3, the bucket's default encryption
- B. SSE-KMS with the AWS managed key `aws/s3`
- C. SSE-KMS with a customer managed key in AWS KMS
- D. SSE-KMS with an AWS owned key

<details><summary>Answer</summary>

**C is right.** The pharmacy writes the key policy, so one role can administer the key and another decrypt, and it chooses the rotation.

- **A is wrong.** S3 manages SSE-S3's keys.
- **B is wrong.** Its policy can't be changed.
- **D is wrong.** Customers can't see or control AWS owned keys.

</details>

**B3.** A tutoring platform must encrypt (1) live sessions between browsers and its CloudFront distribution, and (2) recordings in S3, with the key controlled by the company. Which TWO should it use? (Select TWO.)

- A. A public certificate from ACM on the distribution, with HTTPS required
- B. A KMS key attached to the distribution to encrypt the live sessions
- C. An ACM certificate attached to the bucket to encrypt the stored recordings
- D. AWS CloudHSM, so the sessions travel off the internet
- E. SSE-KMS with a customer managed key on the recordings bucket

<details><summary>Answer</summary>

**A and E are right.** Live sessions are data in transit, protected by TLS with an ACM certificate; recordings are data at rest, and a customer managed key lets the company write the key policy.

- **B is wrong.** Web traffic is encrypted with TLS.
- **C is wrong.** Certificates protect connections, not objects.
- **D is wrong.** CloudHSM doesn't move traffic.

</details>

**B4.** Which TWO matches of a finding to its service are right? (Select TWO.)

- A. A container image in Amazon ECR has a package with a known flaw: Amazon GuardDuty
- B. Files in a research bucket contain passport numbers: Amazon Macie
- C. The account's settings fail controls in the CIS benchmark: Amazon Inspector
- D. A server keeps looking up domains linked to cryptocurrency mining: Amazon GuardDuty
- E. Find the root cause and the scope of a GuardDuty finding: AWS Trusted Advisor

<details><summary>Answer</summary>

**B and D are right.** Macie finds sensitive data inside S3 objects; lookups of mining domains are activity in DNS logs, which GuardDuty reads.

- **A is wrong.** That's Amazon Inspector.
- **C is wrong.** That's AWS Security Hub.
- **E is wrong.** That's Amazon Detective.

</details>

**B5.** Which TWO plans match the attack to the right protection? (Select TWO.)

- A. Product reviews carry scripts that run in other visitors' browsers: an AWS WAF cross-site scripting rule
- B. Most bad traffic comes from one country the shop doesn't serve: a network ACL rule for that country
- C. A UDP reflection flood against the site: AWS Shield Standard, already on
- D. Every account in the organization needs the same WAF rules: AWS Shield Standard
- E. A flood of page requests from hundreds of addresses: the web servers' security groups

<details><summary>Answer</summary>

**A and C are right.** Only WAF reads request content; Shield Standard absorbs network floods automatically.

- **B is wrong.** A network ACL doesn't know countries; WAF does.
- **D is wrong.** That's AWS Firewall Manager.
- **E is wrong.** Security groups can't count requests.

</details>

**B6.** An exam provider wants DDoS experts on call during an attack and credits for the scaling charges an attack causes. Which fits?

- A. AWS Shield Standard, plus CloudFront in front of the site
- B. AWS WAF, plus managed rule groups and rate-based rules
- C. AWS Shield Advanced, plus the Support plan its response team requires
- D. An Enterprise Support plan alone, which includes the Shield Response Team

<details><summary>Answer</summary>

**C is right.** Shield Advanced brings the Shield Response Team (SRT) and DDoS cost protection; AWS's page says the SRT also needs a Business or Enterprise Support plan (checked 2026-10-24).

- **A and B are wrong.** Neither brings experts or bill protection.
- **D is wrong.** The SRT is a Shield Advanced feature.

</details>

**B7.** A health insurer with a BAA wants a service that isn't listed under HIPAA on AWS's Services in Scope page to process claims. Which statement is correct?

- A. AWS blocks unlisted services in accounts that have accepted a BAA
- B. The service may never be used anywhere in the insurer's company
- C. Accepting the BAA brings every AWS service into HIPAA scope
- D. It isn't forbidden; the insurer must decide, with its auditor, before relying on it

<details><summary>Answer</summary>

**D is right.** AWS says a service missing from the list isn't forbidden; whether it can hold regulated data is the insurer's decision.

- **A is wrong.** AWS doesn't block services by program.
- **B is wrong.** It can be used, at least outside the regulated part.
- **C is wrong.** The BAA doesn't change which services were assessed.

</details>

**B8.** An SCP attached to an organization's root denies leaving the organization. The root user of a member account tries to remove the account from the organization. What happens?

- A. It's denied, because SCPs limit a member account's root user too
- B. It works, because the root user is outside every policy
- C. It works, because the root user needs no IAM policy to act
- D. It's denied only if the root user signed in without MFA

<details><summary>Answer</summary>

**A is right.** Only the management account is outside SCPs.

- **B is wrong.** In a member account, SCPs reach the root user.
- **C is wrong.** Root needs no IAM policy, but the SCP's ceiling still applies.
- **D is wrong.** MFA doesn't change what an SCP allows.

</details>

**B9.** An IT team wants new accounts to arrive set up with logging, single sign-on and ready-made rules for whole groups of accounts, plus a dashboard. It has no staff to design OUs and policies. Which fits best?

- A. AWS Organizations alone, with OUs and SCPs the team writes
- B. AWS Control Tower
- C. AWS Audit Manager, with a framework assessment
- D. AWS Config alone, recording in each account

<details><summary>Answer</summary>

**B is right.** Control Tower builds a landing zone, applies controls to OUs, and creates accounts through Account Factory.

- **A is wrong.** The team would have to design it all.
- **C is wrong.** Audit Manager is closed to new accounts.
- **D is wrong.** Config doesn't create accounts.

</details>

**B10.** For the threat "a web server runs software with a known, published flaw", which pair gives one preventive control and one detective control?

- A. AWS WAF rules, and Amazon Detective
- B. AWS Shield Advanced, and CloudWatch metrics
- C. An SCP that denies changes to EC2, and AWS Trusted Advisor
- D. Regular patching from updated images, and Amazon Inspector findings

<details><summary>Answer</summary>

**D is right.** Patching removes the flaw; Inspector rescans when a new CVE is published and reveals any server still carrying it.

- **A is wrong.** WAF doesn't fix software; Detective doesn't find flaws.
- **B is wrong.** Neither knows what software is installed.
- **C is wrong.** The SCP would block patching too.

</details>

---

"Module 09 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
