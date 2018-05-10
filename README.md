# Visualization Project CUSP

# Team members
Ci(Hans)  He        NetID: ch3183
Chenrui   Zhang     NetID: cz1605

# Objectives of the projects including a brief context of the project, and what tasks you're aiming to solve using visualizations
This is the class final project for CUSP Urban Data Visualization. It is an interactive map visualizing the number of the 7 major felonies from year 2000 to 2017 by police precincts in New York City. The map is designed to help people(users) who are new to the city or who are trying to relocate within five boroughs or people who are just trying to compare their neighborhood to others. It demostrates the changing trend of major crimes in all NYC areas for the last 17 years time span.  Instead of reading police report(excel, PDF), users can be more efficient and effective to get a direct view of the major crimes levels utilizing this map. To sum up, the map is designed to:

## 1.Visualizing spatial distribution of the 7-major-felony.
2.Comparing different precincts felony levels.
3.Demostrating crime levels' changing trends in different precincts.
4.Providing reference information for people who are finding new rent,buying new home or just visiting the area. 

# Data set involves

The seven-major-felony-offenses by precinct from NYPD historical crime data statistics report. The report has Excel format and PDF format, we are using the Excel. The report has yearly aggregated number of each major felony in each precinct.
Link:
https://www1.nyc.gov/assets/nypd/downloads/excel/analysis_and_planning/historical-crime-data/seven-major-felony-offenses-by-precinct-2000-2017.xls


NYPD Geojson file. It covers NYC police precinct boundaries within five boroughs.
Link:
https://data.cityofnewyork.us/api/geospatial/78dh-3ptz?method=export&format=GeoJSON

# Descriptions on your visualization design choices. For example, why you're choosing the types of visualization, representations, and/or interactions in your project.



# Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.




# Visualization Tools Used
This data visualization uses D3.js, some modern front-end tools and techniques like React, Babel, npm and related cleaning and exploratory analysis with Python/pandas.

# Where is the map, See it live
https://hcpenguin.github.io/visproject_crime_map/

# Running locally
Step 1: Use command 'git clone' this repo
Step 2: Check whether you have the NODEjs(NPM) package in your machine, you can use the command line to check:
        
        npm -v
        
        If not, you can install from:
        
        https://nodejs.org/
        
Step 3: Within the directory you clone(download) this repo, run following command line:  

npm install  
npm run build  
npm run start  

Step 4: The map should be live on localhost:8080.

# Possible future work
- add ability to show/hide top 5 precincts with most crime number using a separate bar chart.
- add more precinct-based datasets, maybe combine with other demographic data.
