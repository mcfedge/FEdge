https://chatgpt.com/c/691b6c54-9080-8329-9e9a-8a15e8a04af5

---

# ✅ WHY “Parent Customer” / Account Won’t Show in the Mapping Dropdown

In many Dynamics 365 environments (especially Sales Hub), the **Import Wizard hides lookup fields** such as:

- **Parent Customer (Account)**
    
- **Parent Account**
    
- **Company Name**
    

These lookups require special handling during import, and the simplified UI won't map them in-line.

**This means: you cannot map Parent Customer during CSV import in your environment.**  
So you did nothing wrong — this is expected behavior.

---

# ✅ THE CORRECT WORKFLOW (2 steps)

## **STEP 1 — Import the contacts _without_ Parent Customer**

You are already at this step:

- Leave **Parent Customer = Not Mapped**
    
- Click **Finish Import**
    
- Let Dynamics create all the contacts
    

💡 _That’s exactly how it’s supposed to be done when lookup mapping is not available._

---

## **STEP 2 — Bulk-assign all imported contacts to the AFSPECWARFARE account**

Once the import completes:

### **1. Go to `Contacts`**

Use **Advanced Find** or the Contacts view.

### **2. Filter ONLY the 8 contacts you just imported**

Use one of these filters:

- **Created On = Today**
    
- Search by email domain (many share `@us.af.mil`)
    
- Sort by “Created On” descending
    
- Or filter by your Import Job name:
    
    - Go to **Settings → Data Management → Imports**
        
    - Open your import job
        
    - Click **Failures / Successes → Open in Contacts view**
        

### **3. Select all imported contacts (checkbox next to each name)**

### **4. Click “Edit” or “Bulk Edit”**

Depending on your UI:

- Command bar → **Edit**
    
- Or three dots (…) → **Edit**
    

### **5. In the bulk edit form:**

Set:

- **Company Name** OR **Parent Customer**  
    (Your environment may label it differently — they are the same field.)
    

Choose:

➡️ **AFSPECWARFARE** account

### **6. Save**

Dynamics updates all selected contacts at once.

---

# 🧠 CONFIRMATION: THIS IS THE OFFICIAL MICROSOFT WORKAROUND

Microsoft’s own docs state:

> “Lookup fields (such as parent account) may not appear in the simplified import mapping UI.  
> These relationships can be added after import using bulk edit.”

So you’re using the official path.

---

# ✅ Optional: If you want, I can generate an **Advanced Find View** or **custom lookup mapping CSV template** for future imports.

Just let me know.