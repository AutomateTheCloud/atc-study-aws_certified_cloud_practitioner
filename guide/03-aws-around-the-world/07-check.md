---
type: check
id: clf-03-07
title: "Module 03 mastery check"
tasks: ["3.2", "1.1"]
objectives: ["03.01a", "03.02a", "03.03a", "03.04a"]
reader: "Adult studying alone, possibly new to IT, who has finished the Module 03 lessons; about 20 minutes for each check; works on a phone"
prerequisites: [clf-03-01, clf-03-02, clf-03-03, clf-03-04]
pillars: [reliability, performance-efficiency, cost-optimization]
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html"
  - "https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html"
  - "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html"
  - "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html"
  - "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"
  - "https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html"
  - "https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"
---

# Module 03 mastery check: show that you can place a workload in the world and keep it running

**For:** an adult studying alone, possibly new to IT, who has finished lessons [03.01](01-regions-availability-zones-data-centers.md) to [03.04](04-the-edge.md). **Time:** about 20 minutes per check.

## How to use this check

Take **Check A** closed-book, then open the answers. A "(Select TWO.)" question counts only if both choices are right. With **8 or more right (80%)**, go on to Module 04. Otherwise, reread what the [correction map](#correction-map) names for your misses, then take **Check B**, a parallel retest.

## Check A

**A1.** Which description of AWS's infrastructure, from largest to smallest, is accurate?

- A. A Region holds two or more AZs, and each AZ is exactly one data center.
- B. A Region holds at least three AZs, and each AZ holds one or more data centers.
- C. An AZ holds several Regions, and each Region is one large data center.
- D. A data center holds several AZs, which share its power and network.

<details><summary>Answer</summary>

**B is right.** That is AWS's description.

- **A is wrong.** Three AZs at least, and an AZ can be several data centers.
- **C is wrong.** It reverses the nesting.
- **D is wrong.** AZs don't share power, and data centers sit inside AZs.

</details>

**A2.** A news site runs web servers in `us-east-1a` and `us-east-1b` behind a load balancer, and an Amazon RDS Multi-AZ database with the main copy in `us-east-1a` and the standby in `us-east-1b`. Then `us-east-1a` loses power. Which two things happen? (Select TWO.)

- A. The load balancer sends readers' requests to the web server in `us-east-1b`.
- B. The site stops, because both AZs are in the same Region.
- C. The standby database in `us-east-1b` takes over from the main copy.
- D. AWS moves the stopped web server to `us-east-1c` by itself.
- E. An edge location runs the site until the power returns.

<details><summary>Answer</summary>

**A and C are right.** The load balancer skips the failed server; the standby takes over.

- **B is wrong.** AZs fail separately.
- **D is wrong.** An EC2 server is zonal; AWS doesn't move it.
- **E is wrong.** Edge locations don't run your servers.

</details>

**A3.** A company's head office is in Paris, but nearly all its customers live in southern Germany. A contract requires their data to stay in the European Union (EU). Every Region considered offers the services it needs. Which Region should it choose?

- A. Europe (Paris), because the company's head office is there
- B. Europe (Zurich), because it is the closest Region to the customers
- C. Europe (Frankfurt), because it is the closest Region inside the EU
- D. US East (N. Virginia), because the guide's labs use it

<details><summary>Answer</summary>

**C is right.** After the EU rule, Frankfurt, in Germany, is closest to the customers.

- **A is wrong.** What matters is where the *users* are.
- **B is wrong.** Zurich is in Switzerland, outside the EU.
- **D is wrong.** The data would leave the EU.

</details>

**A4.** Four teams each ask for a second AWS Region. Which request has the strongest reason?

- A. A staff app used in one city, whose goals two AZs already meet
- B. An online shop that wants to keep taking orders if one data center loses power
- C. A blog whose owner thinks its Region's three AZs are too few for high availability
- D. A video-call service with large groups of users in Japan and in Brazil, who both complain about delay

<details><summary>Answer</summary>

**D is right.** Low latency for users far apart is one of the four reasons.

- **A is wrong.** A second Region only adds cost here.
- **B is wrong.** That's a job for several AZs.
- **C is wrong.** Two AZs already give high availability.

</details>

**A5.** A ride-booking app's users are almost all in South Africa and expect instant responses. No data rules apply, and both Regions considered offer every service it needs. Africa (Cape Town) charges more than Europe (Ireland). Which choice is best justified?

- A. Europe (Ireland), because price decides between Regions that pass both filters
- B. Africa (Cape Town), because nearness to users justifies the higher price
- C. Europe (Ireland), because European Regions have more AZs
- D. Both Regions, to share the higher price

<details><summary>Answer</summary>

**B is right.** With every user thousands of kilometers from Ireland, latency justifies the price.

- **A is wrong.** Price decides only when latency is similar.
- **C is wrong.** AZ count isn't a factor; every Region has at least three.
- **D is wrong.** A second Region adds cost for no gain.

</details>

**A6.** An internal reporting tool can be down for a day if its Region is lost (RTO) and can lose up to 12 hours of data (RPO). The team proposes multi-site active/active. Which assessment is best?

- A. Keep the proposal, because active/active is the safest choice for any workload.
- B. Replace it with a pilot light, the cheapest strategy that meets a one-day RTO.
- C. Drop disaster recovery, because two AZs already cover losing the Region.
- D. Replace it with backup and restore, which meets both objectives at a much lower cost.

<details><summary>Answer</summary>

**D is right.** It recovers in hours, and backups every few hours keep loss under 12 hours, at the lowest cost.

- **A is wrong.** Unneeded protection wastes money every month.
- **B is wrong.** A pilot light works but costs more.
- **C is wrong.** Two AZs go down with their Region.

</details>

**A7.** A clinic's last good backup was at 01:00. At 07:30 its booking database is lost. At 09:00 it's taking bookings again, restored from that backup. Its RTO is 2 hours and its RPO is 4 hours. Which objective did the recovery meet?

- A. Both objectives
- B. Only the RPO
- C. Only the RTO
- D. Neither objective

<details><summary>Answer</summary>

**C is right.** Downtime, 07:30 to 09:00, is 1.5 hours: inside the RTO. Data lost, back to 01:00, is 6.5 hours: over the RPO.

- **A and D are wrong.** Only the RTO was met.
- **B is wrong.** It swaps the two.

</details>

**A8.** An online store runs in three AZs with an Amazon RDS Multi-AZ database, keeps a warm standby in a second Region, and takes a database snapshot every night. Which two claims are accurate? (Select TWO.)

- A. "Our Multi-AZ standby lets us undo a mistaken change to the data."
- B. "Our warm standby protects us if our main Region is lost."
- C. "Running in three AZs means we need no plan for losing the Region."
- D. "Our nightly snapshots let us go back to before a mistaken deletion."
- E. "Copying data to the other Region within seconds replaces our snapshots."

<details><summary>Answer</summary>

**B and D are right.** The warm standby covers losing the Region; the snapshots are point-in-time copies that undo a mistake.

- **A is wrong.** The standby receives the mistake too.
- **C is wrong.** All three AZs are in one Region.
- **E is wrong.** The other Region receives deletions within seconds too.

</details>

**A9.** Which pairing of a place and its purpose is correct?

- A. Local Zone: inside a telecom carrier's 5G network, for apps on mobile devices
- B. Edge location: inside an AZ, for running web servers near users
- C. Outposts: in the customer's own building, for systems and data that must stay on site
- D. AZ: in many cities outside the Regions, for caching web content

<details><summary>Answer</summary>

**C is right.** Outposts puts AWS-managed hardware in the customer's site.

- **A is wrong.** That's Wavelength (out of scope).
- **B is wrong.** Edge locations never run your servers.
- **D is wrong.** That describes edge locations.

</details>

**A10.** A shop uses Amazon Route 53 and Amazon CloudFront. A customer in Spain types the shop's address, and the photos load quickly. Which describes each service's job?

- A. Route 53 told the browser where to go; CloudFront served the photos from a nearby edge location.
- B. Route 53 served the cached photos; CloudFront told the browser where the site is.
- C. Both services kept cached copies of the photos at edge locations near the customer.
- D. Route 53 ran the shop's web server at the edge; CloudFront stored the original photos.

<details><summary>Answer</summary>

**A is right.** Route 53 (DNS) answers "where is this site?"; CloudFront (the CDN) serves cached copies nearby.

- **B is wrong.** It swaps the two.
- **C is wrong.** Only CloudFront caches.
- **D is wrong.** No service runs your web servers at the edge.

</details>

## Correction map

| Questions | Objective | Reread |
|---|---|---|
| A1, B1 | 03.01a | [A data center is a building](01-regions-availability-zones-data-centers.md#a-data-center-is-a-building-an-availability-zone-is-one-or-more-of-them) |
| A2, B2 | 03.01a | [High availability means more than one AZ](01-regions-availability-zones-data-centers.md#high-availability-means-running-in-more-than-one-availability-zone) |
| A3, B3 | 03.02a | [Rules first](02-choosing-a-region.md#rules-first-decide-where-the-data-may-live) |
| A4, B4 | 03.02a | [More than one Region](02-choosing-a-region.md#use-more-than-one-region-only-when-you-have-a-reason) |
| A5, B5 | 03.02a | [Services, latency and price](02-choosing-a-region.md#then-services-latency-and-price) |
| A6, B6 | 03.03a | [Four strategies](03-surviving-failure.md#four-strategies-from-cheap-and-slow-to-costly-and-fast); [Simulation S2](06-sim-blast-radius.md) |
| A7, B7 | 03.03a | [RTO and RPO](03-surviving-failure.md#rto-and-rpo-how-long-you-can-be-down-and-how-much-you-can-lose) |
| A8, B8 | 03.03a | [HA vs DR](03-surviving-failure.md#high-availability-and-disaster-recovery-answer-different-questions); [replication vs backup](03-surviving-failure.md#replication-copies-your-mistakes-backups-undo-them) |
| A9, B9 | 03.04a | [Local Zones, Outposts and Wavelength](04-the-edge.md#local-zones-outposts-and-wavelength-run-aws-servers-outside-a-region) |
| A10, B10 | 03.04a | [Three services use the edge](04-the-edge.md#three-services-use-the-edge-each-in-its-own-way) |

## Check B: parallel retest

Same rules: closed-book, 8 of 10 to pass.

**B1.** An engineer says: "An AZ is one data center, so 'survive losing a data center' and 'survive losing an AZ' each need their own design." Which correction is accurate?

- A. The engineer is right.
- B. An AZ can hold several data centers, and copies in a second AZ meet both requirements.
- C. Losing one data center takes down the Region, so both need a second Region.
- D. Copies in different data centers of one AZ meet the first requirement.

<details><summary>Answer</summary>

**B is right.** You can't choose a building, so copies in two AZs cover both.

- **A is wrong.** An AZ is one *or more* data centers.
- **C is wrong.** One building can't take down a Region.
- **D is wrong.** You can't choose a data center inside an AZ.

</details>

**B2.** Which two designs, in one Region, keep working if one AZ fails? (Select TWO.)

- A. Two web servers in different AZs behind a load balancer, with an Amazon RDS Multi-AZ database
- B. Four web servers in one AZ behind a load balancer, with an Amazon RDS Multi-AZ database
- C. An application built only from AWS Lambda functions and objects in Amazon S3 Standard
- D. Two web servers in different AZs behind a load balancer, with one database server in one of those AZs
- E. One large server running the site and its database, sized for twice the busiest day

<details><summary>Answer</summary>

**A and C are right.** A copies every zonal part; C uses only Regional services.

- **B is wrong.** The web servers share one AZ.
- **D is wrong.** The one database server is a single point of failure.
- **E is wrong.** Size doesn't survive an AZ failing.

</details>

**B3.** A Swiss insurer must keep its customers' data in Switzerland. Its customers are all there, and every Region considered offers the services it needs. Which Region should it choose?

- A. Europe (Frankfurt), the large Region nearest Switzerland
- B. Europe (Ireland), because it is in the EU
- C. US East (N. Virginia), because it offers the most services
- D. Europe (Zurich), because the data rule outranks size, services and price

<details><summary>Answer</summary>

**D is right.** Only a Region in Switzerland passes the rule.

- **A is wrong.** Frankfurt is in Germany.
- **B is wrong.** Switzerland isn't in the EU.
- **C is wrong.** It fails the rule.

</details>

**B4.** Four teams each ask for a second AWS Region. Which request has the strongest reason?

- A. A recipe website whose owner feels two AZs "aren't really enough", though they meet its goals
- B. A shop that wants a live copy of its product list in a second Region, in case an employee deletes it
- C. A bank that must keep serving customers even if its whole Region fails
- D. A team that wants its web servers to survive one server's disk failing

<details><summary>Answer</summary>

**C is right.** Business continuity through losing a Region is one of the four reasons.

- **A is wrong.** Two AZs already meet the goals.
- **B is wrong.** A live copy receives the deletion too.
- **D is wrong.** A second server handles that.

</details>

**B5.** A survey company must keep its data in the EU, and its respondents are spread across the EU. It has shortlisted two EU Regions, P and Q, which both offer every service it needs with similar latency. Q charges less. Which choice is best justified?

- A. Region Q, because it costs less and nothing else separates them
- B. Region P, because the pricier Region always performs better
- C. Both Regions, so each respondent gets the nearer one
- D. The Region closest to the company's office

<details><summary>Answer</summary>

**A is right.** With latency about equal, price decides.

- **B is wrong.** Price reflects local costs.
- **C is wrong.** A second Region solves nothing here.
- **D is wrong.** The office isn't a reason.

</details>

**B6.** A checkout service must take payments again within about 5 minutes if its Region is lost, and can lose only a few minutes of data. Its budget is moderate, and it doesn't want two Regions serving customers every day. The team proposes backup and restore. Which assessment is best?

- A. Accept it, because the cheapest strategy is always right.
- B. Replace it with a pilot light, which keeps app servers off until needed.
- C. Replace it with a warm standby, the cheapest strategy that meets both objectives.
- D. Replace it with multi-site active/active, the only strategy that recovers within minutes.

<details><summary>Answer</summary>

**C is right.** It takes payments at once and scales up within minutes.

- **A is wrong.** Backup and restore takes hours; pick the cheapest *that meets both*.
- **B is wrong.** A pilot light typically needs tens of minutes.
- **D is wrong.** It isn't the only one, and it serves daily from both.

</details>

**B7.** A shop's last backup was at 22:00. At 03:00 its order database is lost. At 06:30 it's taking orders again, restored from that backup. Its RTO is 3 hours and its RPO is 6 hours. Which objective did the recovery meet?

- A. Only the RPO
- B. Only the RTO
- C. Both objectives
- D. Neither objective

<details><summary>Answer</summary>

**A is right.** Data lost, back to 22:00, is 5 hours: inside the RPO. Downtime, to 06:30, is 3.5 hours: over the RTO.

- **B is wrong.** It swaps the two.
- **C and D are wrong.** Only the RPO was met.

</details>

**B8.** Which two statements in a payments team's resilience plan are accurate? (Select TWO.)

- A. "Our standby database in a second AZ covers us if the whole Region fails."
- B. "Point-in-time backups let us return to before an attacker changed our data."
- C. "Our pilot light copies our data continuously to the recovery Region."
- D. "Because our data reaches another Region within seconds, we can stop taking backups."
- E. "High availability across two AZs is our plan for a Region outage."

<details><summary>Answer</summary>

**B and C are right.** A backup stopped changing before the attack; a pilot light copies data continuously.

- **A is wrong.** Both AZs are in one Region.
- **D is wrong.** Replication carries the attacker's changes too.
- **E is wrong.** High availability isn't disaster recovery.

</details>

**B9.** Which pairing of a place and its purpose is correct?

- A. Wavelength Zone: inside the customer's own building, for controlling factory machines
- B. Outposts: at edge locations around the world, for caching web content near users
- C. Edge location: inside a Region's AZs, for running customers' databases
- D. Local Zone: in a large city away from its parent Region, for very low latency there

<details><summary>Answer</summary>

**D is right.** A Local Zone gives single-digit-millisecond latency in a large city.

- **A is wrong.** Wavelength is in 5G networks (out of scope); a building means Outposts.
- **B is wrong.** Outposts runs in your building; caching is CloudFront.
- **C is wrong.** Edge locations never run your databases.

</details>

**B10.** Which statement about Amazon CloudFront and AWS Global Accelerator is accurate?

- A. Both keep cached copies of content at edge locations near users.
- B. Global Accelerator keeps cached copies; CloudFront only answers DNS lookups.
- C. CloudFront keeps cached copies near users; Global Accelerator carries traffic without caching.
- D. Both run customers' application servers inside edge locations near users.

<details><summary>Answer</summary>

**C is right.** Global Accelerator carries traffic over AWS's network and keeps no copies.

- **A is wrong.** Only CloudFront caches.
- **B is wrong.** It swaps them; DNS is Route 53's job.
- **D is wrong.** No service runs your servers at the edge.

</details>

---

"Module 03 mastery check" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
