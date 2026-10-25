# Questions and actions for the owner, collected for the end (owner reviews everything at the end)

## Needs the owner
- Similarity REVIEW clearance: six q05 storage-class questions (see practice/clf-c02-practice-review.md).
- Live lab runs (need sign-in): Labs 02, 05, 06, 07, 08, 09, 10, 11, 13, 14 (+ 12 and later labs).
  Lab 13/14: confirm Athena and Polly speech work on the Free plan and the new sign-up path.
  Lab 10/11: CloudShell `edit`, validate-template behavior, alarm wizard tags, email timing.
  Question from writer: capture screenshots of CloudFormation Events tab and alarm History on the run?

## Decisions I made (owner may revisit)
- Module 12 written now, not after 2027-01-01 (owner: finish all material first).
- 10.01 keeps a short refutation of Kinesis Data Analytics as an answer (course plan says refute;
  docs/10 says don't mention). Wording follows AWS: deletion of applications began 2026-01-27.
- CloudShell: out of the exam's scope per the exam guide, but taught in 08.01 as the labs' CLI tool,
  flagged as not exam content.
- 08.04: one objective code 08.04a (messaging + build/release tools).
- 08.02's effort chart uses illustrative made-up figures, labelled as such.
- Bundle description keeps the AI-assistance disclosure (skill requirement).
- Labs tag guide=clf (B11).

## Content notes for review
- Brief length: 10-00 is ~940 words with its map (limit 800).
- Lessons run slightly over 3,500 words by full count (same as models).
- Lab 12 (Artifact): many reports require accepting confidentiality terms before download; the lab
  forbids the Agreements page but allows report terms (not a Free plan upgrade trigger). Owner to
  confirm, and on the live run check whether any report downloads without terms.
- Labs and sims run 10–30% over the brief's word limits (same as the earlier models).
- S11 billing example uses an illustrative 30 TB per account.
- 10.02 tells learners Comprehend showed an upgrade page on the Free plan in our test account (Polly
  opened). OK to say?
- Editorial calendar: Secure Browser closes 2026-10-29 (10.03 says "closes … on"); switch to past
  tense after. Also Q Developer IDE plugins end 2027-04-30.
- 08.04 and 08.03: Cloud9/CodeDeploy/OpsWorks in an "older material" box (A6 vs docs/10 "don't mention").
- Bedrock and AppSync mentioned only as not-on-the-exam names; Forecast/Fraud Detector kept as dated distractors.
- 09.05: Free plan warning about Artifact agreements is phrased around "designating the account
  HIPAA/SEC compliant" (AWS's upgrade trigger) rather than naming the BAA outright. Keep?
- 09.04: whether Business Support+ qualifies for the Shield Response Team isn't on AWS's pages;
  lesson says "check the page" in a dated note (no contact with AWS, per owner's preference).
- Glossary ownership: `finding`/`CVE` defined in 09.03 (S9 also lists them); SCP owned by S4, 09.05
  deepens it. Rule applied: the first page that defines a term owns it; later pages go in also_in.
- 08 and 09 warm-ups name each other's modules by title only (written in parallel); links could be
  added later.
- Labs 13 and 14: `free_plan` left out until a live run confirms Athena/Polly on the Free plan.
- Editorial calendar: after 2026-10-29 change Secure Browser to "closed since" in 10-00, 10-03, its
  two charts and S12.
- Length: Module 08–10 lessons ~4,000–5,000 words by full count (models similar); not cut.
- Q Developer: paid subscriptions and IDE plugins end 2027-04-30 (research docs/10 updated, 875bbed).
- Lab 17 includes a read-only stop at the Support Plans console (next to the upgrade buttons). Keep?
- Lab 17 reuses approved screenshots sec-35 and sec-35b (Trusted Advisor) as images/12-05-*.png.
- Bakery's monthly AWS bill = $1,200 in Module 12 (Module 11 told to align).
- Story continuity: S4/S11 say the bakery grew into a chain; Module 13 (course plan) says a chain buys
  the bakery. Module 13 review told to reconcile with the smallest change (decision: keep Module 13's
  acquisition, make earlier mentions compatible). Owner may prefer otherwise.
- S16 wholesale portal: "refactor" vs 13.02's "rehost now, then refactor": review to align.
- S17 rates relocate/BYOL without dollar figures (no Dedicated Host/Windows prices in our summary).
- 12.02 names the three AWS pages that disagree on Trusted Advisor's check count without the numbers
  (B3). Show the numbers labeled as conflicting?
- Unknown: whether a Free plan account can buy a paid Support plan (not claimed either way).
- AWS IQ: docs/10 says don't mention; review told to keep at most one dated line (or remove).
- 12.04 maps old "Consulting/Technology Partner" names to today's paths (verify; owner may prefer
  dropping the old names).
- Trust & Safety email address left out of pages (PRIV-2); pages name the abuse form instead.
- Free plan credit expiry: AWS's FAQ says 6 months in two answers and 12 in two others; 11.01 teaches
  "12 months, AWS's pages disagree" (open question B9). Owner to settle.
- Bakery bill: ~$210/month in Module 11; Module 12's $1,200 framed as a later, grown bill (review).
- 11.01's bill leaves out RDS (no RDS price in our summaries) and public IPv4 addresses.
- 13.04 prices for Windows, SQL Server and Dedicated Hosts taken from the full EC2 price list file
  (2026-10-23), not the summary; summary rows not yet added to the research repo.
- 13.04's three-year business case uses made-up numbers (like Module 02).
- Lab 16 sets free_plan: true without a live run; tells learners to leave guide/lab tags active.
- 11.04: AWS's custom billing views (newer) left out; cost categories and account tags taught as not
  on the exam.
- 11.04: RI/SP sharing "on by default" inferred from AWS wording (review to state only AWS's words).
- 12.01/S15 payments firm: rewritten so Unified Operations is the only fit on included features
  (Enterprise + paid Incident Detection and Response add-on was cheaper, which made the answer ambiguous).
- Module 12 shows the bakery's bill as ~$210 now and $1,200 a year later (both labeled made up).
- Trusted Advisor: AWS pages say 482, 500+ and 465+ checks; no count in the guide (B3).
- Glossary: rename 'control (AWS Control Tower)' (same card prompt as 'AWS Control Tower') after Module 12 glossary.
- Word limits: Modules 08–13 lessons run ~4,000–4,700 prose words, labs ~2,300–2,900, sims ~1,500–2,000
  (models 07.02 similar). Change the limits in the brief, or trim?
- Running case: S4 says "twelve shop accounts and thirty staff"; 10.01 says "ten shops". Small
  inconsistency for a final consistency pass.
- 13.04: m7i Dedicated Host $10.644/h not shown on AWS's pages (= 1.1 × m7i.48xlarge); kept, dated.
- Free Tier "two clocks": 11.01 now = calendar (6 months) and credit balance; 00-04 reworded to match.
  Primer page 01 (released) says credits expire 12 months per our Credits page and the 6-month date
  comes first: compatible, left unchanged. Course plan's 11.01 row still says "credits 12".
- "Up to 75%" (RIs) treated as older AWS wording; the RI pricing page says 72%.
- 11.01's bill has no public IPv4 line (note added instead of changing every figure).
- 08.01 corrected: CloudTrail records management events by default (data events opt-in); CloudFormation updates compare templates, not live resources (drift detection finds hand changes).
- Lab 18: course plan §10 lists it among labs needing a new-sign-up-path simulation; AWS lists the WA Tool in that path's Free Tier, so the lab's callout says it should work there (unrun). Objective codes 14.02a/14.03a created for Labs 18/19.
- Coverage gap: AWS RAM (Resource Access Manager) is the one in-scope service the guide doesn't teach;
  Systems Manager only via Parameter Store. To add (likely 09.05 next to Organizations).
- Data notes from the reference generator: SSO rename date not on 04.05; Simple AD date format on 04.05;
  Snowmobile/CodeStar dates not on 00-04; AWS IQ two dates (05-28 vs 05-20).
- Capstone model answer recommends Business Support+ ($29 fee > half of a ~$50 bill), with Basic acceptable as a recorded accepted risk. Stance OK?
- Capstone 14.01 is ~5,400 prose words (carries rubric + model answer). Cut or allow?
- Capstone finding 6 uses SEC06-BP01 (vulnerability management); OPS05-BP05 (patch management) also fits.
- Course plan now has Module 14's objective rows (14.01a–14.03a), copied from the brief.
- AWS RAM now taught in 09.05 (new section before the SCP heading); glossary entry still to add.
- Task cards (98-how-to, 9 cards): use the short "Your account, your responsibility." pointer, not the
  full liability notice. Unconfirmed console labels: include in the live lab run session.
- Labs' cleanup/recovery steps could link to the task cards (final consistency pass).
- Lesson 08.02 says the stack creator needs permissions for every resource (CloudFormation service roles
  avoid that); 09.04 doesn't say Shield Advanced's automatic L7 mitigation covers CloudFront/ALB only
  (unverified); 11.03 has "18 months" in a heading anchor (volatile).
- To verify in the final fact pass: 04.03 "only Organizations can restrict a member account's root user"
  (a bucket policy's explicit deny also blocks root); 05.05 read replica limits for Oracle/SQL Server;
  05.05 "standby serves no reads" vs Multi-AZ DB clusters; align S5 vs 05.03 minimum-duration wording.
- Sims' and labs' closing "Next: mastery check" lines to link the check pages (final pass).
- ~~q14-risk-from-worst-missing-practice depends on Lab 18's unconfirmed risk rule: confirm on the live run or cut.~~ Resolved 2026-10-25: the live run confirmed the rule at all three levels (a missing High gave high risk; missing Mediums only, medium; a missing Low only, no risk). The item stands.

- Module 03 (2026-10-25 live run): AWS's status page shows a long-running "Operational issue - Multiple services (UAE)" in
  `me-central-1` (Region damaged; one AZ unrecoverable per AWS's Sep 15 update). Use it as a real Region-isolation
  example in lesson 03.03 or Lab 02, or leave it out as too sensitive?
