# Blueprint: Module 06, Running applications: compute

Items file: `practice/items/06-running-applications.yaml`. Exam task 3.3 throughout, with 1.1
(elasticity, high availability), 2.1 (shared responsibility), 3.1 (Outposts as hybrid) and 4.1
(purchasing options, what a stopped instance bills) where a page's front matter lists them.

Targets from the brief: about 75 questions (about 15 "Select TWO") and 18 concept cards. No item
depends on a price. Limits the guide teaches as dated facts (Lambda's 15 minutes, no GPUs on
Fargate) appear only as scenario details far from the boundary, with the check date in the
explanation.

## Objectives

The course plan gives each lesson one objective. The sub-objectives are the lesson's "What you'll
learn" bullets and section headings, so the counts can be checked against the sections.

| Code | Objective (course plan) | Level | Page and sections | Questions (planned / actual) | Cards (planned / actual) |
|---|---|---|---|---|---|
| **06.01a** | Choose an EC2 instance family from a workload's bottleneck | C·Ap | `01-ec2.md`; Lab 08 | **21 / 21** | **4 / 4** |
| | · AMI and the five launch choices | | "An instance is a virtual server started from an image"; "The big picture" | 2 / 2 | 0 / 0 |
| | · Family from the bottleneck (central) | | "Choose the family from the bottleneck"; its worked example | 7 / 8 | 1 / 1 |
| | · Reading a type's name | | "Read an instance type's name from left to right" | 1 / 1 | 1 / 1 |
| | · Types are not purchasing options; the four options (central) | | "Instance types are not purchasing options" | 5 / 5 | 0 / 0 |
| | · Stop vs terminate; what still bills | | "Stopping pauses the instance bill; terminating ends it"; Lab 08 Part C | 4 / 4 | 1 / 1 |
| | · Your side of the line on EC2 | | "Your side of the line on EC2" | 2 / 1 | 1 / 1 |
| **06.02a** | Explain how Auto Scaling and load balancers together give elasticity and high availability | C·Un | `02-auto-scaling-and-load-balancers.md`; Sim S7 | **20 / 20** | **4 / 4** |
| | · What an Auto Scaling group does; min, max, launch template (central) | | "An Auto Scaling group keeps the right number of instances running" | 5 / 5 | 0 / 0 |
| | · Ways to scale: target tracking, scheduled, predictive | | same section; Sim S7 Decision 5 | 3 / 3 | 1 / 1 |
| | · What a load balancer does | | "A load balancer sends each request to a healthy instance" | 1 / 1 | 1 / 1 |
| | · Auto Scaling vs ELB; elasticity vs high availability (central) | | "Auto Scaling changes how many; the load balancer chooses which"; worked example; Sim S7 Decision 4 | 4 / 4 | 2 / 2 |
| | · ALB, NLB, GWLB; Classic is previous generation | | "Choose ALB, NLB or GWLB; Classic is the previous generation" | 4 / 4 | 1 / 1 |
| | · Your side of the line | | "Your side of the line" | 1 / 1 | 0 / 0 |
| | · Simulation: minimum and capacity per hour | | Sim S7 "Decision 1" | 1 / 1 | 0 / 0 |
| | · Exam name AWS Auto Scaling vs Amazon EC2 Auto Scaling | | Auto Scaling section, note | 1 / 1 | 0 / 0 |
| **06.03a** | Pick EC2, Fargate or Lambda for a workload, and say what you manage on each | J·Ap | `03-containers-and-serverless.md`; Lab 07 | **21 / 21** | **6 / 6** |
| | · Containers; ECR, ECS, EKS, Fargate jobs (central) | | "A container packages..."; "Four names, four jobs"; "Fargate orchestrates containers" is wrong | 6 / 6 | 1 / 1 |
| | · Fargate's facts (storage, GPUs) | | "Fargate runs containers without servers to manage" | 2 / 2 | 0 / 0 |
| | · Lambda: events, scaling, state, availability, billing | | "Lambda runs your code only when an event triggers it"; "What you pay for" | 4 / 4 | 2 / 2 |
| | · Lambda vs Fargate vs EC2 (central) | | "Lambda or Fargate..."; worked example | 3 / 3 | 1 / 1 |
| | · Your side of the line (central for 2.1) | | "Your side of the line" | 4 / 4 | 2 / 2 |
| | · Lab 07: execution role, log retention | | Lab 07 "Look at the role", "Read the logs and set retention" | 2 / 2 | 0 / 0 |
| **06.04a** | Match Elastic Beanstalk, Lightsail, Batch and Outposts to their uses | C·Ap | `04-simpler-paths.md` | **15 / 15** | **4 / 4** |
| | · Elastic Beanstalk; not serverless; platform updates | | "Elastic Beanstalk builds and runs the setup for your code" and its misconception | 4 / 4 | 1 / 1 |
| | · Lightsail; stopped still bills; Upgrade to EC2 | | "Lightsail sells a simple server..." | 3 / 3 | 0 / 0 |
| | · EC2 vs Beanstalk vs Lightsail | | "EC2, Elastic Beanstalk or Lightsail..."; worked example | 2 / 2 | 1 / 1 |
| | · Batch | | "Batch runs large numbers of jobs from a queue" | 3 / 3 | 1 / 1 |
| | · Outposts, and its line of responsibility | | "Outposts brings AWS hardware..."; "Your side of the line" | 2 / 2 | 1 / 1 |
| | · What each costs (pricing model, not prices) | | "What you pay for" | 1 / 1 | 0 / 0 |
| **Total** | | | | **77 / 77** | **18 / 18** |

## Mix

- **Selection:** 62 single answer, 15 "Select TWO" (3 in 06.01, 4 in 06.02, 4 in 06.03, 4 in 06.04).
- **Levels:** planned about 15 recall, 35 understanding, 27 application; actual 13 recall (17%), 36
  understanding (47%), 28 application (36%). Three of the module's four objectives are at the apply
  level, so application runs a little above the brief's 30%.
- **Confused pairs covered** (course plan section 7): instance families; ECS, EKS, Fargate, ECR;
  Lambda vs Fargate; Auto Scaling vs ELB; ALB, NLB, GWLB; EC2, Beanstalk, Lightsail.
- **Misconceptions refuted:** On-Demand, Reserved and Spot are instance types; Fargate orchestrates;
  Auto Scaling spreads traffic; Classic is a current peer of ALB; a stopped instance costs nothing;
  Beanstalk is serverless; serverless means AWS handles all security.

## Cards (concept cards only; glossary terms are carded automatically)

06.01: bottleneck-first order; reading a type name around the dot; delete on termination after
terminate; why EC2 puts the most on the customer. 06.02: where elasticity and high availability come
from; the two responses to a failed health check; scaling ahead of a daily rush; choosing ALB, NLB or
GWLB. 06.03: the ECR + ECS + Fargate trio; the Lambda / Fargate / EC2 rule; what stays yours
everywhere; a flawed library in a Fargate image; moving off a retiring Lambda runtime; why Lambda
needs no AZ spreading. 06.04: what you still decide on Beanstalk; what differs among EC2, Beanstalk
and Lightsail; what Batch saves you building on EC2; Outposts' physical-security line.
