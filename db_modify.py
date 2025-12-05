import sqlite3

# Connect to the existing database file
conn = sqlite3.connect('project_data.db')
c = conn.cursor()

print("--- Starting Database Modification ---")

# 1. UPDATE Command: Mark one record as inactive (is_active=0)
# We target the record with the lowest ID (which was inserted first)
c.execute('''
    UPDATE projects 
    SET is_active = 0 
    WHERE id = 1
''')
print(f"Updated {c.rowcount} record(s). ID 1 is now inactive.")

# 2. DELETE Command: Remove the duplicate record with the highest ID
# This cleans up the duplicate entry from your last run
c.execute("DELETE FROM projects WHERE id = (SELECT MAX(id) FROM projects)")
print(f"Deleted {c.rowcount} duplicate record(s).")

# 3. Commit the changes permanently
conn.commit()

# 4. Final Verification: Select ALL remaining records
c.execute("SELECT * FROM projects")
final_results = c.fetchall()

print("\n--- Final Project List ---")
if final_results:
    for row in final_results:
        # 1:id, 2:name, 3:files_moved, 4:is_active (1=True, 0=False)
        status = "Active" if row[3] == 1 else "Inactive"
        print(f"ID: {row[0]}, Name: {row[1]}, Status: {status}")
else:
    print("Database is empty.")

# Close the Connection
conn.close()