# Writer's brief: guide pages for one module

You write pages of Automate the Cloud's **Study Guide for the AWS Certified Cloud Practitioner Exam
(CLF-C02)**, in `/data/atc/study/atc-study-aws_certified_cloud_practitioner` (paths below are
relative to it unless absolute). The message that sent you here names your module, your pages,
and the other writers working on the same module at the same time.

Modules 00 and 02–07 are written. Read the earlier modules' pages your lessons build on, and build
on them rather than re-teach them. Modules being written at the same time as yours don't exist yet:
mention them by title only, never link to them (a link to a missing page fails the site build).

## Read first, in this order

1. The design skill: `/data/atc/study/study-learning-design/skills/study-material-design/SKILL.md`
   and the reference files it directs you to (page templates, style rules and the review checklist
   at minimum).
2. Project rules: `CLAUDE.md`; `design/conventions.md` (page anatomy, front matter, labs, sims,
   visuals, linking, the reference linker); `design/course-plan.md` sections 1–4 (your module's
   scenario, lessons, coverage and objectives), 5 (your labs and sims), 6 (spaced review: what your
   warm-ups draw on) and 7 (your module's misconceptions and confused pairs).
3. The site contract every page must pass: `/data/atc/atc-learn-site/docs/COURSE-AUTHORING.md`
   section 3 (the checklist for every page: front matter fields, one H1, headings, callout labels,
   answers in `<details>`, links, images, Mermaid `accTitle`/`accDescr`, the attribution line) and
   `/data/atc/atc-learn-site/docs/CONTRACT.md` sections 3 and 7. Don't change anything in
   `/data/atc/atc-learn-site`.
4. Model pages, written and corrected: `guide/07-connecting-it/02-filtering-traffic.md` (a lesson),
   `guide/07-connecting-it/00-brief.md` (a brief), `guide/04-shared-responsibility-and-access/06-lab-03-a-group-and-a-policy.md`
   and `guide/02-why-the-cloud/06-lab-01-first-resource.md` (labs run live), and
   `guide/07-connecting-it/06-sim-packet-journey.md` (a simulation). Copy their structure and
   front matter, not their words.
5. Research, for facts: `/data/atc/study/study-aws-certified_cloud_practitioner/docs/`:
   `01-exam-guide-clf-c02.md` (your task statements), the `04-services/*.md` files for your
   services, `03-whitepapers-and-concepts.md`, `10-names-and-status.md` (exam names vs current names,
   closures, dates), `13-content-decisions.md` (owner decisions A1–A9 and B1–B16: follow them),
   `12-labs-and-simulation.md`, `16-test-account-findings.md` (what a real new account shows),
   `11-glossary-reference.md`, and `08-landscape/` (how others teach it and the errors in
   circulation: for misconceptions only, never wording). Prices: the summaries in
   `/data/atc/study/study-aws-certified_cloud_practitioner/sources/raw/pricing/` (US East (N.
   Virginia), from AWS's Price List files); date every price "as of" its retrieval date and cite
   the service's pricing page. Never invent a price.
6. The guardrails primer, which labs depend on: `/data/atc/study/atc-study-aws_account_guardrails/primer/`
   (page IDs `guardrails-00` to `guardrails-10`; link it by GitHub URL as the conventions say).

**Verify as you write.** You may use WebSearch and WebFetch, but only on `docs.aws.amazon.com` and
`aws.amazon.com`, to confirm a fact or get the right page to cite. A fact-check after the last
modules found 16 places where the guide had simplified a fact until it was wrong (for example, "a
NAT gateway lives in one AZ" when a Regional option exists, or "Vault Lock stops everyone" when
that's true only in compliance mode). Say the guide-level truth, with the qualifier that makes it
true. Read AWS pages for facts only: their text is CC BY-SA, so never copy or closely paraphrase
it, and never adapt AWS diagrams.

**Clean room.** Never open `/data/atc/study/study-aws-ccp-dump-analysis/`, anything under
`sources/practice-bank/`, `docs/02a-official-sample-questions.md` or `docs/06-practice-exams.md`.
Write every question and task fresh.

## Rules that matter most

- **Every page passes the site contract.** Front matter as in the model pages and the contract
  (`id` `clf-MM-PP`; `type`; `title` up to 90 characters; `sources` public `https://` only;
  `prerequisites` and `needs` real page IDs of pages that exist now; lab fields only on labs and
  sims). One H1. Callout labels exactly as the checklist lists them. Every Mermaid block has
  `accTitle:` and `accDescr:` lines after its first line. The page ends with `---`, a blank line
  and the three-line attribution naming the `title` exactly.
- **`terms_introduced` lists only terms the page defines in its text.** A glossary is built from
  them.
- **Visuals:** plan them before writing (conventions, "Visuals"). Charts as SVG from a script in
  `source/charts/MM-PP-charts.py` using `chartkit.py` (house style; don't modify it); diagrams as
  Mermaid. Invoke the dataviz skill before writing chart code. Render every SVG and look at it in
  light and dark mode. Image files are `images/MM-PP-descriptor.svg`, with alt text and a long
  description as in the model pages.
- **The running case** is the bakery from earlier modules: its site runs on AWS (an EC2 web
  server, an RDS order database, Lambda functions, an S3 photo bucket, the VPC from Module 07).
  Keep its details consistent with earlier pages.
- **Warm-ups** draw on the previous module, one two to four back, and one from 02–04 (course plan
  section 6). Refute your module's misconceptions (section 7) where they fit, and teach its
  confused pairs side by side.
- **Names:** the exam's name and the current name at first mention, per `10-names-and-status.md`.
  Services closed to new customers or out of the exam's scope are taught as such, with dates.
- **Dates:** prices, limits, counts, plan details and anything AWS changes get a
  `**Dated (checked YYYY-MM-DD):**` callout or an "as of" date where they appear.
- **Links to standards:** every Well-Architected best-practice ID, design principle, task statement
  and CIS reference links to its official page. When you finish, run the linker command in
  `design/conventions.md` on your files and check what it changed.
- **Length:** lessons 2,000–3,500 words; a brief under 800; a lab under 2,000; a sim under 1,500.
- **Labs** follow conventions "Labs": the liability notice word for word, `us-east-1`, tags
  `guide=clf` (decision B11) and `lab=NN`, a cost box, cleanup in dependency order with a check that nothing
  tagged with the lab's number remains, and a `**New sign-up path:**` callout. Our labs haven't been
  run on these pages: say so in the "About the screens" note, hedge console labels the research
  doesn't support, and leave `last_run_pass` out (as Lab 09 does). A lab must not create anything
  that bills by the hour or needs a commitment; state the cost and the worst case honestly.
- **Sims** are static pages with decisions and feedback, as in the model sim; `mode: sim`.
- **No mastery check page** (`NN-check.md`): it comes later. The brief may say one follows.
- No notes to the author in the pages. Put questions, gaps and unverified facts in your final
  message.

## Check before you finish

From `/data/atc/atc-learn-site` (it only reads the guide):

```bash
node scripts/courses.mjs --check --only clf --worktree clf=/data/atc/study/atc-study-aws_certified_cloud_practitioner
```

Fix every finding on your own pages. Findings on other writers' pages of your module are theirs;
a link from your page to a sibling page that isn't written yet is fine until the end, but tell me
which ones.

Write only your own pages, their images and their chart scripts. Don't edit `course.yaml`, the
glossary, `practice/`, other modules or other writers' pages. Don't commit.

## Final message

Files written with word counts; images; facts you couldn't verify or left out; departures from
this brief; links to sibling pages; questions for the owner.
