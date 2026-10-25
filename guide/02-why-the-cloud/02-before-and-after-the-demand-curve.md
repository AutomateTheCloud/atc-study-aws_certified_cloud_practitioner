---
type: lesson
id: clf-02-02
title: "Before and after: the demand curve"
tasks: ["1.1", "1.4"]
objectives: ["02.02a"]
reader: "Adult studying alone, possibly new to IT; about 35 minutes; works on a phone"
prerequisites: [clf-02-01]
terms_introduced: [demand, capacity, demand curve, idle capacity, lost sales, fixed expense, variable expense, capital expense, operating expense, economies of scale]
pillars: [cost-optimization, reliability]
facts_checked: 2026-10-23
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://aws.amazon.com/what-is-cloud-computing/"
  - "https://aws.amazon.com/pricing/"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html"
---

# Owning equipment means guessing your demand; the cloud lets capacity follow it

When you buy your own servers, you must guess how much you will need, and the guess is wrong somewhere: you either pay for idle equipment or turn customers away. In the cloud, you add and remove capacity as demand changes, so your costs follow your use. One picture, the demand curve, explains this and most of the cloud's other advantages.

**For:** an adult studying alone, possibly new to IT, who wants to understand AWS and use it safely. **Time:** about 35 minutes. Reading works on a phone.

**Before you start:** read [What cloud computing is](01-what-cloud-computing-is.md) first. This lesson uses the bakery's made-up facts from the [module brief](00-brief.md); the table you need is repeated below.

## Warm-up: from the last lesson

1. Name the three features that together make something cloud computing.
2. The bakery runs its website on three servers in a room behind the shop. Which deployment model is that?

<details><summary>Feedback</summary>

1. On demand, over the internet, and pay as you go. If you can't say all three, reread the [three features](01-what-cloud-computing-is.md#three-features-together-make-something-cloud-computing).
2. On-premises: every part runs in a building the bakery controls.

</details>

## What you'll learn

By the end of this lesson, you can:

- read a demand curve and point to the idle cost and the lost sales (objective 02.02a);
- explain the difference between fixed and variable expense, and why variable isn't automatically cheaper;
- link each of AWS's six advantages of cloud computing to the same picture.

Try these before you read on. Guessing is fine.

1. The bakery buys enough servers for its busiest day of the year. What problem does it have in January?
2. Does moving to the cloud always lower an organization's monthly bills?

## The big picture: the bakery's year as a demand curve

**Demand** is how much work customers ask the system to do; for the bakery, orders per hour. **Capacity** is how much work the system can do. A **demand curve** plots demand over time.

The chart shows the bakery's year. Each column is the number of servers needed to handle the busiest hour of that month. The flat line is the three servers the bakery owns.

![Column chart of servers needed each month against a flat line at the 3 servers the bakery owns. Idle capacity fills the columns up to the line in eleven months; in December the column rises 3 servers above the line.](../../images/02-02-demand-vs-owned.svg)

*Notice the two kinds of gap. In most months, part of what the bakery owns sits idle (the light part of each column, below the line). In December, demand rises above the line: customers arrive and the site can't serve them (the top part of the column).*

**Long description.** A column chart with months January to December along the bottom and servers (0 to 6) up the side. A flat line at 3 marks the servers owned. Each column shows servers needed: 1 in January, February, July and August; 2 in March to June, September and October; 3 in November; 6 in December. Up to the line, each column has two parts: servers owned and used, and servers owned but idle. In December, the column goes 3 servers above the line; that part is labeled lost sales. The table below gives the same data.

The same data as a table, with the bakery's made-up facts:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orders in the busiest hour | 10 | 20 | 30 | 30 | 40 | 30 | 20 | 20 | 30 | 40 | 60 | 120 |
| Servers needed (20 orders an hour each) | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 3 | 6 |
| Servers owned | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

## Key terms (skip if you know them)

- **Idle capacity:** capacity you pay for but don't use. On the chart, the light part of a column, below the line.
- **Lost sales:** customers you can't serve because demand is above capacity. On the chart, the part of a column above the line.
- **Fixed expense:** a cost that stays the same however much you use, such as servers you have bought.
- **Variable expense:** a cost that rises and falls with how much you use, such as servers you rent by the hour.
- **Economies of scale:** the lower cost per unit that a very large operation can reach, because it buys, builds and runs things in bulk.

## Buying for the peak means paying for idle servers

If you own your servers, you must decide how many to buy before you know what demand will be. Suppose the bakery buys for its busiest hour of the year: six servers.

Then it can serve every December customer. But in January, it needs one server and owns six. Five sit idle. Across the year, it needs 25 server-months of capacity (add up the columns) and owns 72 (six servers for twelve months). It pays for 47 server-months that do nothing.

Idle servers still cost money: they were paid for, and they still need space and power. Lesson 02.04 looks at what goes into that cost.

## Buying for normal months turns customers away at the peak

Suppose instead the bakery buys for a normal busy month, as it actually did: three servers. Now idle capacity is smaller, but December is a problem.

In December's busiest hour, 120 customers try to order, and the servers can handle 60. At best, the extra 60 can't order. In practice, an overloaded website often slows down or fails for everyone, which is why the bakery's site crashes. Lost sales never appear on a bill, but the orders go to another bakery, and some customers may not come back.

**Any fixed number is a guess, and every guess is wrong somewhere.** Buy for the peak, and you pay for idle servers most of the year. Buy for the average, and you lose customers at the peak. AWS names the cloud's answer to this **Stop guessing capacity**, one of its six advantages of cloud computing ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)).

> **Your turn:** A ski-equipment rental shop has a website. Demand is high for three winter months and very low for the rest of the year. Sketch its demand curve in words, then describe what happens if it owns enough servers for (a) its busiest month and (b) its quietest month.

<details><summary>Model answer</summary>

The curve is low for nine months and high for three. (a) Bought for the busiest month: no lost sales, but most of the servers sit idle for nine months, and the shop pays for them anyway. (b) Bought for the quietest month: little idle capacity, but in the three busy months the site can't serve most customers, so the shop loses sales in exactly the months that matter most.

</details>

## In the cloud, capacity follows the curve

In the cloud, the bakery doesn't choose one number for the whole year. It rents what each month needs: one server in January, six in December. When demand drops, it removes servers and stops paying for them.

![Column chart of servers needed each month, with a dot on top of every column showing servers rented. The dots always sit exactly on the column tops.](../../images/02-02-capacity-in-cloud.svg)

*Notice that the servers rented (the dots) sit exactly on top of every column. There is no idle part and no part above what is rented: no idle servers and no lost sales.*

**Long description.** The same columns as the first chart: servers needed of 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3 and 6 from January to December. A dot on each column shows the servers rented, which equal the servers needed every month.

This picture is simplified. Real demand changes by the hour, and in the cloud you can follow it hour by hour, which saves more. And adding a server takes a few minutes, so real systems keep a little spare. Even so, capacity follows demand, instead of demand being forced to fit capacity.

What makes this possible is the definition from the last lesson. Because resources are **on demand**, the bakery can add servers within minutes. Because they are **pay as you go**, it stops paying when it removes them. Lesson 02.03 gives this ability its name, elasticity.

## Worked example: the bakery's year in numbers

An advisor would make this comparison for the owner. All the money figures are made up for teaching. To keep the comparison about the *shape* of demand, assume one server costs $150 a month either way, owned or rented. (In reality the prices differ; lesson 02.04 and [Simulation S1](07-sim-demand-curve.md) look at that.)

**Step 1: what the bakery pays now.** It owns 3 servers for 12 months: 36 server-months × $150 = **$5,400 a year**, whatever happens.

**Step 2: how much of that is idle.** Add up the servers actually used each month, capped at the 3 it owns: 1 + 1 + 2 + 2 + 2 + 2 + 1 + 1 + 2 + 2 + 3 + 3 = 22 server-months. It pays for 36, so 36 − 22 = **14 server-months are idle: $2,100 a year** for nothing.

**Step 3: what it loses at the peak.** Suppose December has about 10 hours when demand is above 60 orders an hour, with about 40 extra orders in each (made-up). That's about 400 orders that can't be placed. At $20 an order, that's about **$8,000 of lost sales**, more than the bakery spends on servers in a year. If the site crashes completely, the loss is larger.

**Step 4: the same year in the cloud.** It rents exactly what each month needs: 25 server-months (add up all the columns) × $150 = **$3,750 a year**, and it serves every December customer.

**Step 5: what the advisor tells the owner.** "With these assumptions, renting would cost about $1,650 a year less than owning, and you would stop losing about $8,000 of December orders. The bigger gain is the orders, not the server bill. These are rough numbers; before deciding, we should check real prices and real order data."

Notice the advisor's thinking: count what is paid for, count what is used, and look for the cost that doesn't appear on any bill (the lost orders). Then say which numbers are assumptions.

> **Your turn:** The bakery's owner says: "Let's move to the cloud, but rent six servers all year, so we're safe in December." Using the same $150 a month, what would that cost? What has the owner misunderstood?

<details><summary>Model answer</summary>

6 servers × 12 months × $150 = **$10,800 a year**: twice what the bakery pays now. The owner has kept the old habit of buying for the peak. The cloud only saves money if you remove capacity when demand falls. Renting the peak all year turns idle equipment into idle rent.

</details>

The chart puts the four options side by side.

![Horizontal bar chart of a year's cost for four options. Own 3 servers: $5,400 of server cost plus about $8,000 of lost sales. Own 6 servers: $10,800. Cloud, renting 6 all year: $10,800. Cloud, renting what each month needs: $3,750.](../../images/02-02-annual-cost.svg)

*Notice that today's real cost is the longest bar once lost sales are counted, and that the cloud gives the shortest bar only when the bakery rents what each month needs.*

**Long description.** Four horizontal bars, one for each option, measured in dollars a year. Own 3 servers (today): $5,400 of server cost plus about $8,000 of lost sales, about $13,400 in all. Own 6 servers: $10,800. Cloud, renting 6 servers all year: $10,800. Cloud, renting what each month needs: $3,750.

## Fixed expense becomes variable expense, which isn't the same as cheaper

AWS's first advantage of cloud computing is **Trade fixed expense for variable expense**. Instead of paying in advance for data centers and servers you may or may not use, you pay when you use resources, and for how much you use ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)). The chart shows the difference for the bakery, month by month.

![Line chart of the bakery's monthly server cost. Owning 3 servers is a flat line at $450 a month. Renting what each month needs moves between $150 and $900, following demand.](../../images/02-02-monthly-cost.svg)

*Notice that the variable line is below the fixed line in ten months, level with it in November, and twice as high in December. Over the year, the variable line adds up to less: $3,750 against $5,400.*

**Long description.** A line chart, January to December, in dollars a month. Owning 3 servers: $450 every month. Renting what each month needs: $150, $150, $300, $300, $300, $300, $150, $150, $300, $300, $450 and $900.

| | Fixed expense (owning) | Variable expense (cloud) |
|---|---|---|
| When you pay | Up front, before you know your demand | As you use resources |
| What the amount depends on | The capacity you bought | The capacity you use |
| Idle capacity | Paid for anyway | Paid for only if you leave it running |
| Risk | Guessing wrong: idle servers or lost sales | Forgetting to remove what you don't need |
| Where it suits best | Demand that is steady and predictable | Demand that changes, or isn't known yet |

**What's the same:** both pay for capacity. **What differs:** whether the bill follows your use. **The principle:** variable expense saves money when your use varies and you actually reduce capacity when demand falls.

You may see the same idea called **CapEx versus OpEx** in other material. **Capital expense (CapEx)** is money spent up front on things you own, like servers. **Operating expense (OpEx)** is money spent on running costs, like rent and bills. AWS's own wording is fixed versus variable expense. Lesson 02.04 shows why the two pairs of words answer different questions.

### The cloud doesn't always cut operating costs

A popular claim is that moving to the cloud reduces operating costs. That isn't right as a general rule. What the cloud changes is the *kind* of cost: an up-front purchase becomes a running bill. Your operating bills often go *up*, because costs that used to be purchases now arrive every month. Whether your *total* cost falls depends on your demand and your habits.

The belief is tempting because the cloud often does save money, as it did for the bakery. But the owner's six-servers-all-year plan above costs twice as much as owning. A system with steady, predictable demand gains less from paying by use. AWS offers lower prices in exchange for a commitment to steady use; module 11 covers those options.

> **Check:** Which statement best describes "trade fixed expense for variable expense"?
>
> A. The cloud always costs less than owning servers.\
> B. You pay for resources as you use them, instead of paying up front for capacity you might not use.\
> C. You pay a fixed monthly fee to a cloud provider instead of buying servers.\
> D. Your operating expenses go down because the provider pays for the servers.

<details><summary>Feedback</summary>

**B is right.** The trade is about *when* and *on what basis* you pay: as you use, not up front.

- **A is wrong.** Paying by use can cost more, for example if you keep peak capacity running all year.
- **C is wrong.** A fixed monthly fee is still a fixed expense. Variable means the amount changes with use.
- **D is wrong.** Running bills often rise, because purchases become monthly costs. The total may or may not fall.

</details>

## Economies of scale: a very large provider can charge less per unit

AWS's second advantage is **Benefit from massive economies of scale**. AWS combines the usage of hundreds of thousands of customers, which lets it buy and run equipment at a scale no single customer could. AWS says this leads to lower pay-as-you-go prices ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html); [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)).

Economies of scale affect the *price of each unit* of capacity: on the chart, how much each column costs. They don't change the shape of the curve. That is why the worked example used the same price for owned and rented servers: following the curve saves money even before economies of scale.

AWS's pricing also lowers the price per unit for some services as you use more, which it describes as paying less by using more ([AWS Pricing](https://aws.amazon.com/pricing/)). Module 11 shows examples.

## Six advantages, one picture

AWS lists six advantages of cloud computing in its Overview of Amazon Web Services whitepaper ([six advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)). The headings are AWS's; the links to the demand curve are ours.

| AWS's advantage | What it means on the demand curve |
|---|---|
| **Trade fixed expense for variable expense** | You pay for the columns, not the flat line. |
| **Benefit from massive economies of scale** | Each column costs less, because the provider buys and runs at huge scale. |
| **Stop guessing capacity** | There is no flat line to choose, so no wrong guess. |
| **Increase speed and agility** | New capacity arrives in minutes, not weeks, so capacity can change when demand does. AWS describes the time to get resources falling from weeks to minutes. |
| **Stop spending money running and maintaining data centers** | The bakery's back room, power and repairs are the provider's job, not the bakery's. |
| **Go global in minutes** | If the bakery started selling in another country, it could place servers near those customers in minutes, with a second curve for them. |

The exam asks about these advantages under task [1.1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.1) (benefits) and task [1.4](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html#cloud-practitioner-02-task1.4) (cloud economics). Lesson 02.03 teaches you to tell the related benefit terms apart in a scenario.

> **Your turn:** Without looking at the table, explain to the bakery owner in three sentences how "stop guessing capacity" would change December.

<details><summary>Model answer</summary>

Today you had to choose a number of servers years ago, and in December that number is too small, so the site crashes. In the cloud, you add servers within minutes when December orders rise, and remove them when they fall. You don't have to predict December in advance, and you don't pay for the extra servers the rest of the year.

</details>

## In real work: this is the cost optimization pillar

The AWS Well-Architected Framework, which lesson 02.05 introduces, turns this lesson into guidance:

- Its general design principles start with "[Stop guessing your capacity needs](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)".
- Its cost optimization pillar includes the design principle "[Adopt a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)". It means letting what you pay for track what the business needs right now, rather than what it might need at its busiest. The Framework's example is turning off development and test systems outside working hours. If they run 40 hours of a 168-hour week, that saves about 75% ([cost optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)).

The worked example's warning matters most at work. The cloud *allows* you to pay for what you use, but it doesn't *make* you. Teams that keep peak capacity running all the time end up paying more. For the same reason, every lab in this guide ends by deleting what it created. The reliability pillar cares about this picture too: a site that crashes at its peak isn't doing its job.

## Summary

- **A demand curve** shows demand over time. Against a fixed amount of owned capacity, it shows two costs: **idle capacity** below the line, and **lost sales** above it.
- **Buying for the peak** wastes money on idle servers; **buying for the average** loses customers at the peak. Any fixed number is a guess.
- **In the cloud, capacity follows the curve**, because resources are on demand and paid for as you go.
- **Fixed expense becomes variable expense.** That is not the same as cheaper: it saves money when use varies and you remove what you don't need.
- **Economies of scale** lower the price of each unit of capacity; they don't change the shape of the curve.
- **AWS's six advantages** all follow from the same picture.

**For your recommendation:** note the bakery's idle cost, its lost December orders, and the risk of keeping peak capacity running all year.

## Practice

1. **On a demand curve with a flat line for owned servers, what does the area where demand is above the line represent?**

   A. Idle capacity\
   B. Lost sales\
   C. Economies of scale\
   D. Variable expense

   <details><summary>Feedback</summary>

   **B is right.** Above the line, customers want more than the servers can handle, so some can't be served.

   - **A is wrong.** Idle capacity is *below* the line: owned but unused.
   - **C is wrong.** Economies of scale are about the price per unit, which the curve doesn't show.
   - **D is wrong.** Variable expense is a way of paying; it isn't an area on this chart.

   </details>

2. **A company's website has the same steady demand every hour of every day, and it already owns enough servers for it. Which statement is most accurate?**

   A. Moving to the cloud will certainly lower its costs, because the cloud always costs less.\
   B. Its main benefit from the cloud's variable expense is small, because there is little idle capacity to remove.\
   C. It has a large lost-sales problem.\
   D. It should rent its peak capacity all year in the cloud.

   <details><summary>Feedback</summary>

   **B is right.** Paying by use saves the most when use varies. With steady demand, there is little to remove. (Other advantages, such as not running a data center, may still apply.)

   - **A is wrong.** The cloud doesn't always cost less; it depends on demand and habits.
   - **C is wrong.** Demand never exceeds its capacity, so there are no lost sales.
   - **D is wrong.** With steady demand, the "peak" is the same as normal use, so this adds nothing; and as a habit, renting the peak all year wastes money.

   </details>

3. **Using the bakery's table, how many server-months of capacity would the bakery pay for if it owned four servers instead of three? How many would be idle?**

   <details><summary>Feedback</summary>

   It would pay for 4 × 12 = **48** server-months. Usage capped at 4: 1 + 1 + 2 + 2 + 2 + 2 + 1 + 1 + 2 + 2 + 3 + 4 = 23, so **25** would be idle. December would still be short by 2 servers. A fourth server nearly doubles the idle capacity (from 14 to 25 server-months) and still doesn't fix the peak.

   </details>

4. **Explain, in two sentences, why "the cloud cuts operating costs" is misleading.**

   <details><summary>Feedback</summary>

   **Model answer:** The cloud turns up-front purchases into running bills, so operating costs often rise even when the total falls. Whether the total falls depends on whether demand varies and whether you remove capacity you don't need.

   </details>

5. **From the last lesson: a company runs its website on AWS and its stock-control system on servers in its warehouse, and the two exchange data. Which deployment model is this?**

   <details><summary>Feedback</summary>

   **Hybrid.** Some parts run in the cloud and some on-premises, and they're connected. If you weren't sure, review [the three deployment models](01-what-cloud-computing-is.md#the-three-deployment-models-are-cloud-hybrid-and-on-premises).

   </details>

**Practice more:** [Simulation S1: the demand curve](07-sim-demand-curve.md) lets you finish the bakery's cost comparison yourself.

**Next:** [Telling the benefits apart](03-telling-the-benefits-apart.md).

## Where to check the current details

- [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html), Overview of Amazon Web Services whitepaper (checked 2026-10-23)
- [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/), AWS (checked 2026-10-23)
- [AWS Pricing](https://aws.amazon.com/pricing/), AWS (checked 2026-10-23)
- [General design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html), AWS Well-Architected Framework (checked 2026-10-23)
- [Cost optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html), AWS Well-Architected Framework (checked 2026-10-23)

---

"Before and after: the demand curve" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
