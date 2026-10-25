# Blueprint: Module 08, Building and operating

Items file: `practice/items/08-building-and-operating.yaml`. Targets: about 70 questions (about 14
"Select TWO") and 18 concept cards. Exam tasks: 3.1 (ways to provision and operate: console, CLI,
SDKs, infrastructure as code, CloudFormation), 3.8 (application integration: SNS, SQS, EventBridge,
Step Functions; developer tools CodeBuild and CodePipeline; X-Ray for request tracing), 2.2
(monitoring and logging: CloudWatch and CloudTrail as the guide contrasts them) and 1.4 (the
economics of automation). No prices are tested.

The module has four objectives, one per lesson, so the table breaks each objective into the
sections that teach it. Lab 10 (page 05) serves 08.01a and 08.02a; Lab 11 (page 06) serves 08.03a
and 08.04a.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

## 08.01a Choose the console, the CLI, an SDK or infrastructure as code for a task [J·Ap] (lesson 08.01, task 3.1)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "The big picture: four doors, one set of services" | Same IAM permissions and one CloudTrail record, whichever way in | Re, Ap | 2 | 1 | 0 |
| 01, "The console is for seeing, learning and doing something once" | The console for one look at existing settings | Ap | 1 | 0 | 0 |
| 01, ""Console clicks are fine for production" is wrong" | Why a hand-built setup can't be copied or rebuilt reliably | Un | 1 | 0 | 0 |
| 01, "The CLI turns each action into a command you can save and run again" | The CLI offers the console's administration functions | Re | 1 | 0 | 0 |
| 01, "An SDK puts AWS calls inside your own program" | A program's own calls; what an SDK handles (role credentials, retries) | Ap, Un | 2 | 1 | 1 |
| 01, "Infrastructure as code describes the end result in a file" | A template knows the end result; a script repeats steps | Un | 1 | 0 | 1 |
| 01, "One-time or repeatable: the question that picks the way in" | One-time bulk work by CLI; repeatable jobs for IaC; person vs program; the three questions | Ap, Un | 3 | 1 | 1 |
| 01, "Worked example: six jobs at the bakery" | A weekly test copy built and deleted from a template | Ap | 1 | 0 | 0 |
| 01, "Your side of the line" | Identities, permissions and credentials are the customer's | Un | 1 | 0 | 0 |
| 05 (Lab 10), "Part B: the AWS CLI in CloudShell (follow-along)" | S3's defaults apply whichever tool creates the bucket | Un | 1 | 0 | 0 |
| 05 (Lab 10), "Recap" | What each way leaves behind | Un | 1 | 0 | 0 |
| **Total 08.01a** | | | **15** | **3** | **3** |

## 08.02a Explain how infrastructure as code makes work repeatable and cheaper [C·Un] (lesson 08.02, tasks 3.1 and 1.4)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "A template describes what should exist, not the steps to build it" | Launch template vs CloudFormation template; Region-neutral zones; parameters; CloudFormation orders the build | Un, Ap | 3 | 0 | 1 |
| 02, "A stack is the unit you create, change and delete" | Rollback on a failed create; what a delete can leave behind | Re, Un | 2 | 1 | 0 |
| 02, "Change sets preview a change; drift detection finds changes made by hand" | Change set to preview a replacement, and its limits; drift detection; hand changes missing from copies; drift is only reported | Ap, Re, Un | 4 | 0 | 1 |
| 02, "One template, many Regions and accounts, but not the data" | Data is not rebuilt; StackSets for many accounts; AMIs are Regional | Un, Re | 2 | 1 | 1 |
| 02, "Automation makes work repeatable and cheaper" | Benefits of automation; no discount for template-built resources; when a template pays back (task 1.4) | Un, Ap | 3 | 1 | 1 |
| 02, "Service Catalog lets others launch only what you've approved" | Self-service of approved products; launch constraints; CloudFormation vs Service Catalog | Ap, Re, Un | 3 | 1 | 0 |
| 02, "Your side of the line" | A template copies its mistakes everywhere | — | 0 | 0 | 1 |
| 05 (Lab 10), "Part C: a template you finish (completion)" | `!Ref` to a parameter makes a template reusable | Un | 1 | 0 | 0 |
| 05 (Lab 10), "Clean up" | A bucket that holds objects stops the stack's delete | Ap | 1 | 0 | 0 |
| **Total 08.02a** | | | **19** | **4** | **5** |

## 08.03a Pick the tool for an operations question: CloudWatch, X-Ray or CloudTrail [C·Ap] (lesson 08.03, tasks 2.2 and 3.8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "CloudWatch metrics show how each part is doing, as numbers over time" | Free service metrics; the CloudWatch agent; metrics and alarms are Regional | Re, Un | 3 | 1 | 0 |
| 03, "An alarm watches one metric and acts when its state changes" | One notification per state change; alarm actions; the Auto Scaling exception | Re, Un | 2 | 1 | 1 |
| 03, ""OK" means below the threshold, not "working"" | What OK does and doesn't tell you | Un | 1 | 0 | 0 |
| 03, "CloudWatch Logs keeps what your code writes, and lets you search it" | Metric filter then alarm; Logs Insights to search; logs never expire by default | Ap | 2 | 0 | 1 |
| 03, "X-Ray follows one request through every part it touches" | Tracing one slow request; what a trace adds to a metric; sampling; the name change (task 3.8) | Ap, Un | 2 | 0 | 2 |
| 03, "CloudTrail records actions on your account, not how your application runs" | Who changed a setting; keeping events past 90 days; data events | Ap, Re | 3 | 0 | 0 |
| 03, ""CloudTrail monitors my application" is wrong" | The misconception | Un | 1 | 0 | 0 |
| 03, "Pick the service by the question it must answer" | Matching questions to services; the Health Dashboard for AWS's side | Ap | 2 | 1 | 1 |
| 06 (Lab 11), "Part B: build the alert from the owner's request (challenge)" | Missing data treated as not breaching | Ap | 1 | 0 | 0 |
| 06 (Lab 11), "Recap" | An error-rate alarm for a busy function | Ap | 1 | 0 | 0 |
| **Total 08.03a** | | | **18** | **3** | **5** |

## 08.04a Choose a messaging service by the shape of the message, and name the build or release tool [C·Ap] (lesson 08.04, task 3.8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "Key terms (skip if you know them)" | What continuous delivery means | Re | 1 | 0 | 0 |
| 04, "A direct call fails when the other side fails; a message in between waits" | A queue between parts; what a queue gives | Ap, Un | 2 | 1 | 0 |
| 04, "SQS holds work in a queue until a worker pulls it" | FIFO for strict order; standard queue traits; dead-letter queue; polling; a crashed worker | Ap, Re | 3 | 1 | 2 |
| 04, "SNS pushes one message to every subscriber of a topic" | Fan-out; SNS plus SQS | Ap | 2 | 0 | 0 |
| 04, "An email from SNS is an alert; an email from SES is your mail" | SES for branded mail; the SNS-is-SES misconception; the SES sandbox | Ap, Un | 3 | 0 | 0 |
| 04, "EventBridge routes events by rules on what they say" | React to AWS events; what EventBridge does; SNS vs EventBridge | Ap, Re, Un | 3 | 1 | 0 |
| 04, "Step Functions runs several steps in order and remembers where it is" | A long workflow with a person's sign-off; Step Functions abilities | Ap, Re | 2 | 1 | 0 |
| 04, "Choose by the shape of the message" | Who waits in SQS, SNS and Step Functions | — | 0 | 0 | 1 |
| 04, "Shipping software: CodeBuild builds and tests, CodePipeline runs the release" | CodeBuild; CodePipeline; CodeDeploy and Cloud9 as distractors and cards | Ap | 2 | 0 | 2 |
| 06 (Lab 11), "Recap" | Lambda reports, the alarm decides, SNS delivers | Un | 1 | 0 | 0 |
| **Total 08.04a** | | | **19** | **4** | **5** |

## Totals

71 questions (57 single, 14 "Select TWO"); 18 concept cards.

Question levels: 15 recall (21%), 25 understanding (35%), 31 application (44%). This leans further
toward application than the 20/50/30 target, on purpose: three of the module's four objectives are
at the apply level (choose a way in, pick the monitoring tool, choose a messaging service), so many
items describe a situation and ask for a decision.

By task: 3.1 31, 3.8 21, 2.2 16, 1.4 3 (the 1.4 benefits also run through several 3.1 items and
two cards). By page: 01 13, 02 17, 03 16, 04 18, Lab 10 4, Lab 11 3. Correct single answers sit 14,
14, 14 and 15 times in positions A to D; the correct choice is the longest in 16 of 57.

Left out on purpose: prices and free-tier amounts of every kind; CloudShell's session and storage
limits; metric retention steps, trace retention and the sampling percentages; the SES sandbox's
sending limits and AWS's response time; EventBridge's newer Custom Event Bus; Step Functions
Express limits; the CDK and Terraform (named as "not on the exam"). AWS CloudShell, AWS CodeDeploy
and AWS Cloud9 appear only as wrong answers or in cards that say how to treat them;
OpsWorks doesn't appear.
