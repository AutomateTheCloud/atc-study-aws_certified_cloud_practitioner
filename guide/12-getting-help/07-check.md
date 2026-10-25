---
type: check
id: clf-12-07
title: "Module 12 mastery check"
tasks: ["4.3", "3.8", "2.4"]
objectives: ["12.01a", "12.02a", "12.03a", "12.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 12 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-12-01, clf-12-02, clf-12-03]
pillars: [operational-excellence, cost-optimization, security]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
  - "https://repost.aws/knowledge-center/report-aws-abuse"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html"
---

# Module 12 mastery check: choose the plan, the tool, the source and the people

**For:** an adult studying alone, possibly new to IT, who has finished lessons [12.01](01-support-plans.md) to [12.03](03-where-to-find-answers.md). **Time:** about 20 minutes per check.

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 13.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

**A1.** A translation agency wants to open technical cases with AWS engineers at any hour, and to let its monitoring program call the AWS Health API. It doesn't need a named contact at AWS. Which is the cheapest plan that covers both?

- **A.** Basic Support
- **B.** AWS Business Support+
- **C.** AWS Enterprise Support
- **D.** AWS Unified Operations

<details><summary>Answer</summary>

**B is right.** It's the first plan with both.

- **A is wrong.** Basic can't open technical cases or call the Health API.
- **C and D are wrong.** Both cover the needs, but add named people the agency doesn't need, for much higher fees.

</details>

**A2.** A software company has been on Enterprise On-Ramp Support since 2024. What should its finance lead plan for next year?

- **A.** The company drops to Basic unless it acts
- **B.** On-Ramp continues unchanged
- **C.** AWS moves the company to Unified Operations
- **D.** AWS moves the company to Enterprise Support

<details><summary>Answer</summary>

**D is right.** During 2026, AWS is moving On-Ramp customers to Enterprise Support automatically, and On-Ramp ends on 2027-01-01 (as of 2026-10-24).

- **A is wrong.** Falling back to Basic is what happens to a Developer Support customer who doesn't choose a plan.
- **B is wrong.** On-Ramp ends on 2027-01-01.
- **C is wrong.** Nobody is moved to Unified Operations automatically; it's a new plan.

</details>

**A3.** A hospital on Enterprise Support is writing its outage runbook. Which two lines belong in it? (Select TWO.)

- **A.** "AWS guarantees that a business-critical outage is fixed within the plan's response time."
- **B.** "Use the highest severities only for problems we can't work around, or that hit production."
- **C.** "Technical cases opened at night wait until the next business day."
- **D.** "Our own recovery plan must not depend on AWS fixing a problem by a set time."
- **E.** "Only the root user may open a case at the highest severity."

<details><summary>Answer</summary>

**B and D are right.** The top severities are for real production problems, and response times are targets for a first reply.

- **A is wrong.** The times are targets, and they measure the first reply, not the fix.
- **C is wrong.** Every paid plan takes technical cases 24/7.
- **E is wrong.** Any IAM identity with the right permissions can open a case.

</details>

**A4.** A cinema chain on Business Support+ asks: (1) Is AWS planning maintenance on the hardware under one of our EC2 instances? (2) Are we paying for EBS volumes we hardly use? (3) Can an AWS engineer explain why an AWS API keeps throttling us? Which tools answer them, in order?

- **A.** (1) Trusted Advisor; (2) AWS Health; (3) AWS re:Post
- **B.** (1) a technical case; (2) Trusted Advisor; (3) AWS Health
- **C.** (1) AWS Health; (2) Trusted Advisor; (3) a technical case in Support Center
- **D.** (1) AWS Health; (2) Support Center; (3) Trusted Advisor

<details><summary>Answer</summary>

**C is right.** AWS Health reports what AWS runs, Trusted Advisor checks what you built, and a case reaches a person.

- **A is wrong.** It swaps the first two tools, and re:Post can't see your account.
- **B is wrong.** AWS announces maintenance through AWS Health, not a case.
- **D is wrong.** Support Center doesn't scan resources.

</details>

**A5.** A journalist with no AWS account wants to see whether AWS reported a service problem in one Region last month. Where can she look?

- **A.** The AWS Health API, once her newspaper buys Business Support+
- **B.** The AWS Health Dashboard's Service health view
- **C.** The Your account health view, which lists every customer's events
- **D.** AWS Support Center

<details><summary>Answer</summary>

**B is right.** Service health is public and keeps 12 months of history.

- **A is wrong.** The API is for programs.
- **C is wrong.** Your account health shows only your own resources' events.
- **D is wrong.** She has no account, and AWS doesn't publish service events in cases.

</details>

**A6.** A company moves from Basic to Business Support+. What does it now see in Trusted Advisor that it didn't before?

- **A.** All the service limits checks
- **B.** Trusted Advisor Priority
- **C.** Automatic fixes for its findings
- **D.** Every check, in all six categories

<details><summary>Answer</summary>

**D is right.** Paid plans see all checks; Basic sees only some.

- **A is wrong.** Basic already has every service limits check.
- **B is wrong.** Priority comes only with Enterprise and Unified Operations.
- **C is wrong.** Trusted Advisor only reports, on every plan.

</details>

**A7.** A photographer on Basic finds her photos copied onto a website at an address in AWS's published IP ranges. Where does her complaint go?

- **A.** A technical case in AWS Support Center
- **B.** An account and billing case in Support Center
- **C.** A post on AWS re:Post that names the website
- **D.** AWS Trust & Safety, through the abuse form

<details><summary>Answer</summary>

**D is right.** Copied content on an AWS resource is abuse, which Trust & Safety handles.

- **A and B are wrong.** AWS Support can't help with abuse reports, whatever the case type.
- **C is wrong.** Nobody on re:Post can act on another customer's resource.

</details>

**A8.** A city's IT team on Basic asks: (1) Why does our invoice include a charge for a Region we never use? (2) How should we organize moving 40 servers to AWS over a year? (3) What did AWS announce this month for Amazon RDS? Where does each go?

- **A.** (1) a case in Support Center; (2) Prescriptive Guidance; (3) the AWS News Blog
- **B.** (1) AWS re:Post; (2) the Knowledge Center; (3) a case in Support Center
- **C.** (1) Prescriptive Guidance; (2) a case in Support Center; (3) AWS whitepapers
- **D.** (1) a case in Support Center; (2) AWS re:Post; (3) the Knowledge Center

<details><summary>Answer</summary>

**A is right.** The charge needs an account and billing case, which Basic can open; a year-long plan is a Prescriptive Guidance job; announcements are on the News Blog.

- **B, C and D are wrong.** re:Post and Prescriptive Guidance can't see one account's invoice, community answers aren't AWS's plan, and AWS announces features on its blog, not in cases or the Knowledge Center.

</details>

**A9.** An insurer wants (1) a free design review by an AWS expert, (2) AWS's own consultants to run a migration under contract, and (3) another company to patch its servers nightly. Who provides each?

- **A.** (1) a solutions architect; (2) AWS Professional Services; (3) an AWS Partner
- **B.** (1) AWS Support; (2) a solutions architect; (3) AWS Professional Services
- **C.** (1) AWS Professional Services; (2) an AWS Partner; (3) AWS Support
- **D.** (1) a solutions architect; (2) an ISV's product in AWS Marketplace; (3) AWS Support

<details><summary>Answer</summary>

**A is right.** Solutions architects advise for free, Professional Services is AWS's paid consultancy, and partners are other companies.

- **B is wrong.** Support doesn't review designs, and Professional Services is AWS, not another company.
- **C is wrong.** Professional Services isn't free, and Support doesn't patch your servers.
- **D is wrong.** A product isn't a consultant, and Support doesn't run your systems.

</details>

**A10.** A media group subscribes to a third-party product through AWS Marketplace. Which two statements are correct? (Select TWO.)

- **A.** The product's charges arrive on the group's AWS bill.
- **B.** AWS becomes responsible for securing the product's settings.
- **C.** The group still configures and secures the product itself.
- **D.** Private Marketplace now controls what software can run in its accounts.
- **E.** AWS Support will administer the product on any paid plan.

<details><summary>Answer</summary>

**A and C are right.** Marketplace changes whom you pay, not who configures the product.

- **B is wrong.** The shared responsibility line doesn't move.
- **D is wrong.** Private Marketplace limits subscriptions, not deployments.
- **E is wrong.** AWS Support doesn't administer customers' systems.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 12.01a | [Each paid plan adds speed and people](01-support-plans.md#each-paid-plan-adds-speed-and-people) |
| A2, B2 | 12.01a | [Older plan names](01-support-plans.md#older-material-uses-plan-names-that-are-being-retired) |
| A3, B3 | 12.01a | [Response times are targets](01-support-plans.md#response-times-are-targets-for-a-first-reply-not-guarantees) |
| A4, B4 | 12.02a | [The big picture: three tools](02-tools-that-watch-your-account.md#the-big-picture-three-tools-three-directions) |
| A5, B5 | 12.02a | [AWS Health](02-tools-that-watch-your-account.md#aws-health-reports-problems-on-awss-side-in-one-dashboard-with-two-views) |
| A6, B6 | 12.02a | [Trusted Advisor](02-tools-that-watch-your-account.md#trusted-advisor-checks-your-setup-in-six-categories-and-your-plan-sets-how-much-you-see) |
| A7, B7 | 12.03a | [Abuse goes to Trust & Safety](03-where-to-find-answers.md#abuse-from-an-aws-address-goes-to-aws-trust--safety-not-to-support) |
| A8, B8 | 12.03a | [AWS's free pages](03-where-to-find-answers.md#awss-free-pages-answer-how-does-this-work) and [Support Center](02-tools-that-watch-your-account.md#support-center-is-where-you-open-cases) |
| A9, B9 | 12.04a | [Who does the work](03-where-to-find-answers.md#when-you-need-people-ask-who-does-the-work) |
| A10, B10 | 12.04a | [AWS Marketplace](03-where-to-find-answers.md#aws-marketplace-sells-partners-products-with-three-services-for-buyers) |

## Check B: parallel retest

**B1.** A model railway club's website can wait for a volunteer to fix it at the weekend. The treasurer wants AWS to answer billing questions, and AWS Health events sent to a chat channel through Amazon EventBridge. Which is the cheapest plan that covers this?

- **A.** AWS Business Support+
- **B.** AWS Enterprise Support
- **C.** Basic Support
- **D.** AWS Unified Operations

<details><summary>Answer</summary>

**C is right.** Basic opens billing cases, and every plan can use EventBridge.

- **A is wrong.** It adds technical cases and the Health API, which the club doesn't need.
- **B and D are wrong.** Both are far beyond the club's needs.

</details>

**B2.** A 2022 checklist says: "Subscribe to Business Support so your engineers can phone AWS at any hour." A startup signing up today wants that. Which plan is cheapest?

- **A.** Business Support
- **B.** AWS Enterprise Support
- **C.** Basic Support
- **D.** AWS Business Support+

<details><summary>Answer</summary>

**D is right.** It's today's cheapest plan with technical cases 24/7.

- **A is wrong.** Business Support has taken no new subscriptions since 2025-12-02 and ends on 2027-01-01 (as of 2026-10-24).
- **B is wrong.** It costs far more and adds a TAM nobody asked for.
- **C is wrong.** Basic can't open technical cases.

</details>

**B3.** A payroll company has moved to Business Support+. Which two statements to staff are accurate? (Select TWO.)

- **A.** "We can open technical cases at any hour, by phone, web or chat."
- **B.** "AWS promises to fix any outage within the plan's fastest response time."
- **C.** "Response times are AWS's targets for its first reply to a case."
- **D.** "AWS engineers will sign in to our servers and repair them for us."
- **E.** "The response target is the same whichever severity we choose."

<details><summary>Answer</summary>

**A and C are right.**

- **B is wrong.** No plan promises a fix by a set time.
- **D is wrong.** AWS Support doesn't sign in to or administer customers' systems.
- **E is wrong.** Each severity has its own target.

</details>

**B4.** A ferry company on Basic asks: (1) Is an AWS service in our Region having trouble right now? (2) Are we close to our service quotas? (3) Can AWS explain a duplicate payment on our account? Which tools answer them, in order?

- **A.** (1) the AWS Health Dashboard; (2) Trusted Advisor; (3) an account and billing case
- **B.** (1) Trusted Advisor; (2) the AWS Health Dashboard; (3) a technical case
- **C.** (1) the AWS Health API; (2) Trusted Advisor; (3) an account and billing case
- **D.** (1) the AWS Health Dashboard; (2) a case in Support Center; (3) Trusted Advisor

<details><summary>Answer</summary>

**A is right.** The dashboard is free, Basic gets every service limits check, and billing questions are account and billing cases.

- **B is wrong.** It swaps the first two, and Basic can't open technical cases.
- **C is wrong.** The Health API needs a paid plan and is for programs.
- **D is wrong.** Support Center is where you ask for more quota, not where you see usage.

</details>

**B5.** A logistics company is on Basic. A contractor with no AWS sign-in must see whether AWS has a public event in Frankfurt, and the administrator wants events that affect the company's own instances. Which statement is right?

- **A.** Both must call the AWS Health API, which needs a paid plan.
- **B.** The contractor opens Service health; she signs in for the account's events.
- **C.** The contractor needs his own AWS account to see any event.
- **D.** She must buy Business Support+ to see events about her own instances.

<details><summary>Answer</summary>

**B is right.** Service health is public; Your account health appears after sign-in. Both are free.

- **A is wrong.** People use the free dashboard.
- **C is wrong.** Service health needs no account.
- **D is wrong.** Your account health is free on Basic too.

</details>

**B6.** A retailer moves from Business Support+ to Enterprise Support. What change to Trusted Advisor does the move bring?

- **A.** Trusted Advisor starts reporting AWS's planned maintenance
- **B.** Trusted Advisor closes open ports by itself
- **C.** The cost optimization checks appear for the first time
- **D.** Its account team picks the findings to work on first

<details><summary>Answer</summary>

**D is right.** That's Trusted Advisor Priority, only on Enterprise and Unified Operations.

- **A is wrong.** AWS Health reports maintenance.
- **B is wrong.** Trusted Advisor only reports.
- **C is wrong.** Business Support+ already shows every check.

</details>

**B7.** GuardDuty warns that a company's own access keys are launching instances nobody asked for. How should it get AWS's help?

- **A.** Report it to AWS Trust & Safety, because the instances run on AWS
- **B.** Wait for the AWS Health Dashboard to post an event
- **C.** Open a support case from that account, marked as an urgent security incident
- **D.** Rely on Trusted Advisor to turn the keys off

<details><summary>Answer</summary>

**C is right.** An intruder in your own account is a support case from that account.

- **A is wrong.** Trust & Safety handles abuse from other people's resources.
- **B is wrong.** AWS Health reports AWS's events, not a break-in.
- **D is wrong.** Trusted Advisor only reports.

</details>

**B8.** A charity on Basic asks: (1) What is the largest item one Amazon DynamoDB table can store? (2) Our EC2 instance stopped answering after a restart, a common problem; is there AWS's own step-by-step fix? (3) Where do we ask for a higher quota? Where does each go first?

- **A.** (1) the AWS News Blog; (2) AWS re:Post; (3) AWS Prescriptive Guidance
- **B.** (1) the Knowledge Center; (2) Prescriptive Guidance; (3) a technical case
- **C.** (1) the AWS documentation; (2) Prescriptive Guidance; (3) AWS re:Post
- **D.** (1) the AWS documentation; (2) the Knowledge Center; (3) a service limit increase case

<details><summary>Answer</summary>

**D is right.** Limits are in the documentation, common fixes in the Knowledge Center, and every plan can request quota.

- **A, B and C are wrong.** Blog posts are dated, Prescriptive Guidance plans bigger jobs, a quota request isn't a technical case, and re:Post can't raise quotas.

</details>

**B9.** Clinics on Business Support+ need (1) an AWS engineer to explain why their RDS database rejects connections, (2) a software company's backup product on the AWS bill, and (3) another company to build a data platform. Who provides each?

- **A.** (1) a solutions architect; (2) AWS Professional Services; (3) AWS Support
- **B.** (1) AWS Support; (2) an ISV's product in AWS Marketplace; (3) a system integrator
- **C.** (1) AWS Support; (2) a system integrator; (3) an ISV's product in AWS Marketplace
- **D.** (1) AWS Professional Services; (2) AWS Support; (3) a solutions architect

<details><summary>Answer</summary>

**B is right.** A technical case for the database; an ISV sells software; a system integrator builds systems.

- **A is wrong.** Support answers cases, and Professional Services doesn't sell software.
- **C is wrong.** It swaps the last two.
- **D is wrong.** Professional Services doesn't answer cases, and Support doesn't sell products.

</details>

**B10.** An engineering firm has several AWS accounts in one organization and buys software through AWS Marketplace. Which two needs can Marketplace's buyer features meet? (Select TWO.)

- **A.** Stop anyone deploying software that didn't come from Marketplace
- **B.** Let staff subscribe only to products the firm has approved
- **C.** Have each seller take over securing its product
- **D.** Have AWS Support administer every product the firm buys
- **E.** Share a subscription's license from one account with its other accounts

<details><summary>Answer</summary>

**B and E are right.** Private Marketplace is the governance feature, and License Manager shares entitlements.

- **A is wrong.** Private Marketplace blocks new subscriptions, not deployments.
- **C is wrong.** The firm secures what it buys.
- **D is wrong.** AWS Support doesn't administer customers' systems.

</details>

**Next:** [Module 13, "Moving to AWS"](../13-moving-to-aws/00-brief.md). **Beyond the exam:** [what this module left out](08-beyond-the-exam.md).

---

"Module 12 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
