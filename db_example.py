import sqlite3

# 1. Connect to or Create the Database File
# If the file doesn't exist, it is created.
conn = sqlite3.connect('project_data.db')
c = conn.cursor()

# 2. Create a Table (Only runs if the table doesn't already exist)
try:
    c.execute('''
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            files_moved INTEGER,
            is_active BOOLEAN
        )
    ''')
    print("Table 'projects' created.")
except sqlite3.OperationalError:
    # This runs if the table already exists, preventing a crash.
    pass

# 3. Insert Data (The 'Desktop Cleaner' project)
c.execute('''
    INSERT INTO projects (name, files_moved, is_active) 
    VALUES (?, ?, ?)
''', ('Desktop Cleaner', 6, True)) # The '?' prevent SQL injection

# 4. Save (Commit) the changes
conn.commit()

# --- NEW QUERY 1: Find projects where files_moved > 5 ---
c.execute("SELECT name, files_moved FROM projects WHERE files_moved > ?", (5,))
high_impact_projects = c.fetchall()

print("\n--- Projects that moved > 5 files ---")
for row in high_impact_projects:
    print(f"Name: {row[0]}, Files Moved: {row[1]}")

# --- NEW QUERY 2: Find projects with a specific name ---
project_name_to_find = "Desktop Cleaner"
c.execute("SELECT * FROM projects WHERE name = ?", (project_name_to_find,))
specific_project = c.fetchone() # use fetchone() for a single result

print("\n--- Specific Project Details ---")
if specific_project:
    print(f"ID: {specific_project[0]}, Is Active: {specific_project[3]}")
else:
    print("Project not found.")
    
# 6. Close the Connection
conn.close()