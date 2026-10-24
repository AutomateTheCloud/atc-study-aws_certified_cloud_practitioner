# Reviewer's brief: review and fact-check one module

A module's pages have just been written by several writers working in parallel, following
`design/module-writer-brief.md`. Your job is to make the module correct, consistent and
contract-clean before its glossary terms and practice items are written from it. Paths are
relative to `/data/atc/study/atc-study-aws_certified_cloud_practitioner` unless absolute.

## Read first

- `design/module-writer-brief.md` (everything the writers were told) and everything it says to read
  first, in particular the design skill's review checklist
  (`/data/atc/study/study-learning-design/skills/study-material-design/`), `design/conventions.md`,
  your module's rows in `design/course-plan.md` sections 4–7, and section 3 of
  `/data/atc/atc-learn-site/docs/COURSE-AUTHORING.md`.
- Every page of your module, whole.

Clean room: never open `/data/atc/study/study-aws-ccp-dump-analysis/`, `sources/practice-bank/`,
`docs/02a-official-sample-questions.md` or `docs/06-practice-exams.md` in the research repository.

## What to do

1. **Fact-check every factual claim** that a learner could be tested on or act on: what a service
   does, who is responsible for what, defaults, limits, names and statuses, prices, free-tier
   terms, console labels in labs. Check each against current official AWS documentation with
   WebSearch and WebFetch (`docs.aws.amazon.com`, `aws.amazon.com` only). For each claim that is
   wrong, or simplified until a careful learner would be misled, correct the page with the
   smallest edit that makes it true at the guide's level, in the page's voice, add the source URL
   to `sources`, and set `facts_checked` to today. AWS text is CC BY-SA: never copy or closely
   paraphrase it.
2. **Review against the checklist:** objectives covered at their level; warm-ups and review
   questions per the course plan; misconceptions refuted and confused pairs taught side by side;
   every `**Your turn:**` has a model answer and every check its feedback; `terms_introduced`
   lists only terms the page defines; exam names vs current names; dated facts dated; visuals
   present, with alt text and long descriptions; the running case consistent with earlier modules
   and between this module's pages; no duplicated teaching between sibling pages; links between
   sibling pages working; labs safe (nothing billed hourly, cleanup in dependency order, the
   liability notice word for word, the new sign-up path callout).
3. **Fix what you find.** You may change headings in this module only if one is wrong, duplicated
   or misleading (nothing cites these pages yet). Keep each writer's structure otherwise.
4. **Run the checks:**

   ```bash
   cd /data/atc/atc-learn-site && node scripts/courses.mjs --check --only clf --worktree clf=/data/atc/study/atc-study-aws_certified_cloud_practitioner
   ```

   It must report 0 errors and 0 warnings for your module's pages. Re-render any chart you changed
   (its script in `source/charts/`) and look at it in light and dark mode.

Edit only your module's pages, its images and chart scripts. Don't touch `course.yaml`, the glossary,
`practice/` or other modules (if an earlier module's page contradicts yours, say so instead). Don't
commit.

## Final message

A table of the claims you corrected (page, old claim, new claim, source URL); the review fixes you
made; anything you couldn't verify; contradictions with other modules; questions for the owner.
