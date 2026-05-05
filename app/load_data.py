import sqlite3
import csv
import os
import glob

###csv_path = os.path.join(base_dir, 'data', 'OpenDataWebsite_Crime_view_-3942881780502137226.csv') 
###Hard coded path to CSV, incorrected for deployment, replaced with glob to find any CSV in data folder

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_files = glob.glob(os.path.join(base_dir, 'data', '*.csv'))
database_path = os.path.join(base_dir, 'atlanta_crime.db')

#Connect to the SQLite DB -- also crewate the .db if it doesn't exist
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

#Opens CSV file and read its contents. -- Prints header columns for verification
for csv_path in csv_files:
    print(f"--Loading:{csv_path} into database...")
    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip  header row
        print('--Found Columns in CSV:', headers) 

        #Assembles crime table using headers found in CSV -- Create table names 'crimes' if it doesn't exist
        columns = ', '.join([f'"{col}" TEXT' for col in headers])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS crimes ({columns})') 
        print('--Table Created Successfully.')

        #Read remaining rows and insert into crimes DB
        for row in reader: 
            placeholders = ', '.join(['?' for _ in row])
            cursor.execute(f'INSERT INTO crimes VALUES ({placeholders})', row)
        
    #Save (commit) a; omserts tp the database
    conn.commit()
    print(f"--Data loaded successfully")
  

conn.close()
print ('--CSV file read successfully and Database connection closed.')

