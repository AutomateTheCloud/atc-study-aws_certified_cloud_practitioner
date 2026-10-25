# Writer's brief: exam preparation pages (mixed sets and practice exams)

You write pages in `guide/90-exam-prep/` of Automate the Cloud's **Study Guide for the AWS Certified
Cloud Practitioner Exam (CLF-C02)**, in `/data/atc/study/atc-study-aws_certified_cloud_practitioner`.
Read `design/check-writer-brief.md` first: its item rules, clean room, similarity check, site check
and blind-solve steps all apply. Its page structure doesn't; this brief's does.

Also read: `design/course-plan.md` section 6 (mixed sets after Modules 05, 09 and 13, interleaved
and weighted by domain; practice exams: at least two full forms in exam format, as of 2026-10-23
65 items, 90 minutes, single and multiple response, weighted 24/30/34/12; readiness scored only on
unseen items, as a range per domain; never claims to predict a score),
`guide/00-start-here/03-the-exam-at-a-glance.md` (the exam's format and scoring as the guide
teaches it), the research repository's `docs/01-exam-guide-clf-c02.md` (task statements and
domain weights; never its practice questions), and every module brief.

Your items must be new: different scenarios and wording from the lessons' checks, the mastery
check pages (`guide/*/NN-check.md`), the practice bundle (`practice/items/`) and the other
exam-prep pages. Spread items across every task statement in proportion to the domain weights;
mix single answer (four choices) and "(Select TWO.)" (five choices) about four to one; scenario
stems like the exam's; no prices or volatile counts; one defensible answer that holds on real AWS
too; exam names where the exam uses them, with today's names in the explanations.

- **Answer choices on separate lines:** the site joins consecutive lines into one paragraph, so end every
  choice line that is followed by another choice line with a backslash (`A. Elasticity\`), or write
  the choices as a bulleted list. Otherwise "A. … B. … C. …" shows as one run-on line.

## Page format

- Front matter as the site contract requires (`type: check`, `id: clf-90-NN`, `tasks` listing
  every task the page covers, `objectives: []`, `prerequisites` the module briefs it assumes).
- A short "How to take it" (time limit, closed book, no answers until you finish, how to score).
- The questions, numbered, with choices, and **no answers inline**.
- **Answer key** after all the questions: for each item, the answer, the task statement, a two-
  to-four-sentence explanation (why right, why the tempting wrong choice is wrong) and a link to
  the section that teaches it. Put the whole key inside one `<details><summary>Answer key</summary>`
  block, so it doesn't spoil the questions.
- **Score by domain:** a table that turns a learner's correct answers per domain into a readiness
  band (for example "below 60%: restudy", "60–79%: review the linked sections", "80% or more:
  ready on this domain"), with the domain's share of the exam, and a plain statement that a
  practice score is not a prediction of an exam score.

## Check

Similarity (every question, with its choices) into `<scratchpad>/exam-NN/candidates.jsonl`, run
the checker as the check brief says (never `--show-text`), and rewrite every REJECT or REVIEW item;
the site check (0 errors, 0 warnings on your pages); and a blind solve by a fresh helper from the
guide pages (give it the page with the answer key removed), fixing every disagreement or two-
defensible flag and re-checking fixed items with another fresh helper. Don't commit.
