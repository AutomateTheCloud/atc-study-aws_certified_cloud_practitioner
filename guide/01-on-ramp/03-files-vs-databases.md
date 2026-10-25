---
type: lesson
id: clf-01-03
title: "Files vs databases"
tasks: []
objectives: ["01.03a"]
reader: "Adult studying alone, new to IT, who has read lessons 01.01 and 01.02 or tested out of them; about 15 minutes; works on a phone"
prerequisites: [clf-01-01, clf-01-02]
terms_introduced: [file, folder, file system, lost update, database, database engine, relational database, table, row, column, query, SQL, transaction, key-value database, document database]
pillars: []
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/cloud-file-storage/"
  - "https://aws.amazon.com/rds/what-is-a-relational-database/"
  - "https://aws.amazon.com/nosql/key-value/"
---

# Keep whole things in files; keep records that many people search and change in a database

A file is a named piece of data, such as a photo, that a program opens and saves as a whole. A database is a store of many small records, run by a program that lets many people change them at once and answers questions about them.

**For:** an adult studying alone, new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on lessons [01.01](01-computers-and-servers.md) and [01.02](02-networks-ip-dns-https.md).

## Test out: do you already know this?

Answer without looking anything up. If you get all three right, and didn't guess, skip to [Data centers and virtualization](04-data-centers-and-virtualization.md).

1. The bakery keeps all its orders in one spreadsheet file that three staff edit. Name two things that can go wrong.
2. In a database table, what is a row, and what is a column?
3. Should the bakery keep its cake photos in files or in a database? And its orders? Say why.

<details><summary>Answer key</summary>

1. Any two: one person's save wipes out another's changes; a question means reading the whole file; nothing stops a wrong date; a crash mid-save can damage it.
2. A **row** is one record, such as an order; a **column** is one fact every record has, such as the pickup date.
3. **Photos in files:** each is one whole thing. **Orders in a database:** many small records, searched and changed by many people.

</details>

## Warm-up: what you already know

1. From lesson 01.02: an order travels to the bakery's server over HTTPS. Once the server saves it, does HTTPS still protect it?

<details><summary>Feedback</summary>

1. **No.** HTTPS protects data while it travels. Protecting stored data is a separate job, which lesson 01.06 introduces.

</details>

## What you'll learn

By the end, you can explain how a database differs from a file, and say which one fits a kind of data (objective 01.03a).

Guess before you read on: is a spreadsheet a database?

## The big picture: the same orders, kept two ways

![The question "Which orders are for pickup on December 24?" answered two ways: a program reading every order file in a folder, or one query to a database engine that returns the matching rows.](../../images/01-03-big-picture.svg)

*Notice who does the searching: with files, your program; with a database, the database.*

**Long description.** Left, files: a program opens each of three order files in a folder in turn. Right, highlighted, a database: a table named orders, with the columns order_id, cake, pickup_date and customer_id and one row per order; one query goes to the database engine, which returns the two rows for December 24. The orders are made up.

## A file is opened and saved as a whole

A **file** is a named piece of data in storage, such as `birthday-cake.jpg`, and a **folder** holds files and other folders. The operating system keeps them in a **file system**, a tree of folders and files ([What is cloud file storage?](https://aws.amazon.com/what-is/cloud-file-storage/), checked 2026-10-24). Files are the right home for **whole things**, such as a photo or a menu PDF: nobody edits half a photo.

Files struggle when many people change many small records. Say Sam and Lee both open `orders.xlsx` at 9:00, each getting a copy in memory. Sam changes order 1041 and saves; Lee adds order 1044 and saves a minute later, replacing the whole file. Sam's change is gone without a warning: a **lost update**. A shared file also has to be read in full to answer any question, nothing checks what people type, and a crash mid-save can damage it.

## A database puts one program in charge of the data

A **database** puts one program, the **database engine** (such as PostgreSQL or MySQL), in charge. Nobody else opens its files: programs send it requests over the network, such as to port 5432 for PostgreSQL.

Most business data lives in **relational databases**, which keep data in **tables**: each **row** is one record, and each **column** one fact about it. Every row has a key no other row shares, such as the order number, and a column can hold another table's key to link them, as each order points to its customer ([What is a relational database?](https://aws.amazon.com/rds/what-is-a-relational-database/), checked 2026-10-24). A **query** is a question sent to the database, and **SQL** is the standard language for writing them:

```sql
SELECT order_id, cake FROM orders WHERE pickup_date = '2026-12-24';
```

The engine also fixes the shared-file problems:

- **Many people at once.** Each change touches only the rows it names, so Sam's and Lee's changes both survive.
- **Rules.** A date column accepts only dates, and no two orders can share an order number.
- **All or nothing.** A **transaction** groups changes, such as "save the order and record the payment": either all are saved or none are, even if the power fails halfway.

> **Misconception:** "A spreadsheet is a database." It isn't: it's a file. Online spreadsheets merge several people's edits, but they don't enforce column types and unique keys, make changes all-or-nothing, or answer programs' queries the way a database engine does. The mix-up is easy because both show rows and columns. What makes a database is the program in charge of the data.

## Not every database uses tables

Relational databases fit records that link, like customers and orders. A **key-value database** stores each item under a unique key and fetches it by that key, very fast ([What is a key-value database?](https://aws.amazon.com/nosql/key-value/), checked 2026-10-24); the bakery's website keeps each shopping cart this way, under a cart ID. A **document database** stores each record as a self-contained document, usually in JSON (lesson 01.05), and different documents can have different fields. Every kind still has an engine in charge.

> **Example:** on AWS, the bakery's cake photos are whole things, so they're kept as objects in Amazon S3. Orders and customers are linked records that staff and the website change at once: a relational database, Amazon RDS. Shopping carts are always fetched by one key: a key-value database, Amazon DynamoDB. Module 05 teaches all three.

> **Your turn:** the bakery keeps one allergy warning per cake, which the website shows next to each cake and staff update when a recipe changes. File or database? Why?

<details><summary>Model answer</summary>

**A database.** It's many small records, one per cake, changed by staff while the website reads them. A table with one row per cake fits, beside the orders.

</details>

## Summary

- **Keep whole things in files,** opened and saved as a whole.
- **Shared files break as use grows:** lost updates, slow questions, no rules on the data, damage from a crash.
- **A database puts one engine in charge.** It keeps records in tables, answers SQL queries, lets many people change records at once, and makes transactions all-or-nothing. A spreadsheet is a file, not a database.
- **Not every database uses tables:** key-value and document databases store other shapes.

## Practice

1. **Which of these belongs in a database rather than a file?**

   A. A video of a cake being decorated\
   B. The list of who has booked each baking class, which staff and customers change online\
   C. The signed lease for the shop

   <details><summary>Feedback</summary>

   **B is right.** Many small records, changed by several people at once.

   - **A is wrong.** A video is one whole thing.
   - **C is wrong.** A lease is one whole document, read, not edited in parts.

   </details>

2. **A teammate says: "Our spreadsheet has rows and columns, so it's a database." What's missing?**

   A. Nothing: rows and columns make a database\
   B. An engine in charge of the data, enforcing rules and all-or-nothing changes\
   C. A file format

   <details><summary>Feedback</summary>

   **B is right.** The engine makes it a database, not the look of the data.

   - **A is wrong.** A spreadsheet is a file that looks like a table.
   - **C is wrong.** A spreadsheet already has one; that's why it's a file.

   </details>

3. **(From lesson 01.02.) The website sends orders to the database engine on port 5432. What does the port number tell the server?**

   A. Which computer the data is for\
   B. Which program on the computer the data is for\
   C. That the data is encrypted

   <details><summary>Feedback</summary>

   **B is right:** the PostgreSQL engine, not the web server on 443.

   - **A is wrong.** The IP address picks the computer.
   - **C is wrong.** A port number says nothing about encryption.

   </details>

**Next:** [Data centers and virtualization](04-data-centers-and-virtualization.md).

## Where to check the current details

- [What is a relational database?](https://aws.amazon.com/rds/what-is-a-relational-database/), AWS (checked 2026-10-24)
- [What is a key-value database?](https://aws.amazon.com/nosql/key-value/), AWS (checked 2026-10-24)

---

"Files vs databases" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
