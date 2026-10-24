# Review report: CLF-C02 practice bundle, version 0.1.0

**Practice Questions and Flashcards for the AWS Certified Cloud Practitioner Exam (CLF-C02)**,
built 2026-10-24 from the guide's Modules 02 to 07 and its glossary.

- Bundle: `clf-c02-practice.waymark` (OpenWaymark 0.2), built from `clf-c02-practice/study.yaml`.
- **460 questions** (368 with one answer, 92 "Select TWO") and **822 flashcards**.

## Source and license

- **Source:** this repository's own guide: `guide/02-*` to `guide/07-*` and `reference/glossary.yaml`.
  The material belongs to Automate the Cloud Inc. and is licensed CC BY-NC 4.0 with the Additional
  Permission for Internal Training.
- **Bundle license:** the same terms, stated in `bundle.yaml` and covered by `LICENSE.md`, which
  now names `practice/`.
- **Clean room:** the writers worked only from the guide. They never opened the dump-analysis
  repository, `sources/practice-bank/` or the research repository, and they didn't browse the web.
- **Not used:** no AWS documentation text and no third-party questions.

## Answer variants

Every choice of every question has three wordings: the text plus two variants. The app shows one
wording per choice, picked at random. That needs format **0.2**, so the app must read OpenWaymark
0.2.

Where a question tests an official name (the six advantages of cloud computing, the
Well-Architected design principles), every wording is the exact name in a different frame, such
as `The line "…"` or `The phrase "…"`. Service names use their official short and long forms.

## Coverage

| Module | Questions | Select TWO | Recall | Understanding | Application | Concept cards | Glossary cards |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 Start here | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| 02 Why organizations use the cloud | 71 | 14 | 13 | 33 | 25 | 18 | 93 |
| 03 AWS around the world | 63 | 12 | 10 | 29 | 24 | 15 | 71 |
| 04 Who secures what | 85 | 19 | 14 | 37 | 34 | 24 | 104 |
| 05 Storing data | 89 | 17 | 13 | 43 | 33 | 22 | 193 |
| 06 Running applications | 77 | 15 | 13 | 35 | 29 | 18 | 123 |
| 07 Connecting it | 75 | 15 | 12 | 25 | 38 | 18 | 109 |
| **Total** | **460** | **92** | **75** | **202** | **183** | **115** | **707** |

**Questions per exam task:**

| Task | Questions | Task | Questions |
| --- | --- | --- | --- |
| 1.1 | 33 | 3.2 | 70 |
| 1.2 | 15 | 3.3 | 54 |
| 1.4 | 22 | 3.4 | 30 |
| 2.1 | 47 | 3.5 | 59 |
| 2.3 | 55 | 3.6 | 47 |
| 3.1 | 8 | 4.1 | 20 |

**Not covered yet:** tasks 1.3, 2.2, 2.4, 3.7, 3.8, 4.2 and 4.3. Modules 08 to 13 teach them, and
items are added as those modules are written.

**Flashcards by kind:**

| Kind | Cards |
| --- | --- |
| Glossary term to definition | 473 |
| Confused pairs ("how is X different from Y") | 194 |
| Abbreviations | 36 |
| Exam-guide names | 4 |
| Concept cards written by hand (rules, causes, "why", how to choose) | 115 |

Every objective in each module's blueprint (`work/blueprint-NN.md`) has items. A few blueprint
level counts shifted by one or two in the fixes; this table has the final numbers.

The level mix leans toward application (40%, against a plan of 30%), because most of these
modules' objectives are "choose", "predict" or "apply". Module 07 is 51% application.

**Left out on purpose:**
- prices, free-tier amounts, and counts of Regions or services;
- the console steps in the labs;
- best-practice IDs.

## Checks

- **OpenWaymark lint:** 0 errors, 0 warnings, on the folder and on the packed file.
- **`check_items.py`:**
  - 0 warnings.
  - Correct-answer positions: A 91, B 92, C 95, D 90.
  - The correct choice is the longest in 99 of 368 single-answer questions (27%; one in four
    would be chance).
  - The 361 notes are judgment calls. Almost all say a service name's long form, such as "Amazon
    Elastic Container Registry", is longer than its short form, "Amazon ECR".
- **Blind solve:** a fresh solver per module answered every question from the guide pages,
  without the key. All 460 matched: 71, 63, 85, 89, 77 and 75. The solvers flagged 30 wording
  problems (giveaways, variants that drifted) and 9 cards that were only partly supported. All were
  fixed, and every changed item was solved blind again by new helpers until they agreed with the
  key and raised no flags.
- **Similarity to known dump questions** (`tools/check_similarity.py`, run blind):
  - The final check covered all 460 questions in all three wordings, 1,380 candidates: 1,374 PASS,
    6 REVIEW, 0 REJECT.
  - The first run had flagged 29 questions (1 REJECT, 28 REVIEW). Each was rewritten with a new
    scenario and, where needed, a new choice set.
- **Glossary:**
  - Definitions and "don't confuse" lines are now at most 40 words, counted as the item check
    counts them. 82 fields in 75 entries changed: most were tightened without changing their
    meaning, and the rest carry the corrections in item 3 below.
  - `build_glossary.py` enforces the limit.

## Needs a human

1. **Six questions need an authorized reviewer** (`--show-text` on just these):
   `q05-classes-that-need-a-restore`, `q05-dr-backups-restore-in-hours`,
   `q05-regenerable-preview-clips`, `q05-scans-read-a-few-times-a-year`,
   `q05-ten-year-records-lowest-cost`, `q05-unpredictable-video-library`.
   - Each is REVIEW on its first wording only, for one reason: a known question offers a similar
     set of S3 storage classes and keys the same one. None has stem or wording overlap.
   - Questions about choosing a storage class tend to share their choices, so these may be fine.
   - A fixer had made them pass by writing the class names without "S3". That defeats the check
     rather than satisfying it, so the official names are back and the REVIEW verdicts stand.
2. **Items to look at first:**
   - *Rest on a fact dated 2026-10-23, said in their explanations:* `q03-european-sovereign-cloud`,
     `q04-root-mfa-requirement` and the root-only questions, `q06-containers-that-need-gpus` (Fargate
     has no GPUs), `q06-scaling-several-resource-types` (the scaling-plan naming).
   - *Assume the usual zonal NAT gateway, as the stem says:* `q07-nat-gateway-per-az`.
   - *Turn on an assumption in the stem:*
     - `q05-fast-scratch-space` assumes the instance type has instance store.
     - `q05-before-deleting-test-database` assumes "a few months" is longer than backup retention.
     - `q04-customer-specific-example` depends on the guide's reading of "customer-specific".
   - *Not blind-solved after one last distractor edit:* `q07-dx-media-transfers`.
3. **Guide pages corrected along the way.** The solvers found claims on the pages that were wrong or
   misleading. Each one was checked against current AWS documentation and corrected, with the source
   added and `facts_checked: 2026-10-24`. No headings changed. The matching glossary entries were
   corrected too.
   - Edge locations run more than CloudFront, Route 53 and Global Accelerator.
   - A pilot light's RPO can be far shorter than its recovery time.
   - The root email change applies to standalone accounts.
   - RDS still leaves Multi-AZ, backup retention and sizing to you.
   - RDS automated backups can be retained when the database is deleted.
   - Vault Lock's governance and compliance modes.
   - EBS snapshots are Regional.
   - Storage optimized instances.
   - The instance naming terms: family, series and options. The `06-01-name-decoded` figure was
     redrawn.
   - ELB health checks in Auto Scaling must be turned on.
   - Lambda doesn't keep state you can rely on between runs.
   - Zonal vs Regional NAT gateways.
   - CloudFront's Anycast static IPs.
   - Reply port ranges.
   - S3 replication of deletions.
   - Labs 03 and 04 no longer say they haven't been run.
4. **Smaller doubts left on the pages (low risk, no item depends on them):**
   - 02.03 links elasticity to performance efficiency and cost optimization but not reliability.
   - 02.02 says operating bills "often go up" in the cloud. That is true of the shift from capital
     to operating spending, but the page doesn't say so.
   - 07.02 presents the route table as a step an inbound request meets.
   - 04.01 doesn't say that Lambda container images leave the image's OS updates to you.
5. **What the format couldn't express:**
   - A bundle has one question pool, so modules, pages and exam tasks are tags, not sections. An
     app's tag filter is the only way to "follow along".
   - The item check's length heuristic can't tell a service's long and short official names apart
     from a giveaway.
   - Ordering tasks, such as "put these steps in order", aren't possible. Lab sequences were
     tested through their decisions instead.

A validator checks structure only. These items were checked against the guide by blind solvers,
but someone who knows AWS should review the answers before learners rely on them.
