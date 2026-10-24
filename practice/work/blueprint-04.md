# Blueprint: Module 04, Who secures what: shared responsibility and access

Practice items for `practice/items/04-shared-responsibility-and-access.yaml`. Exam tasks 2.1 (shared
responsibility model) and 2.3 (access management). Targets from the request: about 85 questions,
about 17 of them "Select TWO", and about 22 concept cards. Counts below are planned; the final
column pair is updated to the actual counts at the end.

Domain 2 is the exam's heaviest area per task, so most questions are scenarios: "whose job is
this?" for 2.1 and "which identity, policy or credential fits?" for 2.3. Glossary entries for
module 04 already become term, abbreviation and "how is X different from Y" cards, so the concept
cards hold rules, cause and effect, "why" answers, old vs new names and root-only tasks instead.

## Objectives

| Objective | Wording (course plan, section 4) | Level | Taught in (page, section) | Q planned | Cards planned | Q actual | Cards actual |
|---|---|---|---|---|---|---|---|
| 04.01a | Say whether AWS or you does a security task, for EC2, RDS, Lambda or S3, and why | C·Ap | 01 (of the cloud; in the cloud; the line moves; data and access always yours; worked example), 08 (decisions 1 to 4) | 21 (01: 17, 08: 4) | 6 | 21 (01: 17, 08: 4) | 6 |
| 04.02a | Explain what "shared" means, with examples of inherited, shared and customer-specific controls | C·Un | 02 (all sections) | 9 | 2 | 9 | 2 |
| 04.03a | Pick the right kind of identity for a case | C·Ap | 03 (authentication vs authorization; four kinds; admin is not root; worked example) | 10 | 2 | 10 | 1 |
| 04.03b | Recognize the tasks only the root user can do | F·Re | 03 (root-only tasks; Support-plan trap; protecting root; root MFA) | 6 | 4 | 6 | 4 |
| 04.04a | Predict whether a request is allowed or denied | P·An | 04 (statements; identity vs resource; managed vs inline; evaluation; least privilege), 06 (simulator), 07 (Parts A to C), 09 (decisions 1 to 4) | 20 (04: 12, 06: 3, 07: 2, 09: 3) | 6 | 21 (04: 12, 06: 3, 07: 2, 09: 4) | 6 |
| 04.05a | Choose a way to store credentials and a way to manage identities | J·Ap | 05 (passwords and MFA; access keys; secrets stores; federation; Identity Center; four identity services; cross-account roles; why labs use an IAM user), 09 (decision 5) | 19 (05: 17, 09: 2) | 5 | 18 (05: 16, 09: 2) | 5 |
| **Total** | | | | **85** | **25** | **85** | **24** |

## Actual counts (final)

- **Questions:** 85: 66 single answer, 19 "Select TWO". By page: 01: 17, 02: 9, 03: 16, 04: 12,
  05: 16, 06 (Lab 03): 3, 07 (Lab 04): 2, 08 (Sim S3): 4, 09 (Sim S4): 6. By task: 2.1: 30, 2.3: 55.
- **Levels:** recall 16, understanding 36, application 33 (19% / 42% / 39%). Application runs above
  the 30% aim because the request asked for many "whose job is this?" and "which identity or
  credential fits?" scenarios.
- **Select TWO by page:** 01: 5, 02: 2, 03: 3, 04: 2, 05: 4, 08: 1, 09: 2.
- **Cards:** 24 (one fewer than planned: "the expert's two questions for choosing an identity" was
  dropped as too thin; "IAM password policy has no lockout" replaced "which MFA types resist
  phishing", which a question already covers, and "keyless CLI" was left to a question).
- **Correct-answer positions** (single answer): A 16, B 16, C 17, D 17.

## Shape (as planned)

- **Select TWO:** about 17: page 01: 4, 02: 2, 08: 1, 03: 3, 04: 3, 05: 4.
- **Levels:** about 20% recall, 50% understanding, 30% application. Application items are bakery or
  company scenarios with a decision; they carry a hint.
- **Misconceptions refuted** (course plan section 7, module 04): changing the Support plan needs
  root; access keys are the normal way to use the CLI; "AWS Single Sign-On" as a current name;
  "shared" means both sides do the same task; root MFA is optional; `AdministratorAccess` equals
  root; plus the pages' own: "with serverless, AWS handles security", "AWS protects my data because
  it's in AWS", "an allow somewhere means it's allowed".
- **Confused pairs** used as distractors: of vs in; inherited, shared, customer-specific; user,
  group, role; managed vs inline; identity vs resource policy; IAM, Identity Center, Cognito,
  Directory Service; Secrets Manager vs Parameter Store; host vs guest OS; implicit vs explicit
  deny; SCP vs permissions boundary.
- **Volatile facts** (root-only list, root MFA requirement, Simple AD, prices): tested only where
  the objective needs them, dated "(as of 2026-10-23)" in the explanation. No prices, limits or
  counts are tested.

## Cards planned (25)

Lesson 04.01: the layers that never move; EC2's three customer items; S3's three customer items;
what stays the customer's on RDS; what stays the customer's on Lambda; what moving a database from
EC2 to RDS hands to AWS. Lesson 04.02: the "one task or one kind of control" rule; evidence for an
inherited control. Lesson 04.03: the expert's two questions for choosing an identity; why a program
on AWS gets a role; the pattern of root-only tasks; the Support-plan trap; root MFA is required;
two reasons an admin isn't root. Lesson 04.04: explicit deny wins; the three limit-only policy
types; one account vs two accounts; three ways to narrow a policy; AWS's path from managed to
customer managed; how the simulator shows implicit vs explicit deny. Lesson 04.05: the old name of
IAM Identity Center; where AWS credentials for code belong; AKIA vs ASIA; the keyless ways to use
the CLI; which MFA types resist phishing; why the labs use an IAM user.
