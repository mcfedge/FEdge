# Start simple, avoid overbuilding SFDC

**What's new:** Nina (Head of Ops & Tech) and Connor shared Salesforce best practices to help Forward Edge structure our CRM implementation correctly from day one.

**Why it matters:** Building Salesforce wrong slows down projects significantly—the right approach now saves us time, effort, and prevents the expensive rework cycle we experienced with Dynamics.

---

## The Core Principle

**Start basic. Scale later.** Don't try to build everything perfectly from the beginning. Add complexity only after you understand what you actually need.

---

## Must-Do Recommendations

### 1. Define Attribution Models Early
**The problem:** Most companies struggle with this, especially when sales + marketing + referrals all touch the same prospects.

- Track lead sources systematically (Memory Blue, outbound, channel partners, referrals)
- Tag **every** lead/opportunity with its source so you can measure what's working
- Decide your approach: **first-touch, last-touch, or blend model**
- Your consultant can help guide this once your data flows are clear

### 2. Decide When to Create Opportunities
**Current issue:** Creating opportunities immediately on meeting booking creates "junk" in the pipeline.

- **Option A:** Pre-qualification stage (sales meeting object) → filtered conversion to opportunity
- **Option B:** Create opportunities immediately (if SDR/AE already qualified the meeting)
- **Our approach:** Use a "Sales Meeting" intermediate step; only convert qualified meetings to opportunities
- **Why it matters:** Prevents deal velocity skewing and keeps reporting accurate

### 3. Set Up Validation Rules Between Stages
**The trap:** Reps skip stages or move deals too fast; you lose visibility into what's really happening.

- **Enforce sequential stage progression:** No jumping from Created → Contracts
- **Add validation gates:** Must answer budget/decision-maker/timeline questions before advancing
- **Balance carefully:** Over-validation causes reps to copy-paste answers (bad behavior). Keep it simple enough that they want to use it properly
- **Provide rep guides:** Make clear what's required at each stage so they understand the "why"

### 4. Implement Scoring Mechanisms
**Use two tracking methods:**

- **Lead scoring rubric:** Internal team rates quality of leads (1-5 scale)
- **Closed-lost tracking:** Categorize why deals didn't move forward (budget, no champion, not a fit, etc.)
- **Why:** Allows you to spot patterns ("We lost 20% of deals last quarter due to X") and coach teams on gaps

### 5. Use Contact Roles (Not Just Lookups)
**Better relationship tracking:**

- Assign contact roles: Decision Maker, Technical Evaluator, Budget Owner, etc.
- **Why it matters:** When your tech buyer moves companies, that contact history follows them—critical for recurring business and relationship mapping

### 6. Turn On History Tracking Immediately
**And build custom field tracking:**

- Enable Salesforce history tracking for all key fields and objects
- **Add custom fields:** Date stamp for each opportunity stage + days-in-stage counter
- **Why:** History reports are clunky for dashboards; custom fields let you surface "deals stuck in Discovery for 47 days" insights to reps for coaching

---

## Configuration Specifics

**Opportunity stages:** Use Salesforce's out-of-the-box 5-6 stages rather than 8+
- 5-6 stages are simpler and sufficient for a 6-8 month sales cycle
- More stages = more granular tracking but also more bureaucracy
- Set SLA expectations: Reps should move deals through each stage in ~4 weeks

**External tools:**
- Salesforce Trailhead Academy has thousands of resources (can feel overwhelming—use selectively)
- Your implementation team should guide you through getting Started mode before expanding

---

## What's Next

**Immediate:**
- [ ] Finalize your **attribution model** (first-touch, last-touch, or blend)
- [ ] Design your **opportunity creation workflow** (immediate vs. pre-qualified)
- [ ] Define **validation rules** for each stage with rep resources/guides
- [ ] Implement **lead scoring rubric** (use Nina's internal example as reference)

**Before full rollout:**
- [ ] Enable history tracking on key fields
- [ ] Build custom stage timestamp fields for deal velocity tracking
- [ ] Test validation rules with pilot group (avoid over-validation)
- [ ] Confirm permission sets and role-based access controls (Azure integration)

---

## The Bottom Line

The difference between a smooth Salesforce implementation and a painful one is **deciding how you'll work BEFORE you build the system.** Start simple, measure what matters, add complexity only when justified. Avoid the Dynamics trap: learn the tool, *then* layer in custom requirements—not both at once. 


Chat with meeting transcript: https://notes.granola.ai/d/6c76bae3-baf2-4e3e-afb8-3b8960208b6e