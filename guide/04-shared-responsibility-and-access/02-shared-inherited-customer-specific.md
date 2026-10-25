---
type: lesson
id: clf-04-02
title: "Shared, inherited and customer-specific controls"
tasks: ["2.1"]
objectives: ["04.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished lesson 04.01, Module 02 and the guardrails primer; about 15 minutes; works on a phone"
prerequisites: [clf-04-01, guardrails-03, guardrails-06]
terms_introduced: [IT control, audit, compliance, inherited control, shared control, customer-specific control, patch management, configuration management, awareness and training]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
---

# "Shared" means each side does its own half of the same kind of work, not the same task together

AWS sorts security safeguards into three kinds. You **inherit** some from AWS without lifting a finger; some are **shared**, with AWS and you each doing the same kind of work on different things; and some are **customer-specific**, so only you can do them.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** read [lesson 04.01](01-security-of-vs-in-the-cloud.md) first; this lesson uses its "line" between AWS's side and yours.

## Warm-up: what you remember

1. (Lesson 04.01.) The bakery's website runs on an EC2 virtual server. Who patches that server's guest operating system?
2. (Primer page 03.) You set a password policy for your account's IAM users. Did AWS set it for you, or did you?

<details><summary>Feedback</summary>

1. **The bakery.** On EC2, AWS says the customer manages the guest operating system, including its patches.
2. **You did.** AWS offered the setting; choosing the rules was your job. This lesson calls that your half of configuration management.

</details>

## What you'll learn

By the end of this lesson, you can explain what "shared" means in the shared responsibility model, with examples of inherited, shared and customer-specific controls (objective 04.02a).

Try this first, and guess if you're unsure: patch management is called a "shared control". Does that mean AWS helps you patch your EC2 server?

## The big picture: three kinds of control

An **IT control** is a safeguard, such as a rule, a process or a setting, that lowers a risk and that someone can check. An **audit** is an independent check that controls exist and work, and **compliance** means meeting the rules that apply to you, such as laws or industry standards. The shared responsibility model divides controls as well as tasks ([Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)), and the difference between the three kinds is who does the work.

![Three panels. Inherited: AWS does all of it, and you have nothing to do. Shared, highlighted: AWS does its own half for the infrastructure, and you do your own half for what you run. Customer-specific: AWS has no counterpart, and you do all of it. Each panel gives AWS's example and a bakery example.](../../images/04-02-three-kinds.svg)

*Notice that only the middle panel has work on both sides, and even there each side has its own part. No panel shows the two sides working on the same thing.*

**Long description.** Three panels side by side. Inherited: AWS's part is all of it; your part is nothing to do, because you inherit it. AWS's example is physical and environmental controls; for the bakery, no more locking the server room or keeping it cool. Shared, highlighted: AWS does its own half, for the infrastructure; you do your own half, for what you run. AWS's examples are patch management, configuration management, and awareness and training; for the bakery, AWS patches its hosts and the bakery patches its web server. Customer-specific: AWS has no counterpart, and your part is all of it. AWS's example is routing or zoning data within specific security environments; for the bakery, the order database accepts connections only from the web server.

## Inherited controls: AWS does all of it

An **inherited control** is one AWS fully carries out, and you get the benefit. AWS's example is **physical and environmental controls**: who can enter the buildings, and the power, cooling and network that keep machines running. You can't do anything about these on AWS, and you don't need to. Locking and cooling the bakery's old back room was the bakery's control; now the bakery inherits it.

Inheriting a control doesn't remove the need for evidence: AWS suggests reviewing third-party audit reports to see what you inherit. Asked how its servers are protected from fire and power cuts, the bakery answers: "AWS carries out those controls; here is AWS's audit report."

## Shared controls: each side does its own half

A **shared control** applies to both AWS's infrastructure and your part, "in completely separate contexts", as AWS puts it. AWS gives three examples.

![Three rows, each split by a dashed divider into AWS's half and your half. Patch management: AWS patches its infrastructure; you patch the guest operating system and applications you run. Configuration management: AWS configures its own infrastructure devices; you configure your operating systems, databases, applications and resource settings. Awareness and training: AWS trains its employees; you train your own people.](../../images/04-02-shared-controls.svg)

*Notice the dashed divider down the middle. It is the line from lesson 04.01. Each row has work on both sides of it, but no single task crosses it.*

**Long description.** Three rows, each split into AWS's half and your half by a dashed divider. Patch management: AWS patches and fixes flaws in its infrastructure; you patch the guest operating system and applications you run, such as the bakery's web server and the libraries in its order functions. Configuration management: AWS configures its own infrastructure devices; you configure your operating systems, databases, applications and resource settings, such as the web server's security group and Block Public Access on the photo bucket. Awareness and training: AWS trains AWS employees; you train your own people, such as the owner, her nephew and the new teammate. A note says a question about one specific task has one answer, one side; the control as a whole is what is shared.

- **Patch management** (keeping software updated): AWS patches its infrastructure; you patch your guest operating systems and applications. How big your half is depends on the service: on EC2 it's the guest OS and the website software; on RDS, AWS also patches the operating system and database software ([RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)); on Lambda, you keep the code, its libraries and the move off retired runtimes ([Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)).
- **Configuration management** (keeping systems set up correctly): AWS configures its own devices; you configure your operating systems, databases, applications and the settings of the resources you create, such as Block Public Access and a security group.
- **Awareness and training** (teaching people to work securely): AWS trains its own employees, and you must train yours. AWS's training does nothing for the bakery's staff, so the new teammate's training is the bakery's job.

## "Shared" doesn't mean both sides do the same task

You may have read that "shared responsibility" means AWS and you work on the same tasks together, so that AWS helps patch your EC2 server. That's wrong: a shared control is a *kind* of work that both sides do, each for its own things, and any specific task belongs to one side only. The customer alone patches the guest operating system on EC2; AWS alone patches the host underneath.

It's tempting because in everyday English "shared" means "done together", and practice questions often offer "both AWS and the customer" as a choice. Use this rule: if a question names **one specific thing** ("who patches the guest OS on EC2?"), the answer is one side. If it asks which **type of control** is shared, the answer is patch management, configuration management, or awareness and training.

## Customer-specific controls: only you can do these

A **customer-specific control** depends only on what you build, so AWS has no matching half. AWS's example is "service and communications protection or zone security": rules that keep certain data inside certain protected areas, or send it only along certain paths. For the bakery, that could mean the order database accepts connections only from the web server, never from the internet. Only the bakery knows which data needs that, and why.

| | Inherited | Shared | Customer-specific |
|---|---|---|---|
| Who does the work | AWS only | Each side, on its own things | The customer only |
| AWS's example | Physical and environmental controls | Patch management, configuration management, awareness and training | Routing or zoning data in specific security environments |
| Evidence for an auditor | AWS's audit reports | AWS's reports for its half; your own records for yours | Your own records |

> **Example:** the bakery's insurer asks, "How do you keep operating systems up to date?" The expert splits the question into AWS's things and the bakery's things. Patch management has work on both sides, so it's **shared**: the bakery patches the web server's guest OS and keeps its own patch records; AWS patches the hosts, and the database's OS on RDS, and its audit reports cover that half. A question about the bakery's own staff or settings never has "AWS" as the whole answer.

> **Your turn:** Sort each control and say who does the work. (a) Replacing failed hard disks in the servers that store the orders. (b) Teaching the new teammate to sign in with MFA. (c) Keeping customers' phone numbers only in the order database, never in the photo bucket.

<details><summary>Model answer</summary>

(a) **Inherited**: hardware is physical infrastructure, so AWS does all of it, and the bakery's evidence is AWS's audit report. (b) **Shared** control, but this task is the bakery's alone: AWS trains only its own staff. (c) **Customer-specific**: the requirement comes only from the bakery's own application, so AWS has no matching half.

</details>

## Summary

- **Controls are safeguards an auditor checks**, and the shared responsibility model divides them as well as tasks.
- **Inherited controls** are AWS's alone, such as physical and environmental controls; you show AWS's audit reports as evidence.
- **Shared controls** are patch management, configuration management, and awareness and training: each side does its own half, and how big your half is depends on the service.
- **"Shared" doesn't mean done together.** A specific task belongs to one side; the kind of control is what is shared.
- **Customer-specific controls** come only from what you build, such as keeping certain data in certain protected areas.

## Practice

1. **Which of these is a shared control?**

   A. Physical security of the data centers\
   B. Configuration management\
   C. Zoning sensitive data into a specific security environment\
   D. Replacing failed hardware

   <details><summary>Feedback</summary>

   **B is right.** AWS configures its infrastructure devices; customers configure their own operating systems, databases and applications.

   - **A is wrong.** Physical security is inherited.
   - **C is wrong.** That is AWS's example of a customer-specific control.
   - **D is wrong.** Hardware is AWS's alone, part of the physical infrastructure.

   </details>

2. **A company runs its application on EC2 and its database on RDS. For patch management, which part is the company's?**

   A. Patching the RDS database software\
   B. Patching the EC2 guest operating system\
   C. Patching the hosts under both services\
   D. None, because patch management is inherited

   <details><summary>Feedback</summary>

   **B is right.** On EC2, the customer patches the guest OS.

   - **A is wrong.** On RDS, AWS patches the database software.
   - **C is wrong.** The hosts are AWS's on every service.
   - **D is wrong.** Patch management is shared, not inherited.

   </details>

3. **A colleague says, "Training is a shared control, so AWS's security training covers our staff." Which reply is correct?**

   A. Right: shared controls are done by both sides together.\
   B. Wrong: training is an inherited control, so AWS needs no help.\
   C. Wrong: AWS trains its own employees, and the company must train its own staff.\
   D. Right: AWS's training reaches every customer's staff.

   <details><summary>Feedback</summary>

   **C is right.** Shared means each side does its own half, in its own context.

   - **A is wrong.** No specific task is done by both sides together.
   - **B is wrong.** Training is shared, not inherited.
   - **D is wrong.** AWS's training covers AWS employees only.

   </details>

**Next:** try [Simulation S3: the responsibility slider](08-sim-responsibility-slider.md), then [Identities](03-identities.md), which starts the second half of the module: who can do what in your account.

## Where to check the current details

- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS, including the inherited, shared and customer-specific controls (checked 2026-10-24)
- [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), Amazon RDS User Guide (checked 2026-10-24)

---

"Shared, inherited and customer-specific controls" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
