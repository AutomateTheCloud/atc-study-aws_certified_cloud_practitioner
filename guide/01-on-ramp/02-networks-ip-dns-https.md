---
type: lesson
id: clf-01-02
title: "Networks, IP addresses, DNS and HTTPS"
tasks: []
objectives: ["01.02a"]
reader: "Adult studying alone, new to IT, who has read lesson 01.01 or tested out of it; about 15 minutes; works on a phone"
prerequisites: [clf-01-01]
terms_introduced: [network, internet, router, internet service provider, packet, protocol, IP address, IPv4, IPv6, public IP address, private IP address, port, firewall, UDP, bandwidth, domain name, Domain Name System, DNS resolver, HTTP, URL, HTTPS, TLS, certificate]
pillars: [security]
facts_checked: 2026-10-24
sources:
  - "https://aws.amazon.com/what-is/computer-networking/"
  - "https://aws.amazon.com/what-is/tcp-ip/"
  - "https://aws.amazon.com/what-is/udp/"
  - "https://aws.amazon.com/what-is/ipv4/"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html"
  - "https://aws.amazon.com/route53/what-is-dns/"
  - "https://aws.amazon.com/compare/the-difference-between-https-and-http/"
  - "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html"
---

# A request finds a website in four steps: look up the name, travel to the address, secure the line, then ask

DNS turns the site's name into an IP address, the request crosses many networks to it, and HTTPS scrambles the conversation and proves the server is the real site.

**For:** an adult studying alone, new to IT, who wants to understand AWS and use it safely. **Time:** about 15 minutes. Reading works on a phone.

**Before you start:** this lesson builds on [Computers and servers](01-computers-and-servers.md) (clients, servers, requests).

## Test out: do you already know this?

Answer without looking anything up. If you get all three right, and didn't guess, skip to [Files vs databases](03-files-vs-databases.md).

1. What is an IP address for, and what does a port number add to it?
2. You type `bakery.example` into a browser. What does DNS do, and what doesn't it do?
3. HTTPS adds two things to plain HTTP. What are they?

<details><summary>Answer key</summary>

1. An **IP address** identifies a device so data can reach it; a **port** says which program on it the data is for.
2. It **turns the name into an IP address**. It doesn't hold or deliver the website.
3. **Encryption** and **proof of identity**.

</details>

## Warm-up: what you already know

1. From lesson 01.01: in a conversation between a client and a server, which one speaks first?

<details><summary>Feedback</summary>

1. **The client.** It sends a request; the server sends back a response.

</details>

## What you'll learn

By the end, you can explain how a request travels from a browser to a website: the DNS lookup, the networks it crosses, the IP address and port it goes to, and what HTTPS adds (objective 01.02a).

Guess before you read on: does the name `bakery.example` say where in the world the bakery's server is?

## The big picture: four steps to one web page

![Four numbered steps from a customer's phone to the bakery's web server: look up the name with DNS, travel across networks to the address and port, secure the line with the server's certificate, then ask and answer inside the encrypted connection.](../../images/01-02-big-picture.svg)

*Notice step 3. It happens before any page is sent, so even the first request travels scrambled.*

**Long description.** 1, look up: the phone asks DNS "where is bakery.example?" and gets 192.0.2.10. 2, travel: the request crosses the home network, the internet service provider and the internet, passed on by routers, to 192.0.2.10, port 443. 3, highlighted, secure: the server sends its certificate for bakery.example and both sides agree how to encrypt. 4, ask: the request and the reply travel inside the encrypted connection. The name and addresses are reserved for examples.

## The internet is a network of networks

A **network** is computers connected so they can exchange data, and the **internet** is a network of networks. At home your devices join through a **router**, which connects to your **internet service provider (ISP)**, which connects onward to other networks ([What is computer networking?](https://aws.amazon.com/what-is/computer-networking/), checked 2026-10-24).

Data travels in **packets**, small pieces that each carry their destination address, and routers pass them along. A **protocol** is a set of rules both ends follow: IP gets each packet to its address, and TCP puts packets back in order and resends lost ones ([What is TCP/IP?](https://aws.amazon.com/what-is/tcp-ip/)). **UDP** skips those checks, which is faster, so calls and games often use it ([What is UDP?](https://aws.amazon.com/what-is/udp/), both checked 2026-10-24). How much a connection carries each second is its **bandwidth**, in megabits or gigabits per second (Mbps, Gbps).

## An IP address says which computer; a port says which program

Every device on a network has an **IP address**. **IPv4** addresses are four numbers from 0 to 255, such as `192.0.2.10`; there are about 4.3 billion, all already handed out ([What is IPv4?](https://aws.amazon.com/what-is/ipv4/), checked 2026-10-24). **IPv6** addresses, such as `2001:db8::8a2e:370:7334`, are longer and vastly more plentiful.

Because IPv4 ran short, networks reuse **private IP addresses** from three ranges: addresses starting `10.`, `172.16.` to `172.31.`, and `192.168.` ([VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html), checked 2026-10-24). They work only inside one network, so millions of homes can all use `192.168.1.23`. A **public IP address** is unique on the whole internet; a home router usually shares one among its private devices.

A **port** number picks the program. Ports worth knowing: 443 (HTTPS), 80 (plain HTTP), 22 (SSH, remote sign-in to a Linux server), 3389 (RDP, remote desktop for Windows) and 5432 (PostgreSQL, the bakery's database). A **firewall** lets packets in or blocks them by address and port ([Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html), checked 2026-10-24). In firewall rules, `0.0.0.0/0` means every IPv4 address, and `/32` after an address means that one address alone (Modules 06 and 07).

> **Your turn:** classify each address as private or public: (a) `10.0.1.25`, (b) `192.168.0.4`, (c) `198.51.100.7`, a home router's internet-facing address. Which one could a customer on the internet send packets to?

<details><summary>Model answer</summary>

(a) and (b) are **private**: they start with `10.` and `192.168.`. (c) is **public**, and the only one reachable from the internet.

</details>

## DNS turns names into addresses

The **Domain Name System (DNS)** turns a **domain name** such as `bakery.example` into an IP address ([What is DNS?](https://aws.amazon.com/route53/what-is-dns/), checked 2026-10-24). Your device asks a **DNS resolver**, usually your ISP's, which finds the answer and saves it for a while. Saved copies make DNS fast, but a change of address takes time to reach everyone.

> **Misconception:** "The domain name is where the website lives." That's wrong. The name says nothing about where the server is: DNS only hands out the address the owner set, and the owner can change it at any time. It feels true because the name is all you ever see. Amazon Route 53, AWS's DNS service (Module 03), works the same way: it answers "where is it?" and doesn't store or deliver the site.

## HTTPS adds encryption and proof of identity to HTTP

The phone then talks to the web server in **HTTP**, the web's request-and-response protocol. A request names a web address, or **URL**, such as `https://bakery.example/order`, and an action: GET asks for something, PUT sends something to store.

Plain HTTP can be read or changed by anyone on the way. **HTTPS** runs HTTP inside **TLS** (Transport Layer Security), which adds two things ([HTTP vs HTTPS](https://aws.amazon.com/compare/the-difference-between-https-and-http/), checked 2026-10-24):

1. **Encryption:** anyone in between sees only scrambled data (lesson 01.06 explains encryption).
2. **Proof of identity:** the server shows a **certificate** proving it holds the name the customer typed, so an attacker can't pose as the bakery.

A browser's padlock proves those two things, not that the business is honest: a fraudster can get a certificate for a look-alike name. And HTTPS protects data only while it travels, not once it's stored.

> **Example:** a customer's browser says the bakery's site "can't be found", yet the server is running. Each step needs the one before, so a symptom points to a step: "can't be found" points to step 1, probably a wrong DNS record. A certificate warning points to step 3.

## Summary

- **Four steps:** look up the name, travel to the address, secure the line, then ask.
- **The internet connects networks.** Data travels as addressed packets that routers pass along.
- **An IP address picks the computer; a port picks the program,** and a firewall decides which packets get in. Private addresses work inside one network, public ones across the internet.
- **DNS turns names into addresses.** It doesn't hold the site, and changes take time to spread.
- **HTTPS is HTTP plus encryption and proof of identity,** for data in transit only.

## Practice

1. **Put these in the order they happen when you open a website:** (a) the server sends the page; (b) the phone asks DNS for the address; (c) the server shows its certificate; (d) packets travel to the server's IP address.

   <details><summary>Feedback</summary>

   **b, d, c, a.** The name becomes an address first, and the line is secured before any page is sent.

   </details>

2. **A firewall rule lets in port 22 from `0.0.0.0/0`. What does that allow?**

   A. Web visitors from anywhere\
   B. Remote sign-in (SSH) attempts from any IPv4 address on the internet\
   C. Remote sign-in from one address only\
   D. Nothing, because 22 is a private port

   <details><summary>Feedback</summary>

   **B is right,** and it's risky.

   - **A is wrong.** Web traffic uses 443 or 80.
   - **C is wrong.** One address would be written with `/32`.
   - **D is wrong.** Ports aren't private or public; addresses are.

   </details>

3. **The bakery moves its website from the back room to AWS. What has to change so customers can keep typing `bakery.example`?**

   A. The domain name\
   B. The address DNS gives out for the name\
   C. Nothing: DNS finds the server wherever it is

   <details><summary>Feedback</summary>

   **B is right.** The name stays; its DNS record points to the new address.

   - **A is wrong.** Customers would have to learn a new name.
   - **C is wrong.** DNS doesn't search; it gives the answer it was told to give.

   </details>

**Next:** [Files vs databases](03-files-vs-databases.md).

## Where to check the current details

- [What is DNS?](https://aws.amazon.com/route53/what-is-dns/), AWS (checked 2026-10-24)
- [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html), Amazon EC2 User Guide: common ports (checked 2026-10-24)

---

"Networks, IP addresses, DNS and HTTPS" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
