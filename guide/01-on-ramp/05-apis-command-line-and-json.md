---
type: lesson
id: clf-01-05
title: "APIs, the command line and JSON"
tasks: []
objectives: ["01.05a", "01.05b"]
reader: "Adult studying alone, new to IT, before Module 02; about 15 minutes; works on a phone, though a computer helps for the JSON reading"
prerequisites: [clf-01-01, clf-01-02]
terms_introduced: [API, endpoint, command line, terminal, shell, command, argument, option, AWS CLI, JSON, JSON object, name-value pair, array, YAML]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/api/"
  - "https://aws.amazon.com/what-is/cli/"
  - "https://aws.amazon.com/documentdb/what-is-json/"
  - "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html"
  - "https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html"
  - "https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html"
  - "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html"
---

# Programs ask each other for things through APIs; you can type those requests at a command line, and the answers often come back as JSON

Every AWS service runs on requests such as "create this" or "list those", whether you click, type or write code. Many answers, and AWS's permission documents, are written in JSON.

**For:** an adult studying alone, new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone; for the JSON, a bigger screen helps.

**Before you start:** this lesson uses server, request and HTTPS from lessons [01.01](01-computers-and-servers.md) and [01.02](02-networks-ip-dns-https.md).

## Test out: do you already know this?

Answer without looking anything up. If you get all three right, and didn't guess, skip to [Everyday security](06-everyday-security.md).

1. In one sentence, what is an API?
2. In `aws s3 ls --region us-east-1`, which part is an option?
3. In this JSON, how many statements are there, and what is the second one's `Effect`?

   ```json
   {"Statement": [{"Effect": "Allow", "Action": "s3:GetObject"}, {"Effect": "Deny", "Action": "s3:DeleteObject"}]}
   ```

<details><summary>Answer key</summary>

1. A defined set of requests one program can send another, and its answers.
2. `--region us-east-1`.
3. Two: the square brackets hold two objects. The second's is `"Deny"`.

</details>

## Warm-up: what you already know

1. From lesson 01.02: a web address starts with `https://`. What does the "S" add?

<details><summary>Feedback</summary>

1. Encryption and proof of identity. AWS's tools send their requests over HTTPS too.

</details>

## What you'll learn

By the end, you can explain what an API and the command line are for (objective 01.05a), and read a small JSON document: its names, values, lists and nested parts (objective 01.05b).

Guess before you read on: when you click a button in the AWS website and when you type a command, do your requests reach AWS by different routes?

## An API is a fixed menu of requests one program can make of another

An **API** (application programming interface) lets two programs talk by agreed rules: the client sends a request, and the server sends back a response ([What is an API?](https://aws.amazon.com/what-is/api/), checked 2026-10-24). Like a restaurant menu, it lists what may be ordered and in what form, and a misspelled request is refused with an error. The address an API listens on is its **endpoint**, such as a web address for one service in one place.

Every AWS service has an API. The console you click in, the AWS CLI you type in, and programs you write all send requests to the same APIs (lesson 08.01), which answers the guess. Two things happen to every request:

- **It's signed** with your credentials, so AWS can check who is asking and that nobody changed the request on the way ([Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html), checked 2026-10-24).
- **It's checked.** If that identity may not do that action, the answer is an error such as `AccessDenied`, and nothing is done. Module 04 is about that check.

## The command line does exactly what you type

At a **command line** you type a line, press Enter, and the computer prints its answer. The window is a **terminal**, and the program that reads your line and runs it is a **shell** ([What is a CLI?](https://aws.amazon.com/what-is/cli/), checked 2026-10-24).

The **AWS CLI** (AWS Command Line Interface) is a free program that turns typed commands into AWS API requests ([What is the AWS CLI?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), checked 2026-10-24). Its commands read left to right, from general to specific ([Command structure](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html)):

```text
aws s3 mb s3://example-bakery-photos --region us-east-1
```

`aws` is the program; `s3`, the **command**, names the service; `mb`, the subcommand, says what to do (make a bucket); the **argument** says what to do it to; and `--region us-east-1` is an **option**, a name with two dashes and then its value.

A command acts at once, often with no "are you sure?" and no undo, so read it before you press Enter, and never paste a password or secret key into one. You won't install anything for this guide's labs: **AWS CloudShell** opens a command line in your browser, already signed in as you, and on the guardrails primer's [page 04](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/04-command-line-without-access-keys.md) you'll run `aws sts get-caller-identity` there, which asks AWS "who am I?"

## JSON writes data as names and values

**JSON** is a text format for data that both programs and people can read ([What is JSON?](https://aws.amazon.com/documentdb/what-is-json/), checked 2026-10-24). It's the AWS CLI's default output ([Setting the output format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html)) and the format of AWS's permission documents, called policies (Module 04).

![A made-up bakery order in JSON, with each part labeled: object, name-value pair, number, true-or-false value, array, nested object and null.](../../images/01-05-json-anatomy.svg)

*Notice that every name is in double quotes, and a colon always separates a name from its value.*

**Long description.** The whole order is one object in curly braces. `"order_id": "1042"` is a name-value pair, with commas between pairs; its value is text, in quotes. `"cupcakes": 14` is a number, without quotes. `"paid": true` is a true-or-false value. `"toppings": ["sprinkles", "lemon icing"]` is an array. `"customer"` holds a nested object with a name and a pickup day. `"note": null` means no value, and as the last pair it has no comma after it.

So a **JSON object**, in curly braces, is a set of **name-value pairs**, and an **array**, in square brackets, is a list of values in order. Text goes in double quotes; numbers, `true`, `false` and `null` don't. Commas separate items, with none after the last. Nesting one object inside another shows what belongs together, and indenting is only for people: programs ignore spaces. **YAML** (Module 08) writes the same kind of data without braces and quotes, and there the indentation does carry meaning.

> **Example:** read a policy from the outside in, shape first.
>
> ```json
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {"Effect": "Allow", "Action": ["s3:GetObject", "s3:PutObject"], "Resource": "arn:aws:s3:::bakery-menu-photos/*"},
>     {"Effect": "Deny", "Action": "s3:DeleteObject", "Resource": "arn:aws:s3:::bakery-menu-photos/*"}
>   ]
> }
> ```
>
> The outer braces make one object with two names. `Version` is text, a date that labels the policy language: leave it as it is. `Statement` opens a square bracket, so it's a list; count the objects inside: two. The first allows a list of two actions, reading and uploading the bakery's menu photos; the second denies one, deleting them, so its `Action` is plain text, not a list.

> **Your turn:** `aws sts get-caller-identity` prints something like this. (a) How many name-value pairs are there? (b) Which value is the 12-digit account you're working in? (c) Is any value a list?
>
> ```json
> {"UserId": "AIDAEXAMPLE1234567890", "Account": "123456789012", "Arn": "arn:aws:iam::123456789012:user/lab-admin"}
> ```

<details><summary>Model answer</summary>

(a) **Three:** `UserId`, `Account` and `Arn`. (b) **`Account`**, an example number that also appears inside the `Arn`. (c) **No:** there are no square brackets. The account number is in quotes, so it's text.

</details>

## Summary

- **An API** is a fixed menu of requests one program can make of another. The console, the CLI and programs all use the same AWS APIs, and every request is signed and checked.
- **The command line** runs exactly what you type, at once. An AWS CLI command reads `aws`, the service, what to do, then arguments and options.
- **JSON** is names and values in curly-brace objects, with square-bracket arrays for lists, double quotes for text, and commas between items but not after the last.
- **To read JSON,** go from the outside in: shape first, then each name and value.

## Practice

1. **What comes back when a request to an AWS API isn't allowed?**

   A. Nothing at all\
   B. An error such as `AccessDenied`, and nothing is done\
   C. The result, with a warning

   <details><summary>Feedback</summary>

   **B is right.** The service checked the request and refused it.

   - **A is wrong.** A refusal is still a response.
   - **C is wrong.** A refused request isn't carried out.

   </details>

2. **Which of these is valid JSON?**

   A. `{'cupcakes': 14}`\
   B. `{"cupcakes": 14, "muffins": 4,}`\
   C. `{"cupcakes": 14, "muffins": 4}`\
   D. `{"cupcakes": 14 "muffins": 4}`

   <details><summary>Feedback</summary>

   **C is right.**

   - **A is wrong.** JSON needs double quotes.
   - **B is wrong.** No comma is allowed after the last pair.
   - **D is wrong.** A comma must separate the two pairs.

   </details>

3. **In `{"order_id": "1046", "customer": {"name": "Ana", "pickup": "Friday"}}`, where is the pickup day?**

   A. In the top-level object, next to `order_id`\
   B. Inside the nested `customer` object\
   C. In an array

   <details><summary>Feedback</summary>

   **B is right.** `pickup` sits inside the braces that are the value of `customer`.

   - **A is wrong.** The top level has only `order_id` and `customer`.
   - **C is wrong.** There are no square brackets, so there's no array.

   </details>

**Next:** [Everyday security](06-everyday-security.md).

## Where to check the current details

- [Command structure in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html), AWS CLI User Guide (checked 2026-10-24)
- [What is JSON?](https://aws.amazon.com/documentdb/what-is-json/), AWS (checked 2026-10-24)

---

"APIs, the command line and JSON" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
