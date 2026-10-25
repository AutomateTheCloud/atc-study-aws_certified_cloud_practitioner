# Brief: make one module concise and exam-focused

The owner decided on 2026-10-25 that the course is too extensive for a foundational exam. The
main path goes from about 57 hours to about **25 hours**. You rewrite one module to fit that
budget. This brief overrides the length rules and the lesson anatomy in
`design/module-writer-brief.md` and `design/conventions.md`; everything else in them still applies
(front matter, site contract, labs' safety rules, facts and dates, links to standards, US English,
the date format).

## The test for every paragraph

Keep a paragraph only if it helps a learner answer a CLF-C02 question. The exam guide sets the
depth (research repo `docs/01-exam-guide-clf-c02.md`, sections 2, 5 and 6):

- **The exam asks which service or concept fits, not how to build or fix it.** Coding, designing
  architectures, troubleshooting, implementation and load or performance testing are out of scope
  for the candidate. Teach what a service is for, what problem it solves and how it differs from the
  service it's confused with. Don't teach configuration, step-by-step design or internals.
- **In-scope services** (the guide's list): one or two short paragraphs each at most, often a
  table row. The more a task statement leans on it (EC2, S3, IAM, VPC basics, RDS/DynamoDB, the
  billing tools), the more room it gets.
- **Out-of-scope services** (the guide's list, for example CodeDeploy, CloudShell, Transfer
  Family, MemoryDB, Personalize, Network Firewall): at most one line, only where the exam uses them
  as wrong answers. Otherwise leave them out.
- **Advanced topics** (anything an Associate-level exam would test: detailed networking, policy
  syntax, architecture patterns, pricing arithmetic beyond the basic idea) go to the module's
  "Beyond the exam" page, or are dropped. The owner will build higher-level courses for them.

Facts stay exactly as true as they are now. When you shorten, keep the qualifier that makes a
statement true (see the writer brief's "Verify as you write"). Don't add new facts; if you must,
verify them on AWS's pages.

## Budget (words by full count, including front matter)

| Page | Target |
|---|---|
| Brief (`00-brief.md`) | 400–600 |
| Lesson | 1,500–2,500. Merge lessons when two would each be thin. |
| Simulation | at most 1,500, and only if it practices an exam decision; otherwise cut it or fold its best decision into a lesson as a "Your turn" |
| Mastery check (`NN-check.md`) | at most 3,000: Check A of 10 items, Check B a parallel retest of 10, a short correction map. No enrichment section. |
| "Beyond the exam" page (new, `NN-beyond-the-exam.md`, `type: page`) | at most 800: a short list of the topics left out, one or two sentences each, with the AWS page to read. Say once that later, higher-level courses will cover them. |
| Core lab | at most 2,500 |
| Optional lab | unchanged except: title starts "Optional lab NN:", and the brief and lessons say it's optional |

Your module's total budget for lessons (not counting the other pages) is in your assignment.

## Lean lesson anatomy (replaces conventions, "Concept lessons")

1. H1 stating the main idea; a key message of one or two sentences.
2. The reader/time line (time for the new length: about 150 words a minute plus activities) and
   "Before you start" (one line).
3. Warm-up: one or two retrieval questions, with feedback.
4. Objectives (two to four) and one prequestion.
5. One big-picture diagram if it explains something; key terms only as inline definitions (the
   glossary holds the rest).
6. Two to four sections. One "Your turn" in the lesson, two at most. Misconception boxes only for
   misconceptions the exam actually tests (course plan section 7), keeping their three moves.
7. At most one short worked example (an `**Example:**` callout) where a decision needs showing.
8. Summary (three to five bullets); retrieval practice of three items, every option explained;
   "Where to check the current details" (three links at most).
9. The attribution line.

Drop "In real work" sections and long "What's the same / What differs / The principle" blocks;
fold a one-line version into the summary if it matters. Keep explanatory visuals that teach an
exam distinction; drop charts that teach arithmetic the exam doesn't need, and delete their image
files and chart scripts.

## Keep consistent

- **`tasks` front matter** must name the exam tasks the page really covers: a script will turn it
  into the "Exam guide" line under each title, so don't write that line yourself.
- **`terms_introduced`** lists only terms the page still defines. Report every term you removed
  or moved, and every page you renamed, merged or deleted (old path → new path), so the glossary,
  links and practice questions can be updated.
- **Core labs** are 01, 02, 03, 05, 08, 12, 15, 17 and 19 (close-out). All other labs become
  optional: retitle them, keep them working, and don't trim their steps.
- The running case (the bakery) stays, but in one or two sentences per lesson, not a story arc.
- Liability notices stay word for word.

## Check before you finish

- Run the site check (writer brief, "Check before you finish") and fix every finding on your
  pages. List broken links that come from other modules into yours.
- `python3 -I source/tools/fix_choice_breaks.py guide/MM-*/*.md`.
- Report each page's old and new word count.

Write only your module's pages, their images and chart scripts. Don't edit other modules,
`reference/`, `practice/`, `course.yaml` or `guide/README.md`. Don't commit.

## Final message (under 400 words)

Pages with old → new word counts; pages renamed, merged or deleted; terms removed or moved;
what went to "Beyond the exam"; sims cut; broken inbound links; anything you were unsure about.
