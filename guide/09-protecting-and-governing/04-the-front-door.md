---
type: lesson
id: clf-09-04
title: "The front door"
tasks: ["2.4", "2.2"]
objectives: ["09.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 08 and the guardrails primer; about 20 minutes; works on a phone"
prerequisites: [clf-09-03, clf-07-02, clf-07-03, clf-03-04]
terms_introduced: [DDoS attack, network layer attack, application layer attack, AWS Shield Standard, AWS Shield Advanced, Shield Response Team, DDoS cost protection, AWS WAF, web ACL, rate-based rule, SQL injection, AWS Firewall Manager, penetration test]
pillars: [security, reliability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html"
  - "https://aws.amazon.com/shield/pricing/"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html"
  - "https://aws.amazon.com/security/penetration-testing/"
---

# Shield absorbs floods, WAF reads each web request, and Firewall Manager repeats both in every account: choose the layer that fits the attack

Lesson 09.03's services report problems; this lesson's services stop them, at the site's front door. Name the attack, and the protection follows: AWS Shield for floods of traffic, AWS WAF for bad web requests, AWS Firewall Manager for the same rules in many accounts.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.2) and [2.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.4).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Filtering traffic](../07-connecting-it/02-filtering-traffic.md) (security groups and network ACLs) and [Names and the edge](../07-connecting-it/03-names-and-the-edge.md) (Route 53 and CloudFront).

## Warm-up: what you remember

1. From lesson 07.03: name one protection every CloudFront distribution gets at no extra cost.
2. From lesson 03.04: what is an edge location, and why does AWS have so many more of them than Regions?

<details><summary>Feedback</summary>

1. **AWS Shield Standard.** CloudFront also offers AWS WAF rules as an option. This lesson explains both.
2. **A site in AWS's network that serves content and answers requests near users,** for CloudFront and Route 53. There are many so they sit close to people; this lesson uses them to meet floods far from your servers.

</details>

## What you'll learn

By the end of this lesson, you can tell a network flood from an application layer attack, say what Shield Standard, Shield Advanced, WAF and Firewall Manager each give you, and choose protections for an attack type (objective 09.04a).

Try this before you read on, and guess if you're unsure: can a security group stop an attacker typing database commands into the bakery's order form?

## The big picture: three kinds of bad traffic

A **DDoS attack** (distributed denial of service) tries to make a site unavailable by overwhelming it from many machines at once. It comes in two shapes. A **network layer attack** floods the network with raw traffic, such as a SYN flood or UDP reflection (AWS calls these layer 3 and 4). An **application layer attack** uses normal-looking web requests, such as thousands of requests a second for the order page (layer 7). A third problem isn't a flood at all: **SQL injection**, typing database commands into a form field so the site's database runs them. Each needs a different layer: Shield at AWS's edge, WAF on the resource that receives web requests, and security groups and network ACLs around your servers.

## AWS Shield Standard is already protecting every AWS account

**AWS Shield** is AWS's DDoS protection. **AWS Shield Standard** is on for every AWS customer automatically, at no additional charge, and defends against the most common network and transport layer attacks ([AWS Shield Standard overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html), checked 2026-10-24). You turn nothing on. It protects best when your front door is at AWS's edge: AWS says resources reached first through Route 53, CloudFront or Global Accelerator get the fullest protection. So putting CloudFront in front of the whole site is part of DDoS protection.

Shield Standard doesn't read web requests, so an HTTP flood or an SQL injection gets through. There's no one to call, and nothing protects your bill if Auto Scaling launches servers to absorb a flood.

## Shield Advanced adds detection, people and bill protection, for a price

**AWS Shield Advanced** is the paid tier. You subscribe and choose the resources to protect: CloudFront distributions, Route 53 hosted zones, load balancers, Elastic IP addresses and Global Accelerator accelerators ([AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html), checked 2026-10-24). It adds:

- **Automatic application layer mitigation** during request floods, through AWS WAF rules;
- **the Shield Response Team (SRT):** AWS's DDoS experts, around the clock;
- **DDoS cost protection:** credits for the extra charges an attack causes, such as servers Auto Scaling launched;
- **detailed metrics and reports** on attacks against your protected resources.

> **Dated (checked 2026-10-24):** Shield Advanced costs **$3,000 a month with a 1-year subscription**, plus data transfer fees, billed once per payer account ([AWS Shield pricing](https://aws.amazon.com/shield/pricing/)). To use the SRT, AWS's page says you need Shield Advanced **and** the Business Support or Enterprise Support plan ([Managed DDoS event response with SRT support](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html)). Business Support ends on 2027-01-01, replaced by Business Support+, and AWS's pages don't yet say whether Business Support+ qualifies.

### "Any Business Support plan brings the Shield Response Team" is wrong

You may read that a Business Support plan gives you the SRT. That's not right on two counts. The SRT is a Shield Advanced feature, so a Support plan alone, of any level, doesn't bring it. And the plan AWS's page names is the retiring Business Support plan. It's tempting because AWS words the requirement in terms of Support plans, so the SRT looks like a Support plan benefit.

## AWS WAF reads each web request and allows, blocks or challenges it

**AWS WAF** is a web application firewall: it inspects the HTTP and HTTPS requests sent to your site or API, and allows, blocks, counts or challenges each one by rules you set ([AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html), checked 2026-10-24). You attach it to the resource that receives the requests, such as a CloudFront distribution, an Application Load Balancer or an API Gateway REST API, not to an EC2 instance directly. Its rules live in a **web ACL** (web access control list) and can match:

- **addresses and countries:** a set of bad addresses, or countries you don't serve;
- **request content:** SQL injection and cross-site scripting patterns;
- **rate:** a **rate-based rule** limits how many requests one address may send in a time window, the usual answer to a small HTTP flood;
- **managed rule groups:** ready-made rules from AWS or from sellers in AWS Marketplace.

**WAF or a security group?** A security group or network ACL sees only addresses, ports and protocols. WAF reads the request itself: the page, the form fields, the headers. An SQL injection arrives on port 443 like any honest order, passes the security group, and only WAF can see it.

### Firewall Manager applies the same protections in every account

**AWS Firewall Manager** is a central manager, not another firewall. You write a policy once, such as "every load balancer gets this web ACL" or "no security group may allow SSH from anywhere", and it applies the policy across every account in your organization, including accounts created later, and reports what doesn't comply. It manages AWS WAF, Shield Advanced, security groups and network ACLs, and it needs **AWS Organizations** (lesson 09.05) and **AWS Config** ([Firewall Manager prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html), checked 2026-10-24). The bakery has one account, so it doesn't need it yet.

## Choose the protection by the attack, then check the cost

![A grid of six needs against five protections. Network flood: Shield Standard is the main protection, Shield Advanced adds detection, experts and bill protection. Flood of web requests: WAF rate-based rule is main, Shield Advanced adds automatic mitigation. SQL injection or cross-site scripting: WAF managed rule groups. One bad address range: a WAF IP set rule for web traffic or a network ACL deny rule for a subnet. Same rules in every account: Firewall Manager. Expert help and bill protection: Shield Advanced.](../../images/09-04-attack-matrix.svg)

*Notice that WAF appears as the main choice in three rows: most attacks a small website meets are web requests.*

**Long description.** A grid of six needs against five protections: Shield Standard, Shield Advanced, AWS WAF, network ACL or security group, and Firewall Manager; each cell says Main, Adds or No in words. Network flood, such as a SYN flood or UDP reflection: Shield Standard main, automatic; Shield Advanced adds detection, experts and bill protection; the others no. Flood of web requests from many addresses: WAF main, a rate-based rule; Shield Advanced adds automatic mitigation through WAF; network ACL or security group no, can't read requests. SQL injection or cross-site scripting in a form: WAF main, managed rule groups. Requests from one bad address range: WAF main, an IP set rule, for web traffic; network ACL main, a deny rule, for a subnet. The same rules in all of a company's accounts: Firewall Manager main, one policy for all; WAF and network ACLs work one account or VPC at a time. Expert help and bill protection during a big attack: Shield Advanced main, the SRT and cost protection.

For the bakery, the answer is CloudFront in front of the whole site, with a WAF web ACL on it, for about $10 a month in WAF charges at its made-up traffic (as of 2026-10-24, [AWS WAF pricing](https://aws.amazon.com/waf/pricing/)), and no Shield Advanced: a year of it is at least $36,000. A large retailer that loses more than that in an hour offline would decide the other way.

> **Your turn:** Choose the first protection for each, and say why in one sentence. (a) A news site expects floods of page requests during elections and wants experts on call. (b) A shop sees requests with `' OR 1=1 --` in its search box. (c) A bank with 300 accounts must prove every public load balancer has the same web rules.

<details><summary>Model answer</summary>

(a) **Shield Advanced**, with WAF: it adds automatic layer 7 mitigation, the SRT (with a qualifying Support plan) and cost protection. (b) **AWS WAF** with a managed rule group for SQL injection: only WAF reads request content. (c) **Firewall Manager**: one WAF policy applied to every account and checked for compliance, which needs AWS Organizations.

</details>

### Testing your own front door: AWS's penetration-testing policy

A **penetration test** is a planned, authorized attack on your own systems. Under AWS's policy, testing your own resources in listed services, such as EC2, load balancers, RDS, CloudFront and Lambda, needs no approval. Denial-of-service tests, including request flooding, aren't allowed under it, and AWS's own infrastructure is off limits ([AWS penetration testing policy](https://aws.amazon.com/security/penetration-testing/), checked 2026-10-24).

## Summary

- **Shield Standard is automatic and free** for every customer, against common network floods, and strongest with CloudFront, Route 53 and Global Accelerator in front.
- **Shield Advanced is a paid, yearly subscription** that adds automatic layer 7 mitigation, the Shield Response Team and DDoS cost protection. The SRT also needs a qualifying Support plan.
- **AWS WAF reads each web request** and blocks SQL injection, cross-site scripting, request floods and bad addresses; security groups can't read requests. **Firewall Manager** applies WAF, Shield Advanced and security group policies across an organization.
- **Choose by attack:** Shield for volume, WAF for content, Firewall Manager for scale. Shield Standard absorbing a flood doesn't make your WAF rules AWS's job.

## Practice

1. **A company wants protection against SQL injection on its Application Load Balancer. What should it use?**

   A. AWS Shield Standard\
   B. AWS WAF\
   C. A network ACL\
   D. Amazon Inspector

   <details><summary>Feedback</summary>

   **B is right.** WAF reads request content and has managed rules for SQL injection.

   - **A is wrong.** Shield absorbs floods; it doesn't read requests.
   - **C is wrong.** A network ACL sees addresses and ports, not what a request says.
   - **D is wrong.** Inspector reports software vulnerabilities and exposure; it blocks nothing.

   </details>

2. **Which of these does every AWS customer get automatically, at no additional charge?**

   A. AWS Shield Advanced\
   B. The Shield Response Team\
   C. AWS Shield Standard\
   D. DDoS cost protection

   <details><summary>Feedback</summary>

   **C is right.**

   - **A, B and D are wrong.** All three are parts of the paid Shield Advanced subscription; the SRT also needs a qualifying Support plan.

   </details>

3. **A security officer must make sure every account in the company's organization uses the same WAF rules, including accounts created next year. Which service does this?**

   A. AWS Shield Standard\
   B. AWS Firewall Manager\
   C. Amazon GuardDuty\
   D. A security group in each account

   <details><summary>Feedback</summary>

   **B is right.** A Firewall Manager WAF policy applies the rules to matching resources in every account, including new ones. It needs AWS Organizations and AWS Config.

   - **A is wrong.** Shield Standard has no rules to copy; it absorbs floods automatically.
   - **C is wrong.** GuardDuty reports threats; it applies no rules.
   - **D is wrong.** Security groups can't read web requests, and setting them account by account is what the officer wants to avoid.

   </details>

**Next:** [Compliance and governance](05-compliance-and-governance.md).

## Where to check the current details

- [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) and [AWS Shield pricing](https://aws.amazon.com/shield/pricing/) (checked 2026-10-24)
- [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) (checked 2026-10-24)
- [AWS penetration testing policy](https://aws.amazon.com/security/penetration-testing/) (checked 2026-10-24)

---

"The front door" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
