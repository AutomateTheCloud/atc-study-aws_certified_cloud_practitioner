---
type: check
id: clf-02-08
title: "Module 02 mastery check"
tasks: ["1.1", "1.2", "1.4", "3.1"]
objectives: ["02.01a", "02.02a", "02.03a", "02.04a", "02.05a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 02 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-02-01, clf-02-02, clf-02-03, clf-02-04, clf-02-05]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/types-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html"
---

# Module 02 mastery check: show that you can explain why organizations use the cloud

**For:** an adult studying alone, possibly new to IT, who has finished lessons [02.01](01-what-cloud-computing-is.md) to [02.05](05-the-well-architected-framework.md). **Time:** about 20 minutes per check.

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right.

- **8 or more right (80%):** go on to Module 03.
- **Fewer than 8:** reread the sections the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

### Question A1

An engineering firm runs new servers in its own data center. Software lets each team create virtual servers within minutes, and each team is charged monthly for what it used. Nothing runs at a cloud provider. Which deployment model is this?

- A. On-premises deployment
- B. Hybrid deployment, because it combines owned servers with cloud-style software
- C. Cloud deployment, because teams get servers in minutes and pay for use
- D. Community deployment, because the teams share the same servers

<details><summary>Answer</summary>

**A is right.** Every part runs in the firm's own building, on equipment it bought. AWS calls this a private cloud and counts it as on-premises.

- **B is wrong.** Hybrid needs some parts at a cloud provider.
- **C is wrong.** Speed and internal charging don't move anything to a provider.
- **D is wrong.** "Community" isn't one of AWS's deployment models.

</details>

### Question A2

A ferry company's booking website needs 2 servers from September to May and 8 in June, July and August. The company owns 5. Which two statements are accurate? (Select TWO.)

- A. In nine months of the year, it pays for 3 servers that do no work.
- B. In the summer months, some customers can't book.
- C. Its server costs rise in the busy summer months.
- D. Buying 3 more servers would also cut its idle capacity.
- E. The bookings it loses appear as a charge on its server bill.

<details><summary>Answer</summary>

**A and B are right.** 3 servers sit idle for nine months; in summer, demand is 3 above capacity.

- **C is wrong.** Owned servers are a fixed expense.
- **D is wrong.** It would double the idle servers in quiet months.
- **E is wrong.** Lost sales never appear on a bill.

</details>

### Question A3

A city's parking-permit website gets a rush of visitors on the first day of every month. Servers are added within minutes as visitors arrive, and removed by the evening. Which benefit does this show best?

- A. Agility
- B. High availability
- C. Global reach
- D. Elasticity

<details><summary>Answer</summary>

**D is right.** Capacity went up and down, driven by demand.

- **A is wrong.** "Within minutes" sounds like agility, but nothing new was created to try an idea.
- **B is wrong.** Nothing failed.
- **C is wrong.** No new location was involved.

</details>

### Question A4

A photo service keeps copies of every photo in three Availability Zones, so a failed disk or data center loses nothing. A customer asks: "So I can open my photos at every moment?" Which reply is accurate?

- A. Yes: storage that never loses a photo also keeps every photo reachable at all times.
- B. Not necessarily: that design is about photos not being lost, and reaching them is measured separately.
- C. Yes: copies in three Availability Zones also make the service elastic.
- D. Not necessarily: the copies only protect photos the customer deletes by mistake.

<details><summary>Answer</summary>

**B is right.** Copies protect durability (will the photo still exist later?); reaching it now is availability, measured separately.

- **A is wrong.** A photo can be safe but briefly out of reach.
- **C is wrong.** Elasticity is capacity following demand.
- **D is wrong.** Durability doesn't protect against your own deletes.

</details>

### Question A5

A charity's donation site runs in Europe. After an earthquake in Southeast Asia, it runs a copy in a Region there so donors aren't slowed by distance. That copy adds servers automatically as donations surge and removes them when the appeal ends. Which two benefits does this show? (Select TWO.)

- A. Durability
- B. Global reach
- C. High availability
- D. Elasticity
- E. Agility

<details><summary>Answer</summary>

**B and D are right.** The *place* changed (near donors, lower delay): global reach. The *capacity* followed demand: elasticity.

- **A is wrong.** Nothing is about stored data.
- **C is wrong.** Nothing failed.
- **E is wrong.** How fast the copy was set up isn't the point.

</details>

### Question A6

A dental clinic compares two ways to run its records system for three years (made-up numbers). **Owning:** $9,000 for servers in the first month, plus $300 a month for 36 months. **Cloud:** a usage bill averaging $380 a month, matched to demand, nothing up front. Which statement is accurate?

- A. Owning costs about $2,900 less, because its monthly cost is lower.
- B. The cloud costs about $6,100 less over the three years.
- C. The two options cost about the same over the three years.
- D. The cloud costs about $9,000 less, the price of the servers.

<details><summary>Answer</summary>

**B is right.** Owning: $9,000 + 36 × $300 = $19,800. Cloud: 36 × $380 = $13,680.

- **A is wrong.** It forgets the $9,000 paid up front.
- **C is wrong.** The totals differ by about $6,100.
- **D is wrong.** It forgets the cloud's higher monthly bill, $2,880 over three years.

</details>

### Question A7

A print shop used to buy new servers every four years. It now runs the same work in the cloud and is billed for the server hours it uses. Which description of its server spending is accurate?

- A. From capital and fixed to operating and fixed
- B. From operating and variable to capital and fixed
- C. From capital and variable to operating and fixed
- D. From capital and fixed to operating and variable

<details><summary>Answer</summary>

**D is right.** Before: a large payment up front (capital) that didn't change with use (fixed). Now: an ongoing bill (operating) that follows hours used (variable).

- **A is wrong.** A bill for hours used is variable.
- **B is wrong.** It reverses the change.
- **C is wrong.** Bought servers cost the same whatever the shop does: fixed.

</details>

### Question A8

An exam platform's servers are the right type and size, and pages load quickly, but all of them are in one Availability Zone. A review asks what would happen to exams in progress if that AZ lost power. Which pillar does this question belong to?

- A. Performance efficiency
- B. Reliability
- C. Sustainability
- D. Cost optimization

<details><summary>Answer</summary>

**B is right.** What's at risk is whether the platform keeps working and recovers when a part fails.

- **A is wrong.** The resources are already the right type and amount.
- **C is wrong.** Nothing is about wasted resources or energy.
- **D is wrong.** Nothing is about wasted money.

</details>

### Question A9

A software company runs a demo environment with no real data. Which two proposals are trade-offs of the kind the Well-Architected Framework accepts? (Select TWO.)

- A. Run the demo on one server with no standby copy, accepting longer outages.
- B. Let all the sales staff share one administrator sign-in without MFA.
- C. Switch the demo off outside working hours.
- D. Stop recording what changes are made to the demo.
- E. Leave the demo's software unpatched, because it holds no real data.

<details><summary>Answer</summary>

**A and C are right.** Both trade reliability for cost where a failure costs little.

- **B is wrong.** It trades away security, which is generally not traded.
- **D is wrong.** It trades away operational excellence, the other pillar generally not traded.
- **E is wrong.** Unpatched software is a security trade, whatever data it holds.

</details>

### Question A10

A consultant wants to read AWS's reasoning behind each pillar and its design principles before her client builds anything. What should she use?

- A. The AWS Well-Architected Tool
- B. AWS Trusted Advisor
- C. The AWS Well-Architected Framework
- D. An AWS audit that certifies the design

<details><summary>Answer</summary>

**C is right.** The Framework is the written guidance and needs no workload.

- **A is wrong.** The Tool records answers about one workload; it isn't where you read the reasoning.
- **B is wrong.** Trusted Advisor checks an existing account, in categories, not pillars.
- **D is wrong.** A Well-Architected review is a conversation, not an audit.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 02.01a | [Deployment models](01-what-cloud-computing-is.md#the-three-deployment-models-are-cloud-hybrid-and-on-premises) and ["Public, private and community"](01-what-cloud-computing-is.md#public-private-and-community-are-not-awss-deployment-models) |
| A2, B2 | 02.02a | [Any fixed amount is a guess](02-before-and-after-the-demand-curve.md#any-fixed-amount-of-capacity-is-a-guess) |
| A3, B3 | 02.03a | [Elasticity and agility](03-telling-the-benefits-apart.md#capacity-and-speed-elasticity-and-agility) |
| A4, B4 | 02.03a | [Durability isn't availability](03-telling-the-benefits-apart.md#durability-isnt-availability) |
| A5, B5 | 02.03a | [All five side by side](03-telling-the-benefits-apart.md#all-five-side-by-side) |
| A6, B6 | 02.04a | [Costs don't fall automatically](04-what-a-data-center-really-costs.md#moving-to-the-cloud-doesnt-automatically-lower-costs) |
| A7, B7 | 02.04a | [Capital or operating, fixed or variable](04-what-a-data-center-really-costs.md#capital-or-operating-fixed-or-variable-two-different-questions) |
| A8, B8 | 02.05a | [Pillars that sound alike](05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side) |
| A9, B9 | 02.05a | [Trade-offs](05-the-well-architected-framework.md#the-pillars-can-be-traded-against-each-other-but-not-all-of-them) |
| A10, B10 | 02.05a | [Framework and Tool](05-the-well-architected-framework.md#the-framework-is-guidance-the-well-architected-tool-applies-it) |

## Check B: parallel retest

Question B1 tests the same objective as A1, and so on. The pass mark is the same: 8 of 10.

### Question B1

A bank runs a private cloud in its own data centers and sends month-end calculation jobs to AWS, whose results flow back into the private cloud. In AWS's terms, which deployment model describes the whole setup?

- A. Cloud deployment, because both parts are clouds
- B. On-premises deployment, because a private cloud is on-premises
- C. Community deployment, because the bank shares AWS with other customers
- D. Hybrid deployment, because on-premises parts connect to AWS

<details><summary>Answer</summary>

**D is right.** The private cloud is on-premises, the jobs run at AWS, and results pass between them.

- **A is wrong.** Owning a "cloud" doesn't make the bank a cloud provider.
- **B is wrong.** Half right: the month-end jobs run at AWS.
- **C is wrong.** "Community" isn't one of AWS's deployment models.

</details>

### Question B2

A university's application website needs 1 server in ten months of the year and 7 in the two months before deadlines. It owns 4 servers. Which two statements are accurate? (Select TWO.)

- A. Owning 7 servers would remove both its idle servers and its lost applications.
- B. In ten months of the year, it pays for 3 servers that do no work.
- C. Renting 7 cloud servers all year would remove both of its problems.
- D. In the two deadline months, some applicants can't submit.
- E. Owning just 1 server would remove both of its problems.

<details><summary>Answer</summary>

**B and D are right.** 3 servers sit idle in quiet months; demand is 3 above capacity in deadline months.

- **A is wrong.** Six servers would then sit idle in quiet months.
- **C is wrong.** It keeps 6 idle servers for ten months, now as rent.
- **E is wrong.** Deadline months would turn away 6 servers' worth of applicants.

</details>

### Question B3

A bank's data team wants to test a new fraud-detection model. One afternoon it starts 50 servers, runs the test overnight, and deletes them all the next morning. Which benefit does this show best?

- A. Elasticity
- B. Durability
- C. High availability
- D. Agility

<details><summary>Answer</summary>

**D is right.** A team tried something new quickly and deleted everything afterwards.

- **A is wrong.** Servers went up and down, but not following customer demand.
- **B is wrong.** Nothing is about stored data.
- **C is wrong.** Nothing failed.

</details>

### Question B4

A medical-imaging company writes two storage requirements. **R1:** "No scan may ever be lost, even when disks fail." **R2:** "Doctors must be able to open any scan at any hour, even during a failure." Which benefit does each describe?

- A. R1 durability; R2 high availability
- B. R1 high availability; R2 durability
- C. Both durability
- D. Both high availability

<details><summary>Answer</summary>

**A is right.** R1 asks whether the scan will still exist; R2 asks whether a doctor can reach it now.

- **B is wrong.** It swaps the two.
- **C is wrong.** A scan can be safe but out of reach for a while.
- **D is wrong.** A reachable system with one copy can still lose a file.

</details>

### Question B5

An emergency-alert sign-up site runs in two Availability Zones. In a storm, one AZ lost power and the site kept taking sign-ups; that night, servers were added automatically as sign-ups jumped, and removed the next week. Which two benefits does this show? (Select TWO.)

- A. High availability
- B. Agility
- C. Global reach
- D. Elasticity
- E. Durability

<details><summary>Answer</summary>

**A and D are right.** A part failed and the site kept working: high availability. Capacity rose and fell with demand: elasticity.

- **B is wrong.** Nothing new was set up to try an idea.
- **C is wrong.** Both AZs are in one Region.
- **E is wrong.** Nothing is about stored data.

</details>

### Question B6

A factory's monitoring system runs at the same load all day, every day. Over three years (made-up numbers): **owning** costs $6,000 for servers in the first month plus $200 a month; the **cloud** costs $450 a month. Which statement is accurate?

- A. The cloud costs about $3,000 less, because there is no up-front payment.
- B. The two options cost the same, because the load never changes.
- C. Owning costs about $3,000 less over the three years.
- D. Owning costs about $9,000 less, because its monthly cost is $250 lower.

<details><summary>Answer</summary>

**C is right.** Owning: $6,000 + 36 × $200 = $13,200. Cloud: 36 × $450 = $16,200. Flat demand leaves no idle capacity to give back.

- **A is wrong.** No up-front payment helps the first month, not the three-year total.
- **B is wrong.** The totals differ by $3,000.
- **D is wrong.** It forgets the $6,000 paid up front.

</details>

### Question B7

A firm moves its servers to a hosting company and pays the same fee every month for a set number of servers, whether it uses them or not, on a month-to-month contract. How is its server spending best described?

- A. Capital and fixed
- B. Operating and variable
- C. Operating and fixed
- D. Capital and variable

<details><summary>Answer</summary>

**C is right.** A monthly fee with nothing bought up front is operating; an amount that doesn't change with use is fixed, however short the contract.

- **A is wrong.** Nothing is bought up front.
- **B is wrong.** Paying monthly doesn't make a cost variable.
- **D is wrong.** There's neither a purchase up front nor an amount that follows use.

</details>

### Question B8

A payroll company backs up its database every night, and its servers are well sized and fast. Nobody has ever tried restoring from a backup. Which pillar does this concern most?

- A. Reliability
- B. Performance efficiency
- C. Cost optimization
- D. Sustainability

<details><summary>Answer</summary>

**A is right.** What's at risk is recovery; the reliability design principle "[Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" covers it.

- **B is wrong.** The servers are already the right size.
- **C is wrong.** Nothing wastes money.
- **D is wrong.** Nothing wastes resources or energy.

</details>

### Question B9

A training company runs a live booking system and a classroom environment it rebuilds for each course. Which two proposals are trade-offs of the kind the Well-Architected Framework accepts? (Select TWO.)

- A. Run the classroom environment in one Availability Zone, with no standby copy.
- B. Give the classroom environment one shared password with no MFA.
- C. Pay for copies of the booking system in three Availability Zones, because every lost hour loses bookings.
- D. Release changes to the booking system without any review.
- E. Store customers' card details unencrypted, so bookings complete faster.

<details><summary>Answer</summary>

**A and C are right.** Both weigh reliability against cost by what a failure would cost the business.

- **B is wrong.** It trades away security.
- **D is wrong.** It trades away operational excellence.
- **E is wrong.** It trades away security too.

</details>

### Question B10

A hospital's IT lead wants her team to answer the Well-Architected Framework's questions about the patient portal one by one, get a list of high-risk issues, and save a snapshot to compare with after the fixes. What should the team use?

- A. AWS Trusted Advisor
- B. The AWS Well-Architected Tool
- C. The AWS Well-Architected Framework whitepaper
- D. An AWS audit that certifies the portal

<details><summary>Answer</summary>

**B is right.** The Tool asks the Framework's questions about one workload, flags risks, and saves milestones.

- **A is wrong.** Trusted Advisor runs automatic account checks, not a question-by-question review.
- **C is wrong.** The whitepaper doesn't record answers or snapshots.
- **D is wrong.** A Well-Architected review is a conversation, not an audit.

</details>

---

"Module 02 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
