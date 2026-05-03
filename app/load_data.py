import sqlite3
import csv
import os

#Define the path to database and the CSV file
##DATABASE_PATH = 'database.db'
##CSV_FILE_PATH = 'OpenDataWebsite_Crime_view_-3942881780502137226.csv'

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'data', 'OpenDataWebsite_Crime_view_-3942881780502137226.csv')
database_path = os.path.join(base_dir, 'atlanta_crime.db')

#Connect to the SQLite DB -- also crewate the .db if it doesn't exist
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

#Open the CSV file and read its contents
#Print header columns for verification
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip  header row
    print('--Found Columns in CSV:', headers) 

    #Create crime table using headers found in CSV
    #Create table names 'crimes' if it doesn't exist
    columns = ', '.join([f'"{col}" TEXT' for col in headers])
    cursor.execute(f'CREATE TABLE IF NOT EXISTS crimes ({columns})') 
    print('--Table Created Successfully.')
  

conn.close()
print ('--CSV file read successfully and Database connection closed.')

#Read remaining rows and insert into crimes DB
for row in reader: 
    placeholders = ', '.join(['?' for _ in row])
    cursor.execute(f'INSET INTO crimes VALUES ({placeholders})', row)




#Save (commit) a; omserts tp the database
conn.commit()
print(f"data loaded successfully")