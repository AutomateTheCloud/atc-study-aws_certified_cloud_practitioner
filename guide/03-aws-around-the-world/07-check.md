---
type: check
id: clf-03-07
title: "Module 03 mastery check"
tasks: ["3.2", "1.1"]
objectives: ["03.01a", "03.02a", "03.03a", "03.04a"]
reader: "Adult studying alone, possibly new to IT; end of Module 03; about 25 minutes for each check; works on a phone"
prerequisites: [clf-03-01, clf-03-02, clf-03-03, clf-03-04]
pillars: [reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-24
sources:
  - "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
  - "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html"
  - "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"
  - "https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html"
  - "https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"
---

# Module 03 mastery check: show that you can place a workload in the world and keep it running

This check tells you whether you can use the ideas of Module 03 in new situations: how Regions, Availability Zones and data centers nest, how to choose a Region, how to choose a way to survive failure, and where each kind of edge site runs. Every question is one you haven't seen before.

**For:** an adult studying alone, possibly new to IT, who has worked through the four lessons of Module 03. **Time:** about 25 minutes for Check A, and the same for Check B if you need it. Reading works on a phone.

## How to use this check

Take **Check A** closed-book: no notes, no lessons, no searching. Answer every question before you open any answer. Then score yourself: each question is worth one point, and a "(Select TWO.)" question scores only if both choices are right.

**You pass at 80%:** 8 of the 10 questions.

- **Below 8:** for each question you missed, use the [correction map](#correction-map) to reread the section it points to, and do the activity it names. Then take **Check B**, the parallel retest. It tests the same ideas with new scenarios, so you can't pass it by remembering Check A's answers.
- **8 or more:** you have mastered the module. Skip Check B and try the [enrichment tasks](#enrichment-harder-tasks-for-when-you-pass) instead.

The questions follow the exam's style: four choices with one answer, or five choices with two answers when the question says "(Select TWO.)". Each answer explains why the right choice is right and why each wrong one is wrong. Read the explanations for the questions you got right, too: a lucky guess looks the same as knowing.

## Check A

**A1.** A new engineer sketches AWS's infrastructure as boxes inside boxes, from the largest box to the smallest. Which sketch matches AWS's description?

- A. A Region holds two or more Availability Zones, and each Availability Zone is exactly one data center.
- B. A Region holds at least three Availability Zones, and each Availability Zone holds one or more data centers.
- C. An Availability Zone holds several Regions, and each Region is one large data center.
- D. A data center holds several Availability Zones, which share its power and its network.

<details><summary>Answer</summary>

**B is right.** The Region is the outer box: an area of the world with at least three Availability Zones. Each AZ is one or more separate data centers, with its own power and network.

- **A is wrong.** It has two common errors. Every Region has at least three AZs, not two. And an AZ can be several data centers, not exactly one.
- **C is wrong.** It reverses the nesting. Regions contain AZs.
- **D is wrong.** AZs don't share power or a network; they are built to stay separate. And a data center sits inside an AZ, not the other way round.

</details>

**A2.** A news site runs one web server in `us-east-1a` and one in `us-east-1b`, behind a load balancer. Its Amazon RDS database uses Multi-AZ: the main copy is in `us-east-1a` and the standby is in `us-east-1b`. Then `us-east-1a` loses power. Which two things happen? (Select TWO.)

- A. The load balancer sends readers' requests to the web server in `us-east-1b`.
- B. The site stops, because both Availability Zones are in the same Region.
- C. The standby database in `us-east-1b` takes over from the main copy.
- D. AWS moves the stopped web server from `us-east-1a` to `us-east-1c` by itself.
- E. Readers are served from an edge location, which runs the site until the power returns.

<details><summary>Answer</summary>

**A and C are right.** Every part the site needs has a copy in `us-east-1b`. The load balancer skips the server that fails its health checks, and the Multi-AZ standby takes over as the database. That is how running in more than one AZ gives high availability.

- **B is wrong.** AZs in one Region are built to fail separately: separate power, cooling and network. A power cut in one doesn't reach the other.
- **D is wrong.** An EC2 server is zonal: it lives in one AZ and fails with it. AWS doesn't move it to another AZ for you; the copy you placed in `us-east-1b` is what keeps the site going.
- **E is wrong.** Edge locations run networking services such as Amazon CloudFront, not your web servers or database.

</details>

**A3.** A company's head office is in Paris, but nearly all its customers live in southern Germany. A contract requires the customers' data to stay inside the European Union (EU). Every service it needs is offered in all the Regions it is considering. Which Region should it choose, and why?

- A. Europe (Paris), because the company's head office is there
- B. Europe (Zurich), because it is the closest Region to the customers
- C. Europe (Frankfurt), because it is the closest Region inside the EU
- D. US East (N. Virginia), because the guide's labs use it

<details><summary>Answer</summary>

**C is right.** Apply the filters in order. The rule comes first: only Regions in EU countries pass. Services remove nothing here. Among the Regions left, the one closest to the customers gives them the lowest latency, and Frankfurt is in Germany.

- **A is wrong.** Paris passes the EU rule, but what matters is where the *users* are, not the office. The Well-Architected Framework names choosing a Region by your own location as a common mistake.
- **B is wrong.** Zurich is in Switzerland, which isn't in the EU. A Region's name and nearness never rescue it from a rule it breaks.
- **D is wrong.** It fails the rule: the data would leave the EU. It is also far from the customers.

</details>

**A4.** Four teams each ask for their workload to run in a second AWS Region. Which request has the strongest reason?

- A. A staff holiday-booking app, used in one city, whose goals are already met by two Availability Zones
- B. An online shop that wants to keep taking orders if a single data center loses power
- C. A blog in a Region with three Availability Zones, whose owner thinks three is too few for high availability
- D. A video-call service with large groups of users in Japan and in Brazil, who both complain about delay

<details><summary>Answer</summary>

**D is right.** Low latency for users far apart is one of the four reasons the exam guide gives for using more than one Region. Users on two continents can't both be close to one Region, so a copy near each group fixes the delay.

- **A is wrong.** A second Region costs more and is harder to run. When two AZs already meet the goals, AWS's guidance names going multi-Region as a common mistake.
- **B is wrong.** Surviving the loss of one data center is a job for several AZs in one Region, not for a second Region.
- **C is wrong.** Three AZs is the minimum every Region has, and two AZs are enough for high availability. Having "too few" AZs isn't a reason to add a Region.

</details>

**A5.** A ride-booking app has almost all of its users in South Africa, and riders expect every screen to respond at once. There are no rules about where its data lives, and every service it needs is in both Regions it is considering. The team finds that Africa (Cape Town) charges more for the same services than Europe (Ireland). Which choice is best justified?

- A. Europe (Ireland), because price decides between any Regions that pass both filters
- B. Africa (Cape Town), because being near the users justifies paying the higher price
- C. Europe (Ireland), because Regions in Europe have more Availability Zones to use
- D. Both Regions, so that the higher price is shared across the two Regions

<details><summary>Answer</summary>

**B is right.** Both Regions pass the two filters (rules and services), so latency and price are weighed against each other. Here nearly every user is in South Africa, and Ireland is thousands of kilometers away, which puts a floor under every request's delay. AWS's cost guidance says to pay for a higher-priced Region when latency requires it.

- **A is wrong.** Price ranks the shortlist, but it doesn't outweigh latency for users who are all far from the cheaper Region. It decides when the latency difference is small.
- **C is wrong.** Every Region has at least three AZs, and the number of AZs isn't one of the four things that decide a Region choice.
- **D is wrong.** A second Region adds cost and work; it doesn't share or lower a price. Nothing here calls for more than one Region.

</details>

**A6.** A company's internal reporting tool can be down for a day if its Region is lost (RTO), and it can lose up to 12 hours of data (RPO). Its team proposes multi-site active/active, with full copies serving users in two Regions. Which assessment is best?

- A. Keep the proposal, because active/active is the safest choice for any workload.
- B. Replace it with a pilot light, the cheapest strategy that meets a one-day RTO.
- C. Drop disaster recovery, because running in two AZs already covers losing the Region.
- D. Replace it with backup and restore, which meets both objectives at a much lower cost.

<details><summary>Answer</summary>

**D is right.** Pick the cheapest strategy that meets both numbers. Backup and restore typically recovers in hours, well inside a day, and backups every few hours keep the data loss under 12 hours. Active/active would cost the most of all four strategies, every month, to buy recovery speed the business doesn't need.

- **A is wrong.** More protection than the business needs is wasted money. AWS's guidance is to size the plan to what the outage would cost.
- **B is wrong.** A pilot light would also meet the objectives, but it isn't the cheapest: it keeps a database running in the recovery Region all the time. Backup and restore costs less.
- **C is wrong.** Two AZs give high availability inside one Region. If the whole Region is lost, both AZs go with it; that needs disaster recovery.

</details>

**A7.** A clinic's booking database is backed up, and the last good backup was taken at 01:00. At 07:30 the database is lost, and bookings stop. At 09:00 the clinic is taking bookings again, restored from that backup. Its RTO is 2 hours and its RPO is 4 hours. Which objective did the recovery meet?

- A. Both objectives
- B. Only the RPO
- C. Only the RTO
- D. Neither objective

<details><summary>Answer</summary>

**C is right.** Measure each one from the failure at 07:30. Downtime runs *forward* to 09:00: 1 hour 30 minutes, inside the 2-hour RTO. Data loss runs *back* to the last backup at 01:00: 6 hours 30 minutes of bookings, more than the 4-hour RPO allows. To meet the RPO, the clinic needs a saved copy at least every 4 hours.

- **A is wrong.** The data loss, 6 hours 30 minutes, is above the RPO.
- **B is wrong.** It swaps the two. The RTO, time without service, was met; the RPO, the gap back to the last saved point, was missed.
- **D is wrong.** The clinic was back within 1 hour 30 minutes, so the RTO was met.

</details>

**A8.** In a design review, a team makes five claims about its online store. The store runs in three Availability Zones with an Amazon RDS Multi-AZ database, keeps a warm standby in a second Region, and takes a database snapshot every night. Which two claims are accurate? (Select TWO.)

- A. "Our Multi-AZ standby lets us undo a mistaken change to the data."
- B. "Our warm standby protects us if our main Region is lost."
- C. "Running in three AZs means we need no plan for losing the Region."
- D. "Our nightly snapshots let us go back to before a mistaken deletion."
- E. "Copying data to the other Region within seconds replaces our snapshots."

<details><summary>Answer</summary>

**B and D are right.** The warm standby is a separate, working copy in another Region, which is disaster recovery for a Region-wide failure. The nightly snapshots are point-in-time copies that stopped changing, so they can take the data back to before a mistake, losing up to a day of changes.

- **A is wrong.** A standby receives every change within moments, including the mistaken one. Replication copies mistakes; only a backup undoes them.
- **C is wrong.** High availability isn't disaster recovery. All three AZs are in one Region, so losing that Region stops all of them.
- **E is wrong.** The copy in the other Region also receives deletions and corruption within seconds. Even multi-site active/active needs point-in-time backups.

</details>

**A9.** Which pairing of a place and its purpose is correct?

- A. Local Zone: inside a telecom carrier's 5G network, for apps on mobile devices
- B. Edge location: inside an Availability Zone, for running web servers near users
- C. Outposts: in the customer's own building, for systems and data that must stay on site
- D. Availability Zone: in many cities outside the Regions, for caching web content

<details><summary>Answer</summary>

**C is right.** AWS Outposts puts AWS-managed racks or servers in the customer's own data center or site, running AWS services with the same tools as in a Region. The customer provides the space, power and network connection.

- **A is wrong.** That describes AWS Wavelength, which the exam guide lists as out of scope. A Local Zone is in a large city, away from its parent Region.
- **B is wrong.** Edge locations sit outside the Regions, and they never run your own servers. They run networking services such as Amazon CloudFront.
- **D is wrong.** That describes edge locations. An AZ is one or more data centers inside a Region.

</details>

**A10.** An online shop uses Amazon Route 53 and Amazon CloudFront together. A customer in Spain types the shop's web address, and the product photos load quickly. Which describes the job each service did?

- A. Route 53 told the browser where to go; CloudFront served the photos from a nearby edge location.
- B. Route 53 served the cached photos; CloudFront told the browser where the site is.
- C. Both services kept cached copies of the photos at edge locations near the customer.
- D. Route 53 ran the shop's web server at the edge; CloudFront stored the original photos.

<details><summary>Answer</summary>

**A is right.** Route 53 is AWS's DNS service: it answers "where is this site?" with an address. CloudFront is AWS's content delivery network: it keeps copies of content such as photos at edge locations and serves them from the one nearest the user.

- **B is wrong.** It swaps the two. Route 53 isn't a content delivery network; it never delivers the photos.
- **C is wrong.** Only CloudFront caches content. Both run at edge locations, which is why they are often confused.
- **D is wrong.** No service runs your web servers at edge locations, and the original photos live at the origin, such as an S3 bucket in a Region.

</details>

## Correction map

Find each question you missed. Reread the section it names, then read the line under "Another way to see it", which explains the idea differently from the lesson. Then do the activity in the last column, if there is one.

| Question | Objective | Reread | Another way to see it | Practice |
|---|---|---|---|---|
| A1, B1 | 03.01a How the layers nest | [A data center is a building; an Availability Zone is one or more of them](01-regions-availability-zones-data-centers.md#a-data-center-is-a-building-an-availability-zone-is-one-or-more-of-them) and ["A Region can have just two AZs" is wrong](01-regions-availability-zones-data-centers.md#a-region-can-have-just-two-azs-is-wrong) | You can only point at two of the three boxes: a Region and an AZ. AWS never tells you which building you are in, so the AZ is the smallest unit you can design around | [Lab 02](05-lab-02-see-the-global-infrastructure.md), steps 9 to 11 |
| A2, B2 | 03.01a How nesting gives high availability | [Where your resources live: in one AZ, across a Region, or everywhere](01-regions-availability-zones-data-centers.md#where-your-resources-live-in-one-az-across-a-region-or-everywhere) and [High availability means running in more than one Availability Zone](01-regions-availability-zones-data-centers.md#high-availability-means-running-in-more-than-one-availability-zone) | Cross out one AZ on a drawing of the design. For every part the site needs, ask: is there a copy left outside the crossed-out AZ? Any "no" is a single point of failure | The worked example and "Your turn" in that section |
| A3, B3 | 03.02a Choose a Region | [Rules first: decide where the data may live](02-choosing-a-region.md#rules-first-decide-where-the-data-may-live) and ["Choose the Region nearest your office" is wrong](02-choosing-a-region.md#choose-the-region-nearest-your-office-is-wrong) | Treat the rule like a locked door: look up the Region's country, not its name, and cross out every Region behind the door. Only then measure the distance from the remaining Regions to the users | The mixed practice in that lesson |
| A4, B4 | 03.02a Justify more than one Region | [Use more than one Region only when you have a reason](02-choosing-a-region.md#use-more-than-one-region-only-when-you-have-a-reason) | Ask what the second Region would protect or fix that a second AZ can't. If the answer is "a data center" or "an AZ", the second Region is the wrong tool | The "Your turn" in that section |
| A5, B5 | 03.02a Weigh latency and price | [Pick the shortlisted Region closest to your users](02-choosing-a-region.md#pick-the-shortlisted-region-closest-to-your-users) and [Weigh the price](02-choosing-a-region.md#weigh-the-price-the-same-thing-costs-different-amounts-in-different-regions) | Latency and price are weights on a scale, used only after the filters. A large gap in distance to the users outweighs a price difference; when the distances are similar, price tips the scale | The Check in the price section |
| A6, B6 | 03.03a Choose a recovery strategy | [Four strategies, from cheap and slow to costly and fast](03-surviving-failure.md#four-strategies-from-cheap-and-slow-to-costly-and-fast) | Walk up the stairs from the cheapest step and stop at the first one that meets both numbers. Every higher step also works, but costs more every month, disaster or not | [Simulation S2](06-sim-blast-radius.md), decisions 3 and 4 |
| A7, B7 | 03.03a RTO and RPO | [RTO and RPO: how long you can be down, and how much you can lose](03-surviving-failure.md#rto-and-rpo-how-long-you-can-be-down-and-how-much-you-can-lose) | Put the failure in the middle of a time line. RPO looks back to the last saved copy; RTO looks forward to the restart. Check each against its own limit, separately | The Check in that section |
| A8, B8 | 03.03a High availability, recovery and backups | [High availability and disaster recovery answer different questions](03-surviving-failure.md#high-availability-and-disaster-recovery-answer-different-questions) and [Replication copies your mistakes; backups undo them](03-surviving-failure.md#replication-copies-your-mistakes-backups-undo-them) | A replica is a mirror: it shows the data as it is now, damage included. A backup is a photograph: it shows the data as it was. You need the photograph to undo damage | [Simulation S2](06-sim-blast-radius.md), decisions 1, 2 and 5 |
| A9, B9 | 03.04a Where each site runs | [Region, AZ, edge location, Local Zone, Outposts: where is it?](04-the-edge.md#region-az-edge-location-local-zone-outposts-where-is-it) | Say each name with a place: Outposts, "in my building"; Local Zone, "in that city"; edge location, "near users everywhere, no servers of mine"; Wavelength, "inside the phone network" | The Check in [Local Zones, Outposts and Wavelength run AWS servers outside a Region](04-the-edge.md#local-zones-outposts-and-wavelength-run-aws-servers-outside-a-region) |
| A10, B10 | 03.04a What each edge service is for | [Three services use the edge, each in its own way](04-the-edge.md#three-services-use-the-edge-each-in-its-own-way) | Route 53 gives directions, CloudFront hands over a stored copy, and Global Accelerator provides a fast private road. Only CloudFront keeps copies | The Check in that section |

## Check B: parallel retest

Take Check B only after you have worked through the correction map for the questions you missed. Use the same rules as Check A: closed-book, one point a question, and 8 of 10 to pass. If you pass, go on to Module 04. If not, use the correction map again for the questions you missed, and retry the practice questions at the end of each lesson before you take Check A again on another day.

**B1.** An engineer says: "An Availability Zone is one data center. So 'survive losing a data center' and 'survive losing an AZ' are two different requirements, and each needs its own design." Which correction is accurate?

- A. The engineer is right: because an AZ is one data center, each requirement needs its own design.
- B. An AZ can hold several data centers, and copies in a second AZ meet both requirements.
- C. Losing one data center takes down the whole Region, so both requirements need a second Region.
- D. You can place copies in different data centers of one AZ, so one AZ meets the first requirement.

<details><summary>Answer</summary>

**B is right.** AWS describes an AZ as one or more data centers, and you can't tell which building your resources are in. So you can't design around a building: the smallest unit you can choose is the AZ. A design with copies in two AZs survives losing a data center and losing a whole AZ, so one design meets both requirements.

- **A is wrong.** An AZ is *one or more* data centers, not exactly one. And the two requirements don't need different designs: copies in a second AZ cover both.
- **C is wrong.** A data center sits inside an AZ, and AZs are built to fail separately. One building can't take down a whole Region.
- **D is wrong.** AWS doesn't let you choose a data center inside an AZ. With everything in one AZ, that AZ is a single point of failure.

</details>

**B2.** A company compares five designs for its web application in one Region. Which two would keep working if one Availability Zone failed? (Select TWO.)

- A. Two web servers in different AZs behind a load balancer, with an Amazon RDS Multi-AZ database
- B. Four web servers in one AZ behind a load balancer, with an Amazon RDS Multi-AZ database
- C. An application built only from AWS Lambda functions and objects stored in Amazon S3 Standard
- D. Two web servers in different AZs behind a load balancer, with one database server in one of those AZs
- E. One large web server and its database on the same server, sized for twice the busiest day

<details><summary>Answer</summary>

**A and C are right.** In A, every zonal part has a copy in a second AZ: the web servers, and the database through its Multi-AZ standby. In C, both services are Regional: AWS already runs Lambda across several AZs and stores S3 Standard objects across at least three, so there is no single AZ to lose.

- **B is wrong.** All four web servers are in one AZ. If it fails, the web tier stops, even though the database could fail over.
- **D is wrong.** The only database server is a single point of failure. If its AZ fails, the web servers in the other AZ have no database to use.
- **E is wrong.** Size doesn't protect against failure. One server in one AZ fails with that AZ, however large it is.

</details>

**B3.** A Swiss insurer must keep its customers' data in Switzerland, under a Swiss regulation. All its customers are in Switzerland, and every service it needs is offered in the Regions it is considering. Which Region should it choose?

- A. Europe (Frankfurt), because it is the large Region nearest to Switzerland
- B. Europe (Ireland), because it is inside the European Union
- C. US East (N. Virginia), because it offers the most services
- D. Europe (Zurich), because the data rule outranks size, services and price

<details><summary>Answer</summary>

**D is right.** The rule comes first: the data must stay in Switzerland, so only a Region in Switzerland passes. AWS lists Europe (Zurich) as being in Switzerland. It is also closest to the customers, so latency agrees.

- **A is wrong.** Frankfurt is in Germany. Being close to Switzerland doesn't move the data inside the country, and nearness never rescues a Region that breaks a rule.
- **B is wrong.** The rule here is Switzerland, not the EU. Switzerland isn't in the EU, so an EU Region fails the rule.
- **C is wrong.** It fails the rule, and the number of services matters only when a Region lacks one you need.

</details>

**B4.** Four teams each ask for a second AWS Region. Which request has the strongest reason?

- A. A recipe website whose owner feels two Availability Zones "aren't really enough", although she agrees they meet its goals
- B. An online shop that wants a live copy of its product list in a second Region, in case an employee deletes it
- C. A bank that must keep serving its customers even if its whole Region fails
- D. A team that wants its web servers to keep running when the disk in one server fails

<details><summary>Answer</summary>

**C is right.** Business continuity through the loss of a whole Region is one of the four reasons the exam guide gives for using more than one Region. Several AZs can't cover it, because all of them sit inside the Region that fails. (The bank would still check that its data rules allow the second Region it picks.)

- **A is wrong.** When two AZs meet the goals, a second Region adds cost and work for no gain. AWS's guidance names this as a common mistake.
- **B is wrong.** A live copy receives every change, so the deletion would reach the second Region within moments. Point-in-time backups protect against mistakes, not a live copy elsewhere.
- **D is wrong.** A failed disk is the smallest failure. A second server, ideally in a second AZ, handles it inside one Region.

</details>

**B5.** A survey company must keep its data inside the EU. Its respondents are spread evenly across the EU. It has shortlisted two EU Regions, which we call P and Q here. Both offer every service it needs, and both give its respondents similar latency. Region Q charges less for the same services. Which choice is best justified?

- A. Region Q, because it costs less and nothing else separates them
- B. Region P, because the more expensive Region always performs better
- C. Both Regions, so that each respondent is always served by the nearer of the two
- D. The Region closest to the company's own office, since its staff run the survey

<details><summary>Answer</summary>

**A is right.** Rules and services are the filters, and both Regions passed. Latency and price then rank the shortlist. With latency about equal, price decides, and AWS's cost guidance is to prefer the lower-priced Region when nothing requires the other.

- **B is wrong.** Price reflects local costs such as land, power and taxes, not better performance.
- **C is wrong.** Latency is already similar for everyone, so a second Region adds cost and work without solving a problem.
- **D is wrong.** Closeness to your office isn't a reason at all; what matters is where your users are.

</details>

**B6.** An online checkout service must be taking payments again within about 5 minutes if its Region is lost, and it can lose only a few minutes of data. Its budget is moderate, and it doesn't want two Regions serving customers every day. To save money, its team proposes backup and restore. Which assessment is best?

- A. Accept the proposal, because the cheapest strategy is always the right one.
- B. Replace it with a pilot light, which keeps the app servers off until they are needed.
- C. Replace it with a warm standby, the cheapest strategy that meets both objectives.
- D. Replace it with multi-site active/active, the only strategy that recovers within minutes.

<details><summary>Answer</summary>

**C is right.** A warm standby keeps a smaller but complete copy running in the recovery Region. It can take payments at once and scale up within minutes, and its data is copied continuously. That meets both objectives without paying for two Regions serving customers every day.

- **A is wrong.** Backup and restore typically takes hours, which fails a 5-minute RTO. The rule is the cheapest strategy *that meets both objectives*, not the cheapest of all.
- **B is wrong.** A pilot light typically needs tens of minutes, because its app servers must first be switched on. That is too slow for about 5 minutes.
- **D is wrong.** Active/active would meet the objectives, but it isn't the only strategy that does, and it serves customers from both Regions every day, which the company doesn't want.

</details>

**B7.** A shop's order database was last backed up at 22:00. At 03:00 the next morning the database is lost, and orders stop. At 06:30 the shop is taking orders again, restored from that backup. Its RTO is 3 hours and its RPO is 6 hours. Which objective did the recovery meet?

- A. Only the RPO
- B. Only the RTO
- C. Both objectives
- D. Neither objective

<details><summary>Answer</summary>

**A is right.** Measure each one from the failure at 03:00. Data loss runs *back* to the backup at 22:00: 5 hours of orders, inside the 6-hour RPO. Downtime runs *forward* to 06:30: 3 hours 30 minutes, longer than the 3-hour RTO. To meet the RTO, the shop needs a faster restart, for example by rehearsing the restore or moving to a pilot light.

- **B is wrong.** It swaps the two. The RPO, the gap back to the last saved point, was met; the RTO, time without service, was missed.
- **C is wrong.** The downtime, 3 hours 30 minutes, is above the RTO.
- **D is wrong.** The 5 hours of lost orders is inside the 6-hour RPO, so the RPO was met.

</details>

**B8.** A payments team writes five statements in its resilience plan. Which two are accurate? (Select TWO.)

- A. "Our standby database in a second Availability Zone covers us if the whole Region fails."
- B. "Point-in-time backups let us return to before an attacker changed our data."
- C. "Our pilot light copies our data continuously to the recovery Region."
- D. "Because our data reaches another Region within seconds, we can stop taking backups."
- E. "High availability across two Availability Zones is our plan for a Region outage."

<details><summary>Answer</summary>

**B and C are right.** A point-in-time backup stopped changing before the attack, so it can take the data back to a good state. And a pilot light keeps data copied continuously to live databases in the recovery Region, with the app servers off until needed.

- **A is wrong.** Both AZs are in the same Region. A Multi-AZ standby is high availability; losing the whole Region takes it down too.
- **D is wrong.** Replication carries an attacker's changes, deletions and corruption to the other Region within the same seconds. Every strategy still needs point-in-time backups.
- **E is wrong.** High availability isn't disaster recovery. A Region outage needs a separate copy in another Region and a plan to use it.

</details>

**B9.** Which pairing of a place and its purpose is correct?

- A. Wavelength Zone: inside the customer's own building, for controlling factory machines
- B. Outposts: at edge locations around the world, for caching web content near users
- C. Edge location: inside a Region's Availability Zones, for running customers' databases
- D. Local Zone: in a large city away from its parent Region, for very low latency there

<details><summary>Answer</summary>

**D is right.** A Local Zone puts selected AWS services, such as compute and storage, in a large city, and extends a parent Region. It is for users in that city who need single-digit-millisecond latency, or for data that must stay there.

- **A is wrong.** Wavelength Zones are inside telecom carriers' 5G networks, for mobile devices, and the exam guide lists Wavelength as out of scope. The customer's own building is where Outposts runs.
- **B is wrong.** Outposts runs in the customer's own building. Caching web content near users is what CloudFront does at edge locations.
- **C is wrong.** Edge locations sit outside the Regions and never run customers' servers or databases.

</details>

**B10.** Which statement about Amazon CloudFront and AWS Global Accelerator is accurate?

- A. Both keep cached copies of content at edge locations near users.
- B. Global Accelerator keeps cached copies; CloudFront only answers DNS lookups.
- C. CloudFront keeps cached copies near users; Global Accelerator carries traffic without caching.
- D. Both run customers' application servers inside edge locations near users.

<details><summary>Answer</summary>

**C is right.** CloudFront is a content delivery network: it serves cached copies from edge locations and fetches from the origin only when it has no copy. Global Accelerator gives an application fixed addresses announced from edge locations, and carries each user's traffic over AWS's network to the best healthy endpoint in a Region. It keeps no copies, so every request still reaches the application.

- **A is wrong.** Only CloudFront caches. Both use edge locations, which is why they are easy to mix up.
- **B is wrong.** It swaps the caching, and answering DNS lookups is Amazon Route 53's job, not CloudFront's.
- **D is wrong.** No service runs your servers at edge locations. For running servers outside a Region, AWS offers Local Zones and Outposts.

</details>

## Enrichment: harder tasks for when you pass

These go beyond what the exam asks. There is no single right answer to each, so compare your answer with the model answer and look for the same reasoning, not the same words.

### Task 1: defend the bakery's plan against a "safer" idea

The bakery's plan from the [module brief](00-brief.md) runs the US site in US East (N. Virginia) and the German site in Europe (Frankfurt), each across two Availability Zones, with backup and restore for Region disasters. The German partner now says: "To be extra safe, also copy the German backups to US East (Ohio), and let's switch to active/active across both continents." Write four or five sentences in reply.

<details><summary>Model answer</summary>

Copying German customers' backups to Ohio would move their data out of the EU and break the contract, even though the copies are "only backups": a recovery Region inherits the data's rules. If a second copy is wanted, it should go to another EU Region, such as Europe (Ireland) or Europe (Paris). Active/active across continents would also put German data in the US, and it would cost the most of all four strategies every month. The owner accepts a day of phone orders and a few hours of lost orders, which backup and restore already meets. A better use of the money is to test the restore regularly and time it, so the plan is known to work.

Check that your answer rejects the US copy on the data rule, keeps any extra copy inside the EU, and judges active/active by the RTO, RPO and cost, not by how safe it sounds.

</details>

### Task 2: a Region your account can't fully use

A company plans a new workload in US West (N. California), near its users. Its design needs servers in three Availability Zones. When the team lists the AZs in its account, it sees only two. A team member says, "So that Region has only two AZs, and AWS's minimum must be two." What is really going on, and what are the team's options?

<details><summary>Model answer</summary>

The Region has at least three AZs, as every Region does; what the account can *use* is a separate question. AWS notes that newer accounts can use only two AZs in US West (N. California), and that it can stop offering a crowded AZ to new accounts. The team has two options. It can check whether the design really needs three AZs, since two already give high availability. Or it can choose another Region near its users that offers three AZs to its account, if no data rule prevents it. Whatever it decides, it should list the AZs from inside the account, as in [Lab 02](05-lab-02-see-the-global-infrastructure.md), and compare AZ IDs, not names, when it coordinates with other accounts.

</details>

### Task 3: prove the recovery plan works

The bakery's plan relies on backup and restore, with an RTO of about a day and an RPO of a few hours. Using [REL13-BP01 Define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html) and [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html), describe a test the bakery could run twice a year, what it would measure, and what result would make you recommend moving up to a pilot light.

<details><summary>Model answer</summary>

Pick a quiet day and restore the latest backup of the order database into the recovery Region, then rebuild the site there from its infrastructure-as-code templates, without touching the live site. Measure two things. First, the time from the start of the test to the first test order taken in the recovery Region: compare it with the RTO of about a day. Second, the age of the newest data in the restored backup: compare it with the RPO of a few hours. Check that the restored orders are complete and readable, not just that a file came back. Recommend a pilot light only if the business's numbers change (for example, if an outage starts costing much more, and the owner lowers the RTO to under an hour), or if repeated tests show the restore can't fit inside a day. Otherwise, keep backup and restore, fix whatever slowed the test, and write down the results so the next test can be compared with this one.

</details>

---

"Module 03 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
