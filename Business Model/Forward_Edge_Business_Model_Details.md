# Forward Edge-AI Business Model & Revenue Intricacy

**Summary:** Hardware + subscription SaaS + professional services with multiple customer types, pricing tiers, and deal structures

---
Brandon just sent me this message on the side “for buyers, it allows them to pay via Operations Expense vs Capital Expense. For us, the desire from leadership is to have the recurring revenue. 1600 per device + ~$70/mo  vs say $400/mo/device. “

why is this better?  help me make sense of it

**For buyers (customers):**

- **OpEx vs CapEx** - Monthly payments come from operating budget (easier to approve) vs capital budget (requires big upfront approvals)
- **Cash flow** - Spread $1600 device cost over time instead of paying upfront
- **Predictable costs** - Know exactly what you’ll pay each month

**For ForwardEdge.ai:**

- **Recurring revenue** - Much more valuable for company valuation and growth
- **Predictable income** - $400/month is steadier than hoping for new hardware sales
- **Customer retention** - Harder for customers to leave when they don’t own the devices
- **Higher lifetime value** - $400/month over 2 years = $9,600 vs $1600 + ($70 × 24 months) = $3,280

The subscription model potentially triples the revenue per customer while making it easier for customers to say yes.

---

## Primary Revenue Streams

### 1. Hardware Sales (Devices)

**Two purchasing models:**

**Model A: One-time device purchase (primarily government)**
- Customer pays upfront for devices
- Licensing included with purchase
- Warranty & support available (optional add-on)
- Example: "I'll pay you once for 100 devices, handle everything myself"

**Model B: Subscription model (primarily commercial)**
- Customer leases devices over contract term
- Monthly OpEx vs. CapEx approach
- Recurring revenue model
- Example: "I'll pay you $X/month for 100 devices for 2 years"

### 2. Subscription Management Software (Cassium)

**Bundled with hardware, NOT sold separately**

**Pricing structure:** $100/device/month
- Covers device + management software (Cassium) + support
- Minimum 2 devices as a "pair" (they communicate with each other)
- Scaling: 100 devices = $100/month × 100 = $10,000/month (not per instance of software, per physical device)

**Important nuance:** If customer has 100 devices but only one management instance, they still pay per device, not per instance. This simplifies pricing and prevents customers from trying to reduce costs by "pooling" instances.

**Billing structure:**
- Priced monthly but billed annually (or quarterly, TBD)
- Monthly pricing provides flexibility if customer reduces units mid-year (prorate)

### 3. Professional Services (Consulting/Implementation)

**Ancillary revenue, bundled with POC or full sales**

**Examples:**
- Engineering support hours (e.g., 4 hours included with POC, additional hours billable)
- Consultation on network integration
- Implementation support (setting up systems, training)
- Only sold as part of:
  - Proof of concept (optional add-on)
  - Full sales/implementation (optional add-on)

### 4. Warranty & Support Packages

**Status:** Planning to offer multiple tiers (potentially 2-3 versions)
- Currently unclear if these will be identical or truly differentiated
- Decision deferred—build one version, replicate it if needed

---

## Customer Types & Buying Motions

### Government (Direct Selling)

**Characteristics:**
- Buy direct, no middleman
- Often one-time purchase model
- May be large volume (e.g., "Air Force needs 1,000 units")
- Examples: USAF, Navy, Army, DoD

**Buying motion:**
- Forward Edge salesman handles entire deal
- Or: If FE has a reseller partner aligned with government agency, route through partner
- Pricing: GSA schedule baseline

### Resellers/Partners (PREFERRED channel—"tip of the funnel")

**Characteristics:**
- Partners buy inventory at volume discount
- Partners mark up and resell to their customers
- FE provides inventory, technical support, but partners do customer relationship management
- Examples: Forage Japan (joint venture), other regional/vertical resellers

**Buying motion:**
- Partner identified as "registered deal" (they bring the opportunity to FE)
  - Discount = Reseller Tier 1 + incentive for bringing deal
  - Potential for increased discounts at higher volume tiers
- OR: FE routes opportunity to partner
  - Discount = Reseller Tier 1 only (no "brought deal" incentive)

**Pricing structure:**
- Registered new logo: Partner gets higher discount
- New deal (routed by FE): Partner gets standard Reseller Tier 1 discount
- Volume tiers: Increased discounts at 1K units/year, 20K units/year, etc.
- **Not exclusive** by default (FE works with multiple partners in same geography)
  - Exception: International territories (e.g., Japan = exclusive to Forage Japan)

**Why FE prefers resellers:**
- FE doesn't want to be the customer-facing salesman for every deal
- Resellers handle their own customers, their own marketing, their own prospecting
- FE supplies inventory + tech support, resellers handle commercial relationship

### OEMs (Integration Partners / Direct selling)

**Characteristics:**
- OEM integrates FE devices into larger solution
- OEM sells the combined solution to their customers
- FE is a supplier to OEM, not customer-facing
- Examples: Dell, Toshiba, Cubic (hypothetical)

**Buying motion:**
- High-volume, direct relationship with OEM
- OEM pays FE directly for devices
- OEM integrates into their product, resells to their customers
- Volume breaks apply (e.g., 1K units = 10% discount, 20K units = 15-18% discount)

**Why direct:** OEM integration means high volume and ongoing relationship; can't be channel-ed through resellers

### Edge Cases

**FE as supplier to reseller fulfilling government contracts:**
- Reseller has relationship with government agency
- Reseller orders from FE
- FE supplies reseller, reseller delivers to government
- FE never touches government customer directly
- Treated as reseller purchase, not direct government sale

---

## Pricing Architecture

### Baseline: GSA Schedule (Government pricing)

**Requirement:** GSA pricing is "most favored customer" pricing
- Means: Under same/similar conditions, GSA must get best available price
- Implication: If reseller buys at lower price, they must provide something GSA doesn't (sales, marketing, deal closure)
- This justifies reseller discounts vs. GSA baseline

### Pricing Tiers

**Tier 1: GSA Schedule (government/most-favored baseline)**
- Example: $100/device/month (illustration only)

**Tier 2: Reseller Tier 1 (standard reseller discount)**
- Example: $85/device/month (15% discount)
- Reason: Resellers do sales, marketing, customer relationship mgmt (work GSA doesn't do)

**Tier 3: Reseller Tier 2 (volume-based upgrade)**
- Triggers at ~1K devices/year volume
- Example: $80/device/month (20% discount)

**Tier 4: Reseller Tier 3 (high-volume tier)**
- Triggers at ~20K devices/year volume
- Example: $75/device/month (25% discount)

**Tier 5: OEM/Direct (negotiated)**
- Highest volume = negotiated pricing
- Could range from 10-25% discount depending on volume and commitment

### Deal Registration Discount

**"Brought deal" (partner brings opportunity to FE):**
- Partner gets higher discount (incentivizes prospecting)
- Example: Reseller Tier 1 + 5% "brought deal" bonus

**"Routed deal" (FE routes to reseller):**
- Partner gets standard Reseller Tier 1 discount
- No bonus because FE did the prospecting

---

## Contract & Renewal Terms

### Subscription Contracts

**Auto-renewal:** Optional, customer can choose
- Some customers want "set it and forget it" (auto-renew)
- Others prefer annual renegotiation

### Hardware Refresh Cycle

**Incentive-based renewal:**
- Contract terms: 2-3 years (TBD, likely 2-3 year refresh cycle)
- At renewal: Customer can get latest hardware at discount if they re-sign subscription
- Example: "Your 2-year contract is up. Renew for another 2 years, get new devices at 50% off"
- Similar to cell phone contracts (upgrade incentive)

**Goal:** Encourage subscription continuation + stay current on latest hardware

---

## Special Pricing Considerations

### Government vs. Commercial Rates

**Question:** Are there truly different price points?

**Answer:** GSA schedule IS the government rate (baseline). Commercial resellers get lower prices because they provide services GSA doesn't.

**Risk:** Competitors could offer resellers lower prices. FE has flexibility on reseller pricing but must maintain GSA as baseline.

### Volume Break Thresholds

**Current thinking:**
- 1K units/year = first volume break
- 20K units/year = second volume break
- Applies to both resellers and OEMs

**Caveat:** COGS roughly the same whether customer buys 50 or 2,000 devices. Volume breaks are about competitive positioning and incentivizing larger deals, not reducing costs.

---

## Minimum Order Requirements

**Device pairs:** Minimum 2 devices (they need to communicate with each other)
- Can order any number > 2 (3, 5, 100, etc.)
- Pricing applies per device regardless of quantity

**Subscription:** Minimum matches hardware (if 100 devices, minimum 100 subscriptions × $100/mo)

---

## Professional Services Pricing

**Not defined in detail yet** (deferred)

**Expected structure:**
- Engineering support hours (bundled with POC, add-on thereafter)
- Consultation for network integration (add-on)
- Implementation & training (add-on)

**Scope:** Only offered bundled with hardware sale or POC, never standalone

---

## Revenue Forecasting & Mix

**Q: Which revenue stream will be highest volume in next 12 months?**

**Answer:** Subscription (recurring revenue) is the goal
- Rationale: Reduces customer CapEx burden, creates predictable recurring revenue for FE

**Current state:** Hardware-heavy (up-front sales focus)

**Future state:** Subscription-heavy (long-term contracts, higher lifetime value)

---

## Go-to-Market Implications for Salesforce

**For Quotes module:**
- Need to handle multiple pricing tiers (GSA, Reseller T1-T3, OEM)
- Need to handle "brought deal" discount logic
- Need ability for partners to request discount tiers based on annual volume

**For Contracts module:**
- Hardware refresh incentives must be noted
- Renewal dates must trigger proactive outreach

**For Reporting:**
- Track revenue by customer type (Government, Reseller, OEM)
- Track revenue by pricing tier
- Track subscription renewal rate and hardware refresh participation

**For Partner Portal (future):**
- Resellers need visibility to their pricing tier
- Resellers need to see available volume breaks
- Resellers need ability to register new deals

---

## Key Business Model Decisions Made

✓ Device + Subscription is a "pair"—simplifies pricing, prevents gaming

✓ Resellers are preferred channel—FE doesn't want to be customer-facing sales force

✓ GSA baseline protects government pricing—reseller discounts justified by work resellers do

✓ Volume breaks incentivize larger deals—competitive positioning

✓ Hardware refresh on renewal—keeps customers current, encourages re-signing

✓ Professional services optional add-on—high-margin, differentiator vs. competitors

✓ Deal registration bonus—incentivizes partner prospecting vs. FE routing

---

## Outstanding Questions for Refinement

- [ ] Are warranty package options truly distinct, or identical?
- [ ] What's the exact hardware refresh cadence? (2 years? 3 years?)
- [ ] At what customer size do volume breaks trigger? (1K units confirmed, but others?)
- [ ] What's the professional services pricing structure? ($/hour, $/project, bundled hours?)
- [ ] How flexible is pricing within tiers? (Fixed vs. negotiable?)
- [ ] International pricing: GSA scale + reseller discounts, or separate model?
