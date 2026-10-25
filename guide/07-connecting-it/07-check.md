---
type: check
id: clf-07-07
title: "Module 07 mastery check"
tasks: ["3.5", "3.2", "4.1", "2.1"]
objectives: ["07.01a", "07.02a", "07.03a", "07.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 07 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-07-01, clf-07-02, clf-07-03, clf-07-04]
pillars: [security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html"
  - "https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html"
  - "https://aws.amazon.com/directconnect/faqs/"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
---

# Module 07 mastery check: read a network, choose a filter, and pick the right edge service and link

**For:** an adult studying alone, possibly new to IT, who has finished lessons [07.01](01-your-own-network.md) to [07.04](04-connecting-networks-and-offices.md). **Time:** about 20 minutes per check.

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 08.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

### Question A1

A VPC has two subnets. Subnet X's route table sends `0.0.0.0/0` to a NAT gateway. Subnet Y's sends `0.0.0.0/0` to an internet gateway. A server in X has a public IPv4 address; a server in Y has none. Which statement is correct?

- A. Subnet X is public, because its server has a public IPv4 address
- B. Subnet Y is public, but neither server can be reached from the internet
- C. Both subnets are public, because both send `0.0.0.0/0` to a gateway
- D. Subnet Y is private, because its server has no public IPv4 address

<details><summary>Answer</summary>

**B is right.** A route to an internet gateway makes Y public. X's server can't be reached through a NAT gateway, and Y's server has no public address.

- **A is wrong.** An address doesn't make a subnet public; it only adds an hourly charge.
- **C is wrong.** A route to a NAT gateway leaves a subnet private.
- **D is wrong.** Public is about the subnet's route, not a server's address.

</details>

### Question A2

Pricing servers in private subnets call a currency-rate service on the internet every minute, and nothing on the internet may ever open a connection to them. An architect adds a NAT gateway. Which TWO statements are true? (Select TWO.)

- A. The private subnets' route tables send `0.0.0.0/0` to the NAT gateway
- B. The currency-rate service can now open connections to the servers
- C. The NAT gateway bills for every hour it exists, even when little data passes
- D. The private subnets become public once their routes point at it
- E. The NAT gateway has no charge, like the internet gateway

<details><summary>Answer</summary>

**A and C.**

- **B is wrong.** A NAT gateway lets only your servers start connections.
- **D is wrong.** Only a route to an internet gateway makes a subnet public.
- **E is wrong.** A NAT gateway bills by the hour and per GB.

</details>

### Question A3

Servers in private subnets read from Amazon S3 and send messages to Amazon SQS through a NAT gateway. The company wants both kinds of traffic to skip the NAT gateway at the lowest cost. Which design fits?

- A. Gateway endpoints for both S3 and SQS
- B. A route from the private subnets to the internet gateway
- C. Interface endpoints for both
- D. A gateway endpoint for S3 and an interface endpoint for SQS

<details><summary>Answer</summary>

**D is right.** Gateway endpoints exist only for S3 and DynamoDB and have no charge; SQS needs an interface endpoint, which bills.

- **A is wrong.** There's no gateway endpoint for SQS.
- **B is wrong.** That makes the subnets public.
- **C is wrong.** It works, but an S3 interface endpoint bills where the gateway endpoint is free.

</details>

### Question A4

Which TWO statements about security groups and network ACLs are true? (Select TWO.)

- A. A security group can deny traffic from one IP address
- B. A network ACL is stateless, so replies must be allowed by its rules
- C. A security group applies to a whole subnet
- D. A security group is stateful, so replies to allowed requests pass automatically
- E. A network ACL considers all its rules together, in no order

<details><summary>Answer</summary>

**B and D.**

- **A is wrong.** Security groups have allow rules only.
- **C is wrong.** A security group guards the resources attached to it; a network ACL guards a subnet.
- **E is wrong.** A network ACL checks numbered rules in order; the first match decides.

</details>

### Question A5

Thousands of failed logins reach a company's site from addresses in `192.0.2.0/24`. Everyone else must still reach the site over HTTPS. What should the company change?

- A. Add a deny rule for the range to the web servers' security group
- B. Add a deny rule for the range to the subnet's network ACL, numbered below the rule that allows HTTPS
- C. Turn on Amazon Inspector to block the range
- D. Turn on VPC Flow Logs for the subnet

<details><summary>Answer</summary>

**B is right.** Only a network ACL has deny rules, and the lower number makes the deny match first.

- **A is wrong.** Security groups have no deny rules.
- **C is wrong.** Inspector reports exposure; it blocks nothing.
- **D is wrong.** Flow Logs record traffic; they block nothing.

</details>

### Question A6

A company's site runs in two Regions. It wants (1) to register a new domain name and (2) customers sent to the other Region automatically when one stops working. Which TWO Route 53 features meet these needs? (Select TWO.)

- A. Domain registration
- B. Origin access control
- C. Usage plans with API keys
- D. Failover routing with health checks
- E. Two static anycast IP addresses

<details><summary>Answer</summary>

**A and D.**

- **B is wrong.** Origin access control is a CloudFront feature that keeps an S3 bucket private.
- **C is wrong.** Usage plans are API Gateway's.
- **E is wrong.** Static anycast addresses come from Global Accelerator.

</details>

### Question A7

A website runs in one Region. Customers on other continents say pages load slowly. Each page carries large product photos that are the same for every visitor. Which service helps most?

- A. Amazon CloudFront
- B. AWS Global Accelerator
- C. Route 53 latency routing
- D. Amazon API Gateway

<details><summary>Answer</summary>

**A is right.** The same photos go to many people, so copies at edge locations near customers can answer.

- **B is wrong.** Global Accelerator keeps no copies; every request still goes to the Region.
- **C is wrong.** With one Region, there's nothing to choose between, and Route 53 never carries content.
- **D is wrong.** API Gateway is the entrance for programs calling an API.

</details>

### Question A8

A mobile app calls Lambda functions through an Application Load Balancer. Now each partner developer needs their own key and monthly allowance of calls. What should it use as the entrance?

- A. Amazon API Gateway
- B. Amazon CloudFront
- C. AWS Global Accelerator
- D. A second Application Load Balancer

<details><summary>Answer</summary>

**A is right.** API Gateway manages an API: who may call, how often, which version.

- **B is wrong.** CloudFront delivers and caches content.
- **C is wrong.** Global Accelerator gives fixed addresses and a fast path, not per-caller limits.
- **D is wrong.** A load balancer spreads traffic; it has no per-caller keys or allowances.

</details>

### Question A9

A bank's traffic between its data center and AWS must avoid the public internet and be encrypted in transit. It can wait weeks for setup. Which design meets both rules?

- A. AWS Site-to-Site VPN alone
- B. AWS Direct Connect alone
- C. AWS Direct Connect, with a Site-to-Site VPN run over the connection
- D. AWS Client VPN on every computer in the data center

<details><summary>Answer</summary>

**C is right.** Direct Connect gives the private path; the VPN over it adds encryption.

- **A is wrong.** A VPN is encrypted, but crosses the public internet.
- **B is wrong.** Direct Connect isn't encrypted unless you add encryption.
- **D is wrong.** Client VPN connects individual devices, over the internet.

</details>

### Question A10

Application servers in one Availability Zone exchange a lot of data, over private IP addresses, with a cache server in another AZ of the same Region. The bill shows a data transfer charge. Which statement is correct?

- A. All data moving inside a Region is charged, so nothing can remove it
- B. Data across AZs is charged; moving the cache into the servers' AZ would end the charge, at a cost in availability
- C. Sending the traffic through a NAT gateway would make it free
- D. Only data out to the internet is charged, so the bill must be wrong

<details><summary>Answer</summary>

**B is right.** Data inside one AZ over private addresses is free; crossing AZs is charged per GB.

- **A is wrong.** Data within one AZ has no transfer charge.
- **C is wrong.** A NAT gateway adds a per-GB charge.
- **D is wrong.** Data across AZs and between Regions is charged too.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 07.01a | [A subnet is public because of its route](01-your-own-network.md#a-subnet-is-public-because-of-its-route-not-because-of-its-addresses) |
| A2, B2 | 07.01a | [NAT gateways](01-your-own-network.md#a-nat-gateway-lets-private-servers-reach-out-never-the-internet-reach-in-and-it-bills-by-the-hour) |
| A3, B3 | 07.01a | [VPC endpoints](01-your-own-network.md#vpc-endpoints-reach-aws-services-without-the-internet-and-one-kind-is-free) |
| A4, B4 | 07.02a | [Security group or network ACL](02-filtering-traffic.md#security-group-or-network-acl-use-both-for-different-jobs) |
| A5, B5 | 07.02a | [Network ACLs](02-filtering-traffic.md#a-network-acl-checks-every-packet-entering-or-leaving-a-subnet-in-number-order) and [Amazon Inspector](02-filtering-traffic.md#amazon-inspector-finds-open-paths-it-doesnt-block-anything) |
| A6, B6 | 07.03a | [Route 53](03-names-and-the-edge.md#route-53-answers-where-is-it-and-it-can-choose-the-answer) |
| A7, B7 | 07.03a | [Global Accelerator vs CloudFront](03-names-and-the-edge.md#global-accelerator-gives-fixed-addresses-and-a-fast-path-but-keeps-no-copies) |
| A8, B8 | 07.03a | [API Gateway](03-names-and-the-edge.md#api-gateway-is-the-managed-entrance-to-your-code) |
| A9, B9 | 07.04a | ["A VPN is a private connection" is wrong](04-connecting-networks-and-offices.md#a-vpn-is-a-private-connection-is-wrong) and [Direct Connect](04-connecting-networks-and-offices.md#direct-connect-is-a-dedicated-line-that-bypasses-the-internet) |
| A10, B10 | 07.04a | [Data transfer](04-connecting-networks-and-offices.md#data-in-is-free-across-between-and-out-usually-costs) |

## Check B: parallel retest

### Question B1

A VPC has three subnets. P's route table sends `0.0.0.0/0` to an internet gateway, Q's to a NAT gateway, and R's has only the local route. One server in each has a public IPv4 address, and every filter allows HTTPS from anywhere. Which servers can a customer on the internet reach?

- A. Only the server in P
- B. The servers in P and Q
- C. All three, because each has a public IPv4 address
- D. None, because a server needs an Elastic IP address

<details><summary>Answer</summary>

**A is right.** Only P routes to an internet gateway, and its server has a public address.

- **B is wrong.** A NAT gateway never lets the internet start a connection in.
- **C is wrong.** An address without a route to an internet gateway gives no path.
- **D is wrong.** Any public IPv4 address works; an Elastic IP address is just one you keep.

</details>

### Question B2

A clinic's booking servers must accept connections from patients on the internet. Its lab-results server must fetch files from a partner's site, and nothing on the internet may connect to it. Which TWO choices fit? (Select TWO.)

- A. Lab-results server: a private subnet with an Elastic IP address and no other route
- B. Booking servers: a private subnet routing to a NAT gateway
- C. Booking servers: a public subnet routing to the internet gateway, with public addresses
- D. Lab-results server: a private subnet reaching the partner through a gateway endpoint
- E. Lab-results server: a private subnet routing `0.0.0.0/0` to a NAT gateway

<details><summary>Answer</summary>

**C and E.** If the internet must start connections, use a public subnet; if a server only reaches out, use a NAT gateway.

- **A is wrong.** An address without a route gives no path out.
- **B is wrong.** A NAT gateway refuses connections from patients.
- **D is wrong.** Gateway endpoints reach only S3 and DynamoDB.

</details>

### Question B3

An application in private subnets writes to Amazon DynamoDB and calls a payment provider on the internet. The subnets must stay private, at the lowest cost. Which design fits?

- A. A NAT gateway for both
- B. Gateway endpoints for both
- C. A gateway endpoint for DynamoDB and a NAT gateway for the payment provider
- D. A route to the internet gateway for both

<details><summary>Answer</summary>

**C is right.** The free gateway endpoint carries the DynamoDB traffic; the internet traffic needs the NAT gateway.

- **A is wrong.** It works, but every GB to DynamoDB pays the NAT gateway's charge.
- **B is wrong.** Gateway endpoints don't reach services on the internet.
- **D is wrong.** That makes the subnets public.

</details>

### Question B4

A web server's security group allows HTTPS in. Someone replaces the subnet's default network ACL with a custom one that allows inbound HTTPS and outbound HTTPS only. Requests arrive, but the site stops loading. Why?

- A. The security group blocks the replies, because it has no outbound rule for them
- B. The network ACL is stateless, and its outbound rules don't allow the replies, which go to the customers' high-numbered ports
- C. A custom network ACL blocks all inbound traffic
- D. The internet gateway was removed with the old network ACL

<details><summary>Answer</summary>

**B is right.** The security group passes the replies; the stateless network ACL checks them again and drops them.

- **A is wrong.** A security group is stateful: replies to allowed requests pass.
- **C is wrong.** Its inbound rule lets the requests in.
- **D is wrong.** Network ACLs and gateways are separate.

</details>

### Question B5

A security team wants a report of EC2 instances that can be reached from the internet on ports nobody meant to open. Which service fits?

- A. Amazon Inspector
- B. A network ACL
- C. VPC Flow Logs
- D. AWS Network Firewall

<details><summary>Answer</summary>

**A is right.** Inspector scans workloads and reports unintended network exposure as findings.

- **B is wrong.** A network ACL filters traffic; it reports nothing.
- **C is wrong.** Flow Logs record traffic; they don't assess exposure.
- **D is wrong.** It's a firewall, and out of the exam's scope.

</details>

### Question B6

Which TWO needs does Amazon Route 53 meet? (Select TWO.)

- A. Registering the company's domain name
- B. Keeping copies of the site's images at edge locations
- C. Giving each partner's app its own API key
- D. Sending 10 in every 100 visitors to a new version of the site
- E. Giving the application two fixed anycast IP addresses

<details><summary>Answer</summary>

**A and D.** Weighted routing sends a share you set to each place.

- **B is wrong.** That's CloudFront; Route 53 is not a CDN.
- **C is wrong.** That's API Gateway.
- **E is wrong.** That's Global Accelerator.

</details>

### Question B7

Need 1: a large firmware file that thousands of customers download in the same week. Need 2: machines send small, unique messages over TCP to an application in two Regions, and can store only fixed IP addresses. Which pairing fits?

- A. Need 1: CloudFront. Need 2: Global Accelerator
- B. Need 1: Global Accelerator. Need 2: CloudFront
- C. Need 1: CloudFront. Need 2: Route 53 latency routing
- D. Need 1: Route 53 latency routing. Need 2: Global Accelerator

<details><summary>Answer</summary>

**A is right.** Copies at the edge can serve the same file to many people; unique messages that need fixed addresses suit Global Accelerator.

- **B is wrong.** It swaps the two.
- **C is wrong.** Latency routing gives no fixed addresses.
- **D is wrong.** Route 53 never carries the download.

</details>

### Question B8

Which service lets developers publish and secure APIs at any scale, with throttling and no servers to manage?

- A. Elastic Load Balancing
- B. Amazon API Gateway
- C. Amazon CloudFront
- D. Amazon Route 53

<details><summary>Answer</summary>

**B is right.** API Gateway is the managed entrance to your code.

- **A is wrong.** A load balancer spreads traffic across targets; it doesn't manage an API.
- **C is wrong.** CloudFront delivers content.
- **D is wrong.** Route 53 answers DNS questions.

</details>

### Question B9

A manufacturer needs an encrypted link from its data center within days. In six months, large nightly loads will need steady bandwidth off the public internet. Which plan fits?

- A. Direct Connect now, because it's ready within minutes
- B. Client VPN now; Transit Gateway later for the bandwidth
- C. Site-to-Site VPN now; later add Direct Connect, and keep the VPN as a backup
- D. VPC peering with the data center now; Direct Connect later

<details><summary>Answer</summary>

**C is right.** A VPN connects a network, encrypted, in minutes; Direct Connect later gives the private, consistent path.

- **A is wrong.** Direct Connect needs physical work.
- **B is wrong.** Client VPN connects devices, and Transit Gateway is a hub, not a faster path.
- **D is wrong.** Peering joins VPCs, not a data center.

</details>

### Question B10

A company serving large downloads from an S3 bucket puts Amazon CloudFront in front of it. What happens to the data transfer charges?

- A. S3 to CloudFront is free; downloads bill at CloudFront's prices
- B. Each download is charged twice, leaving S3 and leaving CloudFront
- C. Every transfer becomes free
- D. Nothing changes, because only data coming in is charged

<details><summary>Answer</summary>

**A is right.** Moving content from S3 to CloudFront has no transfer charge.

- **B is wrong.** The S3-to-CloudFront leg is free.
- **C is wrong.** CloudFront charges for what it delivers.
- **D is wrong.** Data in is the free direction.

</details>

---

"Module 07 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
