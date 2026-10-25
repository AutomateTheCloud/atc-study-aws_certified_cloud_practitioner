---
type: lesson
id: clf-01-01
title: "Computers and servers"
tasks: []
objectives: ["01.01a"]
reader: "Adult studying alone, new to IT; first lesson of the on-ramp; about 15 minutes; works on a phone"
prerequisites: [clf-01-00]
terms_introduced: [hardware, software, processor, CPU, core, memory, RAM, storage, throughput, network connection, byte, gigabyte, GiB, operating system, application, client, server, request, response, web server, rack, bottleneck]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/cpu/"
  - "https://aws.amazon.com/what-is/flash-memory/"
  - "https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/"
  - "https://aws.amazon.com/ec2/instance-types/"
  - "https://aws.amazon.com/ec2/faqs/"
---

# A server is an ordinary computer with one job: it waits for requests and answers them

Every computer has a processor, memory, storage and a network connection. When you rent a server from AWS, you choose how much of each it gets.

**For:** an adult studying alone, new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** you need nothing earlier. The [module brief](00-brief.md) explains the on-ramp.

## Test out: do you already know this?

Answer without looking anything up. If you get all three right, and didn't guess, skip to [Networks, IP addresses, DNS and HTTPS](02-networks-ip-dns-https.md).

1. In one sentence each: what does a computer's processor do, and what does its memory do?
2. A server restarts after a power cut. Which is gone: what was in its memory, or what was in its storage?
3. Could an ordinary laptop work as a server? Why or why not?

<details><summary>Answer key</summary>

1. The **processor** carries out instructions; **memory** holds the programs and data in use right now.
2. **What was in memory.** Storage keeps data with the power off.
3. **Yes.** A server is a role, not a kind of machine.

</details>

## Warm-up: what you already know

1. You open a weather app. Where does today's forecast come from?

<details><summary>Feedback</summary>

1. From another computer, which the app asked over the internet: a **server**, with your phone as its **client**.

</details>

## What you'll learn

By the end, you can explain what a server is and what its processor, memory, storage, network connection and operating system each do (objective 01.01a).

Guess before you read on: in December, the bakery's servers slow down. Would adding more storage help?

## The big picture: four parts, then the software on top

![One of the bakery's servers in three layers: four hardware parts at the bottom, the operating system above them, and the bakery's applications on top, with customers' requests arriving at the network connection.](../../images/01-01-inside-a-server.svg)

*Notice that the bakery's programs never touch the hardware directly. They ask the operating system, and it uses the four parts for them.*

**Long description.** Bottom layer, hardware: the processor does the work; memory holds the work in progress and empties when the power goes off; storage keeps data with the power off; the network connection sends and receives data. Middle: the operating system, such as Linux or Windows, shares the parts out. Top: the bakery's website and order records. Outside, customers' phones send requests to the network connection and receive answers.

## Four parts do four different jobs

**Hardware** is the physical machine; **software** is the programs that run on it.

- **The processor, or CPU, does the work.** It carries out a program's instructions one after another, very fast. A processor with several **cores** can work on several things at once ([What is a CPU?](https://aws.amazon.com/what-is/cpu/), checked 2026-10-24).
- **Memory, or RAM, holds the work in progress:** the open programs and the data they're using. The processor reaches it very quickly, but it needs constant power, so a restart empties it ([What is flash memory?](https://aws.amazon.com/what-is/flash-memory/), checked 2026-10-24).
- **Storage keeps things.** It's bigger and slower than memory and keeps data with the power off: programs, photos, saved orders. How much data it moves per second is its **throughput**.
- **The network connection talks to other computers.** Lesson 01.02 follows what travels through it.

People say a phone "has 128 GB of memory" when they mean storage; in computing, memory is only the fast part that empties without power.

**Sizes are counted in bytes.** A **byte** is about one letter of text; a **gigabyte** (GB) is a billion bytes, and a phone photo is a few million. AWS often writes **GiB**, a unit based on powers of two that's about 7% bigger than a GB, as in a server size of "2 vCPUs and 8 GiB of memory" ([Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/), checked 2026-10-24).

## The operating system runs everything else

The **operating system** is the first program a computer starts. It starts and stops the other programs, shares the hardware between them, and decides who may sign in. Most servers run Linux or Windows Server, and when you rent a server from AWS you choose one of these, among others ([Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/), checked 2026-10-24). **Applications**, such as the bakery's website, run on top of it.

Its makers publish updates, called patches, that fix flaws, often security flaws. Lesson [04.01](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md) asks, for each AWS service, who installs them.

## A server is a job, not a special kind of box

A **server** is any computer running a program that waits for requests and answers them. The computer that asks is the **client**: it sends a **request**, and the server sends back a **response**. Your browser is a client when it asks for a page; the computer that sends the page is a **web server** ([Web server vs application server](https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/), checked 2026-10-24). The client always speaks first.

> **Misconception:** "A server is a different kind of machine." It isn't: it has the same four parts as your laptop. What differs is how it's built and kept: usually no screen, often two power supplies and several disks so one failure doesn't stop it, mounted in a **rack** (a tall metal frame holding many servers) and running all day for many users. It's tempting because servers live out of sight, in locked rooms and data centers.

What you rent from AWS is a virtual server, carved out of a physical one (lesson [01.04](04-data-centers-and-virtualization.md)). Even "serverless" services (Module 06) run on servers; you just don't manage them.

## Find the part that runs out first

When a server is slow, ask which part runs out first. That part is the **bottleneck**, and adding to any other part changes nothing. AWS's server families follow the same idea: some have more processor, some more memory (lesson 06.01).

> **Example:** the bakery's three back-room servers slow down in December, when customers try to place about 120 orders an hour (made-up figures, as in Module 02). During the rush the processors are 100% busy, memory is 95% full and storage 30% full. Orders in progress need processor time and memory, so those are the bottleneck, and more storage wouldn't help: that answers the guess. In January, though, extra servers bought for December would sit idle. Module 02 starts there.

> **Your turn:** the bakery's website keeps the order a customer is still filling in, and saves it when they pay. Which part holds the unfinished order, and which holds the paid one? What happens to each if the server loses power?

<details><summary>Model answer</summary>

The unfinished order is in **memory**, so a power cut loses it. The paid order is saved to **storage**, so it survives.

</details>

## Summary

- **A server is an ordinary computer with one job:** it answers requests from clients, runs all the time, and usually sits in a rack.
- **Four parts:** the processor does the work; memory holds the work in progress and empties without power; storage keeps data with the power off; the network connection talks to other computers.
- **The operating system** shares the hardware between applications, and its patches need installing.
- **When a server is slow, find the bottleneck** and add to that part only.

## Practice

1. **The bakery's server shows: processor 20% busy, memory 40% full, storage 99% full. What should it add?**

   A. More processor cores\
   B. More memory\
   C. More storage, or delete old files\
   D. A faster network connection

   <details><summary>Feedback</summary>

   **C is right.** Storage is the part about to run out: the bottleneck.

   - **A is wrong.** The processor is only 20% busy.
   - **B is wrong.** Memory is less than half full.
   - **D is wrong.** Nothing shows the network running short.

   </details>

2. **Which of these is the operating system's job, not an application's?**

   A. Building the bakery's menu page\
   B. Sharing the processor and memory between running programs\
   C. Working out the price of an order

   <details><summary>Feedback</summary>

   **B is right.** Sharing out the hardware is the operating system's core job.

   - **A is wrong.** That's the website application's work.
   - **C is wrong.** Pricing happens inside an application.

   </details>

3. **A friend leaves an old laptop on at home, running a program that lets family download shared photos. Is it a server?**

   A. No: only machines built as servers count\
   B. Yes: it answers requests from clients\
   C. No: it has a screen and keyboard

   <details><summary>Feedback</summary>

   **B is right.** The family's phones are its clients.

   - **A is wrong.** A server is a role; machines built as servers are just more reliable at it.
   - **C is wrong.** A screen doesn't change what the computer is doing.

   </details>

**Next:** [Networks, IP addresses, DNS and HTTPS](02-networks-ip-dns-https.md).

## Where to check the current details

- [What is a CPU?](https://aws.amazon.com/what-is/cpu/), AWS (checked 2026-10-24)
- [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/), AWS (checked 2026-10-24)

---

"Computers and servers" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
