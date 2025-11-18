# Salesforce Implementation Discovery Questions
## Asked by Nick Millsner (Solutions Architect) — Nov 18 Call

**Purpose:** Reference guide for questions Nick asked to understand business model, org structure, and processes. Use to prep answers before follow-up Friday call.

---

## Business Model & Revenue Questions

### Q1: Walk me through your full revenue model in simple terms, starting with hardware sales

**Status:** ANSWERED
- Model A: One-time device purchase (government)
- Model B: Subscription model (commercial)
- Combination is possible

### Q2: Are there different warranty packages, or is it all the same?

**Status:** NEEDS CLARIFICATION
- Brandon: "Should be the same"
- Joey: "Better to build 2-3 packages just in case"
- Nick: "Once you build one, you can replicate it"
- **Decision:** Plan for 2-3 but build 1 initially

### Q3: Are there any revenue models related to services, architecture fees, or support?

**Status:** ANSWERED
- Yes, professional services as add-on to POC or full sale
- Examples: Engineering support hours, consultation, integration help
- Only bundled with hardware sale or POC, never standalone

### Q4: Which revenue streams do you anticipate will be highest volume in next 12 months?

**Status:** ANSWERED
- **Goal:** Subscription (recurring revenue)
- **Current:** Hardware-heavy

### Q5: Who are your core customer types?

**Status:** ANSWERED
- Government (direct buyers)
- Resellers/Partners (preferred channel)
- OEMs (integration partners, direct)

### Q6: What's the ideal future state buying motion?

**Status:** ANSWERED
- **Primary:** Through resellers
- **Edge cases:** Direct government, OEM integrations
- Avoid: Exclusive deals (except international territories)

### Q7: Can you explain the difference between a direct customer and a partner?

**Status:** ANSWERED
- **Direct:** Air Force, OEM like Dell/Toshiba (FE-facing relationship)
- **Partner:** Forage Japan example (FE supplies, partner sells to customers)

### Q8: For hardware, does every device automatically require a SaaS subscription?

**Status:** ANSWERED
- Minimum 2 devices as a "pair" (they talk to each other)
- Scaling: 100 devices = $100/device/month (not per instance, per device)
- Even if 1 management instance serves 100 devices, price = 100 × $100

### Q9: Can the subscription cost be spread across devices?

**Status:** ANSWERED
- Originally considered but creates pricing complexity
- **Decision:** Charge per device ($100/device/month) to simplify

### Q10: What about auto-renewal vs. renegotiation of subscription terms?

**Status:** ANSWERED
- **Option:** Customers can choose auto-renew or renegotiate annually
- **Hardware refresh:** 2-3 year cycle, incentivize renewal with device discount

### Q11: How are government vs. commercial rates determined?

**Status:** ANSWERED
- **Government baseline:** GSA schedule pricing (most-favored customer)
- **Reseller discount:** Justified because resellers do sales/marketing/deal closure (work GSA doesn't do)
- **Volume breaks:** Tiered discounts for higher volume (1K, 20K units)

### Q12: Will resellers initially get a discount rate, or do they need to reach a certain tier?

**Status:** ANSWERED
- **Initial:** Yes, Reseller Tier 1 discount immediately (if registered deal or standard routed deal)
- **Higher tiers:** Unlock at 1K units/year and 20K units/year volumes

### Q13: Do you think you'll need tiered pricing in the future for services or partners?

**Status:** ANSWERED
- **Yes**, both in terms of volume tiers (reseller levels) and potentially service tiers

### Q14: Partner deal registration—how does this work?

**Status:** ANSWERED
- **Brought deal** (partner brings opportunity): Higher discount (incentivizes prospecting)
- **Routed deal** (FE routes to partner): Standard Reseller Tier 1 discount
- Different discount = different value partner provides

---

## Org Structure & User Access Questions

### Q15: Who are the key users that will need Salesforce access?

**Status:** PARTIALLY ANSWERED
- **Confirmed:** Joey, Brandon, Mark, Corey, Yanni, Justin, George
- **TBD:** How many SDRs? Partner portal users? Read/edit/approve access per role?

### Q16: George (CFO/COO) needs visibility—what role should he have?

**Status:** ANSWERED WITH CAVEAT
- **Visibility:** Yes, need read-only reporting access
- **Admin:** NO—violates segregation of duties (SOX/HIPAA/ISO compliance issue)
- **Action:** Design security model offline with Andrea (CIO)

### Q17: Who should be configured to build automation, set up security, and manage access?

**Status:** ANSWERED
- **Admin:** Justin (System Admin)
- **Collaborators:** Joey, Brandon, Andrea (CIO) for governance/compliance design
- **Note:** Must follow segregation of duties (George can see everything but not change everything)

### Q18: How much will System Admin Justin need to be involved in day-to-day configuration?

**Status:** DEFERRED
- Depends on governance model to be developed offline

---

## Sales Process & Lead Management Questions

### Q19: Where are leads coming from today?

**Status:** ANSWERED
- Trade shows & conferences (manual capture)
- Website inbound forms (Joey processes)
- Partner-sourced deals
- Outbound SDR (starting Dec 4, aligning with Dec 10 go-live)

### Q20: Does lead qualification follow a standard checklist?

**Status:** NEEDS CREATION
- **Current:** Ad-hoc, discussion-based
- **Future:** Create formal checklist using Brandon's 6-stage framework

### Q21: At what point in the funnel does a lead become "qualified"?

**Status:** ANSWERED WITH NUANCE
- **Current state:** POC request = qualified (hardware ships)
- **Missing gate:** NDA execution (critical, but not clearly tracked)
- **Future state:** Qualifying stage (initial convo) + NDA = qualified, then moves to Discovery

### Q22: Is proof of concept really the qualification portion?

**Status:** ANSWERED
- **No**, POC is much further down the funnel
- **Reality:** Initial conversation + NDA + interest in devices = qualified lead (moves to Discovery)
- **POC:** Part of Scoping/Validation (not Qualifying)
- **Goal:** Close deal by end of POC (customer returns devices + signs contract)

### Q23: Do you need automated lead routing—territory-based or partner-based?

**Status:** ANSWERED
- **International:** Yes, exclusive territories (Forage Japan example)
- **US:** Not exclusive initially, cherry-picking approach
- **Automation:** Not needed immediately; manual routing fine for current volume

### Q24: Will you need multicurrency and multilingual support?

**Status:** ANSWERED
- **Yes**, needed for international expansion

---

## Approval & Automation Questions

### Q25: Walk me through the different approval processes in your business

**Status:** ANSWERED
- **Reseller authorization:** CEO/COO approval (highly selective)
- **Quote/discount approvals:** George (CFO/COO) approves all quotes
- **NDA execution:** Legal review + George signature (currently email, future: DocuSign)

### Q26: Is there an approval process needed for quote discounts?

**Status:** ANSWERED
- **Year 1:** Yes, George approves all quotes/discounts
- **Future:** Potentially less rigid, but TBD

### Q27: Do you currently have an NDA process in Salesforce?

**Status:** ANSWERED
- **No**, currently manual email back-and-forth
- **Pain point:** Cumbersome, multiple emails in and out
- **Future roadmap:** DocuSign integration (Phase 2, 2025)

---

## Sales Stage & Process Questions

### Q28: Tell me about your 6-stage sales process

**Status:** ANSWERED (Brandon framework provided)
1. **Qualifying:** Initial outreach, partner/SDR involvement
2. **Discovery:** NDA, needs discovery, sales engineer introduced
3. **Scoping:** Consultation, POC document, decision-maker engagement
4. **Validation:** POC execution, device shipment, demo
5. **Contracts:** Quote generation, pricing, legal review
6. **Closed:** Won/Lost

### Q29: Can you clarify who owns each stage?

**Status:** ANSWERED
- **Qualifying:** Mark + Brandon + SDRs
- **Discovery:** Mark/Brandon + Corey (Sales Engineer introduces)
- **Scoping:** Joey leads (POC doc, decision-maker engagement)
- **Validation:** Joey + Corey (POC execution, devices)
- **Contracts:** Brandon (quotes) + George (approval) + Legal (contract)
- **Closed:** Joey (post-sale, procurement, onboarding)

### Q30: Can you add revenue forecasting to stage understanding?

**Status:** ANSWERED
- **Yes**, during Discovery/Scoping you forecast revenue ("If we win this deal, we get $X")

### Q31: Should you have fewer stages (5-6 vs. 8)?

**Status:** ANSWERED
- **Recommendation:** 5-6 stages are sufficient for 6-8 month sales cycle
- **Benefit:** Simpler, less bureaucracy, but still trackable progression
- **Note:** Set SLA expectations per stage (reps should move deals through each stage ~4 weeks)

---

## Salesforce Technical & Configuration Questions

### Q32: Stage transitions—should reps manually move them or auto-trigger based on field completion?

**Status:** ANSWERED ONLINE (see earlier research)
- **Manual (default):** Rep clicks to advance stage
- **Automated:** Use Flows (record-triggered, before-save or after-save)
- **Hybrid (recommended):** Validation rules prevent advancement without required fields + manual stage click
- **Best practice:** Avoid mixing manual + automated on same opportunity

### Q33: How do you automate stage transitions?

**Status:** ANSWERED ONLINE (see earlier research)
- **Tool:** Record-Triggered Flows (Salesforce's primary automation engine)
- **Types:** Before-save (field updates), After-save (related actions, DocuSign, etc.)
- **Note:** Flows are replacing legacy Workflow/Process Builder (which are retiring)

### Q34: What Salesforce security/sharing training do we need?

**Status:** ANSWERED
- **For Justin:** Salesforce Trailhead security/sharing module (gameified badges)
- **Caveat:** Trailhead best practices may differ from real-world requirements—expect supplemental resources

### Q35: Is DocuSign integration in scope for Phase 1?

**Status:** ANSWERED
- **No**, out of scope for Phase 1
- **Roadmap:** Phase 2 (2025) candidate
- **Note:** Salesforce + DocuSign integration is well-established and doable

### Q36: Is Revenue Cloud a better option than Sales Cloud?

**Status:** ANSWERED
- **No**, Sales Cloud Enterprise is correct choice
- **Revenue Cloud:** Overkill for current state; deferred to future roadmap
- **Philosophy:** Start with Sales Cloud, add Revenue Cloud features later if needed

### Q37: Do you need Experience Cloud (partner portal) immediately?

**Status:** ANSWERED
- **No**, Phase 2 (2025) implementation
- **Purpose:** Let resellers self-serve quoting
- **Licensing:** Per-login basis, estimate cost upfront

---

## Compliance & Security Questions

### Q38: Can Salesforce be federated to Azure?

**Status:** ANSWERED
- **Yes**, Salesforce integrates with Azure for identity/access management
- **Setup:** Permission sets + roles + profiles in Salesforce, connected to Azure
- **Benefit:** Centralized access control across systems

### Q39: What are the compliance/governance concerns?

**Status:** ANSWERED
- **Segregation of duties:** George (CFO/COO) cannot have admin rights
- **Standards:** SOX, HIPAA, ISO compliance required
- **Solution:** Design access model where George can VIEW everything but not EDIT/APPROVE everything
- **Next step:** Offline meeting (Joey, Brandon, Andrea, Justin, Nick) to design model

### Q40: Who should own data migration?

**Status:** DEFERRED
- Consultant will help develop data migration strategy
- SharePoint being set up for data files (XLS, CSVs, etc.)

---

## Follow-Up Questions (To Be Answered by Friday)

### From Nick's Perspective

- [ ] Define 6-stage sales process in detail (actions, tools, pain points per stage)
- [ ] Build security/access control model (who sees what, who can change what)
- [ ] Create persona definitions (responsibilities, goals, KPIs per user)
- [ ] Define lead qualification checklist
- [ ] Clarify warranty package options (identical or distinct?)
- [ ] Confirm hardware refresh cadence (2 years? 3 years?)
- [ ] Detail professional services pricing structure
- [ ] Define flexibility of pricing within tiers (fixed vs. negotiable?)

### From FE's Perspective

- [ ] How many SDRs will use Salesforce?
- [ ] Will partners have immediate portal access (no, Phase 2)
- [ ] What read/edit/approve access does each role need?
- [ ] Should stage transitions be manual or automated?
- [ ] What happens if customers skip stages or move too fast?
- [ ] How do you forecast deals (when in pipeline)?

---

## Key Questions NOT Fully Answered

- **Pricing flexibility:** Can George negotiate pricing within tiers, or is it fixed?
- **Professional services:** What's the exact $/hour rate or bundled hour approach?
- **International pricing:** Same GSA baseline + reseller discounts, or separate model?
- **Warranty tiers:** Are they truly distinct, or replicates of one master?
- **Lead routing automation:** When do you implement this? (Deferred to Phase 2?)

---

## Next Steps

**Friday, Nov 22 @ 3PM ET:** Discuss answers to deferred questions, finalize sales process framework, begin Lucidchart diagram build
