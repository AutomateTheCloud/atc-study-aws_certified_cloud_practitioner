# Contents

The guide's pages in reading order. Module 01 is optional: take it if you are new to IT.

Look up any term in the [glossary](99-reference/01-glossary.md).

Before your first lab, work through the [guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md).

## Start here

- [Welcome](00-start-here/01-welcome.md) · Lesson
- [How to study with this guide](00-start-here/02-how-to-study-with-this-guide.md) · Lesson
- [The exam at a glance](00-start-here/03-the-exam-at-a-glance.md) · Reference
- [AWS changes fast](00-start-here/04-aws-changes-fast.md) · Lesson
- [Before your first lab](00-start-here/05-before-your-first-lab.md) · Task card

## Module 01: On-ramp: IT foundations (optional)

- [Module 01: On-ramp: IT foundations (optional)](01-on-ramp/00-brief.md) · Module brief
- [Computers and servers](01-on-ramp/01-computers-and-servers.md) · Lesson
- [Networks, IP addresses, DNS and HTTPS](01-on-ramp/02-networks-ip-dns-https.md) · Lesson
- [Files vs databases](01-on-ramp/03-files-vs-databases.md) · Lesson
- [Data centers and virtualization](01-on-ramp/04-data-centers-and-virtualization.md) · Lesson
- [APIs, the command line and JSON](01-on-ramp/05-apis-command-line-and-json.md) · Lesson
- [Everyday security: passwords, MFA, encryption and least privilege](01-on-ramp/06-everyday-security.md) · Lesson

## Module 02: Why organizations use the cloud

- [Module 02: Why organizations use the cloud](02-why-the-cloud/00-brief.md) · Module brief
- [What cloud computing is](02-why-the-cloud/01-what-cloud-computing-is.md) · Lesson
- [Before and after: the demand curve](02-why-the-cloud/02-before-and-after-the-demand-curve.md) · Lesson
- [Telling the benefits apart](02-why-the-cloud/03-telling-the-benefits-apart.md) · Lesson
- [What a data center really costs](02-why-the-cloud/04-what-a-data-center-really-costs.md) · Lesson
- [The Well-Architected Framework](02-why-the-cloud/05-the-well-architected-framework.md) · Lesson
- [Lab 01: Create, find and delete your first storage bucket](02-why-the-cloud/06-lab-01-first-resource.md) · Lab
- [Simulation S1: Finish the bakery's cost comparison](02-why-the-cloud/07-sim-demand-curve.md) · Simulation

## Module 03: AWS around the world

- [Module 03: AWS around the world](03-aws-around-the-world/00-brief.md) · Module brief
- [Regions, Availability Zones and data centers](03-aws-around-the-world/01-regions-availability-zones-data-centers.md) · Lesson
- [Choosing a Region](03-aws-around-the-world/02-choosing-a-region.md) · Lesson
- [Surviving failure](03-aws-around-the-world/03-surviving-failure.md) · Lesson
- [The edge](03-aws-around-the-world/04-the-edge.md) · Lesson
- [Lab 02: See Regions, Availability Zones and AWS Health in your own account](03-aws-around-the-world/05-lab-02-see-the-global-infrastructure.md) · Lab
- [Simulation S2: The blast-radius ladder and three recovery plans](03-aws-around-the-world/06-sim-blast-radius.md) · Simulation

## Module 04: Who secures what

- [Module 04: Who secures what: shared responsibility and access](04-shared-responsibility-and-access/00-brief.md) · Module brief
- [Security of the cloud vs security in the cloud](04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md) · Lesson
- [Shared, inherited and customer-specific controls](04-shared-responsibility-and-access/02-shared-inherited-customer-specific.md) · Lesson
- [Identities](04-shared-responsibility-and-access/03-identities.md) · Lesson
- [Policies and least privilege](04-shared-responsibility-and-access/04-policies-and-least-privilege.md) · Lesson
- [Credentials and federation](04-shared-responsibility-and-access/05-credentials-and-federation.md) · Lesson
- [Lab 03: Give a group read-only access to one bucket, and test it in the policy simulator](04-shared-responsibility-and-access/06-lab-03-a-group-and-a-policy.md) · Lab
- [Lab 04: Finish a policy, write one yourself, and find the deny that blocks it](04-shared-responsibility-and-access/07-lab-04-finish-and-fix-a-policy.md) · Lab
- [Simulation S3: Slide the line from your own servers to Amazon S3](04-shared-responsibility-and-access/08-sim-responsibility-slider.md) · Simulation
- [Simulation S4: Predict allow or deny across accounts, boundaries and organizations](04-shared-responsibility-and-access/09-sim-policy-playground.md) · Simulation

## Module 05: Storing data

- [Module 05: Storing data: storage and databases](05-storing-data/00-brief.md) · Module brief
- [Block, file and object storage](05-storing-data/01-block-file-object.md) · Lesson
- [S3 in practice](05-storing-data/02-s3-in-practice.md) · Lesson
- [Storage classes and lifecycle](05-storing-data/03-storage-classes-and-lifecycle.md) · Lesson
- [Hybrid storage and backup](05-storing-data/04-hybrid-storage-and-backup.md) · Lesson
- [Managed or self-managed databases](05-storing-data/05-managed-or-self-managed-databases.md) · Lesson
- [Choosing a database](05-storing-data/06-choosing-a-database.md) · Lesson
- [Lab 05: Keep every version, add a lifecycle rule, and set up an archive bucket](05-storing-data/07-lab-05-versions-and-lifecycle.md) · Lab
- [Lab 06: Create a DynamoDB table for shopping carts, put and get items, and delete it](05-storing-data/08-lab-06-a-dynamodb-table.md) · Lab
- [Simulation S5: Run a year of lifecycle rules forward and find the cost traps](05-storing-data/09-sim-lifecycle-cost-timeline.md) · Simulation
- [Simulation S6: Multi-AZ, read replica or backup: protect the order database](05-storing-data/10-sim-multi-az-vs-read-replica.md) · Simulation

## Module 06: Running applications

- [Module 06: Running applications: compute](06-running-applications/00-brief.md) · Module brief
- [Amazon EC2: instances, images and instance types](06-running-applications/01-ec2.md) · Lesson
- [Auto Scaling and load balancers](06-running-applications/02-auto-scaling-and-load-balancers.md) · Lesson
- [Containers and serverless](06-running-applications/03-containers-and-serverless.md) · Lesson
- [Simpler paths: Elastic Beanstalk, Lightsail, Batch and Outposts](06-running-applications/04-simpler-paths.md) · Lesson
- [Lab 07: Run a Lambda function, read its logs, and stop them piling up](06-running-applications/05-lab-07-a-lambda-function.md) · Lab
- [Lab 08: Launch a virtual server, stop it, terminate it, and prove nothing is left](06-running-applications/06-lab-08-launch-and-terminate-an-instance.md) · Lab
- [Simulation S7: Scale the bakery's web servers through a December Saturday](06-running-applications/07-sim-elasticity-with-auto-scaling.md) · Simulation

## Module 07: Connecting it

- [Module 07: Connecting it: networks and the edge](07-connecting-it/00-brief.md) · Module brief
- [Your own network](07-connecting-it/01-your-own-network.md) · Lesson
- [Filtering traffic](07-connecting-it/02-filtering-traffic.md) · Lesson
- [Names and the edge](07-connecting-it/03-names-and-the-edge.md) · Lesson
- [Connecting networks and offices](07-connecting-it/04-connecting-networks-and-offices.md) · Lesson
- [Lab 09: Build a small network with a public and a private subnet, then take it apart](07-connecting-it/05-lab-09-build-a-small-vpc.md) · Lab
- [Simulation S8: Follow a packet and find the rule that blocks it](07-connecting-it/06-sim-packet-journey.md) · Simulation

## Module 08: Building and operating

- [Module 08: Building and operating](08-building-and-operating/00-brief.md) · Module brief
- [Four ways in](08-building-and-operating/01-four-ways-in.md) · Lesson
- [IaC and automation](08-building-and-operating/02-iac-and-automation.md) · Lesson
- [Watching workloads](08-building-and-operating/03-watching-workloads.md) · Lesson
- [Connecting parts, shipping software](08-building-and-operating/04-connecting-parts-shipping-software.md) · Lesson
- [Lab 10: Create the same bucket three ways: console, command line and template](08-building-and-operating/05-lab-10-same-bucket-three-ways.md) · Lab
- [Lab 11: Email the owner when the order function fails](08-building-and-operating/06-lab-11-alarm-on-errors.md) · Lab

## Module 09: Protecting, governing and proving compliance

- [Module 09: Protecting, governing and proving compliance](09-protecting-and-governing/00-brief.md) · Module brief
- [Who did what, how it runs, how it was set](09-protecting-and-governing/01-who-did-what.md) · Lesson
- [Encryption](09-protecting-and-governing/02-encryption.md) · Lesson
- [Finding threats and weaknesses](09-protecting-and-governing/03-finding-threats-and-weaknesses.md) · Lesson
- [The front door](09-protecting-and-governing/04-the-front-door.md) · Lesson
- [Compliance and governance](09-protecting-and-governing/05-compliance-and-governance.md) · Lesson
- [A defense map](09-protecting-and-governing/06-a-defense-map.md) · Lesson
- [Lab 12: Answer an auditor with evidence from your own account](09-protecting-and-governing/07-lab-12-answer-the-auditor.md) · Lab
- [Simulation S9: Match security findings to the service that raised them](09-protecting-and-governing/08-sim-security-findings-tour.md) · Simulation
- [Simulation S10: Read a resource's AWS Config timeline, and tell Config from CloudTrail](09-protecting-and-governing/09-sim-config-timeline.md) · Simulation
- [Simulation S11: Govern many accounts with OUs and SCPs, and pay one bill](09-protecting-and-governing/10-sim-organizations-and-scps.md) · Simulation

## Module 10: Data, AI and the rest of the catalog

- [Module 10: Data, AI and the rest of the catalog](10-data-ai-and-more/00-brief.md) · Module brief
- [Analytics in five verbs](10-data-ai-and-more/01-analytics-in-five-verbs.md) · Lesson
- [AI and machine learning](10-data-ai-and-more/02-ai-and-ml.md) · Lesson
- [People, apps and devices](10-data-ai-and-more/03-people-apps-and-devices.md) · Lesson
- [Lab 13: Query a small sales file in S3 with Athena, then delete everything](10-data-ai-and-more/04-lab-13-athena-query.md) · Lab
- [Lab 14 (optional): Have Amazon Polly read a product description aloud](10-data-ai-and-more/05-lab-14-polly-text-to-speech.md) · Lab
- [Simulation S12: Match each request to a service by what goes in and what comes out](10-data-ai-and-more/06-sim-input-output-matcher.md) · Simulation

## Module 11: Paying for AWS

- [Module 11: Paying for AWS](11-paying-for-aws/00-brief.md) · Module brief
- [How AWS charges](11-paying-for-aws/01-how-aws-charges.md) · Lesson
- [Purchasing options](11-paying-for-aws/02-purchasing-options.md) · Lesson
- [Estimate, watch, analyze](11-paying-for-aws/03-estimate-watch-analyze.md) · Lesson
- [Many accounts, one bill](11-paying-for-aws/04-many-accounts-one-bill.md) · Lesson
- [Lab 15: Price the bakery's setup in the AWS Pricing Calculator](11-paying-for-aws/05-lab-15-pricing-calculator.md) · Lab
- [Lab 16: Turn on cost allocation tags and find them in Cost Explorer](11-paying-for-aws/06-lab-16-cost-allocation-tags.md) · Lab
- [Simulation S13: Choose how to pay for each of the bakery's workloads](11-paying-for-aws/07-sim-purchasing-option-tree.md) · Simulation
- [Simulation S14: Follow a runaway cost and see which guardrails alert and which stop it](11-paying-for-aws/08-sim-guardrail-timeline.md) · Simulation

## Module 12: Getting help

- [Module 12: Getting help](12-getting-help/00-brief.md) · Module brief
- [Support plans](12-getting-help/01-support-plans.md) · Lesson
- [Tools that watch your account](12-getting-help/02-tools-that-watch-your-account.md) · Lesson
- [Where to find answers](12-getting-help/03-where-to-find-answers.md) · Lesson
- [Partners and paid help](12-getting-help/04-partners-and-paid-help.md) · Lesson
- [Lab 17: Tour the help every AWS account gets, on the Basic plan](12-getting-help/05-lab-17-support-center-tour.md) · Lab
- [Simulation S15: Choose the cheapest Support plan that fits](12-getting-help/06-sim-support-plan-chooser.md) · Simulation

## Module 13: Moving to AWS

- [Module 13: Moving to AWS](13-moving-to-aws/00-brief.md) · Module brief
- [The Cloud Adoption Framework](13-moving-to-aws/01-the-cloud-adoption-framework.md) · Lesson
- [Seven migration strategies](13-moving-to-aws/02-seven-migration-strategies.md) · Lesson
- [Migration tools](13-moving-to-aws/03-migration-tools.md) · Lesson
- [The business case](13-moving-to-aws/04-the-business-case.md) · Lesson
- [Simulation S16: Sort the chain's ten applications into the 7 Rs](13-moving-to-aws/05-sim-portfolio-sorter.md) · Simulation
- [Simulation S17: Rightsize the chain's servers and settle their licenses](13-moving-to-aws/06-sim-rightsizing-and-licensing.md) · Simulation

## Module 14: Capstone: a Well-Architected review

- [Module 14: Capstone: a Well-Architected review](14-capstone/00-brief.md) · Module brief
- [The capstone review](14-capstone/01-the-capstone-review.md) · Lesson
- [Lab 18: Record the bakery's review in the AWS Well-Architected Tool](14-capstone/02-lab-18-well-architected-tool-review.md) · Lab
- [Lab 19: Close out the account you used for the course](14-capstone/03-lab-19-close-out.md) · Lab

## Reference

- [Glossary](99-reference/01-glossary.md) · Reference
- [Names: the exam's and today's](99-reference/02-names-exam-vs-current.md) · Reference
- [Commonly confused terms](99-reference/03-commonly-confused.md) · Reference
- [Service map](99-reference/04-service-map.md) · Reference
- [Cost traps](99-reference/05-cost-traps.md) · Reference
- [Blueprint map](99-reference/06-blueprint-map.md) · Reference

---

"Contents" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
