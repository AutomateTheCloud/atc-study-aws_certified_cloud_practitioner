---
type: page
id: clf-04-11
title: "Module 04: beyond the exam"
reader: "Adult who has finished Module 04 and wants to know what it left out; about 5 minutes"
prerequisites: [clf-04-00]
pillars: [security, reliability, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html"
  - "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html"
  - "https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html"
  - "https://aws.amazon.com/secrets-manager/pricing/"
---

# Module 04: what we left out, and where to read it

The CLF-C02 exam asks who is responsible for a task and which identity, policy or sign-in fits a need, not how to write or debug policies. These topics go deeper than the exam does, so the module leaves them out. Later, higher-level courses in this series will cover them; until then, each line names the AWS page to read.

## Writing and evaluating policies

- **Policy grammar.** A JSON policy has a `Version` (AWS recommends `2012-10-17`), optional `Sid` labels, and statements with `Effect`, `Action` (written `service:action`), `Resource` (an Amazon Resource Name, or ARN) and an optional `Condition`, such as `aws:MultiFactorAuthPresent`. Browsing to a bucket in the console also needs `s3:ListAllMyBuckets`. See [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
- **The full evaluation logic.** Besides identity-based and resource-based policies, some policy types only set limits and grant nothing: service control policies (SCPs) in AWS Organizations, permissions boundaries, session policies and resource control policies. When one applies, it must allow the request too. Within one account, an allow in a resource-based policy alone can be enough; across two accounts, both sides must allow. See [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).
- **SCPs and the root user.** An SCP caps everyone in a member account, its root user included, but doesn't apply to the organization's management account. Module 09 introduces SCPs. See [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).
- **How roles work inside.** A role's trust policy (a resource-based policy) says who may assume it; its permissions policy says what it may do; the caller needs permission for `sts:AssumeRole`. Service-linked roles are roles an AWS service creates and owns to act for you. See the [cross-account tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) and [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).
- **Policy tools in depth.** IAM Access Analyzer runs over 100 policy checks, can draft a policy from an identity's CloudTrail activity, and charges for each "Check for new access" run; last accessed information shows which services an identity has used. The policy simulator's results can differ from the live account. See [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) and [the policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html). [Optional lab 04](07-lab-04-finish-and-fix-a-policy.md) practices validation and an explicit deny.

## Credentials and identity services

- **Password policy settings.** As of 2026-10-23, the default asks for 8 to 128 characters with three of four character types and never expires passwords; a custom policy can expire them after 1 to 1,095 days and block reuse of the last 1 to 24. See [Set an account password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html).
- **Credential limits and lifetimes.** Each user can register up to eight MFA devices and have at most two access keys, whose secret is shown only once. `aws login` (AWS CLI 2.32.0 or later) renews credentials every 15 minutes for up to 12 hours; a CloudShell session lasts about 12 hours at most. See [Temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html).
- **Identity service details.** Cognito user pools sign app users in, and identity pools swap that sign-in for temporary AWS credentials. Directory Service offers AWS Managed Microsoft AD and AD Connector; Simple AD has been closed to new customers since 2026-07-30. IAM itself can federate one account with a SAML 2.0 or OIDC identity provider. See [What is Amazon Cognito?](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) and [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html).
- **Identity Center instance types.** An organization instance gives console access to accounts but needs AWS Organizations; an account instance doesn't, and has no access portal to AWS accounts. See [Organization and account instances](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html).
- **Secrets Manager pricing.** It charges per secret per month plus API calls; standard Parameter Store parameters have no additional charge. See [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/).

## The same split beyond security

AWS splits resilience the same way, of and in the cloud, in [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/pdfs/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.pdf), and sustainability in the [Sustainability Pillar](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/sustainability-pillar/wellarchitected-sustainability-pillar.pdf).

## Well-Architected practices for access

Mapping each control to a side ([SEC01-BP03 Identify and validate control objectives](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_control_objectives.html)), relying on a central identity provider ([SEC02-BP04 Rely on a centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html)), reducing permissions over time ([SEC03-BP04 Reduce permissions continuously](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_continuous_reduction.html)) and reviewing cross-account access ([SEC03-BP07 Analyze public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html)) belong to running security programs, not to this exam.

---

"Module 04: beyond the exam" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
