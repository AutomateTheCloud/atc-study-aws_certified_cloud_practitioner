# Writing conventions

How every page of the guide is built. For authors and reviewers; learners never see this file. The
project rules in `CLAUDE.md` come first, then this file, then the study-material-design skill in the
`study-learning-design` repo. The course plan (`course-plan.md`) says what each page covers.

## Reader

Every page opens with a one-line reader statement in learner terms, adapted from the course plan's:
an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely.

## Files

- Path: `guide/MM-module-slug/PP-page-slug.md`, as in the course plan section 9. Lowercase ASCII,
  hyphens, two-digit prefixes.
- Images: `images/MM-PP-descriptor.png|svg`. Diagram sources: `diagrams/`. Chart scripts: `source/charts/`.
- Links inside the guide are relative `.md` links. Links to the guardrails primer use its GitHub
  address, `https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/<page>.md`,
  until the learning site exists.

## Front matter

Every page starts with YAML front matter, which the site and PDF builds read:

```yaml
---
type: lesson            # lesson | lab | sim | brief | task-card | reference
id: clf-02-01           # stable; never changes after publication
title: "What cloud computing is"
tasks: ["1.1"]          # CLF-C02 task statements
objectives: ["02.01a"]
pillars: [cost-optimization]   # Well-Architected pillars the page touches
facts_checked: 2026-10-24
sources: ["https://docs.aws.amazon.com/..."]
---
```

Labs add `lab`, `rung`, `mode` (real | sim), `free_plan`, `time`, `cost`, `worst_case` and
`needs`. Leave `last_run_pass` out until a lab has been run end to end on a fresh account.

Front matter is for the builds. Everything a learner needs (time, cost, prerequisites) is also in
the page text.

## Concept lessons

Follow the skill's concept-lesson template and lesson sequence:

1. H1 that states the main idea; a two- or three-sentence key message.
2. Reader line, time, and "Before you start" (earlier lessons; what to do if they don't exist yet).
3. **Warm-up:** two or three retrieval questions on earlier material, with feedback (course plan
   section 6). The first module's warm-ups draw on everyday experience and the guardrails primer.
4. Objectives in learner words, and one to three prequestions to guess at.
5. The big-picture diagram, then key terms (skip-if-known).
6. Sections, each main point first, each ending in a "Your turn" task with a model answer or
   per-option feedback in a `<details>` block.
7. A worked example with the expert's thinking visible.
8. "In real work", naming the Well-Architected pillar where one fits.
9. Summary; retrieval practice (3–5 items on this lesson, 1–2 on earlier ones), every option
   explained; "Where to check the current details".
10. The attribution line from the licensing playbook, section 7.

Aim for 2,000–3,500 words. Domain 1 and 2 lessons run about 35 minutes of study; Domain 3 lessons
about 25.

## Labs

Follow the skill's lab template and `CLAUDE.md`:

- The approved liability notice (research repo `docs/13`), word for word, before the first step.
- Goal and end state; what it creates; time; cost on the Free plan and the worst case on a Paid
  plan; the safety prerequisites (primer pages 02, 03 and 05, linked).
- Region `us-east-1`; tags `guide=clf` and `lab=NN` on everything created.
- Steps with "You should see" and recovery blocks; console labels hedged or dated in the step.
- Check your work; cleanup with a check that it worked; a next-day check where billing is involved.
- A sidebar for learners on the new sign-up experience.

## Simulations

Ship a static version first: the scenario, the data as tables, the decisions to make, and model
answers. It must work as plain Markdown, on the site and in the PDF. Interactive versions come later
in `source/sims/`.

## Facts and wording

- Facts trace to the research repo. Volatile facts carry their check date where they appear.
- Exam name and current name at first mention (`docs/10`).
- Original words only; no copying or close paraphrase of AWS documentation or third-party courses.
  Short console labels may be quoted with their date.
- Name the misconceptions in the course plan section 7 for the module, and refute them; teach the
  confused pairs side by side.
- Everything the research marks unverified stays labeled for the learner, or is left out.

## Links to standards

Every Well-Architected best-practice ID, design principle, CLF-C02 task statement and CIS
benchmark reference links to its official page. After writing, run:

```
python3 -I ../study-aws-certified_cloud_practitioner/tools/link_refs.py \
  ../study-aws-certified_cloud_practitioner/sources/wa-bp-urls.tsv guide/MM-*/*.md
```

It adds the links and flags titles that differ from AWS's current wording.

## Visuals

The owner wants the guide visually rich and engaging (2026-10-24). Every visual must teach, never
decorate: learning research shows explanatory visuals help and decorative ones hurt. So plan the
visuals for a page before writing it, and use many of them:

- **Every lesson:** a big-picture visual near the top, and at least one more visual for most
  sections. A lesson with fewer than three visuals needs a reason.
- **Numbers become charts.** Costs over time, demand curves, comparisons of prices or durations:
  draw them as a chart, not only a table. Keep the table too, as the accessible version.
- **Systems and flows become diagrams.** Anything with parts that interact, nest or happen in order.
- **Confused pairs become comparison graphics** (side-by-side panels or a decision flowchart), in
  addition to the comparison table.
- **Screenshots** where seeing the screen helps a step (approved, redacted ones only).
- Each visual has a caption that says what to notice, alt text, and a visible long description or
  data table. Color never carries meaning alone, and colors work in light and dark mode.

**How to make them:**

- Diagrams and flowcharts: Mermaid in the page for drafts. No AWS icons in Mermaid; when a diagram
  needs service icons, draw it with AWS Icons for PlantUML (source in `diagrams/`). Never adapt an
  AWS diagram.
- Charts: generate SVG from a script in `source/charts/` (software, so Apache-2.0 under
  `LICENSE.md`; two-line SPDX header), output in `images/MM-PP-descriptor.svg`, so charts can be
  regenerated when numbers change. The SVGs themselves are illustrations under CC BY-NC. Follow
  the dataviz skill for chart design.
- All three editions must render every visual; prefer SVG for drawn images.

## Attribution line

```
---

"<Page title>" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
```
