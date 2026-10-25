---
type: lesson
id: clf-07-04
title: "Connecting networks and offices"
tasks: ["3.5", "4.1", "2.1"]
objectives: ["07.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 06, the guardrails primer and lessons 07.01 to 07.03; about 15 minutes; works on a phone"
prerequisites: [clf-07-01, clf-07-02, clf-07-03, clf-05-04, clf-03-03]
terms_introduced: [on-premises network, encryption in transit, AWS Site-to-Site VPN, AWS Client VPN, AWS Direct Connect, VPC peering, transitive, AWS Transit Gateway, hub and spoke, AWS PrivateLink, data transfer]
pillars: [reliability, performance-efficiency, security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"
  - "https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html"
  - "https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html"
  - "https://aws.amazon.com/directconnect/faqs/"
  - "https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html"
  - "https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html"
  - "https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json"
---

# Choose a link by three questions: is the path private, is the traffic encrypted, and how soon do you need it?

The bakery's head office, the owner's laptop, a second VPC in Europe and a partner's service all need to reach the bakery's VPC. AWS offers a link for each, and they differ on who connects, whether the path avoids the public internet, whether it's encrypted, and how fast you can set it up. AWS also bills the data they carry by direction.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Your own network](01-your-own-network.md) and [Hybrid storage and backup](../05-storing-data/04-hybrid-storage-and-backup.md). The bakery is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From Module 06: which service puts AWS-managed racks or servers in a customer's own building, and what links it to its Region?

<details><summary>Feedback</summary>

1. **AWS Outposts,** through its **service link**, a network connection. Getting a building's network to AWS is this lesson's subject.

</details>

## What you'll learn

By the end of this lesson, you can choose a link by whether it's private, encrypted and quick to set up (objective 07.04a), and say which directions of data transfer cost money.

Try this before you read on, and guess if you're unsure: a VPN from an office to AWS encrypts everything it carries, over the internet. Is it a private connection?

## The big picture: two families of links

Three links connect **people or places outside AWS** to a VPC: Site-to-Site VPN, Client VPN and Direct Connect. Three connect **networks inside AWS**: VPC peering, Transit Gateway and PrivateLink.

![Map of the bakery's networks. The head office and the owner at home sit outside AWS; the site VPC, a German VPC and a partner's service sit inside it. Site-to-Site VPN and Client VPN cross the public internet; Direct Connect goes around it. VPC peering joins the two VPCs, and PrivateLink reaches the partner's one service.](../../images/07-04-connection-map.svg)

*Notice which lines cross the internet band and which go around it. That single detail decides whether a link is private.*

**Long description.** Left, outside AWS: the head office and the owner's laptop. Middle: the public internet. Right, inside AWS: the German VPC, the site VPC and a partner's service in its own account. Site-to-Site VPN (from the office) and Client VPN (from the laptop) cross the internet to the site VPC. Direct Connect runs from the office around the internet, through a Direct Connect location. VPC peering joins the two VPCs; PrivateLink reaches the partner's one service.

## A Site-to-Site VPN links an office network over the internet, encrypted

**AWS Site-to-Site VPN** connects a whole **on-premises network** (one in a building you run, such as the bakery's head office) to a VPC. It builds encrypted tunnels across the public internet between your office router and AWS, two per connection for high availability ([What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)). AWS says VPN connections can be configured in minutes, and suit an immediate need with modest bandwidth ([AWS Direct Connect FAQs](https://aws.amazon.com/directconnect/faqs/)).

**AWS Client VPN** is for individual people: the owner at home, staff on the road. Each person runs a VPN client app and connects, encrypted over the internet, to the VPC ([What is AWS Client VPN?](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)). **Site-to-Site joins two networks** through a router; **Client VPN joins one device**.

### "A VPN is a private connection" is wrong

You may read that a VPN gives you private connectivity to AWS. That's not right. A VPN is **encrypted** (**encryption in transit** scrambles data while it travels), but its traffic crosses the **public internet**, and its speed varies with the internet's. The mix-up is tempting because "VPN" stands for virtual *private* network. In networking questions, **private is about the path; encrypted is about the protection.** So the answer to the prequestion is no.

![A two-by-two grid: over the public internet or private, by encrypted or not. AWS VPN, both kinds, is encrypted but not private (highlighted). Direct Connect on its own is private but not encrypted unless you add it. Direct Connect plus MACsec or a VPN over it is both.](../../images/07-04-private-vs-encrypted.svg)

*Notice that both kinds of AWS VPN sit in the left column: encrypted, yet on the internet's path. Only Direct Connect is in the private column.*

**Long description.** Columns: over the internet, or private. Rows: encrypted, or not unless you add it. Top left, highlighted: AWS VPN, both kinds. Top right: Direct Connect plus MACsec on supported connections, or a VPN over it. Bottom left: plain internet traffic, not a connection option. Bottom right: Direct Connect alone.

## Direct Connect is a dedicated line that bypasses the internet

**AWS Direct Connect** joins your network to AWS over a dedicated cable at a Direct Connect location. The traffic never passes through internet providers, so it's **private**, with more consistent performance than internet links ([What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)). Setup is physical work, so it takes longer than a VPN's minutes. Encryption is something you add, such as a VPN run over the connection, and a VPN over the internet is a common, cheaper backup.

| | Site-to-Site VPN | Client VPN | Direct Connect |
|---|---|---|---|
| **Who connects** | A whole network | One person's device | A whole network |
| **Path** | Public internet | Public internet | Private line |
| **Encrypted?** | Yes | Yes | Only if you add it |
| **Setup** | Minutes | A managed endpoint; each person installs an app | Longer: physical work |
| **Clue in a question** | "quickly", "encrypted", "backup for Direct Connect" | "remote employees" | "consistent performance", "doesn't use the internet" |

## Peering, Transit Gateway and PrivateLink connect networks inside AWS

These three stay on AWS's network and differ in how much they connect: two whole networks, many, or one service.

- **VPC peering** joins two VPCs so they talk over private addresses, across accounts and Regions. It is **not transitive**: if A is peered with B and B with C, A can't reach C through B. And the two VPCs' address ranges must not overlap ([How VPC peering connections work](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html)).
- **AWS Transit Gateway** is a **hub**: each VPC, VPN or Direct Connect link (through a Direct Connect gateway) attaches to it once, and its route tables decide which networks reach which ([What is AWS Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)). That's a **hub and spoke** design: twenty VPCs need twenty attachments, where a full mesh of peering would need 190 connections.
- **AWS PrivateLink** connects a VPC to **one service**, not a whole network, through an interface endpoint (lesson 07.01): an AWS service, a partner's product, or another team's application ([What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)).

> **Your turn:** Choose a link for each of the bakery's needs. (a) The head office needs an encrypted link to the site VPC this week; traffic is modest. (b) The owner wants to reach the order system from home. (c) The site VPC must talk to the German VPC both ways. (d) The web server must use a partner's tracking service without joining the two networks.

<details><summary>Model answer</summary>

(a) **Site-to-Site VPN:** a whole network, encrypted, set up in minutes; Direct Connect later if traffic grows. (b) **Client VPN:** one person's device. (c) **VPC peering:** two VPCs, if their address ranges don't overlap; Transit Gateway only once there are many networks. (d) **PrivateLink:** one service, not a network.

</details>

## Data in is free; across, between and out usually costs

AWS bills **data transfer** by direction (task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1)). Learn the pattern, not the prices: data **in** from the internet is free, and so is data inside one Availability Zone over private addresses. Data **out** to the internet, **between Regions** and **across Availability Zones** is charged per GB.

| Direction, from US East (N. Virginia) | US dollars per GB |
|---|---|
| In from the internet | 0.00 |
| Between resources in the same AZ, private addresses | 0.00 |
| From S3 to CloudFront | 0.00 |
| Across AZs in the Region | 0.01 charged on each side |
| To another Region | 0.02 to most Regions; 0.01 to US East (Ohio) |
| Out to the internet, first 10 TB a month | 0.09, after 100 GB a month free across all Regions |
| Processed by a NAT gateway (adds to the above) | 0.045 |

> **Dated (checked 2026-10-23):** from AWS's [data transfer price list](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json) (published 2026-09-16) and the [EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) page; NAT gateway as of 2026-10-24. Rates differ by Region, and outbound rates fall as volume grows.

**"Only data out to the internet costs money" is wrong.** Data between Regions and across AZs is charged too, so a multi-AZ or multi-Region design pays a little for every copy it keeps in step. The mistake is tempting because data out to the internet is usually the biggest item.

## Summary

- **Site-to-Site VPN links a network over the internet, encrypted,** in minutes; **Client VPN** does the same for one person's device. Both are encrypted, **not private**.
- **Direct Connect is a dedicated line that bypasses the internet:** private and consistent, slower to set up, with encryption added when needed and a VPN as a cheaper backup.
- **Peering joins two VPCs and isn't transitive; Transit Gateway is a hub for many; PrivateLink exposes one service.**
- **Data in is free; across AZs, between Regions and out to the internet costs.**
- **Your side of the line:** AWS runs the links; you own your end of each, who may connect, encryption on Direct Connect, and the routes and filters that still decide what passes.

## Practice

1. **A company needs a connection from its data center to AWS this week. Its traffic is modest and must be encrypted. Which option fits best?**

   - A. AWS Direct Connect
   - B. AWS Site-to-Site VPN
   - C. AWS Client VPN

   <details><summary>Feedback</summary>

   **B is right.** It connects a network, encrypted, and can be configured in minutes.

   - **A is wrong.** Direct Connect needs physical work, and isn't encrypted unless you add it.
   - **C is wrong.** Client VPN connects individual devices.

   </details>

2. **VPC A is peered with VPC B, and VPC B with VPC C. Can A reach C?**

   - A. Yes, through B
   - B. No: peering isn't transitive, so A needs its own link to C, or all three attach to a transit gateway
   - C. Only if all three are in the same Region

   <details><summary>Feedback</summary>

   **B is right.** Traffic can't pass through a peered VPC to a third one.

   - **A is wrong.** That is exactly what peering doesn't allow.
   - **C is wrong.** The Region doesn't change it; peering works across Regions too.

   </details>

3. **Which data transfer is free, at the prices in this lesson?**

   - A. 1 GB from a web server to a database in another AZ
   - B. 1 GB uploaded from the internet to an S3 bucket
   - C. 1 GB copied to another Region

   <details><summary>Feedback</summary>

   **B is right.** Data in from the internet has no transfer charge.

   - **A is wrong.** Across AZs is charged on each side.
   - **C is wrong.** Between Regions is charged per GB.

   </details>

**Next:** the [Module 07 mastery check](07-check.md). To build a small VPC at no cost, try [Optional lab 09](05-lab-09-build-a-small-vpc.md).

## Where to check the current details

- [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) and [What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) (checked 2026-10-23)
- [How VPC peering connections work](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html) and [What is AWS Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) (checked 2026-10-23)
- [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/): data transfer (checked 2026-10-23)

---

"Connecting networks and offices" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
