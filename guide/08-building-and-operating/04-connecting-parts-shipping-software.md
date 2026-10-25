---
type: lesson
id: clf-08-04
title: "Connecting parts, shipping software"
tasks: ["3.8"]
objectives: ["08.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 07, the guardrails primer and lesson 08.03; about 20 minutes; works on a phone"
prerequisites: [clf-08-03, clf-06-00, clf-07-00]
terms_introduced: [decoupling, message, Amazon SQS, queue, standard queue, FIFO queue, Amazon SNS, topic, subscription, fan-out, Amazon SES, Amazon EventBridge, event bus, rule, EventBridge Scheduler, AWS Step Functions, state machine, continuous integration, continuous delivery, AWS CodeBuild, AWS CodePipeline, pipeline]
pillars: [reliability, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"
  - "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html"
  - "https://aws.amazon.com/sqs/faqs/"
  - "https://docs.aws.amazon.com/sns/latest/dg/welcome.html"
  - "https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html"
  - "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html"
  - "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html"
  - "https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html"
  - "https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html"
  - "https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html"
  - "https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html"
  - "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/"
---

# Pick the messenger by the shape of the message, and let a pipeline build and release your code

AWS has a service for each shape of conversation between parts (SQS, SNS, EventBridge, Step Functions and SES), and the exam asks you to choose by shape. It also asks which tool builds code (CodeBuild) and which runs the release (CodePipeline).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** [Watching workloads](03-watching-workloads.md), where an alarm notifies an SNS topic.

## Warm-up: what you remember

1. From Module 07: a delivery partner's app asks Amazon API Gateway for an order and waits. If the function behind it has crashed, what does the app get?

<details><summary>Feedback</summary>

1. **An error, at once.** The app waited for an answer that couldn't come. This lesson shows how to let work wait instead of fail.

</details>

## What you'll learn

By the end of this lesson, you can choose SQS, SNS, EventBridge, Step Functions or SES by the shape of the message, and name the service that builds code and the one that runs the release (objective 08.04a).

Try this before you read on, and guess if you're unsure: the owner wants an email when orders fail, and each customer wants an email confirming the order. Is that one service or two?

## The big picture: five shapes of message

![Five panels, one per service: SQS, a queue where work waits for a worker; SNS, a topic that pushes one message to every subscriber; EventBridge, a bus whose rules route events; Step Functions, steps in order; and SES, email from the bakery's domain to customers.](../../images/08-04-message-shapes.svg)

*Notice who waits in each panel. In a queue, the message waits for the worker. In a topic, nobody waits. In a workflow, Step Functions waits and remembers the next step.*

**Long description.** Five panels. SQS: the web server sends orders into a queue and a packing worker pulls them, so orders wait while the worker is down. SNS: the order function publishes once, and the topic pushes the message to the owner's email, a kitchen queue and an invoice function. EventBridge: AWS services, apps and SaaS partners send events to a bus whose rules route them to targets, or run a report at 23:00. Step Functions: deposit, baker check, owner approval and booking, in order. SES: the website emails customers from the bakery's own domain.

## Five services for messages

### SQS holds work in a queue until a worker pulls it

When the web server calls the packing system directly and waits, the two fail together: if packing is down for an hour, every order in that hour fails. Putting a queue in between is **decoupling**: each part can fail, slow down or grow without breaking the other. That's the reliability habit [REL04-BP02 Implement loosely coupled dependencies](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html).

**Amazon Simple Queue Service (Amazon SQS)** is that queue: one part sends a **message** (such as "order 1043: 14 cupcakes"), and a worker asks for messages when it's ready, processes each one, then deletes it ([What is Amazon SQS?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html), checked 2026-10-24). SQS never pushes. Messages wait 4 days by default, up to 14 ([Amazon SQS FAQ](https://aws.amazon.com/sqs/faqs/)), and each goes to one worker. A **standard queue** has nearly unlimited throughput but may deliver a message twice or out of order; a **FIFO queue** (first in, first out) keeps the order and processes each message exactly once, with lower throughput ([Amazon SQS queue types](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html)).

### SNS pushes one message to every subscriber of a topic

**Amazon Simple Notification Service (Amazon SNS)** delivers each message published to a **topic** to every **subscription** at once: email addresses, phone numbers for SMS, mobile apps, web addresses, SQS queues and Lambda functions ([What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html), checked 2026-10-24). Publishing once to many receivers is **fan-out**. A CloudWatch alarm notifies a topic, which is how the owner gets her alert, and an email address receives nothing until its owner confirms the subscription.

### An email from SNS is an alert; an email from SES is your mail

You may read that SNS "sends email", so it's AWS's email service. It isn't. **Amazon Simple Email Service (Amazon SES)** is the email platform: it sends and receives email from **your own addresses and domains**, for order confirmations, newsletters and other mail to customers ([What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html), checked 2026-10-24). AWS's SNS guide says SNS email bodies can't be customized and are meant for internal system alerts, not marketing ([Email subscriptions](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html)). The mix-up is natural because both put a message in an inbox.

![An SNS email subscription compared with Amazon SES on six rows: who receives it, who it's from, what it looks like, what's needed before the first send, what it's meant for, and a bakery example.](../../images/08-04-sns-vs-ses.svg)

*Notice the "Who it's from" row. A customer's receipt must come from the bakery, so it's SES.*

**Long description.** Two columns. Who receives it: SNS, subscribed addresses that confirmed; SES, any recipient once out of the sandbox. Who it's from: SNS, an SNS no-reply address; SES, your own verified domain. What it looks like: SNS, plain text you can't customize; SES, whatever you design. Before the first send: SNS, subscribe and confirm; SES, verify your domain and request production access. Meant for: SNS, internal alerts; SES, mail to customers. At the bakery: SNS tells the owner "Orders are failing"; SES tells each customer "Your order 1043 is confirmed".

So the prequestion needs two services: SNS for the owner's alert, SES for the customers' confirmations.

### EventBridge routes events by rules on what they say

**Amazon EventBridge** receives events from AWS services, your own applications and SaaS partners, and sends each to targets according to **rules** ([What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), checked 2026-10-24). AWS services feed each account's default **event bus** on their own, so a rule such as "an EC2 instance stopped" can trigger a function or an SNS topic with no code watching. **EventBridge Scheduler** runs a task on a timetable, such as every night at 23:00. With SNS, your code publishes to a topic it chose; with EventBridge, the event's content decides where it goes. "React to something that happened in AWS" points to EventBridge.

### Step Functions runs several steps in order and remembers where it is

**AWS Step Functions** runs workflows, also called **state machines**: steps carried out in order and tracked to the end ([What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), checked 2026-10-24). A step can call a Lambda function or another service, choose a path, retry, or wait for a person. The bakery's custom-cake order is a workflow, and a Standard workflow can wait a day for the owner's approval, which one Lambda invocation, limited to 15 minutes, can't. Amazon Simple Workflow Service (SWF) is an older service the exam guide lists as out of scope; next to Step Functions, it's most likely the distractor.

## Choose by the shape of the message

| | SQS | SNS | EventBridge | Step Functions | SES |
|---|---|---|---|---|---|
| **Shape** | One to one, waits | One to many, pushed | Routed by rules; schedules | Steps in order | Email to customers |
| **Who waits** | The message | Nobody | Nobody | The workflow | The customer's inbox |
| **Bakery use** | Orders for packing | "Order failed" to three places | "Server stopped"; 23:00 report | Custom-cake order | Order confirmations |

All five are managed and serverless: you pay for use and run no servers.

> **Your turn:** Name the service for each. (a) A price change and a sale for the same cake, one second apart, must be applied in the order sent. (b) The owner wants an email whenever anyone stops the web server. (c) The kitchen tablet, the accounting system and the owner must all hear about each large order at the same moment.

<details><summary>Model answer</summary>

(a) **An SQS FIFO queue:** a standard queue may deliver them out of order. (b) **EventBridge:** a rule on the default bus matches the stop event and sends it to an SNS topic the owner subscribed to. (c) **SNS:** one message, many receivers, pushed at once; in a queue, only one of them would get it.

</details>

## Shipping software: CodeBuild builds and tests, CodePipeline runs the release

In **continuous integration (CI)**, every code change is built and tested automatically; in **continuous delivery (CD)**, every change that passes is also prepared for release automatically ([Continuous delivery and continuous integration](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html)).

- **AWS CodeBuild** is a fully managed build service: it compiles source code, runs tests and produces packages ready to deploy, with no build servers to set up, patch or scale ([What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html), checked 2026-10-24).
- **AWS CodePipeline** is a continuous delivery service: it models the release as a **pipeline** of stages, such as source, build, test, approval and deploy, and runs each change through them in order, stopping if one fails ([What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)). It calls CodeBuild for the build and test stages.

![Five stages, Source, Build, Test, Approve and Deploy, under a bracket labeled AWS CodePipeline; Build and Test, highlighted, are done by CodeBuild.](../../images/08-04-pipeline.svg)

*Notice that CodeBuild appears inside two stages, while CodePipeline is the bracket over all five. One does work; the other runs the order of work.*

**Long description.** Under a bracket labeled "AWS CodePipeline: runs the stages in order and stops the release if one fails": Source, a code change is pushed; Build, highlighted, CodeBuild compiles, tests and packages; Test, highlighted, CodeBuild runs more tests; Approve, the owner approves after an SNS email; Deploy, CloudFormation updates both Regions. A note says CodeDeploy can also deploy, but it's out of the exam's scope.

### "CodeDeploy, Cloud9 or OpsWorks is the answer" is wrong

Older material offers these as current answers, and they sound like they belong next to CodeBuild. They aren't the answer on this exam (checked 2026-10-24). **AWS CodeDeploy** still deploys code, but the exam guide lists it as **out of scope**, so next to CodeBuild and CodePipeline it's most likely the distractor. **AWS Cloud9**, a code editor in the browser, has been **closed to new customers since 2024-07-25** ([AWS DevOps blog](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)). **AWS OpsWorks** was shut down on 2024-05-01.

## Summary

- **Decoupling:** a queue, topic or bus between parts lets work wait instead of failing.
- **SQS** holds messages until one worker pulls each (standard for throughput, FIFO for strict order); **SNS** pushes each message to every subscriber of a topic.
- **An SNS email is not SES:** SNS emails are plain alerts to people who subscribed; SES sends your own mail, from your domain, to customers.
- **EventBridge** routes events from AWS services, apps and SaaS partners by rules, and runs schedules; **Step Functions** runs steps in order, with choices, retries and waits.
- **CodeBuild** builds and tests; **CodePipeline** runs the release stages in order. CodeDeploy is out of scope; Cloud9 is closed to new customers.

## Practice

1. **The bakery's web server must hand each order to a packing worker that is sometimes offline for maintenance. No order may be lost. Which service?**

   A. Amazon SNS\
   B. Amazon SQS\
   C. Amazon SES\
   D. AWS CodePipeline

   <details><summary>Feedback</summary>

   **B is right.** The queue keeps each order until the worker pulls it.

   - **A is wrong.** SNS pushes at once; it doesn't hold work for a worker that's offline.
   - **C is wrong.** SES sends email.
   - **D is wrong.** CodePipeline releases software; it doesn't carry orders.

   </details>

2. **Which service sends the bakery's newsletter, with its logo, from the bakery's own address to customers who signed up?**

   A. An Amazon SNS email subscription\
   B. Amazon SES\
   C. Amazon EventBridge\
   D. Amazon SQS

   <details><summary>Feedback</summary>

   **B is right.** SES sends mail you design, from your own verified domain.

   - **A is wrong.** SNS email bodies can't be customized, and SNS email is meant for alerts, not marketing.
   - **C is wrong.** EventBridge routes events; it doesn't send email.
   - **D is wrong.** SQS holds messages for workers; it doesn't deliver to inboxes.

   </details>

3. **A loan application needs a credit check, then a manager's approval that may take two days, then a contract. Which service coordinates the steps and waits for the manager?**

   A. AWS Lambda\
   B. Amazon SQS\
   C. AWS Step Functions\
   D. AWS Cloud9

   <details><summary>Feedback</summary>

   **C is right.** A Standard workflow keeps its place and can wait for a person.

   - **A is wrong.** One Lambda invocation lasts at most 15 minutes, and it doesn't coordinate steps.
   - **B is wrong.** A queue holds messages; it doesn't know about steps or approvals.
   - **D is wrong.** Cloud9 is a code editor, closed to new customers since 2024-07-25.

   </details>

**Next:** the [mastery check](07-check.md). To build the owner's alert yourself, do the [optional Lab 11](06-lab-11-alarm-on-errors.md).

## Where to check the current details

- [What is Amazon SQS?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) and [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (checked 2026-10-24)
- [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) and [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) (checked 2026-10-24)
- [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) (checked 2026-10-24)

---

"Connecting parts, shipping software" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
