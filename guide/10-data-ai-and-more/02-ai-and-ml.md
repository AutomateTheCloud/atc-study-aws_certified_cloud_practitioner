---
type: lesson
id: clf-10-02
title: "AI and machine learning"
tasks: ["3.7", "2.1"]
objectives: ["10.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 09, the guardrails primer and lesson 10.01; about 20 minutes; works on a phone"
prerequisites: [clf-10-01, clf-05-02, clf-09-00]
terms_introduced: [artificial intelligence, machine learning, model, training, ready-made AI service, generative AI, sentiment, entity, Amazon Comprehend, Amazon Translate, Amazon Polly, Amazon Transcribe, Amazon Lex, bot, Amazon Rekognition, Amazon Textract, Amazon SageMaker AI, Amazon Bedrock, Amazon Q Developer, Amazon Q Business]
pillars: [performance-efficiency, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/translate/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/polly/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/textract/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"
  - "https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html"
  - "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html"
  - "https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/"
  - "https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html"
  - "https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html"
  - "https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-availability-change.html"
  - "https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html"
  - "https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html"
---

# Say what goes in and what must come out, and the ready-made AI service picks itself; build your own model only when none fits

Most teams that use artificial intelligence on AWS buy it ready-made: AWS has trained the model, and you call it. Each ready-made service is defined by what you give it and what it gives back, and you build your own model with SageMaker AI only when none of them fits.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** read lesson 10.01, [Analytics in five verbs](01-analytics-in-five-verbs.md), first. This lesson answers three of the bakery's requests in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From Module 09: which AWS service scans S3 buckets for sensitive data, such as credit card numbers?

<details><summary>Feedback</summary>

1. **Amazon Macie.** Keep it in mind: Comprehend, in this lesson, can also spot personal data, but in text you send it, not in your buckets.

</details>

## What you'll learn

By the end of this lesson, you can choose an AI or machine learning service by what goes in and what must come out (objective 10.02a), say when a team uses SageMaker AI instead, and say which Amazon Q product does what.

Try this before you read on, and guess if you're unsure: a customer phones the bakery and hears the opening hours read out by a computer voice. Which service makes the voice: Polly, Transcribe or Lex?

## The big picture: one grid, eight services

**Artificial intelligence (AI)** is computer systems doing tasks that once needed a person, such as understanding speech. **Machine learning (ML)** is the usual way to build it: people show a computer many examples and it learns the patterns. What it learns is a **model**, and building one from examples is **training**. A **ready-made AI service** is one whose model AWS has already trained: you send input through an API, get a result back, and need no ML skills.

![A grid of rows, each reading input, AWS service, output, grouped by text in, sound in, a conversation, pictures in, and a last row for when nothing ready-made fits: your own data goes to Amazon SageMaker AI.](../../images/10-02-input-output-grid.svg)

*Notice the "Text in" group. Text goes into three different services, and the output you need decides which one.*

**Long description.** Three columns: what goes in, the AWS service, what comes out. Text goes to Comprehend (meaning), Translate (another language) or Polly (speech); speech to Transcribe (a transcript); a conversation to Lex (a bot's reply); photos or video to Rekognition (objects, scenes, faces, unsafe content); scanned documents to Textract (text, form fields, tables, receipt totals). These seven are ready-made. Your own data goes to SageMaker AI, for a model you build, train and deploy.

## Ready-made services: name the input, then the output

### Text in: Comprehend finds meaning, Translate changes the language

**Amazon Comprehend** reads text and tells you what's in it: the **sentiment** (positive, negative, neutral or mixed), the **entities** it mentions (people, places, organizations, dates), key phrases, the language, and personal data such as names and card numbers ([What is Amazon Comprehend?](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), checked 2026-10-23). It describes the text; it doesn't change it. **Amazon Translate** turns text in one language into another, in real time or in batches ([What is Amazon Translate?](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)). Comprehend can tell you *which* language a review is in; only Translate rewrites it.

### Sound and conversation: Transcribe listens, Polly speaks, Lex holds the conversation

- **Amazon Transcribe** turns speech into text, from a recording or live audio ([What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html), checked 2026-10-23). Speech in, text out.
- **Amazon Polly** turns text into lifelike speech, in many languages and voices ([What is Amazon Polly?](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)). Text in, audio out.
- **Amazon Lex** builds a **bot**: a program that holds a conversation, in text or by voice. It works out what the customer wants, asks for missing details and replies ([What is Amazon Lex V2?](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)).

That answers the prequestion: the voice is Polly's; a Lex bot would decide what to say. Polly and Transcribe run in opposite directions, so "turn our call recordings into text" is never Polly.

### Pictures and documents: Rekognition sees, Textract reads

**Amazon Rekognition** analyzes images and video: it finds objects, scenes and text in pictures, flags unsafe content, and analyzes faces ([What is Amazon Rekognition?](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html), checked 2026-10-23). **Amazon Textract** reads documents: typed and handwritten text, **form fields** (a label and its value) and **tables**, and the vendor, total and line items of receipts and invoices ([What is Amazon Textract?](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), checked 2026-10-24). Rekognition can find words in a picture too; the difference is what comes back.

![A made-up supplier receipt sent to three services: Rekognition returns labels and loose lines of words; Textract, highlighted, returns the vendor, date, total and line items; Comprehend needs text first, so it's a second step.](../../images/10-02-one-receipt-three-services.svg)

*Notice that only Textract returns the receipt's structure: who was paid, how much, and for what.*

**Long description.** A made-up receipt from Mill and Co., total $84.20, goes to three panels. Rekognition returns labels such as "paper" and loose lines of words. Textract, highlighted, returns the vendor, date, total and line items: it fits. Comprehend needs text, not a photo, so it's a second step. The outputs are illustrations, not real responses.

| | Comprehend | Textract | Rekognition |
|---|---|---|---|
| **What goes in** | Text | Scanned documents, PDFs, photos of forms | Images and video |
| **What comes out** | Meaning: sentiment, entities, key phrases, personal data | Text and structure: lines, form fields, tables, receipt totals | What's in the picture: objects, scenes, faces, unsafe content |

> **Your turn:** Name the service for each: (a) the app reads each cake's description aloud; (b) a chat window where customers ask "is order 1234 ready?"; (c) which of 400 reviews are angry.

<details><summary>Model answer</summary>

(a) **Polly**: text in, speech out. (b) **Lex**: a conversation in, and the bot works out the request and replies. (c) **Comprehend**: text in, sentiment out (add **Translate** first if some reviews aren't in English).

</details>

## When nothing ready-made fits, SageMaker AI builds your own model

**Amazon SageMaker AI** is a fully managed service for building, training and deploying your own ML models: data scientists bring data, train a model and host it so applications can call it ([What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), checked 2026-10-24). AWS runs the servers; the data, the model and the ML skill are yours. A team turns to it when the question is its own, such as a flour supplier predicting next week's orders from its own history. Reading receipts is a solved problem, so start ready-made.

> **Misconception:** "Amazon SageMaker is the service for building models." That's the old name. On 2024-12-03 AWS renamed it **Amazon SageMaker AI**; "Amazon SageMaker" now names a wider platform for data, analytics and AI that includes it. The old name is tempting because most practice material, and many AWS command names, still say "sagemaker". An older question that says "Amazon SageMaker" for a custom model means SageMaker AI.

**Amazon Bedrock** offers foundation models from Amazon and other AI companies through an API, for building **generative AI** applications, which produce new content such as text or code ([What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)). It isn't on the exam's in-scope list (checked 2026-10-24); you'll meet the name because Amazon Q is built on it.

## Amazon Q, and the AI names that are closed

"Amazon Q" is a brand for AWS's generative AI assistants, and they do different jobs:

- **Amazon Q Developer** helps people who build and run on AWS: in the console you ask about AWS services and your resources, and in a code editor it explains, suggests and writes code ([What is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html), checked 2026-10-24).
- **Amazon Q Business** answered employees' questions from their company's own documents. It's **closed to new customers** (announced 2026-06-30), and AWS points them to Amazon Quick ([Q Business availability change](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html)).

> **Dated (checked 2026-10-24):** Q Developer's code-editor (IDE) plugins and paid subscriptions take no new sign-ups since 2026-05-15 and reach end of support on **2027-04-30**; AWS points to a separate tool, Kiro. Q Developer in the AWS console carries on ([end of support announcement](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/)).

> **Misconception:** "Amazon Q is one product." It isn't: Q Developer helps with code and AWS, and Q Business worked over company data. The exam guide lists just "Amazon Q", which makes the single-product idea tempting. Help with code, the AWS console or AWS resources means Q Developer.

Older practice questions still offer names you should recognize but not choose ([AWS lifecycle list](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html), checked 2026-10-24): **Amazon Fraud Detector**, closed to new customers since 2025-11-07 ([availability change](https://docs.aws.amazon.com/frauddetector/latest/ug/frauddetector-availability-change.html)); **Amazon Forecast**, closed to new customers (announced 2024-07-29; [What is Amazon Forecast?](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)); and **Amazon Personalize** (recommendations), available but out of the exam's scope.

> **Misconception:** "Amazon Kendra is the answer for searching company documents." Not any more: AWS closed it to new customers on 2026-07-30, pointing them to Amazon Bedrock Knowledge Bases, and the exam guide no longer lists it ([Kendra availability change](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html)). It's tempting because older practice banks use it, and the name sounds like an exact fit. Treat it as a distractor.

## Your side of the line

Ready-made AI services sit far toward AWS's side of the shared responsibility line: AWS trains and runs the models and the servers. Yours: **who may call them** (IAM policies), **the data you send and get back** (receipts can hold personal data), and **checking the results**. With SageMaker AI, more moves to your side: the training data, the model and how it's hosted.

> **Example:** the owner's three requests. The phone bot is a conversation: **Amazon Lex** (lesson 10.03 adds the phone line). The spoken descriptions are text in, speech out: **Amazon Polly**. The receipts are documents: **Amazon Textract**, with the accountant checking totals. None needs SageMaker AI.

## Summary

- **Choose a ready-made AI service by what goes in and what must come out.** AWS trained the model; you need no ML skills.
- **Text, sound and conversation:** Comprehend finds meaning; Translate changes the language; Polly speaks; Transcribe writes speech down; Lex builds bots. **Pictures and documents:** Rekognition describes images and video; Textract reads documents.
- **SageMaker AI** (formerly Amazon SageMaker) builds, trains and deploys your own model, when nothing ready-made fits.
- **Amazon Q is a family:** Q Developer helps you build and run on AWS; Q Business is closed to new customers. Kendra, Fraud Detector and Forecast are closed to new customers; treat them, and Personalize, as distractors.

## Practice

1. **The bakery wants subtitles for its cake-decorating videos. Which service turns the spoken words into text?**

   A. Amazon Polly\
   B. Amazon Transcribe\
   C. Amazon Translate\
   D. Amazon Rekognition

   <details><summary>Feedback</summary>

   **B is right.** Speech in, text out.

   - **A is wrong.** Polly does the opposite: text in, speech out.
   - **C is wrong.** Translate changes the language of text you already have; it doesn't listen.
   - **D is wrong.** Rekognition analyzes what's seen in video, not what's said.

   </details>

2. **Which need calls for Amazon SageMaker AI rather than a ready-made AI service?**

   A. Detecting whether product reviews are positive or negative\
   B. Reading totals from scanned invoices\
   C. Predicting next week's flour orders from a supplier's own order history, with a model the supplier's data scientists build\
   D. Translating the menu into Spanish

   <details><summary>Feedback</summary>

   **C is right.** It's the supplier's own question, answered by a model trained on its own data.

   - **A is wrong.** Comprehend's sentiment analysis does that, ready-made.
   - **B is wrong.** Textract reads invoices, ready-made.
   - **D is wrong.** Translate does that, ready-made.

   </details>

3. **Which pairing of service and output is correct?**

   A. Amazon Comprehend: tables and form fields from a scanned form\
   B. Amazon Textract: the sentiment of a customer email\
   C. Amazon Rekognition: objects and unsafe content in uploaded photos\
   D. Amazon Lex: spoken audio from a product description

   <details><summary>Feedback</summary>

   **C is right.** Images in; objects, scenes and unsafe content out.

   - **A is wrong.** Tables and form fields come from Textract.
   - **B is wrong.** Sentiment comes from Comprehend.
   - **D is wrong.** Speech from text is Polly; Lex holds conversations.

   </details>

**Next:** lesson 10.03, [People, apps and devices](03-people-apps-and-devices.md). To hear Polly yourself, do [Optional lab 14](05-lab-14-polly-text-to-speech.md).

## Where to check the current details

- [What is Amazon Comprehend?](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [What is Amazon Textract?](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) and [What is Amazon Rekognition?](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) (checked 2026-10-24)
- [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) (checked 2026-10-24)
- AWS's [list of services in maintenance](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html), for closures (checked 2026-10-24)

---

"AI and machine learning" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
