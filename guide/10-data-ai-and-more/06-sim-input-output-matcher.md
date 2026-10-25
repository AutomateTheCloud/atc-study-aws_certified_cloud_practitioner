---
type: sim
id: clf-10-06
title: "Simulation S12: Match each request to a service by what goes in and what comes out"
tasks: ["3.7", "3.8"]
objectives: ["10.01a", "10.02a", "10.03a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 10.01 to 10.03; about 30 minutes"
prerequisites: ["clf-10-01", "clf-10-02", "clf-10-03"]
terms_introduced: []
pillars: [performance-efficiency, cost-optimization]
lab: "S12"
rung: L2-L3
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "30 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/textract/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/polly/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/translate/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"
  - "https://docs.aws.amazon.com/quick/latest/userguide/what-is.html"
  - "https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html"
  - "https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html"
  - "https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html"
  - "https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html"
  - "https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html"
  - "https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html"
  - "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html"
  - "https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html"
---

# Simulation S12: Match the owner's six requests to services by what goes in and what comes out

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [10.01 Analytics in five verbs](01-analytics-in-five-verbs.md), [10.02 AI and machine learning](02-ai-and-ml.md) and [10.03 People, apps and devices](03-people-apps-and-devices.md). **Time:** about 30 minutes. **Cost:** $0; no AWS account is used.

**Why a simulation:** on our Free plan test account on 2026-10-23, Amazon Comprehend opened a page about Free plan limits with an **Upgrade plan** button instead of its console. Several other services here bill by the user, the hour or the month, such as Amazon WorkSpaces desktops. Choosing the service is the skill the exam tests, and that needs no account.

**Goal:** finish an input-to-output grid, then match each of the bakery owner's six requests to a service and name the likeliest wrong pick. **End state:** a filled grid, six matches and four follow-up answers in your notes.

**Why this matters:** each match hands a hard problem (speech, vision, desktops, device fleets) to a service AWS runs. That is the design principle "[Democratize advanced technologies](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html)": build only what no ready-made service does.

## The rules of this simulation

Match by two questions, in this order, before you think about names.

```mermaid
flowchart TD
  accTitle: How to match a request to a service
  accDescr: First name what goes in. Then name what must come out. If a ready-made service turns that input into that output, use it, and name the service you are ruling out. If none does, or the answer must be learned from your own data, build a model with SageMaker AI.
  A["1. What goes in?<br/>text, speech, images, documents,<br/>files, device readings, people"] --> B["2. What must come out?"]
  B --> C{"Does a ready-made<br/>service do exactly this?"}
  C -->|"yes"| D["Use it, and name the<br/>service you rule out"]
  C -->|"no, or it must learn<br/>from our own data"| E["Build and train a model<br/>with Amazon SageMaker AI"]
```

*Notice that SageMaker AI is the last branch, not the first: it's for when nothing ready-made fits.*

**Long description.** Top to bottom: (1) what goes in: text, speech, images, documents, files, device readings or people; (2) what must come out. A decision: does a ready-made service do exactly this? Yes: use it, and name the service you rule out. No, or the answer must be learned from your own data: build and train a model with Amazon SageMaker AI (formerly Amazon SageMaker).

Service names and status are as of 2026-10-24.

## Part 1: finish the grid

### Decision 1: fill the five blanks

| Input | Output wanted | Service |
|---|---|---|
| Text | Spoken audio | Amazon Polly |
| Spoken audio | Written text | 1 ____ |
| English text | The same text in Spanish | 2 ____ |
| Text you already have | Its sentiment, key phrases, names of people and places | 3 ____ |
| A scanned form or a photo of a receipt | The text, plus fields and tables | Amazon Textract |
| Images or video | Objects, faces, unsafe content | 4 ____ |
| A typed or spoken conversation | A bot that understands the request and replies | 5 ____ |

<details><summary>Model answer</summary>

1. **Amazon Transcribe**, speech to text: the reverse of Polly.
2. **Amazon Translate**. Comprehend can detect which language a text is in, but it doesn't translate.
3. **Amazon Comprehend**. It reads meaning in text you already have; it doesn't pull text out of a picture.
4. **Amazon Rekognition**. It can find text in an image, but not a document's fields and tables: that's Textract.
5. **Amazon Lex**. Polly can give the bot a voice, but it understands nothing.

The pairs to keep apart: **Polly and Transcribe** run in opposite directions. **Textract, Comprehend and Rekognition** all "look at" content: Textract extracts a document's text and structure, Comprehend interprets text, and Rekognition interprets images and video.

</details>

## Part 2: the owner's six requests

### Decision 2: for each request, name the input, the output, the service, and one service you'd rule out

These are the owner's requests from the [module brief](00-brief.md):

| # | The owner says |
|---|---|
| 1 | "One screen each morning with sales by day, by cake and by shop, and which cake pages people look at before they order." |
| 2 | "When the shop is busy, a bot should answer the phone and take simple orders." |
| 3 | "Read each cake's description aloud on the website, for customers who would rather listen." |
| 4 | "Turn the suppliers' paper receipts into text the accountant can search." |
| 5 | "Give December's temporary staff a work desktop they can reach from their own laptops, and take it away in January." |
| 6 | "The freezers have temperature sensors. Collect their readings and warn us before the dough thaws." |

<details><summary>Model answer</summary>

![Six cards. 1, sales dashboard: Amazon Quick Sight, not Athena alone. 2, phone bot: Amazon Lex on a phone line from Amazon Connect Customer, not Polly alone. 3, spoken descriptions: Amazon Polly, not Transcribe. 4, receipts: Amazon Textract, not Rekognition. 5, seasonal desktops: Amazon WorkSpaces, not buying PCs, or WorkSpaces Applications if staff need one app only. 6, freezer sensors: AWS IoT Core, not Kinesis alone.](../../images/10-06-six-requests.svg)

*Notice that only three of the six are AI services. The others come from analytics, end-user computing, business applications and IoT, which is why the method starts from input and output, not from a category.*

**Long description.** Six cards, 1 to 6, each giving the input, the output wanted, the service and the likeliest wrong pick. The list below gives each card's content and the reasons.

- **1: Amazon Quick Sight** (formerly Amazon QuickSight), part of Amazon Quick, draws the screen; Athena, from [Lab 13](04-lab-13-athena-query.md), answers the queries underneath, and page views can arrive through Amazon Data Firehose (formerly Kinesis Data Firehose). Athena alone gives tables, not a screen people read.
- **2: Amazon Lex** builds the bot that understands "Can I order two lemon tarts for Saturday?". The phone number and call routing come from **Amazon Connect (now Amazon Connect Customer)**, the cloud contact center, which can hand callers to a Lex bot. Lex and Connect are a pair, not rivals.
- **3: Amazon Polly**, as in [Lab 14](05-lab-14-polly-text-to-speech.md). Transcribe does the reverse.
- **4: Amazon Textract**, which has a feature for invoices and receipts. Rekognition finds words in a photo but not "supplier", "date" and "total"; Comprehend needs the text to exist already.
- **5: Amazon WorkSpaces**, a whole virtual desktop per person, billed by the hour or the month with no long-term commitment, and removed when the staff leave. Buying laptops for six weeks is the wrong pick; if the staff need one app only, see Decision 3.
- **6: AWS IoT Core** connects the sensors securely and routes their readings, for example to an alert before the dough thaws. Kinesis streams data once it's in AWS, but it doesn't connect or manage devices.

</details>

### Decision 3: "The temporary staff only use our ordering app, not a whole desktop. And could they just use a secure browser?"

<details><summary>Model answer</summary>

For one app, **Amazon AppStream 2.0 (now Amazon WorkSpaces Applications)** streams just that application to any device, so nobody gets a desktop they don't need. **Amazon WorkSpaces Secure Browser** (formerly WorkSpaces Web) gives a hosted, isolated browser for web apps, but it closes to new customers on 2026-10-29, and the bakery isn't a customer yet ([availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html)). Learn what it does for the exam; don't plan new work on it.

</details>

### Decision 4: "Can the receipts service also tell me which suppliers sound annoyed in their emails?"

<details><summary>Model answer</summary>

No. Textract extracts text; judging tone is **Amazon Comprehend**'s sentiment analysis, on email text you already have. It is also the service our Free plan test account couldn't open, so on that plan you'd meet it here, not in a lab.

</details>

### Decision 5: "My nephew says to use Amazon Q to answer staff questions from our recipe binder."

<details><summary>Model answer</summary>

Ask which Amazon Q he means. **Amazon Q Developer** helps people who build and run software on AWS; it doesn't answer staff questions from company documents. **Amazon Q Business** did that, but it's no longer open to new customers, and AWS now points to **Amazon Quick** instead ([availability change](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html)). "Amazon Q" alone isn't one product.

</details>

### Decision 6: "Should we train our own model to read receipts? And what about predicting how many croissants to bake each morning?"

<details><summary>Model answer</summary>

Receipts: no. Textract already does it, so training a model would be building what AWS runs for you. Croissants: that answer must be learned from the bakery's own sales history. AWS's ready-made forecasting service, Amazon Forecast, is closed to new customers, and it isn't on the exam's list. So this is a job for **Amazon SageMaker AI** (formerly Amazon SageMaker): build, train and deploy your own model. It's the last branch of the flowchart, and it needs someone with machine learning skills.

</details>

## Recap

Name what goes in and what must come out, then pick the ready-made service that turns one into the other, and say which near-miss you're ruling out. Pairs work together as often as they compete: Athena under Quick Sight, Lex inside Connect Customer. Build with SageMaker AI only when nothing ready-made fits. Check status before you plan: a service can be on the exam and closed to new customers.

**Next:** [the Module 10 mastery check](07-check.md). First, rebuild the grid from Decision 1 from memory, without looking back.

---

"Simulation S12: Match each request to a service by what goes in and what comes out" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
