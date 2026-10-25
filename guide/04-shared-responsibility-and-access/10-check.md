---
type: check
id: clf-04-10
title: "Module 04 mastery check"
tasks: ["2.1", "2.3"]
objectives: ["04.01a", "04.02a", "04.03a", "04.03b", "04.04a", "04.05a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 04 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-04-01, clf-04-02, clf-04-03, clf-04-04, clf-04-05]
pillars: [security]
facts_checked: 2026-10-25
sources:
  - "https://aws.amazon.com/compliance/shared-responsibility-model/"
  - "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html"
  - "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"
  - "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
---

# Module 04 mastery check: split the security work, and choose who gets in and how

**For:** an adult studying alone, possibly new to IT, who has finished lessons [04.01](01-security-of-vs-in-the-cloud.md) to [04.05](05-credentials-and-federation.md). **Time:** about 20 minutes per check.

**Exam guide:** [Domain 2, Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) (30% of the exam): tasks [2.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.1) and [2.3](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html#cloud-practitioner-02-task2.3).

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 05.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

### Question A1

A veterinary practice runs its booking website on Amazon EC2 and keeps X-ray images in Amazon S3. Which task is AWS's?

- A. Installing updates for the booking software on the EC2 instances
- B. Patching the virtualization layer that the EC2 instances run on
- C. Choosing which staff members can open the X-ray images
- D. Writing the security group rules for the web servers

<details><summary>Answer</summary>

**B is right.** The virtualization layer is security **of** the cloud.

- **A is wrong.** Software you install on EC2 is yours to update.
- **C is wrong.** Who can reach the data is always the customer's decision.
- **D is wrong.** AWS puts security group configuration on EC2 customers.

</details>

### Question A2

A film festival's AWS Lambda functions use a managed Python runtime. AWS publishes a security update for that runtime, and a flaw is found in an image library bundled with the festival's code. By default, who deals with each?

- A. The festival applies the runtime update, and AWS replaces the library
- B. AWS deals with both, because the functions are serverless
- C. AWS applies the runtime update, and the festival updates the library
- D. The festival deals with both, because the functions are its code

<details><summary>Answer</summary>

**C is right.** AWS applies updates to the runtimes it manages, by default; you update your code and its libraries.

- **A is wrong.** It reverses the split.
- **B is wrong.** Serverless doesn't take your code's libraries off your list.
- **D is wrong.** Managed runtime updates are AWS's work.

</details>

### Question A3

A translation agency's auditor says patch management is a shared control and asks what that means for the agency's EC2 instances. Which explanation is accurate?

- A. AWS patches the hosts, and the agency patches the guest operating systems
- B. AWS and the agency take turns patching the guest operating systems
- C. AWS patches the guest operating systems, and the agency checks AWS's work
- D. The agency patches the hosts, and AWS patches the guest operating systems

<details><summary>Answer</summary>

**A is right.** Each side patches its own things.

- **B is wrong.** No specific task is done by both sides.
- **C is wrong.** AWS doesn't patch the guest operating system on EC2.
- **D is wrong.** It reverses the split; customers can't reach AWS's hosts.

</details>

### Question A4

A payments start-up sorts its controls into AWS's three kinds. Which pairing is correct?

- A. Keeping card data in one isolated network zone: customer-specific
- B. Training its own staff to spot fake sign-in pages: inherited
- C. Controlling who enters the data center buildings: shared
- D. Keeping its guest operating systems securely configured: inherited

<details><summary>Answer</summary>

**A is right.** Zoning data is AWS's own example of a customer-specific control.

- **B is wrong.** Training is shared; the start-up trains its own staff.
- **C is wrong.** Physical entry is inherited.
- **D is wrong.** Configuring the guest OS is the customer's half of a shared control.

</details>

### Question A5

For a cycling club's single AWS account, which pairing of a need and an identity follows AWS's advice?

- A. An AWS Lambda function that records race times: an IAM user group
- B. A sponsor's own AWS account that must read the results: the treasurer's access key
- C. Three volunteers who need the same access: an IAM user each, in one group
- D. A backup program on an EC2 instance: an access key for the root user

<details><summary>Answer</summary>

**C is right.** Each person gets their own IAM user, and the group carries the shared policy.

- **A is wrong.** Nothing can act as a group; a function should use an IAM role.
- **B is wrong.** Another account should use a cross-account role, not a person's long-term key.
- **D is wrong.** Root access keys should never exist.

</details>

### Question A6

In a standalone AWS account, which task needs the root user's credentials?

- A. Creating a budget, once IAM access to billing is on
- B. Fixing a bucket policy that locks out every principal
- C. Choosing which AWS Regions the account may use
- D. Updating the account's alternate contacts

<details><summary>Answer</summary>

**B is right.** A policy that denies everyone locks out every IAM identity, so only root can fix it.

- **A is wrong.** Once billing access is on, an IAM identity with permission can create budgets.
- **C is wrong.** Choosing Regions isn't on AWS's root-only list (as of 2026-10-23).
- **D is wrong.** Contact details can be changed without root.

</details>

### Question A7

A small firm wants to sign in as root as rarely as possible. Which TWO tasks on its list need the root user? (Select TWO.)

- A. Moving from Basic Support to a paid Support plan
- B. Changing the root user's password
- C. Creating an IAM role for a new application
- D. Restoring IAM permissions after the only IAM administrator removed their own
- E. Viewing the monthly bill after IAM access to billing is turned on

<details><summary>Answer</summary>

**B and D are right.** Both are on AWS's root-only list (checked 2026-10-23): one changes the account's own sign-in, the other rescues it.

- **A is wrong.** Older material says so, but AWS's current list doesn't include it.
- **C is wrong.** Creating roles is ordinary IAM work.
- **E is wrong.** IAM identities with permission can read the bill.

</details>

### Question A8

A reporting role has a customer managed policy that allows reading the `sales-data` bucket and an inline policy that allows writing to `reports`. An engineer deletes the role, creates a new one with the same name, and attaches the same customer managed policy. Can the job still write to `reports`?

- A. Yes, because the new role has the same name as the old one
- B. No, because the inline policy was deleted with the old role
- C. Yes, because the inline policy is kept in the account for reuse
- D. No, because the customer managed policy denies writing

<details><summary>Answer</summary>

**B is right.** An inline policy is deleted with its identity, so nothing allows the write.

- **A is wrong.** Permissions come from attached policies, not a name.
- **C is wrong.** That describes a managed policy, which is standalone.
- **D is wrong.** The managed policy has no Deny.

</details>

### Question A9

A ferry company's app needs the web address of a partner's timetable service, which isn't secret, and a payment API token that must be replaced automatically every 60 days. Where should each go?

- A. The address in AWS Secrets Manager, and the token in Parameter Store
- B. Both in the app's code, with the token encrypted
- C. Both in Parameter Store, as `SecureString` parameters
- D. The address in Parameter Store, the token in Secrets Manager with rotation

<details><summary>Answer</summary>

**D is right.** Parameter Store holds configuration values; Secrets Manager holds secrets and can rotate them on a schedule.

- **A is wrong.** It swaps them: Parameter Store can't rotate the token.
- **B is wrong.** Anyone who sees the code sees the values.
- **C is wrong.** `SecureString` encrypts but can't rotate.

</details>

### Question A10

A library network's staff accounts live in Microsoft Active Directory in its own data center, and it wants AWS to pass staff sign-ins to that directory. Its members sign in to a mobile app to reserve books. Which TWO services fit? (Select TWO.)

- A. Amazon Cognito, for the members' app sign-in
- B. AWS IAM Identity Center, for the members' app sign-in
- C. IAM users in each account, for every member
- D. AWS Directory Service, to connect AWS to the staff directory
- E. AWS Secrets Manager, to hold each staff member's password

<details><summary>Answer</summary>

**A and D are right.** Cognito gives an app sign-in for its customers; Directory Service connects AWS to an existing Active Directory.

- **B is wrong.** Identity Center (formerly AWS Single Sign-On) is for the workforce, not app customers.
- **C is wrong.** App customers should never be IAM users.
- **E is wrong.** Secrets Manager stores application secrets; it doesn't sign people in.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 04.01a | [AWS is responsible for security of the cloud](01-security-of-vs-in-the-cloud.md#aws-is-responsible-for-security-of-the-cloud) |
| A2, B2 | 04.01a | [The line moves with the service](01-security-of-vs-in-the-cloud.md#the-line-moves-with-the-service-ec2-rds-lambda-and-s3) |
| A3, B3 | 04.02a | [Shared controls](02-shared-inherited-customer-specific.md#shared-controls-each-side-does-its-own-half) and ["Shared" doesn't mean the same task](02-shared-inherited-customer-specific.md#shared-doesnt-mean-both-sides-do-the-same-task) |
| A4, B4 | 04.02a | [Customer-specific controls](02-shared-inherited-customer-specific.md#customer-specific-controls-only-you-can-do-these) |
| A5, B5 | 04.03a | [Four kinds of identity](03-identities.md#an-aws-account-has-four-kinds-of-identity) |
| A6, B6 | 04.03b | [Root-only tasks](03-identities.md#only-the-root-user-can-do-a-short-list-of-tasks) |
| A7, B7 | 04.03b | ["Changing the Support plan needs root" is out of date](03-identities.md#changing-the-support-plan-needs-root-is-out-of-date) |
| A8, B8 | 04.04a | [AWS managed, customer managed or inline](04-policies-and-least-privilege.md#aws-managed-customer-managed-or-inline-who-writes-it-and-how-far-it-reaches) |
| A9, B9 | 04.05a | [Secrets belong in a store](05-credentials-and-federation.md#your-applications-secrets-belong-in-a-store-not-in-the-code) |
| A10, B10 | 04.05a | [Four identity services](05-credentials-and-federation.md#four-identity-services-side-by-side) |

## Check B: parallel retest

### Question B1

A travel writer runs her blog on Amazon EC2 and stores its photos in Amazon S3. Which task is AWS's?

- A. Applying updates to the blogging software she installed
- B. Deciding whether the photo bucket allows public reads
- C. Replacing a failed network switch in the data center
- D. Patching the instance's guest operating system

<details><summary>Answer</summary>

**C is right.** Network hardware is infrastructure: security **of** the cloud.

- **A is wrong.** Software she installs on EC2 is hers to update.
- **B is wrong.** Who can read her data is always her decision.
- **D is wrong.** On EC2, the customer patches the guest OS.

</details>

### Question B2

A charity's AWS Lambda functions run on a managed Node.js runtime. AWS announces that the runtime version is being deprecated, and a flaw is found in a library bundled with the code. What must the charity do?

- A. Wait, because AWS moves the functions and fixes the library
- B. Update the library, and wait for AWS to move the functions
- C. Move to the new runtime, and wait for AWS to fix the library
- D. Update the library, and move the functions to a supported runtime

<details><summary>Answer</summary>

**D is right.** Lambda's runtime documentation puts both on the customer.

- **A is wrong.** AWS doesn't change your code or move your functions.
- **B is wrong.** The move off a deprecated runtime is the customer's job.
- **C is wrong.** Bundled libraries are the customer's to fix.

</details>

### Question B3

A logistics firm's audit report says configuration management is a shared control. The firm runs its web servers on EC2. Which explanation is accurate?

- A. AWS sets up its own devices; the firm sets up its servers and settings
- B. AWS and the firm set up each EC2 instance together
- C. AWS sets up the firm's security groups, and the firm reviews them
- D. The firm sets up the network devices inside AWS's data centers

<details><summary>Answer</summary>

**A is right.** Each side configures its own things.

- **B is wrong.** "Shared" doesn't mean a task is done together.
- **C is wrong.** The EC2 customer writes the security group rules.
- **D is wrong.** Customers can't reach AWS's network devices.

</details>

### Question B4

A law practice sorts its controls into AWS's three kinds. Which pairing is correct?

- A. Patching its guest operating systems: inherited
- B. Controlling who enters the data center buildings: customer-specific
- C. Backup power and cooling for the servers: inherited
- D. Sending client files only along one protected network path: shared

<details><summary>Answer</summary>

**C is right.** Power and cooling are physical and environmental controls, fully inherited.

- **A is wrong.** Patch management is shared.
- **B is wrong.** Building entry is inherited.
- **D is wrong.** Keeping data on protected paths is customer-specific.

</details>

### Question B5

For a bookshop's single AWS account, which pairing of a need and an identity follows AWS's advice?

- A. An outside accountant with her own AWS account: the root user, shared with MFA
- B. A nightly job on an EC2 instance that writes stock reports: an IAM role
- C. Four shop assistants who do the same job: a group that they sign in as
- D. An AWS Lambda function that sends receipts: an access key stored in its code

<details><summary>Answer</summary>

**B is right.** A program on AWS should use a role, so nothing long-lived is stored.

- **A is wrong.** Root should never be shared; another account should use a cross-account role.
- **C is wrong.** Nobody can sign in as a group.
- **D is wrong.** A key in code is long-term and leaks easily.

</details>

### Question B6

In a standalone AWS account, which task needs the root user's credentials?

- A. Creating an IAM user for a new employee
- B. Changing the account's name
- C. Upgrading to a paid Support plan
- D. Closing the account

<details><summary>Answer</summary>

**D is right.** Closing the account changes the account itself (root-only, checked 2026-10-23).

- **A is wrong.** Creating IAM users is ordinary admin work.
- **B is wrong.** The account name can be changed without root.
- **C is wrong.** The Support plan isn't on AWS's current root-only list.

</details>

### Question B7

An office manager lists tasks she thinks need the root user. Which TWO really do? (Select TWO.)

- A. Choosing which AWS Regions the account may use
- B. Turning on IAM access to the billing pages
- C. Updating the account's alternate contacts
- D. Creating a role for an AWS Lambda function
- E. Turning on MFA Delete for an S3 bucket

<details><summary>Answer</summary>

**B and E are right.** Both are on AWS's root-only list (checked 2026-10-23).

- **A is wrong.** Choosing Regions isn't root-only.
- **C is wrong.** Contact details can be changed without root.
- **D is wrong.** Creating roles is ordinary IAM work.

</details>

### Question B8

An IAM user is in a group whose customer managed policy allows uploading to the `invoices` bucket, and she has an inline policy that allows reading it. An administrator removes her from the group. Can she still upload?

- A. Yes, because the customer managed policy still exists in the account
- B. Yes, because the inline policy keeps the group's permissions
- C. No, because the inline policy explicitly denies uploads
- D. No, because no policy that applies to her allows it

<details><summary>Answer</summary>

**D is right.** Her inline policy allows reading only, so nothing allows the upload: an implicit deny.

- **A is wrong.** A managed policy applies only to identities it's attached to.
- **B is wrong.** An inline policy holds only its own statements.
- **C is wrong.** The inline policy has no Deny.

</details>

### Question B9

A weather service's app on Amazon EC2 needs the ID of the sensor feed it reads, a plain setting, and permission to write to Amazon DynamoDB. What fits best?

- A. The feed ID in Parameter Store, and an IAM role for the DynamoDB access
- B. The feed ID in AWS Secrets Manager, and an access key in Parameter Store
- C. Both in Secrets Manager, with automatic rotation turned on
- D. The feed ID in the code, and an access key in Secrets Manager

<details><summary>Answer</summary>

**A is right.** Parameter Store holds configuration; AWS access comes from a role, not a stored key.

- **B is wrong.** The app shouldn't need an access key at all.
- **C is wrong.** Rotation is for secrets, and AWS access should come from a role.
- **D is wrong.** Settings in code need a code change, and roles exist to avoid stored keys.

</details>

### Question B10

A hospital group runs ten AWS accounts in AWS Organizations, and its staff accounts live in Microsoft Active Directory. Staff should sign in once with their existing names and passwords, then pick an AWS account. Which TWO services together meet this need? (Select TWO.)

- A. Amazon Cognito
- B. AWS IAM Identity Center
- C. AWS Secrets Manager
- D. AWS Directory Service
- E. IAM users in each account, one for each staff member

<details><summary>Answer</summary>

**B and D are right.** Identity Center gives a workforce one sign-in to many accounts; Directory Service connects it to the existing Active Directory.

- **A is wrong.** Cognito is for the customers of your own app.
- **C is wrong.** Secrets Manager doesn't sign people in.
- **E is wrong.** That means long-term sign-ins per person per account, which single sign-on avoids.

</details>

---

"Module 04 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
