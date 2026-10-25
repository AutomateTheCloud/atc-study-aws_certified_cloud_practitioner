---
type: lesson
id: clf-12-02
title: "Tools that watch your account"
tasks: ["4.3", "2.4"]
objectives: ["12.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 11, the guardrails primer and lesson 12.01; about 15 minutes; works on a phone"
prerequisites: [clf-12-01, clf-02-05, clf-03-05]
terms_introduced: [AWS Trusted Advisor, Trusted Advisor check, check category, Trusted Advisor Priority, AWS Health, AWS Health event, Service health, Your account health, AWS Health API, AWS Support Center, service quota]
pillars: [operational-excellence, reliability, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html"
  - "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/"
  - "https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html"
  - "https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html"
  - "https://aws.amazon.com/about-aws/whats-new/2022/02/aws-health-dashboard-first-iteration/"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
---

# Trusted Advisor checks what you built, AWS Health reports what AWS runs, and Support Center is where you ask a person

Three tools keep an eye on your account, and each looks in a different direction. Trusted Advisor compares your setup with AWS's best practices, AWS Health tells you when something on AWS's side affects you, and Support Center is where you open a case. Your Support plan decides how much of each you get.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** read [Support plans](01-support-plans.md) first. You met the AWS Health Dashboard in [Lab 02](../03-aws-around-the-world/05-lab-02-see-the-global-infrastructure.md).

## Warm-up: what you remember

1. From lesson 02.05: what is the difference between the AWS Well-Architected Tool and AWS Trusted Advisor?

<details><summary>Feedback</summary>

1. **The Well-Architected Tool** is a question-by-question review of one workload that you run, against the Framework's pillars. **Trusted Advisor** runs automatic checks on the resources in your account, grouped into categories, not pillars.

</details>

## What you'll learn

By the end of this lesson, you can say what Trusted Advisor, AWS Health and Support Center each show, and how much of each your Support plan gives you (objective 12.02a).

Try this before you read on, and guess if you're unsure: how many Trusted Advisor checks does an account on the free Basic plan get?

## The big picture: three tools, three directions

![Three cards. On your side of a dashed line: AWS Trusted Advisor, which reads your account's settings and asks whether anything is wasteful, risky or near a limit; and AWS Support Center, where you ask a person at AWS for help. On AWS's side, highlighted: AWS Health, which reports AWS's own events, such as issues and planned maintenance. Under them, the bakery's account feeds Trusted Advisor, and AWS's services, Regions and data centers feed AWS Health.](../../images/12-02-big-picture.svg)

*Notice which side each tool looks at. Trusted Advisor can't tell you AWS is having an outage, and AWS Health can't tell you your bucket is open to the world.*

**Long description.** A dashed line splits the picture into your side, your account and its resources, on the left, and AWS's side on the right. On your side: AWS Trusted Advisor answers "Is anything in our setup wasteful, risky or near a limit?" It checks your settings against AWS's best practices in six categories; Basic gets some checks and paid plans all of them. An arrow labeled "reads settings" runs up to it from the bakery's account: the EC2 web servers, the RDS orders database, Lambda functions, the S3 photo bucket and the VPC. AWS Support Center answers "We need a person at AWS to help." It is where you open cases and request quota increases; Basic gets account, billing and quota cases, and paid plans technical cases too. On AWS's side, highlighted: AWS Health answers "Is AWS having a problem that affects us?" It reports AWS's own events, such as issues, planned maintenance and account notices; its dashboard is free for everyone, and its API needs a paid plan. An arrow labeled "reports events" runs up to it from AWS's services, Regions and data centers.

## Trusted Advisor checks your setup in six categories, and your plan sets how much you see

**AWS Trusted Advisor** inspects your account and recommends changes where you could save money, improve availability or performance, or close a security gap ([AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html), checked 2026-10-24). Each test it runs is a **Trusted Advisor check**, and the checks fall into six **check categories** ([check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html), checked 2026-10-24):

| Category | What it looks for | One example check |
|---|---|---|
| **Cost optimization** | Money spent on things you don't use | Low utilization Amazon EC2 instances |
| **Performance** | Resources working too hard, or slower than they could be | High CPU Utilization Amazon EC2 Instances |
| **Security** | Settings that leave a door open | MFA on root account |
| **Fault tolerance** | Single points of failure, missing backups | Amazon RDS Multi-AZ |
| **Service limits** | Usage close to a **service quota**, the most of something an account may use | One check per quota it watches |
| **Operational excellence** | Missing logs and operating practices | Amazon VPC Without Flow Logs |

Many older sources list only five categories, leaving out operational excellence, and AWS's product page calls fault tolerance "resilience". Trusted Advisor only reports: if it flags an open port, you fix the security group.

- **Basic:** every service limits check, plus a few chosen security checks (such as root MFA, S3 bucket permissions and public EBS or RDS snapshots) and one fault tolerance check.
- **Business Support+ and up:** all checks in all six categories, refreshed automatically, with the Trusted Advisor API.
- **Enterprise Support and Unified Operations** add **Trusted Advisor Priority**: your AWS account team picks out the recommendations that matter most for you ([Trusted Advisor product page](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), checked 2026-10-24).

### "Basic gets a fixed number of checks" is wrong

You may have learned that Basic gets a set number of "core checks". It doesn't: AWS defines the rule above, and the count behind it changes as AWS adds and retires checks. When we checked, three AWS pages each gave a different total. A number is tempting because it's easy to memorize, but learn the rule and read the count from the live page when you need it. That answers the prequestion.

## AWS Health reports problems on AWS's side, in one dashboard with two views

**AWS Health** reports **AWS Health events**: a service having trouble in a Region, maintenance AWS has planned on hardware your resources use, or a notice about your account ([What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html), checked 2026-10-24). The **AWS Health Dashboard** is free for every customer and has two views ([AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html)):

- **Service health** is public: anyone can open it, without signing in. It shows events for every service and Region, with 12 months of history.
- **Your account health** appears after you sign in, and shows events that affect your own resources, such as maintenance planned on a server you run.

People use the dashboard. Programs use the **AWS Health API**, which needs Business Support+, Enterprise or Unified Operations. Every plan can also send Health events to its own tools through Amazon EventBridge at no extra cost.

### "The Personal and Service Health Dashboards are separate products" is out of date

You may have read about two dashboards: a Service Health Dashboard for AWS's overall status and a Personal Health Dashboard for your account. On 2022-02-28, AWS announced a single AWS Health Dashboard that brings them together ([What's New post](https://aws.amazon.com/about-aws/whats-new/2022/02/aws-health-dashboard-first-iteration/)). The old names survive in older material and on a few AWS pages, which keeps the idea alive. If an answer names either one, read it as the matching view: Service health or Your account health.

## Support Center is where you open cases

**AWS Support Center** is where you ask AWS for help, in one of three case types ([Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html), checked 2026-10-24):

| Case type | For | Who can open it |
|---|---|---|
| **Account and billing** | Your account, charges and payments | Every plan, Basic included |
| **Service limit increase** | A higher service quota | Every plan, Basic included |
| **Technical** | How a service behaves, from AWS engineers | Business Support+ and higher only |

Any IAM identity with the right permissions can open a case; the root user isn't needed. Trusted Advisor warns you that a quota is near; Support Center, or the Service Quotas console, is where you ask for more.

> **Your turn:** match each of the bakery's questions to Trusted Advisor, AWS Health or Support Center. (a) "Is AWS having trouble in N. Virginia right now?" (b) "Are we paying for an Elastic IP address attached to nothing?" (c) "There's a charge on our bill we don't recognize."

<details><summary>Model answer</summary>

(a) **AWS Health**, the Service health view: AWS's side, free on every plan. (b) **Trusted Advisor**, a cost optimization check, which needs Business Support+ or higher. (c) **Support Center**, an account and billing case, which Basic can open.

</details>

## Summary

- **Trusted Advisor checks what you built** in six categories: cost optimization, performance, security, fault tolerance, service limits and operational excellence. It reports; you fix.
- **Basic sees** all service limits checks and a few security and fault tolerance checks; **paid plans** see all checks and the API; **Enterprise and Unified Operations** add Trusted Advisor Priority. Don't learn a count.
- **AWS Health reports what AWS runs:** one free dashboard with two views, Service health (public) and Your account health (signed in). The Health API is for programs and needs a paid plan.
- **Support Center** takes account and billing and quota cases on every plan, and technical cases on paid plans.

## Practice

1. **Which AWS tool tells a company that AWS has scheduled maintenance on hardware that one of its EC2 instances uses?**

   A. AWS Trusted Advisor\
   B. AWS Health, in Your account health\
   C. AWS Support Center\
   D. AWS Health, in Service health only

   <details><summary>Feedback</summary>

   **B is right.** Planned maintenance on your resources is an account event, shown once you sign in.

   - **A is wrong.** Trusted Advisor checks your settings; it doesn't report AWS's events.
   - **C is wrong.** Support Center is for cases you open.
   - **D is wrong.** Service health shows public events that aren't about any one account.

   </details>

2. **A startup on Basic Support wants Trusted Advisor's recommendations for cutting costs. What must change?**

   A. Nothing: Basic includes all cost optimization checks\
   B. It must move to Business Support+ or higher\
   C. It must turn on AWS Health\
   D. It must enable Trusted Advisor Priority on Basic

   <details><summary>Feedback</summary>

   **B is right.** Cost optimization checks come with Business Support+ and higher.

   - **A is wrong.** Basic gets service limits and a few security and fault tolerance checks only.
   - **C is wrong.** AWS Health reports AWS's events, not savings.
   - **D is wrong.** Priority is only on Enterprise Support and Unified Operations.

   </details>

3. **A company's operations tool must read AWS Health events through the AWS Health API. What is the cheapest plan that allows it?**

   A. Basic\
   B. Business Support+\
   C. Enterprise Support\
   D. Unified Operations

   <details><summary>Feedback</summary>

   **B is right.** The Health API needs Business Support+ or higher.

   - **A is wrong.** Basic can't call the API, though it can receive Health events through EventBridge.
   - **C and D are wrong.** Both allow it, but cost more for things the company didn't ask for.

   </details>

**Next:** [Where to find answers](03-where-to-find-answers.md). To see these tools in your own account, do [Lab 17](05-lab-17-support-center-tour.md).

## Where to check the current details

- [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html), AWS Support User Guide: categories and plan access (checked 2026-10-24)
- [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) (checked 2026-10-24)
- [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html): case types (checked 2026-10-24)

---

"Tools that watch your account" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
