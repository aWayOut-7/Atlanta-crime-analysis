import sqlite3
import os
import sys



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(base_dir, 'atlanta_crime.db')

sql_file = sys.argv[1]

#f shorthand for File 
with open(sql_file, 'r') as f: 
    query = f.read()

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

cursor.execute(query)
rows = cursor.fetchall()

for row in rows: 
    print(row)

print(f"\nTotal Results: {len(rows)}")
conn.close()
