---
type: task-card
id: clf-00-05
title: "Before your first lab"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT; about 5 minutes to read, plus 2 to 3 hours for the guardrails primer; a laptop or desktop"
prerequisites: ["clf-00-01"]
terms_introduced: [lab log, Region, tag]
pillars: [cost-optimization, security, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md"
  - "https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md"
  - "https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html"
---

# Set up your account and learn the lab routine before Lab 01

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Use this when:** you are about to start Lab 01 in module 02, or any lab after it. You need a laptop or desktop, an email address, a payment card, and 2 to 3 hours for the primer. Open an AWS account only when you reach this page.

## Steps

1. **Work through the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md), pages 01 to 07.** It creates your account on the advanced sign-up and the Free plan, then sets up the protections every lab relies on. Three are required: the root user (the all-powerful sign-in) protected with MFA and put away ([page 02](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md)); an IAM admin user with MFA for daily work ([page 03](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md)); and budgets and billing alerts ([page 05](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md)).
2. **Start a lab log**, in a notebook or a file. For every lab, write the date, Region, tags, what you created, whether you deleted it, and your next-day check ([OPS07-BP03 Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html)).
3. **Sign in as your IAM admin user, never the root user.** One stolen root sign-in can do anything in the account.
4. **Check the Region selector at the top right: every lab uses US East (N. Virginia), `us-east-1`,** unless it says otherwise. A **Region** is a part of the world where AWS runs data centers. A new account may open elsewhere: ours opened in US East (Ohio) on 2026-10-23.
5. **Tag everything you create with `guide` = `clf` and `lab` = the lab's two-digit number,** for example `lab` = `07`. A **tag** is a free label made of a key and a value; it lets one search find everything a lab made, in every Region ([COST03-BP02 Add organization information to cost and usage](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_org_information.html)).
6. **Never choose an Upgrade plan button** unless you have decided to pay. Upgrading to the Paid plan can't be undone, and some actions upgrade automatically, such as creating an organization in AWS Organizations; [primer page 00](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md#know-what-moves-you-to-the-paid-plan) lists them (as of 2026-10-23).
7. **End every lab the same way: find, delete, confirm, then check the next day.** Find what you made by its tags in every Region, delete it (stopping isn't deleting), and confirm it's gone. Cost data runs about a day behind, so check the **Credits** page, your bill and your budget alerts the next day ([primer page 07](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md); [COST04-BP03 Decommission resources](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_decommission.html)).

> **New sign-up path:** AWS's newer sign-up, announced 2026-09-16, uses a login such as Google or GitHub ([Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html)). As of 2026-10-23 it has no root user, its IAM users can't use the console, it picks your Region, and it doesn't support some services, such as IAM Identity Center. Our labs are written for the advanced sign-up, and each has a box like this one saying what changes; [primer page 01](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/01-create-your-account.md#if-you-landed-in-the-new-sign-up-experience) has the details. Free Tier credits are for one account only, so read AWS's terms before opening a second account.

## Verify

You are ready for Lab 01 when all of these are true:

- [ ] You can sign in as your IAM admin user, with MFA.
- [ ] The root user has MFA, and you don't use it for daily work.
- [ ] Your budgets exist, and you clicked the verification link in AWS's email, so alerts can reach you (AWS has required this for new recipients since 2026-09-30).
- [ ] The Region selector shows N. Virginia (`us-east-1`).
- [ ] Your lab log is ready.
- [ ] The account is on the Free plan, and you know not to choose **Upgrade plan**.

**Related:** [Lab 01: Create, find and delete your first storage bucket](../02-why-the-cloud/06-lab-01-first-resource.md); [primer page 10, bad practices and checklist](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/10-bad-practices-and-checklist.md).

---

"Before your first lab" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
