# Working rules

Rules for anyone writing or changing this study guide, people and AI
assistants alike. This repository is the publishable guide. It will become
public, so everything committed here must be fit to publish.

## Where the facts come from

- Research lives in the private repo `study-aws-certified_cloud_practitioner`
  (checked out beside this repository). Start from its `docs/01` (exam guide
  blueprint), `docs/03`–`docs/04` (AWS concepts and services), `docs/08`
  (how others teach each topic, and the errors in circulation), `docs/10`
  (exam names vs current names), `docs/09` (visual-asset permissions), and
  `docs/12` (labs). Every fact must trace to an official AWS page; cite it.
- Learning-design evidence lives in the private repo `study-learning-design`.
  Follow it for how lessons, explanations, diagrams, and labs are built.
- **Clean room.** Never read the exam-dump repo (`study-aws-ccp-dump-analysis`)
  or the research repo's `sources/practice-bank/` while writing for this
  repo, and never copy from them. The guide must be provably written without
  them.

## Writing

- **Original words only.** Never copy or closely paraphrase AWS
  documentation, whitepapers, or diagrams: AWS docs are CC BY-SA 4.0, and
  share-alike conflicts with this guide's CC BY-NC 4.0. Never copy
  third-party courses, notes, or cheat sheets either. Cite AWS for facts and
  explain in our own words.
- Don't reproduce the exam guide's text. Refer to domains and task
  statements by number and a short title, and link to the guide.
- Teach current reality. Where the exam uses an old or retiring name, give
  the exam's name and the current one on first mention, and say what changed
  (see the research repo's `docs/10`). Date-stamp facts that change often:
  prices, plan names, Free Tier terms, service availability.
- American English. "Automate the Cloud" in prose, "Automate the Cloud Inc."
  in legal text.

## Labs

- Labs run in the learner's own AWS account. Before the first lab, the guide
  sends learners through the guardrails primer
  (`atc-study-aws_account_guardrails`); don't repeat its steps here, link to
  them.
- Every lab says what it creates, what it costs, and how to delete it, and
  starts with the liability notice. Where a lab would cost money or isn't
  possible on the Free plan, teach the topic anyway and simulate it.

## AWS trademarks

- AWS names in plain text only, to make true factual statements. No AWS
  logos, no certification badges, no AWS trade dress (colors, fonts, look and
  feel). Our branding is always at least as prominent as any AWS name.
- Never state or imply that AWS made, endorsed, or sponsors the guide. The
  trademark notice in `README.md` appears in the front matter of every
  edition and in the website footer.

## Images

- Diagrams we draw are CC BY-NC. Icons and other third-party assets keep
  their own licenses and are credited where used.
- AWS service icons come only from the AWS Icons for PlantUML set (CC BY-ND
  2.0): unmodified (no recoloring, cropping, or redrawing), credited, and
  marked as outside our license. Generic icons come from openly licensed
  sets (MIT, ISC, Apache). Don't use the official AWS Architecture Icons
  package. Never adapt a diagram from AWS documentation; draw our own. See the
  research repo's `docs/09`.
- Screenshots are taken in our own AWS accounts and redacted (account IDs,
  ARNs, emails, and anything else in the `docs/09` redaction checklist).
  They are AWS material used as limited fair use, marked as outside our
  licenses. Use them sparingly, only where they teach something.

## Licensing

- Follow `LICENSING-PLAYBOOK.md` in the `atc-brand_kit` repo. Fetch a fresh
  copy before any licensing change.
- Every lesson and article ends with the attribution line from the playbook,
  section 7.
- Code examples meant to be Apache-2.0 are marked so; scripts and
  infrastructure files carry the two-line SPDX header.

## Commits

- Commit with `git commit -s`, using `55336416+david-singer@users.noreply.github.com`, so no personal address is published.
  Never mention an AI tool in commits or pull requests.
