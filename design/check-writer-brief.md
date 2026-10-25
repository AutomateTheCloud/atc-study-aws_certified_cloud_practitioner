# Writer's brief: a module's mastery check page

You write the mastery check page that ends one module of Automate the Cloud's **Study Guide for
the AWS Certified Cloud Practitioner Exam (CLF-C02)**, in
`/data/atc/study/atc-study-aws_certified_cloud_practitioner` (paths relative to it). The message
that sent you here names the module(s), the file name and the number of items.

## Read first

1. The design skill's references on checks and the mastery loop:
   `/data/atc/study/study-learning-design/skills/study-material-design/references/course-architecture.md`
   (section 4, the mastery loop), `assessment-notes.md`, `page-templates.md` and `style-rules.md`.
2. `design/conventions.md`, and `design/course-plan.md` section 6 ("Mastery check and parallel
   retest": every objective at its level, scenarios for Ap and higher, the module's confused pairs
   from section 7, a correction map, enrichment).
3. The site contract: `/data/atc/atc-learn-site/docs/COURSE-AUTHORING.md` section 3 (front matter;
   `type: check`; callouts; answers in `<details>`; the attribution line). Don't change anything in
   `/data/atc/atc-learn-site`.
4. Every page of the module, whole: its objectives (front matter `objectives`, the brief's table),
   its confused pairs and misconceptions, and its in-lesson checks and practice, which your items
   must not repeat.
5. The module's practice-bundle items, `practice/items/NN-*.yaml`: learners see those too, so your
   items must test the same objectives with different scenarios and wording.

**Clean room.** Never open `/data/atc/study/study-aws-ccp-dump-analysis/` (except to run its
checker as below), `sources/practice-bank/`, or the research repository's
`docs/02a-official-sample-questions.md` and `docs/06-practice-exams.md`. Write every item fresh.

## The page

File `guide/MM-<module-folder>/PP-check.md`, `id: clf-MM-PP`, `type: check`, title "Module MM
mastery check", the module's `tasks` and `objectives` in front matter, `prerequisites` the
module's lessons. Structure:

1. **How to use this check:** take Check A closed-book; the threshold is 80%; if you score below
   it, use the correction map, then take Check B (the parallel retest); if you pass, do the
   enrichment. Say it once, plainly.
2. **Check A:** the number of items you were given. Every objective gets at least one item at its
   level (Re/Un items may be single-answer; Ap and higher are short scenarios). Cover the module's
   confused pairs. Mix single-answer (four choices) and "(Select TWO.)" (five choices) the way the
   exam does, about a fifth multiple. Each item's answer and feedback (why the right choice is
   right, why each wrong one is wrong) in a `<details><summary>Answer</summary>` block right after
   it.
3. **Correction map:** a table from each Check A item to its objective and the exact section
   (linked heading) to reread, and the lab or simulation that practices it.
4. **Check B: parallel retest:** the same number of items, one-for-one on the same objectives and
   levels as Check A, with new scenarios and new choices (never the same question reworded), each
   with its answer in `<details>`.
5. **Enrichment:** two or three harder tasks for learners who pass (a design to justify, a
   real-world complication, a link to a Well-Architected best practice), with model answers.

- **Answer choices on separate lines:** the site joins consecutive lines into one paragraph, so end every
  choice line that is followed by another choice line with a backslash (`A. Elasticity\`), or write
  the choices as a bulleted list. Otherwise "A. … B. … C. …" shows as one run-on line.

Item rules: test the guide's ideas at the guide's level, with one defensible answer that holds on
real AWS too; no prices, counts or other volatile facts; no "all/none of the above"; avoid negative
stems; vary the correct position; parallel choices. Use the exam's names where they differ, and the
current name in feedback, as the pages do. Don't key an answer on a point the pages leave open.

## Check before you finish

- Write every Check A and Check B question as JSONL for the dump-similarity checker, one line per
  question: `{"id": "...", "question": "...", "options": {"A": "...", ...}, "answer": ["B"]}`, into
  `<scratchpad>/checks-MM/candidates.jsonl` (`<scratchpad>` is
  `/tmp/claude-1000/-data-atc-study-study-aws-certified-cloud-practitioner/90d7019c-4727-40dc-b5e8-2d3498ef2995/scratchpad`),
  then run
  `cd /data/atc/study/study-aws-ccp-dump-analysis && python3 -I tools/check_similarity.py --candidates <that file> --summary`
  (never `--show-text`). Rewrite any REJECT or REVIEW item with a new scenario and, for "same
  services + same correct answer", a different choice set; never by changing service names. List
  any REVIEW you can't clear without making the item worse.
- Run the site check: `cd /data/atc/atc-learn-site && node scripts/courses.mjs --check --only clf --worktree clf=/data/atc/study/atc-study-aws_certified_cloud_practitioner`
  (0 errors and 0 warnings on your pages).
- Have a **fresh** helper agent answer Check A and Check B blind from the module's pages, with your
  answers removed (copy the page with the `<details>` blocks stripped into your scratch folder);
  fix every item where its answer differs from yours or it flags two defensible answers, and check
  the fixed items again with another fresh helper.

You may edit only your check page(s) and, in the module's `00-brief.md`, the one line or section
that mentions the mastery check, to link your page. Keep scratch files in `<scratchpad>/checks-MM/`.
Don't commit.

## Final message

Items per objective and level for Check A and B; similarity results; blind-solve score; anything on
the module's pages that looked wrong or unclear.
