---
type: lesson
id: clf-02-05
title: "The Well-Architected Framework"
tasks: ["1.2"]
objectives: ["02.05a"]
reader: "Adult studying alone, possibly new to IT; about 25 minutes; works on a phone or a computer"
prerequisites: ["clf-02-04"]
terms_introduced: [AWS Well-Architected Framework, pillar, design principle, best practice, workload, trade-off, AWS Well-Architected Tool, milestone, high-risk issue]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html"
  - "https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf"
  - "https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html"
---

# The Well-Architected Framework turns "is this built well?" into six questions

AWS's Well-Architected Framework splits "is our system built well?" into six pillars, each with design principles and best practices. The exam asks you to tell the pillars apart, to recognize a trade-off between them, and to keep the Framework (guidance you read) apart from the Well-Architected Tool (a service you use).

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 25 minutes.

**Before you start:** read [What a data center really costs](04-what-a-data-center-really-costs.md) first. You met the Framework briefly on [page 00 of the guardrails primer](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md).

## Warm-up

1. *(From 02.04)* The bakery leaves its holiday-sized cloud setup running all year. Is that mainly a problem of fixed cost or of idle capacity?
2. *(From 02.03)* The bakery's site gains capacity automatically when orders climb, and gives it back when they fall. Which benefit is that?

<details><summary>Feedback</summary>

1. **Idle capacity.** The cloud bill is variable, but the bakery pays for capacity it doesn't use; scaling down after the peak fixes it.
2. **Elasticity**: capacity follows demand up and down.

</details>

## What you'll learn

By the end of this lesson, you can name the six pillars and match a concern to its pillar, explain a trade-off between pillars, and tell the Framework apart from the AWS Well-Architected Tool (objective 02.05a).

Try this before you read on: how many pillars does the Framework have?

## Six pillars, six questions

The **AWS Well-Architected Framework** is AWS's published guidance for designing and running systems well in the cloud. A **pillar** is one of its six areas of concern; a **design principle** is a short, named idea that guides decisions; a **best practice** is a specific recommended action with an ID. Each pillar is easiest to remember as the question it asks about your **workload**, the set of parts that together deliver something of value, such as the bakery's ordering site. The questions are our summaries of AWS's definitions ([The pillars of the framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)).

![Six cards in three rows of two, one per pillar, each with its ID prefix, name and question. Row 1, generally not traded away: operational excellence (OPS) and security (SEC). Row 2, sound alike: reliability (REL) and performance efficiency (PERF). Row 3, usually point the same way: cost optimization (COST) and sustainability (SUS).](../../images/02-05-six-pillars.svg)

*Notice how the rows group the pillars: the two generally not traded away, the two that sound alike, and the two that usually point the same way.*

**Long description.** Six cards in three rows of two, each with a pillar's ID prefix, name and question, the same questions as the table below. Row 1, generally not traded away: operational excellence (OPS) and security (SEC). Row 2, sound alike, both care about capacity: reliability (REL) and performance efficiency (PERF). Row 3, usually point the same way, because waste costs money and energy at once: cost optimization (COST) and sustainability (SUS).

| Pillar | The question it asks | A bakery example | One of its design principles |
|---|---|---|---|
| **Operational excellence** | Can we run this well day to day, see what it's doing, and keep improving how we work? | Updates are made by hand on the live site at night, and nobody records what changed | "[Make frequent, small, reversible changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html)" |
| **Security** | Are the data, systems and accounts protected? | The owner's password is on a sticky note by the till | "[Implement a strong identity foundation](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html)" |
| **Reliability** | Does it do its job correctly whenever it's needed, and recover when something fails? | Nobody has ever tried restoring the site from a backup | "[Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" |
| **Performance efficiency** | Are we using the right kind and amount of resources, as demand and technology change? | Customers in another country wait seconds for each page | "[Go global in minutes](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html)" |
| **Cost optimization** | Does it deliver its value at the lowest cost? | Six rented servers run all year for a December peak | "[Adopt a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)" |
| **Sustainability** | Are we using as few resources, and as little energy, as we can? | Three owned servers run all January, when one would do | "[Maximize utilization](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-design-principles.html)" |

### "The Framework has five pillars" is wrong

It has six. Older material lists five because it predates the sustainability pillar, and one older AWS security whitepaper, now marked by AWS as for historical reference only, still says five. The CLF-C02 exam guide, under task [1.2](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.2), lists all six. The old figure is tempting because so much study material online was written before the change.

### Pillars that sound alike, side by side

**Reliability and performance efficiency** both care about capacity. Reliability asks whether the system keeps working and recovers from failure (for example, "[Automatically recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)"); performance efficiency asks whether it uses the right type and amount of resources for the job (for example, "[Use serverless architectures](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html)"). **Cost optimization and sustainability** usually point the same way, because unused resources waste money and energy at once; the first measures money, the second resources and energy.

So decide by what's at risk. It stops working or can't recover: reliability. It works, but on the wrong kind or amount of resource: performance efficiency. Money is wasted: cost optimization. Resources and energy are wasted: sustainability.

> **Your turn:** match each bakery concern to a pillar, and say in one line why.
>
> 1. The site went down for a day when its only server failed.\
> 2. Anyone who knows the owner's email address could try to guess the one password that controls everything.\
> 3. Nobody can tell how many orders failed last week, because nothing records errors.

<details><summary>Model answer</summary>

1. **Reliability.** The site couldn't keep working, or recover quickly, when one part failed.
2. **Security.** Access to the account is weakly protected; MFA and separate identities fix it.
3. **Operational excellence.** The team can't see what the workload is doing, so it can't run or improve it.

</details>

## Real design principles, and slogans that only sound like them

Besides each pillar's principles, the Framework lists six **general design principles** ([General design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)):

- "[Stop guessing your capacity needs](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": scale with demand instead of buying for a guess (the demand curve from 02.02).
- "[Test systems at production scale](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": build a full-size copy for testing, then remove it.
- "[Automate with architectural experimentation in mind](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": automated builds make a change cheap to try and undo.
- "[Consider evolutionary architectures](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": expect the design to change over time.
- "[Drive architectures using data](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": decide from measurements, not opinions.
- "[Improve through game days](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)": rehearse failures and busy days in practice runs.

### "Design for failure" and "geographic diversity" are not Framework principles

Older study notes and practice questions present "design for failure", "think parallel", "decouple your components", "implement elasticity" and "geographic diversity" as Well-Architected design principles. None of them is a general or pillar design principle in the current Framework. The Framework names the sound ideas behind them differently: planning for failure appears as "[Automatically recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" and "[Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)", and elasticity as "[Stop guessing your capacity needs](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)". The slogans are tempting because they're short and sound official; on the exam, prefer the Framework's own wording.

## The pillars can be traded against each other, but not all of them

A **trade-off** means accepting less of one good thing to get more of another. You can't maximize all six pillars at once, and the Framework expects you to weigh them against what the business needs: for example, lower reliability in a development environment, or more spent on reliability for a system the business can't run without. It also says security and operational excellence are generally not traded against the other pillars ([AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf), 2024-11-06 edition).

> **Example:** the bakery has a live ordering site and a test copy where the owner's nephew tries changes. If the live site fails at a holiday peak, the bakery loses orders; if the test copy fails, the nephew waits until tomorrow. So the test copy bends toward cost (one small server, no standby, off at night), and the live site pays more for reliability in the peak months. Security and operational excellence hold on both: the test copy still needs a strong password with MFA, because a break-in there can reach the rest of the account.

![Two panels. Test copy: if it fails, the nephew waits until tomorrow, and a slider between reliability and cost optimization sits near cost. Live ordering site: if it fails, the bakery loses orders at a holiday peak, and the slider sits near reliability. A band across both reads "Held on both copies: Security, Operational excellence".](../../images/02-05-trade-offs.svg)

*Notice that only one balance moves between the two copies, reliability against cost. Security and operational excellence sit outside the sliders.*

**Long description.** Two panels, each with a slider between reliability and cost optimization. Test copy: if it fails, the nephew waits until tomorrow; the slider sits near cost optimization (one small server, no standby copy, switched off at night). Live ordering site: if it fails, the bakery loses orders at a holiday peak; the slider leans toward reliability. A band below both reads "Held on both copies: Security, Operational excellence", noting that the test copy still needs a strong password with MFA. A last line says to write the decision down.

## The Framework is guidance; the Well-Architected Tool applies it

| | AWS Well-Architected Framework | AWS Well-Architected Tool |
|---|---|---|
| What it is | Guidance: a set of AWS whitepapers | A service in the AWS console |
| What you do with it | Read it to learn how to design and run systems well | Define a workload, answer the Framework's questions about it, and get its **high-risk issues** (HRIs, serious gaps) and medium-risk issues, an improvement plan, and saved **milestones** (snapshots to compare later) |
| Cost | Free to read | No charge to use (as of 2026-10-23) |

AWS describes a review as a conversation about architecture decisions, not an audit: nobody passes or fails ([What is AWS Well-Architected?](https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html)). Don't confuse either with **AWS Trusted Advisor**, which runs automatic checks on your account and groups them into categories, not pillars. Some practice material names Trusted Advisor as the service that reviews a workload against the Framework; that service is the Well-Architected Tool. Module 12 covers Trusted Advisor.

## Summary

- **Six pillars, six questions:** operational excellence (run and improve), security (protect), reliability (work and recover), performance efficiency (right resources), cost optimization (lowest cost for the value), sustainability (fewest resources and least energy). Not five.
- **Pillars that sound alike:** decide by what's at risk.
- **The six general design principles** include "stop guessing your capacity needs" and "improve through game days"; "design for failure", "think parallel" and "geographic diversity" aren't Framework principles.
- **Trade-offs are expected**, such as less reliability in a test environment, but security and operational excellence are generally not traded away.
- **The Framework is guidance; the Well-Architected Tool** reviews one workload against it. Trusted Advisor is a different service.

## Practice

1. **The bakery's site loads slowly for customers in another country, though it never fails. Which pillar does this concern most?**

   A. Reliability\
   B. Performance efficiency\
   C. Security\
   D. Sustainability

   <details><summary>Feedback</summary>

   **B is right.** The site isn't using resources placed and sized to serve those users well; "go global in minutes" is one of this pillar's principles.

   - **A is wrong.** Nothing fails or needs recovery.
   - **C is wrong.** Nothing is exposed.
   - **D is wrong.** The issue is speed for users, not wasted resources or energy.

   </details>

2. **Which of these is a general design principle of the AWS Well-Architected Framework?**

   A. Design for failure\
   B. Think parallel\
   C. Improve through game days\
   D. Geographic diversity

   <details><summary>Feedback</summary>

   **C is right.** It's one of the six general design principles.

   - **A is wrong.** It's a slogan from older material; "automatically recover from failure" covers the idea.
   - **B is wrong.** It isn't in the current Framework.
   - **D is wrong.** It isn't a Framework term.

   </details>

3. **A team decides its development environment doesn't need a standby copy, to save money. Which statement best describes this?**

   A. A breach of the Framework, which requires maximum reliability everywhere\
   B. An acceptable trade-off between reliability and cost, of the kind the Framework describes\
   C. A trade-off of security for cost\
   D. A performance efficiency decision

   <details><summary>Feedback</summary>

   **B is right.** Lower reliability in development, for lower cost, is a trade the Framework itself describes.

   - **A is wrong.** The Framework expects trade-offs based on business needs.
   - **C is wrong.** A standby copy is about recovering from failure, which is reliability.
   - **D is wrong.** The decision is about recovery and cost, not the type or amount of resources.

   </details>

**Next:** measure agility for yourself in [Lab 01: create, find and delete your first storage bucket](06-lab-01-first-resource.md).

## Where to check the current details

- [The pillars of the framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), AWS Well-Architected Framework (checked 2026-10-23)
- [General design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html), AWS Well-Architected Framework (checked 2026-10-24)
- [What is AWS Well-Architected?](https://docs.aws.amazon.com/wellarchitected/latest/userguide/well-architected.html), AWS Well-Architected Tool User Guide (checked 2026-10-23)

---

"The Well-Architected Framework" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
