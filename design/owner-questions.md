# Questions and actions for the owner

## Still open

- **Next-day checks (2026-10-26, need sign-in):** Lab 16 steps 9–11 (Cost Explorer group by tag
  `lab`), Lab 19 Part E (credits were $160.00 at 2026-10-25 11:27), and whether the SNS
  subscription for the deleted `clf-lab11-orders-failing` topic has cleared. Then add
  `last_run_pass` to Labs 16 and 19.
- **Editorial calendar:** WorkSpaces Secure Browser closes 2026-10-29: after that, change "closes" to
  "closed since" in 10-00, 10-03, its two charts, S12 and the 00-04 names table. Snowball support
  ends 2026-12-31; legacy Support plans end 2027-01-01 (Module 12's dated box); Amazon Q Developer
  IDE plugins and paid subscriptions end 2027-04-30.
- **Screenshots:** 65 approved captures of 2026-10-25 are in `_captures/aws-test-account/redacted/`;
  none is in the guide yet.

## Decided by the owner on 2026-10-25 (applied)

1. The `me-central-1` (UAE) outage appears as one dated, neutral example in 03.03, quoting AWS.
2. Lab 12 keeps letting learners accept a single SOC report's confidentiality terms (optional, with
   the cancel path).
3. 10.02 keeps the dated note that Comprehend showed an upgrade page on the Free plan.
4. 09.05 keeps AWS's wording ("designate the account as HIPAA or SEC compliant") and names the BAA.
5. AWS IQ is gone from the lessons; it stays in the 00-04 table of retired names and the names
   reference.
6. 12.04 keeps its one-line mapping of the old Consulting/Technology Partner names.
7. The "older material" box for Cloud9, CodeDeploy and OpsWorks in 08.03/08.04 stays.
8. Length limits raised to match the written modules (brief and conventions updated).
9. The capstone recommends Basic with a recorded accepted risk, and Business Support+ once the site
   carries much of the bakery's revenue.
10. Module 13's acquisition story stays; earlier mentions are compatible.
11. Earlier writer decisions stay: Module 12 written now; 10.01's short Kinesis Data Analytics
    refutation; CloudShell taught in 08.01 but flagged as off-exam; one objective code for 08.04;
    labelled made-up chart figures; the bundle's AI-assistance disclosure; labs tag `guide=clf`.

## Settled by the live runs of 2026-10-24/25

- All labs run; pages corrected (see `design/handoff.md` and the research repo's `docs/16`).
- Athena, Polly and Cost allocation tags work on the Free plan (`free_plan: true` on Labs 13, 14, 16).
- A Free plan account can't buy a paid Support plan (12.01 now says so, dated).
- Lab 18's worst-missing-practice rule held at all three levels; practice item
  `q14-risk-from-worst-missing-practice` stands.
- Credit expiry (B9): the test account's credits expire 12 months after sign-up, while the plan ends
  at 6, as 11.01 teaches.
- The m7i Dedicated Host price ($10.644 an hour) is in AWS's price list; it and 13.04's Windows and
  SQL Server prices are now in the research repo's price summary.
- Task cards' console labels confirmed or corrected; the six similar q05 items were rewritten blind
  on 2026-10-24.

## Closed in the final consistency pass (2026-10-25)

- Trusted Advisor check count: no number in the guide, because AWS's pages disagree (owner's
  2026-10-23 principle).
- Glossary: AWS RAM entry present; "Control Tower control" already renamed.
- Story: S4 heading now says "ten shop accounts", matching its text and 10.01; S16's wholesale
  portal already matches 13.02 ("refactor, probably after a rehost").
- Capstone finding 6 also names OPS05-BP05 Perform patch management.
- Links: labs' cleanup steps point to the matching task cards; the "Next" lines already link the
  mastery checks; Module 08 pages link Module 09 where they name it.
- Reference generator: no data notes left.
- Fact checks of 04.03, 05.03/S5, 05.05, 08.02, 09.04, 11.03 and 11.04: see the commit that follows
  this file's update.

## Content notes kept for the record

- 13.04's three-year business case and 08.02's effort chart use made-up figures, labelled as such.
- 11.01's bill leaves out RDS and public IPv4 (a note says so); S11 uses an illustrative 30 TB.
- 09.04: whether Business Support+ qualifies for the Shield Response Team isn't on AWS's pages; the
  lesson says "check the page" in a dated note.
- Glossary ownership rule: the first page that defines a term owns it; later pages go in `also_in`.
- "Up to 75%" (RIs) is treated as older AWS wording; the RI pricing page says 72%.
