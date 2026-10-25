---
type: page
id: clf-90-01
title: "How to use the exam preparation"
tasks: []
objectives: []
reader: "Adult studying alone, possibly new to IT, planning the last weeks before the CLF-C02 exam; about 10 minutes to read"
prerequisites: [clf-00-03]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/certification/certified-cloud-practitioner/"
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
---

# How to use the exam preparation: practice as you go, then check your readiness twice

This section holds two kinds of practice. Three **mixed sets** come during the course, to make you tell topics apart; two **practice exams** come at the end, to show whether you're ready. Use each at its moment, score every one by domain, and treat the result as a guide to what to study, never as a forecast of your exam score.

**For:** an adult studying alone, possibly new to IT, who wants to know when to use each page of this section. **Time:** about 10 minutes to read.

## What's in this section

| Page | What it is | When to take it | Time | What its score is for |
|---|---|---|---|---|
| [Mixed set 1](02-mixed-set-1.md) | 30 questions from Modules 02 to 05, shuffled together | After Module 05 | About 45 minutes | Learning: which ideas you still mix up |
| [Mixed set 2](03-mixed-set-2.md) | 30 questions from Modules 02 to 09, weighted by domain | After Module 09 | About 45 minutes | Learning |
| [Mixed set 3](04-mixed-set-3.md) | 30 questions from Modules 02 to 13, weighted 24/30/34/12 like the exam | After Module 13 | About 45 minutes | Learning, and the signal to start the practice exams |
| [Practice exam 1](05-practice-exam-1.md) | A full form: 65 questions in the exam's format | At the end of the course, once | 90 minutes | Readiness, by domain |
| [Practice exam 2](06-practice-exam-2.md) | A second full form, with different questions | A few days after practice exam 1, once | 90 minutes | Readiness, by domain |

Every question on these five pages was written for this section, apart from the lessons' practice and the mastery checks. The questions follow the exam's style: one correct answer out of four, or "(Select TWO.)" with two correct answers out of five. They use the exam's names for services, with today's names in the answer keys ([The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md) describes the real exam's format).

## When to use each part

```mermaid
flowchart LR
  accTitle: Where the mixed sets and practice exams fit in the course
  accDescr: Modules 02 to 05 lead to Mixed set 1, Modules 06 to 09 to Mixed set 2, and Modules 10 to 13 to Mixed set 3. After Mixed set 3 come Practice exam 1 and then Practice exam 2, each taken once, unseen, in 90 minutes. A weak domain on any of them sends you back to the linked lessons and the mastery checks.
  M1["Modules 02–05"] --> S1["Mixed set 1"]
  S1 --> M2["Modules 06–09"] --> S2["Mixed set 2"]
  S2 --> M3["Modules 10–13"] --> S3["Mixed set 3"]
  S3 --> E1["Practice exam 1<br/>once, 90 min"] --> E2["Practice exam 2<br/>once, 90 min"]
  S1 -.->|"weak domain"| R["Reread linked sections,<br/>retake mastery checks"]
  S2 -.-> R
  S3 -.-> R
  E1 -.-> R
```

*Notice that the mixed sets sit inside the course, between modules, while the two practice exams come only after all the teaching modules.*

**Long description.** A flowchart from left to right. Modules 02 to 05 lead to Mixed set 1; then Modules 06 to 09 lead to Mixed set 2; then Modules 10 to 13 lead to Mixed set 3. Mixed set 3 leads to Practice exam 1, taken once in 90 minutes, which leads to Practice exam 2, taken once in 90 minutes. Dashed arrows from each mixed set and from Practice exam 1, labeled "weak domain", lead to a box: reread the linked sections and retake the mastery checks.

**The mixed sets are for learning.** Each module's mastery check tests one module, so you always know what a question is about. The exam doesn't tell you, and the hardest part of many questions is noticing which idea they test. A mixed set shuffles everything you've studied so far, so you practice that choice, and it brings back older modules before you forget them. Take each one when you reach it in the course:

- **Mixed set 1 after Module 05.** It assumes Modules 02 to 05 only.
- **Mixed set 2 after Module 09.** It assumes Modules 02 to 09.
- **Mixed set 3 after Module 13.** It assumes Modules 02 to 13 and is the first set that can ask about any part of the exam. Module 14, the capstone, adds no new exam content, so you can do it before or after this set.

You can come back to a mixed set later. A second try still helps you learn, but your score on it then measures memory of the questions as much as understanding.

**The practice exams are for readiness.** Take them after Mixed set 3, when every domain is at least in the review band:

- **Each one once, unseen.** A practice exam shows readiness only the first time, while every question is new to you, as on the real exam. Don't read its questions or its answer key beforehand.
- **In 90 minutes, in one sitting,** closed book, as on exam day. If you'll take the exam in English as a non-native speaker with the extra 30 minutes AWS allows, give yourself 120.
- **A few days apart,** with study of your weak domains in between. Practice exam 2 then tells you whether that study worked.
- **Answer every question.** On the exam a blank counts as wrong and a wrong guess costs nothing, so practice guessing well rather than skipping.

## How to score by domain

The exam guide splits the exam into four domains with fixed shares of the scored questions. Every page in this section scores you domain by domain, because a total hides where the gaps are.

| Domain | Share of the exam |
|---|---|
| 1 Cloud Concepts | 24% |
| 2 Security and Compliance | 30% |
| 3 Cloud Technology and Services | 34% |
| 4 Billing, Pricing, and Support | 12% |

1. **Mark each answer** right or wrong with the answer key. A "(Select TWO.)" question counts as right only if both of your choices are right, as on the exam.
2. **Count the right answers in each domain.** Every page lists which questions belong to which domain.
3. **Find your band** in the page's table: below 60% means restudy the domain, 60% to 79% means review the sections linked from the questions you missed, and 80% or more means ready on that domain for now.
4. **Reread the linked section for every miss, and every lucky guess.** Each explanation in the answer keys links to the section that teaches the idea.

> **Example:** On Mixed set 3 you get 6 of 7 in Domain 1 (86%, ready), 6 of 9 in Domain 2 (67%, review), 9 of 10 in Domain 3 (90%, ready) and 2 of 4 in Domain 4 (50%, restudy). Your total, 23 of 30, looks fine, but the domain view says what to do: restudy Module 11's and 12's lessons for Domain 4, reread the sections linked from your three Domain 2 misses, and leave Domains 1 and 3 for later review.

With few questions in a domain, one answer moves the percentage a long way: on a mixed set, Domain 4 has only 2 to 4 questions. Read the bands as pointers, and trust the practice exams a little more, since they have more questions in every domain.

## Why a practice score isn't a prediction

No practice score here predicts your exam score, and none of these pages claims to. The reasons:

- **The real exam reports a scaled score** from 100 to 1,000, with 700 to pass, adjusted so different forms are equally hard. A percentage of right answers on our questions can't be turned into that scale.
- **Passing is compensatory:** you pass on your total, not domain by domain, and each real form mixes questions differently. A weak domain can be made up elsewhere on one form and not on another.
- **15 of the exam's 65 questions are unscored,** and you can't tell which. Our pages score every question.
- **Our questions aren't AWS's.** They're written from the public exam guide, never from real exam questions, so they can be easier or harder than the exam in ways nobody can measure.
- **Seen questions inflate scores.** That's why only a first attempt at a practice exam counts for readiness.

So read your two practice-exam results as a **range for each domain**, from your lower score to your higher one. If both are in the ready band in every domain, you're probably prepared; if a domain falls below 60% on either, it needs more study before you book or sit the exam. Either way, the decision is yours, and the [exam page](https://aws.amazon.com/certification/certified-cloud-practitioner/) and [The exam at a glance](../00-start-here/03-the-exam-at-a-glance.md) tell you what the real exam involves.

## What to do with a weak domain

1. **Find the pages.** The [blueprint map](../99-reference/06-blueprint-map.md) lists, for each of the exam's task statements, every lesson, lab and simulation in this guide that covers it. The answer keys name the task statement of each question, so you can go from a missed question to its task, and from the task to every page that teaches it.
2. **Reread the linked sections first,** then the lessons around them if the idea still isn't clear. The [commonly confused pairs](../99-reference/03-commonly-confused.md) page helps when you keep picking a neighbor of the right answer.
3. **Retake the module's mastery check.** Each module ends with a mastery check whose correction map points every question to a section, a lab or a simulation, and whose Check B is a parallel retest with new questions. Start from the module's brief, for example [Module 09](../09-protecting-and-governing/00-brief.md) for most of Domain 2.
4. **Do the labs and simulations** the correction map lists. Doing a task makes the ideas easier to tell apart than rereading does.
5. **Then go on,** to the next module, the next mixed set or practice exam 2. Don't retake a practice exam to check the study worked: you've seen its questions, so it would flatter you.

AWS changes names, plans and services often. Where an answer key gives today's name next to the exam's, learn both ([AWS changes fast](../00-start-here/04-aws-changes-fast.md) and [exam names and current names](../99-reference/02-names-exam-vs-current.md)).

---

"How to use the exam preparation" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
