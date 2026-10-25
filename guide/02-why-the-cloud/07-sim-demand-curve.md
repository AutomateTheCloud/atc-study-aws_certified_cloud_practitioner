---
type: sim
id: clf-02-07
title: "Simulation S1: Finish the bakery's cost comparison"
tasks: ["1.1", "1.4"]
objectives: ["02.02a", "02.04a"]
reader: "Adult studying alone, possibly new to IT; about 30 minutes; paper or a spreadsheet helps"
prerequisites: ["clf-02-02", "clf-02-04"]
terms_introduced: [server-month]
pillars: [cost-optimization, sustainability]
lab: "S1"
rung: L2
mode: sim
free_plan: "not needed"
signup_path: "none"
time: "30 minutes"
cost: "$0 (no AWS account used)"
worst_case: "$0"
needs: []
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html"
---

# Simulation S1: Finish the bakery's cost comparison

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have read [02.02](02-before-and-after-the-demand-curve.md) and [02.04](04-what-a-data-center-really-costs.md). **Time:** about 30 minutes. **Cost:** $0; this simulation uses no AWS account.

**Goal:** finish a half-built cost comparison for the bakery's ordering site and make a recommendation to the owner. **End state:** a completed table and a three-sentence recommendation you can defend.

**Why this matters:** this is the comparison behind the Framework's general design principle "[Stop guessing your capacity needs](https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html)" and AWS's advantage of trading fixed expense for variable expense ([Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)). Doing the arithmetic yourself shows when that trade pays off, and when it doesn't.

## The scenario

The bakery's ordering site crashes every holiday season and sits nearly idle in January. Today it runs on three servers the bakery owns. The owner asks you: "Should I buy more servers, or move to the cloud?"

All numbers here are **made-up numbers for teaching**. They are not AWS prices or real costs; they are chosen to make the patterns easy to see.

**The rules of this simulation** (the bakery's facts from the [module brief](00-brief.md) and [02.02](02-before-and-after-the-demand-curve.md)):

- One server handles about 20 orders an hour. If the busiest hour has 30 orders, you need 2 servers; you can't run half a server.
- **Owning** a server costs $150 a month, every month, used or not. That figure includes its share of hardware, space, power, cooling, network, staff and licenses. (It is rounded up from the roughly $136 a server-month in [02.04](04-what-a-data-center-really-costs.md)'s example, to keep the arithmetic simple.)
- **Renting** in the cloud costs $250 per **server-month** (one server running for one month), only for the months you run it. Unlike in 02.02, renting costs more per unit than owning here.
- Orders the site can't take are lost. In 02.02 you estimated December's lost orders with three servers at about $8,000 (400 orders at $20).

## The data

| Month | Orders in the busiest hour | Servers needed |
|---|---|---|
| Jan | 10 | 1 |
| Feb | 20 | 1 |
| Mar | 30 | **?** |
| Apr | 30 | 2 |
| May | 40 | 2 |
| Jun | 30 | 2 |
| Jul | 20 | 1 |
| Aug | 20 | 1 |
| Sep | 30 | 2 |
| Oct | 40 | 2 |
| Nov | 60 | **?** |
| Dec | 120 | **?** |

![Column chart of servers needed each month: 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3 and 6, against flat lines at 3 owned servers today and 6 owned for the peak. Only December rises above the line at 3; every column sits at or below the line at 6.](../../images/02-07-demand.svg)

*Figure: the bakery's demand as servers needed each month, against two flat lines of owned capacity. Notice how far the higher line sits above the bars for eleven months of the year. (The chart already shows the answers to decision 1; cover it if you want to work them out first.)*

**Long description.** A bar chart with one bar per month, January to December, showing servers needed: 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3 and 6. A flat line at 3 shows today's three owned servers; only the December bar rises above it. A second flat line at 6 shows owning enough for the December peak; every bar sits at or below it, and most sit far below.

## Decisions

### Decision 1: fill in the missing months

Work out the servers needed for March, November and December.

<details><summary>Model answer</summary>

March: 30 ÷ 20 = 1.5, so **2**. November: 60 ÷ 20 = **3**. December: 120 ÷ 20 = **6**. Round up whenever there is a remainder; a site that is half a server short still drops orders. Over the year the bakery needs **25 server-months**.

</details>

### Decision 2: finish the comparison

Two rows are done. Complete the other two.

| Option | What it is | Yearly cost to run | Lost orders | Total | Idle server-months |
|---|---|---|---|---|---|
| A | Keep 3 owned servers | 3 × $150 × 12 = $5,400 | about $8,000 | about $13,400 | 14 |
| B | Own 6 servers, enough for the peak | 6 × $150 × 12 = $10,800 | $0 | $10,800 | 47 |
| C | Cloud, matching each month's need | **?** | **?** | **?** | **?** |
| D | Cloud, but 6 servers left running all year | **?** | **?** | **?** | **?** |

How row A works: the bakery is 3 servers short in December, which loses about $8,000 of orders. Capped at the 3 servers it owns, it uses 22 of its 36 owned server-months, leaving 14 idle.

<details><summary>Model answer</summary>

- **C:** 25 server-months × $250 = **$6,250**. Lost orders $0. Total **$6,250**. Idle server-months: **0**, because it runs exactly what each month needs.
- **D:** 6 × 12 = 72 server-months × $250 = **$18,000**. Lost orders $0. Total **$18,000**. Idle server-months: 72 − 25 = **47**, the same waste as owning six, at a higher price.

The chart puts the four options side by side.

![Horizontal bar chart of a year under each option. A, keep 3 owned servers: $5,400 to run plus about $8,000 of lost orders. B, own 6 servers: $10,800. C, cloud matching each month's need: $6,250. D, cloud with 6 servers left running all year: $18,000.](../../images/02-07-option-totals.svg)

*Notice that C is the shortest bar and D the longest: the same cloud price gives the cheapest and the most expensive option, depending only on whether the bakery scales down. A looks cheap until the lost orders are counted.*

**Long description.** Four horizontal bars, in dollars a year, made-up figures. A, keep 3 owned servers: $5,400 to run plus about $8,000 of lost orders, about $13,400 in all. B, own 6 servers, enough for the peak: $10,800. C, cloud, matching each month's need: $6,250. D, cloud, but 6 servers left running all year: $18,000.

</details>

### Decision 3: recommend an option

Write three sentences to the owner: which option, why, and the one condition that makes it work.

<details><summary>Model answer</summary>

Move to the cloud and match capacity to each month's need (option C): at about $6,250 a year it costs less than either owned option in this comparison, and the site stops dropping holiday orders. It works because the bakery pays only for the server-months it uses, instead of paying all year for a December peak. The condition is that the setup really scales down after the peak, ideally automatically; left at peak size (option D), the cloud would cost the most of all.

</details>

### Decision 4: change one assumption

Suppose a different business needs **6 servers every month**, all year. Work out the cost of owning six and of renting six in the cloud. What does the result tell you?

<details><summary>Model answer</summary>

Owning: 6 × $150 × 12 = **$10,800**. Cloud: 72 × $250 = **$18,000**. With these made-up prices, owning wins for flat demand, because there is no idle capacity to give back. The cloud doesn't automatically cost less: its savings in this simulation come from the bakery's demand going up and down, together with scaling down. Real prices could tip the result either way; Module 11 shows the discounts AWS offers for steady, committed use, and how to estimate real costs.

</details>

### Decision 5: look inside the $150

The $150 owned price bundles several costs. Name four of them, and one cost that this simulation leaves out entirely.

<details><summary>Model answer</summary>

Inside the $150: hardware, space, power, cooling, network, staff and licenses (any four). Left out: the weeks it takes to buy and install new servers, and the large up-front payment when you buy them, because the simulation spreads that cost evenly over the months. Both make owning look better here than it feels in practice, above all for option B, which needs three new servers before the next holiday peak.

</details>

### Decision 6: name the ideas

Which benefit from [02.03](03-telling-the-benefits-apart.md) does option C rely on, and which two Well-Architected pillars does the idle capacity in options B and D concern?

<details><summary>Model answer</summary>

Option C relies on **elasticity**: capacity follows demand up and down. Idle capacity concerns **cost optimization** (money spent on servers doing no work) and **sustainability** (hardware and energy used for nothing). See [02.05](05-the-well-architected-framework.md).

</details>

## Recap

Paying only for what you use beat owning in this comparison because the bakery's demand swings, and only when the bakery scaled down after the peak. With flat demand, or with the cloud left at peak size, the advantage disappeared. When someone says "the cloud is cheaper", ask two questions: how much does the demand move, and will we actually give capacity back?

**Next:** [the Module 02 mastery check](08-check.md). Before you take it, retry the practice questions at the end of [02.04](04-what-a-data-center-really-costs.md) and [02.05](05-the-well-architected-framework.md) without looking back.

---

"Simulation S1: Finish the bakery's cost comparison" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
