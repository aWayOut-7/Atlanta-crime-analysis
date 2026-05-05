import sqlite3
import os
import sys

# Define the path to the SQLite database
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(base_dir, 'atlanta_crime.db')

#Sql file path is passedd as terminal argument when running 
sql_file = sys.argv[1]

#Reads SQL file, f shorthand for File 
with open(sql_file, 'r') as f: 
    query = f.read()

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

cursor.execute(query)
rows = cursor.fetchall()
# Prints each row returned by query
for row in rows: 
    print(row)

#Print total count of rows returned by query
print(f"\nTotal Results: {len(rows)}")

#close connection to database
conn.close()
