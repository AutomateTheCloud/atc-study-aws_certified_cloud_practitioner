---
type: sim
id: clf-07-06
title: "Simulation S8: Follow a packet and find the rule that blocks it"
tasks: ["3.5", "2.1"]
objectives: ["07.02a", "07.01a"]
reader: "Adult studying alone, possibly new to IT, who has read lessons 07.01 and 07.02 and done Lab 09; about 30 minutes"
prerequisites: ["clf-07-01", "clf-07-02", "clf-07-05"]
terms_introduced: [packet]
pillars: [security]
lab: "S8"
rung: L3-L4
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "30 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
  - "https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"
  - "https://aws.amazon.com/vpc/pricing/"
---

# Simulation S8: Follow a packet through the bakery's network, and find the rule that blocks it

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [07.01 Your own network](01-your-own-network.md) and [07.02 Filtering traffic](02-filtering-traffic.md), and done [Lab 09](05-lab-09-build-a-small-vpc.md). **Time:** about 30 minutes. **Cost:** $0; no AWS account is used.

**Why a simulation:** real traffic needs running servers with public IPv4 addresses ($0.005 an hour each), and updates for a private server need a NAT gateway ($0.045 an hour; US East (N. Virginia), as of 2026-10-24, [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)). Breaking rules on purpose in a live network is also how outages start.

**Goal:** trace five **packets** (the small units data travels in across a network) through the bakery's network, then find the one rule behind each of three support tickets. **End state:** five traces and three fixes in your notes.

**Why this matters:** letting each layer accept only the traffic it needs is [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html). Writing and fixing these rules is the customer's side of the shared responsibility line.

## The rules of this simulation

The network and addresses are made up; how each check behaves is AWS's (Amazon VPC User Guide, checked 2026-10-23).

![The simulation's network: the internet, an internet gateway, and a VPC whose public subnet holds the web server and whose private subnet holds the order database.](../../images/07-06-bakery-network.svg)

*Notice that only the public subnet's route table mentions the internet gateway.*

**Long description.** The internet holds a customer at `192.0.2.44`, a bad range `203.0.113.0/24` and an update site at `192.0.2.200`, all joined to the internet gateway on the edge of the VPC `10.0.0.0/16`. In Availability Zone a, the public subnet `10.0.1.0/24` (network ACL `public-nacl`; routes: local, and `0.0.0.0/0` to the gateway) holds the web server: private address `10.0.1.10`, public IP `198.51.100.20`, security group `web-sg`. The private subnet `10.0.3.0/24` (network ACL `private-nacl`; local route only) holds the order database at `10.0.3.20`, port 5432, security group `db-sg`. AZ b, not drawn, holds the second web server and the database standby in their own pair of subnets.

The checks happen in a fixed order. A security group remembers a connection it allowed and lets the reply through; a network ACL checks every packet, both ways, every time ([network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)).

![The checks a request and its reply pass through, with the network ACL's outbound check on the reply highlighted.](../../images/07-06-checkpoints.svg)

*Notice the thick outline: the reply passes the security group without a rule, but the network ACL checks it again.*

**Long description.** Request in: the internet gateway swaps the public IP for the private one; the route table's local route delivers the packet to the subnet; the network ACL's inbound rules run, lowest number first; the security group's inbound rules, which can only allow, decide; the packet reaches the web server. Reply out: the security group lets the reply out because it remembers the request; the network ACL checks its outbound rules again; the route `0.0.0.0/0` sends it to the internet gateway, which swaps the address back. Between subnets, a packet passes the sender's security group and network ACL, then the receiver's network ACL and security group.

**Network ACLs.** Rules run from the lowest number up; the first match decides; `*` denies anything left.

| ACL | Direction | Rule | Ports (TCP) | Other side | Action |
|---|---|---|---|---|---|
| public-nacl | In | 90 | All traffic | `203.0.113.0/24` | Deny |
| public-nacl | In | 100 | 443 | `0.0.0.0/0` | Allow |
| public-nacl | In | 110 | 1024–65535 | `10.0.0.0/16` | Allow |
| public-nacl | Out | 100 | 1024–65535 | `0.0.0.0/0` | Allow |
| private-nacl | In | 100 | 5432 | `10.0.0.0/16` | Allow |
| private-nacl | Out | 100 | 1024–65535 | `10.0.0.0/16` | Allow |
| both | Both | `*` | All traffic | anywhere | Deny |

**Security groups.** Allow rules only. A new connection a server *starts* is checked against its outbound rules; replies pass automatically ([security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)).

| Group | Inbound | Outbound |
|---|---|---|
| web-sg | TCP 443 from `0.0.0.0/0` | All traffic |
| db-sg | TCP 5432 from web-sg | All traffic |

A computer opening a connection sends from a temporary **ephemeral port**, such as 50000; the reply goes back to it.

## Part 1: follow five packets

### Decision 1: for each packet, list the checks it passes, in order, and name the rule that stops it, if any

| Packet | From | To |
|---|---|---|
| A | A customer, `192.0.2.44`, port 50000 | The shop, `198.51.100.20`, port 443 |
| B | `203.0.113.9`, port 50000 | The shop, port 443 |
| C | The web server, `10.0.1.10`, port 41000 | The database, `10.0.3.20`, port 5432 |
| D | The database, `10.0.3.20` | The update site, `192.0.2.200`, port 443 |
| E | A test server someone added to the public subnet, `10.0.1.50`, with its own security group `test-sg` (all outbound allowed) | The database, port 5432 |

<details><summary>Model answer</summary>

![The checks each of the five packets passes, and the rule that stops B, D and E.](../../images/07-06-trace-grid.svg)

*Notice that each layer stops something different: the network ACL stops B and D, and only the security group can stop E.*

**Long description.** A: the gateway, public-nacl inbound rule 100, web-sg's rule for 443; the reply passes web-sg because it remembers, then public-nacl outbound rule 100 and the route to the gateway; it reaches the customer. B: the gateway, then public-nacl inbound rule 90 denies it. C: web-sg outbound, public-nacl outbound rule 100, the local route, private-nacl inbound rule 100, db-sg's rule for web-sg; the reply passes db-sg, private-nacl outbound rule 100 and public-nacl inbound rule 110. D: db-sg outbound allows it, then private-nacl's `*` rule denies it. E: test-sg, public-nacl outbound rule 100, the local route and private-nacl inbound rule 100 allow it; db-sg stops it.

- **A** gets through. Its reply needs public-nacl's outbound rule 100, because port 50000 is an ephemeral port.
- **B** stops at rule 90, before rule 100 can allow it. A security group couldn't do this: it has no deny rules.
- **C** gets through. Port 5432 falls inside outbound rule 100's range, so no separate rule is needed.
- **D** stops at private-nacl's `*` rule. Even with an allow there, the private route table has no route to the internet, so the packet would go nowhere. The fix is a NAT gateway (billed hourly) or, for AWS services, a VPC endpoint, not a public IP.
- **E** passes both network ACLs, which see only that it comes from inside the VPC. db-sg stops it, because its rule names a security group, not a subnet.

</details>

## Part 2: find the blocking rule

Each ticket follows one change to the tables above. Name the rule that blocks the traffic and the fix.

### Decision 2: "The site times out for everyone since this morning's tidy-up. The server logs show requests arriving."

The change: public-nacl outbound rule 100 now allows TCP **443** only, "because the shop only uses HTTPS".

<details><summary>Model answer</summary>

**public-nacl outbound: the `*` rule now catches every reply.** Requests still get in, which is why the logs show them, but replies go *to* the customer's ephemeral port, not to 443. Restore 1024–65535. The same change also broke packet C. **Return traffic doesn't always pass:** the security group lets it out, but a network ACL checks it again.

</details>

### Decision 3: "We blocked the bad range yesterday, but its requests still reach the shop."

The change: the deny for `203.0.113.0/24` was added as rule **120**, not 90.

<details><summary>Model answer</summary>

**public-nacl inbound rule 100.** It allows 443 from anywhere and comes first, so rule 120 is never reached. Renumber the deny below 100.

</details>

### Decision 4: "The shop loads, but every order page says the database is unavailable."

The change: web-sg's outbound rule "All traffic" was replaced by "TCP 443 to `0.0.0.0/0`", to "tighten things up".

<details><summary>Model answer</summary>

**web-sg outbound.** The web server *starts* the connection to the database, so its outbound rules apply, and port 5432 isn't allowed. Customers still get pages because replies to their requests pass automatically. Add an outbound rule for TCP 5432 to db-sg.

</details>

### Decision 5: the owner asks, "Should we turn on Amazon Inspector to block that bad range?"

<details><summary>Model answer</summary>

No. Amazon Inspector scans EC2 instances, container images and Lambda functions for software vulnerabilities and unintended network exposure, and reports what it finds ([What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)). It blocks nothing. The block belongs in the network ACL, as in Decision 3.

</details>

## Recap

To predict whether traffic passes, walk the checks in order; the first "no" decides. A network ACL runs numbered rules, both ways, on every packet, so replies need their own rules and a deny must come before any matching allow. A security group can only allow, remembers what it let through, and still checks connections its own server starts. A subnet reaches the internet only through a route.

**Next:** the Module 07 mastery check. First, retry the practice questions at the end of [07.01](01-your-own-network.md) and [07.02](02-filtering-traffic.md) without looking back.

---

"Simulation S8: Follow a packet and find the rule that blocks it" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
