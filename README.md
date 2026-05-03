# Atlanta-crime-analysis
Visualzing Atlanta neighborhood crime trends using SQL and Python

--
## Business Questions
- Which Atlanta neighborhoods have the highest number of incidents?
- What crime types are most common by zone or NPU?
- How do crime rates trend month over month?
- What time of day do most incidents occur?
- How does my neighborhood (DeKalb) compare to others?

--
## Dataset
Source: https://opendata.atlantapd.org -- Atlanta Police Department Open Data
Format: CSV (by month, year, crime type)
Fields include: date, time, neighborhood, NPU, police zone, crime type, location

--
## Tech Stack
SQLite -- local database to store and query the data
SQL --  core analysis layer
Python -- data loading and Flask API
Flask --  serves query results as JSON endpoints


--
## How to Run

--
## Project Structure
atlanta-crime-analysis
README.md
schema.sql # table definitions

data/
    README.md # instruction on how to download data 


queries/
    by_neighborhood.sql
    by_crime_type.sql
    by_time_of_day.sql
    monthly_trends.sql

app/
    app.py #Flask API
    db.py #DB connection helper

findings.md #Summary of Key Insights

--
## Key Findings
TBA

--
## Future Improvements
Add date range filtering to the API
Build a simple frontend dashboard
Add an interactive map (Leaflet.js) to visualize incidents by neighborhood
Compare year-over-year crime trends
Predictive Analysis
