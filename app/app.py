import sqlite3
import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask import send_from_directory

#creates Flask app instance
app = Flask(__name__)
CORS(app)


#path to database, assumes it's in the parent directory of app
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(base_dir, 'atlanta_crime.db')

def run_query(sql_file):
    with open(sql_file, 'r') as f:
        query = f.read()
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

@app.route('/')
def index():
    return send_from_directory('..','index.html')

@app.route('/api/neighborhoods')
def neighborhoods():
    return jsonify(run_query('queries/by_Hood.sql'))

@app.route('/api/TimeOfDay')
def time_of_day():
    return jsonify(run_query('queries/by_ToD.sql'))

@app.route('/api/zones')
def zones():
    return jsonify(run_query('queries/by_Zone.sql'))

@app.route('/api/ZoneByTimeofDay')
def zone_by_time_of_day():
    return jsonify(run_query('queries/zone_by_tod.sql'))

# @app.route('/api/ZoneByTimeofDay')
# def zone_by_time_of_day():
#     return jsonify(run_query('queries/zone_by_tod.sql'))

if __name__ == '__main__':
    app.run(debug=True)