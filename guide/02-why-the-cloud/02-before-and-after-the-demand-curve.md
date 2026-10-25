---
type: lesson
id: clf-02-02
title: "Before and after: the demand curve"
tasks: ["1.1", "1.4"]
objectives: ["02.02a"]
reader: "Adult studying alone, possibly new to IT; about 25 minutes; works on a phone"
prerequisites: [clf-02-01]
terms_introduced: [demand, capacity, demand curve, idle capacity, lost sales, server-month, fixed expense, variable expense, economies of scale]
pillars: [cost-optimization, reliability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://aws.amazon.com/what-is-cloud-computing/"
  - "https://aws.amazon.com/pricing/"
---

# Owning equipment means guessing your demand; the cloud lets capacity follow it

When you buy your own servers, you guess how many you'll need, and the guess is wrong somewhere: you pay for idle equipment or turn customers away. In the cloud you add and remove capacity as demand changes, so your costs follow your use, and one picture, the demand curve, explains most of AWS's six advantages.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 25 minutes. Reading works on a phone.

**Before you start:** read [What cloud computing is](01-what-cloud-computing-is.md) first.

## Warm-up: from the last lesson

1. Name the three features that together make something cloud computing.
2. The bakery runs its website on three servers in a room behind the shop. Which deployment model is that?

<details><summary>Feedback</summary>

1. On demand, over the internet, and pay as you go. If you missed one, reread [the three features](01-what-cloud-computing-is.md#three-features-together-make-something-cloud-computing).
2. On-premises: every part runs in a building the bakery controls.

</details>

## What you'll learn

By the end of this lesson, you can read a demand curve and point to the idle cost and the lost sales (objective 02.02a), explain why variable expense isn't automatically cheaper than fixed expense, and link AWS's six advantages of cloud computing to the same picture.

Try this before you read on: does moving to the cloud always lower an organization's monthly bills?

## The big picture: the bakery's year as a demand curve

**Demand** is how much work customers ask a system to do; for the bakery, orders per hour. **Capacity** is how much work the system can do. A **demand curve** plots demand over time. In the chart, each column is the number of servers the busiest hour of a month needs, and the flat line is the three servers the bakery owns (one server handles about 20 orders an hour; all figures are made up).

![Column chart of servers needed each month against a flat line at the 3 servers the bakery owns. Idle capacity fills the columns up to the line in eleven months; in December the column rises 3 servers above the line.](../../images/02-02-demand-vs-owned.svg)

*Notice the two kinds of gap. In most months, part of what the bakery owns sits idle (below the line). In December, demand rises above the line, and customers arrive whom the site can't serve.*

**Long description.** A column chart, January to December, of servers needed (the values in the table below) against a flat line at 3 servers owned. Below the line, each column splits into servers owned and used and servers owned but idle. In December the column goes 3 servers above the line, labeled lost sales.

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orders in the busiest hour | 10 | 20 | 30 | 30 | 40 | 30 | 20 | 20 | 30 | 40 | 60 | 120 |
| Servers needed | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 6 |
| Servers owned | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

## Any fixed amount of capacity is a guess

The chart shows two costs of owning. **Idle capacity** is capacity you pay for but don't use: the part of each column below the line. **Lost sales** are customers you can't serve because demand is above capacity: the part above the line. Idle servers still cost money and need space and power. Lost sales never appear on a bill, and an overloaded site often fails for everyone.

Moving the line only trades one gap for the other. Buy six servers for December, and in January five sit idle. Keep three, as the bakery did, and December's extra customers can't order. AWS names the cloud's answer **Stop guessing capacity**, one of its six advantages ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)).

## In the cloud, capacity follows the curve

In the cloud, the bakery doesn't pick one number for the year. It rents what each month needs, one server in January and six in December, and removes servers when demand drops. Because resources are **on demand**, it can add servers within minutes; because they're **pay as you go**, it stops paying when it removes them. Lesson 02.03 calls this ability elasticity.

![Column chart of servers needed each month, with a dot on top of every column showing servers rented. The dots always sit exactly on the column tops.](../../images/02-02-capacity-in-cloud.svg)

*Notice that the servers rented (the dots) sit on top of every column: no idle part, and nothing above what is rented.*

**Long description.** The same columns as the first chart, with a dot on each showing servers rented, equal to servers needed every month.

> **Example:** count in **server-months**, one server running for one month, and price one at a made-up $150, owned or rented. Owning 3 servers costs 36 server-months, $5,400 a year, whatever happens; the bakery uses only 22 of them (capping December at the 3 it owns), so 14 sit idle. Renting what each month needs costs 25 server-months, $3,750, and serves every December customer, whose lost orders the bakery estimates at about $8,000 a year today. The bigger gain is the orders, not the server bill.

> **Your turn:** the owner says, "Let's move to the cloud, but rent six servers all year, so we're safe in December." At $150 a server-month, what would that cost, and what has the owner misunderstood?

<details><summary>Model answer</summary>

6 × 12 × $150 = **$10,800 a year**, twice what the bakery pays now. The owner has kept the old habit of buying for the peak. The cloud saves money only if you remove capacity when demand falls; renting the peak all year turns idle equipment into idle rent.

</details>

## Fixed expense becomes variable expense, which isn't the same as cheaper

AWS's first advantage is **Trade fixed expense for variable expense**: instead of paying in advance for data centers and servers you may not use, you pay when you use resources, for how much you use ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)). A **fixed expense** stays the same however much you use, like servers you've bought. A **variable expense** rises and falls with use, like servers rented by the hour.

![Line chart of the bakery's monthly server cost. Owning 3 servers is a flat line at $450 a month. Renting what each month needs moves between $150 and $900, following demand.](../../images/02-02-monthly-cost.svg)

*Notice that the variable line is below the fixed line in ten months and twice as high in December, yet adds up to less over the year: $3,750 against $5,400.*

**Long description.** A line chart, January to December, in dollars a month. Owning 3 servers: $450 every month. Renting what each month needs: $150, $150, $300, $300, $300, $300, $150, $150, $300, $300, $450 and $900.

| | Fixed expense (owning) | Variable expense (cloud) |
|---|---|---|
| When you pay | Up front, before you know your demand | As you use resources |
| Idle capacity | Paid for anyway | Paid for only if you leave it running |
| Risk | Guessing wrong: idle servers or lost sales | Forgetting to remove what you don't need |
| Suits best | Steady, predictable demand | Demand that changes, or isn't known yet |

You may also meet the same idea as capital expense versus operating expense; lesson 02.04 shows why those words answer a different question.

### "The cloud always cuts operating costs" is wrong

A popular claim is that moving to the cloud reduces operating costs. As a general rule, that's not right. What the cloud changes for certain is the *kind* of cost: an up-front purchase becomes a running bill, so running bills often go *up*, and the total falls only when use varies and you actually remove capacity you don't need. The owner's six-servers-all-year plan costs twice as much as owning, and steady demand gains little from paying by use (AWS offers lower prices for committed steady use, which Module 11 covers). The claim is tempting because the cloud often does save money, as it did for the bakery.

## Six advantages, one picture

AWS lists six advantages of cloud computing ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)). One of them needs a short explanation first; then the table links all six to the demand curve.

### Economies of scale: a very large provider can charge less per unit

**Economies of scale** are the lower cost per unit that a very large operation reaches by buying, building and running in bulk. AWS combines the usage of hundreds of thousands of customers and says this leads to lower pay-as-you-go prices ([What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)). On the chart, economies of scale change what each column costs, not the shape of the curve, which is why the example above saved money even at the same price per server. AWS's pricing also lowers the unit price for some services as you use more ([AWS Pricing](https://aws.amazon.com/pricing/)).

| AWS's advantage | What it means on the demand curve |
|---|---|
| **Trade fixed expense for variable expense** | You pay for the columns, not the flat line. |
| **Benefit from massive economies of scale** | Each column costs less, because the provider buys and runs at huge scale. |
| **Stop guessing capacity** | There's no flat line to choose, so no wrong guess. |
| **Increase speed and agility** | New capacity arrives in minutes, not weeks, so it can change when demand does. |
| **Stop spending money running and maintaining data centers** | The back room, power and repairs become the provider's job. |
| **Go global in minutes** | The bakery could place servers near customers in another country in minutes, with a second curve for them. |

## Summary

- **A demand curve** against owned capacity shows two costs: **idle capacity** below the line and **lost sales** above it. Any fixed amount is a guess.
- **In the cloud, capacity follows the curve**, because resources are on demand and paid for as you go.
- **Fixed expense becomes variable expense.** That isn't the same as cheaper: it saves money when use varies and you remove what you don't need.
- **Economies of scale** lower the price of each unit; they don't change the shape of the curve.
- **AWS's six advantages** all follow from the same picture.

## Practice

1. **On a demand curve with a flat line for owned servers, what does the area where demand is above the line represent?**

   A. Idle capacity\
   B. Lost sales\
   C. Economies of scale\
   D. Variable expense

   <details><summary>Feedback</summary>

   **B is right.** Above the line, customers want more than the servers can handle.

   - **A is wrong.** Idle capacity is *below* the line: owned but unused.
   - **C is wrong.** Economies of scale are about the price per unit, which the curve doesn't show.
   - **D is wrong.** Variable expense is a way of paying, not an area on the chart.

   </details>

2. **Which statement best describes "trade fixed expense for variable expense"?**

   A. The cloud always costs less than owning servers.\
   B. You pay for resources as you use them, instead of paying up front for capacity you might not use.\
   C. You pay a fixed monthly fee to a cloud provider instead of buying servers.\
   D. Your operating expenses go down because the provider pays for the servers.

   <details><summary>Feedback</summary>

   **B is right.** The trade is about *when* and *on what basis* you pay: as you use, not up front.

   - **A is wrong.** Paying by use can cost more, for example with peak capacity running all year.
   - **C is wrong.** A fixed monthly fee is still a fixed expense.
   - **D is wrong.** Running bills often rise, because purchases become monthly costs.

   </details>

3. **A company's website has the same steady demand every hour of every day, and it already owns enough servers for it. Which statement is most accurate?**

   A. Moving to the cloud will certainly lower its costs.\
   B. Its gain from the cloud's variable expense is small, because there is little idle capacity to remove.\
   C. It has a large lost-sales problem.\
   D. It should rent its peak capacity all year in the cloud.

   <details><summary>Feedback</summary>

   **B is right.** Paying by use saves the most when use varies. (Other advantages, such as not running a data center, may still apply.)

   - **A is wrong.** The cloud doesn't always cost less.
   - **C is wrong.** Demand never exceeds its capacity.
   - **D is wrong.** With steady demand, renting the "peak" all year adds nothing, and as a habit it wastes money.

   </details>

**Next:** [Telling the benefits apart](03-telling-the-benefits-apart.md).

## Where to check the current details

- [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html), Overview of Amazon Web Services whitepaper (checked 2026-10-23)
- [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/), AWS (checked 2026-10-23)
- [AWS Pricing](https://aws.amazon.com/pricing/), AWS (checked 2026-10-23)

---

"Before and after: the demand curve" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
