# Blueprint: Module 03, AWS around the world

Items file: `practice/items/03-aws-around-the-world.yaml`. Main task: 3.2 (global infrastructure).
Module 03 has four objectives (course plan section 4); each is split below by the page section
that teaches it, so the counts show where the questions sit. Region and AZ counts are not tested
(the guide says not to memorize them); the "at least three AZs per Region" design minimum is used
only inside explanations and distractor feedback.

Level tags from the course plan: C concept, J judgment; Un understand, Ap apply, Ev evaluate.

Counts are the actual counts in the items file. Planned counts were 60 questions (12 multiple
response) and 15 cards; the result is 63 and 15.

| Objective | Wording (course plan) | Level | Page and section | Questions (of which Select TWO) | Cards |
|---|---|---|---|---|---|
| 03.01a | Explain how Regions, AZs and data centers nest, and how that gives high availability | C·Un | 01, "A data center is a building; an Availability Zone is one or more of them" + misconception "An AZ is one data center" | 2 (0) | 1 |
| 03.01a | | | 01, "Availability Zones don't share a single point of failure" | 2 (1) | 0 |
| 03.01a | | | 01, "A Region is at least three Availability Zones in one area" + misconception "A Region can have just two AZs" | 2 (1) | 1 |
| 03.01a | | | 01, "Where your resources live: in one AZ, across a Region, or everywhere" | 3 (1) | 1 |
| 03.01a | | | 01, "High availability means running in more than one Availability Zone" + worked example | 3 (0) | 0 |
| 03.01a | | | 05 (Lab 02), Region selector (opt-in Regions); AZ names and AZ IDs | 2 (0) | 0 |
| 03.02a | Choose a Region for a workload and justify the choice | J·Ap | 02, "The big picture: two filters, then a trade-off" | 0 | 1 |
| 03.02a | | | 02, "Rules first: decide where the data may live" | 5 (1) | 2 |
| 03.02a | | | 02, "Then check that the Region has the services you need" | 2 (0) | 0 |
| 03.02a | | | 02, "Pick the shortlisted Region closest to your users" + misconception "nearest your office" | 2 (0) | 0 |
| 03.02a | | | 02, "Weigh the price: the same thing costs different amounts in different Regions" | 2 (0) | 1 |
| 03.02a | | | 02, "Use more than one Region only when you have a reason" | 4 (2) | 0 |
| 03.03a | Choose a resilience approach from RTO, RPO and budget | J·Ev | 03, "High availability and disaster recovery answer different questions" + misconception "HA = DR" | 3 (1) | 1 |
| 03.03a | | | 03, "RTO and RPO: how long you can be down, and how much you can lose" | 3 (0) | 1 |
| 03.03a | | | 03, "Four strategies, from cheap and slow to costly and fast" + worked example | 7 (1) | 2 |
| 03.03a | | | 03, "Replication copies your mistakes; backups undo them" + misconception "replication replaces backup" | 2 (0) | 0 |
| 03.03a | | | 06 (Sim S2), ladder (Decision 1) and strategy choices (Decisions 3 and 4); "The rules of this simulation" | 4 (1) | 1 |
| 03.04a | Say where each kind of edge site runs and what it's for | C·Un | 04, "Edge locations deliver and answer close to users; they don't run your servers" | 4 (1) | 1 |
| 03.04a | | | 04, "Three services use the edge, each in its own way" (CloudFront, Route 53, Global Accelerator) | 4 (0) | 0 |
| 03.04a | | | 04, "Local Zones, Outposts and Wavelength run AWS servers outside a Region" + comparison table + worked example | 7 (2) | 2 |
| | | | **Total** | **63 (12)** | **15** |

Every objective is covered; the central judgment objectives (03.02a, 03.03a) carry the most
questions. Confused pairs from course plan section 7 used as distractors: Region / AZ / edge
location / Local Zone / Outposts (and Wavelength); HA vs DR; RTO vs RPO; pilot light vs warm
standby; CloudFront / Route 53 / Global Accelerator. Misconceptions refuted: an AZ is one data
center; a Region can have two AZs; HA equals DR; replication replaces backup; choose the Region
near your office; Route 53 is a CDN.

## Checks

Build, lint (0 errors, 0 warnings) and check_items (no warnings on q03/c03 items) are clean.
A fresh helper solved all 63 questions blind from the module's pages: 63 of 63 matched the key.
Its notes led to: Q `q03-pick-warm-standby` RTO changed from about 10 to about 5 minutes (10 sat on
the pilot-light boundary); a Wavelength distractor made clearly wrong; five variant wordings
tightened; two cards re-pointed or trimmed to what their cited section says.

## Final counts

- Questions: 63 (51 single answer, 12 "Select TWO").
- Per page: 01: 12; 02: 15; 03: 15; 04: 15; 05 (Lab 02): 2; 06 (Sim S2): 4.
- Per level: recall 11 (17%), understanding 28 (44%), application 24 (38%). Application runs above
  the 30% target because two of the four objectives are judgment objectives (Ap, Ev).
- Concept cards: 15 (01: 3; 02: 4; 03: 4; 04: 3; 06: 1). The glossary already supplies term, abbreviation
  and "different from" cards for the module's 44 terms, so the concept cards hold rules, "why"
  cards and how-to-choose cards only.
