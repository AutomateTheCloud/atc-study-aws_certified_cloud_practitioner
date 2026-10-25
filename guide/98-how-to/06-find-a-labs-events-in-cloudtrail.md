---
type: task-card
id: clf-98-06
title: "Find a lab's events in CloudTrail Event history"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 5 minutes"
prerequisites: ["clf-00-05"]
terms_introduced: []
pillars: [security, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html"
---

# Find a lab's events in CloudTrail Event history

> **Your account, your responsibility.** These steps only read your account, but read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow them.

**Goal:** you find the record of who created, changed or deleted something during a lab, and when.

**Use this when:** you want proof that a lab's cleanup ran; you can't remember whether you deleted something; you wonder who or what made a resource; or a lab asks for an event, as [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md#find-it-in-the-activity-record) and [Lab 12](../09-protecting-and-governing/07-lab-12-answer-the-auditor.md) do.

**Before you start:** the lab's date and Region from your lab log. Sign in as your IAM admin user. Viewing Event history costs nothing ([Working with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html), checked 2026-10-24).

## Steps

1. In the console search bar, type `CloudTrail` and open it. Check that the Region selector shows the lab's Region, usually N. Virginia ([Switch to US East (N. Virginia)](01-switch-to-us-east-1.md)). Event history shows one Region at a time.
2. In the left menu, choose **Event history**.
   **You should see:** recent events, newest first, filtered on **Read-only** = **false**, which hides events that only read ([Viewing recent management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html), checked 2026-10-24).
3. Under **Lookup attributes**, change the first box from **Read-only** to the attribute you need, and type the full value beside it. You can use one attribute at a time, plus a time range:

   | To find | Attribute | Value, for example |
   |---|---|---|
   | One kind of action | **Event name** | `CreateBucket`, `DeleteBucket`, `TerminateInstances` |
   | Everything done to one service | **Event source** | `s3.amazonaws.com`, `lambda.amazonaws.com` |
   | Everything about one resource | **Resource name** | the bucket name, or an ID such as `vpc-…` |
   | Everything one identity did | **User name** | your IAM user name, or `root` |

4. Narrow the time: in the time range bar, choose **Absolute range** and set the lab's day, or a **Relative range** such as 1 day.
   **You should see:** the matching events, with **Event name**, **Event time**, **User name**, **Event source**, **Resource type** and **Resource name** columns.
5. Choose an event's name to open it. Scroll to **Event record** for the full JSON: who (`userIdentity`), what (`eventName`), when (`eventTime`, in UTC), from where (`sourceIPAddress`) and to what.

## Check it worked

For a lab's cleanup, a lookup by **Event name** for each delete action the lab used (`DeleteBucket`, `DeleteFunction`, `DeleteVpc`) shows one event per resource, made by your IAM user, on the day you cleaned up.

## If something went wrong

- **Nothing appears:** wait five minutes and refresh; in our run events took up to four minutes. Then check the Region, the spelling (values must be exact; `createbucket` won't match), and that the time range covers the lab.
- **IAM events aren't there:** IAM, STS and CloudFront are global services; Event history shows their events in the Region where they occurred, which for most is N. Virginia ([Global service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events)). Switch to N. Virginia.
- **The lab was more than 90 days ago:** Event history keeps 90 days of management events and you can't extend it. Keeping more takes a trail or an event data store, which you would pay to store. That gap is a finding in its own right ([Lab 12](../09-protecting-and-governing/07-lab-12-answer-the-auditor.md#part-a-follow-one-change-from-start-to-finish-follow-along)).
- **You were looking for a file download or upload:** those are **data events**, which Event history never shows.
- **You want a copy:** choose **Download events**, then CSV or JSON. Open a CSV in a plain text editor, not a spreadsheet: AWS warns that event text can act as commands in spreadsheet programs. Don't share files that show your IP address.

**Why it matters:** checking the record of who did what is [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) in practice, and the habit you'll rely on when something happens that you didn't do ([primer page 08](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/08-when-something-goes-wrong.md#lock-down-a-leaked-key-or-activity-you-didnt-do)).

## Used in

- Lessons: [Who did what, how it runs, how it was set](../09-protecting-and-governing/01-who-did-what.md#cloudtrail-records-who-did-what-when-and-from-where); [Watching workloads](../08-building-and-operating/03-watching-workloads.md#cloudtrail-records-actions-on-your-account-not-how-your-application-runs).
- Labs: [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md#find-it-in-the-activity-record); [Lab 12](../09-protecting-and-governing/07-lab-12-answer-the-auditor.md).
- Primer: [page 06, CloudTrail](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/06-safe-defaults.md#cloudtrail-see-what-happened-in-your-account).

---

"Find a lab's events in CloudTrail Event history" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
