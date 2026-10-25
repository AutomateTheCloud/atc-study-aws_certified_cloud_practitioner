---
type: lesson
id: clf-13-01
title: "The Cloud Adoption Framework"
tasks: ["1.3"]
objectives: ["13.01a"]
reader: "Adult studying alone, possibly new to IT, who has finished Modules 02 to 12; about 20 minutes; works on a phone"
prerequisites: [clf-02-05, clf-02-04]
terms_introduced: [AWS Cloud Adoption Framework, business outcome, ESG, transformation domain, perspective, capability, stakeholder, Envision phase, Align phase, Launch phase, Scale phase, pilot]
pillars: [cost-optimization, operational-excellence]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/business-perspective.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html"
  - "https://aws.amazon.com/cloud-adoption-framework/"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html"
---

# The Cloud Adoption Framework plans a move around the outcomes a business wants and six groups of people who must be ready for it

The **AWS Cloud Adoption Framework (AWS CAF)** is AWS's guidance for changing a whole organization to use the cloud well. The exam asks you to name its business outcomes and to say which of its six perspectives deals with a given concern.

**Exam guide:** [Domain 1, Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) (24% of the exam): task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 20 minutes. Reading works on a phone.

**Before you start:** this lesson compares the CAF with [the Well-Architected Framework](../02-why-the-cloud/05-the-well-architected-framework.md); the chain and its ten applications are in the [module brief](00-brief.md).

## Warm-up: what you remember

1. From lesson 02.05: does the Well-Architected Framework review a whole organization or one workload?

<details><summary>Feedback</summary>

1. **One workload**, against six pillars. The CAF works one level up, on the whole organization. Keep the two apart; the practice at the end tests it.

</details>

## What you'll learn

By the end of this lesson, you can name the CAF's four business outcomes and six perspectives, and map a concern raised during a migration to the perspective that deals with it (objective 13.01a).

Try this before you read on, and guess if you're unsure: is "process" one of the CAF's six perspectives?

## The big picture: capabilities enable change, change delivers outcomes

Read the picture from the bottom up. The organization builds **capabilities** (things it can do well, such as managing its cloud spending), grouped in six **perspectives**. They make change possible in four **transformation domains**, and the change delivers four **business outcomes**. The phases on the right are the order of work.

![The AWS CAF in three layers: six perspectives at the bottom enable four transformation domains, which deliver four business outcomes at the top; four phases run down the right.](../../images/13-01-big-picture.svg)

*Notice where "Process" sits: in the middle layer, among the things that change. It isn't one of the six perspectives at the bottom.*

**Long description.** Three layers, read from the bottom up. Bottom: six perspectives with their number of capabilities and focus: Business (8), strategy and outcomes; People (7), culture and change; Governance (7), control and oversight; Platform (7), infrastructure and applications; Security (9), compliance and assurance; Operations (9), health and availability. An arrow labeled "enable" leads to four transformation domains in a chain: Technology, Process (highlighted: a domain, not a perspective), Organization, Product. An arrow labeled "deliver" leads to four business outcomes: reduce business risk, improve ESG performance, grow revenue, increase operational efficiency. On the right, the phases Envision, Align, Launch and Scale loop back to Envision.

## The CAF aims at four business outcomes

The CAF starts from what the business wants, not from technology. AWS names four **business outcomes**, the same four the exam guide lists in task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3) ([AWS CAF page](https://aws.amazon.com/cloud-adoption-framework/), checked 2026-10-24):

| Outcome, and what AWS says it covers | The chain's version |
|---|---|
| **Reduce business risk:** better reliability, performance and security | The website slows every December; the recipe archive runs on an unpatched operating system |
| **Improve ESG performance:** sustainability and corporate transparency | A supermarket customer asks for the chain's energy and carbon figures |
| **Grow revenue:** new products, customers and market segments | Five times as many wholesale café customers |
| **Increase operational efficiency:** lower operating costs, more productivity | Stop paying for a data center; free the two staff who run the mail servers |

**ESG** stands for environmental, social and governance: how an organization treats the planet, people and its own management.

The change itself happens in four **transformation domains**, each enabling the next: **technology** (migrate and modernize infrastructure, applications and data), **process** (digitize and automate how the business runs), **organization** (change how teams work) and **product** (new offers and ways to earn money) ([Accelerating business outcomes](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/accelerating-business-outcomes.html)).

### "Process is one of the CAF perspectives" is wrong

Some lists of perspectives include "process", but process is a **transformation domain**, one of the things that changes. The six perspectives are **Business, People, Governance, Platform, Security and Operations** ([Foundational capabilities](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html), checked 2026-10-24). The slip is natural because "people, process and technology" is a familiar trio in IT, and the CAF uses all three words in different parts. That answers the prequestion.

## Six perspectives group the capabilities, each owned by different people

Each perspective groups related capabilities and is owned by its common **stakeholders**, the people with a say in that part of the change, such as the CFO or the CISO. You don't need all 47 capabilities for the exam: know what each perspective is for and recognize its typical capabilities.

| Perspective | Focus | Typical capabilities | A chain concern it owns |
|---|---|---|---|
| **Business** | Strategy and outcomes | Strategy management, portfolio management, innovation management | "Which applications go first, and is it worth it?" |
| **People** | Culture and change | Cloud fluency, workforce transformation, change acceleration | "Nobody here has used AWS. Who trains them?" |
| **Governance** | Control and oversight | Program and project management, benefits management, risk management, cloud financial management | "Split the bill by shop and keep it in budget" |
| **Platform** | Infrastructure and applications | Platform architecture, provisioning and orchestration, continuous integration and delivery | "One standard way to set up accounts and networks" |
| **Security** | Compliance and assurance | Identity and access management, threat detection, data protection, incident response | "Protect card data and pass the payment audit" |
| **Operations** | Health and availability | Observability, incident and problem management, patch management | "Who is alerted at 3 a.m. when ordering slows?" |

### Map a concern by asking what is at stake, not who is asking

Job titles repeat across perspectives (the CFO is in Business and Governance, the CTO in four), and so do words like "governance" and "incident". So ignore who raised the concern and ask what it's about:

- skills, roles or culture: **People**;
- what to change, in what order, and whether it's worth it: **Business**;
- running the program, measuring benefits, controlling spend and licenses, managing risk: **Governance**;
- protecting data, identities and systems, or proving compliance: **Security**;
- keeping running services healthy (monitoring, incidents, patching): **Operations**;
- building and standardizing the environment: **Platform**.

A service that fails at night with no attack involved is an Operations incident, even though Security has a capability called "incident response".

> **Your turn:** Map each concern to a perspective. (a) "Our server engineers will need new skills, and some of their jobs will change." (b) "Every new server must be patched within a week of a fix being released." (c) "The migration projects for our ten applications keep blocking each other; somebody must coordinate them."

<details><summary>Model answer</summary>

(a) **People:** cloud fluency and workforce transformation. The people are engineers, but the concern is skills and roles, not technology. (b) **Operations:** patch management keeps services healthy. (c) **Governance:** program and project management.

</details>

### Business or Governance: deciding what to do, or overseeing how it goes

These two are the pair people mix up most: both talk about money and portfolios, and the CFO sits in both.

![The Business and Governance perspectives compared side by side on five rows, with the portfolio and money row highlighted.](../../images/13-01-business-vs-governance.svg)

*Notice the highlighted row: both have a "portfolio" capability, but Business chooses what to invest in, and Governance keeps the inventory and tracks spend and results.*

**Long description.** Two columns compared on five rows. Focus: Business, strategy and outcomes; Governance, control and oversight. Common stakeholders: the CFO, CIO and CTO appear in both; Business adds the CEO and COO, Governance the chief transformation, data and risk officers. The question it answers: Business, what should we change, in what order, and why is it worth it; Governance, is the change delivered as planned, are the benefits real, and is spending under control. Portfolio and money, highlighted: Business uses portfolio management and the 7 Rs to build the business case; Governance uses cloud financial management, benefits management and application portfolio management to track spend and licenses, measure results and keep the application inventory. The last row lists every capability of each perspective: eight for Business, seven for Governance.

"Should we, and in what order?" is Business. "Is it going as planned, and within budget?" is Governance. So when the chain's finance director asks how the cloud bill will be split by shop and kept within budget, that's Governance's **cloud financial management**, which AWS says includes managing the licenses you own and those included with cloud resources ([Governance perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html)).

## Four phases, repeated: Envision, Align, Launch, Scale

The CAF suggests working in four phases and repeating them, so each round shows value quickly ([Your cloud transformation journey](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html), checked 2026-10-24):

- **Envision phase:** show how the cloud will speed up business outcomes, and choose the opportunities to pursue.
- **Align phase:** find the gaps in capabilities across the six perspectives and surface stakeholders' concerns. The chain finds it has no AWS skills (People) and no cost split by shop (Governance).
- **Launch phase:** deliver **pilots** in production, small first projects run for real, and show value step by step. The chain moves its loyalty database first and measures it.
- **Scale phase:** expand the pilots to the size the business needs, and make sure the benefits last.

## The CAF and the 7 Rs work at different levels

Both are in task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3), and they're easy to blur. The CAF is about the **organization**: is it ready, and what outcomes does it want? The 7 Rs, the next lesson's subject, are about **one application at a time**: retire it, keep it, move it as it is, or change it on the way. They meet at one point: the Business perspective's **portfolio management** capability uses discovery tools and the 7 Rs to sort the existing applications and build a business case ([Business perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/business-perspective.html)). The Well-Architected Framework is a third level: it reviews how well one workload is built, against six pillars.

> **Dated (checked 2026-10-24):** AWS's current CAF whitepaper is the edition of 2021-11-22, and the exam guide's outcome wording matches it.

## Summary

- **Four business outcomes:** reduce business risk, improve ESG performance, grow revenue, increase operational efficiency. Four transformation domains change: technology, process, organization, product.
- **Six perspectives:** Business, People, Governance, Platform, Security, Operations. Process is a domain, not a perspective.
- **Map a concern by what is at stake, not by who asks.** Business decides what is worth doing; Governance oversees benefits, spending, licenses, risk and the program.
- **Four phases, repeated:** Envision, Align, Launch, Scale. Gaps across the perspectives are found in Align; pilots run in Launch.
- **The CAF works on the organization, the 7 Rs on one application,** and the Well-Architected Framework on one workload's design.

## Practice

1. **The chain's chief risk officer wants someone to coordinate the migration projects and report each quarter whether the promised savings are arriving. Which CAF perspective?**

   A. Business\
   B. Governance\
   C. Operations\
   D. People

   <details><summary>Feedback</summary>

   **B is right.** Program and project management and benefits management are Governance capabilities.

   - **A is wrong.** Business chose the projects; overseeing their delivery and benefits is Governance.
   - **C is wrong.** Operations keeps running services healthy, not the migration program.
   - **D is wrong.** People covers skills, culture and organizational change.

   </details>

2. **Which of these is a business outcome the AWS CAF names, rather than a transformation domain?**

   A. Process\
   B. Improve environmental, social and governance (ESG) performance\
   C. Organization\
   D. Technology

   <details><summary>Feedback</summary>

   **B is right.** The four outcomes are reduce business risk, improve ESG performance, grow revenue and increase operational efficiency.

   - **A, C and D are wrong.** They're three of the four transformation domains (the fourth is product): the areas that change, not the results.

   </details>

3. **The chain wants to check whether its new wholesale portal on AWS follows good practice for reliability and cost. Which fits?**

   A. The AWS CAF's six perspectives\
   B. A Well-Architected review of the portal\
   C. The 7 Rs\
   D. The CAF's Envision phase

   <details><summary>Feedback</summary>

   **B is right.** The Well-Architected Framework judges one workload against six pillars.

   - **A is wrong.** The perspectives assess the organization's readiness, not one workload's design.
   - **C is wrong.** The 7 Rs choose how an application moves, not how well it's built.
   - **D is wrong.** Envision chooses the outcomes for a round of change.

   </details>

**Next:** [Seven migration strategies](02-seven-migration-strategies.md), where the chain decides what happens to each application.

## Where to check the current details

- [An Overview of the AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html), AWS whitepaper (checked 2026-10-24)
- [AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/): outcomes, perspectives, phases and domains on one page (checked 2026-10-24)
- [CLF-C02 exam guide, Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html), task [1.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.3) (checked 2026-10-24)

---

"The Cloud Adoption Framework" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
