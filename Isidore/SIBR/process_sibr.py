import re

def parse_markdown_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    headers = []
    data = []
    start_parsing = False
    
    for line in lines:
        line = line.strip()
        # Remove the line number prefix if present (e.g., "1: ")
        line = re.sub(r'^\d+:\s*', '', line)
        
        if not line.startswith('|'):
            continue
        
        # Split by pipe and strip whitespace
        cells = [c.strip() for c in line.split('|')]
        # Remove empty first and last elements caused by leading/trailing pipes
        if len(cells) > 0 and cells[0] == '': cells.pop(0)
        if len(cells) > 0 and cells[-1] == '': cells.pop(-1)
        
        if '---' in cells[0]:
            continue
            
        if not start_parsing:
            headers = cells
            start_parsing = True
        else:
            row = {}
            for i, cell in enumerate(cells):
                if i < len(headers):
                    row[headers[i]] = cell
            data.append(row)
    return data

def clean_topic_id(raw_topic):
    # Remove status like (Pre-Release), (Open)
    # Example: A254-049(Pre-Release) -> A254-049
    return re.sub(r'\([^\)]+\)$', '', raw_topic).strip()

def find_in_crm(topic_id, crm_data):
    # CRM Topic column example: "(Eric) A254-P030 xTechOverwatch Open Topic"
    # We look for the topic_id in the CRM topic string.
    # We want to ensure it's a distinct word/token to avoid partial matches (e.g. A254-01 matching A254-010)
    # But the format varies. Let's try simple substring first, but maybe check boundaries.
    
    matches = []
    for row in crm_data:
        crm_topic = row.get('Topic', '')
        if topic_id in crm_topic:
            matches.append(row)
    
    # Filter matches to be more robust if needed
    # For now, return the first match if any
    if matches:
        return matches[0]
    return None

def main():
    published_path = 'currently_published_list.md'
    crm_path = 'listed_in_crm.md'
    
    published_data = parse_markdown_table(published_path)
    crm_data = parse_markdown_table(crm_path)
    
    update_list = []
    missing_list = []
    
    print(f"Loaded {len(published_data)} published topics.")
    print(f"Loaded {len(crm_data)} CRM topics.")
    
    matched_count = 0
    for item in published_data:
        raw_topic = item.get('Topic # (Status)', '')
        topic_id = clean_topic_id(raw_topic)
        title = item.get('Title', '')
        close_date = item.get('Close', '')
        
        crm_match = find_in_crm(topic_id, crm_data)
        
        if crm_match:
            matched_count += 1
            crm_deadline = crm_match.get('Deadline', '')
            crm_topic_name = crm_match.get('Topic', '')
            
            if crm_deadline != close_date:
                update_list.append({
                    'topic_id': topic_id,
                    'crm_topic': crm_topic_name,
                    'current_crm_deadline': crm_deadline,
                    'new_deadline': close_date
                })
        else:
            missing_list.append({
                'topic_id': topic_id,
                'title': title,
                'close_date': close_date
            })
            
    print(f"\nAnalysis Results:")
    print(f"Total Published Topics: {len(published_data)}")
    print(f"Total CRM Entries: {len(crm_data)}")
    print(f"Overlap (Published topics found in CRM): {matched_count}")
    print(f"Missing (Published topics NOT found in CRM): {len(missing_list)}")
    
    print("\n--- UPDATE DUE DATES (Send to Dr. Harvey and Melina) ---")
    if update_list:
        for item in update_list:
            print(f"Topic: {item['topic_id']}")
            print(f"  CRM Name: {item['crm_topic']}")
            print(f"  Current CRM Deadline: {item['current_crm_deadline']}")
            print(f"  New Deadline: {item['new_deadline']}")
            print("-" * 20)
    else:
        print("No updates needed.")
        
    print("\n--- MISSING FROM CRM (Review list) ---")
    if missing_list:
        for item in missing_list:
            print(f"Topic: {item['topic_id']}")
            print(f"  Title: {item['title']}")
            print(f"  Due Date: {item['close_date']}")
            print("-" * 20)
    else:
        print("No missing items found.")

if __name__ == "__main__":
    main()
