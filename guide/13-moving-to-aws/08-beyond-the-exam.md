---
type: page
id: clf-13-08
title: "Module 13: beyond the exam"
reader: "Adult who has finished Module 13 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-13-00]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html"
  - "https://aws.amazon.com/migration-acceleration-program/"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html"
  - "https://aws.amazon.com/application-migration-service/faqs/"
  - "https://aws.amazon.com/migration-evaluator/faqs/"
  - "https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html"
  - "https://aws.amazon.com/windows/resources/licensing/"
  - "https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing.html"
---

# Module 13: what we left out, and where to read it

The CLF-C02 exam asks which framework part, migration strategy or tool fits a situation, not how to run a migration. These topics go deeper, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## The Cloud Adoption Framework

- **All 47 capabilities and their stakeholders.** Each perspective has seven to nine capabilities, from data monetization in Business to data curation in Governance, each with its common stakeholders. See [Foundational capabilities](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html).
- **Migration Readiness Assessment and the AWS Migration Acceleration Program (MAP).** The assessment uses the CAF to find how ready an organization is to migrate. MAP runs large migrations in three phases (assess, mobilize, and migrate and modernize) and offers tools, training, partner expertise and funding; check its current terms. See [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/strategy-migration/strategy-migration.pdf) and the [MAP page](https://aws.amazon.com/migration-acceleration-program/).

## Migration strategies

- **AWS's full retire and retain criteria.** AWS defines a zombie application as averaging below 5% CPU and memory use, and an idle one as 5 to 20% over 90 days; mainframe, mid-range and non-x86 Unix systems are another reason to retain. See [About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html).
- **Migration waves.** Large migrations move applications in groups, starting with simpler ones, and keep refactoring for after the move. See the same guide.
- **VMware on AWS.** Amazon Elastic VMware Service runs VMware's software on AWS for relocating; rehosting the virtual machines onto EC2 is the other route. See [Migrate VMware to the cloud](https://aws.amazon.com/vmware/aws-services/).

## Migration tools

- **How Application Migration Service works, and what it costs.** An agent copies disks block by block into a low-cost staging area; you launch test instances, then cut over. Each source server gets 2,160 free hours of replication (90 days), then an hourly charge, plus the AWS resources it uses (as of 2026-10-24). See the [AWS Transform MGN FAQs](https://aws.amazon.com/application-migration-service/faqs/).
- **AWS Transform.** The AI-agent service AWS points new customers to for discovery, planning and tracking. See [AWS Transform](https://aws.amazon.com/transform/).
- **Migration Evaluator in detail.** An agentless collector runs on one Windows Server virtual machine; it covers x86 servers only and doesn't map dependencies; AWS's migration solutions architects help prepare the full business case. See the [Migration Evaluator FAQs](https://aws.amazon.com/migration-evaluator/faqs/).
- **Planning a large file transfer.** Transfer time is terabytes × 8,000,000 ÷ (link speed in Mbps × the share of the link you use) seconds; DataSync tasks take bandwidth limits, and DataSync bills per gigabyte copied, among other charges. See [Setting bandwidth limits](https://docs.aws.amazon.com/datasync/latest/userguide/configure-bandwidth.html) and [DataSync pricing](https://aws.amazon.com/datasync/pricing/).

## Rightsizing and licensing

- **Compute Optimizer's requirements and options.** It needs at least 30 hours of metrics for an EC2 instance, sees memory only with the CloudWatch agent, looks back 14 days by default or 32 if you choose, and up to 93 days with paid enhanced infrastructure metrics. It can also flag a SQL Server Enterprise license that uses no Enterprise features. See [Resource requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) and [License recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html).
- **Microsoft license routes.** With active Software Assurance, License Mobility lets eligible products such as SQL Server (not Windows Server) run on shared instances. Without it, Microsoft licenses can come only to Dedicated Hosts, and only if bought before 2019-10-01 (or added as a true-up under an Enterprise Enrollment effective before then). RDS for SQL Server accepts your own SQL Server 2019 or later licenses with active Software Assurance. See [Microsoft licensing on AWS](https://aws.amazon.com/windows/resources/licensing/), [SQL Server licensing on EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing.html) and [Licensing SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.Licensing.html).
- **Pricing the license options.** A Dedicated Host bills for the whole server (an m7i host has 96 physical cores), so BYOL on a host pays off only when you can fill it, and licenses counted per core may have to cover every core on it. See [Dedicated Hosts pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/) and [Amazon EC2 On-Demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/).

## Well-Architected practices for a migration

Finance and engineers building the case together ([COST01-BP02 Establish a partnership between finance and technology](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_partnership.html)), choosing licensing with cost in mind ([COST05-BP04 Select software with cost-effective licensing](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_licensing.html)) and sizing from data ([COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html)) belong to running a migration, not to this exam.

---

"Module 13: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
