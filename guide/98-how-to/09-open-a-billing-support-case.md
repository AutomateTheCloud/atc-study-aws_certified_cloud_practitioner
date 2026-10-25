---
type: task-card
id: clf-98-09
title: "Open an account and billing support case on the Basic plan"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 10 minutes to open, then a wait for a reply"
prerequisites: ["clf-00-05"]
terms_introduced: []
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-example.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/ai-enhanced-support.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/aws-support-console.html"
---

# Open an account and billing support case on the Basic plan

> **Your account, your responsibility.** Read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow these steps.

**Goal:** a real person at AWS has your billing or account question, with the facts they need to answer it, at no charge.

**Use this when:** there's a charge you can't explain after [reading the bill](08-read-this-months-bill.md) and following [primer page 08](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/08-when-something-goes-wrong.md#track-down-an-unexpected-charge); a question about credits, the Free plan or a payment; or an account problem. **Not** for practice: real people answer these.

**Before you start:** sign in as your IAM admin user; its administrator permissions include Support Center. Have ready: the service, Region and amount from the bill, the dates, and what you've already checked. Every plan, including the free Basic plan, can open **Account and billing** cases. Basic can't open **Technical** cases ([Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html), checked 2026-10-24).

## Steps

1. Choose the question mark icon at the top right of the console, then **Support Center**.
   **You should see:** Support Center. It may first ask you to describe the issue and offer AI-generated troubleshooting before a case form ([AI-enhanced troubleshooting](https://docs.aws.amazon.com/awssupport/latest/user/ai-enhanced-support.html)). On 2026-10-25 it opened on **Hi. How can we help?**: describe your issue there and send it. Read what the AI suggests; it may answer you. If not, choose **Create a case** below its answer.
2. In the case form that opens, choose the **Case type** **Account and billing**. (Basic lists **Technical** too, but can't open it: choosing it shows a paid-plan trial offer. Don't start the trial.)
3. Choose the **Service** and **Category** closest to your question, such as billing and an unexpected charge. Links to help pages may appear; read them first.
   **You should see:** on Basic, no choice of severity, or only the default; severity levels belong to paid plans.
4. Write a short **Subject**, such as "Charge for EC2 in us-east-1 I can't explain, October 2026".
5. In **Description**, give the facts: the service, Region and amount; the dates; what you deleted and when; what you've checked (the bill, Tag Editor in all Regions). AWS asks for as much detail as you can give ([Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#describing-your-problem)). **Never** include passwords, MFA codes, access keys or full card numbers.
6. Choose a contact method. **Web** means you read and reply in Support Center; **Chat** or **Phone** may also appear, depending on the case type ([Example: account and billing case](https://docs.aws.amazon.com/awssupport/latest/user/case-example.html), checked 2026-10-24). Choose **Submit**.
   **You should see:** the case's page, with a case ID. Write it in your lab log.

## Check it worked

The case appears in Support Center's case history, and you may also get an email about it. Replies arrive on the case page; respond there, not by starting a new case. When you have your answer, mark the case resolved with the option on its page.

## If something went wrong

- **You can't sign in at all:** use AWS's [Contact Us](https://aws.amazon.com/contact-us/) page, which handles billing and account issues without a sign-in ([Manage access to AWS Support Center](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html)).
- **Access denied in Support Center:** you may be signed in as a lab test identity. Sign in as your IAM admin user. By default IAM users have no Support access unless a policy grants it; administrator access does. AWS says custom policies need its `support-console` actions by 2026-11-16 ([About the Support Center Console API](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-console.html)).
- **Only Technical fits your question:** Basic can't open it. Use the documentation, the Knowledge Center and re:Post ([Where to find answers](../12-getting-help/03-where-to-find-answers.md)). A quota increase has its own request, open to every plan.
- **You opened a case by mistake:** reply on the case that it was opened in error and can be closed.

> **Dated (checked 2026-10-24):** case types, plan names and the free tier of support change. Check [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) before you rely on the details above.

**Why it matters:** asking the provider early, with evidence, keeps a surprise charge small, which supports [COST01-BP06 Monitor cost proactively](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_proactive_process.html).

## Used in

- Lessons: [Support plans](../12-getting-help/01-support-plans.md#every-account-starts-on-basic-which-answers-account-questions-but-not-technical-ones); [Where to find answers](../12-getting-help/03-where-to-find-answers.md).
- Lab: [Lab 17, Stop 2](../12-getting-help/05-lab-17-support-center-tour.md#stop-2-which-cases-can-you-open), which looks at the case types without submitting one.
- Optional simulation: [S15, Support plan chooser](../12-getting-help/06-sim-support-plan-chooser.md).

---

"Open an account and billing support case on the Basic plan" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
