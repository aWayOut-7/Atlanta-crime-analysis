import sqlite3
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(base_dir, 'atlanta_crime.db')

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

cursor.execute(''Select )