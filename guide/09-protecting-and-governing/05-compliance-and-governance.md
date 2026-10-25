---
type: lesson
id: clf-09-05
title: "Compliance and governance"
tasks: ["2.2", "2.4", "2.3", "4.2"]
objectives: ["09.05a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-04-02, clf-04-04, clf-09-01]
terms_introduced: [compliance program, attestation, AWS Artifact, Artifact report, Artifact agreement, Business Associate Addendum (BAA), Services in Scope, AWS Organizations, organization, management account, member account, organizational unit (OU), service control policy (SCP), consolidated billing, FullAWSAccess, AWS Resource Access Manager (AWS RAM), AWS Control Tower, landing zone, control (AWS Control Tower), Account Factory, AWS Security Center, AWS Security Blog, AWS Security Bulletins, AWS Trust Center]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html"
  - "https://aws.amazon.com/compliance/programs/"
  - "https://aws.amazon.com/compliance/services-in-scope/"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
  - "https://docs.aws.amazon.com/ram/latest/userguide/what-is.html"
  - "https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html"
  - "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html"
  - "https://aws.amazon.com/security/"
---

# AWS proves its half of compliance and you prove yours; across many accounts, an SCP sets a ceiling nobody can rise above

**AWS Artifact** hands you AWS's half of an audit: its auditors' reports. Everything about your data, settings and people stays yours to prove. As a business grows into several accounts, **AWS Organizations** and its **service control policies** set limits nobody in those accounts can pass, and **AWS Control Tower** builds that structure for you.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Shared, inherited and customer-specific controls](../04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md) and [Policies and least privilege](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md).

## Warm-up: what you remember

1. From lesson 04.04: a user has `AdministratorAccess`, and another policy that applies to them explicitly denies `s3:DeleteBucket`. Can they delete a bucket?

<details><summary>Feedback</summary>

1. **No.** An explicit deny beats every allow. This lesson adds a kind of policy that sets limits for whole accounts.

</details>

## What you'll learn

By the end of this lesson, you can say what AWS Artifact gives you and which compliance work stays yours, explain a service control policy as a ceiling (objective 09.05a), tell AWS Organizations from AWS Control Tower, and name where AWS publishes security information.

Try this before you read on, and guess if you're unsure: the auditor wants proof that AWS's data centers have been audited against SOC 2. Where does the bakery get it, and does that report show the bakery is compliant?

## The big picture: every audit question has an owner

![Two columns under the auditor's questions. Left, AWS's controls (security of the cloud): physical security, hardware, the global network and the services' own infrastructure, proved by AWS's audit reports, downloaded from AWS Artifact. Right, highlighted, the bakery's controls (security in the cloud): its data, who has access, its settings, its staff, proved by the bakery's own records: CloudTrail, AWS Config, IAM access reports, policies and training records. A band underneath says that both halves are needed before the bakery can say it is compliant.](../../images/09-05-two-halves.svg)

*Notice that Artifact feeds only the left column. The right column is where the bakery does its own work, and an auditor checks both.*

**Long description.** At the top, "The auditor's question". Below it, two columns. Left, "AWS's controls: security of the cloud": physical security of data centers, hardware, the global network and the infrastructure of each service; evidence, AWS's audit reports and certificates, such as SOC 2, ISO 27001 and PCI DSS; from AWS Artifact, free. Right, highlighted, "The bakery's controls: security in the cloud": its data and where it lives, who has access, how its services are configured, and its staff; evidence, the bakery's own records: CloudTrail activity, AWS Config history and rules, IAM access reports, written policies and training records; from the bakery. A band across the bottom: "Compliant only when both halves are covered."

## AWS Artifact hands you AWS's audit reports, not a verdict on you

**AWS Artifact** is a free, self-service portal in the console ([What is AWS Artifact?](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html), checked 2026-10-24). **Artifact reports** are AWS's security and compliance documents, such as SOC reports, ISO certificates and PCI reports: each an **attestation**, an independent auditor's written finding that controls exist and work. **Artifact agreements** are contracts with AWS that you accept and manage, such as the **Business Associate Addendum (BAA)** that United States healthcare businesses typically need before handling protected health information.

### "Artifact checks your compliance" is wrong

You may read that Artifact tells you whether *you* are compliant. It doesn't: every report in it is about AWS. AWS says customers are responsible for producing the documents that show their own security and compliance. A SOC 2 report on AWS says nothing about whether the bakery's bucket is public. The mistake is tempting because the reports carry the names of the standards your auditor cares about, and they come from your own console.

> **Warning:** On the Free plan, don't accept any agreement in AWS Artifact. Designating an account as HIPAA or SEC compliant moves a Free plan account to the Paid plan automatically, and a Paid plan can't be downgraded ([Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), checked 2026-10-24).

## AWS lists its compliance programs, and which services each one covers

A **compliance program** is a standard, law or framework AWS is audited against or aligns with. **[AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)** lists them (checked 2026-10-24), and they differ by **industry** (PCI DSS for card payments, HIPAA for US health data) and by **geography** (C5 in Germany, IRAP in Australia). Some are certifications or attestations of AWS. For laws such as HIPAA and GDPR, no cloud provider can be certified, so AWS offers features and agreements that help you comply.

**[AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/)** lists, for each program, which services were assessed. So compliance requirements vary among AWS services.

### "Not in Services in Scope means you can't use it" is wrong

AWS says that a service missing from the list doesn't mean you can't use it. It means you must decide, as part of your shared responsibility, whether that service will handle regulated data ([Services in Scope](https://aws.amazon.com/compliance/services-in-scope/), checked 2026-10-24). The mistake is tempting because "in scope" sounds like "allowed".

After downloading AWS's reports, the bakery still has to know which rules apply, classify its data, configure services correctly, accept and keep the agreements it needs, and produce its own evidence (lesson [09.01](01-who-did-what.md)), at every audit. No service does that for you, including AWS Audit Manager, which is closed to new customers (lesson 09.01).

## AWS Organizations groups accounts so you can govern them together

Suppose the bakery grows: a production account, a test account, and an account for its German business, whose data must stay in the EU. AWS recommends several accounts like this, because an account is a natural boundary for permissions, security and costs ([What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), checked 2026-10-24). **AWS Organizations** joins them into one **organization**:

- The **management account** creates the organization and pays every account's bill; the others are **member accounts**.
- **Organizational units (OUs)** group accounts. A policy attached to the organization's root or to an OU applies to every account below it.
- **Consolidated billing:** one bill for every account, at no extra charge, with each account's costs visible (task [4.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.2); Module 11).

**AWS Resource Access Manager (AWS RAM)** shares a resource you create once, such as VPC subnets or a transit gateway, with other accounts or a whole organization ([What is AWS RAM?](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)). The owner keeps owning it.

> **Warning:** On the Free plan, don't create or join an organization. Joining AWS Organizations, or setting up a Control Tower landing zone, moves a Free plan account to the Paid plan ([Choosing a plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), checked 2026-10-24). Practice with [Simulation S11](10-sim-organizations-and-scps.md) instead.

### An SCP is a ceiling: it limits everyone in a member account, and grants nothing

A **service control policy (SCP)** sets the maximum permissions that IAM users and roles in a member account can have ([Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), checked 2026-10-24):

- **It never grants.** People still need IAM policies; what they can do is the overlap of what the SCPs allow and what their own policies allow.
- **It limits the member account's root user too,** which no IAM policy inside the account can do.
- **Every level must allow.** A block at the root, at any OU or on the account holds even against `AdministratorAccess`.
- **It doesn't apply to the management account,** so keep workloads out of it.
- **AWS attaches FullAWSAccess** to every level by default, an SCP that allows every action; your SCPs then deny what you don't want.

### SCP or IAM policy: a ceiling or a key

| | SCP | IAM policy |
|---|---|---|
| **Set in** | AWS Organizations, from the management account | One account's IAM |
| **Applies to** | Every user and role in the accounts below it | One identity or resource |
| **Grants?** | Never; it sets the maximum | Yes |
| **Root user of a member account** | Limited | Not limited |

An SCP that denies every Region outside Europe turns "German data stays in the EU" from a promise into a rule nobody in that account can break.

> **Your turn:** An SCP on an account allows only S3 actions. A user there has `AdministratorAccess`. Can they launch an EC2 instance? And could the account's root user?

<details><summary>Model answer</summary>

**No, and no.** The user's effective permissions are the overlap of the SCP and their IAM policies, which is S3 only. In a member account, SCPs limit the root user too; only the management account is outside them.

</details>

### AWS Control Tower sets up and watches a multi-account environment, on top of Organizations

**AWS Control Tower** builds a **landing zone**, a multi-account environment based on AWS's security and compliance best practices, using AWS Organizations, AWS Service Catalog and IAM Identity Center ([What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), checked 2026-10-24). It then applies **controls** to whole OUs: preventive ones built from SCPs, and detective ones built from AWS Config rules. AWS used to call them guardrails. **Account Factory** creates new accounts already governed, and a dashboard shows resources that break the controls. Control Tower has no extra charge; you pay for the services it turns on.

If a question says "SCP", "OU" or "one bill", think Organizations. If it says "quickly set up a governed multi-account environment with guardrails", think Control Tower. You can use Organizations without Control Tower, but not Control Tower without Organizations.

## Where AWS publishes security information

Task [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4) asks where AWS's security information is (checked 2026-10-24):

| Your question | Where to look |
|---|---|
| What security services does AWS offer, and how does it approach security? | [AWS Security Center](https://aws.amazon.com/security/) |
| How do I set up a security feature, and what's new? | [AWS Security Blog](https://aws.amazon.com/blogs/security/) |
| How do I fix a common problem, step by step? | [AWS Knowledge Center](https://repost.aws/knowledge-center), on AWS re:Post |
| Does a newly found vulnerability affect an AWS service? | [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/) |
| Where are AWS's security, compliance and privacy commitments in one place? | [AWS Trust Center](https://aws.amazon.com/trust-center/) |

## Summary

- **Every audit question has an owner.** AWS proves its controls with reports from **AWS Artifact**, free; you prove yours with your own records. Artifact doesn't check your compliance.
- **Compliance programs** vary by industry and country; **Services in Scope** shows which services each covers, and not listed means you decide, not forbidden.
- **AWS Organizations** groups accounts under a management account, with OUs, SCPs and one consolidated bill. **An SCP is a ceiling** for everyone in a member account, root included; it grants nothing.
- **AWS Control Tower** builds and watches a best-practice landing zone on top of Organizations.

## Practice

1. **Which statement about AWS Artifact is correct?**

   A. It scans your account and reports whether you meet PCI DSS\
   B. It provides AWS's compliance reports and lets you manage agreements with AWS\
   C. It costs a fee per report downloaded\
   D. It lists which AWS services are in scope for each program

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** Artifact's reports are about AWS, not your account; checking your own resources is a job for AWS Config rules or Security Hub.
   - **C is wrong.** Artifact documents and agreements are free.
   - **D is wrong.** That's the Services in Scope web page.

   </details>

2. **The bakery's German account has an SCP that denies all Regions outside Europe, apart from global services. The account's root user tries to create a database in US East (N. Virginia). What happens?**

   A. It works, because the root user is outside every policy\
   B. It's denied, because SCPs limit a member account's root user too\
   C. It works, because global services are exempt\
   D. It's denied only if the root user has no MFA

   <details><summary>Feedback</summary>

   **B is right.** Only the management account is outside SCPs.

   - **A is wrong.** In a member account, the root user is inside the SCP's ceiling.
   - **C is wrong.** The exemption covers global services such as IAM, not a database in a US Region.
   - **D is wrong.** MFA doesn't change what an SCP allows.

   </details>

3. **A company wants new accounts created from an approved template, ready-made preventive and detective rules, and a dashboard of rule-breaking resources, set up quickly. Which service fits best?**

   A. AWS Organizations alone\
   B. AWS Control Tower\
   C. AWS Artifact\
   D. AWS Audit Manager

   <details><summary>Feedback</summary>

   **B is right.** Account Factory, controls and the dashboard are Control Tower features.

   - **A is wrong.** Organizations provides the parts, but you would design and build all of this yourself.
   - **C is wrong.** Artifact holds AWS's reports and agreements.
   - **D is wrong.** Audit Manager is closed to new customers, and it never created accounts.

   </details>

**Next:** [A defense map](06-a-defense-map.md). To download a real Artifact report, do [Lab 12](07-lab-12-answer-the-auditor.md); to practice SCPs, try [Simulation S11](10-sim-organizations-and-scps.md).

## Where to check the current details

- [What is AWS Artifact?](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) and [AWS Services in Scope](https://aws.amazon.com/compliance/services-in-scope/) (checked 2026-10-24)
- [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (checked 2026-10-24)
- [What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) (checked 2026-10-24)

---

"Compliance and governance" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
