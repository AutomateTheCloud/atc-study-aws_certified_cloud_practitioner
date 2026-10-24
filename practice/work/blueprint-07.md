# Blueprint: Module 07, Connecting it: networks and the edge

Items file: `practice/items/07-connecting-it.yaml`. Targets: about 75 questions (about 15 "Select
TWO") and 18 concept cards. Exam tasks: 3.5 (networking), the edge parts of 3.2, the data transfer
parts of 4.1, and 2.1 where a lesson has a "Your side of the line" section. No prices are tested.

The module has four objectives, one per lesson, so the table breaks each objective into the
sections that teach it. The lab (05) and the simulation (06) serve 07.01a and 07.02a.

Counts are the actual ones in the items file (Q = questions, M = how many of them are "Select TWO",
C = concept cards). Levels: Re recall, Un understanding, Ap application.

## 07.01a Explain what makes a subnet public [C·An] (lesson 07.01, task 3.5; 4.1 and 2.1 in part)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 01, "A VPC is a private network that you lay out inside one Region" | A VPC is in one Region; the default VPC is all public | Un | 2 | 0 | 1 |
| 01, "Each subnet sits in one Availability Zone, so you build them in pairs" | One AZ per subnet; HA needs subnets in two AZs | Ap | 1 | 0 | 1 |
| 01, "A route table decides where traffic leaving a subnet goes" | Route table's job; local route; most specific route wins | Re, Ap | 2 | 0 | 1 |
| 01, "A subnet is public because of its route, not because of its addresses" | Route to an internet gateway defines public; a public address is also needed; an address alone does nothing | Re, Ap | 3 | 1 | 0 |
| 01, ""A public IP address makes a subnet public" is wrong" | The misconception | — | 0 | 0 | 1 |
| 01, "A NAT gateway lets private servers reach out, never the internet reach in, and it bills by the hour" | NAT for outbound only; placement and route; IGW vs NAT | Un, Ap | 3 | 1 | 1 |
| 01, ""A NAT gateway is free" is wrong" | NAT bills hourly and per GB (no rates); one per AZ | Un | 2 | 0 | 1 |
| 01, "VPC endpoints reach AWS services without the internet, and one kind is free" | Gateway vs interface endpoint; DynamoDB via gateway endpoint; SQS via interface endpoint | Re, Ap | 3 | 1 | 1 |
| 01, "What you pay for" | Which VPC parts have no charge (not the prices) | Re | 1 | 1 | 0 |
| 01, "Your side of the line" | Network design is the customer's | Un | 1 | 0 | 0 |
| 05 (Lab 09), "Part A: build the network" | An attached gateway alone makes no subnet public | Ap | 1 | 0 | 0 |
| **Total 07.01a** | | | **19** | **4** | **7** |

## 07.02a Predict whether traffic passes [P·An] (lesson 07.02, task 3.5; Sim S8)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 02, "A security group allows traffic to a resource and remembers each conversation" | Allow-only; new group's defaults; group as source; SSH to the world is a bad practice | Re, Un, Ap | 5 | 1 | 2 |
| 02, "A network ACL checks every packet entering or leaving a subnet, in number order" | Blocking a range; first match by number; renumbering a deny; default vs custom | Re, Ap | 4 | 1 | 1 |
| 02, "A security group lets replies through on its own; a network ACL checks them again" | Stateful replies; a custom network ACL drops replies | Un, Ap | 2 | 0 | 1 |
| 02, ""Return traffic always gets through" is wrong" | The misconception | Un | 1 | 0 | 0 |
| 02, "Security group or network ACL: use both, for different jobs" | The two filters side by side | Un | 1 | 1 | 0 |
| 02, "Predict whether traffic passes by walking the path" | Order of checks; the route comes first | Un, Ap | 2 | 0 | 1 |
| 02, "Worked example: four requests to the bakery" | The outbound rule for replies | — | 0 | 0 | 1 |
| 02, "Amazon Inspector finds open paths; it doesn't block anything" | Inspector reports, Flow Logs record, neither blocks | Un, Ap | 2 | 1 | 0 |
| 06 (Sim S8), Decisions 1 and 4 | Outbound rules apply to connections a server starts; a group-named source stops other servers | Ap | 2 | 0 | 0 |
| **Total 07.02a** | | | **19** | **4** | **6** |

## 07.03a Choose Route 53, CloudFront, Global Accelerator or API Gateway for a need [C·Ap] (lesson 07.03, tasks 3.5 and 3.2)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 03, "Route 53 answers "where is it?", and it can choose the answer" | What Route 53 does; not a CDN; alias record; TTL delays a switch | Re, Un | 4 | 0 | 0 |
| 03, "A routing policy picks the answer" | Failover, geolocation, weighted, latency plus health checks | Ap | 4 | 1 | 2 |
| 03, "CloudFront delivers from near the user, and keeps the origin out of reach" | OAC; invalidation; what CloudFront brings | Re, Ap | 3 | 1 | 0 |
| 03, "Global Accelerator gives fixed addresses and a fast path, but keeps no copies" | UDP game; fixed addresses; CloudFront vs Global Accelerator | Un, Ap | 3 | 0 | 1 |
| 03, "API Gateway is the managed entrance to your code" | Keys and usage plans; throttling; API Gateway vs load balancer | Un, Ap | 3 | 1 | 0 |
| 03, "Choose by what the need is really about" | One copy, many users: CloudFront | Ap | 1 | 0 | 0 |
| 03, "Your side of the line" | What the customer decides at the edge | Un | 1 | 0 | 0 |
| **Total 07.03a** | | | **19** | **3** | **3** |

## 07.04a Choose a link by private, encrypted and setup speed [J·Ap] (lesson 07.04, tasks 3.5 and 4.1)

| Page and section | What is tested | Levels | Q | M | C |
|---|---|---|---|---|---|
| 04, "A Site-to-Site VPN links an office network over the internet, encrypted" | Quick encrypted office link; tunnels | Re, Ap | 2 | 1 | 0 |
| 04, ""A VPN is a private connection" is wrong" | Encrypted is not private | Un | 1 | 0 | 1 |
| 04, "Client VPN connects people, not networks" | Remote people; Site-to-Site vs Client VPN | Un, Ap | 2 | 0 | 0 |
| 04, "Direct Connect is a dedicated line that bypasses the internet" | Private and consistent; adding encryption; VPN as backup | Ap | 3 | 1 | 0 |
| 04, "Peering, Transit Gateway and PrivateLink connect networks inside AWS" | Not transitive; no overlap; hub for many; one service | Un, Ap | 5 | 1 | 1 |
| 04, "Data in is free; across, between and out usually costs" | Free and charged directions; cross-AZ cost; hourly link charges (no prices) | Re, Un | 4 | 1 | 0 |
| 04, "Your side of the line" | Customer gateway device and both tunnels are the customer's | Un | 1 | 0 | 0 |
| **Total 07.04a** | | | **18** | **4** | **2** |

## Totals

75 questions (60 single, 15 "Select TWO"); 18 concept cards.

Question levels: 13 recall (17%), 26 understanding (35%), 36 application (48%). This leans further
toward application than the 20/50/30 target, on purpose: all four of this module's objectives are
at the analyze or apply level (predict whether traffic passes, choose a service or link for a
need), so most items describe a situation and ask for a decision.

By task: 3.5 59, 3.2 7, 4.1 6, 2.1 3. Correct single answers sit 15 times in each of positions A to
D.

Left out on purpose: prices of every kind (NAT gateway, public IPv4, links, data transfer rates);
Direct Connect port speeds and the VPN tunnel bandwidth; Route 53's geoproximity, IP-based and
multivalue policies (named in a table only); Accelerated Site-to-Site VPN; AWS Network Firewall
(out of scope for the exam); CloudFront flat-rate plans.
