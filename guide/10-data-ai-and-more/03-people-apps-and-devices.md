---
type: lesson
id: clf-10-03
title: "People, apps and devices"
tasks: ["3.8"]
objectives: ["10.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 09, the guardrails primer and lessons 10.01 and 10.02; about 20 minutes; works on a phone"
prerequisites: [clf-10-02, clf-07-00, clf-06-00]
terms_introduced: [end-user computing, virtual desktop, pixel streaming, Amazon WorkSpaces, Amazon WorkSpaces Applications, application streaming, Amazon WorkSpaces Secure Browser, contact center, agent, Amazon Connect Customer, transactional email, front end, AWS Amplify, Internet of Things, AWS IoT Core, MQTT, IoT rule]
pillars: [security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html"
  - "https://aws.amazon.com/workspaces-family/workspaces/faqs/"
  - "https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html"
  - "https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-secure-browser.html"
  - "https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html"
  - "https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html"
  - "https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html"
  - "https://docs.aws.amazon.com/ses/latest/dg/Welcome.html"
  - "https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html"
  - "https://aws.amazon.com/amplify/faqs/"
  - "https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html"
---

# Match the need to who is on the other end: staff at a screen, customers on the phone or in their inbox, app users, or machines

The last services on the exam's list serve the people and things around the bakery's website. Ask who is on the other end, and one service fits each need: desktops for staff, a contact center and email for customers, a front end for app users, and a gateway for devices.

**Exam guide:** [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.8](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.8).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** lesson 10.02, [AI and machine learning](02-ai-and-ml.md), introduced Amazon Lex, which returns here. This lesson answers three of the bakery's requests in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From Module 07: AWS Client VPN connects what to a VPC: whole office networks, or individual people's devices?

<details><summary>Feedback</summary>

1. **Individual people's devices.** Client VPN gives a laptop a network path; the person still runs their apps on the laptop. The WorkSpaces family, in this lesson, gives them a computer in AWS instead.

</details>

## What you'll learn

By the end of this lesson, you can match a need for desktops, apps, customer contact, email, a web or mobile front end, or connected devices to the AWS service for it (objective 10.03a).

Try this before you read on, and guess if you're unsure: is Amazon Connect a chatbot?

## The big picture: four kinds of user, seven services

The exam groups these services under end-user computing, business applications, front-end web and mobile, and the Internet of Things. Grouped by who is on the other end, they're easier to keep apart.

![Four groups. Staff at a screen get Amazon WorkSpaces, WorkSpaces Applications or WorkSpaces Secure Browser. Customers get Amazon Connect Customer and Amazon SES. App users get AWS Amplify. Devices get AWS IoT Core.](../../images/10-03-big-picture.svg)

*Notice that the staff group has three services. They differ only in how much of a computer the user gets.*

**Long description.** Four groups by who is on the other end. Staff at a screen: WorkSpaces (a whole desktop), WorkSpaces Applications, the exam's AppStream 2.0 (one application), and WorkSpaces Secure Browser (one web browser). Customers: Amazon Connect Customer, the exam's Amazon Connect (a contact center), and Amazon SES (email). App users: AWS Amplify (the front end). Devices: AWS IoT Core. A note says Secure Browser closes to new customers on 2026-10-29.

## End-user computing: a desktop, an app or a browser that runs in AWS

**End-user computing** is the exam's name for services that give people a computer, an app or a browser that runs in AWS. All three below use **pixel streaming**: the software runs in AWS, and only a moving picture of the screen reaches the user's device, so the business's data stays in AWS.

### WorkSpaces gives each person a whole desktop that runs in AWS

**Amazon WorkSpaces** gives each user a **virtual desktop**, running Windows or Linux in AWS, that they reach from a laptop, tablet, Chromebook or (if the administrator allows) a web browser ([What is Amazon WorkSpaces?](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html), checked 2026-10-23). There's no hardware to buy, and you add or remove users as needs change. You can pay monthly or by the hour; hourly billing suits part-time and seasonal staff ([Amazon WorkSpaces FAQs](https://aws.amazon.com/workspaces-family/workspaces/faqs/), checked 2026-10-24). That fits the owner's request for December's temporary staff: their own laptops, the bakery's systems on desktops in AWS, removed in January.

### WorkSpaces Applications streams single apps; Secure Browser streams one web browser

- **Amazon AppStream 2.0 (now Amazon WorkSpaces Applications)** streams individual desktop applications to a user's browser or client: **application streaming**. Users always get the version you installed, and nothing is installed on their device ([What is Amazon WorkSpaces Applications?](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html), checked 2026-10-23). It suits many people who need one or two specific programs.
- **Amazon WorkSpaces Secure Browser (formerly WorkSpaces Web)** gives users an isolated web browser running in AWS, for internal websites and software-as-a-service apps, with no VPN or client software ([What is WorkSpaces Secure Browser?](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-secure-browser.html), checked 2026-10-23).

> **Dated (checked 2026-10-24):** Amazon WorkSpaces Secure Browser **closes to new customers on 2026-10-29**. Existing customers can keep using it. For new setups, AWS suggests WorkSpaces Applications with a Chrome browser image you manage, or an enterprise secure browser from an AWS Partner ([WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html)). It's still on the exam guide, so learn the job it does.

![Three panels, each with the service running in AWS and only pixels streaming to the user's screen: WorkSpaces shows a whole desktop, WorkSpaces Applications shows one application, and Secure Browser shows one web browser.](../../images/10-03-what-the-user-sees.svg)

*Notice that the three screens get smaller from left to right: a desktop, an app, a browser.*

**Long description.** Three panels; in each, the service runs in AWS and only pixels reach the user's screen, which shows a whole desktop (WorkSpaces), one application (WorkSpaces Applications) or one web browser (Secure Browser, closed to new customers from 2026-10-29). The table below gives the same comparison.

| | WorkSpaces | WorkSpaces Applications (AppStream 2.0) | WorkSpaces Secure Browser |
|---|---|---|---|
| **The user gets** | A whole desktop of their own | One or a few applications | One web browser |
| **Fits** | Staff who need a full work computer | Many people who need the same specific program | Access to internal web apps |

None of them is Client VPN: a VPN gives a device a network path; these give the person a computer, an app or a browser to use.

> **Misconception:** "AppStream 2.0 and WorkSpaces Web are the current names." They aren't: AppStream 2.0 is now **Amazon WorkSpaces Applications**, and WorkSpaces Web became **WorkSpaces Secure Browser**. The old name feels current because the exam guide still prints "Amazon AppStream 2.0"; on the exam, it means application streaming.

## Business applications: Connect runs the contact center, SES sends email

### Connect runs the contact center; Lex is the bot inside it

**Amazon Connect (now Amazon Connect Customer)** is a cloud **contact center**: the system a business uses to handle customer calls and chats. It provides phone numbers, queues and routing, and the staff who answer, called **agents**, handle voice, chat and other channels, with no telephone hardware to buy ([What is Connect Customer?](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html), checked 2026-10-24). "Amazon Connect" is now the brand for a set of AI products; when the exam says Amazon Connect, it means the contact center.

**Amazon Lex** builds the bot. A Connect flow can hand a caller to a Lex bot that understands what they want, and pass them to an agent when the bot can't help ([What is Amazon Lex V2?](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)). That answers the prequestion: Connect isn't a chatbot. It owns the phone line, the queue and the agents, and Lex holds the conversation. A website chat bot needs only Lex; a call center staffed only by people needs only Connect; a contact center with a bot uses both.

### SES sends email at scale

**Amazon Simple Email Service (Amazon SES)**, from Module 08, sends email from your own addresses and domains: **transactional email**, such as order confirmations and password resets, and marketing email such as newsletters, with no mail servers to run ([What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html), checked 2026-10-23). The bakery would use it for "Your order is ready" emails.

## Amplify builds and hosts web and mobile front ends

The **front end** is the part of an app people see and touch: web pages, a phone app. **AWS Amplify** is a set of tools and services for building, connecting and hosting web and mobile apps on AWS ([AWS Amplify FAQs](https://aws.amazon.com/amplify/faqs/), checked 2026-10-23). Amplify Hosting connects to a Git repository and builds and deploys every change you commit ([Welcome to AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)), and its libraries add back-end features such as sign-in and data storage to web, iOS and Android apps.

Don't confuse it with Module 06's simpler paths: **Elastic Beanstalk** runs server-side applications on EC2 instances it builds for you, and **Lightsail** rents a simple server at a fixed monthly price. Amplify is for front-end and mobile developers.

## IoT Core connects devices and routes what they send

The **Internet of Things (IoT)** means physical devices, such as sensors and machines, that connect to the internet to send data or receive commands. **AWS IoT Core** lets connected devices talk securely to AWS services and to each other, at very large scale ([What is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), checked 2026-10-23). Each device proves who it is, typically with a certificate. Devices usually send short messages with **MQTT**, a lightweight protocol for small devices, and an **IoT rule** sends matching messages on to other AWS services, such as S3 or an SNS topic that texts the owner.

Kinesis streams data once it's in AWS, but doesn't connect or authenticate devices. AWS IoT Greengrass and AWS IoT Device Defender, which may appear as options, are out of the exam's scope.

> **Example:** the owner's other three requests. The phone line is **Amazon Connect** with a **Lex** bot inside it (Lex alone has no phone line or agents). The temporary staff get **Amazon WorkSpaces**, billed by the hour and removed in January (Client VPN gives no computer; Secure Browser covers web apps only). The freezers connect through **AWS IoT Core**, with one rule storing readings in S3 and another sending warnings through SNS.

> **Your turn:** A cake-decorating school wants 40 students to use one design program for a two-week course, from school laptops and home computers, without installing it anywhere. Which service fits, and why not WorkSpaces?

<details><summary>Model answer</summary>

**Amazon WorkSpaces Applications** (the exam's AppStream 2.0). The students need one program, which it streams to each device's browser or client with nothing installed. WorkSpaces would give every student a whole desktop, which is more than the course needs.

</details>

## Summary

- **Staff:** WorkSpaces gives a whole desktop; AppStream 2.0 (now WorkSpaces Applications) streams single apps; WorkSpaces Secure Browser streams one browser and closes to new customers on 2026-10-29.
- **Customers:** Amazon Connect (now Connect Customer) runs the contact center, with a Lex bot inside it if needed; SES sends email at scale.
- **App users and devices:** Amplify builds and hosts web and mobile front ends from Git; IoT Core connects and authenticates devices, and its rules route their messages to other AWS services.

## Practice

1. **Which service lets a company stream one specific desktop application to users' web browsers, without giving each user a full desktop?**

   A. Amazon WorkSpaces\
   B. Amazon AppStream 2.0 (now Amazon WorkSpaces Applications)\
   C. AWS Client VPN\
   D. AWS Amplify

   <details><summary>Feedback</summary>

   **B is right.** Application streaming: users get the app, not a desktop.

   - **A is wrong.** WorkSpaces gives each user a whole desktop.
   - **C is wrong.** Client VPN gives a device a network path; it doesn't run applications.
   - **D is wrong.** Amplify builds and hosts web and mobile front ends.

   </details>

2. **A company wants a cloud call center where customers first talk to a bot, then reach a person if needed. Which two services does it combine?**

   A. Amazon Connect and Amazon Lex\
   B. Amazon SES and Amazon Polly\
   C. Amazon Lex and Amazon Transcribe only\
   D. AWS IoT Core and Amazon SNS

   <details><summary>Feedback</summary>

   **A is right.** Connect provides the phone line, queues and agents; Lex provides the bot.

   - **B is wrong.** SES sends email and Polly speaks text.
   - **C is wrong.** Without Connect there's no phone line, queue or agents.
   - **D is wrong.** IoT Core connects devices; SNS sends notifications.

   </details>

3. **The bakery's developer wants the website hosted from a Git repository so each commit goes live automatically, and customer sign-in added to its phone app. Which service fits both?**

   <details><summary>Feedback</summary>

   **AWS Amplify.** Amplify Hosting deploys every commit from Git, and Amplify's libraries add back-end features such as sign-in to web and mobile apps.

   </details>

**Next:** practice the match with [Simulation S12: input → output matcher](06-sim-input-output-matcher.md), then take [the module's mastery check](07-check.md).

## Where to check the current details

- [Amazon WorkSpaces FAQs](https://aws.amazon.com/workspaces-family/workspaces/faqs/) (checked 2026-10-24)
- [WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html) (checked 2026-10-24)
- [What is Connect Customer?](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) (checked 2026-10-24)

---

"People, apps and devices" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
