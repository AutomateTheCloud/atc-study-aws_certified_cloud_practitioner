---
type: page
id: clf-06-09
title: "Module 06: beyond the exam"
reader: "Adult who has finished Module 06 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-06-00]
pillars: [performance-efficiency, reliability, cost-optimization, security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html"
  - "https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html"
  - "https://aws.amazon.com/autoscaling/faqs/"
  - "https://aws.amazon.com/fargate/pricing/"
  - "https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html"
  - "https://aws.amazon.com/elasticbeanstalk/faqs/"
  - "https://aws.amazon.com/outposts/rack/faqs/"
---

# Module 06: what we left out, and where to read it

The CLF-C02 exam asks which compute service fits a need, not how to configure it. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Amazon EC2

- **Reading an instance type's name.** In `m7g.large`, `m` is the series, `7` the generation, `g` an option (here an AWS Graviton processor), and `large` the size. See [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html).
- **Pricing an instance.** Comparing families at the same size, a year On-Demand against a Reserved Instance, and the monthly bill for a running, stopped or terminated instance. See [EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/); Module 11 covers purchasing options.
- **Free Tier eligible types.** For accounts created on or after 2025-07-15, AWS marks `t3.micro`, `t3.small`, `t4g.micro`, `t4g.small`, `c7i-flex.large` and `m7i-flex.large` as eligible (checked 2026-10-24). See [Track your Free Tier usage for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html).
- **Signing in without opening SSH.** EC2 Instance Connect uses your IAM identity and a short-lived key and logs each connection in CloudTrail. See [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html).

## Auto Scaling and load balancing

- **Scaling ahead of a rush.** Predictive scaling forecasts 48 hours ahead and can start instances early; a scheduled action raises capacity at a set time. See the [AWS Auto Scaling FAQs](https://aws.amazon.com/autoscaling/faqs/).
- **Which health checks a group uses.** By default a group judges health by EC2's status checks; turning on Elastic Load Balancing health checks makes it replace instances whose application fails. See [Health checks for your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html).
- **The other scaling services.** Application Auto Scaling scales other services' resources one at a time, such as DynamoDB tables and ECS services. See [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)
- **Load balancer pricing.** An hourly charge plus capacity units for traffic. See [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/).

## Containers and serverless

- **Middle options for containers.** ECS Managed Instances and EKS Auto Mode are EC2 instances that AWS also provisions, patches and scales. See [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- **Fargate details.** Each task gets 20 GiB of temporary storage that is erased when it stops; Fargate Spot runs interruptible tasks at up to 70% off; billing is per second with a 1-minute minimum. See [AWS Fargate pricing](https://aws.amazon.com/fargate/pricing/) and the [Fargate FAQs](https://aws.amazon.com/fargate/faqs/).
- **Lambda limits and costs.** Memory from 128 MB to 10,240 MB; by default up to 1,000 concurrent runs per Region, a quota you can ask to raise; a monthly free allowance of 1 million requests and 400,000 GB-seconds; and the point where a busy server becomes cheaper than pay per use. See [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) and [Lambda pricing](https://aws.amazon.com/lambda/pricing/).
- **Newer Lambda forms.** Longer-running forms such as MicroVMs that last up to 8 hours and durable functions that pause and resume (checked 2026-10-24). See [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

## The simpler paths

- **Elastic Beanstalk in depth.** Standard mode on EC2 and Cluster mode on EKS; managed platform updates in a weekly maintenance window, with major upgrades yours to start. See the [Elastic Beanstalk FAQs](https://aws.amazon.com/elasticbeanstalk/faqs/).
- **Lightsail prices.** Plans, transfer allowances, and how a bundle compares with the same parts on EC2. See [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).
- **Batch compute environments.** Managed environments, where AWS provisions the servers, and unmanaged ones, where you run them. See the [AWS Batch FAQs](https://aws.amazon.com/batch/faqs/).
- **Outposts hardware and terms.** 42U racks or smaller servers, a service link to the Region, and rack terms of one, three or five years (checked 2026-10-23). See the [Outposts racks FAQs](https://aws.amazon.com/outposts/rack/faqs/).

## Well-Architected practices for compute

Choosing compute from data ([PERF02-BP01 Select the best compute options for your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html), [COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html)), scaling it with demand ([PERF02-BP05 Scale your compute resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_scale_compute_resources_dynamically.html)) and healing it automatically ([REL11-BP03 Automate healing on all layers](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_auto_healing_system.html)) belong to designing workloads, not to this exam.

---

"Module 06: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
