---
type: check
id: clf-10-07
title: "Module 10 mastery check"
tasks: ["3.7", "3.8"]
objectives: ["10.01a", "10.02a", "10.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished lessons 10.01 to 10.03; about 15 minutes for each check"
prerequisites: [clf-10-01, clf-10-02, clf-10-03]
pillars: [performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html"
  - "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"
  - "https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-availability-change.html"
  - "https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html"
  - "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html"
  - "https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html"
---

# Module 10 mastery check: match each need to the data, AI or end-user service built for it

**For:** an adult studying alone, possibly new to IT, who has finished lessons [10.01](01-analytics-in-five-verbs.md), [10.02](02-ai-and-ml.md) and [10.03](03-people-apps-and-devices.md). **Time:** about 15 minutes for each check. No AWS account is needed.

## How to use this check

Take Check A closed-book, and write down your answers before you open any feedback. You pass at 8 of 10; a "(Select TWO.)" question counts only if both choices are right. Below 8, use the correction map, then take Check B. Where the exam guide uses an older name, the options use it and the feedback gives today's (as of 2026-10-24).

## Check A

**A1.** A photo-printing website's orders should each go to just one free worker program, and be removed from the waiting list once printed. Which service should hold the orders while they wait?

- A. Amazon Kinesis Data Streams
- B. Amazon SNS
- C. Amazon SQS
- D. Amazon Data Firehose

<details><summary>Answer</summary>

**C is right.** In an SQS queue, a free worker takes a message, does the job and deletes it.

- **A is wrong.** Records in Data Streams stay after they're read, and every consumer can read every record.
- **B is wrong.** SNS pushes each message to every subscriber, so every worker would get every order.
- **D is wrong.** Amazon Data Firehose delivers streaming data to a store such as S3; no worker takes jobs from it.

</details>

**A2.** A Glue crawler has added a clinic group's appointment files in S3 to the Data Catalog. An analyst wants the average wait time per clinic, in SQL, without loading the data or setting up anything to run it on. Which service runs the question?

- A. AWS Glue
- B. Amazon Athena
- C. Amazon Quick Sight
- D. Amazon OpenSearch Service

<details><summary>Answer</summary>

**B is right.** Athena runs SQL on files in S3 where they sit, reads the table definition from the Glue Data Catalog, and is serverless.

- **A is wrong.** Glue described and cleaned the data, but it doesn't answer questions about it.
- **C is wrong.** Quick Sight shows results as dashboards; it isn't where the SQL runs.
- **D is wrong.** OpenSearch Service searches indexed text and logs; a SQL total is a query job.

</details>

**A3.** A store's website needs a search box that finds matching products among tens of thousands of descriptions at once, best matches first. Which service is built for this?

- A. Amazon OpenSearch Service
- B. Amazon Athena
- C. Amazon Quick Sight
- D. Amazon Redshift

<details><summary>Answer</summary>

**A is right.** OpenSearch Service keeps a search index of every word, so it finds and ranks matches at once. Website search is one of its main uses.

- **B is wrong.** Athena reads files to answer SQL questions; it doesn't keep a word index or rank matches.
- **C is wrong.** Quick Sight builds dashboards.
- **D is wrong.** Redshift is a warehouse for heavy, repeated reports, not for finding words in text.

</details>

**A4.** Rangers want thousands of trail-camera photos labeled with what each shows, such as deer, a person or a vehicle. The park has no machine learning staff. Which service fits?

- A. Amazon Macie
- B. Amazon SageMaker AI
- C. Amazon Textract
- D. Amazon Rekognition

<details><summary>Answer</summary>

**D is right.** Rekognition is a ready-made service that returns the objects and scenes it finds in images and video.

- **A is wrong.** Macie finds sensitive data in S3 buckets (Module 09).
- **B is wrong.** SageMaker AI is for building your own model when nothing ready-made fits, and the park has no one to build one.
- **C is wrong.** Textract reads documents, not scenes.

</details>

**A5.** A museum's exhibit descriptions are written in English only. Visitors must be able to hear each one, in English or German, in a natural voice. Which two services does the museum need? (Select TWO.)

- A. Amazon Transcribe
- B. Amazon Translate
- C. Amazon Lex
- D. Amazon Polly
- E. Amazon Comprehend

<details><summary>Answer</summary>

**B and D are right.** Translate turns the English text into German, and Polly reads both versions aloud.

- **A is wrong.** Transcribe runs the other way: speech in, text out.
- **C is wrong.** Lex builds bots that hold a conversation; visitors only listen.
- **E is wrong.** Comprehend describes text; it doesn't translate or speak.

</details>

**A6.** An online shop new to AWS in 2026 wants its data scientists to build a model that scores each order for fraud risk, learning from its own history of orders and chargebacks. Which service should they use?

- A. Amazon SageMaker AI
- B. Amazon Fraud Detector
- C. Amazon Macie
- D. Amazon Comprehend

<details><summary>Answer</summary>

**A is right.** SageMaker AI (formerly Amazon SageMaker) is where data scientists build, train and deploy their own model on their own data.

- **B is wrong.** Amazon Fraud Detector has been closed to new customers since 2025-11-07, and it's out of the exam's scope (checked 2026-10-24).
- **C is wrong.** Macie finds sensitive data in S3; it doesn't predict fraud.
- **D is wrong.** Comprehend finds meaning in text; it doesn't learn from order history.

</details>

**A7.** A shop owner wants "Amazon Q" for two jobs. Job 1: her developer wants help, in the AWS Management Console, understanding why an AWS resource failed to deploy. Job 2: a chat window on the shop's website that takes customers' return requests. Which pairing fits?

- A. Amazon Q Business for job 1, and Amazon Q Developer for job 2
- B. Amazon Q Developer for both jobs
- C. Amazon Lex for both jobs
- D. Amazon Q Developer for job 1, and Amazon Lex for job 2

<details><summary>Answer</summary>

**D is right.** "Amazon Q" is a family. Q Developer helps people who build and run on AWS; a bot that talks to your customers is built with Lex.

- **A is wrong.** Q Business answered employees' questions from company documents (and is closed to new customers).
- **B is wrong.** Q Developer helps the shop's builders, not its customers.
- **C is wrong.** Lex doesn't explain your AWS resources to your developer.

</details>

**A8.** Freelance illustrators each need only an agency's licensed Windows drawing program, from their own computers, with no copy installed there and no whole desktop each. Which service fits?

- A. Amazon WorkSpaces
- B. AWS Client VPN
- C. Amazon AppStream 2.0
- D. Amazon Lightsail

<details><summary>Answer</summary>

**C is right.** AppStream 2.0, now Amazon WorkSpaces Applications, streams single applications to a browser or client, with nothing installed on the user's computer.

- **A is wrong.** WorkSpaces gives each user a whole desktop, more than the job needs.
- **B is wrong.** Client VPN gives a device a network path; the program would still run on each computer.
- **D is wrong.** Lightsail rents simple servers; it doesn't stream a program.

</details>

**A9.** Dental clinics run an Amazon Connect contact center where receptionists answer every call. Now callers should be able to say "Move my appointment to Thursday" to a bot, reaching a receptionist only when it can't help. What should they add?

- A. An Amazon Lex bot, called from a Connect flow
- B. Amazon Polly, called from a Connect flow
- C. Amazon Transcribe, called from a Connect flow
- D. A second Amazon Connect instance, for the bot

<details><summary>Answer</summary>

**A is right.** Lex builds the bot that works out what the caller wants and replies; Connect, now Amazon Connect Customer, keeps the phone line, the queue and the receptionists.

- **B is wrong.** Polly turns text into speech; it understands nothing.
- **C is wrong.** Transcribe writes speech down, but doesn't work out the request or reply.
- **D is wrong.** Connect is the contact center; a second one adds no bot.

</details>

**A10.** A thermostat maker needs two things. Each thermostat must prove its identity to AWS and publish readings over MQTT, routed to other AWS services. Its web app must deploy automatically on each Git commit, with no servers to look after. Which two services fit? (Select TWO.)

- A. Amazon Lightsail
- B. AWS IoT Core
- C. Amazon Kinesis Data Streams
- D. AWS Amplify
- E. Amazon SES

<details><summary>Answer</summary>

**B and D are right.** IoT Core connects and authenticates devices and routes their MQTT messages with rules. Amplify Hosting builds and deploys every commit from Git.

- **A is wrong.** Lightsail gives the team a server to set up and deploy to.
- **C is wrong.** Kinesis streams data once it's in AWS, but doesn't connect or authenticate devices.
- **E is wrong.** SES sends email; neither part is email.

</details>

## Correction map

For each miss, reread the section, then redo the matching decision in [Simulation S12](06-sim-input-output-matcher.md).

| Question | Objective | Reread |
|---|---|---|
| A1 | 10.01a | [Ingest](01-analytics-in-five-verbs.md#ingest-data-streams-holds-records-for-your-programs-firehose-delivers-them-for-you) |
| A2 | 10.01a | [Query](01-analytics-in-five-verbs.md#query-athena-redshift-and-emr-answer-questions-in-three-different-ways), then [Catalog](01-analytics-in-five-verbs.md#catalog-glue-records-what-your-data-looks-like-and-gets-it-ready) |
| A3 | 10.01a | [Search](01-analytics-in-five-verbs.md#search-opensearch-service-finds-words-and-patterns-in-text-and-logs) |
| A4 | 10.02a | [Pictures and documents](02-ai-and-ml.md#pictures-and-documents-rekognition-sees-textract-reads) |
| A5 | 10.02a | [Sound and conversation](02-ai-and-ml.md#sound-and-conversation-transcribe-listens-polly-speaks-lex-holds-the-conversation) |
| A6 | 10.02a | [When nothing ready-made fits](02-ai-and-ml.md#when-nothing-ready-made-fits-sagemaker-ai-builds-your-own-model) |
| A7 | 10.02a | [Amazon Q, and the AI names that are closed](02-ai-and-ml.md#amazon-q-and-the-ai-names-that-are-closed) |
| A8 | 10.03a | [WorkSpaces Applications and Secure Browser](03-people-apps-and-devices.md#workspaces-applications-streams-single-apps-secure-browser-streams-one-web-browser) |
| A9 | 10.03a | [Connect and Lex](03-people-apps-and-devices.md#connect-runs-the-contact-center-lex-is-the-bot-inside-it) |
| A10 | 10.03a | [IoT Core](03-people-apps-and-devices.md#iot-core-connects-devices-and-routes-what-they-send), then [Amplify](03-people-apps-and-devices.md#amplify-builds-and-hosts-web-and-mobile-front-ends) |

## Check B: parallel retest

Take this only after the correction map, and closed-book. You pass at 8 of 10.

**B1.** A company wants its web servers' logs delivered into Amazon OpenSearch Service every minute or so, without writing any programs to move them. Which service fits?

- A. Amazon SQS
- B. Amazon Kinesis Data Streams
- C. Amazon Athena
- D. Amazon Data Firehose

<details><summary>Answer</summary>

**D is right.** Amazon Data Firehose (formerly Kinesis Data Firehose) delivers streaming data to destinations such as OpenSearch Service, S3 or Redshift. You configure it; you write no programs.

- **A is wrong.** SQS hands messages to worker programs that you would write.
- **B is wrong.** Data Streams needs consumer programs that you write to load OpenSearch Service.
- **C is wrong.** Athena queries files in S3; it doesn't move logs.

</details>

**B2.** Partners drop new folders of JSON files, sometimes with new fields, into a company's S3 data lake each week, and analysts query them with Athena. Which service finds the new folders and fields automatically and keeps the table definitions up to date, with no servers?

- A. Amazon Athena
- B. AWS Glue
- C. Amazon Redshift
- D. Amazon Quick Sight

<details><summary>Answer</summary>

**B is right.** Glue crawlers scan the data and add or update tables in the Glue Data Catalog, which Athena reads.

- **A is wrong.** Athena runs the queries; it doesn't find new folders and fields by itself.
- **C is wrong.** Redshift is a warehouse you load data into; it doesn't catalog the data lake.
- **D is wrong.** Quick Sight builds dashboards.

</details>

**B3.** A newspaper new to AWS in November 2026 wants journalists to find, within a second, every archived article that mentions a phrase, best matches first. Which service fits?

- A. Amazon Kendra
- B. Amazon Athena
- C. Amazon OpenSearch Service
- D. Amazon Quick Sight

<details><summary>Answer</summary>

**C is right.** OpenSearch Service has already indexed every word, so a search comes back at once, ranked.

- **A is wrong.** AWS closed Amazon Kendra to new customers on 2026-07-30, and the exam guide no longer lists it (checked 2026-10-24).
- **B is wrong.** Athena reads files to answer SQL questions; it doesn't rank matches.
- **D is wrong.** Quick Sight shows dashboards; it doesn't search text.

</details>

**B4.** A parking office wants the ticket number, date and reason pulled out of photos of handwritten appeal forms as separate fields, with no machine learning staff. Which service fits?

- A. Amazon Textract
- B. Amazon Rekognition
- C. Amazon SageMaker AI
- D. Amazon Translate

<details><summary>Answer</summary>

**A is right.** Textract reads documents, including handwriting, and returns form fields as a label and its value. It's ready-made.

- **B is wrong.** Rekognition can spot words in a picture, but as loose lines, not fields.
- **C is wrong.** Reading forms is covered ready-made, and the office has no one to build a model.
- **D is wrong.** Translate changes the language of text you already have.

</details>

**B5.** A bank wants each recorded complaint call turned into text, then marked positive, negative, neutral or mixed, without building any model. Which two services, used one after the other, do this? (Select TWO.)

- A. Amazon Transcribe
- B. Amazon Polly
- C. Amazon Comprehend
- D. Amazon Textract
- E. Amazon Rekognition

<details><summary>Answer</summary>

**A and C are right.** Transcribe turns the speech into text; Comprehend returns its sentiment.

- **B is wrong.** Polly runs the other way: text in, speech out.
- **D is wrong.** Textract reads scanned documents, not sound.
- **E is wrong.** Rekognition analyzes images and video, not speech.

</details>

**B6.** A recruitment agency new to AWS in November 2026 wants its data scientists to predict how many applicants each job advert will attract, from ten years of its own data. Which service should they use?

- A. Amazon Comprehend
- B. Amazon Forecast
- C. Amazon Textract
- D. Amazon SageMaker AI

<details><summary>Answer</summary>

**D is right.** No ready-made service answers the agency's own question, so its data scientists build, train and deploy a model in SageMaker AI.

- **A is wrong.** Comprehend describes an advert's text; it doesn't learn to predict applicant numbers.
- **B is wrong.** Amazon Forecast is closed to new customers (announced 2024-07-29) and isn't on the exam's list (checked 2026-10-24).
- **C is wrong.** Textract reads documents; it doesn't predict anything.

</details>

**B7.** A school district plans "Amazon Q for all our AI work." Job 1: developers want an assistant in the AWS Management Console for questions about AWS and their resources. Job 2: analysts want to train their own model of bus demand from ridership records. Which pairing fits?

- A. Amazon Q Developer for job 1, and Amazon SageMaker AI for job 2
- B. Amazon Q Business for job 1, and Amazon Q Developer for job 2
- C. Amazon Q Developer for both jobs
- D. Amazon SageMaker AI for both jobs

<details><summary>Answer</summary>

**A is right.** Q Developer helps people who build and run on AWS; building and training a model on your own data is SageMaker AI's job.

- **B is wrong.** Q Business answered questions from company documents (and is closed to new customers), and Q Developer doesn't train models.
- **C is wrong.** Q Developer is an assistant; it doesn't build a prediction model.
- **D is wrong.** SageMaker AI isn't an assistant for questions about AWS resources.

</details>

**B8.** Remote script editors each need a full Windows desktop of their own, with several programs and files kept between sessions, from personal tablets that must store no scripts. Which service fits?

- A. Amazon AppStream 2.0
- B. Amazon WorkSpaces
- C. AWS Client VPN
- D. Amazon Lightsail

<details><summary>Answer</summary>

**B is right.** WorkSpaces gives each person a whole virtual desktop in AWS that reaches the tablet only as a pixel stream, so files stay in AWS.

- **A is wrong.** AppStream 2.0, now WorkSpaces Applications, streams chosen applications, not a whole desktop of one's own.
- **C is wrong.** Client VPN gives a network path; programs and scripts would still be on the tablets.
- **D is wrong.** Lightsail rents simple servers; it doesn't give staff desktops.

</details>

**B9.** A help desk's Amazon Lex bot resets passwords in a website chat. Now callers should reach the same bot by phone, and queue for a staff member when it can't help, with no telephone hardware. Which service should it add?

- A. Amazon Polly
- B. Amazon Transcribe
- C. Amazon Connect
- D. Amazon SNS

<details><summary>Answer</summary>

**C is right.** Amazon Connect, now Amazon Connect Customer, is the cloud contact center: phone numbers, flows, queues and agents. A Connect flow can hand callers to the existing Lex bot.

- **A is wrong.** Polly turns text into speech; it gives no phone line or queue.
- **B is wrong.** Transcribe turns speech into text; it doesn't answer calls.
- **D is wrong.** SNS pushes notifications; it doesn't run phone calls.

</details>

**B10.** A parcel-locker company needs two things. Each locker must prove its identity to AWS and report door events over MQTT, routed to other AWS services. Each customer must get a styled email with a pickup code from the company's own domain. Which two services fit? (Select TWO.)

- A. Amazon SQS
- B. Amazon Connect
- C. AWS IoT Core
- D. Amazon Data Firehose
- E. Amazon SES

<details><summary>Answer</summary>

**C and E are right.** IoT Core connects and authenticates the lockers and routes their MQTT messages; Amazon SES sends transactional email, such as pickup codes, from the company's own domain.

- **A is wrong.** SQS is a queue between parts of an application, with no device identity or email.
- **B is wrong.** Connect runs a contact center for calls and chats.
- **D is wrong.** Firehose delivers streaming data once it's in AWS; it doesn't connect devices or send email.

</details>

---

"Module 10 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
