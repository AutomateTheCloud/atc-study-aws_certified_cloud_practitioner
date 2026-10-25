# Review report: CLF-C02 practice bundle, version 0.4.0

**Practice Questions and Flashcards for the AWS Certified Cloud Practitioner Exam (CLF-C02)**,
built 2026-10-24 from the guide's Modules 01 to 14 and its glossary.

- Version 0.4.0 (2026-10-25) follows the guide's cut to the exam's depth: 200 items that tested
  material moved to the modules' "Beyond the exam" pages (or beyond the exam's depth) are retired,
  leaving 780 questions; every reference points at a current heading; the glossary went from 1,000
  to 456 terms, so 929 flashcards remain. No remaining question's stem or choices changed, so the
  blind solve and the similarity check below still hold for them. Item and choice `id`s are kept.
- Version 0.3.4 (2026-10-25) spells "Long-Form" one way on the "voice engine" flashcard.
- Version 0.3.3 (2026-10-25) writes every date one way (full dates as YYYY-MM-DD, dates without a
  year as "June 3") and spells "canceled" and "traveling" the US way. Three questions' wordings
  changed only in that; all nine wordings pass the dump-similarity check (9 PASS).
- Version 0.3.2 (2026-10-25) changes only the wording of 15 flashcard backs, from the glossary's style
  pass; no question, choice or `id` changed, so the checks below still apply.
- Bundle: `clf-c02-practice.waymark` (OpenWaymark 0.2), built from `clf-c02-practice/study.yaml`.
- **922 questions** (737 with one answer, 185 "Select TWO") and **1,693 flashcards**.
- Each version kept every item and choice `id`: 0.1.0 had Modules 02–07, 0.2.0 added 08–13, and 0.3.0 adds
  the capstone (Module 14), the on-ramp's glossary cards (Module 01) and AWS RAM.

## Source and license

- **Source:** this repository's own guide: `guide/02-*` to `guide/13-*` and `reference/glossary.yaml`.
  The material belongs to Automate the Cloud Inc. and is licensed CC BY-NC 4.0 with the Additional
  Permission for Internal Training.
- **Bundle license:** the same terms, stated in `bundle.yaml` and covered by `LICENSE.md`, which
  names `practice/`.
- **Clean room:** the writers worked only from the guide. They never opened the dump-analysis
  repository, `sources/practice-bank/` or the research repository, and they didn't browse the web.
- **Not used:** no AWS documentation text and no third-party questions.

## Answer variants

Every choice of every question has three wordings: the text plus two variants. The app shows one
wording per choice, picked at random. That needs format **0.2**.

Where a question tests an official name, every wording is the exact name in a different frame.
Service names use their official short and long forms; where the exam guide uses an older name,
choices use the exam's name or both, and the explanation teaches today's.

## Coverage

| Module | Questions | Select TWO | Recall | Understanding | Application | Concept cards | Glossary cards |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 Start here | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| 01 On-ramp (optional) | 0 | 0 | 0 | 0 | 0 | 0 | 111 |
| 02 Why organizations use the cloud | 71 | 14 | 13 | 33 | 25 | 18 | 92 |
| 03 AWS around the world | 63 | 12 | 10 | 29 | 24 | 15 | 70 |
| 04 Who secures what | 85 | 19 | 14 | 37 | 34 | 24 | 102 |
| 05 Storing data | 89 | 17 | 13 | 43 | 33 | 22 | 191 |
| 06 Running applications | 77 | 15 | 13 | 35 | 29 | 18 | 117 |
| 07 Connecting it | 75 | 15 | 12 | 25 | 38 | 18 | 108 |
| 08 Building and operating | 71 | 14 | 15 | 25 | 31 | 18 | 111 |
| 09 Protecting, governing and proving compliance | 90 | 18 | 14 | 37 | 39 | 24 | 157 |
| 10 Data, AI and the rest of the catalog | 64 | 13 | 7 | 26 | 31 | 18 | 114 |
| 11 Paying for AWS | 78 | 15 | 11 | 36 | 31 | 20 | 93 |
| 12 Getting help | 61 | 14 | 10 | 22 | 29 | 16 | 93 |
| 13 Moving to AWS | 65 | 13 | 11 | 22 | 32 | 18 | 81 |
| 14 Capstone | 33 | 6 | 3 | 14 | 16 | 10 | 12 |
| **Total** | **922** | **185** | **146** | **384** | **392** | **239** | **1,454** |

**Questions per exam task (all 19 tasks are covered):**

| Task | Questions | Task | Questions | Task | Questions |
| --- | --- | --- | --- | --- | --- |
| 1.1 | 33 | 2.3 | 63 | 3.5 | 59 |
| 1.2 | 15 | 2.4 | 26 | 3.6 | 47 |
| 1.3 | 45 | 3.1 | 39 | 3.7 | 42 |
| 1.4 | 43 | 3.2 | 70 | 3.8 | 44 |
| 2.1 | 54 | 3.3 | 54 | 4.1 | 59 |
| 2.2 | 76 | 3.4 | 32 | 4.2 | 38 |
| | | | | 4.3 | 50 |

**By domain:** Domain 1 has 136 questions (15%), Domain 2 has 219 (25%), Domain 3 has 387 (44%)
and Domain 4 has 147 (17%). The exam weights them 24/30/34/12, so a practice session drawn from the
whole pool over-weights technology and under-weights cloud concepts. A future version should add
Domain 1 and 2 items, or an app should draw by domain.

**Flashcards by kind:**

| Kind | Cards |
| --- | --- |
| Glossary term to definition | 916 |
| Confused pairs ("how is X different from Y") | 348 |
| Abbreviations | 67 |
| Exam-guide names | 10 |
| Concept cards written by hand (rules, causes, "why", how to choose) | 229 |

**Level mix:** 16% recall, 42% understanding, 42% application, against a plan of 20/50/30. Most
objectives from Module 06 on are "choose", "predict" or "route", and the glossary cards carry the
recall.

**Left out on purpose:** prices, discount percentages, free-tier amounts, credit expiry, counts of
Regions, services or Trusted Advisor checks; points the pages leave open (for example whether
Business Support+ qualifies for the Shield Response Team); and the labs' console steps.

## Checks

- **OpenWaymark lint:** 0 errors, 0 warnings, on the folder and on the packed file.
- **`check_items.py`:** 0 warnings. Correct-answer positions: A 183, B 186, C 188, D 180. The correct
  choice is the longest in 204 of 737 single-answer questions (28%). The 1,058 notes are judgment
  calls, almost all about a service name's long form being longer than its short form.
- **Blind solve:** a fresh solver per module answered every question from the guide pages, without
  the key. All 922 matched (02: 71, 03: 63, 04: 85, 05: 89, 06: 77, 07: 75, 08: 71, 09: 90,
  10: 64, 11: 78, 12: 61, 13: 65, 14: 33). Every flag they raised (giveaways, drifting variants,
  partly supported cards, claims true only in the guide) was fixed, and every changed item was solved
  blind again by new helpers until they agreed with the key and raised no flags.
- **Exam vs today:** where the exam guide still expects a closed or renamed service (for example
  Application Discovery Service, Application Migration Service), questions are framed so only one
  answer applies, and the explanation gives today's status.
- **Similarity to known dump questions** (`tools/check_similarity.py`, run blind): all 889 questions
  in all three wordings, 2,766 candidates: 2,766 PASS, 0 REVIEW, 0 REJECT (version 0.3.1 rewrote the last six REVIEW items, below).
- **Guide pages:** the checks found 40-odd places where the guide had simplified a fact too far.
  Each was checked against current AWS documentation and corrected on the page, with the source.

## Needs a human

1. **The six REVIEW items are resolved without viewing dump text.** In 0.3.0, six Module 05 storage-class
   questions scored REVIEW because a known question offered a similar set of S3 classes. Rather than open the
   dump text (the author stays in the clean room), 0.3.1 rewrote them as statement, trade-off, lifecycle-rule
   and action questions (`revision: 2`); all now PASS and a fresh blind solve matched all six.
2. **Items resting on dated facts:** the explanations date them (2026-10-23 or 2026-10-24). Recheck
   them with every release: Support plan names and the legacy plans' end (2027-01-01), WorkSpaces
   Secure Browser closing to new customers (2026-10-29), Amazon Q Developer's subscriptions ending
   (2027-04-30), Snowball's end of support (2026-12-31), Security Hub's two products, Kendra, Q
   Business, Forecast, Fraud Detector, Inspector Classic, Audit Manager and CloudTrail Lake.
3. **Domain balance** (above).
4. **What the format couldn't express:** a bundle has one question pool, so modules, pages and exam
   tasks are tags, not sections; ordering tasks aren't possible; and the item check's length
   heuristic can't tell a service's long and short official names from a giveaway.

A validator checks structure only. These items were checked against the guide by blind solvers,
but someone who knows AWS should review the answers before learners rely on them.
