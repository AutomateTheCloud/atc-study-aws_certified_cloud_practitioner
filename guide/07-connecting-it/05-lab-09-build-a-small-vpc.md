---
type: lab
id: clf-07-05
title: "Lab 09: Build a small network with a public and a private subnet, then take it apart"
tasks: ["3.5", "2.1"]
objectives: ["07.01a", "07.02a"]
reader: "Adult studying alone, possibly new to IT, who has done Lab 01 and read lessons 07.01 and 07.02; about 50 minutes, plus 5 the next day; a laptop or desktop"
prerequisites: ["clf-02-06", "clf-07-01", "clf-07-02"]
terms_introduced: [CIDR block, local route, main route table, ephemeral port, resource map]
pillars: [security, reliability, cost-optimization]
lab: "09"
rung: L1-L2
mode: real
free_plan: true
signup_path: advanced
time: "50 minutes, plus 5 minutes the next day"
cost: "$0 on the Free plan and on a Paid plan (as of 2026-10-24)"
worst_case: "$0 on a Paid plan if everything is left behind: the VPC, subnets, route tables, internet gateway, security groups and network ACLs have no charge. Only a NAT gateway or a public IPv4 address would bill by the hour, and this lab creates neither"
needs: [guardrails-02, guardrails-03, guardrails-05, guardrails-07, clf-02-06]
last_run_pass: "2026-10-25, standalone Free plan account, advanced sign-up, us-east-1"
recorded: 2026-10-25
facts_checked: 2026-10-25
sources:
  - "https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
  - "https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html"
  - "https://aws.amazon.com/vpc/faqs/"
  - "https://aws.amazon.com/vpc/pricing/"
---

# Lab 09: Build a small network with a public and a private subnet, then take it apart

## Before you start: your account, your responsibility

This guide is provided as is, without warranty. We work hard to keep it correct and current, but AWS changes often, and its services, prices, and free offers may differ from what is written here. The labs run in your own AWS account. You are responsible for that account, for its security, and for any charges it incurs, including charges from resources you forget to delete. Automate the Cloud Inc. is not liable for any costs, losses, or security incidents that result from following, or failing to follow, this material. Technical guidance here is general information, not advice about your specific systems.

**Who this is for:** you have done [Lab 01](../02-why-the-cloud/06-lab-01-first-resource.md) and read [07.01 Your own network](01-your-own-network.md) and [07.02 Filtering traffic](02-filtering-traffic.md). **Time:** about 50 minutes, plus 5 minutes the next day.

**Goal:** you build the skeleton of the bakery's network by hand: a public subnet for the web tier and a private one for the order database, in two Availability Zones, with firewall rules that block a bad address range. Then you take it apart. **End state:** your lab log says why one subnet is public, and your account holds nothing from this lab.

![The lab's VPC: an internet gateway on its edge, a public subnet in us-east-1a whose route table sends 0.0.0.0/0 to the gateway, a private subnet in us-east-1b with only the local route, and two security groups.](../../images/07-05-lab-vpc.svg)

*Notice that both subnets sit in the same VPC with the same internet gateway attached. The only thing that makes one of them public is the highlighted route.*

**Long description.** The internet connects both ways to the internet gateway on the edge of the VPC (`10.0.0.0/16`). In AZ `us-east-1a`, the public subnet (`10.0.1.0/24`) has a route table with a local route and a highlighted route sending `0.0.0.0/0` to the gateway, and a network ACL that denies `203.0.113.0/24`, allows HTTPS in and allows replies out. In AZ `us-east-1b`, the private subnet (`10.0.4.0/24`) has only the local route and the default network ACL. Two security groups belong to the VPC: web (HTTPS from anywhere) and database (port 5432 from the web group only).

**What it creates:** one VPC, two subnets, an internet gateway, a route table, two security groups and a network ACL, in US East (N. Virginia), `us-east-1`, tagged `guide` = `clf` and `lab` = `09`. No servers. You delete it all at the end.

**What it costs:** $0. The VPC itself, internet gateways, security groups and network ACLs have no charge ([Amazon VPC FAQs](https://aws.amazon.com/vpc/faqs/); VPC User Guide, checked 2026-10-23). **Worst case on a Paid plan** if you forget to clean up: still $0. Two things *would* bill by the hour, and this lab never creates them: a **NAT gateway** at $0.045 an hour (about $33 a month) plus $0.045 per GB, and a **public IPv4 address**, including an Elastic IP, at $0.005 an hour (US East (N. Virginia), as of 2026-10-24; [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)). **Free plan:** nothing here upgrades your plan. Never choose **Upgrade plan** during a lab.

**Before you start, you need these guardrails in place:** [root MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/02-secure-the-root-user.md) (primer page 02), [an IAM admin user with MFA](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/03-your-everyday-admin-identity.md), which you use for this lab (page 03), [budgets and billing alerts](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/05-money-alarms.md) (page 05), and [the habits for every lab](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md), including your lab log (page 07).

**Why this matters:** AWS runs the physical network; the routes and rules inside your VPC are on your side of the shared responsibility line ([04.01](../04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md)). Splitting a workload into a public layer and a private layer is [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html); letting each layer accept only the traffic it needs is [SEC05-BP02 Control traffic flow within your network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html). Placing the subnets in two AZs prepares for [REL10-BP01 Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html).

> **New sign-up path:** Amazon VPC is supported there, but IAM users can't sign in to the console and your Region is fixed (as of 2026-10-23). Use your assigned Region and its AZs wherever this lab says `us-east-1`, and sign in the way that path gives you. We haven't run this lab on that path.

**About the screens:** labels in **bold** are what we saw when we ran this lab end to end in our test account on 2026-10-25. AWS changes its console often. If a label differs, look for the option with the same meaning.

## Steps

### Get ready

1. In your lab log, write today's date, `us-east-1`, the tags, and this table; you'll need every value again.

   | Thing | Name | Where or what |
   |---|---|---|
   | VPC | `clf-lab09-vpc` | `10.0.0.0/16` |
   | Public subnet | `clf-lab09-public-a` | `us-east-1a`, `10.0.1.0/24` |
   | Private subnet | `clf-lab09-private-b` | `us-east-1b`, `10.0.4.0/24` |
   | Internet gateway | `clf-lab09-igw` | attached to the VPC |
   | Route table | `clf-lab09-public-rt` | for the public subnet |
   | Security groups | `clf-lab09-web-sg`, `clf-lab09-db-sg` | web tier, database |
   | Network ACL | `clf-lab09-public-nacl` | for the public subnet |

   A **CIDR block** such as `10.0.0.0/16` is an address range: `/16` holds about 65,000 addresses, `/24` holds 256. Each subnet's range sits inside the VPC's.
2. Sign in to the console as your **IAM admin user**, not the root user.
3. Check that the Region selector shows N. Virginia.

### Part A: build the network

4. In the console search bar, type `VPC` and open **VPC**. In the left menu, choose **Your VPCs**.
   **You should see:** probably one VPC already: the default VPC AWS makes in every Region. Leave it alone.
5. Choose **Create VPC**. Under **Resources to create**, choose **VPC only**. Fill in:
   - **Name tag:** `clf-lab09-vpc`
   - **IPv4 CIDR block:** keep **IPv4 CIDR manual input** and type `10.0.0.0/16`
   - **IPv6 CIDR block:** none; **Tenancy:** **Default** (dedicated hardware costs more)
   - **VPC encryption control ($):** keep **None**. The other two modes are charged extras.
   - **Tags:** besides `Name`, which the page adds from the name tag, choose **Add tag** for `guide` = `clf` and `lab` = `09`.

   Choose **Create VPC**.
   **You should see:** your VPC's details page, with its state **Available**.
   > **If something went wrong:** a page with a preview diagram and NAT gateway options is **VPC and more**, which can add hourly NAT gateways. Switch to **VPC only**. If you created resources that way, delete any NAT gateway (left menu, **NAT gateways**) at once, then release any Elastic IP.
6. In the left menu, choose **Subnets**, then **Create subnet**. For **VPC ID**, choose `clf-lab09-vpc`. Fill in name `clf-lab09-public-a`, **Availability Zone** `us-east-1a`, **IPv4 subnet CIDR block** `10.0.1.0/24`, and the two tags. Choose **Create subnet**.
   > **If something went wrong:** an invalid range usually means a typo. A subnet in the wrong VPC can't be moved: delete it and create it again.
7. Repeat step 6 for `clf-lab09-private-b`, in `us-east-1b`, with `10.0.4.0/24`.
   **You should see:** both subnets in the list, each in its own AZ. A subnet always sits in exactly one AZ ([Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)).
8. In the left menu, choose **Internet gateways**, then **Create internet gateway**. Name it `clf-lab09-igw`, add the two tags, and create it.
   **You should see:** the state **Detached**.
9. Choose **Actions**, then **Attach to VPC**. In **Available VPCs**, pick the suggestion that shows your VPC's ID and `clf-lab09-vpc` (not one starting with **Use:**), and choose **Attach internet gateway**.
   **You should see:** the state **Attached**.

> **Your turn:** the gateway is attached. Predict: is either subnet public yet? Write yes or no, and why, in your lab log.
>
> <details><summary>Answer</summary>
>
> No. A subnet is public only when its route table has a route to the internet gateway ([Plan your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)), and neither has one yet.
>
> </details>

10. In the left menu, choose **Route tables**, then **Create route table**. Name it `clf-lab09-public-rt`, choose the VPC `clf-lab09-vpc`, add the two tags, and create it.
    **You should see:** one route, `10.0.0.0/16` to `local`. This **local route** lets everything in the VPC reach everything else in it.
11. On the route table's **Routes** tab, choose **Edit routes**, then **Add route**. Destination: `0.0.0.0/0`, meaning any address not matched by a more specific route. Target: **Internet Gateway**, then pick `clf-lab09-igw` from the box that appears. Choose **Save changes**.
12. On the **Subnet associations** tab, choose **Edit subnet associations**, tick `clf-lab09-public-a` only, and save.
    **You should see:** `clf-lab09-public-a` listed. The private subnet stays with the **main route table**, which AWS made with the VPC; it holds only the local route.
13. Choose **Your VPCs**, select `clf-lab09-vpc`, and open its **Resource map** tab, a picture of how the VPC's parts connect.
    **You should see:** the public subnet → `clf-lab09-public-rt` → the internet gateway, in a column called **Network Connections**; the private subnet → the main route table, shown only by its `rtb-` ID because it has no name, with no line to the gateway.

    ![The VPC's resource map in four columns: the VPC clf-lab09-vpc; two subnets, clf-lab09-public-a in us-east-1a and clf-lab09-private-b in us-east-1b; two route tables, clf-lab09-public-rt and an unnamed rtb- ID; and under Network Connections, clf-lab09-igw. Lines link the public subnet to clf-lab09-public-rt and on to the gateway, and the private subnet to the unnamed main route table.](../../images/07-05-resource-map.png)

    *Screenshot: the resource map, with only the public subnet's route table reaching the internet gateway, captured 2026-10-25 in our test account. AWS console screenshots are AWS material used as limited fair use and are not covered by this guide's license.*

### Part B: security groups

14. In the left menu, choose **Security groups**, then **Create security group**. Fill in:
    - **Name:** `clf-lab09-web-sg`; **Description:** `Lab 09 web tier - HTTPS from anywhere`
    - **VPC:** `clf-lab09-vpc` (the page may start on the default VPC)
    - **Inbound rules:** one rule, type **HTTPS** (port 443), source **Anywhere-IPv4** (`0.0.0.0/0`)
    - **Outbound rules:** leave AWS's rule allowing all outbound traffic
    - **Tags:** `guide` = `clf`, `lab` = `09`

    Create it. HTTPS from anywhere suits a public shop; never open SSH (port 22) or RDP (port 3389) to `0.0.0.0/0`.
    > **If something went wrong:** a group made in the default VPC can't be moved. Delete it and create it again.
15. **Your turn.** Create `clf-lab09-db-sg` for the order database. Suppose it runs PostgreSQL, on port 5432. It must accept port 5432 only from servers that carry `clf-lab09-web-sg`. Write the rule in your lab log, then create the group (same VPC, same tags).

    <details><summary>Model answer</summary>

    One inbound rule: type **PostgreSQL** (or **Custom TCP**, port `5432`), source the security group `clf-lab09-web-sg` (shown as `sg-` and an ID); outbound as AWS sets it. With a group as the source, the rule covers whichever servers carry that group, as they come and go ([security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)). The range `10.0.1.0/24` would let in anything in that subnet.

    </details>

### Part C: a network ACL that blocks a bad range

16. In the left menu, choose **Network ACLs**, then **Create network ACL**. Name it `clf-lab09-public-nacl`, choose the VPC `clf-lab09-vpc`, add the two tags with **Add tag**, and create it.
    **You should see:** inbound and outbound, a single rule numbered `*` that denies all traffic. A new network ACL blocks everything until you add rules; the VPC's default one allows everything.
17. Open the **Inbound rules** tab and choose **Edit inbound rules**. Add two rules, then save:

    | Rule number | Type | Source | Allow or deny |
    |---|---|---|---|
    | 90 | All traffic | `203.0.113.0/24` | Deny |
    | 100 | HTTPS (443) | `0.0.0.0/0` | Allow |

    `203.0.113.0/24`, a range reserved for examples, stands for the module brief's bad range. Rules run from the lowest number up and the first match decides ([network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)), so the bad range never reaches rule 100. A security group couldn't do this: it has no deny rules.
    **You should see:** 90 Deny, 100 Allow, `*` Deny, in that order.
18. **Your turn.** A network ACL is stateless: letting a request in doesn't let the reply out. A customer's browser sends from a temporary high-numbered port, an **ephemeral port**, and the reply goes back to it. Add the outbound rule that lets replies to customers leave, and nothing more.

    <details><summary>Model answer</summary>

    Outbound rule 100: **Custom TCP**, ports `1024-65535`, destination `0.0.0.0/0`, **Allow**; the client's operating system picks the reply port, and AWS suggests this range to cover every kind of client ([ephemeral ports](https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html#nacl-ephemeral-ports); lesson 07.02 explains). "Allow outbound 443" is tempting but wrong: replies go *to* the customer's ephemeral port, not to 443. A security group needs no such rule, because it remembers the request.

    </details>

19. On the **Subnet associations** tab, choose **Edit subnet associations**, tick `clf-lab09-public-a`, and save.
    **You should see:** the public subnet associated. A subnet has one network ACL at a time, so this replaces the default there; the private subnet keeps the default.

## Check your work

- [ ] The resource map shows `clf-lab09-public-a` → `clf-lab09-public-rt` → `clf-lab09-igw`, and `clf-lab09-private-b` → the main route table, with no route to the gateway.
- [ ] `clf-lab09-web-sg` allows HTTPS in from `0.0.0.0/0`; `clf-lab09-db-sg` allows 5432 in from `clf-lab09-web-sg` only.
- [ ] `clf-lab09-public-nacl` has inbound 90 Deny `203.0.113.0/24`, 100 Allow HTTPS, and an outbound rule for ports 1024–65535, and it is associated with the public subnet.
- [ ] Your lab log says what makes `clf-lab09-public-a` public.

## Clean up

Delete in this order: each step removes something the next depends on, and the VPC goes last.

20. In **Security groups**, delete `clf-lab09-db-sg`, then `clf-lab09-web-sg`.
    > **If something went wrong:** a window saying "Some security groups can't be deleted", with `clf-lab09-web-sg` marked **Will not be deleted** because "1 security group associated", means `clf-lab09-db-sg` still refers to it. Cancel, delete `clf-lab09-db-sg` first, then try again.
21. In **Subnets**, delete both `clf-lab09-` subnets. Their route table and network ACL associations go with them.
22. In **Route tables**, delete `clf-lab09-public-rt`. Don't try to delete the main route table; it goes with the VPC.
    > **If something went wrong:** a message that the route table has associations means a subnet is still associated, or the page hasn't caught up: right after deleting the subnets, we had to reload the page before the delete worked. Reload, then check step 21.
23. In **Network ACLs**, delete `clf-lab09-public-nacl`.
24. In **Internet gateways**, select `clf-lab09-igw`, choose **Actions**, then **Detach from VPC**; type `detach` and choose **Detach internet gateway**. Then choose **Actions**, **Delete**, type `delete`, and choose **Delete internet gateway**.
25. In **Your VPCs**, select `clf-lab09-vpc`, choose **Actions**, then **Delete VPC**, type `delete`, and confirm. Its main route table, default network ACL and default security group go with it. Never delete the default VPC.
26. **Confirm:** **Your VPCs** shows only the default VPC. In Tag Editor, search all Regions and all supported resource types for the tag `lab` = `09` ([Lab 01, steps 13 to 16](../02-why-the-cloud/06-lab-01-first-resource.md#find-it-by-its-tags)); expect no results (a deleted item can linger a few minutes). Tick everything off in your lab log.
27. **The next day:** check that your **Credits** balance hasn't fallen ([primer page 07](https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/07-habits-for-every-lab.md), habit 4). (task card: [Read this month's bill by service and Region](../98-how-to/08-read-this-months-bill.md))

## Recap

One route decided which subnet is public. A security group let the database hear only from the web tier. A network ACL blocked a range before any server could see it, and needed a rule for replies because it remembers nothing.

> **Reflect:** the owner says, "Give the database server a public IP address, so I can check orders from home." Would that put the database on the internet? Write two sentences.
>
> <details><summary>Model answer</summary>
>
> No: the private subnet has no route to the internet gateway, and AWS says a server there can't reach the internet even with a public IP address. A public address doesn't make a subnet public; the route table does. The owner needs an encrypted link from home (lesson [07.04](04-connecting-networks-and-offices.md)), not a public database.
>
> </details>

**Next:** [Simulation S8](06-sim-packet-journey.md): follow packets through a network like this one and find the rule that blocks them.

## Where to check the current details

- [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html), Amazon VPC User Guide (checked 2026-10-23)
- [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/) (NAT gateway and public IPv4 rates, checked 2026-10-24)

---

"Lab 09: Build a small network with a public and a private subnet, then take it apart" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional Permission for Internal Training from Automate the Cloud Inc.
License: https://creativecommons.org/licenses/by-nc/4.0/
Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt
