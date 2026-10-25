---
type: page
id: clf-02-09
title: "Module 02: beyond the exam"
reader: "Adult who has finished Module 02 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-02-00]
pillars: [reliability, cost-optimization, operational-excellence]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/what-is-cloud-computing/"
  - "https://aws.amazon.com/what-is/high-availability/"
  - "https://docs.aws.amazon.com/pdfs/wellarchitected/latest/cost-optimization-pillar/wellarchitected-cost-optimization-pillar.pdf"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html"
  - "https://aws.amazon.com/architecture/well-architected/"
---

# Module 02: what we left out, and where to read it

The CLF-C02 exam asks which cloud concept or benefit fits a situation, not how to cost or design a system. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Cloud computing and its benefits

- **IaaS, PaaS and SaaS.** AWS also sorts cloud services by how much the provider runs for you: infrastructure as a service (building blocks you manage), platform as a service (a place to run your code) and software as a service (a finished application). See [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- **Availability arithmetic.** Each extra nine allows a tenth of the downtime: over a year, 99.9% allows about 8.8 hours, 99.99% about 53 minutes and 99.999% about 5 minutes. See [What is high availability?](https://aws.amazon.com/what-is/high-availability/)
- **Following demand hour by hour.** Real demand changes by the hour, and new servers take minutes to start, so real systems scale in smaller steps and keep a little spare capacity. Module 06 shows how auto scaling does it; tuning it is design work.

## Cloud economics

- **Costing a move in detail.** A full comparison prices every on-premises cost over the equipment's life, including the next hardware refresh, and follows the cash month by month: owning pays a large share up front, while the cloud pays as it goes. Module 11 shows the AWS Pricing Calculator; the [Cost Optimization Pillar](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/cost-optimization-pillar/wellarchitected-cost-optimization-pillar.pdf) is AWS's full guide to avoiding cloud waste.
- **Cost best practices behind rightsizing and automation.** [COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html), [COST09-BP03 Supply resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html), [COST11-BP01 Perform automation for operations](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_cost_effort_automations_operations.html), and [COST01-BP02 Establish a partnership between finance and technology](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_partnership.html) for building the comparison together.

## The Well-Architected Framework in depth

- **Best-practice IDs.** An ID such as [SEC02-BP01 Use strong sign-in mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_enforce_mechanisms.html) names the pillar (SEC), its question (02) and the practice (BP01); the other prefixes are OPS, REL, PERF, COST and SUS. The guardrails primer and the labs tag their steps this way. See [The pillars of the framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html).
- **Every pillar's design principles.** Each pillar has its own list, beyond the one per pillar the lesson quotes: [operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html), [security](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html), [reliability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html), [performance efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html), [cost optimization](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) and [sustainability](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-design-principles.html).
- **Designing for a seasonal peak.** Paying for extra copies in more AZs only in the busy months, as the reliability principle "[Scale horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" and [COST09-BP03](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html) suggest together, is architecture design, which the exam leaves out.
- **Lenses and the review itself.** Lenses add questions for particular kinds of workload or industry; a review in the Well-Architected Tool records answers, high-risk and medium-risk issues, and milestones. Module 14 walks through one. See [What is AWS Well-Architected?](https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html)
- **The Well-Architected Agent.** As of 2026-10-23, AWS offered an AI-based AWS Well-Architected Agent in preview, a companion to the Tool. It isn't in the CLF-C02 exam guide. See [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/).

---

"Module 02: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
