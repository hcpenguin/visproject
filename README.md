# Visualization Project CUSP

# Team members

Ci(Hans)  He        NetID: ch3183

Chenrui   Zhang     NetID: cz1605

# Objectives of the projects including a brief context of the project, and what tasks you're aiming to solve using visualizations, domain(target user) and task abstraction.
This is the class final project for CUSP Urban Data Visualization. It is an interactive map visualizing the number of the 7 major felonies from year 2000 to 2017 by police precincts in New York City. The map is designed to help people(users) who are new to the city or who are trying to relocate within five boroughs or people who are just trying to compare their neighborhood to others. It demostrates the changing trend of major crimes in all NYC areas for the last 17 years time span.  Instead of reading police report(excel, PDF), users can be more efficient and effective to get a direct view of the major crimes levels utilizing this map. To sum up, the map is designed to:

- Visualizing spatial distribution of the 7-major-felony.

- Comparing different precincts felony levels.

- Demostrating crime levels' changing trends in different precincts.

- Providing reference information for people who are finding new rent,buying new home or just visiting the area. 

# Data set involves

The seven-major-felony-offenses by precinct from NYPD historical crime data statistics report. The report has Excel format and PDF format, we are using the Excel. The report has yearly aggregated number of each major felony in each precinct.
Link:
https://www1.nyc.gov/assets/nypd/downloads/excel/analysis_and_planning/historical-crime-data/seven-major-felony-offenses-by-precinct-2000-2017.xls


NYPD Geojson file. It covers NYC police precinct boundaries within five boroughs.
Link:
https://data.cityofnewyork.us/api/geospatial/78dh-3ptz?method=export&format=GeoJSON

# Descriptions on your visualization design choices. For example, why you're choosing the types of visualization, representations, and/or interactions in your project.

Types of visualization:
Choropleth Geospatial Map. 
Choropleth maps are based on statistical data aggregated over previously defined regions (e.g., NYPD precincts in our case). Thus, where defined regions of precincts are important to our visualization, achoropleth map is preferred as the type of visualization.

Representations:

We use the single-hue progressions fade from a dark shade of the blue color to a very light or white shade of relatively the same hue. This is a common method used to map magnitude which is the same in our case. The darkest hue represents the greatest number in the data set and the lightest shade representing the least number. And we use the quantile to get even intervals between the lowerest to the highest number in each felony. 

Interactions:

The interactions line up with dataset's felonies category and temporal information.
User can choose any of the seven major felony from a dropdown list and the visualization will update the choropleth map in hue progression with that felony's data in that specific year. The hue intervals are updated with that felony's min and max number in the 17 years time span.
User also can use the slide to either going forward or backward to see each year(2000~2017) certain felony's choropleth map. This enables user to see the changing trend of the felony in all precincts.And compare magnitude among different areas. 


# Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.

The map was shown to some international students who are looking for housing rental for the coming semester, some of them are trying to move to another area, some of them are coming to New York in this Fall semester. They think this are very useful reference in their rent hunting, safety is one of the top consideration and even higher than the price range. Some people we know are looking for house to purchase or relocate with new job are also find this is very helpful for them to decide which neighborhood for their residency.
Overall, for users this tool is simple to use, fast to get information across the whole area and efficient to identiy user targeting areas and the adjecent neighbor areas. 

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
- add more precinct-based datasets, i.e. violations, misdemeanors
- combine with other demographic data.

