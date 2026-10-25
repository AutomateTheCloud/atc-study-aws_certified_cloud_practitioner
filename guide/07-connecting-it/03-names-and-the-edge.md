---
type: lesson
id: clf-07-03
title: "Names and the edge"
tasks: ["3.5", "3.2", "2.4", "2.1"]
objectives: ["07.03a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 06, the guardrails primer and lessons 07.01 and 07.02; about 15 minutes; works on a phone"
prerequisites: [clf-03-04, clf-07-01, clf-07-02, clf-05-02]
terms_introduced: [domain name, routing policy, health check, distribution, origin access control, static IP address, anycast, API, Amazon API Gateway, throttling]
pillars: [reliability, performance-efficiency, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html"
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html"
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html"
  - "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html"
  - "https://aws.amazon.com/cloudfront/faqs/"
  - "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"
  - "https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html"
  - "https://aws.amazon.com/api-gateway/faqs/"
---

# Route 53 tells users where to go; CloudFront, Global Accelerator and API Gateway shape the trip and guard the door

Four services sit between your customers and your servers. **Amazon Route 53** answers "where is it?", **Amazon CloudFront** delivers content from near the user, **AWS Global Accelerator** carries traffic over AWS's network to the best Region, and **Amazon API Gateway** is the managed entrance to your code. The exam asks which one fits a need.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): tasks [3.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.2) and [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [The edge](../03-aws-around-the-world/04-the-edge.md) (edge locations) and [S3 protection, storage classes and lifecycle](../05-storing-data/02-s3-in-practice.md) (private buckets). The bakery is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From lesson 03.04: a colleague says "Route 53 is AWS's CDN." What is wrong with that?

<details><summary>Feedback</summary>

1. **Route 53 is DNS.** It answers "where is this site?" with an address. The content delivery network (CDN) is CloudFront, which keeps copies of content at edge locations.

</details>

## What you'll learn

By the end of this lesson, you can say what each of the four services is for and choose among them for a stated need (objective 07.03a).

Try this before you read on, and guess if you're unsure: an online game sends small, fast messages that aren't web pages, and players want lower lag. Would a CDN that keeps copies of files help?

## The big picture: from a name to an answer

When a customer types `bakery.example`, the browser first asks DNS where the site is, then sends its request there. The four services work at those two moments.

![Route 53 at the edge tells the customer's browser where bakery.example is (steps 1 and 2). CloudFront at a nearby edge location answers the request from its copy (step 3), and fetches from the origin in the Region only when it has none (step 4, dashed). A partner's app calls API Gateway in the Region, which runs Lambda functions (step 5).](../../images/07-03-request-path.svg)

*Notice that steps 1 and 2 only find the way; no page or photo moves yet. Notice too that step 4 is dashed: most photo requests end at the edge.*

**Long description.** Three areas: people, edge locations, and the US East (N. Virginia) Region. 1: the browser asks Route 53, at the edge, where `bakery.example` is. 2: Route 53 answers with an address at CloudFront. 3: the browser sends its request to CloudFront at a nearby edge location. 4, dashed: only without a fresh copy, CloudFront fetches from the origin in the Region, the S3 photo bucket or the web server. 5: a partner's app calls API Gateway in the Region, which runs the Lambda order functions.

## Route 53 answers "where is it?", and it can choose the answer

**Amazon Route 53** is AWS's Domain Name System (DNS) service, the internet's address book. It does three jobs, alone or together: it **registers domain names** such as `bakery.example`, it **answers DNS questions** for your domains, and it **checks the health** of your sites so it can stop sending people to one that fails ([What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)).

When a user could go to more than one place, a **routing policy** tells Route 53 how to choose ([Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)). Each answers one question; four come up most:

- **Failover:** is the main site healthy? If its **health check** fails, Route 53 sends users to the standby, with no person acting ([Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)).
- **Latency:** which Region answers this user fastest?
- **Geolocation:** where is the user, by country or continent?
- **Weighted:** what share goes where, such as 10 in 100 users to a new version?

### "Route 53 is a CDN" is wrong

Some learners think Route 53 delivers content, or balances load. It does neither: it never carries your pages or photos, and only controls which address a user is given. It's tempting because it runs at edge locations and its policies sound like traffic control. CloudFront delivers the content, and a load balancer spreads requests across healthy servers inside one Region. Route 53 picks the place.

## CloudFront delivers from near the user, and keeps the origin out of reach

**Amazon CloudFront** is AWS's content delivery network. Your **distribution** names the **origin**, where the original content lives: an S3 bucket, a web server, a load balancer or a server outside AWS. A nearby edge location answers from its copy if it has one, and fetches from the origin over AWS's network if it doesn't ([What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)). Two more things matter ([Amazon CloudFront FAQs](https://aws.amazon.com/cloudfront/faqs/)):

- **The origin can stay private.** With **origin access control (OAC)**, the photo bucket keeps Block Public Access on, and only your distribution may read it.
- **Protection comes with it.** Every distribution gets AWS Shield Standard at no extra cost, and you can add AWS WAF rules. Module 09 teaches both.

## Global Accelerator gives fixed addresses and a fast path, but keeps no copies

**AWS Global Accelerator** gives your application two **static IP addresses** (IPv4 addresses that don't change; four if you also use IPv6), announced by **anycast** from AWS's edge locations: each user reaches the nearest one. Traffic enters AWS's network there and travels on it to the best healthy endpoint in a Region, such as a load balancer. The addresses stay the same while you move what's behind them ([What is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)).

Global Accelerator and CloudFront both start at the edge, so they're the module's most confused pair. The difference is where the answer comes from.

![Two panels. CloudFront: the nearest edge location keeps copies and answers from them, going to the origin only when it has none. Global Accelerator: two fixed IP addresses at the nearest edge, no copies, and every request carried over AWS's network to a healthy Region.](../../images/07-03-cloudfront-vs-ga.svg)

*Notice the dashed arrow on the left: with CloudFront, many requests end at the edge. On the right, every request goes on to a Region.*

The table gives the same comparison as the image:

| | Amazon CloudFront | AWS Global Accelerator |
|---|---|---|
| Keeps copies? | **Yes**, it's a CDN | **No** |
| Traffic it suits | Web content over HTTP and HTTPS | Any TCP or UDP traffic: games, voice, IoT, or web apps that need fixed addresses |
| Users connect to | A name, such as `bakery.example` | Two fixed IP addresses |
| Choose it when | The same content goes to many people | Every request must reach your application, with fixed addresses or fast failover between Regions |

So the answer to the prequestion is no: the game's moves are fresh every time, so copies don't help. Global Accelerator might.

## API Gateway is the managed entrance to your code

Some requests come from programs, not people: the delivery partner's app asks, "is order 1234 ready?" It uses an **API** (application programming interface), a defined way for one program to ask another for something. **Amazon API Gateway** lets you publish APIs and run them at any scale with no servers of your own. It receives each call, checks who is calling, and hands it to the code behind it, such as a Lambda function ([What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)). **Throttling** caps how fast calls arrive, so a spike doesn't overwhelm your code ([Amazon API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/)).

A load balancer can also pass requests to Lambda functions. The difference is purpose: a load balancer **spreads** traffic across healthy targets; API Gateway **manages an API**: who may call, how often, which version.

> **Your turn:** Pick a service for each need. (a) If the N. Virginia site stops working, customers should reach a copy in Ohio without anyone acting. (b) The same cake photos load slowly for customers on other continents. (c) Each partner developer gets their own key and a monthly limit on calls. (d) Factory machines can store only fixed IP addresses for an application in two Regions.

<details><summary>Model answer</summary>

(a) **Route 53** failover routing, with a health check. (b) **CloudFront:** the same copy can serve many people. (c) **API Gateway:** it manages who may call and how often. (d) **Global Accelerator:** two static IP addresses in front of both Regions.

</details>

## Summary

- **Route 53 answers "where is it?"** It registers domains, answers DNS questions and checks health; routing policies such as failover, latency, geolocation and weighted choose the answer. It is not a CDN and not a load balancer.
- **CloudFront delivers from near the user:** it caches content at edge locations, keeps a bucket private with origin access control, and brings AWS Shield Standard.
- **Global Accelerator gives two fixed addresses and AWS's network to the best Region, with no copies.** Choose CloudFront when a copy can answer.
- **API Gateway is the managed entrance to your code:** who may call, how often, which version. A load balancer spreads traffic; API Gateway manages an API.
- **Your side of the line:** AWS runs these services; you choose the records, what gets cached, who may call your API, and whether the origin stays private.

## Practice

1. **A company runs the same application in two Regions and wants each user sent to whichever Region responds fastest for them. What should it use?**

   - A. Route 53 weighted routing
   - B. Route 53 latency routing
   - C. An Application Load Balancer

   <details><summary>Feedback</summary>

   **B is right.** Latency routing sends each user to the Region with the lowest delay for them.

   - **A is wrong.** Weighted routing splits users by shares you set, regardless of speed.
   - **C is wrong.** A load balancer works inside one Region.

   </details>

2. **Which statement about AWS Global Accelerator is correct?**

   - A. It caches content at edge locations to reduce load on the origin.
   - B. It gives an application fixed IP addresses and carries traffic over AWS's network to healthy endpoints.
   - C. It registers domain names and answers DNS questions.

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** That is CloudFront; Global Accelerator keeps no copies.
   - **C is wrong.** That is Route 53.

   </details>

3. **(From lesson 05.02.) The bakery puts CloudFront in front of its photo bucket. How do customers see the photos while the bucket stays private?**

   - A. Turn off Block Public Access so CloudFront can read the bucket
   - B. Allow only the CloudFront distribution to read the bucket, with origin access control
   - C. Make the bucket public and cache the photos for a short time

   <details><summary>Feedback</summary>

   **B is right.** Origin access control lets the distribution, and only the distribution, read a private bucket.

   - **A is wrong.** CloudFront doesn't need a public bucket; opening it lets anyone bypass CloudFront.
   - **C is wrong.** The cache time doesn't change who can reach the bucket.

   </details>

**Next:** [Connecting networks and offices](04-connecting-networks-and-offices.md).

## Where to check the current details

- [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) and [Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) (checked 2026-10-23)
- [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) and [What is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) (checked 2026-10-23)
- [What is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) (checked 2026-10-23)

---

"Names and the edge" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
