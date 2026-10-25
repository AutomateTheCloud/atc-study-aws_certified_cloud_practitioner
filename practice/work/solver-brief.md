# Brief: blind-solve one module's practice items

You check practice questions and flashcards written from one module of a study guide for the
AWS Certified Cloud Practitioner exam (CLF-C02). You don't see the answer key. Your job is to find
every item where the intended answer isn't the only defensible one, given the guide.

## Inputs (and only these)

- Your folder, named in the message that sent you here, with:
  - `blind-questions.md`: numbered questions (Q1, Q2, ...) with lettered choices;
  - `blind-variants.md`: every wording of each choice (the app shows one wording per choice, picked
    at random);
  - `blind-cards.md`: numbered flashcards with their cited reference.
- The module's guide pages: `/data/atc/study/atc-study-aws_certified_cloud_practitioner/guide/NN-*/`
  (all of them), and if needed the glossary page `guide/99-reference/01-glossary.md`.

Don't open anything else: not `practice/` in the guide repository (it holds the answer key), not
other folders in the scratchpad (`blind-keys/`, other modules' folders), not the web. Don't open
`/data/atc/study/study-aws-ccp-dump-analysis/` or `sources/practice-bank/`.

## What to do

1. Read the module's pages.
2. Answer every question from the guide, as a careful learner who studied those pages would.
   Decide your answer **before** you look at anything else. For "Select TWO", give exactly two.
   Write `answers.json` in your folder: `{"Q1": ["B"], "Q2": ["A", "D"], ...}`.
3. For each question, write in `notes.md`: the passage (page and heading) that supports your answer,
   and a flag when any of these apply:
   - **TWO-DEFENSIBLE:** another choice could also be defended, from the guide or from how AWS
     really works;
   - **UNSUPPORTED:** the guide doesn't teach what's needed to answer;
   - **WRONG-IN-REALITY:** the answer you're confident the item wants is wrong or out of date on
     real AWS, as far as you know (say what you believe and how sure you are);
   - **GIVEAWAY:** the right answer can be spotted without the knowledge (length, echoed words,
     absolute words only on distractors);
   - **VARIANT:** in `blind-variants.md`, a wording of a choice that makes a different claim from
     the choice's other wordings, or that stands out next to the other choices. Name the choice
     and the wording.
   Keep unflagged notes to one line each.
4. For each card in `blind-cards.md`, give a verdict in `notes.md` (supported, partly supported,
   unsupported, wrong reference) against the cited page and section, with a reason when it's not
   "supported".
5. Don't edit any file except `answers.json` and `notes.md` in your folder.

## Final message

Number of questions answered; the list of flagged questions with their flag and a one-line reason;
the card verdict totals and the non-supported cards. Don't include your answers in the message:
they're in `answers.json`.
