---
type: lesson
id: clf-07-01
title: "Your own network"
tasks: ["3.5", "4.1", "2.1"]
objectives: ["07.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 06 and the guardrails primer; about 15 minutes; works on a phone"
prerequisites: [clf-03-01, clf-03-03, clf-05-05]
terms_introduced: [public IP address, private IP address, Amazon VPC, default VPC, subnet, public subnet, private subnet, route table, route, internet gateway, NAT gateway, Elastic IP address, VPC endpoint, gateway endpoint, interface endpoint]
pillars: [security, reliability, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html"
  - "https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html"
  - "https://aws.amazon.com/vpc/faqs/"
  - "https://aws.amazon.com/vpc/pricing/"
---

# A VPC is your own network inside a Region, and a subnet is public only when its route table sends traffic to an internet gateway

With Amazon Virtual Private Cloud (Amazon VPC) you lay out your own network on AWS: which parts the internet can reach, and how the private parts get out when they must. One rule decides what is public, and it isn't the one most people guess.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): task [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1); [Domain 3, Cloud Technology and Services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html) (34% of the exam): task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5); [Domain 4, Billing, Pricing, and Support](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) (12% of the exam): task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Regions, Availability Zones and data centers](../03-aws-around-the-world/01-regions-availability-zones-data-centers.md) and [Managed or self-managed databases](../05-storing-data/05-managed-or-self-managed-databases.md). The bakery is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From lesson 05.05: where does Amazon RDS put a Multi-AZ standby, and why there?

<details><summary>Feedback</summary>

1. **In a different AZ of the same Region,** so losing the primary's AZ doesn't lose the standby too. The bakery's network needs room for the database in both AZs.

</details>

## What you'll learn

By the end of this lesson, you can name the parts of a VPC and say what each is for, and explain what makes a subnet public (objective 07.01a).

Try this before you read on, and guess if you're unsure: the bakery gives its database server a public IP address. Does that put the database on the internet?

## The big picture: one network, two kinds of subnet

![The bakery's VPC with an internet gateway. Two Availability Zones each hold a public subnet with a web server and a private subnet with the order database. Only the public route table sends 0.0.0.0/0 to the internet gateway.](../../images/07-01-big-picture.svg)

*Notice the highlighted line in the public route table. It is the only difference between the top row of subnets and the bottom row.*

**Long description.** The bakery's VPC in US East (N. Virginia) has an internet gateway on its edge. AZs A and B each hold a public subnet with a web server and a private subnet with the order database (primary in A, standby in B). Internet traffic reaches the public subnets only. The public route table has the local route and, highlighted, 0.0.0.0/0 (every address) to the internet gateway; the private route table has only the local route.

## A VPC is a private network that you lay out inside one Region

A **VPC** is a virtual network that belongs to your account and is isolated from everyone else's, like a company's own network built with settings instead of cables ([How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)). You choose its address range, subnets, route tables and gateways. A VPC belongs to one Region, so the bakery's German site needs its own VPC in Europe (Frankfurt).

- A **subnet** is a slice of the VPC's addresses in **one Availability Zone**; it can't stretch across two ([Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)). High availability needs subnets, and resources, in at least two.
- A **route table** is a list of **routes**, each saying "traffic for these addresses goes to this target". Every subnet uses one, and every route table has a **local** route, so a VPC's subnets can reach each other ([Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)).

Every account has a **default VPC** in each Region, where every subnet is public and every server gets a public IPv4 address ([Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html)). It's handy for a test, but it isn't where an order database belongs. The VPC itself costs nothing; some parts you add bill, and so does data transfer (lesson 07.04).

## A subnet is public because of its route, not because of its addresses

An **internet gateway** connects a VPC to the internet in both directions: your servers can reach out, and people on the internet can start connections in. AWS runs it as a redundant, highly available component, at no charge ([Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html), checked 2026-10-23).

- A **public subnet** is one whose route table has a route to an internet gateway.
- A **private subnet** is one whose route table doesn't.

A route alone doesn't put a server on the internet, though. For IPv4, the server also needs a **public IP address**, one that can be reached across the internet, or an **Elastic IP address** (a public address you reserve and keep). A **private IP address** works only inside the network.

![A two-by-two grid: the subnet's route to the internet gateway by the server's public address. Only a route plus a public address reaches the internet. An address without a route, the common mistake, reaches nothing and still bills.](../../images/07-01-public-or-not.svg)

*Notice that the route decides the row and the address decides the column. Only the top-left cell is on the internet.*

**Long description.** Rows: the subnet has a route to the internet gateway, or not. Columns: the server has a public IPv4 address, or not. Route and address: on the internet, like the web server. Route only: can't use the gateway. Address only, the common mistake: can't reach the internet, and the address costs $0.005 an hour as of 2026-10-24. Neither: private, like the order database.

### "A public IP address makes a subnet public" is wrong

You may have read that a subnet is public if its servers have public addresses. That's wrong: AWS defines a public subnet by its route to an internet gateway, and a server with a public address in a subnet without that route can't talk to the internet at all. People believe it because in the default VPC the two always come together. So the answer to the prequestion is no, though the address still bills: as of 2026-10-24, every public IPv4 address, in use or idle, costs **$0.005 an hour** in US East (N. Virginia) ([Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)).

## A NAT gateway lets private servers reach out, never the internet reach in, and it bills by the hour

Sometimes a private server must start a conversation with the internet, for example to download updates. A **NAT gateway** (network address translation) lets it without making the subnet public: the private subnet's route table sends internet traffic to the NAT gateway, which sends it out and passes the replies back. Nobody on the internet can start a connection in through it ([NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)).

The two gateways side by side (prices for US East (N. Virginia), as of 2026-10-24):

| | Internet gateway | NAT gateway |
|---|---|---|
| **Who can start a connection** | Either side | Only your servers, from inside |
| **Cost** | No charge | $0.045 an hour and $0.045 per GB processed, plus its Elastic IP address |

### "A NAT gateway is free" is wrong

You may have read that NAT gateways are free, like internet gateways. They aren't: AWS charges for every hour one exists and every GB it processes ([Pricing for NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html)), about $33 a month before any data. It's tempting because both are called gateways and sit in the same route tables.

The classic (**zonal**) NAT gateway sits in a public subnet in one AZ, with an Elastic IP address; a newer **Regional NAT gateway** expands into each AZ where you have workloads ([Regional NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html), checked 2026-10-24).

## VPC endpoints reach AWS services without the internet, and one kind is free

A private server often needs an AWS service, not the internet: the bakery's servers save cake photos to S3. A **VPC endpoint** gives the VPC a private path to the service, with no internet gateway or NAT gateway ([Amazon VPC FAQ](https://aws.amazon.com/vpc/faqs/)).

| | Gateway endpoint | Interface endpoint |
|---|---|---|
| **Services** | Amazon S3 and Amazon DynamoDB only | Many AWS services, and services others publish |
| **How it attaches** | A route in your route table | A private IP address in your subnet |
| **Built on AWS PrivateLink?** | No | Yes |
| **Cost** | No charge | Hourly in each AZ, plus per GB |

From [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html), checked 2026-10-23.

> **Your turn:** The bakery's private servers send 200 GB of photos a month to S3 through a NAT gateway. Which change removes the NAT gateway's charge on that traffic: an interface endpoint for S3, a gateway endpoint for S3, or moving the NAT gateway to the other AZ?

<details><summary>Model answer</summary>

**A gateway endpoint for S3:** it has no charge, and the photos stop passing through the NAT gateway. An interface endpoint would avoid the NAT gateway too, but it bills. Moving the NAT gateway changes nothing it charges.

</details>

## Summary

- **A VPC is your own isolated network in one Region,** at no charge. Each subnet sits in one AZ, so high availability needs subnets in at least two.
- **A subnet is public only because its route table points to an internet gateway.** A public address in a private subnet does nothing, yet still bills.
- **A NAT gateway lets private servers start connections out, never in,** and bills by the hour and per GB; the internet gateway is free.
- **VPC endpoints reach AWS services privately:** gateway endpoints (S3, DynamoDB) are free; interface endpoints (PrivateLink) bill.
- **Your side of the line:** AWS runs the network and keeps VPCs isolated; you design the subnets, routes and gateways. A database in a public subnet is the customer's mistake.

## Practice

1. **Which route target makes a subnet a public subnet?**

   - A. A NAT gateway
   - B. An internet gateway
   - C. A gateway endpoint

   <details><summary>Feedback</summary>

   **B is right.** A route to an internet gateway defines a public subnet.

   - **A is wrong.** A NAT gateway is how a *private* subnet reaches out; it stays private.
   - **C is wrong.** A gateway endpoint reaches S3 or DynamoDB, not the internet.

   </details>

2. **Servers in a private subnet must download patches from the internet, and nobody on the internet may start a connection to them. What should the company add?**

   - A. A route from the private subnet to the internet gateway
   - B. A public IPv4 address on each server
   - C. A NAT gateway, with a route to it from the private subnet

   <details><summary>Feedback</summary>

   **C is right.** A NAT gateway lets private servers start connections out and refuses connections from outside.

   - **A is wrong.** That makes the subnet public.
   - **B is wrong.** Without a route to an internet gateway, an address gives no path, and it bills.

   </details>

3. **(From lesson 03.03.) The bakery's VPC has subnets in two AZs of one Region. Does that protect it against losing the whole Region?**

   - A. Yes, because the subnets are in two AZs
   - B. No: that needs copies in another Region
   - C. Yes, because a VPC spans every Region

   <details><summary>Feedback</summary>

   **B is right.** Two AZs give high availability inside the Region; surviving a Region's loss is disaster recovery.

   - **A is wrong.** Both AZs are in the same Region.
   - **C is wrong.** A VPC belongs to one Region.

   </details>

**Next:** [Filtering traffic](02-filtering-traffic.md). To build a small VPC yourself at no cost, try [Optional lab 09](05-lab-09-build-a-small-vpc.md); the exam doesn't need it.

## Where to check the current details

- [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html), Amazon VPC User Guide (checked 2026-10-23)
- [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/): NAT gateways and public IPv4 addresses (checked 2026-10-24)
- [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html): gateway and interface endpoints (checked 2026-10-23)

---

"Your own network" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
