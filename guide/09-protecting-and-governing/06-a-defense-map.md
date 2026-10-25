---
type: lesson
id: clf-09-06
title: "A defense map"
tasks: ["2.1", "2.2", "2.4"]
objectives: ["09.06a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08, the guardrails primer and lessons 09.01 to 09.05; about 15 minutes; works on a phone"
prerequisites: [clf-04-01, clf-07-02, clf-09-01, clf-09-02, clf-09-03, clf-09-04, clf-09-05]
terms_introduced: [defense in depth, preventive control, detective control]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"
---

# Build a defense map: stack controls from the edge to the organization, so one mistake never exposes everything

No single control keeps a workload safe. **Defense in depth** puts several independent layers between an attacker and your data, and watches every layer, so that when one fails, another stops or reveals the attack.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1), [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson pulls together lessons 09.01 to 09.05 and [Filtering traffic](../07-connecting-it/02-filtering-traffic.md).

## Warm-up: what you remember

1. From lesson 04.01: on EC2, who protects the data center building, and who writes the security group rules?

<details><summary>Feedback</summary>

1. **AWS protects the building** (security of the cloud); **the bakery writes the rules** (security in the cloud). Every layer in this lesson splits the same way.

</details>

## What you'll learn

By the end of this lesson, you can assemble layered controls for a workload and justify each one (objective 09.06a), and tell a control that prevents from a control that detects.

Try this before you read on, and guess if you're unsure: if every layer has a control that blocks attacks, why also keep logs?

## The big picture: six layers, and a watch across all of them

![Six nested layers from the outside in. Edge: Route 53, CloudFront, Shield, WAF. Network: VPC, subnets and routes, network ACLs, security groups. Compute: patched images, Inspector. Data: encryption with KMS and ACM, S3 Block Public Access, Macie, backups. Identity and account: IAM least privilege, MFA, roles, root protection. Organization: separate accounts, SCPs, Control Tower controls, Firewall Manager. A highlighted vertical band crosses every layer: watch and prove, with CloudTrail, AWS Config, CloudWatch, GuardDuty and Security Hub.](../../images/09-06-defense-map.svg)

*Notice the highlighted band. Each layer stops some things; the watch across all of them is how you learn that something got through, and how you prove to an auditor what happened.*

**Long description.** Six layers, drawn as bands from the internet at the top to the organization at the bottom. 1, Edge, where traffic first reaches AWS: Amazon Route 53, Amazon CloudFront, AWS Shield and AWS WAF. 2, Network, the bakery's VPC: public and private subnets, route tables, network ACLs and security groups. 3, Compute, the servers and functions: patched images and guest operating systems, Amazon Inspector scans. 4, Data, what is stored: encryption with AWS KMS keys and ACM certificates, S3 Block Public Access and versioning, Amazon Macie, backups. 5, Identity and account: IAM least privilege, MFA, roles instead of access keys, root user protection. 6, Organization: separate accounts, service control policies, AWS Control Tower controls, AWS Firewall Manager. A highlighted vertical band labeled "watch and prove" crosses all six layers: AWS CloudTrail, AWS Config, Amazon CloudWatch, Amazon GuardDuty and AWS Security Hub.

The Well-Architected security design principle "[Apply security at all layers](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html)" says the same thing.

## Each layer stops different attacks

A **preventive control** stops something from happening, such as a security group rule, a WAF rule or an SCP. A **detective control** notices and records it afterward, such as a CloudTrail record, a GuardDuty finding or an AWS Config rule.

| Layer | Protects against | Prevent with | Detect with |
|---|---|---|---|
| Edge | Floods; bad web requests | Shield, CloudFront in front, WAF rules | CloudWatch alarms; WAF logs |
| Network | Reaching what should be private | Private subnets, network ACLs, security groups | VPC Flow Logs; Inspector's exposure findings |
| Compute | Known software flaws | Patching (on EC2; Lambda leaves the OS to AWS) | Inspector |
| Data | Reading or losing stored data | Encryption, Block Public Access, versioning, backups | Macie |
| Identity and account | Stolen or misused credentials | Least privilege, MFA, roles, root protection | CloudTrail, GuardDuty, access reports |
| Organization | One account's mistake spreading | Separate accounts, SCPs, Control Tower, Firewall Manager | Control Tower dashboard, organization-wide trail |

## Cover every threat with at least two layers: one that stops it and one that finds it

Preventive controls fail quietly. A security group rule opened "for a minute" during testing, or an access key pasted into a public code repository: nothing blocks these, because the mistake *is* in the blocking layer. A stolen key used through ordinary calls to AWS's APIs passes every network filter and WAF; only CloudTrail and GuardDuty reveal it, and an SCP limits what it can do in a member account. So for each threat, ask which layer stops it and which tells you if that one failed. Records then prove what happened, the job of lesson [09.01](01-who-did-what.md).

> **Your turn:** Place each control on a layer and say whether it prevents or detects: (a) an S3 bucket's Block Public Access; (b) a GuardDuty finding about an access key used from an unusual location; (c) a WAF rate-based rule; (d) an SCP that denies stopping CloudTrail.

<details><summary>Model answer</summary>

(a) Data, prevents. (b) Identity and account, detects: it reports, it doesn't block. (c) Edge, prevents. (d) Organization, prevents: no one in a member account, root included, can switch off the trail.

</details>

## The shared responsibility model holds at every layer

AWS provides the tools and runs what lies under them; you choose the tools and configure them ([Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)). The service moves the line: on EC2 you patch the guest operating system, on Lambda AWS does. But no service moves your data or who can reach it to AWS's side. And most controls on the map are off, or wide open, until you configure them: the default network ACL allows everything, and GuardDuty does nothing until you enable it. AWS applies Shield Standard to every customer, but putting CloudFront in front, writing WAF rules and deciding on Shield Advanced are the bakery's choices.

## Summary

- **Defense in depth** stacks independent layers, edge, network, compute, data, identity and account, organization, so one failure doesn't expose everything.
- **Cover every threat twice:** a preventive control that stops it and a detective control that finds it, because preventive controls fail quietly.
- **Shared responsibility holds at every layer.** AWS provides and runs the tools; you choose and configure them, and data and access stay yours on every service.

## Practice

1. **Which pair gives a preventive and a detective control for the threat "someone makes a bucket public by mistake"?**

   A. S3 Block Public Access, and Amazon Macie\
   B. AWS Shield, and AWS WAF\
   C. A network ACL, and a security group\
   D. AWS Artifact, and AWS Organizations

   <details><summary>Feedback</summary>

   **A is right.** Block Public Access stops the bucket from becoming public; Macie reports public buckets and sensitive data in them.

   - **B is wrong.** Both work at the edge on traffic, not on bucket settings.
   - **C is wrong.** Both filter network traffic in a VPC; they don't set S3 bucket access.
   - **D is wrong.** Artifact holds AWS's reports and Organizations groups accounts; neither stops or finds a public bucket by itself.

   </details>

2. **An attacker uses a stolen access key through ordinary AWS API calls. Which statement is correct?**

   A. Security groups stop it, because the attacker comes from the internet\
   B. WAF stops it, because it inspects every request to AWS\
   C. Network filters don't see it; MFA and no long-term keys prevent it, and GuardDuty and CloudTrail reveal it\
   D. Shield Standard stops it automatically

   <details><summary>Feedback</summary>

   **C is right.** Calls to AWS's own APIs don't pass through the bakery's VPC filters or its WAF.

   - **A is wrong.** Security groups filter traffic to your resources, not calls to AWS's API endpoints.
   - **B is wrong.** WAF inspects requests to the resources you attach it to, such as CloudFront or a load balancer.
   - **D is wrong.** Shield protects against DDoS floods, not misuse of valid credentials.

   </details>

3. **A plan lists CloudFront, WAF, Shield Standard, security groups, private subnets, encrypted storage and MFA. What is the biggest gap?**

   A. It has no detective controls, so a leaked key or a rule opened by mistake would go unnoticed\
   B. It needs AWS CloudHSM for encrypted storage\
   C. Shield Standard must be turned on first\
   D. MFA makes WAF unnecessary

   <details><summary>Feedback</summary>

   **A is right.** Everything listed prevents; nothing watches or records. Add CloudTrail and alarms at least, and GuardDuty.

   - **B is wrong.** Nothing here requires single-tenant HSMs.
   - **C is wrong.** Shield Standard is automatic for every customer.
   - **D is wrong.** MFA protects sign-ins; WAF filters web requests. They guard different layers.

   </details>

**Next:** [Lab 12](07-lab-12-answer-the-auditor.md), where you answer the auditor with evidence from your own account, then the module's [mastery check](11-check.md). For more practice, try the optional [Simulation S9](08-sim-security-findings-tour.md) and [Simulation S11](10-sim-organizations-and-scps.md).

## Where to check the current details

- [Security design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html), AWS Well-Architected Framework (checked 2026-10-24)
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) (checked 2026-10-24)

---

"A defense map" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
