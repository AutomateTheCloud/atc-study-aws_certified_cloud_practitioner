# Brief: fix one module's practice items after review

Your module's items were written, then checked two ways. Now fix what the checks found. Read
`practice/work/writer-brief.md` first: every rule there still applies (clean room, variants on
every choice, the item format, the boundaries). Paths are relative to
`/data/atc/study/atc-study-aws_certified_cloud_practitioner`.

## Inputs

- Your items file: `practice/items/NN-*.yaml`. Edit only this file.
- **Blind-solve notes:** `<scratchpad>/solve-NN/notes.md`, where `<scratchpad>` is
  `/tmp/claude-1000/-data-atc-study-study-aws-certified-cloud-practitioner/90d7019c-4727-40dc-b5e8-2d3498ef2995/scratchpad`.
  A fresh solver answered every question from the guide pages without the key (all matched), and
  flagged GIVEAWAY, VARIANT, TWO-DEFENSIBLE, UNSUPPORTED and WRONG-IN-REALITY problems, and cards
  that are only partly supported. Questions are numbered there (Q1, Q2...); `<scratchpad>/blind-keys/NN.json`
  maps each number to its item `id`.
- **Similarity results:** `practice/work/similarity/flagged.json` lists, by item id, the questions
  (and wordings, as `id#v1`) that the dump-similarity checker scored REVIEW or REJECT, with the
  reasons and scores. It contains no dump text, and you must never try to see any: never pass
  `--show-text` to the checker, and never open `/data/atc/study/study-aws-ccp-dump-analysis/`
  except to run its checker as shown below.

## What to fix

1. **Every flagged question in `flagged.json` for your module:** rewrite it with a new scenario,
   not just new wording. What triggers each reason:
   - `stem_token_jaccard` or `stem_char5_jaccard`: the stem's words overlap a known question.
     Write a different situation, with different nouns and a different sentence shape.
   - `combined`: the stem and choices together overlap. Change the scenario and the set of choices.
   - `scenario(same services + same correct answer)`: a known question offers nearly the same set
     of services and keys the same one. Keep testing the same idea, but change the choice set
     (different distractor services drawn from the module's confused pairs) and the situation.
   A rewritten question that tests the same objective keeps its `id`; if the correct choice now
   claims something different, add `revision: 2`. If an item can't be made distinct without
   becoming a worse question, replace it with a new question on the same objective and a new `id`.
2. **Every solver flag and every partly supported card:** fix the wording, the giveaway, the
   variant that drifts or stands out, the reference that points at the wrong section (cite the
   heading that actually supports the back), or the claim that overreaches.
3. **WRONG-IN-REALITY flags and any page claim the notes call a simplification:** make the item
   hold on real AWS as well as in the guide. Don't key an answer that depends on a doubtful claim;
   hedge it ("by default", "the usual zonal NAT gateway") or test something else. Don't edit guide
   pages; list the doubtful page claims in your final message.

## Check

From the repository root, until clean:

```bash
python3 -I source/practice/build_bundle.py --only NN --out practice/work/tmp-NN --similarity practice/work/similarity/NN.jsonl
npx --yes @automatethecloud/openwaymark lint practice/work/tmp-NN
python3 /home/dsinger/.claude/skills/openwaymark-study-bundles/scripts/check_items.py practice/work/tmp-NN/study.yaml
cd /data/atc/study/study-aws-ccp-dump-analysis && python3 -I tools/check_similarity.py --candidates /data/atc/study/atc-study-aws_certified_cloud_practitioner/practice/work/similarity/NN.jsonl --summary
```

Every question of your module, in every wording, must come back PASS. Then have a **fresh** helper
agent blind-solve just the items you changed:

```bash
python3 /home/dsinger/.claude/skills/openwaymark-study-bundles/scripts/blind_solve.py make practice/work/tmp-NN/study.yaml --only <id>,<id> -o <scratchpad>/fix-NN/blind
```

Move `blind-key.json` out of that folder before the helper starts, give the helper only
`blind-questions.md`, `blind-variants.md`, `blind-cards.md` and the module's guide pages, with the
flags from `<scratchpad>/solver-brief.md`, then score its answers with `blind_solve.py score`. Fix
anything it flags, and check those items again with another fresh helper.

Keep your scratch files in `<scratchpad>/fix-NN/` only; other modules' fixers are working at the
same time.

## Final message

The items you rewrote for similarity (old verdict, new verdict); the solver flags you fixed; the
re-check score; the final lint, item-check and similarity counts; the page claims that looked
doubtful or wrong.
