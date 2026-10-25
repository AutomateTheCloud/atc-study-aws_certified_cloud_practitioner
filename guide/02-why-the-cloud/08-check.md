---
type: check
id: clf-02-08
title: "Module 02 mastery check"
tasks: ["1.1", "1.2", "1.4", "3.1"]
objectives: ["02.01a", "02.02a", "02.03a", "02.04a", "02.05a"]
reader: "Adult studying alone, possibly new to IT; end of Module 02; about 30 minutes for each check; works on a phone"
prerequisites: [clf-02-01, clf-02-02, clf-02-03, clf-02-04, clf-02-05]
pillars: [operational-excellence, security, reliability, performance-efficiency, cost-optimization, sustainability]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/types-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html"
  - "https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html"
---

# Module 02 mastery check: show that you can explain why organizations use the cloud

This check tells you whether you can use the ideas of Module 02 in new situations: deployment models, the demand curve, the cloud's benefits, on-premises costs, and the Well-Architected pillars. Every question is a short scenario you haven't seen before.

**For:** an adult studying alone, possibly new to IT, who has worked through the five lessons of Module 02. **Time:** about 30 minutes for Check A, and the same for Check B if you need it. Reading works on a phone.

## How to use this check

Take **Check A** closed-book: no notes, no lessons, no searching. Answer every question before you open any answer. Then score yourself: each question is worth one point, and a "(Select TWO.)" question scores only if both choices are right.

**You pass at 80%:** 10 of the 12 questions.

- **Below 10:** for each question you missed, use the [correction map](#correction-map) to reread the section it points to, and do the activity it names. Then take **Check B**, the parallel retest. It tests the same ideas with new scenarios, so you can't pass it by remembering Check A's answers.
- **10 or more:** you have mastered the module. Skip Check B and try the [enrichment tasks](#enrichment-harder-tasks-for-when-you-pass) instead.

The questions follow the exam's style: four choices with one answer, or five choices with two answers when the question says "(Select TWO.)". Each answer explains why the right choice is right and why each wrong one is wrong. Read the explanations for the questions you got right, too: a lucky guess looks the same as knowing.

## Check A

**A1.** A city library runs its catalogue-search website on AWS. Its checkout desks use a lending system that runs on a server in the library's basement. When someone searches the catalogue, the website asks the lending system whether each book is on loan. Which deployment model describes the library's setup?

- A. Cloud, because the public reaches the catalogue over the internet
- B. On-premises, because the lending records stay in the library
- C. Hybrid, because connected parts run in both places
- D. Private cloud, because the library controls the lending system

<details><summary>Answer</summary>

**C is right.** Ask where each part runs. The website runs at AWS and the lending system runs in the library's own building, and data flows between them. Some parts in the cloud, some on-premises, connected: that is hybrid.

- **A is wrong.** How people reach a system doesn't decide the model. The lending system doesn't run at a cloud provider.
- **B is wrong.** Only one of the two parts is on-premises. The website runs at AWS.
- **D is wrong.** In AWS's terms, a private cloud is on-premises equipment run with sharing software, and it isn't a separate model. The lending system is one server in the basement, and the website isn't on-premises at all.

</details>

**A2.** An engineering firm replaces its old servers with new ones in its own data center. It installs software that lets each project team create virtual servers within minutes from a self-service web page, and it charges each team every month for what the team used. Nothing runs at a cloud provider. Which deployment model is this?

- A. On-premises deployment, because every server runs in the firm's own building
- B. Hybrid deployment, because it combines owned servers with cloud-style software
- C. Cloud deployment, because teams get servers in minutes and pay for use
- D. Community deployment, because the teams share the same servers

<details><summary>Answer</summary>

**A is right.** Every part runs on equipment in the firm's own building, which decides the model. Sharing software makes the servers quick to hand out, and the monthly charge to each team is internal bookkeeping: the firm itself still buys, houses and pays for all the equipment, busy or idle. AWS calls this kind of setup a private cloud and counts it as on-premises.

- **B is wrong.** Hybrid needs some parts at a cloud provider. Software that behaves like the cloud isn't a cloud provider.
- **C is wrong.** Speed and internal charging don't move anything to a provider. The firm still made the large purchase up front.
- **D is wrong.** "Community" belongs to a different vocabulary. AWS's deployment models are cloud, hybrid and on-premises.

</details>

**A3.** A ferry company's booking website needs 2 servers from September to May, and 8 servers in June, July and August. The company owns 5 servers all year. Which two statements about this setup are accurate? (Select TWO.)

- A. In nine months of the year, it pays for 3 servers that do no work.
- B. In the summer months, some customers can't book.
- C. Its server costs rise in the summer, when the servers are busiest.
- D. Buying 3 more servers would also cut its idle capacity.
- E. The bookings it loses appear as a charge on its server bill.

<details><summary>Answer</summary>

**A and B are right.** Draw the flat line at 5. From September to May, demand (2) is below the line, so 3 owned servers sit idle: that is idle capacity. In the summer, demand (8) is 3 servers above the line, so some customers can't book: those are lost sales.

- **C is wrong.** Owned servers are a fixed expense: the company pays the same in a busy month as in a quiet one.
- **D is wrong.** Three more servers would end the lost bookings, but in the nine quiet months 6 servers would sit idle instead of 3. Idle capacity would double.
- **E is wrong.** Lost sales never appear on a bill. The customers simply book with someone else, which is why the cost is easy to overlook.

</details>

**A4.** A school's homework website runs on 4 servers that the school owns. In the 8 months of normal term it needs 2 servers, in the 2 exam months it needs 6, and in the 2 holiday months it needs 1. Over the year, how many of the server-months it pays for sit idle, and when are students turned away?

- A. 18 idle server-months; students are turned away in the exam months
- B. 22 idle server-months; no students are turned away
- C. 22 idle server-months; students are turned away in the exam months
- D. 26 idle server-months; students are turned away in the holiday months

<details><summary>Answer</summary>

**C is right.** The school pays for 4 servers × 12 months = 48 server-months. It can use at most the 4 it owns, so count each month's use up to 4: 8 × 2 + 2 × 4 + 2 × 1 = 26 server-months used. That leaves 48 − 26 = **22 idle**. In the exam months, demand (6) is above the 4 owned servers, so students are turned away then.

- **A is wrong.** 18 comes from counting 6 servers of use in the exam months, but the school can't use servers it doesn't own. The extra demand is lost, not used.
- **B is wrong.** The idle figure is right, but in the exam months demand is 2 servers above what the school owns.
- **D is wrong.** 26 is the number of server-months *used*, not idle. And in the holiday months demand (1) is below capacity, so nobody is turned away then.

</details>

**A5.** A city's parking-permit website gets a rush of visitors on the first day of every month, when permits renew. On that day, servers are added within minutes as visitors arrive, so the site keeps working. By the evening, the extra servers are removed. Which benefit does this show best?

- A. Agility
- B. High availability
- C. Global reach
- D. Elasticity

<details><summary>Answer</summary>

**D is right.** Ask what changed: the amount of capacity, up and then down, driven by demand. Capacity that follows demand in both directions is elasticity.

- **A is wrong.** "Within minutes" sounds like agility, but nothing new was created to try an idea. The minutes bought more of the same website, in response to visitors.
- **B is wrong.** "The site keeps working" sounds like high availability, but nothing failed. The site kept working because capacity grew with the load, which is elasticity.
- **C is wrong.** No new location was involved.

</details>

**A6.** A photo-storage service tells customers that it keeps copies of every photo in three separate Availability Zones, so that a failed disk, or even a failed data center, doesn't lose any photos. A customer asks: "So I can open my photos at every moment?" Which reply is accurate?

- A. Yes: storage built so that no photo is ever lost also keeps every photo reachable at all times.
- B. Not necessarily: that design is about photos not being lost, and reaching them is measured separately.
- C. Yes: keeping copies in three Availability Zones also makes the storage service elastic.
- D. Not necessarily: the copies protect the photos only from being deleted by the customer by mistake.

<details><summary>Answer</summary>

**B is right.** Copies in several places protect against losing data for good, which is durability: will the photo still exist later? Whether the customer can reach a photo right now is availability, and it is designed and measured separately. Amazon S3 Standard, for example, is designed for eleven nines of durability but 99.99% availability (as of 2026-10-23).

- **A is wrong.** This is the confusion the question tests. A photo can be safe but briefly out of reach during an outage.
- **C is wrong.** Elasticity is about capacity growing and shrinking with demand. Copies in three AZs are about not losing data.
- **D is wrong.** It is the other way round. Durability protects against the storage failing, not against you: if the customer deletes a photo, a durable service deletes it reliably.

</details>

**A7.** A charity runs its donation website in an AWS Region in Europe. After an earthquake in Southeast Asia, it also runs a copy of the site in a Region in that part of the world, so that donors there aren't slowed down by the distance. As donations surge, that copy adds servers automatically, and it removes them when the appeal ends. Which two benefits does this show? (Select TWO.)

- A. Durability
- B. Global reach
- C. High availability
- D. Elasticity
- E. Agility

<details><summary>Answer</summary>

**B and D are right.** Ask what changed. The *place* changed: a copy runs near donors in another part of the world, so they get lower delay. That is global reach. The *capacity* changed with demand, up during the surge and down after: that is elasticity.

- **A is wrong.** Nothing in the scenario is about stored data being kept safe from loss.
- **C is wrong.** Nothing failed. The second copy was added to be near donors, not to survive a failure.
- **E is wrong.** Agility is about how fast or how cheaply you get something new. The scenario stresses *where* the copy runs and how its capacity follows demand, not how quickly it was set up.

</details>

**A8.** A dental clinic compares two ways to run its patient-records system for three years. All the numbers are made up for teaching.

- **Owning:** $9,000 for servers, paid in the first month, plus $300 a month for all 36 months for space, power, network and support.
- **Cloud:** a usage bill that averages $380 a month, matched to the clinic's demand, with no up-front payment.

Which statement is accurate?

- A. Owning costs about $2,900 less, because its monthly cost is lower.
- B. The cloud costs about $6,100 less over the three years.
- C. The two options cost about the same over the three years.
- D. The cloud costs about $9,000 less, the price of the servers.

<details><summary>Answer</summary>

**B is right.** Price each option over its whole life. Owning: $9,000 + 36 × $300 = $9,000 + $10,800 = **$19,800**. Cloud: 36 × $380 = **$13,680**. The difference is $6,120, about $6,100 in the cloud's favor. The first month differs even more: $9,300 against $380.

- **A is wrong.** It compares only the monthly costs ($80 × 36 = $2,880) and forgets the $9,000 paid up front. Comparing the cloud bill with only part of the on-premises cost is the usual mistake.
- **C is wrong.** The totals differ by about $6,100.
- **D is wrong.** It counts the hardware but forgets that the cloud's monthly bill is $80 higher, which adds up to $2,880 over three years.

</details>

**A9.** A print shop used to buy new servers every four years and run them in its back room. It now runs the same work in the cloud, and it is billed for the server hours it uses. Which description of its server spending is accurate, in both pairs of terms (capital or operating, fixed or variable)?

- A. It has changed from capital and fixed to operating and fixed.
- B. It has changed from operating and variable to capital and fixed.
- C. It has changed from capital and variable to operating and fixed.
- D. It has changed from capital and fixed to operating and variable.

<details><summary>Answer</summary>

**D is right.** The two pairs answer two different questions. *When and how does it pay?* Before, a large payment up front for servers that last years: capital. Now, an ongoing bill: operating. *Does the cost change with use?* Before, the same whatever the shop printed: fixed. Now, it follows the server hours used: variable.

- **A is wrong.** A bill for the hours used changes with use, so it is variable, not fixed. A fixed operating expense would be something like a flat monthly fee.
- **B is wrong.** It reverses the change: the shop moved away from buying servers.
- **C is wrong.** Buying servers every four years costs the same whatever the shop does with them, so it was fixed, not variable.

</details>

**A10.** An online exam platform runs on servers that are the right type and size for its load, and its pages load quickly. All of its servers are in one Availability Zone. A design review asks what would happen to the exams in progress if that Availability Zone lost power. Which Well-Architected pillar does this question belong to?

- A. Performance efficiency
- B. Reliability
- C. Sustainability
- D. Cost optimization

<details><summary>Answer</summary>

**B is right.** Decide by what is at risk. The question is whether the platform keeps working, and recovers, when part of it fails. That is reliability. Running copies in more than one AZ is the usual answer.

- **A is wrong.** Performance efficiency asks whether the platform uses the right type and amount of resources. The scenario says they are already right; the risk is failure, not fit.
- **C is wrong.** Nothing here is about wasting resources or energy.
- **D is wrong.** Nothing here is about wasting money. (A second AZ would cost more, which is a trade-off the business decides, but the question itself is about failure.)

</details>

**A11.** A software company runs a demo environment that its sales staff use to show the product to customers. It holds no real customer data. The team proposes five changes to save time or money. Which two are trade-offs of the kind the Well-Architected Framework accepts? (Select TWO.)

- A. Run the demo on one server with no standby copy, accepting longer outages.
- B. Let all the sales staff share one administrator sign-in without MFA.
- C. Switch the demo off outside working hours, accepting that it can't be used at night.
- D. Stop recording what changes are made to the demo, to save the team's time.
- E. Leave the demo's software unpatched, because it holds no real data.

<details><summary>Answer</summary>

**A and C are right.** Both accept less reliability (longer outages, no use at night) in return for lower cost, in an environment where a failure costs little. The Framework itself gives lower reliability in a development environment as an example of a reasonable trade-off. Switching non-production systems off outside working hours is also its example for the cost design principle "[Adopt a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html)".

- **B is wrong.** It trades away security, which the Framework says is generally not traded against the other pillars. A break-in to the demo account can reach everything else in that account.
- **D is wrong.** It trades away operational excellence, the other pillar that is generally not traded away. Without a record of changes, nobody can tell what broke the demo or undo it.
- **E is wrong.** Unpatched software is an easy way in for an attacker, whatever data it holds. That is a security trade, too.

</details>

**A12.** A consultant is preparing a design workshop for a client that hasn't built anything yet. She wants to read AWS's reasoning behind each pillar and its design principles, so the team can use them while it designs. What should she use?

- A. The AWS Well-Architected Tool
- B. AWS Trusted Advisor
- C. The AWS Well-Architected Framework
- D. An AWS audit that certifies the design

<details><summary>Answer</summary>

**C is right.** The Framework is AWS's written guidance: the pillars, their design principles and best practices, with the reasoning behind them. It is free to read, and it needs no workload.

- **A is wrong.** The Tool is a console service for reviewing one existing or planned workload by answering the Framework's questions. It records answers and risks; it isn't where you read the reasoning.
- **B is wrong.** Trusted Advisor runs automatic checks on an AWS account, grouped into categories, not pillars. The client has no account to check yet.
- **D is wrong.** A Well-Architected review is a conversation about decisions, not an audit, and nobody passes or fails it.

</details>

## Correction map

Find each question you missed. Reread the section it names, then read the line under "Another way to see it", which explains the idea differently from the lesson. Then do the activity in the last column, if there is one.

| Question | Objective | Reread | Another way to see it | Practice |
|---|---|---|---|---|
| A1, B1 | 02.01a Classify a setup | [The three deployment models are cloud, hybrid and on-premises](01-what-cloud-computing-is.md#the-three-deployment-models-are-cloud-hybrid-and-on-premises) and [the worked example](01-what-cloud-computing-is.md#worked-example-classifying-three-setups) | Write each part of the system on a sticky note and put it on one of two pages: "at a provider" or "in our building". Both pages used, and the parts talk to each other: hybrid | The "Your turn" in the worked example |
| A2, B2 | 02.01a Classify a setup | ["Public, private and community" are not AWS's deployment models](01-what-cloud-computing-is.md#public-private-and-community-are-not-awss-deployment-models) | Ask who bought the equipment. If the organization did, and it sits in its own building, that part is on-premises, however cloud-like its software feels | The Check in that section |
| A3, B3 | 02.02a Idle cost and lost sales | [Buying for the peak means paying for idle servers](02-before-and-after-the-demand-curve.md#buying-for-the-peak-means-paying-for-idle-servers) and [Buying for normal months turns customers away at the peak](02-before-and-after-the-demand-curve.md#buying-for-normal-months-turns-customers-away-at-the-peak) | Sketch the columns and draw the flat line. Everything below the line and above a column is idle; everything above the line is lost. Moving the line shrinks one gap and grows the other | [Simulation S1](07-sim-demand-curve.md), decisions 1 and 2 |
| A4, B4 | 02.02a Idle cost and lost sales | [Worked example: the bakery's year in numbers](02-before-and-after-the-demand-curve.md#worked-example-the-bakerys-year-in-numbers), step 2 | You can't use a server you don't own. Cap each month's use at the owned number before you add up, and count what is above the cap as lost, not used | [Simulation S1](07-sim-demand-curve.md), decision 2 |
| A5, B5 | 02.03a Name the benefit | [Elasticity and agility both sound like "fast"](03-telling-the-benefits-apart.md#elasticity-and-agility-both-sound-like-fast) | Ask what started the change. Customers arriving or leaving: elasticity. A person deciding to try something: agility. Both can involve many servers appearing quickly | [Lab 01](06-lab-01-first-resource.md), where you time agility yourself |
| A6, B6 | 02.03a Name the benefit | [Durability isn't availability](03-telling-the-benefits-apart.md#durability-isnt-availability) | Durability is a library that never loses a book; availability is a library that is open when you arrive. A library can lose nothing and still be closed on a holiday | The mixed practice in that lesson |
| A7, B7 | 02.03a Name the benefit | [All five side by side](03-telling-the-benefits-apart.md#all-five-side-by-side) and [Global reach and agility both happen "in minutes"](03-telling-the-benefits-apart.md#global-reach-and-agility-both-happen-in-minutes) | Give each sentence of the scenario its own question: capacity, time, failure, data or place. A scenario that names two benefits has two sentences that answer two different questions | The mixed practice in that lesson |
| A8, B8 | 02.04a Compare costs in numbers | [Worked example: the bakery's three-year comparison](04-what-a-data-center-really-costs.md#worked-example-the-bakerys-three-year-comparison) and [Moving to the cloud doesn't automatically lower costs](04-what-a-data-center-really-costs.md#moving-to-the-cloud-doesnt-automatically-lower-costs) | Write one line per option: up-front amount + (monthly amount × number of months). Compare the totals, never just the monthly figures. Then ask whether demand moves enough to give anything back | [Simulation S1](07-sim-demand-curve.md), decisions 2 and 4 |
| A9, B9 | 02.04a Compare costs in numbers | [Capital or operating, fixed or variable: two different questions](04-what-a-data-center-really-costs.md#capital-or-operating-fixed-or-variable-two-different-questions) | Ask two separate questions about the same payment. "Did we pay a large sum up front for something that lasts?" (capital or operating). "Would the amount change if we used half as much?" (fixed or variable) | The Check in that section |
| A10, B10 | 02.05a Match a concern to a pillar | [Pillars that sound alike, side by side](05-the-well-architected-framework.md#pillars-that-sound-alike-side-by-side) | Imagine the worst outcome if nobody fixes the concern. The system stops or can't come back: reliability. It works, but slowly or on the wrong resource: performance efficiency | The "Your turn" in [Six pillars, six questions](05-the-well-architected-framework.md#six-pillars-six-questions) |
| A11, B11 | 02.05a Explain a trade-off | [The pillars can be traded against each other, but not all of them](05-the-well-architected-framework.md#the-pillars-can-be-traded-against-each-other-but-not-all-of-them) | Reliability and cost can move like a slider, depending on what a failure would cost. Security and operational excellence aren't on the slider: they stay in place on every copy of a system | The "Your turn" in that section |
| A12, B12 | 02.05a Framework and Tool | [The Framework is guidance; the Well-Architected Tool applies it](05-the-well-architected-framework.md#the-framework-is-guidance-the-well-architected-tool-applies-it) | The Framework is the textbook; the Tool is the worksheet you fill in about one workload, and keep to compare later. Trusted Advisor is a separate inspector that checks the whole account by itself | The Check in that section |

## Check B: parallel retest

Take Check B only after you have worked through the correction map for the questions you missed. Use the same rules as Check A: closed-book, one point a question, and 10 of 12 to pass. If you pass, go on to Module 03. If not, use the correction map again for the questions you missed, and retry the practice questions at the end of each lesson before you take Check A again on another day.

**B1.** A farm cooperative runs its members' website on AWS. The scales that weigh each delivery of grain send their readings to a server in the co-op's office. The website shows each member's delivery weights by reading them from that server. Which deployment model is this?

- A. Hybrid, because connected parts run in the office and at AWS
- B. On-premises, because the weighing data starts in the co-op's office
- C. Cloud, because members see their weights on a website
- D. Community, because the co-op's members share the system

<details><summary>Answer</summary>

**A is right.** The website runs at AWS, the server with the weighing data runs in the co-op's office, and the website reads from that server. Parts in both places, connected: hybrid.

- **B is wrong.** Where the data starts doesn't make the whole system on-premises. The website runs at a cloud provider.
- **C is wrong.** A website being reachable online doesn't make every part cloud. The office server is on-premises.
- **D is wrong.** "Community" isn't one of AWS's deployment models, and sharing a system among members doesn't change where its parts run.

</details>

**B2.** A bank runs a private cloud in its own data centers: its own servers, with software that gives its teams virtual servers within minutes. At the end of each month, it sends extra calculation jobs to AWS, and the results flow back into the private cloud. In AWS's terms, which deployment model describes this whole setup?

- A. Cloud deployment, because both parts are clouds
- B. On-premises deployment, because a private cloud is on-premises
- C. Community deployment, because the bank shares AWS with other customers
- D. Hybrid deployment, because on-premises parts connect to AWS

<details><summary>Answer</summary>

**D is right.** First, classify each part. The private cloud is the bank's own equipment in its own buildings, so in AWS's terms it is on-premises. The month-end jobs run at AWS. On-premises parts and cloud parts, with results flowing between them: hybrid.

- **A is wrong.** Calling the bank's own servers a "cloud" doesn't make them a cloud provider. AWS counts a private cloud as on-premises.
- **B is wrong.** It is half right: the private cloud is on-premises. But the month-end jobs run at AWS, so the whole setup isn't on-premises.
- **C is wrong.** "Community" belongs to a different vocabulary, not AWS's. Many customers using AWS doesn't make anyone's deployment a community one.

</details>

**B3.** A university's application website needs 1 server in ten months of the year and 7 servers in the two months before application deadlines. The university owns 4 servers. Which two statements are accurate? (Select TWO.)

- A. Owning 7 servers would remove both its idle servers and its lost applications.
- B. In ten months of the year, it pays for 3 servers that do no work.
- C. Renting 7 cloud servers all year would remove both of its problems.
- D. In the two deadline months, some applicants can't submit.
- E. Owning just 1 server would remove both of its problems.

<details><summary>Answer</summary>

**B and D are right.** With the flat line at 4: in the ten quiet months, demand (1) is 3 below the line, so 3 owned servers are idle. In the deadline months, demand (7) is 3 above the line, so some applicants can't submit.

- **A is wrong.** Seven servers would end the lost applications, but in the ten quiet months 6 servers would sit idle.
- **C is wrong.** Renting 7 servers all year ends the lost applications but keeps 6 idle servers for ten months, now as rent. The cloud saves money only if capacity is removed when demand falls.
- **E is wrong.** One server would leave nothing idle in the quiet months, but in the deadline months 6 servers' worth of applicants would be turned away.

</details>

**B4.** A tax-advice firm's client website runs on 3 servers that the firm owns. It needs 1 server for nine months of the year, and 5 servers in the three months of tax season. Over the year, how many of the server-months it pays for sit idle, and when are clients turned away?

- A. 12 idle server-months; clients are turned away in tax season
- B. 18 idle server-months; clients are turned away in tax season
- C. 18 idle server-months; no clients are turned away
- D. 24 idle server-months; clients are turned away outside tax season

<details><summary>Answer</summary>

**B is right.** The firm pays for 3 × 12 = 36 server-months. Capped at the 3 servers it owns, it uses 9 × 1 + 3 × 3 = 18. That leaves 36 − 18 = **18 idle**. In tax season, demand (5) is above the 3 owned servers, so clients are turned away then.

- **A is wrong.** 12 comes from counting 5 servers of use in tax season (9 + 15 = 24 used), but the firm can't use servers it doesn't own.
- **C is wrong.** The idle figure is right, but demand in tax season is 2 servers above what the firm owns.
- **D is wrong.** 24 is the total demand for the year, not the idle capacity. And outside tax season, demand is below capacity, so nobody is turned away.

</details>

**B5.** A bank's data team wants to test whether a new fraud-detection model works. One afternoon it starts 50 servers, runs the test overnight, and deletes all of them the next morning. Which benefit does this show best?

- A. Elasticity
- B. Durability
- C. High availability
- D. Agility

<details><summary>Answer</summary>

**D is right.** Ask what started the change: a team decided to try something new. It got the resources it needed within an afternoon, tried the idea, and deleted everything, with nothing bought up front. That is agility.

- **A is wrong.** The number of servers went up and down, which looks like elasticity. But it wasn't capacity following customer demand for an existing system; it was a one-off experiment that a person decided to run.
- **B is wrong.** Nothing in the scenario is about stored data being kept safe from loss.
- **C is wrong.** Nothing failed, and nothing had to keep running through a failure.

</details>

**B6.** A medical-imaging company writes two requirements for its storage.

- **R1:** "No scan may ever be lost, even when disks fail."
- **R2:** "Doctors must be able to open any scan at any hour, even during a failure."

Which benefit does each requirement describe?

- A. R1 describes durability; R2 describes high availability.
- B. R1 describes high availability; R2 describes durability.
- C. R1 and R2 both describe durability.
- D. R1 and R2 both describe high availability.

<details><summary>Answer</summary>

**A is right.** R1 asks "will the scan still exist later?": durability. R2 asks "can a doctor reach it right now, even when something fails?": high availability. A storage design can meet one and not the other, so the company needs to ask for both.

- **B is wrong.** It swaps the two. Not losing data is durability; being reachable through a failure is availability.
- **C is wrong.** A scan can be perfectly safe but out of reach for a while. R2 is about reaching it, which durability doesn't promise.
- **D is wrong.** A system can be up and reachable and still lose a file when a disk fails, if it keeps only one copy. R1 is about not losing data, which is durability.

</details>

**B7.** A city's emergency-alert sign-up website runs copies in two Availability Zones. During a storm, one Availability Zone lost power, and the site kept taking sign-ups. The same night, servers were added automatically as sign-ups jumped, and they were removed the next week. Which two benefits does this show? (Select TWO.)

- A. High availability
- B. Agility
- C. Global reach
- D. Elasticity
- E. Durability

<details><summary>Answer</summary>

**A and D are right.** Two different things happened. A part failed (one AZ lost power) and the site kept working: high availability. Capacity rose with demand and fell again later: elasticity.

- **B is wrong.** Nothing new was set up to try an idea. The site already existed.
- **C is wrong.** Both AZs are in one Region, and no new part of the world was reached.
- **E is wrong.** Nothing in the scenario is about stored data being lost or kept. Surviving the power cut is about staying up, which is availability.

</details>

**B8.** A factory's sensor-monitoring system runs at the same load 24 hours a day, every day. The factory compares two options over three years. All the numbers are made up for teaching.

- **Owning:** $6,000 for servers, paid in the first month, plus $200 a month for all 36 months.
- **Cloud:** $450 a month, because the system never has quiet hours in which to scale down.

Which statement is accurate?

- A. The cloud costs about $3,000 less, because there is no up-front payment.
- B. The two options cost the same, because the load never changes.
- C. Owning costs about $3,000 less over the three years.
- D. Owning costs about $9,000 less, because its monthly cost is $250 lower.

<details><summary>Answer</summary>

**C is right.** Owning: $6,000 + 36 × $200 = $6,000 + $7,200 = **$13,200**. Cloud: 36 × $450 = **$16,200**. Owning is $3,000 cheaper here. With flat demand, there is no idle capacity to give back, so paying by use has little to save. (The cloud still needs far less money in the first month: $450 against $6,200. And real prices, including AWS's discounts for steady use in Module 11, could change the result. That is why you compare real numbers before deciding.)

- **A is wrong.** No up-front payment makes the cloud cheaper in the first month, not over three years. The higher monthly bill adds up to more than the $6,000 saved.
- **B is wrong.** The totals differ by $3,000. Steady load means less to gain from paying by use, not equal costs.
- **D is wrong.** It compares only the monthly costs ($250 × 36 = $9,000) and forgets the $6,000 owning pays up front.

</details>

**B9.** A firm moves its servers out of its own building to a hosting company. It now pays the same fee every month for a set number of servers, whether it uses them or not. The contract runs from month to month. How is its server spending now best described, in both pairs of terms (capital or operating, fixed or variable)?

- A. Capital and fixed
- B. Operating and variable
- C. Operating and fixed
- D. Capital and variable

<details><summary>Answer</summary>

**C is right.** *When and how does it pay?* A monthly fee, with no large purchase up front: operating. *Does the amount change with use?* No: the fee is the same in a quiet month as in a busy one: fixed. The firm changed the timing of its payments, but its bill still doesn't follow its use. Fixed or variable is about whether the amount changes with use, not about how long the contract runs: a month-to-month fee that stays the same whatever you use is still fixed. (This is also why the arrangement isn't cloud computing in AWS's sense: it isn't pay as you go.)

- **A is wrong.** The firm no longer buys servers up front, so the spending isn't capital.
- **B is wrong.** Paying every month doesn't make an expense variable. Variable means the amount changes with how much you use.
- **D is wrong.** There is neither an up-front purchase nor an amount that follows use.

</details>

**B10.** A payroll company backs up its database every night, and its servers are well sized and fast. Nobody has ever tried restoring the database from a backup, so nobody knows whether the backups work, or how long a restore would take. Which Well-Architected pillar does this concern most?

- A. Reliability
- B. Performance efficiency
- C. Cost optimization
- D. Sustainability

<details><summary>Answer</summary>

**A is right.** What is at risk is recovery: if the database fails, the company may not be able to bring it back. The reliability pillar's design principle "[Test recovery procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" covers exactly this.

- **B is wrong.** The servers are already the right size and fast. Performance efficiency is about the right type and amount of resources, not about recovering from failure.
- **C is wrong.** Nothing here wastes money. The risk is that the payroll can't be restored.
- **D is wrong.** Nothing here wastes resources or energy.

</details>

**B11.** A training company runs a live booking system for its customers, and a classroom environment that it rebuilds for each course. Which two proposals are trade-offs of the kind the Well-Architected Framework accepts? (Select TWO.)

- A. Run the classroom environment in one Availability Zone, with no standby copy.
- B. Give the classroom environment one shared password with no MFA, so that trainees sign in faster.
- C. Pay for copies of the live booking system in three Availability Zones, because every lost hour loses bookings.
- D. Release changes to the live booking system without any review, to ship features faster.
- E. Store customers' card details unencrypted, so that bookings complete faster.

<details><summary>Answer</summary>

**A and C are right.** Both weigh reliability against cost by what a failure would cost the business. A classroom environment that is rebuilt anyway can accept lower reliability to save money. A live system that loses bookings every hour it is down justifies paying more for reliability. The Framework gives both kinds as examples of reasonable trade-offs.

- **B is wrong.** It trades away security, which the Framework says is generally not traded against the other pillars. A break-in through the classroom environment can reach the rest of the account.
- **D is wrong.** It trades away operational excellence, the other pillar that is generally not traded away. Changes without review are hard to trust and hard to undo.
- **E is wrong.** It trades security for speed, on the most sensitive data the company holds.

</details>

**B12.** A hospital's IT lead has read the Well-Architected Framework. Now she wants her team to answer its questions about the patient portal one by one, get a list of high-risk issues, and save a snapshot to compare with after the fixes. What should the team use?

- A. AWS Trusted Advisor
- B. The AWS Well-Architected Tool
- C. The AWS Well-Architected Framework whitepaper
- D. An AWS audit that certifies the portal

<details><summary>Answer</summary>

**B is right.** The Tool is the console service for reviewing one workload against the Framework. It asks the Framework's questions, flags high-risk and medium-risk issues, builds an improvement plan, and saves milestones (snapshots) to compare later. It has no charge to use (as of 2026-10-23).

- **A is wrong.** Trusted Advisor runs automatic checks across an AWS account, grouped into categories. It doesn't take a team through the Framework's questions for one workload.
- **C is wrong.** The whitepaper is the guidance she has already read. It doesn't record answers or save snapshots.
- **D is wrong.** A Well-Architected review is a conversation about decisions, not an audit. Nobody certifies a workload as passing.

</details>

## Enrichment: harder tasks for when you pass

These go beyond what the exam asks. There is no single right answer to each, so compare your answer with the model answer and look for the same reasoning, not the same words.

### Task 1: write the core of the bakery recommendation

The bakery owner from the [module brief](00-brief.md) now says: "I want to move the ordering site, but the till stays in the shop, and I don't want to pay for anything fancy." Write four or five sentences for the recommendation. Name the deployment model, the two benefits that matter most to her, the one cost habit that makes the move pay off, and one trade-off she can accept and one she can't.

<details><summary>Model answer</summary>

Move the ordering site to the cloud and keep the till in the shop; with the two connected, that is a hybrid deployment. The benefit that fixes December is elasticity: capacity grows with holiday orders and shrinks in January, so the site stops dropping orders and stops paying for idle servers. Agility comes second: trying a new product page takes an afternoon, not a purchase. The move only saves money if capacity really comes down after the peak; renting peak capacity all year would cost more than owning. She can accept a cheap, unreliable test copy of the site, but not weaker security anywhere: the account needs MFA and separate identities from the first day.

Check that your answer names hybrid (not cloud), ties elasticity to December, warns about scaling down, and keeps security out of the trade.

</details>

### Task 2: one company, two workloads

A company has two workloads. A payroll system runs at the same load all day, every day, on servers it bought last year. Its marketing website is quiet most of the year and very busy for two weeks around a product launch. A board member says, "The cloud is cheaper. Move both now." Write a short reply: which workload you would move first and why, and what you would compare before moving the other.

<details><summary>Model answer</summary>

Move the marketing website first. Its demand swings a lot, so paying by use, with capacity that follows demand, removes a lot of idle capacity and stops the launch from overloading the site. For payroll, the case is weaker today: steady demand leaves little capacity to give back, and its servers are already paid for. Before moving it, compare its full on-premises cost (space, power, staff, licenses and the next hardware refresh) with real cloud prices for steady use, including AWS's discounts for committed use (Module 11). The decision should come from data about each workload, which is what [COST06-BP02 Select resource type, size, and number based on data](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html) asks for, not from a rule that the cloud is always cheaper.

</details>

### Task 3: when is a second Availability Zone worth paying for?

The bakery's site now runs in the cloud on one server in one Availability Zone, to keep the bill small. Using the reliability pillar's design principle "[Scale horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)" and the cost best practice [COST09-BP03 Supply resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html), propose a design that protects December orders without paying for a second copy all year. Say what you trade, and why it is an acceptable trade.

<details><summary>Model answer</summary>

Keep one small server in January and other quiet months, when an outage would lose few orders and a few hours of downtime is an acceptable risk. Ahead of the holiday season, run copies in at least two Availability Zones, so a failure in one doesn't stop orders, and let capacity grow with demand. After the peak, remove the extra copies. This spreads the work across several smaller resources in separate AZs when a failure would cost the most, and supplies resources when demand needs them, so the bakery pays for the extra reliability only in the months it matters. The trade is lower reliability in quiet months for lower cost, a reliability-against-cost trade the Framework accepts. Security stays the same all year: the same MFA-protected identities and permissions apply to every copy.

</details>

---

"Module 02 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
