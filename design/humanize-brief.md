# Brief: style pass against AI-writing tells

You edit published course pages so they read as written by a careful person. You change
wording only. Every fact, step, number, link and teaching move stays as it is. The owner asked
for this pass over all the content on 2026-10-25, after a pilot on lesson 03.03.

## Read first

1. The tell catalogues of the Slop or Not humanizer, in
   `~/.claude/plugins/cache/slopornot/slopornot/0.3.0/skills/agentic-humanizer/references/`:
   `patterns.md` (33 patterns), `supplemental-ai-tells.md` (S1–S8) and
   `detection-guidance.md` (what *not* to flag). Weigh clusters, not single signals.
2. The voice: `~/.agentic-humanizer/voice-fingerprint.json`. Use only its `fingerprint` fields.
   Don't open the sample it was built from.
3. This repository's `design/conventions.md`, for the page structure you must keep.

## The passes, per page

1. **Pattern surgery.** List the tells the page trips, most frequent first, and fix the top ones
   in place.
2. **Variant and voice.** US English. The fingerprint's register (casual-professional),
   contractions (medium), hedging (low) and function-word habits: plain verbs, "and/but/while",
   a repeated key noun rather than a cycle of synonyms. Keep the second person ("you").
3. **Residual.** Reread; fix the one or two tells still strongest.
4. **Rhythm, lightly.** Vary sentence openings where several in a row start the same way, and
   break a forced group of three. Don't add examples, anecdotes or facts.

Make small targeted edits with the Edit tool. Don't rewrite a page wholesale, and leave a
paragraph alone when it has no real tell: plain, correct prose is the goal, not change for
its own sake. A typical lesson needs a handful to a few dozen edits.

## Never change

- Front matter, headings, fenced blocks (Mermaid, code), tables, images and their alt text.
- Links (text and target), inline code, **bold** text (console labels, terms, callout labels),
  text in double quotes (AWS's words, on-screen messages, quoted beliefs), numbers and dates.
- "**Long description.**" paragraphs: they must match their diagram.
- Questions anywhere: Practice, Check, prequestions, exam-prep sets, task cards. Don't edit a
  question stem or any answer choice. You may smooth an explanation or model answer, but keep
  its claims and keep it within any sentence count its prompt sets ("In two sentences, …").
- Steps in labs and how-tos: keep each step's action, order and "**You should see:**" and
  "If something went wrong" lines; only smooth the prose around them.
- Dated notes ("checked 2026-10-24") and the hedges that make a claim honest about a moving
  target. Don't strengthen or soften any claim.
- Learning-design moves: objectives, prequestions, "Your turn", "Notice" captions, "Next:"
  lines, "Before you start". These are deliberate signposts, not pattern 28.
- Misconception boxes keep three moves: the belief, an explicit refutation sentence, and why
  it's tempting. Their wording was varied on purpose (PR #2); don't make them uniform again.

## House rules that override the catalogue

- Pattern 26 (hyphenated pairs): ignore. Keep the house hyphenation.
- Patterns 15 and 16 (bold, bold-header lists): bold console labels and "**Term:** definition"
  lists are intentional; leave them.
- Pattern 14 (dashes): there should be no em dash in prose; replace any you find. En dashes in
  number ranges and dashes in tables stay.
- Pattern 13 (passive): use active voice when the actor matters ("AWS charges…"), not as a rule.
- Length: each page within ±10% of its words. Glossary `definition` and `not_to_confuse` values
  stay at 40 words or fewer (the glossary builder refuses longer ones): their terse fragments
  are deliberate flashcard compression, not pattern 13.

## Check your work

For every file you change, run from the guide repository root:

```bash
python3 -I source/tools/humanize_guard.py <snapshot copy> <file>
```

The snapshot copies are under
`/tmp/claude-1000/-data-atc-study-study-aws-certified-cloud-practitioner/c75f4e81-04e8-4af2-ac58-0686043c7197/scratchpad/sweep-before/`
(`clf/guide/…`, `clf/reference/glossary.yaml`, `guardrails/primer/…`). Every file must end
with `PASS`. If it fails, fix your edit; never edit the snapshot.

## Scope and conduct

- Edit only the files you were assigned. Don't run git, the builders or the site check.
- If you notice something that looks factually wrong, broken or outdated, don't fix it: report it.

## Report (your final message, under 300 words)

Per file: number of edits, the main patterns fixed, the guard's word change. Then a short list
of anything you flagged and any tell you chose to leave, with the reason.
