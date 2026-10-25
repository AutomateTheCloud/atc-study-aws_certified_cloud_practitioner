---
type: task-card
id: clf-98-05
title: "Set a CloudWatch Logs retention period, and delete a log group"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, with an AWS account of their own; about 5 minutes"
prerequisites: ["clf-00-05"]
terms_introduced: []
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protecting-log-groups-from-deletion.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.html"
  - "https://aws.amazon.com/cloudwatch/pricing/"
---

# Set how long CloudWatch Logs keeps a log group, or delete it

> **Your account, your responsibility.** These steps act on your own AWS account. Read the [notice](../00-start-here/05-before-your-first-lab.md#before-you-start-your-account-your-responsibility) before you follow them.

**Goal:** a log group keeps its logs only as long as you need them, or is gone once the code that wrote it is gone.

**Use this when:** a Lambda function has written its first logs (a new log group keeps them forever); or a lab's cleanup deletes a function and its logs ([Lab 07](../06-running-applications/05-lab-07-a-lambda-function.md#clean-up), [Lab 11](../08-building-and-operating/06-lab-11-alarm-on-errors.md#clean-up)).

**Before you start:** the log group's name. Lambda's are `/aws/lambda/` plus the function name. Sign in as your IAM admin user, in the log group's Region ([Switch to US East (N. Virginia)](01-switch-to-us-east-1.md)).

## Steps: set a retention period

1. In the console search bar, type `CloudWatch` and open it. In the left menu, open the log groups list: **Logs**, then **Log groups** (AWS's guide also calls the entry **Log Management**; checked 2026-10-24).
2. Find the log group, and look at its **Retention** column.
   **You should see:** **Never expire** on a new log group. By default CloudWatch Logs keeps log data indefinitely ([Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)).
3. Choose the retention value itself (**Never expire**). In **Expire events after**, choose a period, such as **1 week (7 days)** for a lab, and choose **Save**.
   **You should see:** the new period in the **Retention** column.

Log events past the period are marked for deletion and stop adding to storage cost; the actual deletion usually happens within 72 hours.

## Steps: delete a log group

Delete the thing that writes the logs first, such as the Lambda function. A function that runs again creates its log group again.

4. In the log groups list, select the log group. Choose **Actions**, then the delete option (**Delete log group(s)** in [Lab 07](../06-running-applications/05-lab-07-a-lambda-function.md#clean-up)), and confirm.
   **You should see:** the log group gone from the list. Deleting it permanently deletes every log event in it ([DeleteLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.html)), so keep anything you must prove later.

## Check it worked

- **Retention:** the **Retention** column shows your period, not **Never expire**.
- **Deletion:** search the log groups list for the lab's name (`clf-lab07`, for example); nothing found. Log groups can't be found by a Tag Editor search, so this name search is the check ([Find everything a lab left behind](03-find-what-a-lab-left-behind.md#net-2-check-what-tags-cant-find)).

## If something went wrong

- **The log group isn't in the list:** check the Region; log groups live in the Region of the code that wrote them. Or the code hasn't logged yet: a Lambda function's group appears after its first run.
- **The log group came back after you deleted it:** something is still writing to it. Delete or stop the writer, then delete the log group again.
- **Deletion refused, with a message about deletion protection:** someone turned on deletion protection, which is off by default. Turn it off with **Actions**, **Edit deletion protection**, then delete ([Protecting log groups from deletion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protecting-log-groups-from-deletion.html), checked 2026-10-24). Make sure the group isn't one you meant to keep.

> **Dated (checked 2026-10-24):** in `us-east-1`, the free tier covers 5 GB of log data a month; ingesting more costs $0.50 per GB, and the logs you keep add a storage charge every month ([Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/); [Cost traps](../99-reference/05-cost-traps.md#logs-are-kept-forever-unless-you-say-otherwise)). A lab's logs are tiny; years of production logs are not.

**Why it matters:** choosing how long to keep data, and deleting it on schedule, is [COST04-BP05 Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html). In real work, the period comes from what you must keep for audits and troubleshooting, not from habit.

## Used in

- Lesson: [Watching workloads](../08-building-and-operating/03-watching-workloads.md#cloudwatch-logs-keeps-what-your-code-writes-and-lets-you-search-it).
- Labs: [Lab 07](../06-running-applications/05-lab-07-a-lambda-function.md#read-the-logs-and-set-retention); [Lab 11](../08-building-and-operating/06-lab-11-alarm-on-errors.md#clean-up); [Lab 19](../14-capstone/03-lab-19-close-out.md#part-b-check-what-tags-cant-find).

---

"Set a CloudWatch Logs retention period, and delete a log group" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
