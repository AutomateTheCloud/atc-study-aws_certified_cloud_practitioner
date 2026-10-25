---
type: page
id: clf-08-08
title: "Module 08: beyond the exam"
reader: "Adult who has finished Module 08 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-08-00]
pillars: [operational-excellence, reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html"
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html"
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html"
  - "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html"
  - "https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html"
  - "https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html"
  - "https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html"
---

# Module 08: what we left out, and where to read it

The CLF-C02 exam asks which access method, monitoring tool or messaging service fits a need, not how to build or run it. These topics go deeper, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Access and infrastructure as code

- **SDK credentials and retries.** SDKs find the temporary credentials of the role code runs with, renew them, and retry brief failures; on your own computer, `aws login` gives the CLI temporary credentials. See [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) and [primer page 04](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md).
- **CloudShell limits.** No extra charge, 1 GB of persistent home storage per Region, and sessions that end after 20 to 30 minutes of inactivity (as of 2026-10-24). See [CloudShell quotas and restrictions](https://docs.aws.amazon.com/cloudshell/latest/userguide/limits.html).
- **Writing templates.** Parameters, references (`!Ref`) and functions such as `!GetAZs` that let one template work in any Region. See [How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html).
- **Change sets and drift detection.** A change set previews what an update would add, change or replace; drift detection reports changes made by hand outside the template but doesn't fix them. See [Detect unmanaged configuration changes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html).
- **What a stack delete leaves behind.** A bucket must be empty to be deleted, a `Retain` deletion policy keeps a resource, and an RDS database keeps a final snapshot by default; each keeps costing until you remove it. See the [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).
- **Copying to other Regions and accounts.** StackSets manage stacks across many accounts and Regions; an AMI belongs to one Region, and bucket names must be unique, so templates must allow for both. See [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
- **Other IaC tools.** The AWS CDK turns code in a programming language into a CloudFormation template; some teams use Terraform. See [What is the AWS CDK?](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- **Service Catalog in depth.** Products, portfolios, template and launch constraints, versions and API pricing. See [Overview of Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html) and [AWS Service Catalog pricing](https://aws.amazon.com/servicecatalog/pricing/).

## Monitoring

- **CloudWatch metrics in detail.** Basic monitoring (EC2 metrics every 5 minutes) and paid detailed monitoring (every minute), custom metrics, and metric retention of 15 months at coarser detail as data ages. See [Metrics concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).
- **Designing alarms.** Periods, statistics, how many periods must breach, how missing data counts, and the fact that actions run once on a change of state (Auto Scaling actions repeat). An alarm in OK proves nothing about its email: the SNS subscription must be confirmed. See [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) and the optional [Lab 11](06-lab-11-alarm-on-errors.md).
- **Metric filters.** Turning matching log lines, such as `PAYMENT_DECLINED`, into a metric you can alarm on. See [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).
- **X-Ray internals.** Segments, sampling (by default the first request each second and 5% of the rest) and 30 days of trace retention. See [AWS X-Ray concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html).
- **CloudTrail Lake.** A store for querying events, closed to new customers on 2026-05-31; CloudTrail itself is fully supported. See [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

## Messaging and developer tools

- **SQS in depth.** Retention from 1 minute to 14 days, a message hidden from other workers while one processes it, and dead-letter queues for messages that keep failing. See [What is Amazon SQS?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- **SNS email.** SNS deletes unconfirmed email subscriptions after 48 hours. See [Email subscriptions](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html).
- **The SES sandbox.** New accounts start in it, in each Region, sending only to verified addresses with daily and per-second limits, until AWS grants production access. See [Request production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html).
- **EventBridge bus types and Step Functions workflow types.** The newer Custom Event Bus beside the "Classic" rules-and-targets bus; Standard workflows (up to a year) and Express workflows (up to five minutes). See [Event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) and [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- **Pipeline integrations and prices.** CodePipeline can deploy with CloudFormation, Amazon ECS, Elastic Beanstalk and others; CodeBuild bills by the build minute. See [CodePipeline action integrations](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-action-type.html) and [AWS CodeBuild pricing](https://aws.amazon.com/codebuild/pricing/).

## Well-Architected practices for operations

Version control for templates ([OPS05-BP01 Use version control](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.html)), actionable alerts ([OPS08-BP04 Create actionable alerts](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_alerts.html)), weighing automation against effort ([COST11-BP01 Perform automation for operations](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_cost_effort_automations_operations.html)) and workers that can safely handle a message twice ([REL04-BP04 Make mutating operations idempotent](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_idempotent.html)) belong to designing and running workloads, not to this exam.

---

"Module 08: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
