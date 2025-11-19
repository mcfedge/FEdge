import pandas as pd
from datetime import datetime

# Load the Excel files
currently_published = pd.read_excel(r'c:\Users\Mark Cetola\Downloads\FEdge\Isidore\SIBR\currently published list.xlsx')
crm_list = pd.read_excel(r'c:\Users\Mark Cetola\Downloads\FEdge\Isidore\SIBR\listed in the CRM.xlsx')

# Clean up column names
currently_published.columns = currently_published.columns.str.strip()
crm_list.columns = crm_list.columns.str.strip()

# Extract topic numbers from both lists
# From currently published list - Topic # is in format like "A254-049(Pre-Release)"
currently_published['Topic_Clean'] = currently_published['Topic # (Status)'].str.extract(r'([A-Z0-9]+-[A-Z0-9]+)', expand=False)

# From CRM list - Topic is the full name, extract the topic number
crm_list['Topic_Clean'] = crm_list['Topic'].str.extract(r'([A-Z0-9]+-[A-Z0-9]+)', expand=False)

# Find opportunities in SITIS but not in CRM
in_sitis_not_in_crm = currently_published[~currently_published['Topic_Clean'].isin(crm_list['Topic_Clean'])]

# Find opportunities in both lists (for due date comparison)
in_both = currently_published[currently_published['Topic_Clean'].isin(crm_list['Topic_Clean'])]

# Create output reports
print("=" * 100)
print("OPPORTUNITIES IN SITIS BUT NOT IN CRM")
print("=" * 100)
print()

if len(in_sitis_not_in_crm) > 0:
    for idx, row in in_sitis_not_in_crm.iterrows():
        print(f"Topic: {row['Topic # (Status)']}")
        print(f"Title: {row['Title']}")
        print(f"Component: {row['Component Instructions']}")
        print(f"Open Date: {row['Open']}")
        print(f"Close Date: {row['Close']}")
        print(f"Release #: {row['Release #']}")
        print("-" * 100)
        print()
else:
    print("All opportunities in SITIS are already in CRM")
    print()

print("=" * 100)
print("OPPORTUNITIES NEEDING DUE DATE UPDATES IN CRM")
print("=" * 100)
print()

updates_needed = []
for idx, row in in_both.iterrows():
    topic_clean = row['Topic_Clean']
    sitis_close_date = pd.to_datetime(row['Close'])

    # Find matching CRM entry
    crm_match = crm_list[crm_list['Topic_Clean'] == topic_clean]

    if not crm_match.empty:
        crm_deadline = pd.to_datetime(crm_match.iloc[0]['Deadline'], errors='coerce')

        # Check if dates differ
        if pd.notna(crm_deadline) and pd.notna(sitis_close_date):
            if crm_deadline.date() != sitis_close_date.date():
                updates_needed.append({
                    'Topic': topic_clean,
                    'CRM_Title': crm_match.iloc[0]['Topic'],
                    'SITIS_Close_Date': sitis_close_date.strftime('%Y-%m-%d'),
                    'CRM_Current_Date': crm_deadline.strftime('%Y-%m-%d'),
                    'Days_Difference': (sitis_close_date - crm_deadline).days
                })
        elif pd.isna(crm_deadline) and pd.notna(sitis_close_date):
            updates_needed.append({
                'Topic': topic_clean,
                'CRM_Title': crm_match.iloc[0]['Topic'],
                'SITIS_Close_Date': sitis_close_date.strftime('%Y-%m-%d'),
                'CRM_Current_Date': 'No deadline set',
                'Days_Difference': 'N/A'
            })

if updates_needed:
    for update in updates_needed:
        print(f"Topic: {update['Topic']}")
        print(f"CRM Title: {update['CRM_Title']}")
        print(f"SITIS Close Date: {update['SITIS_Close_Date']}")
        print(f"CRM Current Deadline: {update['CRM_Current_Date']}")
        print(f"Difference: {update['Days_Difference']} days")
        print("-" * 100)
        print()
else:
    print("All deadlines in CRM match SITIS")
    print()

print("=" * 100)
print("SUMMARY")
print("=" * 100)
print(f"Total opportunities in SITIS: {len(currently_published)}")
print(f"Total opportunities in CRM: {len(crm_list)}")
print(f"Opportunities in SITIS but not in CRM: {len(in_sitis_not_in_crm)}")
print(f"Opportunities needing due date updates: {len(updates_needed)}")

# Save detailed reports to files
in_sitis_not_in_crm[['Topic # (Status)', 'Title', 'Component Instructions', 'Open', 'Close', 'Release #']].to_csv(
    r'c:\Users\Mark Cetola\Downloads\FEdge\Isidore\SIBR\not_in_crm.csv', index=False
)

if updates_needed:
    pd.DataFrame(updates_needed).to_csv(
        r'c:\Users\Mark Cetola\Downloads\FEdge\Isidore\SIBR\due_date_updates_needed.csv', index=False
    )

print()
print("Reports saved:")
print("- not_in_crm.csv")
if updates_needed:
    print("- due_date_updates_needed.csv")
