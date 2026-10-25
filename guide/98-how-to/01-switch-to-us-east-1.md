---
type: task-card
id: clf-98-01
title: "Switch the console to US East (N. Virginia)"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 2 minutes"
prerequisites: ["clf-00-05"]
terms_introduced: [default Region]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html"
  - "https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region-procedure.html"
  - "https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/change-default-region.html"
  - "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html"
---

# Switch the console to US East (N. Virginia) and keep it there

> **Your account, your responsibility.** These steps act on your own AWS account. Read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow them.

**Goal:** the console shows US East (N. Virginia), `us-east-1`, the Region every lab in this guide uses, and opens there next time.

**Use this when:** you start any lab; a resource you just made has vanished from a list; or a lab step says "check the Region".

**Before you start:** sign in as your IAM admin user, not the root user ([primer page 03](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md)).

## Steps

1. Look at the Region name near the top right of the console, beside your account name.
   **You should see:** a Region name, such as **United States (N. Virginia)** or **US East (Ohio)** (the wording we saw on 2026-10-23). Our new test accounts opened in Ohio, so never assume.
2. If it doesn't say N. Virginia, choose the Region name to open the list, then choose **United States (N. Virginia)** ([Choosing a Region from the navigation bar](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region-procedure.html)).
   **You should see:** N. Virginia in the selector, and the page reloads to show that Region's resources. Each entry also shows its **Region code**; this one is `us-east-1`.
3. Optional, once: make N. Virginia your **default Region**, the one the console opens in. Choose the gear icon in the top bar, then **See all user settings**. Next to **Localization and default Region**, choose **Edit**, set **Default Region** to US East (N. Virginia), and choose **Save settings** ([Setting the default Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/change-default-region.html), checked 2026-10-24). With no default set, the console reopens in the last Region you visited.
   **You should see:** the new default listed on the settings page.

**Don't** enable an opt-in Region while you're in the list. Regions launched after 2019-03-20 start switched off, and a Region you never look at is one more place to forget a resource ([Enable or disable AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html), checked 2026-10-23).

## Check it worked

- The selector reads N. Virginia on the page you're about to work on. Check again after you open a new service: each console page shows its own selector.
- On many service pages the web address also contains the code, for example `region=us-east-1`. Treat that as a second clue, not proof.

## If something went wrong

- **The selector shows no Region, or a word such as "Global":** you are on a page for a service that isn't tied to one Region, such as IAM or the billing pages ([Choosing your Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)). That's normal. Switch when you open a Regional service, such as EC2 or Lambda.
- **The S3 bucket list shows buckets from other Regions:** also normal. S3 shows all your buckets in one list, each with its Region. The Region matters when you create a bucket: check the **AWS Region** on the create page.
- **A resource you created has disappeared:** it is almost always in another Region. Switch Regions and look, or search every Region at once with [Find everything a lab left behind](03-find-what-a-lab-left-behind.md).
- **N. Virginia isn't in the list, or can't be chosen:** you may be on the new sign-up path; see the box below.

> **New sign-up path:** accounts made through AWS's newer sign-up get a Region chosen for them that they can't change (as of 2026-10-23). Use that Region wherever this guide says `us-east-1`, and write it in your lab log.

**Why it matters:** most resources live in one Region, and most console pages show only one Region at a time. Working in one known Region keeps cleanup a single search, which supports [COST04-BP01 Track resources over their lifetime](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_track.html).

## Used in

- Lessons: [Regions, Availability Zones and data centers](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md); [Choosing a Region](../03-aws-around-the-world/02-choosing-a-region.md).
- Labs: every lab, from [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md#get-ready) on; [Lab 02](../03-aws-around-the-world/05-lab-02-see-the-global-infrastructure.md#list-regions-in-the-region-selector) tours the selector.
- Primer: [page 06, Regions](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md#regions-keep-the-extra-ones-off-and-see-what-already-exists), which shows which Regions are on in your account.

---

"Switch the console to US East (N. Virginia)" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
