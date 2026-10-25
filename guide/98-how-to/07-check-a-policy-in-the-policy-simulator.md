---
type: task-card
id: clf-98-07
title: "Check what a policy allows with the IAM policy simulator"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 10 minutes"
prerequisites: ["clf-00-05", "clf-04-04"]
terms_introduced: []
pillars: [security]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html"
---

# Check what a policy allows with the IAM policy simulator

> **Your account, your responsibility.** The simulator changes nothing in your account, but read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow these steps.

**Goal:** for a list of actions on named resources, you see whether a policy (or an identity's policies) would allow or deny each one, and which statement decides.

**Use this when:** you've written a policy and want to test it before anyone relies on it; or someone is denied and you need to know why.

**Before you start:** the actions and resource ARNs to test, written down, with the result you expect for each. Sign in as your IAM admin user. The ideas behind the results are in [Policies and least privilege](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md#how-aws-decides-default-deny-then-allows-then-an-explicit-deny-wins).

The simulator works out the answer without sending a real request, so it's safe to test actions such as `s3:DeleteBucket` ([IAM policy testing with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html), checked 2026-10-24).

## Steps

1. Open IAM and choose **Policy simulator** in the left menu. Or, to test an existing user, group or role, open it, choose its **Permissions** tab, and choose **Simulate**. On 2026-10-24 the simulator opened inside the IAM console, with a notice that the older, separate simulator will be retired.
2. Choose the mode at the top:
   - **Principal** tests the policies attached to one existing identity. You choose the identity under **Identities** and tick its policies.
   - **Custom** tests a policy you paste in. Choose **Add policy**, give it a name, paste the JSON, choose **Save**, then **Back to simulator**. The policy is used only for the simulation and isn't saved to your account.
3. Choose **Add actions**, choose the service (for example **S3**), then **Specify**, and type each action name, using **Add more** between them. Choose **Add actions**.
   **You should see:** one row per action, each with the resource `*`.
4. For each row, choose its **Resource** cell, select **Specific**, choose the **Type** (such as `bucket` or `object`), enter the ARN, and choose **Save**. Replace any text already in the **ARN** box, and clear **Apply to all actions with the same resource type** unless you want the same ARN on every row of that type.
5. Choose **Simulate**.
   **You should see:** **allowed** or **denied** for each row, with **Result details** (wording as of 2026-10-24):
   - "Explicit allow in 1 statement(s)": open it to see which policy and which lines allow it.
   - "Implicit deny due to no statement(s) matching": nothing allows it, so IAM's default deny applies.
   - "Explicit deny found in 1 or more statements": a statement says `"Deny"`, and it wins over every allow. The details name the policy.

## Check it worked

Every row matches the result you wrote down before you started. A surprise is the useful part: read its details before you change anything.

## If something went wrong

- **An allow you expected shows as implicit deny:** compare the ARN in the policy with the one you tested, letter by letter. For objects, the ARN needs a key after the `/`, such as `arn:aws:s3:::BUCKET/cakes/lemon-tart.jpg`.
- **A row has the wrong resource:** the simulator lists each action once. Change the row's resource and choose **Simulate** again, rather than adding the action twice.
- **The page stops responding after you navigate away:** in our runs the tab froze; open the console in a new tab.
- **The real request behaves differently:** AWS warns results can differ from your live account, for example with resource control policies, which the simulator doesn't evaluate, or VPC endpoint policies. After the simulator agrees, test once with a real sign-in.

**Why it matters:** testing a policy against what the task needs, before you rely on it, is how least privilege gets checked rather than assumed: [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html).

## Used in

- Lesson: [Policies and least privilege](../04-shared-responsibility-and-access/04-policies-and-least-privilege.md). Simulation: [S4, Predict allow or deny across accounts, boundaries and organizations](../04-shared-responsibility-and-access/09-sim-policy-playground.md).
- Labs: [Lab 03](../04-shared-responsibility-and-access/06-lab-03-a-group-and-a-policy.md#test-it-in-the-policy-simulator) (Principal mode); [Lab 04](../04-shared-responsibility-and-access/07-lab-04-finish-and-fix-a-policy.md#part-a-finish-the-photographers-policy-completion) (Custom mode) and its [break-fix part](../04-shared-responsibility-and-access/07-lab-04-finish-and-fix-a-policy.md#part-c-uploads-fail-break-fix).

---

"Check what a policy allows with the IAM policy simulator" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
