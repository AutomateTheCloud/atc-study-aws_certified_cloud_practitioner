---
type: lesson
id: clf-03-04
title: "The edge"
tasks: ["3.2", "1.1"]
objectives: ["03.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Module 02 and the guardrails primer; about 12 minutes; works on a phone"
prerequisites: [clf-02-03, clf-03-01, clf-03-02]
terms_introduced: [edge location, point of presence, content delivery network, cache, origin, Domain Name System, Amazon CloudFront, Amazon Route 53, AWS Global Accelerator, Local Zone, AWS Outposts, Wavelength Zone]
pillars: [performance-efficiency, reliability]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/cloudfront/features/"
  - "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html"
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html"
  - "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"
  - "https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html"
  - "https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"
  - "https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html"
---

# Edge locations bring AWS's network close to your users; Local Zones and Outposts bring its computers close to a city or into your building

Many small **edge locations** deliver content and answer requests near users, but never run your servers. When the servers themselves must be closer, **Local Zones** put them in a big city and **Outposts** in your own building. To tell them apart, ask where each one physically is.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 12 minutes. Reading works on a phone.

**Before you start:** read [Regions, Availability Zones and data centers](01-regions-availability-zones-data-centers.md) first.

## Warm-up: what you remember

1. From lesson 02.03: what is latency, and what makes it grow?
2. From lesson 02.01: a company keeps some systems in its own building and some on AWS, connected together. Which deployment model is that?

<details><summary>Feedback</summary>

1. **Latency** is the delay between a request and the response. It grows with distance.
2. **Hybrid.** Outposts, in this lesson, is one way to build it.

</details>

## What you'll learn

By the end of this lesson, you can say where edge locations, Local Zones and Outposts physically are, and what each is for (objective 03.04a).

Try this before you read on: is an edge location a small Availability Zone where the bakery could run its web server?

## The big picture: few Regions, many edge locations

![A schematic with three parts of the world, each holding two Regions and many more scattered edge locations; a customer connects to the nearest edge location, which reaches a Region over AWS's network.](../../images/03-04-regions-and-edge.svg)

*Notice the customer's path. The first hop goes to the nearest edge location. Only when the edge can't answer by itself does the request travel on, over AWS's network, to a Region.*

**Long description.** A schematic, not a map. Three panels, North America, Europe and Asia Pacific, each hold two Region boxes with three small AZ squares inside, and about eight edge-location dots scattered more widely. In Europe, a customer connects by a short line to the nearest edge location; a dashed line runs from it to a Region, used when the edge can't answer by itself. Dashed lines show AWS's network linking everything. Shapes are illustrative, not counts.

## Edge locations deliver and answer close to users; they don't run your servers

An **edge location**, also called a **point of presence**, is a small AWS site in a city near internet users, outside the Regions and linked to them by AWS's network ([Amazon CloudFront key features](https://aws.amazon.com/cloudfront/features/)). It isn't a small Region or AZ: it runs a few networking services, mainly Amazon CloudFront, Amazon Route 53 and AWS Global Accelerator, and you can't launch an EC2 server there. That answers the prequestion.

Edge locations give faster answers, because the first trip is short; fewer requests reaching your servers; and attack traffic absorbed far away (CloudFront includes AWS Shield Standard at no extra cost; Module 09).

> **Dated (checked 2026-10-23):** AWS's CloudFront page listed more than 750 points of presence in more than 100 cities in more than 50 countries. There are far more edge locations than Regions; don't memorize the count.

## Three services use the edge, each in its own way

Exam questions often offer these three side by side; Module 07 teaches them fully.

- **Amazon CloudFront** is AWS's **content delivery network (CDN)**, which keeps copies of content near users. If the nearby edge location has a **cache** (a stored copy), it answers at once; if not, it fetches the content from the **origin**, such as an S3 bucket, and keeps a copy ([What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)).
- **Amazon Route 53** is AWS's **Domain Name System (DNS)** service, the internet's address book that turns a name like `example.com` into an address. It can pick the answer, such as the lowest-latency Region, or a standby when the main site fails its health checks ([What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)).
- **AWS Global Accelerator** gives an application fixed addresses announced from edge locations, so traffic enters AWS's network nearby and rides it to the best healthy endpoint. It keeps no copies ([What is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)).

| | CloudFront | Route 53 | Global Accelerator |
|---|---|---|---|
| Job | Delivers content from cached copies near users | Tells users where to go (DNS) | Carries traffic over AWS's network from the nearest edge |
| Keeps copies? | Yes | No | No |
| Typical use | Websites, images, video, downloads | Domain names; sending users to the right Region or a standby | Fixed addresses; non-web traffic such as games; fast switching between Regions |

**Route 53 is not a CDN.** It only answers "where is it?"; the content comes from elsewhere, often CloudFront. Both run at edge locations, which is why they get mixed up.

> **Example:** German customers find the cake photos slow, because they sit in an S3 bucket in N. Virginia. Photos rarely change and are the same for everyone, so **CloudFront** in front of the bucket serves them from edge locations near Munich. Global Accelerator would still fetch every photo from Virginia.

## Local Zones, Outposts and Wavelength run AWS servers outside a Region

When the servers themselves must be closer, AWS offers places outside a Region, each extending a parent Region:

- **AWS Local Zones** put compute, storage and other selected services in large cities, for needs such as real-time games with single-digit-millisecond latency, or data that must stay in that city ([What is AWS Local Zones?](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html)).
- **AWS Outposts** brings AWS-managed racks or servers into your own site, for systems near on-site equipment or data that must stay on premises: the **hybrid** model. AWS maintains the hardware; you provide space, power and network ([What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)).
- **AWS Wavelength** puts compute inside telecom carriers' 5G networks. The exam guide lists it as **out of scope** (checked 2026-10-24), so it appears only as a wrong answer ([What is AWS Wavelength?](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)).

| Name | Where it physically is | What you can run there | Choose it when |
|---|---|---|---|
| **Region** | A geographic area with at least three AZs | Almost every AWS service | You place a workload near users, under the right laws |
| **Availability Zone** | One or more data centers inside a Region | Your servers and databases | You need copies that survive one location failing |
| **Edge location** | Many cities, near users, outside the Regions | CloudFront, Route 53, Global Accelerator; never your servers | Content delivered, or requests answered, close to users |
| **Local Zone** | A large city away from its parent Region | Selected services, such as compute and storage | Users in one city need single-digit-millisecond latency |
| **Outposts** | Your own building | AWS-managed racks or servers | Systems or data must stay on your premises |

> **Your turn:** a game company's players in one large city complain of lag. Its servers run in a Region several hundred kilometers away, and every move needs a reply within a few milliseconds. Which option would you look at first, and why not CloudFront?

<details><summary>Model answer</summary>

**A Local Zone** in that city, so the game servers run near the players. CloudFront wouldn't help: each move needs a fresh answer from a server, not a cached file.

</details>

## Summary

- **Edge locations** are many small sites outside the Regions that run CloudFront, Route 53 and Global Accelerator near users, never your servers.
- **CloudFront caches content; Route 53 tells users where to go; Global Accelerator carries traffic over AWS's network.**
- **Local Zones** (a big city) and **Outposts** (your building) run AWS servers outside a Region; Wavelength is out of scope. Ask where each one physically is.

## Practice

1. **Which statement about edge locations is correct?**

   A. Each edge location is a small Availability Zone inside a Region.\
   B. Edge locations run services such as CloudFront and Route 53 close to users.\
   C. You choose an edge location when you launch an EC2 instance.\
   D. There are fewer edge locations than Regions.

   <details><summary>Feedback</summary>

   **B is right.** Edge locations run a few networking services near users.

   - **A is wrong.** Edge locations sit outside the Regions.
   - **C is wrong.** EC2 instances run in AZs (or Local Zones and Outposts), not edge locations.
   - **D is wrong.** There are many more edge locations than Regions.

   </details>

2. **A company needs AWS services running inside its own factory so that machines get answers within milliseconds. Which option fits?**

   A. Amazon CloudFront\
   B. AWS Outposts\
   C. A second AWS Region\
   D. Amazon Route 53

   <details><summary>Feedback</summary>

   **B is right.** Outposts puts AWS-managed hardware in the customer's own building.

   - **A is wrong.** CloudFront delivers content; it doesn't run the factory's applications.
   - **C is wrong.** Another Region is still far from the factory.
   - **D is wrong.** Route 53 answers DNS questions.

   </details>

3. **A video-streaming company wants viewers worldwide to load its video files faster, and to reduce the load on its storage in one Region. Which service fits best?**

   A. Amazon Route 53\
   B. Amazon CloudFront\
   C. AWS Global Accelerator\
   D. A second Availability Zone

   <details><summary>Feedback</summary>

   **B is right.** CloudFront caches the files near viewers, so delivery is faster and fewer requests reach the origin.

   - **A is wrong.** Route 53 answers name lookups; it doesn't deliver or cache videos.
   - **C is wrong.** Global Accelerator speeds up the path but keeps no copies, so every request still reaches the origin.
   - **D is wrong.** A second AZ adds high availability, not closeness to viewers.

   </details>

**Next:** see Regions and Availability Zones in your own account in [Lab 02](05-lab-02-see-the-global-infrastructure.md).

## Where to check the current details

- [Amazon CloudFront key features](https://aws.amazon.com/cloudfront/features/), points of presence (checked 2026-10-23)
- [What is AWS Local Zones?](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) and [What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) (checked 2026-10-23)
- [AWS Certified Cloud Practitioner (CLF-C02) exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html), task [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2) and the out-of-scope list (checked 2026-10-24)

---

"The edge" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
