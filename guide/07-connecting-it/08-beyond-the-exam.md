---
type: page
id: clf-07-08
title: "Module 07: beyond the exam"
reader: "Adult who has finished Module 07 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-07-00]
pillars: [security, reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html"
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html"
  - "https://aws.amazon.com/cloudfront/pricing/"
  - "https://aws.amazon.com/vpn/faqs/"
  - "https://aws.amazon.com/directconnect/faqs/"
  - "https://aws.amazon.com/vpc/pricing/"
---

# Module 07: what we left out, and where to read it

The CLF-C02 exam asks what each network service is for, not how to design a network, plan addresses or trace packets. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Inside the VPC

- **Address planning and CIDR notation.** How `10.0.0.0/16` and `/24` describe address ranges, how to split a VPC into subnets, and why connected networks must not overlap. See [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) and [REL02-BP05 Enforce non-overlapping private IP address ranges in all private address spaces where they are connected](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_non_overlap_ip.html).
- **Route table details.** The main route table, and how the most specific matching route wins. See [Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html).
- **Tracing packets and writing network ACL rules.** Ephemeral ports (1024 to 65535 covers every kind of client), rule numbering with gaps, rules for both halves of every conversation, and the fact that traffic inside one subnet doesn't cross its network ACL. See [Custom network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html). The module's old packet-journey simulation practiced this.
- **NAT gateway design and cost.** One zonal NAT gateway per AZ for resilience, the Regional NAT gateway, and working out a month's bill. See [Pricing for NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html) and [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).
- **Interface endpoint and PrivateLink details.** Hourly charges per AZ, and publishing your own service as an endpoint service behind a Network Load Balancer. See [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/) and [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
- **Network layers in Well-Architected terms.** [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) and [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html).

## At the edge

- **All of Route 53's routing policies and records.** Simple, geoproximity, IP-based and multivalue answer routing; alias records for a bare domain; private hosted zones; how a record's time to live (TTL) delays a switch; and Route 53 VPC Resolver. See [Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) and the [Amazon Route 53 FAQs](https://aws.amazon.com/route53/faqs/).
- **CloudFront in depth.** Cache lifetimes, invalidations, geo restriction, signed URLs, the flat-rate pricing plans, and fixed anycast addresses on request. See the [Amazon CloudFront FAQs](https://aws.amazon.com/cloudfront/faqs/) and [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/).
- **API Gateway in depth.** REST, HTTP and WebSocket APIs, usage plans and API keys, stages, and caching. See the [Amazon API Gateway FAQs](https://aws.amazon.com/api-gateway/faqs/).
- **Pricing of the edge services.** Route 53's hosted zone and query charges, Global Accelerator's hourly fee, and API Gateway's per-call pricing. See [Route 53 pricing](https://aws.amazon.com/route53/pricing/) and [Global Accelerator pricing](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-pricing.html).

## Links to offices and networks

- **VPN and Direct Connect details.** The customer gateway device and virtual private gateway, tunnel bandwidth, accelerated Site-to-Site VPN, Client VPN authorization rules, dedicated and hosted Direct Connect connections, MACsec, and planned maintenance. See the [AWS VPN FAQs](https://aws.amazon.com/vpn/faqs/) and the [AWS Direct Connect FAQs](https://aws.amazon.com/directconnect/faqs/).
- **Redundant hybrid connectivity.** A second Direct Connect location, or a VPN as backup. See [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ha_conn_private_networks.html) and [PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.html).
- **Peering and Transit Gateway in depth.** Why a peered VPC can't use its peer's gateways, Transit Gateway route tables, and hub-and-spoke design. See [How VPC peering connections work](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html) and [REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_prefer_hub_and_spoke.html).
- **Costing links and data transfer.** Hourly prices of VPN connections, Transit Gateway attachments and Client VPN, and estimating a month of data transfer. See [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/) and [COST08-BP01 Perform data transfer modeling](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_modeling.html).

## Out of the exam's scope

AWS Network Firewall, Amazon VPC Lattice, AWS Network Access Analyzer and AWS Cloud Map are on the exam guide's out-of-scope list; recognize them as wrong answers.

---

"Module 07: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
