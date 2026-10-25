---
type: check
id: clf-12-07
title: "Module 12 mastery check"
tasks: ["4.3", "3.8", "2.4"]
objectives: ["12.01a", "12.02a", "12.03a", "12.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 12's lessons; about 30 minutes for Check A"
prerequisites: [clf-12-01, clf-12-02, clf-12-03, clf-12-04]
pillars: [operational-excellence, cost-optimization, security]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/premiumsupport/plans/"
  - "https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html"
  - "https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html"
  - "https://repost.aws/knowledge-center/report-aws-abuse"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html"
---

# Module 12 mastery check: choose the plan, the tool, the source and the people

This check tests whether you can do what Module 12 set out to teach: choose the cheapest Support plan that fits, say what each account tool shows and who gets it, send a question to the place that can answer it, and choose the right kind of paid help. Every question is a short situation, like the ones on the exam.

**For:** an adult studying alone, possibly new to IT, who has finished the four lessons of [Module 12](00-brief.md). **Time:** about 30 minutes for Check A, and the same for Check B if you need it.

## How to use this check

Take **Check A** closed-book: no lessons, notes or AWS pages. Answer all ten questions, then open the answers and count your score. A "(Select TWO.)" question counts as right only if you chose both correct answers, as on the exam. You pass at **80%**, which here is 8 of 10.

- **If you scored 8 or more:** you have passed. Read the feedback on anything you missed, then try the [enrichment tasks](#enrichment-for-learners-who-passed).
- **If you scored less than 8:** use the [correction map](#correction-map) to reread the exact section behind each miss, and redo the lab or simulation it names. Then take [Check B](#check-b-parallel-retest), which asks about the same objectives with new situations.

Prices, response times and plan names change. The questions don't depend on any price or count; where a fact is dated, the feedback gives the date we checked it.

## Check A

**A1.** A translation agency's client portal runs in one AWS account, and clients now upload work to it at all hours. The IT lead wants two things: to open technical cases with AWS engineers whenever the portal misbehaves, and to let the agency's own monitoring program read events from the AWS Health API. She doesn't need a named contact at AWS. Which is the cheapest Support plan that covers both needs?

- **A.** Basic Support
- **B.** AWS Business Support+
- **C.** AWS Enterprise Support
- **D.** AWS Unified Operations

<details><summary>Answer</summary>

**B is right.** Business Support+ is the first plan with technical cases around the clock, and the first that lets a program call the AWS Health API.

- **A is wrong.** Basic can't open technical cases, and the Health API refuses calls from a Basic account. (Basic can receive Health events through Amazon EventBridge, but the agency asked for the API.)
- **C is wrong.** Enterprise Support covers both needs, but its main addition is a designated Technical Account Manager, which the agency doesn't need, at a much higher fee.
- **D is wrong.** Unified Operations adds even more on top of Enterprise, such as domain specialists and 24/7 workload monitoring.

</details>

**A2.** A software company has been on Enterprise On-Ramp Support since 2024. Its finance lead is planning next year's budget, and the operations wiki still names On-Ramp as the company's plan. What should she expect, and plan for?

- **A.** The company drops to Basic unless it acts, so she budgets for no Support fee
- **B.** On-Ramp continues unchanged, so she budgets for the same plan as this year
- **C.** AWS moves the company to Unified Operations, which replaced On-Ramp
- **D.** AWS moves the company to Enterprise Support, so she budgets for that plan

<details><summary>Answer</summary>

**D is right.** Enterprise On-Ramp is being retired. During 2026, AWS is moving its customers to Enterprise Support automatically, and the plan ends on 2027-01-01 (as of 2026-10-24). The wiki should name Enterprise Support, and the budget should use its fee.

- **A is wrong.** Falling back to Basic is what happens to a Developer Support customer who doesn't choose a new plan. On-Ramp customers are moved for them.
- **B is wrong.** On-Ramp ends on 2027-01-01; it doesn't continue.
- **C is wrong.** Unified Operations is a new plan with no old plan behind it. Nobody is moved to it automatically.

</details>

**A3.** A hospital's IT manager has just moved its AWS accounts to Enterprise Support, and she is writing the hospital's outage runbook. Which two lines belong in it? (Select TWO.)

- **A.** "AWS guarantees that a business-critical outage is fixed within the plan's response time."
- **B.** "Use the highest severities only for problems we can't work around, or that hit production."
- **C.** "Technical cases opened at night wait until the next business day."
- **D.** "Our own recovery plan must not depend on AWS fixing a problem by a set time."
- **E.** "Only the root user may open a case at the highest severity."

<details><summary>Answer</summary>

**B and D are right.** AWS asks customers to keep the highest severities for problems they can't work around or that directly affect production. And because response times are targets for a first reply, not promises of a fix, the hospital must plan its own recovery, as Module 03 did with "design for failure".

- **A is wrong.** Response times are targets that AWS makes "every reasonable effort" to meet, and they measure the first reply, not the fix.
- **C is wrong.** Every paid plan, Enterprise included, takes technical cases 24/7.
- **E is wrong.** Any IAM identity with the right permissions can open a case, at any severity. The root user isn't needed.

</details>

**A4.** A cinema chain's cloud team is on Business Support+. This week it has three questions:

1. Is AWS planning maintenance on the hardware under one of our EC2 instances?
2. Are we paying for EBS volumes that we hardly use?
3. Why does an AWS API keep returning throttling errors to our app? We'd like an AWS engineer to explain.

Which tools answer them, in order?

- **A.** (1) Trusted Advisor; (2) AWS Health; (3) AWS re:Post
- **B.** (1) a technical case in Support Center; (2) Trusted Advisor; (3) AWS Health
- **C.** (1) AWS Health; (2) Trusted Advisor; (3) a technical case in Support Center
- **D.** (1) AWS Health; (2) Support Center; (3) Trusted Advisor

<details><summary>Answer</summary>

**C is right.** AWS Health reports what AWS runs, including maintenance planned on your resources, in the dashboard's Your account health view. Trusted Advisor checks what you built; its cost optimization checks flag underused EBS volumes, and the paid plan shows them. Support Center is where you ask a person, and Business Support+ can open technical cases.

- **A is wrong.** It swaps the first two tools: Trusted Advisor reads your settings and can't see AWS's maintenance plans, and AWS Health doesn't judge your spending. re:Post is public and can't look at your account.
- **B is wrong.** AWS announces maintenance through AWS Health, not in a support case, and AWS Health doesn't answer questions.
- **D is wrong.** Support Center doesn't scan your resources, and Trusted Advisor doesn't explain errors.

</details>

**A5.** A journalist with no AWS account wants to see whether AWS reported a problem with a service in one Region last month. Where can she look?

- **A.** The AWS Health API, once her newspaper buys Business Support+
- **B.** The AWS Health Dashboard's Service health view, which anyone can open
- **C.** The Your account health view, which lists every customer's events
- **D.** AWS Support Center, by opening an account and billing case

<details><summary>Answer</summary>

**B is right.** Service health is the public view of the AWS Health Dashboard: no sign-in and no AWS account needed, with public events for every service and Region and a history of the last 12 months. Older material calls it the Service Health Dashboard, as if it were a separate product.

- **A is wrong.** The Health API is for programs, and it needs a paid plan on the account that calls it. She has no account, and public events are free to read anyway.
- **C is wrong.** Your account health shows events for your own resources, after you sign in, never other customers' events.
- **D is wrong.** She has no account to open a case from, and a support case isn't where AWS publishes service events.

</details>

**A6.** Two companies open AWS Trusted Advisor on the same day. One is on Basic Support; the other has just moved to Business Support+. What does the second company see that the first doesn't?

- **A.** All the service limits checks, which Basic lacks
- **B.** Trusted Advisor Priority, from its account team
- **C.** Automatic fixes for the findings it flags
- **D.** Every check, in all six categories

<details><summary>Answer</summary>

**D is right.** Basic sees every service limits check plus a few chosen security and fault tolerance checks, and no cost optimization checks at all. Business Support+ and the plans above it see all checks, refreshed automatically, with the Trusted Advisor API. The number of checks changes as AWS adds and retires them, so learn this rule rather than a count.

- **A is wrong.** Basic already includes every service limits check.
- **B is wrong.** Trusted Advisor Priority comes only with Enterprise Support and Unified Operations.
- **C is wrong.** Trusted Advisor only reports, on every plan. The customer makes the fix.

</details>

**A7.** A wedding photographer finds dozens of her photos copied, without her permission, onto a website whose address is in AWS's published IP address ranges. She runs her own portfolio site on AWS, on the Basic plan. Where should she send her complaint?

- **A.** A technical case in AWS Support Center
- **B.** An account and billing case in Support Center
- **C.** A post on AWS re:Post that names the website
- **D.** AWS Trust & Safety, through the abuse form

<details><summary>Answer</summary>

**D is right.** Content hosted on an AWS resource that harms someone, including copyright takedown requests, is abuse, and AWS Trust & Safety handles it. She includes the URL and a description of the content.

- **A and B are wrong.** AWS Support can't help with abuse reports, on any plan, whichever case type you choose. (Basic can't open technical cases anyway.)
- **C is wrong.** re:Post is a public question-and-answer site; nobody there can act on another customer's resource.

</details>

**A8.** A city's IT team is on Basic Support, and it has three questions:

1. Why does our latest invoice include a charge for a Region we never use?
2. We plan to move 40 on-premises servers to AWS over a year. How should we organize the work?
3. What did AWS announce this month for Amazon RDS?

Where should the team take each question?

- **A.** (1) a case in Support Center; (2) Prescriptive Guidance; (3) the AWS News Blog
- **B.** (1) AWS re:Post; (2) the Knowledge Center; (3) a case in Support Center
- **C.** (1) Prescriptive Guidance; (2) a case in Support Center; (3) AWS whitepapers
- **D.** (1) a case in Support Center; (2) AWS re:Post; (3) the Knowledge Center

<details><summary>Answer</summary>

**A is right.** The charge depends on the city's own bill, so only an account and billing case can answer it, and Basic can open one. A year-long migration plan is the kind of "we want to…" job that AWS Prescriptive Guidance's guides are written for. Announcements are dated posts on the AWS News Blog.

- **B is wrong.** re:Post is public and can't see the city's bill; the Knowledge Center answers common errors, not a year-long plan; and a support case isn't where AWS announces features.
- **C is wrong.** Prescriptive Guidance can't explain a charge on one account's invoice, and a migration plan isn't a support case. Whitepapers are long papers on a topic, not this month's news.
- **D is wrong.** The first step is right, but community answers aren't a plan written by AWS experts, and Knowledge Center articles answer common problems, not announcements.

</details>

**A9.** An insurance company's IT director wants three things:

1. An AWS expert to review the company's architecture design, at no charge.
2. AWS's own consultants to carry out a migration, under a contract.
3. Another company to monitor and patch the company's servers every night, as an ongoing service.

Who provides each?

- **A.** (1) a solutions architect; (2) AWS Professional Services; (3) a managed services partner
- **B.** (1) AWS Support; (2) a solutions architect; (3) AWS Professional Services
- **C.** (1) AWS Professional Services; (2) a managed services partner; (3) AWS Support
- **D.** (1) a solutions architect; (2) an ISV's product in AWS Marketplace; (3) AWS Support

<details><summary>Answer</summary>

**A is right.** Solutions architects advise on design at no charge, through the account team or AWS's contact form. Professional Services is AWS's own consulting organization, hired under a contract. Ongoing operation by another company is a managed service from an AWS Partner.

- **B is wrong.** AWS Support fixes problems with AWS services; it doesn't review designs. A solutions architect advises but doesn't carry out projects. And Professional Services is AWS, not another company.
- **C is wrong.** Professional Services is paid, not a free review, and AWS Support doesn't run or patch your systems.
- **D is wrong.** A software product isn't AWS's consultants, and AWS Support doesn't administer customers' servers.

</details>

**A10.** A media group subscribes to a third-party video-processing product through AWS Marketplace. Which two statements about that purchase are correct? (Select TWO.)

- **A.** The product's charges arrive on the group's AWS bill.
- **B.** AWS becomes responsible for securing the product's settings.
- **C.** The group still configures and secures the product itself.
- **D.** Private Marketplace now controls what software can run in its accounts.
- **E.** AWS Support will administer the product on any paid plan.

<details><summary>Answer</summary>

**A and C are right.** Marketplace charges appear on the buyer's AWS bill, and AWS then pays the seller. Buying through Marketplace changes whom you pay, not who configures the product: that stays the customer's job.

- **B is wrong.** The shared responsibility line doesn't move because of where you bought the software.
- **D is wrong.** Private Marketplace limits which products people can subscribe to. It doesn't control what can be deployed, so IAM permissions still matter.
- **E is wrong.** AWS Support doesn't administer customers' systems, whatever the plan.

</details>

## Correction map

For each question you missed, reread the section named, then try the explanation in the last column, which puts the idea a different way. Then redo the practice named.

| Question | Objective | Reread | Practice | Another way to see it |
|---|---|---|---|---|
| A1 | 12.01a Choose the cheapest plan that fits | [Business Support+ adds technical help around the clock](01-support-plans.md#business-support-adds-technical-help-around-the-clock) and [AWS Health reports problems on AWS's side](02-tools-that-watch-your-account.md#aws-health-reports-problems-on-awss-side-through-one-dashboard-with-two-views) | [Simulation S15](06-sim-support-plan-chooser.md), decisions 1 to 3 | Write each need on its own line, cross out every plan that misses one, and take the cheapest plan left. |
| A2 | 12.01a | [Older material uses plan names that are being retired](01-support-plans.md#older-material-uses-plan-names-that-are-being-retired) | The old-names diagram in that section | Each old plan has one path: the two with "Developer" and "Business" in their names need the customer to choose Business Support+, and Enterprise On-Ramp is moved to Enterprise Support for its customers. |
| A3 | 12.01a | [Response times are targets for a first reply, not guarantees](01-support-plans.md#response-times-are-targets-for-a-first-reply-not-guarantees) | [Simulation S15](06-sim-support-plan-chooser.md), decision 3 | A response target is like a promise that someone will pick up the phone soon, not that the problem will be solved soon. |
| A4 | 12.02a Say what each tool shows, and who gets it | [Pick the tool by the question you're asking](02-tools-that-watch-your-account.md#pick-the-tool-by-the-question-youre-asking) | [Lab 17](05-lab-17-support-center-tour.md), stops 2 to 4 | Ask which way the tool looks: at your setup (Trusted Advisor), at AWS's side (AWS Health), or at a person (Support Center). |
| A5 | 12.02a | [AWS Health reports problems on AWS's side, through one dashboard with two views](02-tools-that-watch-your-account.md#aws-health-reports-problems-on-awss-side-through-one-dashboard-with-two-views) | [Lab 17](05-lab-17-support-center-tour.md), stop 3 | One dashboard, two views: the public view anyone can open, like a public notice board, and the view of your own account after you sign in. |
| A6 | 12.02a | [What you see in Trusted Advisor depends on your Support plan](02-tools-that-watch-your-account.md#what-you-see-in-trusted-advisor-depends-on-your-support-plan) | [Lab 17](05-lab-17-support-center-tour.md), stop 4 | Basic gets the checks that stop you hitting a wall (quotas) and the most dangerous security gaps; the money-saving checks are what a paid plan buys. |
| A7 | 12.03a Route a question to the right place | [Abuse from an AWS address goes to AWS Trust & Safety, not to Support](03-where-to-find-answers.md#abuse-from-an-aws-address-goes-to-aws-trust--safety-not-to-support) | [Lab 17](05-lab-17-support-center-tour.md), stop 5 | Ask whose resource is misbehaving. Someone else's resource harming you goes to Trust & Safety; only trouble inside your own account is a support case. |
| A8 | 12.03a | [Support Center is the only door about your own account](03-where-to-find-answers.md#support-center-is-the-only-door-about-your-own-account) and [Prescriptive Guidance is for planning and building](03-where-to-find-answers.md#prescriptive-guidance-is-for-planning-and-building-not-for-fixing-one-error), and the blogs row in [AWS's own pages explain how AWS works](03-where-to-find-answers.md#awss-own-pages-explain-how-aws-works-documentation-whitepapers-and-blogs) | [Lab 17](05-lab-17-support-center-tour.md), the Recap's routing table | "Depends on my account?" sends it to Support Center. "We want to…" sends it to Prescriptive Guidance. "What's new?" sends it to the News Blog. |
| A9 | 12.04a Choose the right kind of paid help | [Compare them side by side](04-partners-and-paid-help.md#professional-services-partners-support-or-a-solutions-architect-compare-them-side-by-side) | The lesson's [worked example](04-partners-and-paid-help.md#worked-example-five-requests-five-kinds-of-help) | Two questions sort it: is it AWS or another company, and do they advise or do the work? |
| A10 | 12.04a | [AWS Marketplace sells partners' products, with three services for the buyer](04-partners-and-paid-help.md#aws-marketplace-sells-partners-products-with-three-services-for-the-buyer) | [Lab 17](05-lab-17-support-center-tour.md), stop 6 | Marketplace is a shop with an AWS checkout: it changes how you pay, not who looks after what you bought. |

## Check B: parallel retest

Take Check B after you've reread and practiced. It tests the same objectives as Check A, one for one, with new situations. You pass at 8 of 10.

**B1.** A model railway club runs its members' website on AWS. If the site breaks, members wait until a volunteer fixes it at the weekend, using AWS's documentation and re:Post. The treasurer wants AWS to answer questions about the club's bill, and wants AWS Health events sent to the club's chat channel automatically through Amazon EventBridge. Which is the cheapest Support plan that covers this?

- **A.** AWS Business Support+
- **B.** AWS Enterprise Support
- **C.** Basic Support
- **D.** AWS Unified Operations

<details><summary>Answer</summary>

**C is right.** Basic, free on every account, opens account and billing cases, and every plan can receive AWS Health events through EventBridge. Nothing the club needs is a technical case.

- **A is wrong.** Business Support+ would add 24/7 technical cases and the Health API, which the club doesn't need: its fixes can wait for the weekend.
- **B is wrong.** Enterprise Support adds a designated Technical Account Manager, far beyond the club's needs.
- **D is wrong.** Unified Operations is for mission-critical systems where minutes matter.

</details>

**B2.** A vendor's onboarding checklist from 2022 tells new customers: "Subscribe to Business Support so that your engineers can phone AWS at any hour." A retail startup that signs up with AWS today wants exactly that. Which plan should it choose at the lowest cost?

- **A.** Business Support
- **B.** AWS Enterprise Support
- **C.** Basic Support
- **D.** AWS Business Support+

<details><summary>Answer</summary>

**D is right.** Business Support+ is today's cheapest plan with technical cases 24/7 by phone, web and chat.

- **A is wrong.** Business Support has taken no new subscriptions since 2025-12-02, and it ends on 2027-01-01 (as of 2026-10-24). Its customers move to Business Support+ if they choose to.
- **B is wrong.** Enterprise Support also has 24/7 technical cases, but it costs far more and adds a TAM the startup didn't ask for.
- **C is wrong.** Basic can't open technical cases.

</details>

**B3.** A payroll company has just moved to Business Support+. Its manager drafts a note to staff about using AWS Support. Which two statements in the note are accurate? (Select TWO.)

- **A.** "We can open technical cases at any hour, by phone, web or chat."
- **B.** "AWS promises to fix any outage within the plan's fastest response time."
- **C.** "Response times are AWS's targets for its first reply to a case."
- **D.** "AWS engineers will sign in to our servers and repair them for us."
- **E.** "The response target is the same whichever severity we choose."

<details><summary>Answer</summary>

**A and C are right.** Business Support+ adds technical cases 24/7 by phone, web and chat. Its response times are targets for a first reply, which AWS makes every reasonable effort to meet.

- **B is wrong.** No plan promises a fix by a set time; the times are targets, and they're about the first reply.
- **D is wrong.** AWS Support doesn't sign in to customers' systems or administer them, on any plan.
- **E is wrong.** Each severity has its own target, from general guidance up to a business-critical system down.

</details>

**B4.** A ferry company's cloud team is on Basic Support. It has three questions before its busy season:

1. Is an AWS service in our Region having trouble right now?
2. Are we close to our service quotas?
3. Can AWS customer service explain a duplicate payment on our account?

Which tools answer them, in order?

- **A.** (1) the AWS Health Dashboard; (2) Trusted Advisor; (3) an account and billing case
- **B.** (1) Trusted Advisor; (2) the AWS Health Dashboard; (3) a technical case
- **C.** (1) the AWS Health API; (2) Trusted Advisor; (3) an account and billing case
- **D.** (1) the AWS Health Dashboard; (2) a case in Support Center; (3) Trusted Advisor

<details><summary>Answer</summary>

**A is right.** The AWS Health Dashboard is free on every plan and shows AWS's side. Trusted Advisor's service limits checks are all included on Basic. A payment question is an account and billing case in Support Center, which every plan can open.

- **B is wrong.** It swaps the first two tools, and a billing question isn't a technical case (which Basic can't open anyway).
- **C is wrong.** Only the first step is wrong: the Health API needs a paid plan, and it's for programs. On Basic, people use the free dashboard.
- **D is wrong.** Support Center is where you ask for a higher quota, not where you see how close you are, and Trusted Advisor doesn't answer billing questions.

</details>

**B5.** A logistics company is on Basic Support. Its administrator wants to know whether AWS has a public event in the Frankfurt Region, and a contractor who has no AWS sign-in must be able to see that too. She also wants to see any event that affects the company's own instances. Which statement is right?

- **A.** Both must call the AWS Health API, which needs a paid Support plan.
- **B.** The contractor opens Service health; she signs in for the account's events.
- **C.** The contractor must have his own AWS account to see any AWS Health event.
- **D.** She must buy Business Support+ to see events about the company's own instances.

<details><summary>Answer</summary>

**B is right.** The AWS Health Dashboard's Service health view is public, with no sign-in. Its Your account health view shows events about your own resources once you sign in. Both are free on every plan.

- **A is wrong.** The Health API is for programs, and people use the dashboard, which needs no paid plan.
- **C is wrong.** Service health needs no AWS account.
- **D is wrong.** Your account health is free on Basic too.

</details>

**B6.** A retailer is about to move from Business Support+ to Enterprise Support. A colleague says, "Then Trusted Advisor will finally start working for us." What change to Trusted Advisor does the move actually bring?

- **A.** Trusted Advisor starts reporting AWS's planned maintenance
- **B.** Trusted Advisor closes open ports in security groups by itself
- **C.** The cost optimization checks appear for the first time
- **D.** Its account team picks the findings to work on first

<details><summary>Answer</summary>

**D is right.** That's Trusted Advisor Priority, which comes only with Enterprise Support and Unified Operations. Everything else in Trusted Advisor, every check with the API, already came with Business Support+.

- **A is wrong.** AWS's planned maintenance is reported by AWS Health, not Trusted Advisor, on every plan.
- **B is wrong.** Trusted Advisor only reports, on every plan; the customer makes the fix.
- **C is wrong.** Business Support+ already shows every check, cost optimization included.

</details>

**B7.** Amazon GuardDuty alerts a company that its own access keys are being used from an unfamiliar country to launch EC2 instances that nobody asked for. The account is on Basic Support. How should the company get AWS's help?

- **A.** Report it to AWS Trust & Safety, because the instances run on AWS
- **B.** Wait for the AWS Health Dashboard to post an event about it
- **C.** Open a case from that account, marked as an urgent security incident
- **D.** Rely on Trusted Advisor to find the keys and turn them off

<details><summary>Answer</summary>

**C is right.** Someone inside your own account is a support case, opened from the affected account so that AWS can confirm you own it, and marked as an urgent security incident. The AWS Customer Incident Response Team (AWS CIRT) can help at no extra charge, whatever the Support plan. Basic can't open technical cases, so if no technical option is offered, an account and billing case that says the same thing is the lesson's reading (as of 2026-10-24).

- **A is wrong.** Trust & Safety handles abuse coming from other people's AWS resources, and notices about yours. An intruder in your own account is a support case.
- **B is wrong.** AWS Health reports AWS's own events, not a break-in to one customer's account.
- **D is wrong.** Trusted Advisor only reports, and the company must act now.

</details>

**B8.** A charity is on Basic Support, and it has three questions:

1. What is the largest item that one Amazon DynamoDB table can store?
2. Our EC2 instance stopped answering after a restart, a problem many customers report. Is there AWS's own step-by-step fix?
3. We need a higher quota for one resource before our appeal week. Where do we ask?

Where does each question go first?

- **A.** (1) the AWS News Blog; (2) AWS re:Post; (3) AWS Prescriptive Guidance
- **B.** (1) the Knowledge Center; (2) Prescriptive Guidance; (3) a technical case in Support Center
- **C.** (1) the AWS documentation; (2) Prescriptive Guidance; (3) AWS re:Post
- **D.** (1) the AWS documentation; (2) the Knowledge Center; (3) a service limit increase case

<details><summary>Answer</summary>

**D is right.** Limits are reference facts that AWS keeps current in each service's documentation. The Knowledge Center holds AWS's official articles on the problems customers ask about most. A quota increase can be requested on every plan, in Support Center (or the Service Quotas console).

- **A is wrong.** A blog post is dated and may describe an old limit. re:Post's community answers vary, and an AWS-written article is the better source when one exists. Prescriptive Guidance doesn't raise quotas.
- **B is wrong.** The Knowledge Center answers common problems, not reference limits; Prescriptive Guidance is for planning bigger jobs; and a quota request isn't a technical case.
- **C is wrong.** The first step is right, but Prescriptive Guidance doesn't troubleshoot one instance, and nobody on re:Post can raise the charity's quota.

</details>

**B9.** A chain of clinics, on Business Support+, has three needs:

1. An AWS engineer to explain why its Amazon RDS database rejects connections.
2. A ready-made backup product, made by a software company and billed on the AWS bill.
3. Another company to design and build a new data platform for it.

Who provides each?

- **A.** (1) a solutions architect; (2) AWS Professional Services; (3) AWS Support
- **B.** (1) AWS Support; (2) an ISV's product in AWS Marketplace; (3) a system integrator
- **C.** (1) AWS Support; (2) a system integrator; (3) an ISV's product in AWS Marketplace
- **D.** (1) AWS Professional Services; (2) AWS Support; (3) a solutions architect

<details><summary>Answer</summary>

**B is right.** A problem with an AWS service is a technical case for AWS Support, which the clinics' paid plan allows. A software product from an independent software vendor (ISV) is bought in AWS Marketplace, on the AWS bill. A company that designs and builds systems for its customers is, in the exam's words, a system integrator.

- **A is wrong.** A solutions architect advises on design; it's AWS Support that answers cases. Professional Services sells consulting, not backup software. AWS Support doesn't build platforms.
- **C is wrong.** It swaps the last two: a system integrator sells services, and an ISV sells software.
- **D is wrong.** Professional Services runs projects, not support cases; AWS Support doesn't sell products; and a solutions architect doesn't build the platform.

</details>

**B10.** An engineering firm has several AWS accounts in one organization, and its staff buy software through AWS Marketplace. Which two needs can Marketplace's features for buyers meet? (Select TWO.)

- **A.** Stop anyone deploying software that didn't come from Marketplace
- **B.** Let staff subscribe only to products that the firm has approved
- **C.** Have each seller take over securing its product in the firm's accounts
- **D.** Have AWS Support administer every product the firm buys
- **E.** Share a machine-image subscription from one account with its other accounts

<details><summary>Answer</summary>

**B and E are right.** Private Marketplace, the governance feature, gives each part of the organization a catalog of approved products. Entitlement works through AWS License Manager, which shares a subscription's licenses with the organization's other accounts.

- **A is wrong.** Private Marketplace blocks new subscriptions to unapproved products, but it doesn't control what can be deployed. IAM permissions do that.
- **C is wrong.** The firm configures and secures what it buys; the seller doesn't take that over.
- **D is wrong.** AWS Support doesn't administer customers' systems.

</details>

## Enrichment for learners who passed

These tasks go past the exam. Each has no single right answer; compare yours with the model answer.

**E1. A plan for six accounts.** A company has six AWS accounts in one organization: two production accounts that run its customer-facing shop, and four development accounts. The shop's team wants AWS engineers on the phone at any hour if the shop fails. The finance director says, "Let's buy Enterprise Support for everything, so we never have to think about it again." Write a short recommendation: which plan on which accounts, why, and what would make you change it. Link it to the Well-Architected best practice behind the decision.

<details><summary>Model answer</summary>

Put the two production accounts on **Business Support+** and leave the development accounts on **Basic**. Business Support+ is charged per account, so paying for it only where production depends on fast technical help is the cheapest fit. Development problems can wait for the documentation, the Knowledge Center and re:Post. Enterprise Support's main addition is a designated Technical Account Manager, plus Well-Architected reviews and included security incident response; nobody has asked for those, and its monthly minimum would buy far more than the company needs today.

Revisit the decision when a need appears that Business Support+ doesn't meet: the company wants a named AWS contact who knows its setup, it plans a big launch or migration and wants AWS's help planning it, or the bill grows enough that Enterprise's fee is a small share of it. This is [OPS07-BP06 Create support plans for production workloads](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_enable_support_plans.html): choose a level of support that matches each workload's needs, and write down how to request and escalate it. Buying more than that works against the cost optimization pillar.

</details>

**E2. When AWS's own pages lag.** The shop from E1 now buys AWS Shield Advanced and wants the Shield Response Team's help during a DDoS attack. A colleague reads AWS's Shield Response Team page, which names the "Business Support" or "Enterprise Support" plan, and concludes that Business Support+ certainly qualifies. What do you tell them, and what do you do before the next big sale?

<details><summary>Model answer</summary>

The page names a plan that is being retired, and when we checked (2026-10-24) it didn't yet say whether Business Support+ qualifies. So neither "it certainly qualifies" nor "it certainly doesn't" is safe. Before the sale, check the live page again, and if it still doesn't say, ask AWS in a support case and keep the written answer with the runbook. If the company needs certainty before AWS answers, the plan the page names that is still sold is Enterprise Support. Either way, the Shield Response Team is extra help, not the defense: AWS WAF rules, CloudFront and the shop's own scaling (Module 09) are what keep it running. This is the same habit as Trusted Advisor's check count: when AWS's pages lag or disagree, learn the rule, check the live page on the day you need it, and write down the date.

</details>

**E3. The "who do we call?" sheet.** Write a one-page escalation sheet for the shop's on-call staff, covering five events: an unknown charge, a suspected AWS outage, an attack from an address in AWS's ranges, unknown access keys in the shop's own account, and a request for a design review before a launch. For each, say where it goes and what to include.

<details><summary>Model answer</summary>

| Event | Where it goes | What to include |
|---|---|---|
| Unknown charge | An account and billing case in Support Center, after a look at the bill's details | The bill line and the account ID |
| Suspected AWS outage | The AWS Health Dashboard: Service health, then Your account health; an EventBridge rule sends Health events to the on-call channel | The Region, the services and the time you noticed |
| Attack from an AWS address | AWS Trust & Safety, through the abuse form; meanwhile block it with AWS WAF or a network ACL | Your target address, the time with its time zone, log lines |
| Unknown keys in our own account | A support case from that account, marked as an urgent security incident (AWS CIRT can help on any plan); then the steps in [primer page 08](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/08-when-something-goes-wrong.md) | What you found, and when |
| Design review before a launch | The Well-Architected Tool, and a solutions architect through the account team; a partner if the team wants a paid review | The design, the launch date and the main worries |

Keeping a list like this, including outside contacts, is [SEC10-BP01 Identify key personnel and external resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_identify_personnel.html), and agreeing in advance who handles what is [OPS10-BP04 Define escalation paths](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_define_escalation_paths.html).

</details>

**Next:** [Module 13, "Moving to AWS"](../13-moving-to-aws/00-brief.md).

---

"Module 12 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
