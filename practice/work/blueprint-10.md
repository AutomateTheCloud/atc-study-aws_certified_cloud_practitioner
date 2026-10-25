# Blueprint: Module 10, Data, AI and the rest of the catalog

Items file: `practice/items/10-data-ai-and-more.yaml`. Targets: about 65 questions (about 13 "Select
TWO") and 18 concept cards. Exam tasks: 3.7 (AI/ML and analytics: choose by input and output, place
services in a pipeline), the end-user computing, business application, front-end and IoT parts of
3.8, and 2.1 where a lesson has a "Your side of the line" section. No prices are tested.

The module has three objectives, one per lesson, so the table breaks each objective into the
sections that teach it. Lab 13 serves 10.01a, Lab 14 serves 10.02a, and Simulation S12 serves all
three.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

Names: choices use today's names, with the exam's name as one of the wordings where they differ
(AppStream 2.0, Amazon Connect); explanations give the old name (Kinesis Data Firehose, QuickSight,
Amazon SageMaker, AppStream 2.0, WorkSpaces Web). Closed services (Kendra, Q Business, Forecast,
Fraud Detector, Kinesis Data Analytics for SQL) appear only as wrong answers, with a dated
explanation.

## 10.01a Name the five jobs of an analytics pipeline and place each service in one [C·Ap] (lesson 10.01, task 3.7; Lab 13)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "The big picture: five verbs, from raw data to a dashboard" | Verb and service pairs; the two ingest services | Re, Un | 2 | 1 | 0 |
| 01, "Ingest: Data Streams holds records for your programs; Firehose delivers them for you" | Firehose lands a stream in S3 with no code; Data Streams for several readers and replay; Firehose's old name | Re, Ap | 3 | 0 | 0 |
| 01, "Data Streams, Firehose or SQS: what happens after the data is read" | What happens after a read, in each of the three; Kinesis Data Analytics for SQL is gone | Un | 2 | 1 | 3 |
| 01, "Catalog: Glue records what your data looks like and gets it ready" | Glue discovers, catalogs and transforms; Glue doesn't run the query; Athena reads the catalog | Un, Ap | 2 | 0 | 2 |
| 01, "Query: Athena, Redshift and EMR answer questions in three different ways" | Athena for occasional SQL on S3; Redshift for repeated, complex reports; EMR for your own Spark code; schema on read | Un, Ap | 5 | 1 | 0 |
| 01, "Search: OpenSearch Service finds words and patterns in text and logs" | Phrase search in logs; why an index is fast | Un, Ap | 2 | 0 | 0 |
| 01, "Visualize: Quick Sight turns answers into dashboards" | Quick Sight's job on top of Athena (old name in the explanation) | Ap | 1 | 0 | 1 |
| 01, "Worked example: the owner's sales dashboard" | Order of the pipeline; when the query step moves to Redshift | Un, Ap | 2 | 0 | 1 |
| 01, "Your side of the line" | What stays the customer's with managed analytics (task 2.1) | Un | 1 | 1 | 0 |
| 01, "What you pay for (as of 2026-10-24)" | Scanning less data makes Athena cheaper (no prices) | Ap | 1 | 0 | 1 |
| 04 (Lab 13), "Clean up" | Dropping an external table leaves the data in S3 | Un | 1 | 0 | 0 |
| **Total 10.01a** | | | **22** | **4** | **8** |

## 10.02a Choose an AI or ML service by what goes in and what must come out [C·Ap] (lesson 10.02, task 3.7; Lab 14; Sim S12)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "Text in: Comprehend finds meaning, Translate changes the language" | Sentiment and entities; personal data in text you send (vs Macie, card cites the warm-up); Translate vs Comprehend's language detection | Un, Ap | 3 | 0 | 1 |
| 02, "Sound and conversation: Transcribe listens, Polly speaks, Lex holds the conversation" | Transcribe; Polly; Lex intents and slots; a Lex chat bot; chaining speech services | Re, Ap | 5 | 1 | 0 |
| 02, ""Polly listens to customers" mixes up two services" | The direction of Polly and Transcribe | Un | 1 | 0 | 0 |
| 02, "Pictures and documents: Rekognition sees, Textract reads" | Rekognition for images; Textract for forms; Textract vs Rekognition; the three look-alikes | Un, Ap | 4 | 1 | 1 |
| 02, "When nothing ready-made fits, SageMaker AI builds your own model" | When to build your own (Forecast as a dated distractor); ready-made first | Un, Ap | 2 | 0 | 1 |
| 02, ""Amazon SageMaker is the ML service" uses an old name" | SageMaker AI is today's name | Re | 1 | 0 | 0 |
| 02, "Amazon Q is a family of assistants, not one product" | Q Developer in the console | Ap | 1 | 0 | 0 |
| 02, ""Amazon Q is one product" leads to wrong answers" | Q is a brand; Q Business closed | Un | 1 | 0 | 0 |
| 02, ""Kendra is the answer for searching company documents" is out of date" | Kendra closed; treat as a distractor | Un | 1 | 0 | 0 |
| 02, "Some AI names are closed or gone: recognize them, don't choose them" | Which services a new customer can use; what "closed to new customers" means | Un | 1 | 1 | 1 |
| 02, "Your side of the line" | IAM and data stay the customer's (task 2.1); the AI services opt-out policy | Re, Un | 2 | 0 | 0 |
| 05 (Lab 14), "Recap" | Synthesize once, store and replay; cheaper engines | Ap | 1 | 1 | 1 |
| 02, "Worked example: three of the owner's requests" | The order of the questions; only text needs a second one | — | 0 | 0 | 1 |
| **Total 10.02a** | | | **23** | **4** | **6** |

## 10.03a Match a need for desktops, apps, customer contact, email, a front end or devices to a service [C·Ap] (lesson 10.03, task 3.8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "WorkSpaces gives each person a whole desktop that runs in AWS" | Whole desktop for temporary staff; hourly billing with AutoStop | Un, Ap | 3 | 1 | 1 |
| 03, "WorkSpaces Applications streams single apps; Secure Browser streams one web browser" | One app for many users; Secure Browser's status; what the user sees; not Client VPN | Re, Un, Ap | 4 | 1 | 1 |
| 03, ""AppStream 2.0" and "WorkSpaces Web" are older names" | AppStream 2.0's name today | Re | 1 | 0 | 0 |
| 03, "Connect runs the contact center; Lex is the bot inside it" | Contact center; Connect with Lex; neither replaces the other | Un, Ap | 3 | 1 | 1 |
| 03, "SES sends email at scale" | Transactional and marketing email; the sandbox | Un, Ap | 2 | 0 | 0 |
| 03, "Amplify builds and hosts web and mobile front ends" | Deploys from Git and back-end features, vs Beanstalk and Lightsail | Ap | 1 | 0 | 0 |
| 03, "IoT Core connects devices and routes what they send" | Connecting sensors; rules route data; Device Shadow | Un, Ap | 3 | 0 | 1 |
| 03, "Your side of the line" | What stays the customer's (task 2.1) | Un | 1 | 1 | 0 |
| 03, "Worked example: finishing the owner's requests" | Who is on the other end | Ap | 1 | 1 | 0 |
| **Total 10.03a** | | | **19** | **5** | **4** |

## Totals

64 questions (51 single, 13 "Select TWO"); 18 concept cards.

By page: 01 21, 02 22, 03 19, 04 (Lab 13) 1, 05 (Lab 14) 1; no question cites 06 (Sim S12),
whose decisions repeat the lessons' material. By task: 3.7 42, 3.8 18, 2.1 4.

Question levels: 7 recall (11%), 26 understanding (41%), 31 application (48%). This leans further
toward application than the 20/50/30 target, on purpose: all three objectives are "choose a service
for a need" [C·Ap], and recall of names and definitions is carried by the glossary's term cards.
Correct single answers sit A 13, B 14, C 12, D 12; the correct choice is the longest in 19 of 51.

Similarity: every question, in every wording, scores PASS (192 of 192). Three items needed rewrites
along the way (q10-quick-sight-charity-board, q10-rekognition-listing-photos,
q10-ses-sandbox-verified-only, all "same services + same correct answer"); each got a new scenario
and choice set, and the Quick Sight item became a "what job does it do" question.

Cards avoid what the module's glossary entries already hold (definitions, old names, Kendra's and
Q Business's status, replay); they carry rules, choices and "why" instead.

Left out on purpose: prices and free allowances of every kind (Athena per TB, Polly per character,
WorkSpaces bundles, Q Developer Pro); retention numbers for Data Streams, SQS and Firehose (the
guide says to learn the pattern); Amazon Bedrock (out of the exam's scope) except as a distractor;
Kiro; Lex V1's end of support; Polly's engine names; Lab 13's 10 MB minimum.
