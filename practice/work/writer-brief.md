# Brief: practice questions and concept cards for one module

You write one module's share of the practice bundle that goes with Automate the Cloud's study guide
for the AWS Certified Cloud Practitioner (CLF-C02) exam. The guide repository is
`/data/atc/study/atc-study-aws_certified_cloud_practitioner` (below, paths are relative to it). The
bundle is in the OpenWaymark format, draft 0.2. Your module number, page list and targets are in
the message that sent you here.

## Read first

1. The skill's references, all of them, before writing any item:
   - `/home/dsinger/.claude/skills/openwaymark-study-bundles/references/study-design.md`
   - `/home/dsinger/.claude/skills/openwaymark-study-bundles/references/authoring-rules.md`
2. `CLAUDE.md` and `design/conventions.md` (original words only; exam names vs current names).
3. `design/course-plan.md`: your module's rows in section 4 (lessons and objectives such as
   `05.03a`, with knowledge type and thinking level) and section 7 (misconceptions and confused
   pairs for your module).
4. Every page of your module in `guide/NN-*/`: briefs, lessons, labs, simulations. Read each whole.
5. Your module's entries in `reference/glossary.yaml` (`module: "NN"`). Every glossary entry already
   becomes a term card, an abbreviation card and a "how is X different from Y" card automatically,
   so don't write cards that restate a glossary definition.
6. `source/practice/build_bundle.py`'s docstring: the build fields described below.

**Clean room.** Never open `/data/atc/study/study-aws-ccp-dump-analysis/`, anything under
`sources/practice-bank/`, or the research repository `/data/atc/study/study-aws-certified_cloud_practitioner`.
Don't browse the web. Write every question fresh from the guide. Don't reproduce questions you
may remember from real exams, dumps or commercial practice tests: every question is checked against
a dump bank later, and near-matches are rejected. Don't reuse the guide's own "Your turn",
"Check" or end-of-lesson retrieval items word for word either; learners will have seen them.

## What to write

**File:** `practice/items/NN-<module-folder-slug>.yaml` (for example
`practice/items/05-storing-data.yaml`), with two top-level lists, `questions` and `flashcards`.
Write it lesson by lesson (append a lesson's items, validate, go on), not all at once.

**Blueprint first:** `practice/work/blueprint-NN.md`: a table of every objective of your module
(code, wording, level from the course plan), the page and section that teaches it, and the number
of questions and cards you plan for it. Central objectives get 3 to 6 questions; every objective
gets at least 1. Then write to the blueprint, and update its counts to the actual ones at the end.

### Questions: the way the exam asks

The CLF-C02 exam has two kinds of question, and the bundle should feel like it:

- **Multiple choice:** one correct answer from four choices. `selection: single`.
- **Multiple response:** two correct answers from five choices, and the stem ends with
  "(Select TWO.)". `selection: multiple`, `selection_count: 2`. About a fifth of your questions.

Stems are mostly short business scenarios: "A company wants to... Which AWS service...?", "A
startup's website traffic doubles every December... What should it use to...?", "Which statement
describes...?", "Which of these is the customer's responsibility under the AWS shared
responsibility model?". Aim for roughly 20% recall, 50% understanding and 30% application;
application questions describe a situation and ask for a decision.

- Test the guide's ideas at the guide's level. Every correct answer must be supported by the page
  and section you cite; every distractor must be definitely wrong, in the guide and in the real
  world. When in doubt, cut the item.
- Distractors come from real confusions: the module's confused pairs and misconceptions (course
  plan section 7, the pages' "Misconception" callouts), neighbouring services, reversals.
- Don't test volatile facts: prices, free-tier amounts, counts of Regions or services, limits. If
  an item can't avoid a dated fact, say "(as of 2026-10-23)" in the explanation.
- Avoid negative stems; if one is unavoidable, write NOT in capitals, and keep them rare. Never
  "all of the above" or "none of the above".
- Keep choices parallel: same form, similar length. Vary which position is correct.
- Use the names the exam guide uses when they differ from today's names, and teach the current
  name in the explanation (conventions.md has the rule).

**Answer variants on every choice ("mutations").** The owner wants every answer, right and wrong,
in several wordings, so learners can't memorize how an answer looks. Give every choice `text` plus
two `variants` (three wordings in all). Follow section 9 of study-design.md exactly: same claim,
same form and length, vary distractors as much as the correct answer. For service names, the
wordings are the name's forms, for example `Amazon S3` / `Amazon Simple Storage Service (Amazon S3)`
/ `S3`; for numbers, equivalent forms (`Three`, `3`). Write each choice's `explanation` so it fits
every wording.

**Every question has** an `explanation` (two to four sentences that teach the idea, not just name
the answer), a per-choice `explanation` on most distractors (why it's tempting, why it's wrong),
and, for application questions, a `hint` that points at the concept without naming the answer.

### Concept flashcards

Cards for the module's major ideas that a glossary definition doesn't hold: rules ("an explicit
deny always wins"), cause and effect, "why" cards ("Why does a NAT gateway sit in a public
subnet?"), how to choose between options, old vs new names, root-only tasks. One fact per card;
the back is 40 words or fewer and lists at most three things.

### Item format

Each item has the OpenWaymark fields plus **build fields** that the build turns into tags and a
reference, then removes:

```yaml
questions:
  - id: q05-reports-read-once-a-month          # q + module + content slug; never positional
    page: guide/05-storing-data/03-storage-classes-and-lifecycle.md
    section: "Infrequent Access: cheaper storage, a fee per read"   # a heading on that page, exactly
    task: "3.6"                                # the exam task statement it serves
    level: application                         # recall | understanding | application
    topics: [s3-storage-classes]               # optional, lowercase-with-hyphens
    type: multiple_choice
    selection: single
    prompt:
      text: |
        A company keeps monthly reports in Amazon S3. ...
    choices:
      - id: standard-ia
        text: S3 Standard-IA
        variants:
          - text: S3 Standard-Infrequent Access
          - text: The Standard-IA storage class
        explanation:
          text: ...
      # three more choices, each with two variants
    correct_answers: [standard-ia]
    hint:
      text: ...
    explanation:
      text: ...
flashcards:
  - id: c05-ia-retrieval-fee
    page: guide/05-storing-data/03-storage-classes-and-lifecycle.md
    section: "..."
    level: recall
    topics: [s3-storage-classes]
    front:
      text: ...
    back:
      text: ...
```

- IDs: `q` or `c`, the two-digit module, then a content slug; at most 64 characters, `a-z0-9-`.
  Choice IDs name the choice (`standard-ia`, `one-zone-ia`).
- `task` is required on questions and optional on cards; use the page's `tasks` front matter.
- Quote text containing `: `; use `text: |` for anything longer than a phrase. Markdown only, no
  HTML, no headings, no URLs.

## Check your work

From the repository root, until all three are clean:

```bash
python3 -I source/practice/build_bundle.py --only NN --out practice/work/tmp-NN
npx --yes @automatethecloud/openwaymark lint practice/work/tmp-NN
python3 /home/dsinger/.claude/skills/openwaymark-study-bundles/scripts/check_items.py practice/work/tmp-NN/study.yaml
```

The build lists problems (missing fields, a section that isn't a heading on the page, choices
without variants). Aim for 0 lint errors and 0 warnings. In `check_items.py`'s output, fix every
warning on your own `q…` and `c…` items (answer-position bias, a correct choice that is longest,
missing explanations, duplicates). Ignore warnings about `term-`, `abbr-` and `diff-` cards: they
come from the glossary and are handled separately.

Then run the dump-similarity check on your module (it shows no dump text; never pass
`--show-text`, and never open anything else in that repository):

```bash
python3 -I source/practice/build_bundle.py --only NN --out practice/work/tmp-NN --similarity practice/work/similarity/NN.jsonl
cd /data/atc/study/study-aws-ccp-dump-analysis && python3 -I tools/check_similarity.py --candidates /data/atc/study/atc-study-aws_certified_cloud_practitioner/practice/work/similarity/NN.jsonl --summary
```

Rewrite any REJECT or REVIEW question with a new scenario and, where the reason is "same services +
same correct answer", a different choice set. If a REVIEW can't be cleared without making the
question worse, keep it and list it in your final message for the owner's review.

Then read your file once as a learner: repeated items, two questions testing one fact the same
way, any question with two defensible answers.

## Boundaries

- Keep scratch files only in your own folder,
  `/tmp/claude-1000/-data-atc-study-study-aws-certified-cloud-practitioner/90d7019c-4727-40dc-b5e8-2d3498ef2995/scratchpad/items-NN/`:
  other writers share the scratchpad, and generic names collide.
- Use the official service names in every wording (short or long form). Never drop or change a
  name to make a question look less like another one: the similarity check must judge the real
  question.
- Write only your items file, your blueprint, and `practice/work/tmp-NN/`. Other writers are working
  on other modules at the same time; don't touch their files, the glossary, the builder or any
  guide page. If a page seems wrong, say so in your final message instead of changing it.
- Don't commit.

## Final message

Counts: questions (single and multiple), cards; questions per page and per level; the check
results; any objective you couldn't cover and why; the items you're least sure of; anything on the
guide's pages that looked wrong or unclear.
