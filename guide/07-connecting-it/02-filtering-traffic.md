---
type: lesson
id: clf-07-02
title: "Filtering traffic"
tasks: ["3.5", "2.1", "2.2"]
objectives: ["07.02a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 06, the guardrails primer and lesson 07.01; about 15 minutes; works on a phone"
prerequisites: [clf-07-01, clf-04-01]
terms_introduced: [inbound rule, outbound rule, security group, network ACL, stateful, stateless, Amazon Inspector, VPC Flow Logs]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html"
  - "https://aws.amazon.com/vpc/faqs/"
  - "https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"
---

# Security groups guard each resource and remember each conversation; network ACLs guard each subnet and check every packet both ways

Lesson 07.01 decided where traffic can go; this lesson decides which traffic may pass. A VPC has two filters, a **security group** around each resource and a **network ACL** at the edge of each subnet, and the exam asks you to tell them apart.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Your own network](01-your-own-network.md) and [Security of vs in the cloud](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md). The bakery is in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From lesson 04.01: on EC2, who writes the security group rules for the bakery's web server, AWS or the bakery?

<details><summary>Feedback</summary>

1. **The bakery.** AWS provides the security group; configuring its rules is on the customer's side of the line. The same holds for network ACLs.

</details>

## What you'll learn

By the end of this lesson, you can tell security groups and network ACLs apart and predict whether traffic passes them (objective 07.02a), and say what Amazon Inspector does.

Try this before you read on, and guess if you're unsure: can a security group block one bad IP address while letting everyone else in?

## The big picture: two checkpoints in, two checkpoints out

A customer's request crosses the subnet's network ACL, then the web server's security group. The reply crosses both again, and they treat it differently.

![A customer's request passes the network ACL at the subnet's edge (check 1) and the security group around the web server (check 2). The reply passes the security group automatically (check 3) and is checked again by the network ACL (check 4, highlighted).](../../images/07-02-packet-path.svg)

*Notice check 4. The security group lets the reply out because it remembers the request; the network ACL doesn't remember, so it checks the reply like any other packet.*

**Long description.** A customer's HTTPS request enters the bakery's public subnet through the internet gateway. Check 1: a network ACL inbound rule must allow it. Check 2: a security group inbound rule must allow it. Check 3: the security group lets the reply out automatically (stateful). Check 4, highlighted: a network ACL outbound rule must allow the reply, which goes to a high-numbered port on the customer's computer (stateless).

## A security group allows traffic to a resource and remembers each conversation

A **security group** is a virtual firewall for the resources you attach it to, such as an EC2 instance or an RDS database: only traffic its rules allow reaches them ([Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)). **Inbound rules** cover traffic arriving; **outbound rules** cover traffic leaving.

- **Allow rules only.** You can't write a deny rule; anything no rule allows is refused.
- **A new security group** allows nothing in and everything out.
- **It's stateful.** If a request was allowed in, its reply goes out whatever the outbound rules say.
- **A rule's source can be another security group,** meaning "anything attached to that group".

The bakery's database group, `db-sg`, allows the database port only from `web-sg`, the web servers' group. When Auto Scaling adds a web server with a new address, the rule still covers it.

## A network ACL checks every packet entering or leaving a subnet, in number order

A **network ACL** (network access control list) filters traffic at the edge of a subnet. Every subnet has exactly one ([Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), checked 2026-10-23). It differs from a security group in three ways:

- **Allow and deny.** Each rule either allows or denies.
- **Numbered, first match wins.** AWS checks the rules from the lowest number up and applies the first one that matches. A final catch-all rule denies anything left.
- **It's stateless.** It doesn't remember requests, so replies need a rule of their own.

A VPC's **default network ACL allows all traffic** in and out, so the layer does nothing until you change it; a **custom network ACL** you create denies everything until you add rules. AWS's advice: security groups are the main control, and network ACLs a second, coarse layer, for example to deny a specific range of addresses ([Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)).

That is the owner's second request. Thousands of failed logins come from one block of addresses; a security group can't help, because it has no deny rule. A network ACL rule that denies that range, numbered below the rule that allows HTTPS, can. So the answer to the prequestion is no.

### "Return traffic always gets through" is wrong

You may have read that replies are always allowed back, because security groups are stateful. They aren't always. The security group lets the reply through, but the reply still crosses the subnet's network ACL, which is stateless. The default network ACL allows everything, so you never notice; a custom one whose outbound rules don't allow the reply drops it, and the site looks down. The belief is easy to pick up because "stateful" sounds like a property of the whole VPC. It's a property of the security group only.

## Security group or network ACL: use both, for different jobs

![Two columns compared. Security group: each resource, allow only, all rules together, replies allowed automatically (stateful, highlighted), the main control. Network ACL: a whole subnet, allow and deny, in number order, replies checked again (stateless, highlighted), a second layer.](../../images/07-02-sg-vs-nacl.svg)

*Notice the highlighted row. Most wrong answers about these two come from mixing up who remembers the conversation.*

The table gives the same comparison as the image ([Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)):

| | Security group | Network ACL |
|---|---|---|
| **Guards** | A resource (instance level) | A subnet (subnet level) |
| **Rules** | Allow only | Allow and deny |
| **Checking** | All rules together | Number order, first match wins |
| **Replies** | Allowed automatically (stateful) | Must be allowed (stateless) |
| **When created** | Nothing in, everything out | Default: everything; custom: nothing |
| **Use it for** | The main control on every resource | A second layer, such as denying a range |
| **Cost** | No charge | No charge |

> **Your turn:** For each need, choose a security group or a network ACL. (a) Only the web servers may reach the database. (b) Block a range of attack addresses from a whole subnet. (c) Let a web server's replies out with no rule written for them.

<details><summary>Model answer</summary>

(a) **Security group:** `db-sg` allows the database port from `web-sg`. (b) **Network ACL:** only it has deny rules, and it covers the whole subnet. (c) **Security group:** it's stateful. A network ACL is stateless, so replies need an outbound rule there.

</details>

## Amazon Inspector finds open paths; it doesn't block anything

The exam lists **Amazon Inspector** under security in a VPC (task [3.5](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html#cloud-practitioner-02-task3.5)), but it isn't a third filter. Inspector is a vulnerability management service: it scans EC2 instances, container images in Amazon ECR and Lambda functions for software vulnerabilities and **unintended network exposure**, such as a server reachable from the internet on a port nobody meant to open, and reports each as a finding ([What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html), checked 2026-10-23). It changes nothing: you fix the rule. Old material describes "assessment templates" and an agent; that was Amazon Inspector Classic, which AWS shut down on 2026-05-20.

Three neighbors to keep apart:

- **VPC Flow Logs** record information about the traffic to and from your network interfaces ([Amazon VPC FAQ](https://aws.amazon.com/vpc/faqs/)). They record; they don't block.
- **AWS WAF** filters web requests to sites and APIs (Module 09).
- **AWS Network Firewall** is out of the exam's scope; as an answer, it's most likely a distractor.

## Summary

- **A security group guards a resource:** allow rules only, all checked together, and stateful, so replies pass on their own. A rule can name another security group as its source.
- **A network ACL guards a subnet:** allow and deny rules, checked in number order, ending in a catch-all deny, and stateless, so replies need their own rule. The default one allows everything.
- **To block an address range, use a network ACL deny rule.** Security groups can't deny.
- **Return traffic doesn't always get through:** the security group passes it, but a custom network ACL can drop it.
- **Amazon Inspector reports unintended network exposure; it filters nothing.** Both filters are free, and both are yours to configure.

## Practice

1. **Which statement about security groups is correct?**

   - A. They support allow and deny rules
   - B. They are stateful: replies to allowed traffic are allowed automatically
   - C. They apply to a whole subnet

   <details><summary>Feedback</summary>

   **B is right.**

   - **A is wrong.** Security groups have allow rules only; network ACLs have both.
   - **C is wrong.** That's a network ACL.

   </details>

2. **What does Amazon Inspector do for network security in a VPC?**

   - A. It blocks traffic that matches known attacks
   - B. It scans workloads and reports unintended network exposure as findings
   - C. It records information about the traffic in the VPC

   <details><summary>Feedback</summary>

   **B is right.** Inspector finds and reports; you change the rules.

   - **A is wrong.** Inspector doesn't filter traffic; for web requests, AWS WAF does.
   - **C is wrong.** That's VPC Flow Logs.

   </details>

3. **(From lesson 07.01.) A server in a private subnet has a security group allowing HTTPS from anywhere. Can customers on the internet reach it?**

   - A. Yes, because the security group allows it
   - B. No, because the subnet has no route to an internet gateway
   - C. Only if the network ACL also allows it

   <details><summary>Feedback</summary>

   **B is right.** Without a route to an internet gateway, nothing from the internet can come in, before any filter gets to decide.

   - **A is wrong.** A security group only decides among traffic that can reach the server.
   - **C is wrong.** No filter setting creates a missing route.

   </details>

**Next:** [Names and the edge](03-names-and-the-edge.md). To write these rules yourself, try [Optional lab 09](05-lab-09-build-a-small-vpc.md).

## Where to check the current details

- [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) and [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), Amazon VPC User Guide (checked 2026-10-23)
- [Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html): the comparison of the two (checked 2026-10-23)
- [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) and [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/) (checked 2026-10-23)

---

"Filtering traffic" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
