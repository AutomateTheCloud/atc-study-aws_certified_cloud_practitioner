---
type: page
id: clf-12-08
title: "Module 12: beyond the exam"
reader: "Adult who has finished Module 12 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-12-00]
pillars: [operational-excellence, security, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/premiumsupport/pricing/"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/case-management.html"
  - "https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html"
  - "https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html"
  - "https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html"
  - "https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html"
  - "https://aws.amazon.com/partners/paths/"
  - "https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html"
---

# Module 12: what we left out, and where to read it

The CLF-C02 exam asks which Support plan, tool or source of help fits a need, not how to run them day to day. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Support plans and cases

- **Working out a plan's fee.** Each paid plan charges the greater of its minimum and a falling percentage of your monthly charges, worked out before credits and discounts; Business Support+ per account, Enterprise across the accounts you enroll. See [AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/).
- **What else the higher plans include.** Enterprise Support adds strategic business reviews and AWS Countdown help around launches and migrations; Unified Operations adds personalized runbooks and a Senior Billing and Account Specialist, and you sign up through AWS sales. See [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/).
- **The Shield Response Team.** DDoS help needs AWS Shield Advanced as well as a qualifying plan, and when we checked (2026-10-24) AWS's page still named the retiring Business Support plan. Check it before you rely on it: [AWS Shield Response Team support](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html).
- **Running cases well.** AI troubleshooting before a case, changing a case's severity later (paid plans only), and the AWS Support API. See [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html).

## Watching your account

- **Trusted Advisor in operations.** Automatic refresh, the Trusted Advisor API and alerts through Amazon EventBridge on paid plans, and how the checks support Well-Architected practices such as [REL01-BP04 Monitor and manage quotas](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_monitor_manage_limits.html). See [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html).
- **Routing AWS Health events.** Sending Health events through EventBridge to a chat channel or an automated fix, and the Health API for your own tools. See [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)

## Sources of answers and security incidents

- **re:Post Private.** A separate, private knowledge site for one organization's teams; AWS has announced its end of support on 2027-06-30 (checked 2026-10-24). See [re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).
- **When someone breaks into your account.** Open a case from the affected account, marked as an urgent security incident; the AWS Customer Incident Response Team (AWS CIRT) can help at no extra charge on any plan. See [Security incident response and resources](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/security-incident-response-and-resources.html) and [primer page 08](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/08-when-something-goes-wrong.md).
- **Checking an address.** AWS publishes its IP ranges as a file, `ip-ranges.json`, that you can search. See [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html).

## Partners and Marketplace

- **Partner Paths.** AWS now groups partners into Software, Hardware, Services, Training and Distribution paths, which replaced the older "Technology Partner" and "Consulting Partner" types. See [AWS Partner Paths](https://aws.amazon.com/partners/paths/).
- **Finding a partner.** The AWS Partner Solutions Finder searches by industry, use case and AWS Specialization, such as AWS Competency or AWS Managed Service Provider. See [Work with an AWS Partner](https://aws.amazon.com/partners/work-with-partners/).
- **Marketplace in depth.** Product types (machine images, SaaS, CloudFormation templates, AWS WAF rules, professional services) and how Procurement insights and License Manager work across an organization. See [What is AWS Marketplace?](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html)
- **Training for everyone.** AWS Skill Builder offers digital courses, many free, with labs in a paid subscription. See [AWS Training and Certification](https://aws.amazon.com/training/).

## Well-Architected practices for getting help

Choosing a plan before production depends on it ([OPS07-BP06 Create support plans for production workloads](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_enable_support_plans.html)), writing down where each problem goes ([OPS10-BP04 Define escalation paths](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_define_escalation_paths.html)), keeping a list of contacts for security events ([SEC10-BP01 Identify key personnel and external resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_identify_personnel.html)) and checking that third-party agreements pay their way ([COST07-BP03 Select third-party agreements with cost-efficient terms](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_third_party.html)) belong to running workloads, not to this exam.

---

"Module 12: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
