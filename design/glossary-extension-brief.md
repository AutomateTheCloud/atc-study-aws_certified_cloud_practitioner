# Brief: add a module's terms to the glossary

The course glossary's source is `reference/glossary.yaml`; `source/glossary/build_glossary.py` checks
it and builds the learner page `guide/99-reference/01-glossary.md`, and the practice bundle turns
every entry into flashcards. Paths are relative to
`/data/atc/study/atc-study-aws_certified_cloud_practitioner`. The message that sent you here names
the modules to add.

## Read first

- `CLAUDE.md`, `design/conventions.md` (original words; exam names vs current names).
- The docstring of `source/glossary/build_glossary.py`: every field and every rule it enforces.
- Every page of your modules: their `terms_introduced`, their "Key terms" sections, and where each
  term is defined in the text.
- `reference/glossary.yaml` as it stands (473 entries for Modules 00 and 02–07): to merge, not
  duplicate.
- `/data/atc/study/study-aws-certified_cloud_practitioner/docs/10-names-and-status.md` for exam
  names.

Clean room: never open `/data/atc/study/study-aws-ccp-dump-analysis/` or `sources/practice-bank/`.
No web.

## Rules

- Add a term only if a page of your modules defines or teaches it. Base the definition on the
  page's own words, tightened into one to three plain sentences that stand alone: **at most 40
  words, counted as runs of letters and digits** (the build checks this). No prices or counts that
  go out of date; if a definition needs one, say "see the lesson".
- A term already in the glossary gets no second entry. If your module is now its main lesson, move
  `taught_in` (and `module`) and put the old page in `also_in`; otherwise add your page to
  `also_in`. Rewrite the definition only if your module teaches it more fully, and keep it true
  to both pages.
- `confused_with` lists only terms with entries; `not_to_confuse` (one sentence, at most 40 words)
  is present whenever `confused_with` is. Use your modules' confused pairs from
  `design/course-plan.md` section 7.
- `exam_name` only when the CLF-C02 exam guide's name differs from today's.
- A term listed in `terms_introduced` but never defined in the page text gets no entry; list it in
  your final message.
- Keep the file sorted, wrapped at 100 characters, and write it atomically (other agents may be
  reading it).

Build and check until clean:

```bash
python3 -I source/glossary/build_glossary.py
python3 -I source/glossary/build_glossary.py --check
```

Touch only `reference/glossary.yaml` and the built page. Don't commit.

## Final message

Entries added per module; existing entries changed (which, and why); terms left out and why;
definitions on the pages that disagreed with each other.
