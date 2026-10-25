---
type: check
id: clf-08-07
title: "Module 08 mastery check"
tasks: ["3.1", "3.8", "2.2", "1.4"]
objectives: ["08.01a", "08.02a", "08.03a", "08.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 08 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-08-01, clf-08-02, clf-08-03, clf-08-04]
pillars: [operational-excellence, reliability, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html"
  - "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html"
  - "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html"
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"
  - "https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html"
  - "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html"
  - "https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html"
  - "https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html"
---

# Module 08 mastery check

This check tells you whether you can do what Module 08 set out to teach: choose how to give AWS instructions, explain what a template buys you, pick the service that answers an operations question, and choose a messenger or a release tool. Every question is a short scenario, like the exam's.

**For:** an adult studying alone, possibly new to IT, who has finished the four Module 08 lessons. **Time:** about 20 minutes for each check. Reading works on a phone.

## How to use this check

Take Check A closed-book, without the lessons open, and write down your answers before you open any of them. Count your score: 10 of 12 (80%) or better is a pass. If you score below that, use the correction map to reread the sections behind each miss, then take Check B, the parallel retest, on another day if you can. If you pass, go on to the enrichment tasks.

Questions marked "(Select TWO.)" have two right answers; you need both for the point, as on the exam.

## Check A

**A1.** A chain of language schools opens a new branch every few months. Each branch gets its own copy of the same AWS setup (a network, two web servers, a database and a file bucket), and every copy must match the others exactly. Which way into AWS fits this job best?

- A. The AWS Management Console, following the head office's written checklist
- B. An AWS CloudFormation template, with the branch's name as a parameter
- C. An AWS SDK, called from the schools' booking website
- D. A saved script of AWS CLI commands that creates each resource in turn

<details><summary>Answer</summary>

**B is right.** The job repeats, and every copy must match. A template describes the end result, so the same file builds the same setup for each branch, and the parameter lets one file serve every branch without editing.

- **A is wrong.** A checklist helps, but every pass by hand is another chance to miss or mistype a setting, and nothing is left behind that a colleague can review or rerun.
- **C is wrong.** An SDK is for a program that calls AWS while it runs. Nothing in this job happens inside the booking website.
- **D is wrong.** This is the closest choice. A script lists steps, so it repeats them; it doesn't know what the finished setup should look like, can't compare a branch with the file, and can't delete a branch as one unit. For whole setups that must match, write a template.

</details>

**A2.** After a security review, an administrator must, once, turn on versioning for 60 existing S3 buckets whose names all start with `logs-`. Nobody will repeat the job. Which way in fits best?

- A. The AWS Management Console, opening each bucket's properties in turn
- B. A new CloudFormation template that describes the 60 `logs-` buckets
- C. AWS SDK calls added to the company's customer-facing website
- D. AWS CLI commands that find the `logs-` buckets and change each one

<details><summary>Answer</summary>

**D is right.** A person does it, once, but to many things. A few commands that select the buckets by name do all 60 in minutes, and the commands can be checked before they run.

- **A is wrong.** It works, but it means 60 passes through the same pages, each a chance to skip a bucket. "Once" points to the console only when the job is also small.
- **B is wrong.** A template earns its cost when a setup is built again and again. These buckets already exist; for a one-time change to them, writing a template is more effort than it saves.
- **C is wrong.** The website's code serves customers. A one-time administrative change doesn't belong in it.

</details>

**A3.** A smart-thermostat company runs a program on Amazon EC2 that receives a reading from each home's device every minute, day and night. The program must store each reading in an Amazon DynamoDB table as it arrives. How should the program reach DynamoDB?

- A. The program calls DynamoDB through the AWS SDK for its language
- B. An operator runs an AWS CLI command for each batch of readings
- C. A CloudFormation stack is updated with each new reading
- D. Staff enter the readings through the DynamoDB pages of the console

<details><summary>Answer</summary>

**A is right.** A program makes the calls while it runs, with no person involved, so it uses an SDK. The SDK also picks up the temporary credentials of the instance's IAM role, so no access key sits in the code.

- **B is wrong.** The CLI is for a person typing or scheduling commands. Readings arrive every minute around the clock; no operator could keep up.
- **C is wrong.** CloudFormation builds and changes infrastructure. Readings are data that the application stores, not resources in a stack.
- **D is wrong.** The console is for people looking and clicking, not for thousands of writes a day.

</details>

**A4.** After a Regional outage, a ticket-selling company builds its whole setup in a second Region from its CloudFormation template. The network, the servers and the database are ready in minutes, but the database holds none of the tickets sold before the outage. What explains this?

- A. The template needed a parameter that names the database's data
- B. CloudFormation deletes a database's data when it builds in a new Region
- C. A template describes resources and their settings, not the data stored in them
- D. Drift detection removed the tickets because they weren't in the template

<details><summary>Answer</summary>

**C is right.** A template rebuilds resources, so the second Region gets a database set up the same way, but empty. The ticket records reach the second Region only if backups or replicas of them are already there.

- **A is wrong.** Parameters supply values such as a name or a size when the stack is created. They don't carry stored records.
- **B is wrong.** CloudFormation deleted nothing. It built a new database, and a new database starts empty.
- **D is wrong.** Drift detection only reports differences between resources and the template; it never changes or removes anything.

</details>

**A5.** A small agency builds a test environment by hand for each client project, and parts of old environments are sometimes forgotten and left running. It plans to build each environment from a CloudFormation template instead. Which TWO explain how that lowers its costs? (Select TWO.)

- A. AWS charges a lower rate for resources that CloudFormation creates
- B. Deleting a stack removes what it made, so forgotten parts stop billing
- C. CloudFormation chooses the cheapest instance type for each resource
- D. Each new environment takes minutes of staff time instead of hours
- E. Resources in a stack stop billing while nobody is using them

<details><summary>Answer</summary>

**B and D are right.** The savings come from the work and the waste: one file builds each copy quickly, and deleting the stack removes what it created (apart from the few kinds of leftover lesson 08.02 lists), so forgotten parts stop costing money.

- **A is wrong.** A resource costs the same whether a person or CloudFormation created it.
- **C is wrong.** CloudFormation builds exactly what the template says, including the instance type you wrote. Choosing sizes is still your job.
- **E is wrong.** Resources in a stack bill like any others while they exist. Running only when needed comes from deleting the stack, or building and removing it on a schedule.

</details>

**A6.** A bank's central cloud team wants branch IT staff to start a standard file-server setup, with fixed sizes and required tags, whenever a branch needs one. Branch staff must not get permission to create EC2 instances or security groups themselves. Which approach fits best?

- A. Publish it as a Service Catalog product with a launch constraint
- B. Give branch staff the template and permissions to create its resources
- C. Add an AWS Config rule that reports nonstandard file servers
- D. Create an Elastic Beanstalk environment for each branch

<details><summary>Answer</summary>

**A is right.** AWS Service Catalog lets administrators publish approved templates as products in a portfolio. The portfolio is granted to branch staff; a launch constraint names an IAM role that builds the product, so they need no permissions on EC2 or security groups, and a template constraint can fix the sizes.

- **B is wrong.** It hands branch staff exactly the permissions the bank wants to withhold, and nothing would stop them changing the sizes or tags, or creating other resources.
- **C is wrong.** AWS Config records and checks how resources are configured. It doesn't give anyone a way to launch the approved setup.
- **D is wrong.** Elastic Beanstalk builds the setup for your application code. It doesn't control who may launch which approved setups.

</details>

**A7.** A food-delivery app's "place order" request passes through an API, a restaurant service, a driver-matching service and an outside payment provider. Some orders hang for several seconds. The developers want to see, for one slow order, how long each of those parts took. What should they use?

- A. A CloudWatch alarm on the API's average response time
- B. AWS CloudTrail Event history
- C. AWS X-Ray traces of the order requests
- D. The AWS Health Dashboard

<details><summary>Answer</summary>

**C is right.** A trace follows one request through every part it touches and times each part, so the slow link stands out. AWS now shows traces in the CloudWatch console, but "request tracing" is still X-Ray on the exam.

- **A is wrong.** An alarm can tell you that responses got slow, but an average over many requests can't say which part of one request took the time.
- **B is wrong.** CloudTrail records actions taken on the account, such as a settings change, not the timing of a customer's request.
- **D is wrong.** The Health Dashboard reports problems on AWS's side. Nothing here suggests AWS is at fault.

</details>

**A8.** A team creates a CloudWatch alarm on its checkout function's `Errors` metric, with an action that notifies an Amazon SNS topic. The alarm shows OK for a week. During a real failure it changes to ALARM, but nobody receives an email. What is the most likely cause?

- A. CloudWatch sends an email only after the third breaching period
- B. The email subscription to the topic was never confirmed
- C. The alarm should have watched CloudTrail events instead of a metric
- D. Alarm emails must go through Amazon SES, which wasn't set up

<details><summary>Answer</summary>

**B is right.** SNS sends nothing to an email address until its owner clicks the confirmation link. The week of OK proved only that the metric stayed below the threshold; CloudWatch doesn't test an alarm's actions for you.

- **A is wrong.** An alarm acts when its state changes, so the change to ALARM triggers the notification at once.
- **C is wrong.** CloudTrail records actions on the account. The function's errors are in its CloudWatch metric, which is the right thing to watch.
- **D is wrong.** A CloudWatch alarm notifies an SNS topic, and SNS delivers the email. SES is for your own mail to customers.

</details>

**A9.** After an incident, a security lead lists five questions. Which TWO need AWS CloudTrail to answer? (Select TWO.)

- A. Who changed the inbound rules of the web servers' security group last week?
- B. How high did the web servers' CPU use climb last week?
- C. Which part of order 5521's request took four of its five seconds?
- D. Which identity created a new access key on Tuesday, and from what IP address?
- E. How many error lines did the payment function write overnight?

<details><summary>Answer</summary>

**A and D are right.** Both ask who did something to the account: changing a security group and creating an access key are actions that CloudTrail records as events, with who, when and from where.

- **B is wrong.** CPU use is a metric, so CloudWatch has it.
- **C is wrong.** The time spent inside one request is a trace question, so X-Ray answers it.
- **E is wrong.** Lines a function writes go to CloudWatch Logs, where Logs Insights can search and count them.

</details>

**A10.** A concert-ticket company matches five needs to AWS services. Which TWO matches are right? (Select TWO.)

- A. Print jobs must wait until the one print worker is back online: Amazon SNS
- B. Each sold ticket must reach the seat map, a fraud function and a queue at once: Amazon SNS
- C. A refund needs a manager's approval, which can take two days, then a payment: Amazon SQS
- D. Each buyer gets a designed receipt from the company's own domain: Amazon SNS
- E. Every night at 01:00, run a function that archives the day's sales: Amazon EventBridge

<details><summary>Answer</summary>

**B and E are right.** One message to several receivers at the same moment is a topic, so SNS. A job on a timetable is EventBridge Scheduler.

- **A is wrong.** Work that must wait for one worker belongs in an Amazon SQS queue. SNS pushes at once and doesn't hold messages for a worker that's offline.
- **C is wrong.** Several steps in order, with a wait for a person, is a workflow, so AWS Step Functions. A queue holds messages but knows nothing about steps or approvals.
- **D is wrong.** Designed mail from your own domain to customers is Amazon SES. SNS email is a plain alert to people who subscribed.

</details>

**A11.** A gym's developer plans to send members a monthly newsletter, designed with the gym's logo, by subscribing every member's email address to an Amazon SNS topic. What is the main problem with that plan?

- A. SNS delivers only to code, such as queues and functions; use Amazon SQS
- B. SNS delivers each message to one subscriber; create a topic per member
- C. SNS emails only people with IAM users; create a user for each member
- D. SNS email is for opt-in alerts and can't be designed; use Amazon SES

<details><summary>Answer</summary>

**D is right.** Every member would have to confirm a subscription first, the email would come from an SNS address, and its body can't be customized; AWS meant SNS email for internal alerts, not marketing. Amazon SES sends mail you design, from your own domain.

- **A is wrong.** SNS does support email subscriptions; that's how alarm emails reach people. SQS holds messages for workers and delivers no email at all.
- **B is wrong.** That describes a queue. SNS delivers each message to every subscriber of the topic, so one topic would reach every member.
- **C is wrong.** Email subscribers need no AWS identity; they confirm by clicking a link. Giving customers IAM users would be a security mistake of its own.

</details>

**A12.** An app team wants two things on AWS: (1) each code change compiled and unit-tested automatically, with no build servers to manage; (2) every change taken through build, tests, a lead's approval and deployment, in that order, stopping if a stage fails. Which pairing fits?

- A. (1) AWS CodePipeline; (2) AWS CodeBuild
- B. (1) AWS CodeDeploy; (2) AWS CodePipeline
- C. (1) AWS CodeBuild; (2) AWS CodePipeline
- D. (1) AWS Cloud9; (2) AWS CodeBuild

<details><summary>Answer</summary>

**C is right.** AWS CodeBuild compiles code, runs tests and produces packages without build servers. AWS CodePipeline runs the release as stages in order, calls CodeBuild for the build and test stages, can pause for an approval, and stops when a stage fails.

- **A is wrong.** It swaps the two: CodePipeline runs the order of work; CodeBuild does the building.
- **B is wrong.** AWS CodeDeploy deploys code; it doesn't compile or test it. The exam guide also lists it as out of scope, so it's most likely a distractor.
- **D is wrong.** AWS Cloud9 is a code editor in the browser, closed to new customers since 2024-07-25, and CodeBuild doesn't run approvals or stages.

</details>

## Correction map

Find each item you missed, reread the section, then try the angle in the last column: it explains the same idea a different way from the lesson. The practice column names the lab that exercises it.

| Item | Objective | Reread | A different way to see it | Practice |
|---|---|---|---|---|
| A1 | 08.01a | [One-time or repeatable: the question that picks the way in](01-four-ways-in.md#one-time-or-repeatable-the-question-that-picks-the-way-in); [Infrastructure as code describes the end result in a file](01-four-ways-in.md#infrastructure-as-code-describes-the-end-result-in-a-file) | A script is a recipe's steps; a template is a photo of the finished dish that the kitchen works toward. To get the same dish every time, hand over the photo | [Lab 10](05-lab-10-same-bucket-three-ways.md), Parts B and C |
| A2 | 08.01a | [The CLI turns each action into a command you can save and run again](01-four-ways-in.md#the-cli-turns-each-action-into-a-command-you-can-save-and-run-again); [One-time or repeatable](01-four-ways-in.md#one-time-or-repeatable-the-question-that-picks-the-way-in) | Ask "how many?" after "how often?". Once and one: the console. Once and many: the CLI | [Lab 10](05-lab-10-same-bucket-three-ways.md), Part B |
| A3 | 08.01a | [An SDK puts AWS calls inside your own program](01-four-ways-in.md#an-sdk-puts-aws-calls-inside-your-own-program) | If nobody is at the keyboard when the call happens, the caller is a program, so the answer is an SDK | [Lab 10](05-lab-10-same-bucket-three-ways.md), the comparison table |
| A4 | 08.02a | [One template, many Regions and accounts, but not the data](02-iac-and-automation.md#one-template-many-regions-and-accounts-but-not-the-data) | A template is a building plan: it gives you a new, empty warehouse, not the stock that was in the old one | [Lab 10](05-lab-10-same-bucket-three-ways.md), Part C |
| A5 | 08.02a | [Automation makes work repeatable and cheaper](02-iac-and-automation.md#automation-makes-work-repeatable-and-cheaper) | Price per resource never changes. Look for savings in people's hours, in mistakes, and in things left running | [Lab 10](05-lab-10-same-bucket-three-ways.md), cleanup |
| A6 | 08.02a | [Service Catalog lets others launch only what you've approved](02-iac-and-automation.md#service-catalog-lets-others-launch-only-what-youve-approved) | CloudFormation is the engine; Service Catalog is the shop counter where staff pick only from the approved shelf | The lesson's Service Catalog check |
| A7 | 08.03a | [X-Ray follows one request through every part it touches](03-watching-workloads.md#x-ray-follows-one-request-through-every-part-it-touches) | A metric is the average speed on a road; a trace is one car's trip, with the time spent at each junction | [Lab 11](06-lab-11-alarm-on-errors.md), Check your work |
| A8 | 08.03a | ["OK" means below the threshold, not "working"](03-watching-workloads.md#ok-means-below-the-threshold-not-working); [SNS pushes one message to every subscriber of a topic](04-connecting-parts-shipping-software.md#sns-pushes-one-message-to-every-subscriber-of-a-topic) | A smoke alarm can read "no smoke" with its battery missing. Test the bell, not the reading | [Lab 11](06-lab-11-alarm-on-errors.md), steps 5 and 6 |
| A9 | 08.03a | [CloudTrail records actions on your account, not how your application runs](03-watching-workloads.md#cloudtrail-records-actions-on-your-account-not-how-your-application-runs); [Pick the service by the question it must answer](03-watching-workloads.md#pick-the-service-by-the-question-it-must-answer) | Underline the question word. "Who" points to CloudTrail; "how much" or "how many" to CloudWatch; "which part of this request" to X-Ray | [Lab 11](06-lab-11-alarm-on-errors.md), Check your work |
| A10 | 08.04a | [Choose by the shape of the message](04-connecting-parts-shipping-software.md#choose-by-the-shape-of-the-message) | Ask who waits. The message waits: SQS. Nobody waits: SNS. The workflow waits: Step Functions. A clock or an AWS event starts it: EventBridge | [Lab 11](06-lab-11-alarm-on-errors.md), Part B |
| A11 | 08.04a | [An email from SNS is an alert; an email from SES is your mail](04-connecting-parts-shipping-software.md#an-email-from-sns-is-an-alert-an-email-from-ses-is-your-mail) | Look at the "From" line. If it must be your company's own address, it's SES | [Lab 11](06-lab-11-alarm-on-errors.md), Part C |
| A12 | 08.04a | [Shipping software: CodeBuild builds and tests, CodePipeline runs the release](04-connecting-parts-shipping-software.md#shipping-software-codebuild-builds-and-tests-codepipeline-runs-the-release) | CodeBuild is a worker on the line; CodePipeline is the conveyor belt that moves each change from station to station | None; the lesson's pipeline figure |

## Check B: parallel retest

Take this after you have worked through the correction map. Each item tests the same objective as the Check A item with the same number, with a new scenario.

**B1.** An engineer accidentally deleted part of a company's staging environment: its subnets, a load balancer and two security groups. Rebuilding it by hand took two days and still missed a rule. The team wants to be able to rebuild staging exactly, in minutes, any time it breaks again. Which approach fits best?

- A. Take screenshots of every console page so the next rebuild can follow them
- B. Ask each developer to add AWS SDK calls for staging to the application's code
- C. Describe staging in an AWS CloudFormation template and rebuild it as a stack
- D. Keep a list of the AWS CLI commands that were typed during the last rebuild

<details><summary>Answer</summary>

**C is right.** A template records the finished setup, so CloudFormation can rebuild the same staging environment in one step whenever it's needed, with every rule in the file.

- **A is wrong.** Screenshots still need a person to click through every page, with the same chances to miss a rule as last time.
- **B is wrong.** SDK calls belong in a program that uses AWS while it runs. Building an environment is not the application's job.
- **D is wrong.** A list of typed commands records steps, including the ones that missed the rule. It doesn't describe the end result, and rerunning it can fail on resources that still exist.

</details>

**B2.** A company finds that 50 of its existing CloudWatch Logs log groups keep their data forever. Once, an engineer must set a 30-day retention period on all 50, which share the name prefix `/app/`. Which way in fits best?

- A. AWS CLI commands that select the log groups by prefix and change each
- B. The CloudWatch console, editing each of the 50 log groups by hand
- C. An AWS SDK call added to each application, run whenever it starts
- D. A Service Catalog product launched once for each `/app/` log group

<details><summary>Answer</summary>

**A is right.** It's a one-time job for a person, but on many existing resources. A command that selects the log groups by their prefix changes all 50 quickly and the same way.

- **B is wrong.** It works, but 50 rounds of the same clicks invite a missed group.
- **C is wrong.** The applications' code serves their users. A one-time administrative change doesn't belong there, and it would run again at every start.
- **D is wrong.** Service Catalog lets people launch approved new setups. It doesn't change settings on resources that already exist.

</details>

**B3.** A hotel's check-in app must put a message in an Amazon SQS queue each time a guest checks in, so the housekeeping system can prepare for the stay. Which way into AWS fits how these messages are sent?

- A. A housekeeping supervisor sends each message with the AWS CLI
- B. A CloudFormation template creates a new message for each guest
- C. A CLI script, run by a scheduled job each hour, that sends the hour's check-ins
- D. The app sends each message through an AWS SDK

<details><summary>Answer</summary>

**D is right.** The app's own code makes the call at each check-in, while it runs, so it uses an SDK, the one for its language. With an IAM role, the SDK finds temporary credentials on its own.

- **A is wrong.** The CLI suits a person's commands. Check-ins happen all day; a person relaying each one would be slow and would miss some.
- **B is wrong.** A template describes infrastructure, such as the queue itself, not the messages that pass through it.
- **C is wrong.** A scheduled script delays every message by up to an hour and needs its own way to find the check-ins. The app already knows the moment a guest checks in, so its own code should send the message then.

</details>

**B4.** A design firm's file storage is built from a CloudFormation template in Europe (Ireland). For disaster recovery, the team creates a second stack from the same template in Europe (London); the template lets CloudFormation name the buckets, so the names don't clash. What does the London stack hold right after it's created?

- A. Buckets set up like Ireland's, empty until the design files are copied there
- B. Buckets set up like Ireland's, already holding copies of every design file
- C. Every setting from Ireland, including changes made there by hand since
- D. Nothing yet, because one template can't build stacks in two Regions

<details><summary>Answer</summary>

**A is right.** The template rebuilds the resources and their settings. The files inside the Ireland buckets reach London only through S3 Replication or a backup copy.

- **B is wrong.** A template carries no data; new buckets start empty.
- **C is wrong.** A change made by hand in Ireland isn't in the template. It shows up only as drift in Ireland, and London is built without it.
- **D is wrong.** Building the same stack from one template in several Regions is exactly what CloudFormation is for.

</details>

**B5.** Last year a charity rebuilt its donation site by hand after an accident. The rebuild took three days and missed a security group rule that nobody noticed for weeks. A volunteer now proposes keeping the setup as a CloudFormation template in version control. Which TWO benefits would that bring? (Select TWO.)

- A. A rebuild would include every rule in the file, with no step to forget
- B. AWS would refund the cost of any outage caused by the template
- C. The template would restore the donation records along with the servers
- D. The servers built from it would no longer need security patches
- E. The site could be rebuilt in one step, so it's down for less time

<details><summary>Answer</summary>

**A and E are right.** The same tested file builds the same setup every time, so a rebuild misses nothing that's in it, and recovery takes one step, which means less downtime and less lost giving.

- **B is wrong.** AWS refunds nothing for mistakes in your own setup; what a template builds is your responsibility.
- **C is wrong.** A template rebuilds resources, not the data in them. The donation records need backups.
- **D is wrong.** Patching the operating system on your servers stays your job, however they were built.

</details>

**B6.** A game studio's platform team wants designers to launch an approved test-server setup on their own, choosing only from the instance sizes the team allows. The designers must not be able to create other resources or touch production. Which approach fits best?

- A. Attach the `AdministratorAccess` policy to the designers so they can run the template
- B. Share the template through AWS Marketplace for the designers to buy
- C. Publish the template as a Service Catalog product with a constraint on sizes
- D. Have the designers copy the setup in the console from the team's screenshots

<details><summary>Answer</summary>

**C is right.** A Service Catalog product launches an approved template; a template constraint limits the sizes, and a launch constraint's role builds it, so the designers need no wider permissions.

- **A is wrong.** Full administrator access breaks least privilege and lets the designers change production.
- **B is wrong.** AWS Marketplace sells third-party software. It doesn't hold a company's own approved setups for its staff.
- **D is wrong.** The designers would need permissions to create every resource by hand, and each copy could differ.

</details>

**B7.** A clinic's "book appointment" request goes through a web front end, a scheduling function, a database and an outside insurance check. CloudWatch shows that the scheduling function's average `Duration` tripled this week. The team wants to know which of those parts slows down a single booking. What should it use?

- A. The scheduling function's `Duration` metric, at one-minute detail
- B. AWS X-Ray traces of booking requests
- C. AWS CloudTrail Event history for the scheduling function
- D. A CloudWatch dashboard of the function's metrics

<details><summary>Answer</summary>

**B is right.** A trace splits one booking into its calls, with the time each took, so the team can see whether the database, the insurance check or the code itself is slow.

- **A is wrong.** Finer detail still describes the whole function, not the parts inside one request.
- **C is wrong.** CloudTrail records actions on the account, such as a change to the function's settings, not how long a request spent in each part.
- **D is wrong.** A dashboard shows the same metrics side by side. It adds a view, not the breakdown of a single request.

</details>

**B8.** Before relying on a new errors alarm, a shop owner wants proof that it will actually reach her inbox. The alarm notifies an SNS topic with her email address subscribed. Which check proves the email path?

- A. Publish a test message to the topic and see it arrive in her inbox
- B. Confirm that the alarm's state shows OK in the CloudWatch console
- C. Confirm that the alarm's graph shows data points for the metric
- D. Find the alarm's creation event in CloudTrail Event history

<details><summary>Answer</summary>

**A is right.** A message published to the topic travels the same path the alarm's notification will: through SNS to a confirmed subscription and into the inbox. If it doesn't arrive, the subscription isn't confirmed or the email is in spam.

- **B is wrong.** OK means only that the metric is below the threshold. CloudWatch doesn't test the alarm's actions.
- **C is wrong.** Data points show that the alarm can evaluate, not that a message can be delivered.
- **D is wrong.** The event proves someone created the alarm. It says nothing about whether its notification reaches anyone.

</details>

**B9.** A manager reviews a quiet Sunday that went wrong. Which TWO of her questions need AWS CloudTrail to answer? (Select TWO.)

- A. How many requests per minute did the load balancer handle on Sunday?
- B. Which role stopped the database instance at 02:10 on Sunday?
- C. Which downstream call made request 88 slow?
- D. Did AWS have a service problem in the Region on Sunday?
- E. Who attached the `AdministratorAccess` policy to the intern's user last month?

<details><summary>Answer</summary>

**B and E are right.** Stopping an instance and attaching a policy are actions on the account. CloudTrail records each one as an event, with who did it and when; both are within Event history's 90 days.

- **A is wrong.** Request counts are a load balancer metric in CloudWatch.
- **C is wrong.** Following one request through its calls is X-Ray's job.
- **D is wrong.** Problems on AWS's side are reported on the AWS Health Dashboard.

</details>

**B10.** An online video shop matches five needs to AWS services. Which TWO matches are right? (Select TWO.)

- A. Uploaded videos must wait until a transcoding worker is free, with none lost if one crashes: Amazon SQS
- B. A price change must reach the website, the mobile app and a partner feed at once: Amazon SQS
- C. When any S3 bucket's settings change in the account, run a check function: AWS Step Functions
- D. A claim is checked, waits up to a week for an adjuster's decision, then is paid or refused: AWS Step Functions
- E. Each customer gets a confirmation with the shop's logo from its own domain: Amazon EventBridge

<details><summary>Answer</summary>

**A and D are right.** Work that waits for one worker, and survives a crash, belongs in a queue: SQS hides a message while a worker handles it and shows it again if the worker fails. Several steps in order, with a long wait for a person, is a Step Functions workflow.

- **B is wrong.** One message to several receivers at the same moment is an Amazon SNS topic. In a queue, each message goes to one worker.
- **C is wrong.** Reacting to something that happened in AWS is an Amazon EventBridge rule, which AWS services feed on their own.
- **E is wrong.** Designed mail from your own domain is Amazon SES. EventBridge routes events; it doesn't send email.

</details>

**B11.** A startup's customers complain that their receipts arrive from an SNS no-reply address, in plain text, and that some never got any receipts after ignoring an email asking them to confirm a subscription. What has the startup done, and what should it change?

- A. Its SES account is still in the sandbox; it should request production access
- B. It sends receipts through an SNS topic; it should send them with Amazon SES
- C. It sends receipts through Amazon SES; it should move them to an SNS topic
- D. It sends receipts through an SQS queue; it should add a dead-letter queue

<details><summary>Answer</summary>

**B is right.** The no-reply sender, the plain text and the confirmation email are the marks of an SNS email subscription, which is meant for alerts to people who opted in. Receipts to customers are the company's own mail: Amazon SES sends them from its verified domain, designed as it likes, with no subscription to confirm.

- **A is wrong.** In the SES sandbox, mail to unverified addresses is refused, but no customer is asked to confirm a subscription, and the mail would come from the startup's own address.
- **C is wrong.** It reverses the services. SES is the right one for receipts; SNS is what's causing the complaints.
- **D is wrong.** A queue holds messages for workers; it doesn't deliver email at all, and a dead-letter queue only sets aside messages that keep failing.

</details>

**B12.** A team already releases through AWS CodePipeline, but its build stage runs on a server the team patches by hand, which is overloaded on release days. It wants a managed service to compile the code and run the tests in that stage instead. Which service should it use?

- A. AWS CodeDeploy
- B. AWS Cloud9
- C. AWS OpsWorks
- D. AWS CodeBuild

<details><summary>Answer</summary>

**D is right.** CodeBuild compiles code and runs tests with no build servers to set up, patch or scale, and CodePipeline can call it for the build and test stages.

- **A is wrong.** CodeDeploy deploys code that's already built. The exam guide lists it as out of scope, so it's most likely the distractor.
- **B is wrong.** Cloud9 was a code editor in the browser, closed to new customers since 2024-07-25. It doesn't run a pipeline's builds.
- **C is wrong.** AWS OpsWorks was shut down on 2024-05-01. It can't be the answer to any current question.

</details>

## Enrichment

For learners who passed Check A. Each task has no single right answer; compare yours with the model answer.

> **Your turn:** **Make Ohio alert too.** The owner says, "Once the Ohio copy exists, we're covered." The template builds the network, servers and order function. Name three things that must also be in Ohio for the owner to hear about failures there and for new code to reach both Regions, and say which one the template can't finish on its own. Justify the design with [REL08-BP05 Deploy changes with automation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html).

<details><summary>Model answer</summary>

1. **An alarm on the Ohio function's `Errors`**, because metrics and alarms belong to one Region; N. Virginia's alarm never sees Ohio's function.
2. **An SNS topic in Ohio with the owner's email subscribed.** The template can create the topic and the subscription, but it can't finish it: the owner must click the confirmation email for the Ohio subscription, or nothing is delivered. Prove it by publishing a test message.
3. **A pipeline that deploys the same template to both Regions,** so a change reaches Ohio and N. Virginia the same way. If someone updates only one Region by hand, the copies drift apart and the disaster plan quietly stops matching production.

REL08-BP05 names manual changes as an anti-pattern: putting the alarm and topic in the template, and every release through the pipeline, keeps both Regions built from one reviewed file. The data (orders and photos) still needs backups or replication in Ohio; the template brings none of it.

</details>

> **Your turn:** **The fix made at 2 a.m.** During an outage, the on-call engineer raises the order function's memory in the console, and the timeouts stop. The function belongs to a CloudFormation stack. Explain what risk the fix now carries for the bakery's Ohio copy and for future rebuilds, how the team finds such changes, and what it should do the next morning.

<details><summary>Model answer</summary>

The console change made the function differ from the template: that's drift. CloudFormation updates only what changed in the template, so the fix may survive later updates in N. Virginia, but the template still says the old memory size. The Ohio stack, any rebuild after a disaster, and the weekly test copy are all built from the file, so they come up with the setting that timed out. Drift detection on the stack reports the function as modified; it doesn't fix anything. The next morning, the team should put the new memory size into the template, review it with a change set, and deploy it through the pipeline, so the file is again the source of truth. An emergency change is fine; leaving it only in the console isn't.

</details>

> **Your turn:** **The order packed twice.** The bakery's orders reach the packing worker through an SQS standard queue. Twice this month, the same order was packed two times. Explain why a standard queue can do this, give two ways to stop the double packing, and say what each costs. Connect your answer to [REL04-BP04 Make mutating operations idempotent](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_idempotent.html).

<details><summary>Model answer</summary>

A standard queue delivers each message at least once, so occasionally it delivers one twice. The same can happen if a worker crashes after packing but before deleting the message: SQS shows it again to another worker. Two fixes:

- **Make the worker idempotent:** before packing, it checks a record of order numbers already packed, such as a small DynamoDB table, and skips an order it has seen. It costs some code and a lookup per order, and it also covers the crash case. This is what REL04-BP04 asks for: doing an operation twice has the same effect as doing it once.
- **Switch to a FIFO queue,** which processes each message exactly once and keeps order. It costs throughput, and a worker that crashes before deleting a message can still see it again, so the check in the first fix is still worth having.

Most teams do the first, because it protects against duplicates from any source, not only the queue.

</details>

---

"Module 08 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
