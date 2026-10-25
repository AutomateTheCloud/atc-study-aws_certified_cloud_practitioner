# Handoff: where the course stands and how to carry on

Written 2026-10-25 so a new session can pick up without the old conversation. Read this, then
`design/owner-questions.md`.

## State

- **Guide:** every page in `design/course-plan.md` exists: Start here (with `06-diagnostic`),
  Module 01 (optional on-ramp), Modules 02–13 (each ending in `NN-check.md`), Module 14 (capstone,
  Labs 18–19), `90-exam-prep` (how-to, three mixed sets, two 65-item practice exams), `98-how-to`
  (nine task cards) and `99-reference` (glossary plus generated reference pages). 149 pages; the
  site contract check passes with 0 errors.
- **Released:** tag `v0.2.0` (2026-10-24) on `ff345ee`. The learning site's daily release
  workflow opens the publishing pull request. The primer's latest release is `v0.1.1`.
- **Practice bundle:** `practice/`, version 0.3.1: 922 questions (three wordings per choice) and
  1,693 flashcards. Every item was solved blind against the guide; every wording passes the
  dump-similarity check (0 REVIEW, 0 REJECT). The site doesn't publish `practice/`.
- **Owner review:** the owner reviews from the published site. Decisions taken without them, and
  open questions, are in `design/owner-questions.md`.

## Live lab runs (done 2026-10-25)

All labs have been run in the test account (`atc-test-01`), driven over CDP from
`/data/atc/study/_captures/aws-test-account/` (`cdp.py` has `type` with `NTH=`, a CloudShell `sh`
command, and a FRAME mode that picks the largest console frame). Ground rules and driving notes are
in the memory file `test-account-browser-control`; keep the Amazon Q side panel closed for captures.

- Labs 01, 03, 04 (2026-10-24) and 02, 05–15, 17, 18 (2026-10-25) carry `last_run_pass`; their
  pages were corrected from what the console showed. The private step-by-step log is
  `_captures/aws-test-account/lab-runs-2026-10-25.md`; the publishable summary is the research
  repo's `docs/16`.
- **Lab 12** stopped at Artifact's "Accept terms to download report" by decision (a legal agreement
  in the owner's name); steps 19–20 follow AWS's documentation.
- **Still due (2026-10-26):** Lab 16 steps 9–11 (Cost Explorer group by tag `lab`; showed "No tags"
  on day one) and Lab 19 Part E (credits were $160.00, $0 used, at 2026-10-25 11:27). Add
  `last_run_pass` to Labs 16 and 19 when those pass. Also check whether the SNS subscription for the
  deleted `clf-lab11-orders-failing` topic has cleared.
- **Screenshots:** 65 first-pass redactions of 2026-10-25 captures are in `redacted/`, logged in
  `redaction-log.tsv` with `checked_by` empty: the owner approves them before any enters the repo.
  The Lab 15 shared estimate (generic figures) stays public for a year.
- Open question for the owner: whether Module 03 should use AWS's long-running `me-central-1`
  (UAE) Region outage as a real Region-isolation example.

## How things are built (all generated files have a `--check` mode)

| Output | Source | Command, from the repository root |
| --- | --- | --- |
| `guide/99-reference/01-glossary.md` | `reference/glossary.yaml` | `python3 -I source/glossary/build_glossary.py` |
| `guide/99-reference/02, 03, 04, 06` | glossary, `reference/names.yaml`, `reference/services.yaml`, page front matter | `python3 -I source/reference/build_reference.py` |
| `guide/README.md` (contents) | `course.yaml`, page front matter | `python3 -I source/contents/build_contents.py` |
| `practice/clf-c02-practice/study.yaml` | `practice/bundle.yaml`, `practice/items/`, the glossary | `python3 -I source/practice/build_bundle.py` |
| `practice/clf-c02-practice.waymark` | the above | `npx --yes @automatethecloud/openwaymark pack practice/clf-c02-practice -o practice/clf-c02-practice.waymark` |

Other checks:

- **Site contract:** `cd /data/atc/atc-learn-site && node scripts/courses.mjs --check --only clf --worktree clf=<path>`.
  To check only what's committed, run it on a `git worktree` of `HEAD`, not on a working tree
  where agents are writing (never `git stash` while agents work).
- **Answer choices on consecutive lines** must end in a backslash or be a bulleted list (the site
  joins lines): `python3 -I source/tools/fix_choice_breaks.py guide/*/*.md` fixes it.
- **Dump similarity:** `cd /data/atc/study/study-aws-ccp-dump-analysis && python3 -I tools/check_similarity.py --candidates <jsonl> --summary`.
  Never `--show-text`: the author stays in the clean room. Rewrite REVIEW and REJECT items with
  new scenarios and choice sets; never rename services to get past it.
- **Blind solve:** `blind_solve.py make|score` from the openwaymark-study-bundles skill; the
  solver brief is `practice/work/solver-brief.md`. Move `blind-key.json` away before a helper
  starts.

## Briefs for new work

- Guide pages: `design/module-writer-brief.md`, reviewed with `design/module-review-brief.md`;
  glossary terms with `design/glossary-extension-brief.md`.
- Check pages: `design/check-writer-brief.md`; exam prep: `design/exam-prep-brief.md`.
- Practice items: `practice/work/writer-brief.md`; fixes after a blind solve:
  `practice/work/fix-brief.md`.
- Exam-prep item sources (the generators the writers used, for reference; the pages are now the
  source of truth): `practice/work/exam-sources/`.

## Working rules learned this session

- **Owner:** produce everything, then review; no per-module sign-off (memory
  `finish-all-material-first`). Owner trusts judgment on similarity REVIEW items (rewrite blind).
- **Tokens** (memory `token-budget`): Sonnet for blind solves, fixes, glossary merges and
  similarity reruns; Opus only for writing and fact-checking pages. One blind solve per item set
  plus at most one re-check. Trimmed briefs. One agent per module. Scripts for mechanics. Stop
  finished agents whose wait timers keep waking them.
- Give each parallel agent its own scratch folder; shared names collided.
- Commits: `git commit -s` with david.singer@automatethe.cloud; no AI tool named in commits.
- Editorial calendar: WorkSpaces Secure Browser closes 2026-10-29 (Module 10 says "closes", then
  "closed since"); Snowball support ends 2026-12-31; legacy Support plans end 2027-01-01 (Module
  12's dated box); Amazon Q Developer plugins and subscriptions end 2027-04-30.
