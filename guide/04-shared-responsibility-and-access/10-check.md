---
type: check
id: clf-04-10
title: "Module 04 mastery check"
tasks: ["2.1", "2.3"]
objectives: ["04.01a", "04.02a", "04.03a", "04.03b", "04.04a", "04.05a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 04 lessons; about 30 minutes for each check; works on a phone"
prerequisites: [clf-04-01, clf-04-02, clf-04-03, clf-04-04, clf-04-05]
pillars: [security]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html"
  - "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"
  - "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html"
  - "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
  - "https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html"
  - "https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html"
  - "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html"
---

# Module 04 mastery check: split the security work, and predict who gets in

This check shows whether you can do what Module 04 set out to teach: say who does a security task on a given service, explain what "shared" means, pick an identity, recognize root-only tasks, predict whether a request is allowed, and choose how people, programs and secrets get into AWS.

**For:** an adult studying alone, possibly new to IT, who has finished lessons [04.01](01-security-of-vs-in-the-cloud.md) to [04.05](05-credentials-and-federation.md). **Time:** about 30 minutes for each check. No AWS account needed.

## How to use this check

Take **Check A** closed-book: no lessons, notes or searching. Answer all 15 questions, then open the answers. A "(Select TWO.)" question counts as right only if you chose both correct options.

- **12 or more right (80%):** you have mastered the module. Go on to the [enrichment tasks](#enrichment-for-learners-who-pass), then to Module 05.
- **Fewer than 12:** for each question you missed, use the [correction map](#correction-map) to reread the named section and redo the linked practice. Then take **Check B**, a parallel retest: new questions on the same objectives. Don't retake Check A; you have seen its answers.

## Check A

### Question A1

A veterinary practice runs its booking website on Amazon EC2 and keeps X-ray images in Amazon S3. After the move to AWS, its IT contractor drafts a list of security tasks. Which task on the list is AWS's responsibility?

- A. Installing updates for the booking software on the EC2 instances
- B. Patching the virtualization layer that the EC2 instances run on
- C. Choosing which staff members can open the X-ray images
- D. Writing the security group rules for the web servers

<details><summary>Answer</summary>

**B is right.** The host operating system and the virtualization layer are part of security **of** the cloud, which AWS does on every service.

- **A is wrong.** Software the customer installs on an EC2 instance is the customer's to update.
- **C is wrong.** Who can reach the data is always the customer's decision, on every service.
- **D is wrong.** AWS puts security group configuration on EC2 customers.

</details>

### Question A2

A film festival sells tickets through AWS Lambda functions that use a managed Python runtime. In the same month, AWS publishes a security update for that runtime, and a flaw is found in an image library that the festival bundled with its function code. By default, who deals with each?

- A. The festival applies the runtime update, and AWS replaces the library
- B. AWS deals with both, because the functions are serverless
- C. AWS applies the runtime update, and the festival updates the library
- D. The festival deals with both, because the functions are its code

<details><summary>Answer</summary>

**C is right.** Lambda's runtime documentation splits it this way: AWS publishes security updates for the runtimes it manages and, by default, applies them; you update your function code, including the libraries it depends on.

- **A is wrong.** It reverses the split.
- **B is wrong.** "Serverless" takes the servers off your list, not your code's libraries.
- **D is wrong.** On a managed runtime, applying the runtime's updates is AWS's work. (Moving off a runtime that is being retired is the festival's, but that isn't what happened here.)

</details>

### Question A3

A charity's donor database runs on Amazon RDS. The charity wants the database to keep working if one Availability Zone fails. How is the work split?

- A. AWS makes every RDS database Multi-AZ, so the charity has nothing to decide
- B. The charity builds a standby server on EC2 and keeps it patched
- C. AWS picks the setting for each database, and the charity can't change it
- D. The charity chooses a Multi-AZ deployment, and AWS carries it out

<details><summary>Answer</summary>

**D is right.** On RDS, high availability is work AWS does, but the customer chooses the settings, including whether to run a Multi-AZ deployment. AWS then runs what the customer chose.

- **A is wrong.** Multi-AZ is a choice the customer makes, not something every database gets.
- **B is wrong.** That is the work RDS takes off the customer's hands; building and patching a standby server would be the EC2 way.
- **C is wrong.** The customer, not AWS, decides the setting.

</details>

### Question A4

A translation agency's audit report says that patch management is a shared control. The auditor asks what that means for the agency's Amazon EC2 instances. Which explanation is accurate?

- A. AWS patches the hosts, and the agency patches the guest operating systems
- B. AWS and the agency take turns patching the guest operating systems
- C. AWS patches the guest operating systems, and the agency checks AWS's work
- D. The agency patches the hosts, and AWS patches the guest operating systems

<details><summary>Answer</summary>

**A is right.** A shared control is a kind of work both sides do, each on its own things: AWS patches its infrastructure, and the customer patches the guest operating systems and applications it runs.

- **B is wrong.** No specific task is done by both sides. The guest operating system on EC2 is the customer's alone.
- **C is wrong.** AWS doesn't patch the guest operating system on EC2.
- **D is wrong.** It reverses the split: customers can't reach AWS's hosts.

</details>

### Question A5

A payments start-up that runs entirely on AWS sorts its controls into AWS's three kinds. Which pairing of a control and its kind is correct?

- A. Keeping card data in one isolated network zone: customer-specific
- B. Training its own staff to spot fake sign-in pages: inherited
- C. Controlling who enters the data center buildings: shared
- D. Keeping its guest operating systems securely configured: inherited

<details><summary>Answer</summary>

**A is right.** Keeping certain data inside certain protected zones is AWS's own example of a customer-specific control: it comes only from what the customer builds, so AWS has no matching half.

- **B is wrong.** Awareness and training is shared: AWS trains its staff, and the start-up must train its own. An inherited control leaves the customer nothing to do.
- **C is wrong.** Physical entry to the buildings is inherited: AWS does all of it.
- **D is wrong.** Configuring the guest operating system is the customer's half of configuration management, a shared control.

</details>

### Question A6

A cycling club's single AWS account uses IAM. Which pairing of a need and an identity follows AWS's advice?

- A. An AWS Lambda function that records race times: an IAM user group
- B. A sponsor's own AWS account that must read the results: the club treasurer's access key
- C. Three volunteers who need the same access: an IAM user each, in one group
- D. A backup program on an EC2 instance: an access key for the root user

<details><summary>Answer</summary>

**C is right.** Each person gets their own IAM user, so every action can be traced to one person, and the group carries the shared policy, so the next volunteer is one step to add.

- **A is wrong.** A group only carries policies for its users. It isn't a principal, so nothing can act as a group. A function should use an IAM role.
- **B is wrong.** Handing over a person's long-term key gives the sponsor everything the treasurer can do, for as long as the key exists. Another account's people should get in through a cross-account role.
- **D is wrong.** Root access keys should never exist. A program on EC2 should use an IAM role.

</details>

### Question A7

A small design studio uses one standalone AWS account, with an IAM user for each person who works in it. It lists five needs. Which TWO should be met with an IAM role? (Select TWO.)

- A. A Lambda function that resizes the images clients upload
- B. The studio owner's own daily administration work
- C. A client's own AWS account that must download finished artwork
- D. Three designers who all do the same job
- E. Closing the account when the studio shuts down

<details><summary>Answer</summary>

**A and C are right.** Programs on AWS get roles, so they receive temporary credentials and nothing long-lived is stored. People in another AWS account get in through a cross-account role, so the studio manages no users for them.

- **B is wrong.** A person working in the account gets their own IAM user, with MFA; the owner keeps the root user for root-only tasks.
- **D is wrong.** People with the same job get their own IAM users in one group that carries the policy.
- **E is wrong.** Closing the account is a root-only task, so it needs the root user, not a role.

</details>

### Question A8

In a standalone AWS account, which of these tasks needs the root user's credentials?

- A. Creating a budget, once IAM access to billing is on
- B. Fixing a bucket policy that locks out every principal
- C. Choosing which AWS Regions the account may use
- D. Updating the account's alternate contacts

<details><summary>Answer</summary>

**B is right.** A bucket policy that denies every principal locks out every IAM identity, administrators included, so only the root user can fix it. It fits the pattern: root-only tasks change the account itself or rescue it from a lockout.

- **A is wrong.** Once IAM access to billing is on, an IAM identity with permission can create budgets.
- **C is wrong.** Choosing Regions is not on AWS's root-only list (as of 2026-10-23).
- **D is wrong.** Contact details can be changed without root.

</details>

### Question A9

A small firm keeps its root user locked away and wants to sign in as root as rarely as possible. Which TWO tasks on its to-do list need the root user? (Select TWO.)

- A. Moving from Basic Support to a paid Support plan
- B. Changing the root user's password
- C. Creating an IAM role for a new application
- D. Restoring IAM permissions after the only IAM administrator removed their own
- E. Viewing the monthly bill after IAM access to billing is turned on

<details><summary>Answer</summary>

**B and D are right.** Both are on AWS's list of tasks that need root (checked 2026-10-23). Changing root's password changes the account's own sign-in; restoring a locked-out administrator rescues the account.

- **A is wrong.** Older material says changing the Support plan needs root, but AWS's current list doesn't include it.
- **C is wrong.** Creating roles is ordinary IAM work for an administrator.
- **E is wrong.** Turning on IAM access to billing needs root once; after that, IAM identities with permission can read the bill.

</details>

### Question A10

A developer's identity-based policy allows every Amazon S3 action and every Amazon DynamoDB action. A permissions boundary on the developer allows only S3 actions. No policy contains a Deny. The developer tries to create a DynamoDB table. What happens?

- A. Allowed, because the identity-based policy allows it
- B. Denied, because an explicit deny overrides the allow
- C. Allowed, because permissions boundaries apply only to roles
- D. Denied, because the boundary doesn't allow the action

<details><summary>Answer</summary>

**D is right.** A permissions boundary only sets limits. When one applies, it must also allow the request, and this one allows only S3 actions.

- **A is wrong.** An allow in the identity-based policy isn't enough when a limit-setting policy applies and doesn't allow the action.
- **B is wrong.** No policy says Deny. The request fails because the boundary doesn't allow it, not because of an explicit deny.
- **C is wrong.** A boundary caps an identity's own policies, and the developer here is a user.

</details>

### Question A11

A researcher's IAM user is in Account C. Her identity-based policy allows `s3:GetObject` on the objects in a bucket that belongs to a university's Account R. Nothing in Account R, neither a bucket policy nor a role, lets Account C in. She tries to download a file. What happens?

- A. Allowed, because her identity-based policy allows the action
- B. Allowed, because S3 buckets can be read from any account
- C. Denied, because Account R's side doesn't allow her account
- D. Denied, because identity policies can't name another account's bucket

<details><summary>Answer</summary>

**C is right.** Across two accounts, both sides must allow: the requester's identity-based policy, and the resource's side (here, a bucket policy or a role in Account R). Only one side allows it.

- **A is wrong.** Within one account that would be enough; across accounts it is only half.
- **B is wrong.** Nothing is allowed by default, least of all to other accounts.
- **D is wrong.** An identity-based policy can name a resource in another account. It just isn't enough on its own.

</details>

### Question A12

A reporting job uses an IAM role with two policies: a customer managed policy that allows reading from the `sales-data` bucket, and an inline policy that allows writing to the `reports` bucket. An engineer deletes the role, creates a new role with the same name, and attaches the same customer managed policy. No bucket policies mention the role. The job then tries to write a report to `reports`. What happens?

- A. Allowed, because the new role has the same name as the old one
- B. Denied, because the inline policy was deleted with the old role
- C. Allowed, because the inline policy is kept in the account for reuse
- D. Denied, because the customer managed policy denies writing

<details><summary>Answer</summary>

**B is right.** An inline policy lives inside one identity and is deleted with it. The new role has only the customer managed policy, which allows reading `sales-data`, so nothing allows the write: an implicit deny.

- **A is wrong.** Permissions come from the policies attached to the role, not from its name.
- **C is wrong.** That describes a managed policy, which is standalone and can be attached again. An inline policy can't.
- **D is wrong.** The customer managed policy has no Deny; it just doesn't mention writing. The request fails by default.

</details>

### Question A13

A ferry company's booking app needs two values when it runs: the web address of a partner's timetable service, which isn't secret, and an API token for its payment provider, which must be replaced automatically every 60 days. Where should each go?

- A. The address in AWS Secrets Manager, and the token in Parameter Store
- B. Both in the app's code, with the token encrypted
- C. Both in Parameter Store, as `SecureString` parameters
- D. The address in Parameter Store, the token in Secrets Manager with rotation

<details><summary>Answer</summary>

**D is right.** Parameter Store, a capability of AWS Systems Manager, is built for configuration values such as an address. Secrets Manager is built for secrets and can rotate them on a schedule, which the token needs.

- **A is wrong.** It swaps the two: Parameter Store can't rotate the token.
- **B is wrong.** Anyone who sees the code sees the values, and changing the token would mean changing the code.
- **C is wrong.** `SecureString` encrypts the token, but Parameter Store still can't replace it automatically.

</details>

### Question A14

A library network runs five AWS accounts. Its staff accounts live in Microsoft Active Directory in its own data center, and it wants AWS to pass staff sign-ins to that existing directory. Its members sign in to a mobile app to reserve books. Which TWO services fit these needs? (Select TWO.)

- A. Amazon Cognito, for the members' app sign-in
- B. AWS IAM Identity Center, for the members' app sign-in
- C. IAM users in each account, for every member
- D. AWS Directory Service, to connect AWS to the staff directory
- E. AWS Secrets Manager, to hold each staff member's password

<details><summary>Answer</summary>

**A and D are right.** Cognito gives an app its own sign-up and sign-in for customers. Directory Service connects AWS to an existing Microsoft Active Directory (its AD Connector passes sign-ins to the directory), often as the identity source for IAM Identity Center.

- **B is wrong.** Identity Center is for the workforce, not for the customers of an app. (Older material calls it AWS Single Sign-On.)
- **C is wrong.** IAM users are for the account's own people and programs; app customers should never be IAM users.
- **E is wrong.** Secrets Manager stores an application's secrets; it doesn't sign people in.

</details>

### Question A15

A museum volunteer needs to run a few AWS CLI commands this afternoon. She is on a shared library computer where she can't install software, and the museum forbids long-term access keys. What should she use?

- A. AWS CloudShell, opened from the console after she signs in
- B. `aws login`, after installing the AWS CLI on the computer
- C. An access key for her IAM user, deleted when she finishes
- D. The root user's access key, protected by MFA

<details><summary>Answer</summary>

**A is right.** CloudShell runs the AWS CLI in the browser, with temporary credentials from her console sign-in, so nothing needs to be installed and no key is created.

- **B is wrong.** `aws login` avoids keys too, but it needs the AWS CLI installed on the computer, which she can't do.
- **C is wrong.** An access key is a long-term credential, which the museum forbids. A key on a shared computer is also easy to leave behind.
- **D is wrong.** The root user should never have access keys, and an access key skips MFA anyway.

</details>

## Correction map

For each question you missed, reread the section, then try the "another way to see it" line before you redo the practice. Lessons are in this module.

| Question | Objective | Reread | Another way to see it | Practice |
|---|---|---|---|---|
| A1 | 04.01a Say who does a task, and why | 04.01, [AWS is responsible for security of the cloud](01-security-of-vs-in-the-cloud.md#aws-is-responsible-for-security-of-the-cloud) | Ask: could the customer even reach it? Nobody outside AWS can touch the hosts or the virtualization software. | [Sim S3](08-sim-responsibility-slider.md), Decision 1 |
| A2 | 04.01a | 04.01, [Four services side by side](01-security-of-vs-in-the-cloud.md#four-services-side-by-side) | On Lambda, AWS owns the language software it publishes; you own every file you upload, libraries included. | [Sim S3](08-sim-responsibility-slider.md), Decision 3 |
| A3 | 04.01a | 04.01, [A database three ways](01-security-of-vs-in-the-cloud.md#a-database-three-ways-on-premises-on-ec2-on-rds) | In the RDS table, "AWS" means AWS does the work. The choices, such as Multi-AZ and how long backups are kept, stay yours. | [Sim S3](08-sim-responsibility-slider.md), Decision 2 |
| A4 | 04.02a Explain "shared" | 04.02, [Shared controls](02-shared-inherited-customer-specific.md#shared-controls-each-side-does-its-own-half) and ["Shared" doesn't mean both sides do the same task](02-shared-inherited-customer-specific.md#shared-doesnt-mean-both-sides-do-the-same-task) | Draw 04.01's dashed line through every shared control: AWS's half sits below it, yours above, and no single task crosses it. | [Sim S3](08-sim-responsibility-slider.md), The whole slider |
| A5 | 04.02a | 04.02, [Customer-specific controls](02-shared-inherited-customer-specific.md#customer-specific-controls-only-you-can-do-these), the comparison table | Run the flowchart: does the customer do anything? Does AWS do its own version for its infrastructure? | 04.02, [the insurer's questionnaire](02-shared-inherited-customer-specific.md#worked-example-answering-the-insurers-questionnaire) |
| A6 | 04.03a Pick the identity | 04.03, [Four kinds of identity](03-identities.md#an-aws-account-has-four-kinds-of-identity) | Only people end up as IAM users; programs and other accounts get roles; groups only hold policies. | [Sim S4](09-sim-policy-playground.md), Decision 3 |
| A7 | 04.03a | 04.03, [Worked example: an identity for every need](03-identities.md#worked-example-an-identity-for-every-need-at-the-bakery) | Ask "what needs access?" first (a person, a team, a program), then "how long should it last?" | [Lab 03](06-lab-03-a-group-and-a-policy.md) |
| A8 | 04.03b Root-only tasks | 04.03, [Only the root user can do a short list of tasks](03-identities.md#only-the-root-user-can-do-a-short-list-of-tasks) | Root-only tasks either change the account itself (its email, the root password, closing it) or rescue it when IAM can't (a lockout, a policy that denies everyone). | [Primer page 02](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md) |
| A9 | 04.03b | 04.03, ["Changing the Support plan needs root" is out of date](03-identities.md#changing-the-support-plan-needs-root-is-out-of-date) | If the task is ordinary account work that an IAM policy could allow, it isn't root-only. | 04.03, [Practice](03-identities.md#practice) |
| A10 | 04.04a Predict allow or deny | 04.04, [How AWS decides](04-policies-and-least-privilege.md#how-aws-decides-default-deny-then-allows-then-an-explicit-deny-wins) | A boundary is an upper limit: the identity gets only what both its own policies and its boundary allow. | [Sim S4](09-sim-policy-playground.md), Decision 1, case 8 |
| A11 | 04.04a | 04.04, [Identity-based and resource-based policies](04-policies-and-least-privilege.md#identity-based-policies-follow-the-identity-resource-based-policies-sit-on-the-thing) | Across accounts, count the allows: one from the requester's account and one from the resource's account. Fewer than two means denied. | [Sim S4](09-sim-policy-playground.md), Decisions 1 and 2, case 5 |
| A12 | 04.04a | 04.04, [AWS managed, customer managed or inline](04-policies-and-least-privilege.md#aws-managed-customer-managed-or-inline-who-writes-it-and-how-far-it-reaches) | A managed policy is a separate document you attach; an inline policy is written inside one identity and goes with it. | [Lab 04](07-lab-04-finish-and-fix-a-policy.md), Part C |
| A13 | 04.05a Choose a credential store and an identity approach | 04.05, [Your application's secrets belong in a store](05-credentials-and-federation.md#your-applications-secrets-belong-in-a-store-not-in-the-code) | Ask two things: is it a secret, and must it change on a schedule? Two yeses mean Secrets Manager. | 04.05, [Practice](05-credentials-and-federation.md#practice) |
| A14 | 04.05a | 04.05, [Four identity services, side by side](05-credentials-and-federation.md#four-identity-services-side-by-side) | Ask whose sign-in it is: customers mean Cognito, staff mean Identity Center, an existing Active Directory means Directory Service. | [Sim S4](09-sim-policy-playground.md), Decision 5 |
| A15 | 04.05a | 04.05, ["Access keys are the normal way to use the command line" is out of date](05-credentials-and-federation.md#access-keys-are-the-normal-way-to-use-the-command-line-is-out-of-date) | Two keyless routes: CloudShell when you can't install anything, `aws login` on your own computer. | [Primer page 04](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md) |

## Check B: parallel retest

Take Check B after you have worked through the correction map. Question B1 tests the same objective as A1, and so on. The pass mark is the same: 12 of 15.

### Question B1

A travel writer runs her blog on an Amazon EC2 instance and stores its photos in Amazon S3. Which task on her security checklist is AWS's?

- A. Applying updates to the blogging software she installed
- B. Deciding whether the photo bucket allows public reads
- C. Replacing a failed network switch in the data center
- D. Patching the instance's guest operating system

<details><summary>Answer</summary>

**C is right.** Network hardware in AWS's buildings is infrastructure: security **of** the cloud, AWS's on every service.

- **A is wrong.** Software she installs on EC2 is hers to keep updated.
- **B is wrong.** Who can read her data is always her decision, and S3's public-access settings are hers to keep.
- **D is wrong.** On EC2, the customer patches the guest operating system.

</details>

### Question B2

A charity creates donation receipts with AWS Lambda functions on a managed Node.js runtime. AWS announces that the runtime version is being deprecated, and a flaw is found in a date-handling library bundled with the function code. What must the charity do?

- A. Wait, because AWS moves the functions and fixes the library
- B. Update the library, and wait for AWS to move the functions
- C. Move to the new runtime, and wait for AWS to fix the library
- D. Update the library, and move the functions to a supported runtime

<details><summary>Answer</summary>

**D is right.** Lambda's runtime documentation puts both on the customer: updating the code's dependencies when they have flaws, and moving functions to a supported runtime before the old one is retired.

- **A is wrong.** AWS updates the runtimes it manages, but it doesn't change your code or move your functions for you.
- **B is wrong.** The move off a deprecated runtime is the customer's job.
- **C is wrong.** Libraries bundled with the code are the customer's to fix.

</details>

### Question B3

A clinic's appointment database runs on Amazon RDS. The clinic's records policy now says automated backups must be kept for two weeks instead of one. How is the work split?

- A. The clinic sets the backup retention period, and AWS takes the backups
- B. The clinic switches to manual snapshots, because automated backups can't be kept longer
- C. AWS sets the retention period, and the clinic can't change it
- D. The clinic turns on Multi-AZ, which keeps older copies of the data

<details><summary>Answer</summary>

**A is right.** On RDS, AWS does the backup work, but the customer chooses whether automated backups are on and how long they are kept.

- **B is wrong.** Automated backups can be kept longer than the default; the clinic only changes the setting.
- **C is wrong.** How long backups are kept is the customer's setting.
- **D is wrong.** A Multi-AZ standby copies every change at once, so it holds no older copies. It is for high availability, not for going back in time.

</details>

### Question B4

A logistics firm's audit report says configuration management is a shared control. The firm runs its web servers on Amazon EC2. Which explanation is accurate?

- A. AWS sets up its own devices; the firm sets up its servers and settings
- B. AWS and the firm set up each EC2 instance together
- C. AWS sets up the firm's security groups, and the firm reviews them
- D. The firm sets up the network devices inside AWS's data centers

<details><summary>Answer</summary>

**A is right.** AWS configures its infrastructure devices; the customer configures its own operating systems, applications and resource settings, such as security groups. Each side works on its own things.

- **B is wrong.** "Shared" doesn't mean a task is done together. Each instance's setup is the firm's alone.
- **C is wrong.** The EC2 customer writes the security group rules, not AWS.
- **D is wrong.** Customers can't reach AWS's network devices; those are AWS's half.

</details>

### Question B5

A law practice that runs entirely on AWS sorts its controls into AWS's three kinds. Which pairing of a control and its kind is correct?

- A. Patching its guest operating systems: inherited
- B. Controlling who enters the data center buildings: customer-specific
- C. Backup power and cooling for the servers: inherited
- D. Sending client files only along one protected network path: shared

<details><summary>Answer</summary>

**C is right.** Power and cooling are physical and environmental controls, which the customer inherits from AWS completely.

- **A is wrong.** Patch management is shared: AWS patches its infrastructure, and the practice patches its guest operating systems.
- **B is wrong.** Building entry is inherited. A customer-specific control is one only the customer can do.
- **D is wrong.** Keeping data on certain protected paths is AWS's example of a customer-specific control; AWS has no matching half.

</details>

### Question B6

A bookshop's single AWS account uses IAM. Which pairing of a need and an identity follows AWS's advice?

- A. An outside accountant with her own AWS account: the bookshop's root user, shared with MFA
- B. A nightly job on an EC2 instance that writes stock reports: an IAM role the instance uses
- C. Four shop assistants who do the same job: a group that they sign in as
- D. An AWS Lambda function that sends receipts: an access key stored in its code

<details><summary>Answer</summary>

**B is right.** A program on AWS should use a role, so AWS delivers temporary credentials to it and nothing long-lived is stored.

- **A is wrong.** Root is for root-only tasks and should never be shared. Another account's people get in through a cross-account role.
- **C is wrong.** Nobody can sign in as a group. Each assistant gets an IAM user, and the group carries the policy.
- **D is wrong.** A key in code is long-term and leaks easily. The function should use a role.

</details>

### Question B7

A nonprofit manages one standalone AWS account with IAM. Two bookkeepers need identical read access to its finance reports. An audit firm, with its own AWS account, must read the same reports for a month, and the nonprofit doesn't want to manage users for the auditors. Which TWO steps fit? (Select TWO.)

- A. Create an IAM user in the nonprofit's account for each auditor
- B. Send the audit firm a copy of the bookkeepers' access keys
- C. Give each bookkeeper an IAM user, in a group that carries the policy
- D. Add the audit firm's account to the bookkeepers' group
- E. Create a role that the audit firm's account may assume

<details><summary>Answer</summary>

**C and E are right.** People with the same job get their own IAM users in one group. Another AWS account's people get in through a cross-account role, with temporary credentials and no new users to manage.

- **A is wrong.** It works, but it means managing users for the auditors, which the nonprofit wants to avoid, and remembering to remove them after the month.
- **B is wrong.** Sharing long-term keys hides who did what and gives the auditors whatever the bookkeepers can do.
- **D is wrong.** A group holds IAM users from the same account only.

</details>

### Question B8

In a standalone AWS account, which of these tasks needs the root user's credentials?

- A. Creating an IAM user for a new employee
- B. Changing the account's name
- C. Upgrading to a paid Support plan
- D. Closing the account

<details><summary>Answer</summary>

**D is right.** Closing the account changes the account itself, and AWS lists it as a root-only task (checked 2026-10-23).

- **A is wrong.** Creating IAM users is ordinary work for an IAM administrator.
- **B is wrong.** The account name can be changed without root.
- **C is wrong.** Older material says the Support plan needs root, but AWS's current list doesn't include it.

</details>

### Question B9

An office manager lists the tasks she thinks need the root user. Which TWO really do? (Select TWO.)

- A. Choosing which AWS Regions the account may use
- B. Turning on IAM access to the billing pages
- C. Updating the account's alternate contacts
- D. Creating a role for an AWS Lambda function
- E. Turning on MFA Delete for an S3 bucket

<details><summary>Answer</summary>

**B and E are right.** Both are on AWS's current list of tasks that need root (checked 2026-10-23).

- **A is wrong.** Choosing Regions isn't on the root-only list.
- **C is wrong.** Contact details can be changed without root.
- **D is wrong.** Creating roles is ordinary IAM work.

</details>

### Question B10

A tester's identity-based policy allows only reading from Amazon S3. A permissions boundary on the tester allows every S3 action and every Amazon DynamoDB action. No policy contains a Deny. The tester tries to write an item to a DynamoDB table. What happens?

- A. Allowed, because the boundary allows DynamoDB actions
- B. Denied, because no identity-based policy allows the write
- C. Allowed, because the boundary overrides the identity policy
- D. Denied, because an explicit deny in the boundary blocks it

<details><summary>Answer</summary>

**B is right.** A permissions boundary grants nothing by itself; it only caps what the identity's own policies can grant. Nothing grants the DynamoDB write, so it is denied by default.

- **A is wrong.** A boundary's allow is a limit, not a grant.
- **C is wrong.** A boundary never adds permissions to an identity's policies; it only takes away what lies outside it.
- **D is wrong.** Nothing says Deny. This is an implicit deny.

</details>

### Question B11

A photographer's Account P has a bucket whose bucket policy allows a publisher's Account Q to use `s3:GetObject` on its objects. In Account Q, an editor's group policy allows `s3:GetObject` on that bucket's objects. Nothing denies the request. The editor downloads a photo. What happens?

- A. Denied, because a bucket can't be shared with another account
- B. Denied, because the editor also needs an IAM user in Account P
- C. Allowed, because both accounts' policies allow the request
- D. Allowed, because a bucket policy alone is enough across accounts

<details><summary>Answer</summary>

**C is right.** Across two accounts, both sides must allow: Account P's bucket policy lets Account Q in, and Account Q's identity-based policy lets the editor do it.

- **A is wrong.** A bucket policy can name a principal in another account.
- **B is wrong.** The bucket policy and her own account's policy are enough; nobody needs a second user.
- **D is wrong.** The result is right, but the reason isn't. Across accounts, the bucket policy is only half: without Account Q's allow, the request would be denied.

</details>

### Question B12

An IAM user is in a group whose customer managed policy allows `s3:PutObject` on the `invoices` bucket. The user also has an inline policy that allows `s3:GetObject` on the same bucket. An administrator removes the user from the group; the customer managed policy stays attached to a role. No bucket policy mentions the user. The user tries to upload an invoice. What happens?

- A. Allowed, because the customer managed policy still exists in the account
- B. Allowed, because the inline policy keeps the group's permissions
- C. Denied, because the inline policy explicitly denies uploads
- D. Denied, because no policy that applies to the user allows it

<details><summary>Answer</summary>

**D is right.** A managed policy applies only to the identities it is attached to. Once the user leaves the group, only her inline policy applies, and it allows reading, not uploading. Nothing allows the upload: an implicit deny.

- **A is wrong.** A policy existing in the account does nothing for identities it isn't attached to.
- **B is wrong.** An inline policy holds only its own statements; it doesn't copy a group's.
- **C is wrong.** The inline policy has no Deny; it simply doesn't allow uploads.

</details>

### Question B13

A weather service's application on Amazon EC2 needs two things: the ID of the sensor feed it reads, a plain setting that rarely changes, and permission to write readings to Amazon DynamoDB. What fits best?

- A. The feed ID in Parameter Store, and an IAM role for the DynamoDB access
- B. The feed ID in AWS Secrets Manager, and an access key in Parameter Store
- C. Both in Secrets Manager, with automatic rotation turned on
- D. The feed ID in the code, and an access key in Secrets Manager

<details><summary>Answer</summary>

**A is right.** Parameter Store, a capability of AWS Systems Manager, holds configuration values. AWS's own credentials don't belong in either store: the application gets a role, and AWS delivers temporary credentials to it.

- **B is wrong.** A plain setting doesn't need a secrets service, and an access key is a long-term credential the app shouldn't need.
- **C is wrong.** Rotation is for secrets. AWS access should come from a role, not from a stored key.
- **D is wrong.** Settings in code mean a code change for every new value, and a stored access key is what roles exist to avoid.

</details>

### Question B14

A hospital group runs ten AWS accounts in AWS Organizations. Its staff accounts live in Microsoft Active Directory in its own data center. It wants staff to sign in once, with the user names and passwords they already have, and then pick the AWS account their job needs. Which TWO services together meet this need? (Select TWO.)

- A. Amazon Cognito
- B. AWS IAM Identity Center
- C. AWS Secrets Manager
- D. AWS Directory Service
- E. IAM users in each account, one for each staff member

<details><summary>Answer</summary>

**B and D are right.** IAM Identity Center (formerly AWS Single Sign-On) gives a workforce one sign-in to many accounts. Directory Service connects AWS to the existing Active Directory, often as Identity Center's identity source, so staff keep the sign-in they already have.

- **A is wrong.** Cognito is for the customers of your own app, not for staff.
- **C is wrong.** Secrets Manager stores an application's secrets; it doesn't sign people in.
- **E is wrong.** That would mean a second, long-term sign-in for every person in every account, which is what single sign-on avoids, and it ignores the directory they already have.

</details>

### Question B15

A developer wants to run scripts on her own laptop that call AWS through a current version of the AWS CLI. The scripts read files stored on the laptop, and her company forbids long-term access keys. What should she use?

- A. An access key for her IAM user, replaced every 90 days
- B. `aws login`, with her console sign-in
- C. AWS CloudShell, so that the commands run in the browser instead
- D. The root user's access key, protected by MFA

<details><summary>Answer</summary>

**B is right.** `aws login` gives the CLI on her own computer temporary credentials from her console sign-in, so no access key is created and her scripts run where her files are.

- **A is wrong.** Rotating a key is better than not rotating it, but it is still a long-term credential, which the company forbids.
- **C is wrong.** CloudShell avoids keys too, but it runs in AWS, not on her laptop, so her scripts couldn't read the laptop's files where they are.
- **D is wrong.** The root user should never have access keys, and an access key skips MFA anyway.

</details>

## Enrichment for learners who pass

These are harder than the checks: there is more than one good answer. Write your answer before you open the model.

### Task 1: design access for the bakery's second year

The bakery now has two AWS accounts in AWS Organizations (live and test), eight staff, a customer mobile app, a delivery partner with its own AWS account, and a payment provider's API key that must change every quarter. Design how each gets in, or where each value lives. For each choice, name the Well-Architected best practice it follows, and one thing that would make you change the design.

<details><summary>Model answer</summary>

- **Staff:** IAM Identity Center with MFA, one permission set per job (for example, photo editor, developer, billing reader), assigned to the accounts each person needs. That follows [SEC02-BP04 Rely on a centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html), and keeping each permission set to its job follows [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html). If the bakery already ran Microsoft Active Directory, you would connect it through AWS Directory Service as Identity Center's source.
- **App customers:** Amazon Cognito user pools, never IAM users.
- **Delivery partner:** a cross-account role in the live account, with read-only access to the day's orders, and a trust policy naming the partner's account. Temporary credentials follow [SEC02-BP02 Use temporary credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html). Review the trust policy as [SEC03-BP07 Analyze public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html) asks.
- **Payment API key:** AWS Secrets Manager with rotation, read at run time by the app's IAM role: [SEC02-BP03 Store and use secrets securely](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_secrets.html).
- **Root users:** one per account, MFA, no access keys, used only for root-only tasks.

What could change it: a partner without an AWS account (then neither a role nor a bucket policy for its account fits, and you would design an app-level route instead); or a regulator requiring that some data never leaves one account (a customer-specific control you would add yourself).

</details>

### Task 2: argue for moving the order database

The bakery's order database runs on an EC2 instance that the nephew patches "when he remembers". Write the owner a short case for moving it to Amazon RDS, using the shared responsibility model. Say what moves to AWS, what stays with the bakery, and what evidence the bakery would show an insurer for each kind of control afterward.

<details><summary>Model answer</summary>

Moving to RDS hands AWS the operating system and database software patching, plus the work of backups, high availability and scaling, which removes the "when he remembers" risk. That is [SEC01-BP05 Reduce security management scope](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_reduce_management_scope.html): choose services that leave you less to run. It also follows the cost design principle "[Stop spending money on undifferentiated heavy lifting](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)".

What stays with the bakery: query tuning; who can connect (IAM and security groups); and the settings AWS then carries out, such as whether to run Multi-AZ and how long automated backups are kept.

Evidence afterward: for physical and environmental controls, which the bakery inherits, AWS's audit reports. For patch management, a shared control, AWS's reports cover the database's patching, and the bakery's own records cover what it still runs, such as the web server. For access to the order data, the bakery's own settings and records, because that is always its side.

</details>

### Task 3: plan the root user's rare appearances

Write a one-page "break-glass" plan for the bakery's root user: where its MFA devices are kept and who can reach them; which situations justify signing in as root; how the owner would notice if root were used without her knowing; and what you would do afterward.

<details><summary>Model answer</summary>

- **Devices:** the passkey with the owner; the backup authenticator in a locked place a second trusted person can reach, so one lost phone doesn't lock the bakery out. No root access keys, ever.
- **When to use it:** only for root-only tasks, such as closing or reopening the account, changing the root password or the standalone account's email, turning on IAM access to billing, or restoring access when the only IAM administrator is locked out. Changing the Support plan isn't one of them (as of 2026-10-23). Everything else uses an IAM identity.
- **Noticing:** filter CloudTrail Event history by `root` regularly, as on primer page 02, and keep the account's email and phone recovery details under the owner's control.
- **Afterward:** record why root was used, sign out, and check that nothing else changed.

This is [SEC01-BP02 Secure account root user and properties](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_aws_account.html), which treats any other use of root as an anti-pattern.

</details>

---

"Module 04 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
