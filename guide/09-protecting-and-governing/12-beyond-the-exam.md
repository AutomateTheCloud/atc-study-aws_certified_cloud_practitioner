---
type: page
id: clf-09-12
title: "Module 09: beyond the exam"
reader: "Adult who has finished Module 09 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-09-00]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html"
  - "https://docs.aws.amazon.com/config/latest/developerguide/delete-config-data-with-retention-period.html"
  - "https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html"
  - "https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html"
  - "https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html"
  - "https://aws.amazon.com/security/ddos-simulation-testing/"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html"
  - "https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html"
---

# Module 09: what we left out, and where to read it

The CLF-C02 exam asks which security, governance or compliance service fits a need, not how to configure it or run an investigation. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Logging and evidence

- **Organization trails and log integrity.** A trail created from an organization's management account logs every member account, and members can't change it; log file integrity validation proves files weren't altered. See [How CloudTrail works](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html).
- **CloudTrail Lake.** CloudTrail's SQL query feature has been closed to new customers since 2026-05-31; AWS points them to Amazon CloudWatch. See the [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).
- **Running AWS Config.** The configuration recorder, retention from 30 days to 7 years, automatic remediation, and pricing per item recorded and per rule evaluation. See [Deleting AWS Config data](https://docs.aws.amazon.com/config/latest/developerguide/delete-config-data-with-retention-period.html) and [Config pricing](https://aws.amazon.com/config/pricing/).
- **Access report limits and IAM Access Analyzer.** Last accessed information can lag about four hours and counts attempts; Access Analyzer's unused access findings are charged. See [Refine permissions using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html).

## Keys and certificates

- **KMS in depth.** Data keys and how services use them, rotation every 365 days by default, a 7-to-30-day waiting period before a key is deleted, request charges, and S3 Bucket Keys, which cut KMS calls but change what CloudTrail shows. See [Rotate AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [Delete an AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) and [S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html).
- **Encrypting an existing RDS database.** Encryption is chosen at creation; adding it later means restoring from an encrypted snapshot copy. See [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).
- **CloudHSM clusters and custom key stores.** Spreading HSMs across Availability Zones, and keeping KMS keys in your own cluster. See [AWS CloudHSM clusters](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html).
- **ACM details and requiring HTTPS.** Certificates for CloudFront come from US East (N. Virginia); exportable certificates cost extra; a bucket policy with `aws:SecureTransport` refuses plain HTTP. See [ACM pricing](https://aws.amazon.com/certificate-manager/pricing/) and [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html).

## Detection and response

- **GuardDuty protection plans and finding types,** Inspector's risk scores, Detective's behavior graph, and the unified Security Hub's exposure findings and attack paths. See [GuardDuty finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) and [Introduction to AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html).
- **Incident response.** Alerting through EventBridge, containing a compromised server, and written playbooks. See [SEC10-BP04 Develop and test security incident response playbooks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html).

## The front door

- **Shield Advanced details.** Since 2026-03-26, AWS's default protection against HTTP floods is the Anti-DDoS managed rule group in AWS WAF; Shield Advanced's older automatic mitigation continues for existing customers. See [Automating application layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html).
- **WAF and Firewall Manager in practice.** Bot Control, CAPTCHA, pricing per rule and request, the end of AWS WAF Classic on 2026-10-07, and Firewall Manager's $100 per policy per Region (as of 2026-10-24). See [AWS WAF pricing](https://aws.amazon.com/waf/pricing/) and [Firewall Manager pricing](https://aws.amazon.com/firewall-manager/pricing/).
- **Security testing.** Which tests need AWS's approval first, and DDoS simulations through approved partners. See the [penetration testing policy](https://aws.amazon.com/security/penetration-testing/) and [DDoS simulation testing policy](https://aws.amazon.com/security/ddos-simulation-testing/).
- **Designing for DDoS resilience.** See [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.html).

## Governance

- **Resource control policies (RCPs),** which cap what anyone can do to resources in member accounts. See [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html).
- **Writing and rolling out SCPs.** Exempting global services from a Region rule, why detaching FullAWSAccess can block everything, and testing on a small OU first. See [SCP examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html).
- **Control Tower controls.** Preventive, detective and proactive controls, and designing your own landing zone. See [How controls work](https://docs.aws.amazon.com/controltower/latest/userguide/how-controls-work.html).

## Well-Architected practices for security

Traceability ([SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html)), key management ([SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html)) and permission guardrails ([SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html)) belong to designing workloads, not to this exam.

---

"Module 09: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
