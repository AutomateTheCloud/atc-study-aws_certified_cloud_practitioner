---
type: lesson
id: clf-08-01
title: "Four ways in, and infrastructure as code"
tasks: ["3.1", "1.4"]
objectives: ["08.01a", "08.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 07 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-07-01, clf-06-01, clf-04-00, clf-02-06, guardrails-04]
terms_introduced: [AWS Management Console, AWS CLI, AWS CloudShell, AWS SDK, programmatic access, infrastructure as code (IaC), one-time operation, repeatable process, AWS CloudFormation, template, stack, AWS Service Catalog]
pillars: [operational-excellence, reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html"
  - "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html"
  - "https://docs.aws.amazon.com/sdkref/latest/guide/overview.html"
  - "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html"
  - "https://aws.amazon.com/cloudformation/pricing/"
  - "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html"
---

# Every way into AWS reaches the same services; a template is the way to build the same setup again and again

You can click in the console, type commands in the AWS CLI, call AWS from a program with an SDK, or describe a whole setup in a template and let CloudFormation build it. The exam asks you to pick the right one, and the deciding question is whether the job is done once or must be repeated exactly.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md), where you made a bucket in the console, and [primer page 04](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md), where you ran a command in CloudShell.

## Warm-up: what you remember

1. From lesson 06.01: you start ten EC2 instances from the same AMI. What do they have in common?
2. From Module 04: why does this guide run commands in CloudShell instead of creating an access key?

<details><summary>Feedback</summary>

1. **The same operating system and software,** because an AMI is a template for a server. This lesson ends with a template for a whole setup.
2. **CloudShell uses temporary credentials** from your console sign-in. An access key is long-term: anyone who copies it can use it until someone deletes it.

</details>

## What you'll learn

By the end of this lesson, you can choose the console, the CLI, an SDK or infrastructure as code for a task (objective 08.01a), and explain how infrastructure as code makes work repeatable and cheaper (objective 08.02a).

Try this before you read on, and guess if you're unsure: the bakery's owner wants the whole setup built again, exactly the same, in US East (Ohio). Which way in suits that?

## The big picture: four doors, one set of services

![The four ways into AWS compared on how you work, what each is best for, whether it's repeatable and its exam clue words, with the repeatable row highlighted.](../../images/08-01-four-ways.svg)

*Notice the highlighted row. Only infrastructure as code repeats the end result rather than the steps, which is why it wins whenever copies must match.*

**Long description.** Four columns, Console, AWS CLI, AWS SDKs and Infrastructure as code, on four rows. How you work: clicking; typed commands, saved as a script; calls in your program's code; a template of the end state. Best for: seeing, learning and one-time tasks; quick or bulk tasks; applications that use AWS while they run; building and copying whole setups. Repeatable, highlighted: no; steps only, if scripted; yes, the same calls each run; yes, the same setup anywhere. Clue words: visual, one-time; command line, script; application code; template, identical environments. Notes say the IaC service on AWS is CloudFormation, and CloudShell is a place to run the CLI.

All four doors reach the same services, where IAM checks the same permissions. So a user denied a permission in the console is denied it in the CLI too, and CloudTrail records the action whichever door it came through ([What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), checked 2026-10-24).

## Four ways in

### The console is for seeing, learning and doing something once

The **AWS Management Console** is the website where you sign in and work with every AWS service by pointing and clicking ([What is the AWS Management Console?](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html), checked 2026-10-24). It's the best way to learn a service and look around an account. But only the result is saved: the steps live in your memory.

#### "Console clicks are fine for production" is wrong

You may have heard that building production by clicking is fine as long as it works. It isn't, for anything that must be rebuilt, copied or reviewed: a hand-built setup can't be rebuilt or copied exactly, and leaves no file a colleague can check. The Well-Architected Framework lists manual changes as an anti-pattern in [REL08-BP05 Deploy changes with automation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html). It's tempting because everyone learns in the console and the first build works. The console is still right for *looking* at production.

### The CLI turns each action into a command you can save and run again

The **AWS CLI** (AWS Command Line Interface) is a free, open-source tool that sends instructions to AWS as typed commands, such as `aws s3 ls`. Every infrastructure administration function in the console is also in the CLI ([What is the AWS CLI?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), checked 2026-10-24). Saved in a script, forty commands cost the same effort as one, so the CLI suits bulk and routine work. A script lists *steps*, though: run it twice and it tries everything again, which can fail or make duplicates.

**AWS CloudShell**, a command line in the browser that's already signed in as you, is where the labs run the CLI, but the exam guide lists it as **out of scope** (checked 2026-10-24): on the exam it's at most a wrong option.

### An SDK puts AWS calls inside your own program

An **AWS SDK** (software development kit) is a set of code libraries, for a language such as Python, JavaScript or Java, that lets a program call AWS services ([AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)). When the code runs with an IAM role, the SDK signs each request with that role's temporary credentials. Use it when a program calls AWS while it runs: the bakery's website saves each cake photo to S3 through an SDK, with no person involved. Using AWS from code or commands, rather than clicks, is **programmatic access**; the exam's examples are APIs, SDKs and the CLI.

### Infrastructure as code describes the end result in a file

**Infrastructure as code (IaC)** means writing down the resources you want, with their settings, in a text file called a **template**, and letting a service build them. On AWS that service is **AWS CloudFormation**. A script says *how* (do this, then that); a template says *what* should exist, and CloudFormation works out the order. So the same template builds the same setup every time, in any Region you choose ([What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), checked 2026-10-24). That answers the prequestion.

## One-time or repeatable: the question that picks the way in

Task [3.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.1) asks you to choose between the console, programmatic access and IaC, and to tell a **one-time operation** (done once, nobody repeats it exactly) from a **repeatable process** (done again, with the same result each time). Three questions settle almost every case:

1. **Does a program do it while it runs?** Then an SDK.
2. **Will it happen again, or must copies match?** Then write it down: a template for whole setups, a script for routine tasks.
3. **Is it one thing or many?** One thing, once, suits the console. Many things, even once, suit the CLI.

> **Your turn:** sort the owner's list. (a) Check last month's bill. (b) Save each customer's receipt to S3 as they pay. (c) Delete 40 old test snapshots tagged `env=test`. (d) Build the Ohio copy, and a test copy every Monday.

<details><summary>Model answer</summary>

(a) **The console:** a person, once, one thing. (b) **An SDK:** a program does it at every payment. (c) **The CLI:** once, but many. (d) **A CloudFormation template:** it repeats, and the copies must match.

</details>

## CloudFormation builds a whole setup from a template

You give CloudFormation a template, written in YAML or JSON, and it builds a **stack**: every resource in the file, created, changed and deleted as one unit ([How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html)). If creation fails partway, it rolls back what it made. Deleting the stack deletes its resources, with a few exceptions such as a resource set to be kept or a bucket that still holds objects, so nothing is forgotten and left running. To copy the bakery's setup to US East (Ohio), you create a second stack from the same file; nothing is typed by hand. A template rebuilds resources, not what's in them: the Ohio database and bucket start empty, so the orders and photos need backups or replication there too (Module 03). CloudFormation itself has no extra charge for AWS's own resource types; you pay for what it creates ([AWS CloudFormation pricing](https://aws.amazon.com/cloudformation/pricing/), checked 2026-10-24).

### Service Catalog lets others launch only what you've approved

The bakery's new developer needs her own test copy each week, but giving her permission to create networks and databases would break least privilege. **AWS Service Catalog** lets administrators publish approved CloudFormation templates as products, and users launch only those, within set limits, through a role that does the building, so they need no wider permissions ([What is Service Catalog?](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html), checked 2026-10-24). CloudFormation is the engine; Service Catalog is the shop counter with rules. Exam clues for it: "approved", "self-service", "only launch what's allowed".

## Automation makes work repeatable and cheaper

Task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4) asks for the **benefits of automation**. A template brings **fewer mistakes** (no missed route or rule), **speed** (a copy takes minutes of a person's time, not hours), **consistency** (test, production and the Ohio copy match), **clean deletion** (nothing forgotten keeps billing, and the test copy can exist only Monday to Friday) and **faster recovery** (a rebuild is one step).

There's no discount: a resource costs the same whether a person or CloudFormation created it. The savings come from staff time, avoided mistakes and resources that don't sit idle. For one throwaway resource, the console is cheaper.

## Summary

- **Four ways in, one set of services:** the console, the CLI, the SDKs and CloudFormation all reach the same services, under the same IAM permissions, recorded by CloudTrail.
- **Console** for looking, learning and one-off changes; **CLI** for quick and bulk work and scripts; **SDK** for programs that call AWS while they run; **IaC** for whole setups that must be repeated or copied. CloudShell runs the CLI in your browser but is out of the exam's scope.
- **CloudFormation** builds a stack from a template and deletes it as a unit; the same template builds the same setup in any Region, but not the data.
- **Service Catalog** lets others launch only approved templates, without wider permissions.
- **Automation** saves money through fewer mistakes, less staff time, consistent copies, clean deletion and faster recovery, not through a lower price per resource.

## Practice

1. **A company must create the same set of resources for each new customer, identically, several times a month. Which fits best?**

   A. The console, following a written checklist\
   B. Infrastructure as code, with AWS CloudFormation\
   C. AWS CloudShell\
   D. AWS Support

   <details><summary>Feedback</summary>

   **B is right.** The job repeats and copies must match, so a template builds the same resources each time.

   - **A is wrong.** Every pass by hand can miss or mistype a step.
   - **C is wrong.** CloudShell is a place to run commands, and it's out of the exam's scope.
   - **D is wrong.** AWS Support helps with problems; it doesn't build resources.

   </details>

2. **A developer's mobile app must upload photos to Amazon S3. Which option lets her code call S3 in the app's programming language?**

   A. The AWS Management Console\
   B. The AWS CLI\
   C. An AWS SDK\
   D. AWS CloudFormation

   <details><summary>Feedback</summary>

   **C is right.** SDKs give programs libraries for calling AWS in their own language.

   - **A is wrong.** The console is for people clicking.
   - **B is wrong.** The CLI is for commands typed or scripted in a terminal.
   - **D is wrong.** CloudFormation builds infrastructure; it doesn't upload an app's photos.

   </details>

3. **A company wants developers to start only pre-approved environments, without giving them broad permissions to create resources. Which service fits best?**

   A. AWS CloudFormation alone\
   B. AWS Service Catalog\
   C. AWS Marketplace\
   D. AWS Elastic Beanstalk

   <details><summary>Feedback</summary>

   **B is right.** Service Catalog publishes approved products and launches them through a role, within limits.

   - **A is wrong.** CloudFormation builds from templates, but nothing limits which templates people use.
   - **C is wrong.** Marketplace sells third-party software, not your own approved setups.
   - **D is wrong.** Beanstalk runs application code; it doesn't control what developers may launch.

   </details>

**Next:** [Watching workloads](03-watching-workloads.md). To try all three ways on one bucket, do the [optional Lab 10](05-lab-10-same-bucket-three-ways.md).

## Where to check the current details

- [What is the AWS CLI?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) (checked 2026-10-24)
- [What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) (checked 2026-10-24)
- [What is Service Catalog?](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) (checked 2026-10-24)

---

"Four ways in, and infrastructure as code" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
