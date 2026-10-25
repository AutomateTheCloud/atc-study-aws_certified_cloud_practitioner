---
type: task-card
id: clf-98-02
title: "Tag a resource you forgot to tag"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 5 minutes"
prerequisites: ["clf-00-05"]
terms_introduced: []
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/tag-editor/latest/userguide/find-resources-to-tag.html"
  - "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-add.html"
  - "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html"
  - "https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"
  - "https://docs.aws.amazon.com/cli/latest/reference/logs/tag-resource.html"
---

# Tag a resource you forgot to tag, so cleanup can find it

> **Your account, your responsibility.** These steps act on your own AWS account. Read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow them.

**Goal:** a resource a lab made carries the lab's two tags, `guide` = `clf` and `lab` = the lab's two-digit number, so a tag search finds it.

**Use this when:** you skipped a lab's **Tags** section, mistyped a tag (`Lab` instead of `lab`), or a service made a part for you that came untagged.

**Before you start:** know which lab made the resource, and roughly its name (the labs name everything `clf-labNN-…`). Sign in as your IAM admin user, in the Region where the resource lives ([Switch to US East (N. Virginia)](01-switch-to-us-east-1.md)).

## Steps

The quickest fix is often on the resource's own page: many services have a **Tags** tab or section with a button such as **Manage tags** or **Edit**. For S3, it's the bucket's **Properties** tab, under **Tags**. To fix several resources at once, use Tag Editor:

1. In the console search bar, type `Tag Editor` and open it. (On 2026-10-24 a banner said tag management is moving to the AWS Resource Explorer console; if it has moved, look for the same steps there.)
2. In **Regions**, choose **All regions**, or the Region you know. In **Resource types**, choose the type, such as `AWS::S3::Bucket`, or **All resource types**. Leave the **Tags** boxes empty, so the search also returns untagged resources ([Finding resources to tag](https://docs.aws.amazon.com/tag-editor/latest/userguide/find-resources-to-tag.html)). Choose **Search resources**.
3. In **Filter resources**, above the results, type `clf-lab` and the lab number.
   **You should see:** the resource you forgot, with **(not tagged)** or a wrong tag in the tag columns.
4. Select it (and any others from the same lab), then choose **Manage tags of the selected resources**.
5. Choose **Add tag**. Enter the key `guide` and the value `clf`. Choose **Add tag** again for the key `lab` and the value, such as `07`. Type them in lowercase: keys and values are case sensitive ([What is Tag Editor?](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)).
6. Choose **Review and apply changes**, then **Apply changes to all selected** ([Add tags to selected resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-add.html), checked 2026-10-24). Stay on the page.
   **You should see:** a green success banner; with many resources it can take a few minutes.

## Tag what Tag Editor can't

| Resource | Where to tag it |
|---|---|
| IAM users and roles | IAM console: open the user or role, then its **Tags** tab. AWS says Tag Editor doesn't support IAM tags ([Tags for IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)). |
| IAM user groups | Can't be tagged at all. The lab's `clf-labNN` name is what marks them. |
| CloudWatch Logs log groups | Not taggable in Tag Editor ([supported resource types](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html), checked 2026-10-24). Use the log group's **Tags** tab, then **Manage tags** (as we did on 2026-10-25), or CloudShell, below. |

To tag a log group from CloudShell ([primer page 04](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md)), replace `ACCOUNT-ID` with your 12-digit account ID and use the log group's name:

```bash
aws logs tag-resource \
  --resource-arn arn:aws:logs:us-east-1:ACCOUNT-ID:log-group:/aws/lambda/clf-lab07-box-count \
  --tags guide=clf,lab=07
```

It prints nothing when it works ([tag-resource](https://docs.aws.amazon.com/cli/latest/reference/logs/tag-resource.html)).

## Check it worked

Repeat the search with the tag `lab` and the lab's number in the **Tags** boxes, as in [Find everything a lab left behind](03-find-what-a-lab-left-behind.md). The resource should now appear.

## If something went wrong

- **Tag Editor refuses the new key:** it won't add a key that one of the selected resources already has. Select only the resources missing it, or open the resource and change the existing value.
- **The mistyped tag is still there:** a tag `Lab` = `07` is a different key from `lab`. Remove the wrong one on the **Manage tags** page or the resource's own **Tags** tab.
- **Access denied:** check that you're signed in as your IAM admin user, not a lab test identity.

> **Note:** tagging now doesn't label costs from before. A tag reaches your cost reports only after its key is activated, and only from then on ([Many accounts, one bill](../11-paying-for-aws/04-many-accounts-one-bill.md#a-tag-reaches-your-cost-reports-only-after-you-activate-it)). Tag as you create.

**Why it matters:** a tag turns cleanup into a search instead of a memory test: [COST03-BP02 Add organization information to cost and usage](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_org_information.html) ([primer page 07](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md#habit-1-tag-everything-you-create), habit 1).

## Used in

- [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md#find-it-by-its-tags) (fixing a missing bucket tag); [Lab 07](../06-running-applications/05-lab-07-a-lambda-function.md#read-the-logs-and-set-retention) (the log group); [Lab 16](../11-paying-for-aws/06-lab-16-cost-allocation-tags.md); [Lab 19](../14-capstone/03-lab-19-close-out.md#part-a-sweep-every-region-by-tag).

---

"Tag a resource you forgot to tag" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
