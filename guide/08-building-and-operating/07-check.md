---
type: check
id: clf-08-07
title: "Module 08 mastery check"
tasks: ["3.1", "3.8", "2.2", "1.4"]
objectives: ["08.01a", "08.02a", "08.03a", "08.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 08 lessons; about 15 minutes for each check; works on a phone"
prerequisites: [clf-08-01, clf-08-03, clf-08-04]
pillars: [operational-excellence, reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html"
  - "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"
  - "https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html"
  - "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html"
  - "https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html"
  - "https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html"
---

# Module 08 mastery check: choose the way in, the watcher and the messenger

**For:** an adult studying alone, possibly new to IT, who has finished lessons [08.01](01-four-ways-in.md), [08.03](03-watching-workloads.md) and [08.04](04-connecting-parts-shipping-software.md). **Time:** about 15 minutes per check.

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 09.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

**A1.** A chain of language schools opens a branch every few months, each with its own copy of the same AWS setup. Every copy must match exactly. Which way into AWS fits best?

- A. The AWS Management Console, following the head office's written checklist
- B. An AWS CloudFormation template, with the branch's name as a parameter
- C. An AWS SDK, called from the schools' booking website
- D. A saved script of AWS CLI commands that creates each resource in turn

<details><summary>Answer</summary>

**B is right.** The job repeats and copies must match, so a template fits.

- **A is wrong.** Each pass by hand can miss a setting.
- **C is wrong.** An SDK is for a program's code.
- **D is wrong.** A script repeats steps; it doesn't describe the finished setup.

</details>

**A2.** An administrator must, once, turn on versioning for 60 existing S3 buckets named `logs-` something. Which way in fits best?

- A. The AWS Management Console, opening each bucket's properties in turn
- B. A new CloudFormation template that describes the 60 `logs-` buckets
- C. AWS SDK calls added to the company's customer-facing website
- D. AWS CLI commands that find the `logs-` buckets and change each one

<details><summary>Answer</summary>

**D is right.** Once, but many things: a few commands do all 60 in minutes.

- **A is wrong.** 60 passes through the same pages invite a skipped bucket.
- **B is wrong.** A template pays back when a setup is built again and again.
- **C is wrong.** An admin change doesn't belong in the website's code.

</details>

**A3.** A program on Amazon EC2 receives a thermostat reading from each home every minute and must store each one in Amazon DynamoDB as it arrives. How should the program reach DynamoDB?

- A. The program calls DynamoDB through the AWS SDK for its language
- B. An operator runs an AWS CLI command for each batch of readings
- C. A CloudFormation stack is updated with each new reading
- D. Staff enter the readings through the DynamoDB pages of the console

<details><summary>Answer</summary>

**A is right.** A program makes the calls while it runs.

- **B is wrong.** No operator could keep up.
- **C is wrong.** CloudFormation builds infrastructure; readings are data.
- **D is wrong.** The console is for people clicking.

</details>

**A4.** An agency builds each client's test environment by hand, and parts of old ones are sometimes left running. It plans to use a CloudFormation template instead. Which TWO explain how that lowers its costs? (Select TWO.)

- A. AWS charges a lower rate for resources that CloudFormation creates
- B. Deleting a stack removes what it made, so forgotten parts stop billing
- C. CloudFormation chooses the cheapest instance type for each resource
- D. Each new environment takes minutes of staff time instead of hours
- E. Resources in a stack stop billing while nobody is using them

<details><summary>Answer</summary>

**B and D are right.** Savings come from staff time and from deleting a stack, which removes what it created (apart from resources set to be kept).

- **A is wrong.** A resource costs the same whoever created it.
- **C is wrong.** CloudFormation builds exactly what the template says.
- **E is wrong.** Resources in a stack bill like any others while they exist.

</details>

**A5.** A bank wants branch IT staff to start a standard file-server setup, with fixed sizes and tags, without permission to create EC2 instances or security groups themselves. Which approach fits best?

- A. Publish it as an AWS Service Catalog product
- B. Give branch staff the template and permissions to create its resources
- C. Add an AWS Config rule that reports nonstandard file servers
- D. Create an Elastic Beanstalk environment for each branch

<details><summary>Answer</summary>

**A is right.** Staff launch only approved templates, within limits, through a role that does the building.

- **B is wrong.** It hands over the permissions the bank wants to withhold.
- **C is wrong.** Config checks how resources are configured; it doesn't launch anything.
- **D is wrong.** Beanstalk runs application code; it doesn't control who may launch what.

</details>

**A6.** A food-delivery app's "place order" request passes through an API, two services and a payment provider. For one slow order, the developers want to see how long each part took. What should they use?

- A. A CloudWatch alarm on the API's average response time
- B. AWS CloudTrail Event history
- C. AWS X-Ray traces of the order requests
- D. The AWS Health Dashboard

<details><summary>Answer</summary>

**C is right.** A trace times each part of one request.

- **A is wrong.** An average can't say which part of one request was slow.
- **B is wrong.** CloudTrail records actions on the account, not request timings.
- **D is wrong.** The Health Dashboard reports problems on AWS's side.

</details>

**A7.** Which TWO of these questions need AWS CloudTrail to answer? (Select TWO.)

- A. Who changed the web servers' security group rules last week?
- B. How high did the web servers' CPU use climb last week?
- C. Which part of order 5521's request took four seconds?
- D. Which identity created an access key on Tuesday, and from what IP address?
- E. How many error lines did the payment function write overnight?

<details><summary>Answer</summary>

**A and D are right.** Both ask who did something to the account.

- **B is wrong.** CPU use is a CloudWatch metric.
- **C is wrong.** Time inside one request is an X-Ray question.
- **E is wrong.** Lines a function writes are in CloudWatch Logs.

</details>

**A8.** Which TWO matches are right? (Select TWO.)

- A. Print jobs wait for the one print worker: Amazon SNS
- B. Each sale reaches the seat map, a fraud check and a queue at once: Amazon SNS
- C. A refund waits two days for approval, then pays out: Amazon SQS
- D. Designed receipts from the company's own domain: Amazon SNS
- E. Archive the day's sales every night at 01:00: Amazon EventBridge

<details><summary>Answer</summary>

**B and E are right.** One message to several receivers is SNS; a timetable is EventBridge Scheduler.

- **A is wrong.** Work that waits for one worker belongs in an SQS queue.
- **C is wrong.** Steps in order with a wait for a person is AWS Step Functions.
- **D is wrong.** Designed mail from your own domain is Amazon SES.

</details>

**A9.** A gym plans to send members a designed monthly newsletter by subscribing every member's email address to an Amazon SNS topic. What is the main problem?

- A. SNS delivers only to code, such as queues and functions; use Amazon SQS
- B. SNS delivers each message to one subscriber; create a topic per member
- C. SNS emails only people with IAM users; create a user for each member
- D. SNS email is for opt-in alerts and can't be designed; use Amazon SES

<details><summary>Answer</summary>

**D is right.** Members would have to confirm, and the body can't be customized; SES sends designed mail from your own domain.

- **A is wrong.** SNS supports email subscriptions; SQS delivers no email at all.
- **B is wrong.** SNS delivers each message to every subscriber.
- **C is wrong.** Email subscribers need no AWS identity.

</details>

**A10.** A team wants (1) each change compiled and tested automatically, with no build servers, and (2) every change taken through build, tests, approval and deployment, in order. Which pairing fits?

- A. (1) AWS CodePipeline; (2) AWS CodeBuild
- B. (1) AWS CodeDeploy; (2) AWS CodePipeline
- C. (1) AWS CodeBuild; (2) AWS CodePipeline
- D. (1) AWS Cloud9; (2) AWS CodeBuild

<details><summary>Answer</summary>

**C is right.** CodeBuild compiles and tests; CodePipeline runs the stages in order.

- **A is wrong.** It swaps the two.
- **B is wrong.** CodeDeploy doesn't compile or test, and it's out of scope.
- **D is wrong.** Cloud9 is a code editor, closed to new customers since 2024-07-25.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 08.01a | [Infrastructure as code](01-four-ways-in.md#infrastructure-as-code-describes-the-end-result-in-a-file) |
| A2, B2 | 08.01a | [One-time or repeatable](01-four-ways-in.md#one-time-or-repeatable-the-question-that-picks-the-way-in) |
| A3, B3 | 08.01a | [The SDK](01-four-ways-in.md#an-sdk-puts-aws-calls-inside-your-own-program) |
| A4, B4 | 08.02a | [Automation](01-four-ways-in.md#automation-makes-work-repeatable-and-cheaper) |
| A5, B5 | 08.02a | [Service Catalog](01-four-ways-in.md#service-catalog-lets-others-launch-only-what-youve-approved) |
| A6, B6 | 08.03a | [X-Ray](03-watching-workloads.md#x-ray-follows-one-request-through-every-part-it-touches) |
| A7, B7 | 08.03a | [CloudTrail](03-watching-workloads.md#cloudtrail-records-actions-on-your-account-not-how-your-application-runs) and [Pick the service](03-watching-workloads.md#pick-the-service-by-the-question-it-must-answer) |
| A8, B8 | 08.04a | [Choose by the shape of the message](04-connecting-parts-shipping-software.md#choose-by-the-shape-of-the-message) |
| A9, B9 | 08.04a | [SNS and SES](04-connecting-parts-shipping-software.md#an-email-from-sns-is-an-alert-an-email-from-ses-is-your-mail) |
| A10, B10 | 08.04a | [CodeBuild and CodePipeline](04-connecting-parts-shipping-software.md#shipping-software-codebuild-builds-and-tests-codepipeline-runs-the-release) |

## Check B: parallel retest

Question B1 tests the same objective as A1, and so on. The pass mark is the same: 8 of 10.

**B1.** Rebuilding a deleted staging environment by hand took two days and still missed a rule. The team wants to rebuild it exactly, in minutes, next time. Which approach fits best?

- A. Take screenshots of every console page to follow next time
- B. Add AWS SDK calls for staging to the application's code
- C. Describe staging in an AWS CloudFormation template and rebuild it as a stack
- D. Keep a list of the AWS CLI commands typed during the last rebuild

<details><summary>Answer</summary>

**C is right.** A template records the finished setup, every rule included, and rebuilds it in one step.

- **A is wrong.** Screenshots still need a person to click through every page.
- **B is wrong.** Building an environment isn't the application's job.
- **D is wrong.** A list of typed commands records steps, including the ones that missed the rule.

</details>

**B2.** Once, an engineer must set a 30-day retention period on 50 existing CloudWatch Logs log groups named with the prefix `/app/`. Which way in fits best?

- A. AWS CLI commands that select the log groups by prefix and change each
- B. The CloudWatch console, editing each of the 50 log groups by hand
- C. An AWS SDK call added to each application, run whenever it starts
- D. An AWS Service Catalog product launched once for each `/app/` log group

<details><summary>Answer</summary>

**A is right.** Once, on many existing resources.

- **B is wrong.** 50 rounds of clicks invite a missed group.
- **C is wrong.** A one-time change doesn't belong in application code.
- **D is wrong.** Service Catalog launches new setups; it doesn't change existing ones.

</details>

**B3.** A hotel's check-in app must put a message in an Amazon SQS queue each time a guest checks in. How should the messages be sent?

- A. A housekeeping supervisor sends each message with the AWS CLI
- B. A CloudFormation template creates a new message for each guest
- C. An hourly CLI script that sends the hour's check-ins
- D. The app sends each message through an AWS SDK

<details><summary>Answer</summary>

**D is right.** The app's code makes the call at each check-in.

- **A is wrong.** A person relaying each check-in would miss some.
- **B is wrong.** A template describes the queue, not the messages.
- **C is wrong.** It delays every message by up to an hour.

</details>

**B4.** A charity's hand rebuild of its site took three days and missed a security group rule. A volunteer proposes a CloudFormation template. Which TWO benefits would that bring? (Select TWO.)

- A. A rebuild would include every rule in the file, with no step to forget
- B. AWS would refund the cost of any outage caused by the template
- C. The template would restore the donation records along with the servers
- D. The servers built from it would no longer need security patches
- E. The site could be rebuilt in one step, so it's down for less time

<details><summary>Answer</summary>

**A and E are right.** The same file builds the same setup, in one step.

- **B is wrong.** AWS refunds nothing for mistakes in your own setup.
- **C is wrong.** A template rebuilds resources, not the data in them.
- **D is wrong.** Patching your servers stays your job, however they were built.

</details>

**B5.** A studio wants designers to launch an approved test-server setup themselves, choosing only allowed sizes, without being able to create other resources. Which approach fits best?

- A. Attach `AdministratorAccess` to the designers so they can run the template
- B. Share the template through AWS Marketplace for the designers to buy
- C. Publish the template as an AWS Service Catalog product with a constraint on sizes
- D. Have the designers copy the setup in the console from the team's screenshots

<details><summary>Answer</summary>

**C is right.** The product launches an approved template within limits; designers need no wider permissions.

- **A is wrong.** Full administrator access breaks least privilege.
- **B is wrong.** Marketplace sells third-party software.
- **D is wrong.** Designers would need wide permissions, and copies could differ.

</details>

**B6.** A clinic's booking request goes through a front end, a function, a database and an insurance check. The function's average duration tripled. Which tool shows which part slows down a single booking?

- A. The scheduling function's duration metric, at one-minute detail
- B. AWS X-Ray traces of booking requests
- C. AWS CloudTrail Event history for the scheduling function
- D. A CloudWatch dashboard of the function's metrics

<details><summary>Answer</summary>

**B is right.** A trace times each call in one booking.

- **A is wrong.** Finer detail still describes the whole function.
- **C is wrong.** CloudTrail records actions on the account, not request timings.
- **D is wrong.** A dashboard shows the same metrics side by side.

</details>

**B7.** Which TWO of these questions need AWS CloudTrail to answer? (Select TWO.)

- A. How many requests per minute did the load balancer handle?
- B. Which role stopped the database instance at 02:10 Sunday?
- C. Which downstream call made request 88 slow?
- D. Did AWS have a service problem in the Region on Sunday?
- E. Who attached `AdministratorAccess` to the intern's user last month?

<details><summary>Answer</summary>

**B and E are right.** Both are actions on the account, within Event history's 90 days.

- **A is wrong.** Request counts are a CloudWatch metric.
- **C is wrong.** Following one request is X-Ray's job.
- **D is wrong.** AWS's own problems are on the AWS Health Dashboard.

</details>

**B8.** Which TWO matches are right? (Select TWO.)

- A. Uploads wait for a free transcoding worker, none lost if one crashes: Amazon SQS
- B. A price change reaches the website, the app and a partner feed at once: Amazon SQS
- C. When any bucket's settings change, run a check function: AWS Step Functions
- D. A claim is checked, waits a week for an adjuster, then is paid or refused: AWS Step Functions
- E. Designed confirmations from the shop's own domain: Amazon EventBridge

<details><summary>Answer</summary>

**A and D are right.** Work waiting for one worker is a queue; steps with a long wait for a person is Step Functions.

- **B is wrong.** One message to several receivers at once is an SNS topic.
- **C is wrong.** Reacting to something that happened in AWS is an EventBridge rule.
- **E is wrong.** Designed mail from your own domain is Amazon SES.

</details>

**B9.** A startup's receipts arrive from an SNS no-reply address in plain text, and customers who ignored a subscription confirmation got none. What should it change?

- A. Request production access, because its SES account is still in the sandbox
- B. Send receipts with Amazon SES instead of through an SNS topic
- C. Move receipts from Amazon SES to an SNS topic
- D. Add a dead-letter queue to its SQS queue

<details><summary>Answer</summary>

**B is right.** Those are the marks of SNS email, meant for opt-in alerts; SES sends the company's own mail.

- **A is wrong.** No SES customer is asked to confirm a subscription.
- **C is wrong.** It reverses the services.
- **D is wrong.** A queue delivers no email at all.

</details>

**B10.** A team's CodePipeline build stage runs on a server it patches by hand. It wants a managed service to compile and test instead. Which service should it use?

- A. AWS CodeDeploy
- B. AWS Cloud9
- C. AWS OpsWorks
- D. AWS CodeBuild

<details><summary>Answer</summary>

**D is right.** CodeBuild compiles and tests with no build servers, and CodePipeline calls it.

- **A is wrong.** CodeDeploy deploys built code, and it's out of scope.
- **B is wrong.** Cloud9 is a code editor, closed to new customers since 2024-07-25.
- **C is wrong.** AWS OpsWorks was shut down on 2024-05-01.

</details>

---

"Module 08 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
