---
type: lesson
id: clf-01-04
title: "Data centers and virtualization"
tasks: []
objectives: ["01.04a"]
reader: "Adult studying alone, new to IT, before Module 02; about 15 minutes; works on a phone"
prerequisites: [clf-01-01]
terms_introduced: [data center, redundancy, virtualization, physical server, host, hypervisor, virtual machine (VM), virtual server, guest operating system, shared tenancy, image, container]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/data-center/"
  - "https://aws.amazon.com/what-is/virtualization/"
  - "https://aws.amazon.com/what-is/containerization/"
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html"
---

# A data center is a building that keeps servers running; virtualization splits each server into several virtual ones

A cloud provider's computers are real machines in buildings called data centers. A hypervisor splits each one into virtual servers that many customers share safely, and those are what you rent.

**For:** an adult studying alone, new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson uses server, operating system and rack from [Computers and servers](01-computers-and-servers.md).

## Test out: do you already know this?

Answer without looking anything up. If you get all three right, and didn't guess, skip to [APIs, the command line and JSON](05-apis-command-line-and-json.md).

1. Name three things a data center provides for its servers besides the building.
2. What does a hypervisor do?
3. What does a virtual machine carry that a container doesn't?

<details><summary>Answer key</summary>

1. Any three: power with backups, cooling, network connections, physical security.
2. It splits one physical server into virtual machines and keeps them apart.
3. Its own operating system.

</details>

## Warm-up: what you already know

1. From lesson 01.01: what does an operating system do?

<details><summary>Feedback</summary>

1. It runs the computer and shares its processor, memory, storage and network between the programs.

</details>

## What you'll learn

By the end, you can explain what a data center provides, how virtualization turns one physical server into several virtual servers, and why that makes renting servers by the minute possible (objective 01.04a).

Guess before you read on: when you rent a "server" from a cloud provider, do you get a whole physical computer?

## The big picture: one physical server, several virtual ones

![A physical server with a hypervisor on it, running three virtual servers, each with its own operating system and application, one of them another customer's. A dashed line marks that on Amazon EC2 the customer runs what is above the hypervisor and the provider everything below.](../../images/01-04-virtualization-stack.svg)

*Notice the third virtual server: another customer's, on the same physical machine. The hypervisor keeps it apart from the bakery's two.*

**Long description.** Bottom to top: the physical server, or host, in a rack; on it, highlighted, the hypervisor, which shares out the hardware and keeps the virtual servers apart. A dashed line: on Amazon EC2, the customer runs what is above it and the provider everything below. Above the line, three virtual servers, each with a guest operating system and an application: the bakery's website and its order database on Linux, and, drawn dashed, another customer's app on Windows.

## A data center keeps servers powered, cool, connected and guarded

A **data center** is a building full of racks of servers, storage and network equipment. It supplies power with battery and generator backup, cooling, fire suppression, network connections and physical security ([What is a data center?](https://aws.amazon.com/what-is/data-center/), checked 2026-10-24).

The backups are **redundancy**: more than one of something, so one failure doesn't stop the whole. Module 03 shows AWS going further, grouping data centers into separate Availability Zones so a system can survive losing a whole building. The bakery's back room has none of this: a power cut takes the website down.

## Virtualization splits one physical server into several

**Virtualization** is software that imitates hardware, so several **virtual machines (VMs)** run on one **physical server**, called the **host** ([What is virtualization?](https://aws.amazon.com/what-is/virtualization/), checked 2026-10-24). The **hypervisor** is the software on the host that creates the VMs, gives each its share of processor, memory and disk, and stops one reaching into another. Cloud providers call a VM a **virtual server**; Amazon EC2 calls it an instance.

Each VM runs its own **guest operating system**, which can differ from its neighbors', and restarts without touching them. Its neighbors can be strangers: on Amazon EC2, by default, instances from several AWS accounts may share one host, which AWS calls **shared tenancy**, and you can pay for hardware used by your account alone ([Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html), checked 2026-10-24).

> **Misconception:** "Shared hardware means other customers can see my data." They can't. The hypervisor keeps each VM's memory and disk apart, and on AWS that layer is AWS's job: the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) puts "the host operating system and virtualization layer" on AWS's side. It's tempting because "shared" sounds like a shared folder, open to all.

On EC2, the bakery patches its guest operating system and runs its website; AWS runs the hypervisor, the host and the building. Lesson 04.01 shows that line moving for other services.

## Virtualization is what lets a provider rent servers by the minute

A physical server running one customer's work typically sits mostly idle. Filling it with many VMs uses that spare capacity, and it lets a provider:

- **Hand out servers in minutes.** A new VM is software on a machine that's already running: no waiting weeks to buy hardware.
- **Copy servers from a template.** An **image** is a saved operating system and software, so ten VMs started from one image are identical. EC2 calls them AMIs (lesson 06.01).
- **Charge only for what you use.** When you delete a VM, its share goes back into the pool for someone else.
- **Move VMs between hosts.** When you stop an EC2 instance and start it again, AWS usually starts it on a different host ([How EC2 instance stop and start works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html), checked 2026-10-24). That's why a disk built into the old host (instance store) loses its data, while a network disk (Amazon EBS) follows the instance (lesson 05.01).

> **Your turn:** answer the guess. When you rent a "server" from AWS, do you get a whole physical computer? Explain in two sentences.

<details><summary>Model answer</summary>

Usually not: you get a virtual server, a share of a host that may also run other accounts' VMs. You can pay for hardware used by your account alone, but sharing is the default, and it's what makes pay-as-you-go possible.

</details>

## Containers share one operating system

A VM behaves like a whole computer, with its own operating system. A **container** packages just one application with the libraries it depends on, and the containers on a machine share its operating system, which makes each one smaller ([What is containerization?](https://aws.amazon.com/what-is/containerization/), checked 2026-10-24). Containers often run inside VMs. **Serverless** services such as AWS Lambda (lesson 06.03) go one step further: the provider runs the servers and operating systems out of your sight, and you hand it only your code.

## Summary

- **A data center** keeps racks of servers powered, cooled, connected and guarded, with redundancy so one failure doesn't stop everything.
- **Virtualization** splits a host into VMs; the hypervisor shares out the hardware and keeps them apart, and each VM runs its own guest operating system.
- **Shared hardware isn't shared data.** EC2 instances may share a host with other accounts'; isolating them is AWS's job.
- **Virtualization makes the cloud possible:** servers in minutes, copies from images, paying only while you use them.
- **Containers** share the host's operating system; serverless hides the servers entirely.

## Practice

1. **Which layer does a cloud customer manage on a virtual server such as an EC2 instance?**

   A. The hypervisor\
   B. The guest operating system\
   C. The physical server's disks\
   D. The data center's cooling

   <details><summary>Feedback</summary>

   **B is right.** The guest operating system runs inside the customer's VM.

   - **A, C and D are wrong.** The hypervisor, the hardware and the building are all the provider's.

   </details>

2. **Why can a cloud provider give you a new server in minutes?**

   A. It keeps a spare physical server boxed for each customer\
   B. A new virtual server is software started on a host that's already running\
   C. Containers don't need an operating system at all

   <details><summary>Feedback</summary>

   **B is right.** No hardware has to be bought.

   - **A is wrong.** Providers fill running machines with many customers' VMs.
   - **C is wrong.** Containers share an operating system; they still need one.

   </details>

3. **You stop an EC2 instance and start it the next morning. Data on a disk built into the old host is gone. Why?**

   A. Stopping always deletes every disk\
   B. AWS usually starts it on a different host, and instance store stays with the old one\
   C. The hypervisor erases memory and disks every night

   <details><summary>Feedback</summary>

   **B is right.** A network disk such as EBS follows the instance; instance store doesn't.

   - **A is wrong.** An EBS volume keeps its data through a stop.
   - **C is wrong.** Nothing is erased on a schedule.

   </details>

**Next:** [APIs, the command line and JSON](05-apis-command-line-and-json.md).

## Where to check the current details

- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS (checked 2026-10-24)
- [How EC2 instance stop and start works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html), Amazon EC2 User Guide (checked 2026-10-24)

---

"Data centers and virtualization" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
