---
type: check
id: clf-07-07
title: "Module 07 mastery check"
tasks: ["3.5", "3.2", "4.1", "2.1"]
objectives: ["07.01a", "07.02a", "07.03a", "07.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the lessons of Module 07; about 30 minutes for each check"
prerequisites: [clf-07-01, clf-07-02, clf-07-03, clf-07-04]
pillars: [security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# Module 07 mastery check: read a network, predict a packet, and choose the right link

This check tests the four objectives of Module 07: explaining what makes a subnet public, predicting whether traffic passes the filters, choosing among Route 53, CloudFront, Global Accelerator and API Gateway, and choosing a link by whether it's private, encrypted and quick to set up.

**For:** an adult studying alone, possibly new to IT, who has finished the lessons of [Module 07](00-brief.md). **Time:** about 30 minutes for Check A, and the same for Check B if you need it. Several items describe a network's rules; read each rule carefully, and sketch the path on paper if that helps.

## How to use this check

Take **Check A** closed-book: no lessons, no notes, no searching. Answer all 12 items before you open any answer. **The threshold is 80%,** which is 10 of 12.

- **If you score below 10,** use the [correction map](#correction-map) for each item you missed: reread the section it names, try the other way of seeing it, and do the lab or simulation it lists. Then take **Check B**, the parallel retest. It tests the same objectives with new scenarios.
- **If you score 10 or more,** go on to the [enrichment tasks](#enrichment-for-learners-who-passed).

On the exam, a "(Select TWO.)" item scores only if you choose both right answers. Score it the same way here.

## Check A

**A1.** A VPC has two subnets. Subnet X's route table has the local route and sends `0.0.0.0/0` to a NAT gateway, which sits in another, public subnet. Subnet Y's route table has the local route and sends `0.0.0.0/0` to an internet gateway. A server in subnet X has a public IPv4 address; a server in subnet Y has none. Every security group and network ACL allows all traffic. Which statement is correct?

A. Subnet X is public, because its server has a public IPv4 address\
B. Subnet Y is public, but neither server can be reached from the internet\
C. Both subnets are public, because both send `0.0.0.0/0` to a gateway\
D. Subnet Y is private, because its server has no public IPv4 address

<details><summary>Answer</summary>

**B is right.** A subnet is public when its route table has a route to an internet gateway, so Y is public and X is private. But neither server can be reached: X's server has no route from the internet (its way out is the NAT gateway, which never lets the internet start a connection in), and Y's server has no public address for the internet gateway to translate.

- **A is wrong.** An address doesn't make a subnet public. Without a route to an internet gateway, X's public address does nothing but add an hourly charge.
- **C is wrong.** Only a route to an internet gateway makes a subnet public. A route to a NAT gateway is how a private subnet reaches out.
- **D is wrong.** Being public is about the subnet's route, not about any server's address. Y is public; its server just can't use the route.

</details>

**A2.** A company's pricing servers sit in private subnets. Every minute they call a currency-rate service on the internet, and the security team insists that nothing on the internet may ever open a connection to them. An architect adds a NAT gateway. Which TWO statements about a correct setup are true? (Select TWO.)

A. The private subnets' route tables send `0.0.0.0/0` to the NAT gateway\
B. The NAT gateway sits in the private subnets, next to the pricing servers\
C. The currency-rate service can now open connections to the pricing servers through it\
D. The NAT gateway bills for every hour it exists, even when little data passes\
E. The private subnets become public subnets once their routes point at it

<details><summary>Answer</summary>

**A and D.** The private route tables send traffic for the internet to the NAT gateway, which passes it out and brings the replies back. Unlike the internet gateway, a NAT gateway is charged by the hour and per GB processed.

- **B is wrong.** The NAT gateway sits in a **public** subnet, with an Elastic IP address, so that it can reach the internet gateway.
- **C is wrong.** A NAT gateway lets only your servers start connections. Replies come back; new connections from outside are refused.
- **E is wrong.** A subnet is public only with a route to an internet gateway. A route to a NAT gateway leaves it private.

</details>

**A3.** Servers in a company's private subnets read objects from Amazon S3 and send messages to Amazon SQS, both in the same Region. Today both kinds of traffic go through a NAT gateway. The company wants both to stay on AWS's network without the NAT gateway, at the lowest cost. Which design fits?

A. Gateway endpoints for both S3 and SQS\
B. A route from the private subnets to the internet gateway\
C. Interface endpoints for both, because only interface endpoints keep traffic off the internet\
D. A gateway endpoint for S3 and an interface endpoint for SQS

<details><summary>Answer</summary>

**D is right.** Gateway endpoints exist only for Amazon S3 and Amazon DynamoDB, and have no charge, so S3 gets one. SQS needs an interface endpoint (AWS PrivateLink), which bills by the hour in each AZ and per GB.

- **A is wrong.** There's no gateway endpoint for SQS.
- **B is wrong.** A route to the internet gateway would make the subnets public and send the traffic toward the internet.
- **C is wrong.** Both kinds of endpoint keep traffic off the internet. An interface endpoint for S3 would work, but it bills where the gateway endpoint is free.

</details>

**A4.** A web server in a public subnet has a public IPv4 address. Its security group has one inbound rule, allowing TCP 443 from `0.0.0.0/0`, and no outbound rules at all. The subnet's custom network ACL has inbound rule 100 allowing TCP 443 from `0.0.0.0/0` and outbound rule 100 allowing TCP 1024–65535 to `0.0.0.0/0`. A customer opens the site over HTTPS. What happens?

A. The page loads: the security group passes the reply by itself, and the network ACL allows its port\
B. The request arrives, but the security group drops the reply, because it has no outbound rule\
C. The request arrives, but the network ACL drops the reply, because no outbound rule allows port 443\
D. The network ACL drops the request, because its inbound rules are checked after the security group's

<details><summary>Answer</summary>

**A is right.** Walk the path. The network ACL's inbound rule 100 allows the request, and the security group's inbound rule allows it. The security group is stateful, so it lets the reply out with no outbound rule. The network ACL is stateless, so it checks the reply again: the reply goes to the customer's temporary high-numbered port, which outbound rule 100 allows.

- **B is wrong.** A security group's outbound rules control connections the server starts, not replies to requests it allowed in.
- **C is wrong.** The reply goes *to* the customer's high-numbered port, not to port 443, so the 1024–65535 rule is the one it needs.
- **D is wrong.** Arriving traffic crosses the subnet's network ACL first, then the server's security group. Both allow this request.

</details>

**A5.** A subnet's network ACL has these inbound rules: rule 100 denies all traffic from `192.0.2.0/24`; rule 200 allows TCP 443 from `0.0.0.0/0`; rule 300 allows TCP 22 from `192.0.2.0/24`; then the `*` rule. The server's security group allows TCP 22 from `192.0.2.0/24`. An administrator at `192.0.2.15` tries to connect to the server over SSH. What happens?

A. It connects, because rule 300 and the security group both allow SSH from that range\
B. It is dropped at the subnet's edge by rule 100, the first rule that matches\
C. It is dropped by the security group, which also applies the network ACL's deny rules\
D. It connects, because an allow rule in a network ACL outranks a deny rule

<details><summary>Answer</summary>

**B is right.** A network ACL checks its rules from the lowest number up, and the first rule that matches decides. Rule 100 matches every packet from `192.0.2.0/24`, so it denies the SSH attempt, and rule 300 is never reached. The security group never sees the packet.

- **A is wrong.** Rule 300 would allow it, but rule 100 matches first.
- **C is wrong.** The two filters are separate. The security group has allow rules only and knows nothing of the network ACL's rules.
- **D is wrong.** In a network ACL, order decides, not the kind of rule. To let the administrator in, the allow rule would need a lower number than the deny.

</details>

**A6.** Two EC2 instances, App and Cache, sit in the same subnet. The subnet's custom network ACL allows only inbound TCP 443 and outbound TCP 1024–65535, and its `*` rule denies everything else. App's security group allows all outbound traffic, and Cache's security group allows TCP 6379 from App's security group. App opens a connection to Cache on TCP 6379. What happens?

A. The network ACL's `*` rule drops the connection, because no rule allows port 6379\
B. Cache's security group drops it, because a rule's source must be a range of IP addresses\
C. It connects: traffic inside one subnet doesn't cross its network ACL, and Cache's group allows it\
D. It connects only after the network ACL gets an outbound rule for TCP port 6379

<details><summary>Answer</summary>

**C is right.** A network ACL checks traffic as it crosses the subnet's edge, not traffic between resources inside the same subnet. So the only checks are the security groups: App's allows the connection out, and Cache's allows port 6379 from anything carrying App's group.

- **A and D are wrong.** The network ACL would block port 6379 between subnets, but this traffic never leaves the subnet.
- **B is wrong.** A security group rule's source can be another security group, meaning anything attached to that group.

</details>

**A7.** A company moves its domain's DNS to Amazon Route 53. Its site runs in two Regions behind load balancers. It wants (1) the bare domain `example.com`, with no `www`, to point at the load balancers, even though their addresses change, and (2) a Region that stops working to be left out of Route 53's answers. Which TWO Route 53 features meet these needs? (Select TWO.)

A. A private hosted zone\
B. Alias records\
C. Origin access control\
D. Usage plans with API keys\
E. Health checks

<details><summary>Answer</summary>

**B and E.** An alias record can point the bare domain at a load balancer (or a CloudFront distribution, or an S3 website bucket) even though its addresses change. Health checks let Route 53 leave a failed place out of its answers.

- **A is wrong.** A private hosted zone answers only inside the VPCs you choose, not for customers on the internet.
- **C is wrong.** Origin access control is a CloudFront feature that keeps an S3 bucket private.
- **D is wrong.** Usage plans and API keys are Amazon API Gateway features for managing who calls an API.

</details>

**A8.** A company's website runs in one Region. Customers on other continents say pages load slowly. Each page carries many large product photos that are the same for every visitor. A colleague proposes Route 53 latency routing. What should the company use instead?

A. Amazon CloudFront, so that edge locations near customers serve copies of the photos\
B. AWS Global Accelerator, so that every photo request travels to the Region on AWS's network\
C. Route 53 geolocation routing, so that each continent gets its own DNS answer\
D. Amazon API Gateway caching, so that the photos are kept with the company's API

<details><summary>Answer</summary>

**A is right.** The same photos go to many people, so a copy near each customer can answer: that is CloudFront's job as a content delivery network. Latency routing only chooses between Regions, and with one Region there is nothing to choose; Route 53 never carries the photos at all.

- **B is wrong.** Global Accelerator keeps no copies. Every request still makes the whole trip to the Region; it suits traffic that must reach the application each time.
- **C is wrong.** Geolocation routing also only chooses which address a user gets. With one Region it changes nothing, and it carries no content.
- **D is wrong.** API Gateway is the entrance for programs calling an API, not for delivering a website's photos to browsers worldwide.

</details>

**A9.** A company's mobile app calls a backend of Lambda functions through an Application Load Balancer. The company now wants each partner developer to have their own credential and monthly allowance of calls, and wants to try new versions separately from the live one. What does moving the entrance to Amazon API Gateway add?

A. The ability to pass requests on to Lambda functions, which a load balancer can't do\
B. Copies of answers kept at edge locations worldwide, so that calls never reach the functions\
C. Two static anycast IP addresses for the API, announced from AWS's edge locations\
D. Usage plans with API keys, and stages, to give each caller an allowance and keep versions apart

<details><summary>Answer</summary>

**D is right.** A load balancer spreads traffic across healthy targets; API Gateway manages an API. Usage plans and API keys give each caller their own allowance, throttling caps how fast calls arrive, and stages keep test and production apart.

- **A is wrong.** An Application Load Balancer can already send requests to Lambda functions, as this one does.
- **B is wrong.** Keeping copies at the edge is CloudFront's job. API Gateway can cache answers, but that isn't what this need asks for.
- **C is wrong.** Two static anycast addresses are what AWS Global Accelerator gives an application.

</details>

**A10.** A bank's rules say that traffic between its data center and AWS must not travel over the public internet, and must also be encrypted in transit. The bank can wait weeks for the link to be set up. Which design meets both rules?

A. AWS Site-to-Site VPN alone, because a VPN is a private connection\
B. AWS Direct Connect alone, because a dedicated line is encrypted by default\
C. AWS Direct Connect, with a Site-to-Site VPN run over the connection\
D. AWS Client VPN on every computer in the data center

<details><summary>Answer</summary>

**C is right.** Direct Connect gives the private path: a dedicated line that bypasses the internet. Encryption is something you add to it, with a Site-to-Site VPN over the connection or MACsec where the connection supports it.

- **A is wrong.** A Site-to-Site VPN is encrypted, but its traffic crosses the public internet. Private is about the path; encrypted is about the protection.
- **B is wrong.** Direct Connect is private, but it isn't encrypted unless you add encryption.
- **D is wrong.** Client VPN connects individual people's devices over the internet, not a data center's network, and it still uses the internet's path.

</details>

**A11.** A company has exactly two VPCs, in two of its AWS accounts, with address ranges that don't overlap. Servers in each VPC must reach servers in the other, in both directions, over private addresses. The company wants the simplest link, with no hub to run between them. Which fits?

A. AWS PrivateLink, through an interface endpoint\
B. A VPC peering connection\
C. AWS Transit Gateway, with both VPCs attached\
D. A Site-to-Site VPN between the two VPCs

<details><summary>Answer</summary>

**B is right.** VPC peering joins two whole VPCs so they talk over private addresses, across accounts, with no gateway device in the way, as long as their ranges don't overlap.

- **A is wrong.** PrivateLink exposes one service to the consumer, one way, not a whole network in both directions.
- **C is wrong.** Transit Gateway would work, but it is a hub, built for many networks; for two VPCs it adds a part to run and pay for.
- **D is wrong.** Site-to-Site VPN links an office or data center network to AWS over the internet, not two VPCs inside AWS.

</details>

**A12.** A company's application servers in one Availability Zone exchange a lot of data, over private IP addresses, with a cache server in another Availability Zone of the same Region. The bill shows a data transfer charge for this traffic. Which statement is correct?

A. Nothing can remove the charge, because all data moving inside a Region is charged per GB\
B. A VPC peering connection between the two zones would make the traffic free\
C. Sending the traffic through a NAT gateway would make the traffic between the zones free\
D. Moving the cache into the servers' zone would end the charge, at a cost in availability

<details><summary>Answer</summary>

**D is right.** Data that crosses Availability Zones is charged per GB, while data inside one zone over private addresses is free. Moving the cache next to the servers saves the charge, but a failure of that zone then takes out the servers and the cache together: the usual trade between cost and availability.

- **A is wrong.** Data inside one Availability Zone over private addresses has no transfer charge.
- **B is wrong.** Peering joins two VPCs, not two zones of one VPC, and traffic over a peering connection that crosses zones is charged too.
- **C is wrong.** A NAT gateway adds a per-GB processing charge; it never removes one.

</details>

## Correction map

For each item you missed, reread the section, then try the other way of seeing it. Each of these says the idea differently from the lesson.

| Item | Objective (level) | Reread | Another way to see it | Practice with |
|---|---|---|---|---|
| A1 | 07.01a, what makes a subnet public (An) | [A subnet is public because of its route, not because of its addresses](01-your-own-network.md#a-subnet-is-public-because-of-its-route-not-because-of-its-addresses) | Draw the two-by-two grid: the route picks the row, the address picks the column. Only "route to the internet gateway" plus "public address" reaches the internet, in both directions. | [Lab 09](05-lab-09-build-a-small-vpc.md), Part A |
| A2 | 07.01a (Un) | [A NAT gateway lets private servers reach out, never the internet reach in, and it bills by the hour](01-your-own-network.md#a-nat-gateway-lets-private-servers-reach-out-never-the-internet-reach-in-and-it-bills-by-the-hour) | Think of a one-way door with a doorkeeper: the NAT gateway stands in the public subnet and lets your servers' conversations out and back, but opens to no one from outside, and it charges for every hour it stands there. | [Lab 09](05-lab-09-build-a-small-vpc.md) (and why it builds no NAT gateway) |
| A3 | 07.01a (Ap) | [VPC endpoints reach AWS services without the internet, and one kind is free](01-your-own-network.md#vpc-endpoints-reach-aws-services-without-the-internet-and-one-kind-is-free) | Ask two questions per service: "Is it S3 or DynamoDB?" If yes, a free gateway endpoint (a route). If no, an interface endpoint (an address in your subnet), which bills. | [Lab 09](05-lab-09-build-a-small-vpc.md) |
| A4 | 07.02a, predict whether traffic passes (An) | [A security group lets replies through on its own; a network ACL checks them again](02-filtering-traffic.md#a-security-group-lets-replies-through-on-its-own-a-network-acl-checks-them-again) | Write the reply as its own packet: from the server's port 443 to the customer's high-numbered port. The security group recognizes it; the network ACL judges it like a stranger. | [Simulation S8](06-sim-packet-journey.md), Decision 2 |
| A5 | 07.02a (An) | [A network ACL checks every packet entering or leaving a subnet, in number order](02-filtering-traffic.md#a-network-acl-checks-every-packet-entering-or-leaving-a-subnet-in-number-order) | Read the rules like a list at a door: the guard stops at the first line that mentions you and does what it says, without reading further. | [Simulation S8](06-sim-packet-journey.md), Decision 3; [Lab 09](05-lab-09-build-a-small-vpc.md), Part C |
| A6 | 07.02a (An) | [Security group or network ACL: use both, for different jobs](02-filtering-traffic.md#security-group-or-network-acl-use-both-for-different-jobs) | A network ACL is a fence around a yard; a security group is a lock on each house. Two houses in the same yard meet without passing the fence, but each lock still decides. | [Simulation S8](06-sim-packet-journey.md), packet E |
| A7 | 07.03a, choose an edge or naming service (Ap) | [Route 53 answers "where is it?", and it can choose the answer](03-names-and-the-edge.md#route-53-answers-where-is-it-and-it-can-choose-the-answer) | Route 53 works only at the moment a browser asks "where?". Every Route 53 feature changes that answer: which address (alias), which place (routing policies), and which places are left out (health checks). | The lesson's [worked example](03-names-and-the-edge.md#worked-example-the-bakerys-names-and-edge) |
| A8 | 07.03a (Ap) | [Global Accelerator gives fixed addresses and a fast path, but keeps no copies](03-names-and-the-edge.md#global-accelerator-gives-fixed-addresses-and-a-fast-path-but-keeps-no-copies) | Ask, "Could yesterday's answer serve today's visitor?" For a product photo, yes: a copy at the edge can answer, so CloudFront. For a game move or a sensor reading, no: every request must reach the application. | [Choose by what the need is really about](03-names-and-the-edge.md#choose-by-what-the-need-is-really-about) |
| A9 | 07.03a (Ap) | [API Gateway is the managed entrance to your code](03-names-and-the-edge.md#api-gateway-is-the-managed-entrance-to-your-code) | A load balancer is a receptionist sharing visitors among clerks. API Gateway is a membership desk: it checks each caller's card, counts their visits, and sends them to the right version. | [Choose by what the need is really about](03-names-and-the-edge.md#choose-by-what-the-need-is-really-about) |
| A10 | 07.04a, choose a link (Ap) | ["A VPN is a private connection" is wrong](04-connecting-networks-and-offices.md#a-vpn-is-a-private-connection-is-wrong) and [Direct Connect is a dedicated line that bypasses the internet](04-connecting-networks-and-offices.md#direct-connect-is-a-dedicated-line-that-bypasses-the-internet) | A sealed letter sent through the public post is encrypted, not private: it travels the public roads. A private courier road is private, but the letter can still be open. Private and encrypted needs both the road and the seal. | [Choosing a link](04-connecting-networks-and-offices.md#choosing-a-link-ask-who-connects-then-the-three-questions) |
| A11 | 07.04a (Ap) | [Peering, Transit Gateway and PrivateLink connect networks inside AWS](04-connecting-networks-and-offices.md#peering-transit-gateway-and-privatelink-connect-networks-inside-aws) | Count what needs joining: two whole networks (peering), many networks or offices (Transit Gateway), or one service (PrivateLink). | [Choosing a link](04-connecting-networks-and-offices.md#choosing-a-link-ask-who-connects-then-the-three-questions) |
| A12 | 07.04a, data transfer (task [4.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html#cloud-practitioner-02-task4.1)) (Ap) | [Data in is free; across, between and out usually costs](04-connecting-networks-and-offices.md#data-in-is-free-across-between-and-out-usually-costs) | Picture each Availability Zone as a separate building: talk inside one building is free, and every trip between buildings, between cities (Regions) or out to the public (the internet) has a fare. | The lesson's data transfer estimate in [Data in is free; across, between and out usually costs](04-connecting-networks-and-offices.md#data-in-is-free-across-between-and-out-usually-costs) |

## Check B: parallel retest

Take Check B after you have worked through the correction map. It tests the same objectives as Check A, item for item, with new scenarios. The threshold is again 10 of 12.

**B1.** A VPC has three subnets. Subnet P's route table sends `0.0.0.0/0` to an internet gateway. Subnet Q's sends `0.0.0.0/0` to a NAT gateway that sits in subnet P. Subnet R's has only the local route. One server in each subnet has a public IPv4 address, and every security group and network ACL allows HTTPS from anywhere. To which servers can a customer on the internet open an HTTPS connection?

A. Only the server in subnet P\
B. The servers in subnets P and Q\
C. All three, because each server has a public IPv4 address\
D. None, because a server needs an Elastic IP address, not an automatic one

<details><summary>Answer</summary>

**A is right.** Only subnet P routes to an internet gateway, so only P is public, and its server has the public address the gateway needs.

- **B is wrong.** Q routes to a NAT gateway, which lets Q's servers start connections out but never lets the internet start one in. Q's public address does nothing.
- **C is wrong.** A public address without a route to an internet gateway gives no path. R's server is as unreachable as if it had no address.
- **D is wrong.** Either kind of public IPv4 address works with an internet gateway; an Elastic IP address is just one you keep.

</details>

**B2.** A clinic designs its VPC. Its booking web servers must accept connections from patients on the internet. Its lab-results server must fetch files from a laboratory partner's site on the internet, but nothing on the internet may open a connection to it. Which TWO choices fit? (Select TWO.)

A. Lab-results server: a private subnet, with an Elastic IP address and no other route\
B. Web servers: a private subnet routing `0.0.0.0/0` to a NAT gateway, for patients to use\
C. Web servers: a public subnet routing `0.0.0.0/0` to the internet gateway, with public addresses\
D. Lab-results server: a private subnet, reaching the partner's site through a gateway endpoint\
E. Lab-results server: a private subnet routing `0.0.0.0/0` to a NAT gateway

<details><summary>Answer</summary>

**C and E.** If the internet must start connections to it, use a public subnet and the internet gateway. If it only needs to reach out, keep it private and route it to a NAT gateway.

- **A is wrong.** A public address in a subnet with no route to an internet gateway gives no path out, and it adds an hourly charge.
- **B is wrong.** A NAT gateway refuses connections started from the internet, so patients couldn't reach the web servers through it.
- **D is wrong.** Gateway endpoints reach only Amazon S3 and Amazon DynamoDB, not a partner's site on the internet.

</details>

**B3.** An application in a company's private subnets must write to Amazon DynamoDB and call a payment provider's service on the public internet. The subnets must stay private, and the company wants the lowest cost. Which design fits?

A. A NAT gateway for both kinds of traffic\
B. Gateway endpoints for both DynamoDB and the payment provider\
C. A gateway endpoint for DynamoDB, and a NAT gateway for the payment provider\
D. A route from the private subnets to the internet gateway for both

<details><summary>Answer</summary>

**C is right.** A gateway endpoint carries the DynamoDB traffic privately at no charge, so it never pays the NAT gateway's per-GB processing. The payment provider is on the internet, so that traffic needs the NAT gateway, which keeps the subnets private.

- **A is wrong.** It works, but every GB written to DynamoDB pays the NAT gateway's processing charge, which the free gateway endpoint avoids.
- **B is wrong.** Gateway endpoints exist only for Amazon S3 and Amazon DynamoDB, not for services on the internet.
- **D is wrong.** A route to the internet gateway would make the subnets public.

</details>

**B4.** A web server in a public subnet has a public IPv4 address. Its security group allows inbound TCP 443 from `0.0.0.0/0` and all outbound traffic. The subnet's custom network ACL has inbound rule 100 allowing TCP 443 from `0.0.0.0/0`, and outbound rule 100 allowing TCP 1024–65535 to `10.0.0.0/16`, the VPC's own range; then the `*` rule. A customer at `192.0.2.44` opens the site over HTTPS. What happens?

A. The page loads, because the security group is stateful, so replies always get through\
B. The network ACL drops the request, because its inbound rule doesn't cover the customer\
C. The security group drops the reply, because its outbound rules don't mention port 443\
D. The request arrives, but the network ACL drops the reply, which isn't going to `10.0.0.0/16`

<details><summary>Answer</summary>

**D is right.** Inbound rule 100 and the security group let the request in, and the security group lets the reply out because it remembers the request. But the stateless network ACL checks the reply again. It is going to `192.0.2.44`, outside `10.0.0.0/16`, so outbound rule 100 doesn't match and the `*` rule drops it. To the customer, the site looks down.

- **A is wrong.** That is the misconception: the security group passes the reply, but the reply still crosses the network ACL, which can drop it.
- **B is wrong.** Inbound rule 100 allows TCP 443 from any address, the customer's included.
- **C is wrong.** The security group allows all outbound traffic, and it would pass a reply to an allowed request in any case.

</details>

**B5.** A subnet's network ACL has these inbound rules: rule 100 allows TCP 22 from `198.51.100.0/24`, a partner's range; rule 110 denies all traffic from `198.51.100.0/24`; rule 120 allows TCP 443 from `0.0.0.0/0`; then the `*` rule. Which arriving packet does the network ACL allow?

A. HTTPS (TCP 443) from `198.51.100.9`\
B. SSH (TCP 22) from `198.51.100.9`\
C. SSH (TCP 22) from `203.0.113.5`\
D. RDP (TCP 3389) from `203.0.113.5`

<details><summary>Answer</summary>

**B is right.** Rule 100 is checked first and matches SSH from the partner's range, so it allows the packet; rule 110's deny is never reached for it.

- **A is wrong.** Rule 100 doesn't match HTTPS, so rule 110 is next, and it denies everything from the partner's range. Rule 120 never gets the chance to allow it.
- **C is wrong.** No numbered rule matches SSH from `203.0.113.5`, so the `*` rule denies it.
- **D is wrong.** No numbered rule matches RDP, so the `*` rule denies it.

</details>

**B6.** A web server's subnet used a route table that sent `0.0.0.0/0` to the internet gateway. While tidying up, an administrator associates the subnet with a different route table that has only the local route. The server keeps its public IPv4 address, its security group still allows HTTPS from anywhere, and the network ACL still allows all traffic. What happens when a customer opens the site?

A. The page still loads, because the security group still allows HTTPS from anywhere\
B. The page still loads, because the server still has its public IPv4 address\
C. The site stops working for customers, because the subnet has no route to the internet gateway\
D. The network ACL drops the request, because a new route table resets its rules to deny all

<details><summary>Answer</summary>

**C is right.** The route is the first check on the path. Without a route to an internet gateway the subnet is now private, and its servers can't talk to the internet, whatever their addresses and filters allow.

- **A is wrong.** A security group only decides among traffic that can reach the server; it doesn't create a path.
- **B is wrong.** A public address without a route to an internet gateway does nothing.
- **D is wrong.** Route tables and network ACLs are separate. Changing the route table leaves the network ACL's rules as they were.

</details>

**B7.** A company is choosing services for a new website. Which TWO of its needs does Amazon Route 53 meet? (Select TWO.)

A. Registering the company's domain name\
B. Keeping copies of the site's images at edge locations\
C. Giving each partner's app its own API key and call limit\
D. Sending 10 in every 100 visitors to a new version of the site\
E. Giving the application two fixed anycast IP addresses

<details><summary>Answer</summary>

**A and D.** Route 53 registers domain names, answers DNS questions and checks health. Weighted routing sends a share of users you set, such as 10 in 100, to each place.

- **B is wrong.** Keeping copies at the edge is CloudFront's job; Route 53 is not a CDN and never carries content.
- **C is wrong.** API keys and call limits are Amazon API Gateway's usage plans.
- **E is wrong.** Two static anycast addresses come from AWS Global Accelerator.

</details>

**B8.** A machinery maker has two needs. Need 1: a large firmware file that tens of thousands of customers around the world download in the same week. Need 2: thousands of machines in factories send small, unique status messages over TCP to an application in two Regions; the machines can store only fixed IP addresses, and if one Region fails, traffic must move to the other without waiting for DNS copies to expire. Which pairing fits?

A. Need 1: Amazon CloudFront. Need 2: AWS Global Accelerator\
B. Need 1: AWS Global Accelerator. Need 2: Amazon CloudFront\
C. Need 1: Amazon CloudFront. Need 2: Amazon Route 53 latency routing\
D. Need 1: Amazon Route 53 latency routing. Need 2: AWS Global Accelerator

<details><summary>Answer</summary>

**A is right.** The same file goes to many people, so copies at edge locations can answer: CloudFront. Every status message is new and must reach the application, through addresses that never change, with fast failover between Regions: Global Accelerator, which gives two static IP addresses and reroutes at the edge without relying on DNS.

- **B is wrong.** It swaps the two. Global Accelerator keeps no copies, so every download would travel to the Region; CloudFront's copies can't answer unique messages.
- **C is wrong.** Latency routing works through DNS answers, which other servers keep until the TTL runs out, and it gives no fixed addresses.
- **D is wrong.** Route 53 only answers where the file is; it never carries or caches the download.

</details>

**B9.** A company is adding live chat to its app. Messages must flow both ways, in real time, between users' devices and Lambda functions, and the company wants no servers of its own to run. Which entrance fits?

A. Amazon API Gateway, with a REST API\
B. Amazon API Gateway, with a WebSocket API\
C. Amazon API Gateway, with an HTTP API\
D. Amazon CloudFront, with the functions as its origin

<details><summary>Answer</summary>

**B is right.** API Gateway is the managed entrance to your code, with no servers of your own. Its WebSocket APIs carry two-way, real-time messages such as chat, and hand them to Lambda functions.

- **A and C are wrong.** REST and HTTP APIs suit request-and-answer calls, where the device asks and the code answers. Chat needs messages pushed both ways over a connection that stays open.
- **D is wrong.** CloudFront delivers and caches content near users; it isn't the entrance that manages a two-way chat API.

</details>

**B10.** A manufacturer starts moving systems from its data center to AWS. It needs an encrypted link from the data center's network within days, while traffic is still light. In about six months, large nightly data loads will need steady, high bandwidth on a path that avoids the public internet. Which plan fits both stages?

A. Direct Connect now, because a dedicated line can be ordered and running within minutes\
B. Client VPN now, for the whole data center network; Transit Gateway later for the bandwidth\
C. Site-to-Site VPN now; later add Direct Connect, and keep the VPN as a backup link\
D. VPC peering with the data center now; Direct Connect later, replacing the peering

<details><summary>Answer</summary>

**C is right.** Site-to-Site VPN connects a whole network over encrypted tunnels and can be set up in minutes, which fits the first stage. When traffic grows and the path must avoid the internet, Direct Connect gives a private, consistent line; it takes longer to set up, so it is ordered ahead. The VPN then stays as a cheaper backup, used only if Direct Connect fails.

- **A is wrong.** Direct Connect needs physical work at a Direct Connect location or through a partner, so it isn't ready in minutes.
- **B is wrong.** Client VPN connects individual people's devices, not a data center's network, and a transit gateway is a hub for joining networks, not a faster path off the internet.
- **D is wrong.** VPC peering joins two VPCs inside AWS; it can't connect a data center.

</details>

**B11.** A company's central data team runs an address-checking service in its own VPC. Dozens of application teams, each with a VPC in another of the company's accounts, must call that one service and reach nothing else in the data team's VPC. Several of those VPCs use the same address range as the data team's. Which service fits?

A. VPC peering between the data team's VPC and each team's VPC\
B. AWS Transit Gateway, with every team's VPC attached to one hub\
C. AWS Site-to-Site VPN from each team's VPC to the data team\
D. AWS PrivateLink, with an interface endpoint in each team's VPC

<details><summary>Answer</summary>

**D is right.** PrivateLink connects a VPC to one service, not a network. The data team publishes its service as an endpoint service behind a Network Load Balancer, and each application team creates an interface endpoint in its own VPC. Only that service is reachable, and nothing else in either network is opened.

- **A is wrong.** Peering joins whole networks in both directions, and VPCs with overlapping address ranges can't be peered.
- **B is wrong.** A transit gateway joins whole networks through a hub, which would open far more than the one service.
- **C is wrong.** Site-to-Site VPN connects an on-premises network to AWS over the internet; it doesn't expose one service privately.

</details>

**B12.** A company serves large downloads straight from an S3 bucket to customers worldwide, and data transfer out is its biggest network cost. It puts Amazon CloudFront in front of the bucket. What happens to the data transfer charges?

A. S3 to CloudFront is free; the customers' downloads bill at CloudFront's prices\
B. Each download is now charged twice: once leaving S3 and again leaving CloudFront\
C. Every transfer becomes free, because CloudFront has no charge for delivery\
D. Nothing changes, because only data coming in from the internet is ever charged

<details><summary>Answer</summary>

**A is right.** Moving content from an AWS origin such as S3 to CloudFront has no transfer charge. The downloads to customers are then billed at CloudFront's own delivery prices, and copies at the edge also take load off the bucket.

- **B is wrong.** The leg from S3 to CloudFront is free, so nothing is charged twice.
- **C is wrong.** CloudFront charges for what it delivers, per GB and per request, or through a flat-rate plan.
- **D is wrong.** Data in from the internet is the free direction; data out is the usual charge.

</details>

## Enrichment for learners who passed

Three harder tasks. Each has no single right answer; compare your reasoning with the model answer, not just your conclusion.

**Task 1: a network to justify.** A clinic moves its booking system to AWS: a load balancer that patients reach over HTTPS, application servers that must download operating system updates and read documents from an S3 bucket, and a database that only the application servers may reach. It must survive the loss of one Availability Zone and keep the bill small. Lay out the subnets, the gateways and endpoints, and the security group chain, and say which choice is the expensive one and why you accept it.

<details><summary>Model answer</summary>

Two public subnets (one per AZ) hold the load balancer; their route table sends `0.0.0.0/0` to the internet gateway. Two private subnets hold the application servers, and two more private subnets hold the database and its standby, so no server and no database has a public address. A **gateway endpoint for S3**, with a route from the application subnets, carries the documents at no charge. The updates need a **NAT gateway**: one in each AZ's public subnet, so losing one AZ doesn't strand the other zone's servers (AWS's newer Regional NAT gateway is an option to check on its current pages). The security groups chain by reference: the load balancer's group allows 443 from anywhere; the application group allows traffic only from the load balancer's group; the database group allows its port only from the application group. The NAT gateways are the expensive part: they bill by the hour whether or not updates are flowing, and two cost twice one. You accept them because the servers need the internet, and the second one is the price of high availability. This applies [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) and [COST08-BP03 Implement services to reduce data transfer costs](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_implement_services.html).

</details>

**Task 2: a real-world complication.** A company's head office reaches its VPC over a single AWS Direct Connect connection. AWS announces planned maintenance on that connection for next month. The office's order system can't stop for hours. What risk does the design have, what are two ways to fix it, and how do they compare?

<details><summary>Model answer</summary>

A single connection is a single point of failure: maintenance, a cut cable or a failed router stops the office's link. **Fix 1:** add a Site-to-Site VPN over the internet to the same VPC (or to a transit gateway). It is quick and cheap to add, and AWS prefers the Direct Connect path while it is up, so the VPN carries traffic only during a failure, encrypted but over the internet's variable path. **Fix 2:** add a second Direct Connect connection, ideally at a second Direct Connect location, so even a whole location's failure leaves a private, consistent path. It costs more and takes longer to set up. A company that only needs to keep working, slowly, during rare outages chooses the VPN; one that needs the same performance during an outage chooses the second connection. This is [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ha_conn_private_networks.html).

</details>

**Task 3: write the rules both ways.** A public subnet holds web servers that serve customers over HTTPS and must also download updates over HTTPS from the internet. Write the smallest set of custom network ACL rules (inbound and outbound) that lets both kinds of conversation work, and say what each rule is for. Then say why the security groups still matter.

<details><summary>Model answer</summary>

Inbound 100: allow TCP 443 from `0.0.0.0/0`, for customers' requests. Inbound 110: allow TCP 1024–65535 from `0.0.0.0/0`, for the replies to the servers' own downloads, which come back to a high-numbered port. Outbound 100: allow TCP 1024–65535 to `0.0.0.0/0`, for the replies to customers. Outbound 110: allow TCP 443 to `0.0.0.0/0`, for the downloads. The `*` rule denies everything else. A stateless filter needs a rule for each half of each conversation, so two conversations take four rules. Inbound rule 110 lets any internet address reach any high-numbered port at the subnet's edge, which is why the security groups stay the main control: the web servers' group allows only 443 inbound, and, being stateful, it lets the download replies in without opening any port. Two layers, each catching what the other lets past, is [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html).

</details>

---

"Module 07 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
