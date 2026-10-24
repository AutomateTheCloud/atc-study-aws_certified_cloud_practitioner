# Practice questions and flashcards

The practice bundle that goes with this guide: exam-style questions and flashcards in the
[OpenWaymark](https://github.com/AutomateTheCloud/openwaymark) format, for any app that reads
OpenWaymark format 0.2.

- `clf-c02-practice.waymark`: the bundle to open in an app.
- `clf-c02-practice/study.yaml`: the bundle's manifest. **Generated; don't edit it by hand.**
- `clf-c02-practice-review.md`: what the bundle covers and how it was checked.

## Following along with the guide

Every item is tagged, so an app can drill one part of the guide:

| Tag | Selects |
| --- | --- |
| `module-05` | everything from Module 05 |
| `clf-05-03` | everything from one page (the page's `id` in its front matter) |
| `domain-3`, `task-3-6` | questions for one exam domain or task statement |
| `recall`, `understanding`, `application` | what a question asks the learner to do |
| `exam-style` | the questions |
| `concept`, `glossary-term`, `confused-pair`, `abbreviation` | the kinds of flashcard |

Each item's reference names the page and section it was written from.

## How it's made

- `bundle.yaml`: the collection header. Keep its `id`; raise `version` with every release.
- `items/NN-<module>.yaml`: each module's questions and concept cards, written by hand from the
  module's pages. Each item carries `page`, `section`, `task`, `level` and `topics`, which the
  build turns into tags and a reference.
- `../reference/glossary.yaml`: every glossary entry also becomes a term card, an abbreviation
  card (when it has one) and a "how is X different from Y" card (when it has confused pairs).
- `work/`: the writers' brief, each module's blueprint and the check results.

Build and check, from the repository root:

```bash
python3 -I source/practice/build_bundle.py                     # write clf-c02-practice/study.yaml
python3 -I source/practice/build_bundle.py --check             # exit 1 if study.yaml is stale
npx --yes @automatethecloud/openwaymark lint practice/clf-c02-practice
npx --yes @automatethecloud/openwaymark pack practice/clf-c02-practice -o practice/clf-c02-practice.waymark
```

## Adding a module

When a module is written, its items are added in the same piece of work:

1. Write `items/NN-<module>.yaml` from the module's pages, following `work/writer-brief.md`.
2. Build, lint, and check the items with the skill's `check_items.py`.
3. Solve the new questions blind against the pages, and fix every disagreement.
4. Run the new questions through the similarity check (below) and rewrite any that don't pass.
5. Raise the minor `version` in `bundle.yaml`, set `updated`, rebuild and pack.

Keep every existing item and choice `id`: learners' progress is attached to them. An item whose
correct answer now claims something different gets `revision: 2` (or one more than before).

## Originality check

Every question is written from this guide only, by writers who never see exam dumps. Before a
release, all of them, in every wording, go through the similarity checker in the private
dump-analysis repository, which reports PASS, REVIEW or REJECT without showing any dump text:

```bash
python3 -I source/practice/build_bundle.py --similarity practice/work/similarity/candidates.jsonl
python3 -I ../study-aws-ccp-dump-analysis/tools/check_similarity.py \
  --candidates practice/work/similarity/candidates.jsonl --summary
```

A REJECT is rewritten with a new scenario; so is a REVIEW, unless an authorized reviewer clears it.

---

"Practice questions and flashcards" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
