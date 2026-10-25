---
type: page
id: clf-03-08
title: "Module 03: beyond the exam"
reader: "Adult who has finished Module 03 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-03-00]
pillars: [reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html"
  - "https://aws.amazon.com/compliance/digital-sovereignty/"
  - "https://aws.amazon.com/what-is/latency/"
  - "https://aws.amazon.com/ec2/pricing/on-demand/"
  - "https://aws.amazon.com/rds/pricing/"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
  - "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html"
  - "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions.html"
---

# Module 03: what we left out, and where to read it

The CLF-C02 exam asks how Regions, Availability Zones and edge locations relate, and which one fits a need, not how to design around them. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Regions and Availability Zones

- **AZ names and AZ IDs.** In AWS's oldest Regions, accounts created before November 2025 have their AZ names, such as `us-east-1a`, mapped to physical AZs separately, so two accounts' `us-east-1a` may differ; the AZ ID, such as `use1-az1`, means the same place in every account. [Lab 02](05-lab-02-see-the-global-infrastructure.md) shows your mapping. See [AWS Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html).
- **Zonal, Regional and global services in depth.** How each kind of service fails, and how to keep one AZ's failure from spreading. See the [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) whitepaper.
- **Opt-in Regions and the newer sign-up path.** How to enable or disable Regions, and the Region that the newer sign-up experience assigns. See [Enable or disable AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) and [AWS Regions for your projects](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html).

## Choosing a Region

- **The physics of latency.** Light in fiber takes about 4.9 microseconds per kilometer, so distance alone puts a floor under every round trip. See [What is latency?](https://aws.amazon.com/what-is/latency/)
- **Data transfer costs.** Prices for data sent to the internet differ by Region; copying data between Regions, and between EC2 and RDS in different AZs, is billed per GB. See [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/) (data transfer) and [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).
- **Sovereignty offerings.** The AWS European Sovereign Cloud, a separate AWS cloud for Europe, and Dedicated Local Zones for one customer or community. See [Digital Sovereignty](https://aws.amazon.com/compliance/digital-sovereignty/).
- **A Region's carbon footprint.** The sustainability pillar suggests weighing it alongside business needs: [SUS01-BP01 Choose Region based on both business requirements and sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html).

## Surviving failure

- **Building and testing a DR plan.** Hot standby as a variant of active/active, infrastructure as code for backup and restore, failover with Route 53 health checks, and rehearsing recovery. See [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) and [Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).
- **Well-Architected practices for recovery.** [REL13-BP01 Define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html), [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) and [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html) belong to designing workloads, not to this exam.

## The edge

- **Code and filtering at the edge.** CloudFront Functions and Lambda@Edge run small pieces of code near viewers, and AWS WAF and AWS Shield Advanced work at the edge when used with CloudFront. See [Customize at the edge with functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions.html).
- **Route 53 routing policies.** Latency-based, geolocation, failover and others. See [Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html). Module 07 covers Route 53 and CloudFront for the exam.
- **AWS Wavelength.** Compute inside telecom carriers' 5G networks, out of scope for CLF-C02. See [What is AWS Wavelength?](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)

---

"Module 03: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
