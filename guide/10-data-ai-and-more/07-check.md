---
type: check
id: clf-10-07
title: "Module 10 mastery check"
tasks: ["3.7", "3.8"]
objectives: ["10.01a", "10.02a", "10.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished lessons 10.01 to 10.03; about 20 minutes for each check"
prerequisites: [clf-10-01, clf-10-02, clf-10-03]
pillars: [performance-efficiency, cost-optimization, security]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html"
  - "https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html"
  - "https://docs.aws.amazon.com/athena/latest/ug/what-is.html"
  - "https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html"
  - "https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/textract/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"
  - "https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-availability-change.html"
  - "https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html"
  - "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html"
  - "https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html"
  - "https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html"
  - "https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html"
---

# Module 10 mastery check: match each need to the data, AI or end-user service built for it

Ten questions test whether you can place an analytics service on its job, choose an AI service by what goes in and what comes out, and match a need from people, apps or devices to its service. A second set of ten, on the same objectives, is there if you need a retest.

**For:** an adult studying alone, possibly new to IT, who has finished lessons [10.01](01-analytics-in-five-verbs.md), [10.02](02-ai-and-ml.md) and [10.03](03-people-apps-and-devices.md). **Time:** about 20 minutes for each check. No AWS account is needed.

## How to use this check

Take Check A closed-book, in one sitting, and write down your answers before you open any feedback. The threshold is 80%: 8 of the 10 questions. A "(Select TWO.)" question counts only if both of your choices are right. If you score below 8, use the correction map to reread the section behind each miss and redo its lab or simulation, then take Check B, the parallel retest. If you score 8 or more, go on to the enrichment tasks.

Service names and status are as of 2026-10-24. Where the exam guide uses an older name, the options use the exam's name and the feedback gives today's.

## Check A

**A1.** A photo-printing website takes orders all day. Each order should go to just one of its worker programs, whichever is free, and be removed from the waiting list once it's printed, so that the other workers don't pick it up. Which service should hold the orders while they wait?

- A. Amazon Kinesis Data Streams
- B. Amazon SNS
- C. Amazon SQS
- D. Amazon Data Firehose

<details><summary>Answer</summary>

**C is right.** Amazon SQS is a message queue: a free worker takes a message, does the job, and deletes the message, so the other workers don't handle it. (In real work, a worker should also cope with the rare message delivered twice.)

- **A is wrong.** Records in Kinesis Data Streams stay after they're read, and every consumer program can read every record. That suits several programs reading the same live data, and replay, not handing each job to one worker.
- **B is wrong.** Amazon SNS pushes each message to every subscriber (Module 08), so every worker would get every order.
- **D is wrong.** Amazon Data Firehose (formerly Kinesis Data Firehose) delivers streaming data to a store such as S3. No worker program takes jobs from it.

</details>

**A2.** A group of clinics runs a nightly AWS Glue job that cleans its appointment records and writes them to Amazon S3 as Parquet files, and a Glue crawler has added the files to the Data Catalog as a table. An analyst now wants to ask, in SQL, "What was the average wait time at each clinic last month?" She doesn't want to load the data anywhere or set up anything to run it on. Which service should she use to run the question?

- A. AWS Glue
- B. Amazon Athena
- C. Amazon Quick Sight
- D. Amazon OpenSearch Service

<details><summary>Answer</summary>

**B is right.** Athena runs standard SQL on files in S3 where they sit. It reads the table definition from the Glue Data Catalog, it's serverless, and it charges for each query.

- **A is wrong.** Glue found, described and cleaned the data, but it doesn't answer questions about it. "Glue now holds the table" is the trap: the catalog holds a description; a query service reads it.
- **C is wrong.** Quick Sight shows results as dashboards, and it can read from Athena. It's the visualize step, not the place the SQL runs on the files.
- **D is wrong.** OpenSearch Service searches text and logs that it has indexed. The files would have to be loaded into a domain first, and a SQL total is a query job, not a search.

</details>

**A3.** A hardware store's website needs a search box. When a visitor types "cordless drill 18V", the site should return matching products from its tens of thousands of product descriptions within a moment, best matches first. Which service is built for this?

- A. Amazon OpenSearch Service
- B. Amazon Athena
- C. Amazon Quick Sight
- D. Amazon Redshift

<details><summary>Answer</summary>

**A is right.** OpenSearch Service keeps a search index of every word, so it finds matches at once and ranks them. Website search is one of its main uses.

- **B is wrong.** Athena answers a SQL question by reading files in S3. It doesn't keep a word index or rank matches, so it's slow for a search box.
- **C is wrong.** Quick Sight builds dashboards for people in the business; it doesn't search product text.
- **D is wrong.** Redshift is a warehouse for heavy, repeated reports, not for finding words in text.

</details>

**A4.** A national park's trail cameras take thousands of photos a week. Rangers want each photo labeled with what it shows, such as deer, a person or a vehicle, so they can find the photos with people in closed areas. The park has no machine learning staff. Which service fits?

- A. Amazon Macie
- B. Amazon SageMaker AI
- C. Amazon Textract
- D. Amazon Rekognition

<details><summary>Answer</summary>

**D is right.** Rekognition is a ready-made service for images and video: it returns the objects and scenes it finds in each photo, with no machine learning skills needed.

- **A is wrong.** Macie finds sensitive data, such as card numbers, in S3 buckets (Module 09). It doesn't say what a photo shows.
- **B is wrong.** SageMaker AI is for building and training your own model when nothing ready-made fits. Labeling objects in photos is covered, and the park has no one to build a model.
- **C is wrong.** Textract reads documents: text, form fields and tables. It doesn't describe animals or people in a scene.

</details>

**A5.** A history museum is adding an audio guide. Curators write each exhibit's description in English only. Visitors must be able to choose English or German and hear the description spoken in a natural voice. Which two services does the museum need? (Select TWO.)

- A. Amazon Transcribe
- B. Amazon Translate
- C. Amazon Lex
- D. Amazon Polly
- E. Amazon Comprehend

<details><summary>Answer</summary>

**B and D are right.** Translate turns the English text into German text. Polly turns text into speech, so it reads both versions aloud.

- **A is wrong.** Transcribe runs the other way: speech in, text out. Nothing here starts as speech.
- **C is wrong.** Lex builds bots that hold a conversation. Visitors listen; they don't talk to the guide.
- **E is wrong.** Comprehend describes text (sentiment, entities, language), but it doesn't change the language or speak.

</details>

**A6.** An online electronics shop that is new to AWS in 2026 wants its data scientists to build a model that scores each new order for fraud risk. The model must learn from the shop's own history of past orders and chargebacks. Which service should they use?

- A. Amazon SageMaker AI
- B. Amazon Fraud Detector
- C. Amazon Macie
- D. Amazon Comprehend

<details><summary>Answer</summary>

**A is right.** SageMaker AI (formerly Amazon SageMaker) is where data scientists build, train and deploy their own model on their own data. It's also where AWS points new customers who would once have used Fraud Detector.

- **B is wrong.** Amazon Fraud Detector has been closed to new customers since 2025-11-07, and it's out of the exam's scope (checked 2026-10-24). The name fits so well that it's tempting.
- **C is wrong.** Macie finds sensitive data, such as card numbers, in S3 buckets (Module 09). It doesn't predict fraud.
- **D is wrong.** Comprehend finds meaning in text. It doesn't learn patterns from a shop's order history.

</details>

**A7.** A shop owner reads that "Amazon Q" is AWS's AI assistant, and wants it for two jobs. Job 1: her developer wants help, in the AWS Management Console, understanding why one of the shop's AWS resources failed to deploy. Job 2: her customers want a chat window on the shop's website that takes return requests and asks for the order number. Which pairing fits?

- A. Amazon Q Business for job 1, and Amazon Q Developer for job 2
- B. Amazon Q Developer for both jobs
- C. Amazon Lex for both jobs
- D. Amazon Q Developer for job 1, and Amazon Lex for job 2

<details><summary>Answer</summary>

**D is right.** "Amazon Q" is a family, not one product. Amazon Q Developer helps people who build and run on AWS, including in the console. A bot that talks to your customers, works out what they want and collects details such as an order number is built with Amazon Lex.

- **A is wrong.** Amazon Q Business answered employees' questions from company documents (and is closed to new customers); it doesn't help with AWS resources. Q Developer doesn't become a customer chatbot.
- **B is wrong.** Q Developer fits job 1 only. It helps the shop's builders, not its customers.
- **C is wrong.** Lex fits job 2 only. It builds bots for your own customers; it doesn't explain your AWS resources to your developer.

</details>

**A8.** A design agency hires freelance illustrators for short projects. Each one needs only the agency's licensed Windows drawing program, opened from the freelancer's own computer. No copy may be installed on those computers, the agency decides which version everyone runs, and a whole desktop for each freelancer would be wasted. Which service fits?

- A. Amazon WorkSpaces
- B. AWS Client VPN
- C. Amazon AppStream 2.0
- D. Amazon Lightsail

<details><summary>Answer</summary>

**C is right.** Amazon AppStream 2.0, now called Amazon WorkSpaces Applications, streams single desktop applications from AWS to a browser or client. Users always get the version you installed, and the program isn't installed on their computers.

- **A is wrong.** WorkSpaces gives each user a whole desktop. The freelancers need one program, so that's more than the job needs.
- **B is wrong.** Client VPN gives a device a network path into a VPC. The program would still have to be installed and run on each computer.
- **D is wrong.** Lightsail rents a simple server at a fixed monthly price, for websites and small applications. It doesn't stream a program to each freelancer.

</details>

**A9.** A group of dental clinics already runs an Amazon Connect contact center, where receptionists answer every call from a queue. Now it wants callers to be able to say "Move my appointment to Thursday" and have a bot understand them, collect the details, and pass the call to a receptionist only when the bot can't help. What should it add?

- A. An Amazon Lex bot, called from a Connect flow
- B. Amazon Polly, called from a Connect flow
- C. Amazon Transcribe, called from a Connect flow
- D. A second Amazon Connect instance, for the bot

<details><summary>Answer</summary>

**A is right.** Lex builds the bot: it works out what the caller wants (the intent), asks for missing details (the slots) and replies. A Connect flow can hand the caller to the Lex bot and back to the queue. Connect, now called Amazon Connect Customer, keeps the phone line, the queue and the receptionists.

- **B is wrong.** Polly turns text into speech. It can give a voice to words, but it understands nothing the caller says.
- **C is wrong.** Transcribe writes speech down as text, but it doesn't work out the request, collect details or reply.
- **D is wrong.** Connect is the contact center. A second one adds another phone system, not a bot that understands requests.

</details>

**A10.** A company that makes smart thermostats is planning two parts of its product. Its thermostats must each prove their identity to AWS and publish their readings over MQTT, with the readings routed to other AWS services. Its web app for owners must be built and deployed automatically each time a developer commits code to the Git repository, with no servers for the team to look after. Which two services fit? (Select TWO.)

- A. Amazon Lightsail
- B. AWS IoT Core
- C. Amazon Kinesis Data Streams
- D. AWS Amplify
- E. Amazon SES

<details><summary>Answer</summary>

**B and D are right.** AWS IoT Core connects devices, checks each one's identity (usually with a certificate), takes their MQTT messages and routes them with rules. AWS Amplify, through Amplify Hosting, builds and deploys every commit from a Git repository and hosts the result.

- **A is wrong.** Lightsail rents a simple server at a fixed monthly price. The team would have to set it up, update it and deploy to it.
- **C is wrong.** Kinesis Data Streams handles streaming data once it's in AWS, but it doesn't connect or authenticate devices.
- **E is wrong.** Amazon SES sends and receives email. Neither part of the product is email.

</details>

## Correction map

For each question you missed, reread the section, then redo the practice next to it before you take Check B.

| Question | Objective | Reread | Then practice |
|---|---|---|---|
| A1 | 10.01a | [Data Streams, Firehose or SQS: what happens after the data is read](01-analytics-in-five-verbs.md#data-streams-firehose-or-sqs-what-happens-after-the-data-is-read) | The lesson's practice question 2; [Simulation S12](06-sim-input-output-matcher.md) |
| A2 | 10.01a | [Query: Athena, Redshift and EMR answer questions in three different ways](01-analytics-in-five-verbs.md#query-athena-redshift-and-emr-answer-questions-in-three-different-ways), then [Catalog: Glue records what your data looks like and gets it ready](01-analytics-in-five-verbs.md#catalog-glue-records-what-your-data-looks-like-and-gets-it-ready) | [Lab 13: query a small sales file in S3 with Athena](04-lab-13-athena-query.md) |
| A3 | 10.01a | [Search: OpenSearch Service finds words and patterns in text and logs](01-analytics-in-five-verbs.md#search-opensearch-service-finds-words-and-patterns-in-text-and-logs) | The section's "Your turn"; [Simulation S12](06-sim-input-output-matcher.md), Decision 2 |
| A4 | 10.02a | [Pictures and documents: Rekognition sees, Textract reads](02-ai-and-ml.md#pictures-and-documents-rekognition-sees-textract-reads) | [Simulation S12](06-sim-input-output-matcher.md), Decision 1 |
| A5 | 10.02a | [Sound and conversation: Transcribe listens, Polly speaks, Lex holds the conversation](02-ai-and-ml.md#sound-and-conversation-transcribe-listens-polly-speaks-lex-holds-the-conversation) | [Lab 14: have Amazon Polly read a product description aloud](05-lab-14-polly-text-to-speech.md); [Simulation S12](06-sim-input-output-matcher.md), Decision 1 |
| A6 | 10.02a | [When nothing ready-made fits, SageMaker AI builds your own model](02-ai-and-ml.md#when-nothing-ready-made-fits-sagemaker-ai-builds-your-own-model), then [Some AI names are closed or gone](02-ai-and-ml.md#some-ai-names-are-closed-or-gone-recognize-them-dont-choose-them) | [Simulation S12](06-sim-input-output-matcher.md), Decision 6 |
| A7 | 10.02a | [Amazon Q is a family of assistants, not one product](02-ai-and-ml.md#amazon-q-is-a-family-of-assistants-not-one-product) | [Simulation S12](06-sim-input-output-matcher.md), Decision 5 |
| A8 | 10.03a | [WorkSpaces Applications streams single apps; Secure Browser streams one web browser](03-people-apps-and-devices.md#workspaces-applications-streams-single-apps-secure-browser-streams-one-web-browser) | [Simulation S12](06-sim-input-output-matcher.md), Decision 3 |
| A9 | 10.03a | [Connect runs the contact center; Lex is the bot inside it](03-people-apps-and-devices.md#connect-runs-the-contact-center-lex-is-the-bot-inside-it) | [Simulation S12](06-sim-input-output-matcher.md), Decision 2 (request 2) |
| A10 | 10.03a | [IoT Core connects devices and routes what they send](03-people-apps-and-devices.md#iot-core-connects-devices-and-routes-what-they-send), then [Amplify builds and hosts web and mobile front ends](03-people-apps-and-devices.md#amplify-builds-and-hosts-web-and-mobile-front-ends) | [Simulation S12](06-sim-input-output-matcher.md), Decision 2 (request 6) |

When you reread, try the method the lessons use instead of memorizing names: for analytics, name the verb first (ingest, catalog, query, search, visualize); for AI, say what goes in and what must come out; for people and devices, say who is on the other end.

## Check B: parallel retest

Take this only after the correction map, and closed-book. The threshold is the same: 8 of 10.

**B1.** A web-hosting company wants the access logs from its web servers delivered into its Amazon OpenSearch Service domain in batches every minute or so, so that support staff can search them. It doesn't want to write or run any programs to move the logs. Which service fits?

- A. Amazon SQS
- B. Amazon Kinesis Data Streams
- C. Amazon Athena
- D. Amazon Data Firehose

<details><summary>Answer</summary>

**D is right.** Amazon Data Firehose (formerly Kinesis Data Firehose) gathers streaming data until a size or time limit is reached, then delivers it to a destination such as OpenSearch Service, S3 or Redshift. You configure it; you write no programs.

- **A is wrong.** SQS hands messages to worker programs, which you would write, and it delivers nothing to OpenSearch Service on its own.
- **B is wrong.** Data Streams holds records for consumer programs that you write and run. Something would still have to read the stream and load OpenSearch Service.
- **C is wrong.** Athena queries files in S3; it doesn't move logs anywhere.

</details>

**B2.** A travel company's partners drop new folders of JSON booking files into its S3 data lake every week, and they sometimes add new fields. The analysts query the files with Amazon Athena. The company wants the new folders and fields found automatically and the table definitions kept up to date, with no servers to run. Which service does this?

- A. Amazon Athena
- B. AWS Glue
- C. Amazon Redshift
- D. Amazon Quick Sight

<details><summary>Answer</summary>

**B is right.** Glue crawlers scan the data, work out its columns, and add or update the tables in the Glue Data Catalog, which Athena reads. Glue is serverless.

- **A is wrong.** Athena runs the queries and reads its table definitions from a catalog. You can type a table definition in Athena by hand, but it doesn't find new folders and fields by itself.
- **C is wrong.** Redshift is a warehouse that you load data into. It doesn't keep the data lake's catalog up to date.
- **D is wrong.** Quick Sight builds dashboards from query results; it doesn't describe the files.

</details>

**B3.** A newspaper that opens its first AWS account in November 2026 wants its journalists to find, within a second, every archived article that mentions a given name or phrase, best matches first. Which service fits?

- A. Amazon Kendra
- B. Amazon Athena
- C. Amazon OpenSearch Service
- D. Amazon Quick Sight

<details><summary>Answer</summary>

**C is right.** OpenSearch Service has already indexed every word, so a search for a name or phrase comes back at once, with the best matches ranked first.

- **A is wrong.** Older material offers Amazon Kendra for "intelligent search" of documents. AWS closed it to new customers on 2026-07-30, and the 2026 exam guide no longer lists it (checked 2026-10-24). Treat it as a distractor.
- **B is wrong.** Athena reads files to answer a SQL question. It has no word index and doesn't rank matches, so it's slower and more work for this.
- **D is wrong.** Quick Sight shows results as dashboards; it doesn't search the text of articles.

</details>

**B4.** A city's parking office receives photos of appeal forms that drivers fill in by hand. It wants the ticket number, the date and the driver's reason pulled out of each form as separate fields, ready for clerks to search. It has no machine learning staff. Which service fits?

- A. Amazon Textract
- B. Amazon Rekognition
- C. Amazon SageMaker AI
- D. Amazon Translate

<details><summary>Answer</summary>

**A is right.** Textract reads documents, including handwriting, and returns their structure: form fields as a label and its value, and tables. It's ready-made, so no one has to train a model.

- **B is wrong.** Rekognition can spot words in a picture, but it returns them as loose lines, not as a form's fields.
- **C is wrong.** SageMaker AI is for building your own model when nothing ready-made fits. Reading forms is covered, and the office has no one to build a model.
- **D is wrong.** Translate changes the language of text you already have. It can't read a photo of a form.

</details>

**B5.** A bank's complaints line records every call. The quality team wants each recording turned into text, and then each call marked as positive, negative, neutral or mixed, without building any model. Which two services, used one after the other, do this? (Select TWO.)

- A. Amazon Transcribe
- B. Amazon Polly
- C. Amazon Comprehend
- D. Amazon Textract
- E. Amazon Rekognition

<details><summary>Answer</summary>

**A and C are right.** Transcribe turns the recorded speech into text. Comprehend then reads the text and returns its sentiment.

- **B is wrong.** Polly runs the other way: text in, speech out. "Polly listens" is a common mix-up.
- **D is wrong.** Textract reads scanned documents, not sound.
- **E is wrong.** Rekognition analyzes what's seen in images and video, not what's said.

</details>

**B6.** A recruitment agency that opens its first AWS account in November 2026 wants to predict how many applicants each new job advert will attract, from its own ten years of adverts and responses. Its own data scientists will do the machine learning work. Which service should they use?

- A. Amazon Comprehend
- B. Amazon Forecast
- C. Amazon Textract
- D. Amazon SageMaker AI

<details><summary>Answer</summary>

**D is right.** No ready-made service answers the agency's own question, so its data scientists build, train and deploy a model on its own data in SageMaker AI (formerly Amazon SageMaker).

- **A is wrong.** Comprehend can tell you the sentiment or entities in an advert's text, but it doesn't learn to predict applicant numbers from the agency's history.
- **B is wrong.** Amazon Forecast made time-series forecasts, not a prediction for each advert. It's also closed to new customers (announced 2024-07-29), so the agency can't sign up, and it isn't on the exam's list (checked 2026-10-24).
- **C is wrong.** Textract reads documents; it doesn't predict anything.

</details>

**B7.** A school district's IT lead says, "We'll use Amazon Q for all our AI work." She has two jobs. Job 1: the district's developers want an assistant in the AWS Management Console that answers questions about AWS services and their own resources. Job 2: the district's analysts want to build and train their own model that predicts how many buses each route needs each morning, from the district's own ridership records. Which pairing fits?

- A. Amazon Q Developer for job 1, and Amazon SageMaker AI for job 2
- B. Amazon Q Business for job 1, and Amazon Q Developer for job 2
- C. Amazon Q Developer for both jobs
- D. Amazon SageMaker AI for both jobs

<details><summary>Answer</summary>

**A is right.** "Amazon Q" is a family, not one product. Amazon Q Developer helps people who build and run on AWS, in the console. Building and training a model on your own data is SageMaker AI's job.

- **B is wrong.** Amazon Q Business answered questions from company documents (and is closed to new customers); it isn't the console assistant. Q Developer doesn't train models.
- **C is wrong.** Q Developer fits job 1 only. It's an assistant; it doesn't build and host a prediction model on the district's data.
- **D is wrong.** SageMaker AI fits job 2 only. It builds models; it isn't an assistant for questions about AWS resources.

</details>

**B8.** A TV production company hires remote script editors for one series. Each needs a full Windows desktop of their own, with several writing and editing programs and their files kept between sessions. They work from their personal tablets, and no scripts may be stored on the tablets. Which service fits?

- A. Amazon AppStream 2.0
- B. Amazon WorkSpaces
- C. AWS Client VPN
- D. Amazon Lightsail

<details><summary>Answer</summary>

**B is right.** WorkSpaces gives each person a whole virtual desktop that runs in AWS and reaches the tablet only as a pixel stream, so files stay in AWS. There are clients for tablets.

- **A is wrong.** AppStream 2.0, now called Amazon WorkSpaces Applications, streams one or a few chosen applications. The editors need a whole desktop of their own, with files kept.
- **C is wrong.** Client VPN gives a device a network path into a VPC. The programs and scripts would still have to run on the tablets.
- **D is wrong.** Lightsail rents simple servers for websites; it doesn't give staff desktops.

</details>

**B9.** A university's IT help desk has built an Amazon Lex bot that resets students' passwords in a website chat window. Now it wants students who phone the help desk to reach the same bot, and to wait in a queue for a staff member when the bot can't help. It wants no telephone hardware. Which service should it add?

- A. Amazon Polly
- B. Amazon Transcribe
- C. Amazon Connect
- D. Amazon SNS

<details><summary>Answer</summary>

**C is right.** Amazon Connect, now called Amazon Connect Customer, is the cloud contact center: phone numbers, flows, queues and the staff who answer. A Connect flow can hand a caller to the existing Lex bot and pass them to a person when it can't help.

- **A is wrong.** Polly turns text into speech. It gives no phone number, queue or agents.
- **B is wrong.** Transcribe turns speech into text. It doesn't answer calls or queue callers.
- **D is wrong.** SNS pushes short notifications to subscribers (Module 08). It doesn't run phone calls.

</details>

**B10.** A company that rents parcel lockers is planning two parts of its service. Each locker must prove its identity to AWS and report door events over MQTT, and the company's app must be able to read each locker's last reported state even while a locker is briefly offline. Each customer must also get a styled email with a pickup code, sent from the company's own domain. Which two services fit? (Select TWO.)

- A. Amazon SQS
- B. Amazon Connect
- C. AWS IoT Core
- D. Amazon Data Firehose
- E. Amazon SES

<details><summary>Answer</summary>

**C and E are right.** AWS IoT Core connects and authenticates the lockers, takes their MQTT messages, and keeps a Device Shadow, the stored copy of each device's last reported state, that the app can read while a locker is offline. Amazon SES sends transactional email, such as pickup codes, from the company's own domain.

- **A is wrong.** SQS is a queue between parts of an application. It has no device identity, MQTT or shadows, and it doesn't send email.
- **B is wrong.** Connect (Connect Customer) runs a contact center for calls and chats; it isn't for sending email at scale or connecting devices.
- **D is wrong.** Firehose delivers streaming data to stores such as S3 once it's in AWS. It doesn't connect devices or send email.

</details>

## Enrichment

For learners who reached 8 or more on Check A. Each task has no single right answer; compare yours with the model answer.

**Task 1: defend the query step.** The bakery from the [module brief](00-brief.md) now has eight shops. The owner's morning dashboard reads from Athena, and a consultant says, "Move everything to Redshift now; it's the proper analytics database." In four or five sentences, say what you would check before agreeing, and what would make you agree. Link your answer to [PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html).

<details><summary>Model answer</summary>

Check the shape of the questions, not the size of the business. Athena fits files in S3 and occasional questions, and it charges for each query, by the data it scans. Redshift fits regular, complex reports that join many large tables from many sources, run again and again. So I'd ask: how many sources feed the dashboard now, how often do the same heavy reports run, and are queries getting slow or costly even after the files are in Parquet and partitioned? If the finance team now joins several systems' data in the same reports every morning, that's the warehouse case, and I'd agree, keeping Quick Sight on top and Athena for one-off questions on the data lake. PERF03-BP01 asks for the store that fits the access pattern, which is the same test.

</details>

**Task 2: a real-world complication on the phone line.** The bakery's phone bot (Connect Customer with a Lex bot) works. Now the owner wants every call recorded and turned into text so she can review complaints, and some callers read out their card numbers. List the services involved and three things that stay the bakery's job under the shared responsibility model. Link your answer to [SEC07-BP02 Apply data protection controls based on data sensitivity](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html).

<details><summary>Model answer</summary>

Connect Customer records the calls; Amazon Transcribe turns the recordings into text, and it can remove personal data from transcripts; Amazon Comprehend can mark complaints by sentiment and can also spot personal data in the text. Three jobs stay the bakery's: deciding how long recordings are kept and who may hear them (a Connect setting); keeping recordings and transcripts in private, encrypted S3 buckets with narrow IAM access; and choosing to remove card numbers before anyone reads the text, then checking the results, because a model can miss one. SEC07-BP02 says data this sensitive gets stronger controls than, say, cake descriptions.

</details>

**Task 3: pay for desktops only while you need them.** The bakery will give WorkSpaces to six seasonal staff who each work about 12 hours a week for six weeks, and to its accountant, who works on hers full time all year. A manager suggests Amazon WorkSpaces Secure Browser for the seasonal staff instead, "because it's cheaper". Write a short recommendation for each group, and say why Secure Browser isn't the plan. Link your answer to [COST07-BP01 Perform pricing model analysis](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_analysis.html).

<details><summary>Model answer</summary>

Seasonal staff: WorkSpaces with hourly billing and AutoStop, so they pay a low monthly fee plus the hours they run, and the desktops are removed in January. The accountant: monthly billing, since full-time hours are likely past the break-even point; check the real break-even for the bundle and Region in the AWS Pricing Calculator. Secure Browser gives only a web browser, and the staff need the ordering and stock systems and other desktop programs. It also closes to new customers on 2026-10-29, and the bakery isn't a customer yet. COST07-BP01 is exactly this choice: compare the billing models against the expected hours before you commit.

</details>

---

"Module 10 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
