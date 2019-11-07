# Milestone 2: Portal

### Use Cases
Based on discussions had, following are the modified use-cases.


#### Use Case 1: Manager wants to know the trend of bugs resolution in a project

1. Preconditions: 
   Here by bugs, we refer to issues which are tagged as "bug"
   Information about bugsand developers is available on the issues tab of the respective GitHub repository. Manager needs to visualise this information.

2. Main flow: 
   User selects the repository to assess bugs in and requests for information regarding it(such as bugs solved monthly in a repository and bugs solved by developers for selected repositories) , which is displayed on the portal. They can select the project as well as the developers they want to assess.

3. Sub Flow: 
    1. User selects the repository they want information about
    2. Portal fetches the visualisation related to that repository 
    3. User chooses the project to include/exclude
    4. Portal filters the fields belonging (or not) to the project user selected
    5. User chooses a certain developer they want (or don't want) to assess
    6. Portal displays visualisation based on the above filter
    7. The visualization shows the following metrics
       (i) For each repository, the number of bugs solved by each developer
       (ii) Bugs solved per month in each repository
    
#### Use case 2: Manager wants to assess the issues resolved by developers and their contribution

1. Preconditions: 
   Information about issues is available. This means the reposotories have certain issues present in the issues tab of GitHub.

2. Main Flow: 
   User selects the repository to assess developer performance. The portal displays their contribution in the form of pie charts and lists issues resolved by each developer and the amount of time it took to resolve each issue.

3. Sub Flow: 
    1. User selects the repository they want mined
    2. Portal displays information from this repository 
    3. User picks the year from which to obtain visualisations
    4. Portal shows results from the selected year
    
#### Use Case 3: Manager wants to know about any new libraries used
 
1. Preconditions:
   There should be a sufficient number of new libraries used. A list of all previously used libraries should be available too.
   The visulaizations are available for programming languages like C, C++, Java, Python. Hence, the repository should contain some files in these languages.
 
2.	Main Flow:
    User selects repositories to find out about new libraries. The portal displays all new libraries found along with their usage, segregated based on the langauge. 
 
3.	Sub Flow:
    1. User selects the repositories they wish to look for new libraries in
    2. Portal fetches information about those repositories and displays the number of occurences of each library along with every language's percentage distribution.
    3. User chooses which libraries to include/exclude 
    4. Portal displays results in the form of pie charts based on user's filter


-----
### Mocking
We have implemented mocking using certain mock repositories and their data pertaining to commits, issues and libraries, sourced from NCSU's enterprise account as well as from GitHub. There are three independent data stores that have been generated, stipulated by the above use cases which, in addition to being recorded in the `backend/mock_data/` directory, have been elucidated below:

 #### 1. Bugs Encountered [UC1]
 
   The [`bugs_encountered.csv`](https://github.ncsu.edu/adhaval/csc510-project/blob/master/backend/mock_data/bugs_encountered.csv)/[`bugs_encountered.json`](https://github.ncsu.edu/adhaval/csc510-project/blob/master/backend/mock_data/bugs_encountered.json) files pertaining to this contain the following attributes:
 
   1. Commit Hash 
   2. Repository name   
   3. Developer's name (involved in resolution)    
   4. Length of their modification (in LoC)   
   5. Timezone (in seconds epoch)   
   6. Branch in which resolution was committed
   7. Timestamp of commit
 
##### CSV:  
`69d0c4af7eeb1ffa5255ef3ace0f51b4568b94f0,mi-prometheus,Younes Bouhadjar,6,25200,{'develop'},2018-03-22 16:15:36-07:00  
037905ed3063167d6cd8f16f412f3cf1a7f366cb,mi-prometheus,Younes Bouhadjar,7,25200,{'develop'},2018-03-28 17:20:30-07:00  
ce0b4628b2301c17e22647a0cbe0fbdb46179796,mi-prometheus,Younes Bouhadjar,8,25200,{'develop'},2018-03-29 15:30:17-07:00`

##### JSON:  
`{"commit.hash": "69d0c4af7eeb1ffa5255ef3ace0f51b4568b94f0", "commit.project_name": "mi-prometheus", "commit.author.name": "Younes Bouhadjar", "len(commit.modifications)": "6", "commit.author_timezone": "25200", "commit.branches": "{'develop'}", "commit.committer_date": "2018-03-22 16:15:36-07:00"}`
 
   These attributes have been generated in a fashion modeled on the data we obtained by scraping GitHub repositories using our scripts found in [`backend/scripts/`](https://github.ncsu.edu/adhaval/csc510-project/tree/master/backend/scripts). Despite being a very valuable attribute, timezone is generated in a numeric format and needs to be converted into a format that can be parsed by Tableau.
 
 #### 2. Timeline of Issues Resolved by Developers [UC2]
 
   All issues resloved by developers have been enumerated in [`developers.csv`](https://github.ncsu.edu/adhaval/csc510-project/blob/master/backend/mock_data/developers.csv)/[`developers.json`](https://github.ncsu.edu/adhaval/csc510-project/blob/master/backend/mock_data/developers.json) represented by means of the following features:
    
   1. Issue Number 
   2. Issue Name 
   3. Created at (timestamp)
   4. Closed at (timestamp)
   5. Closed by (username)
    
   To generate its visualisation, a time difference between `Created at` and `Closed at` has been evaluated and charted against `Closed by` to quantify developers' efficiency.
    
 ##### CSV:  
 `95,Cut more Wolfbot PCBs,2014-03-21T16:55:09Z,2014-03-26T17:19:11Z,ghost  
93,Wiki entry for Opti-track calibrations and trackables,2014-02-04T01:29:23Z,2014-02-04T01:34:25Z,ghost  
92,Unique tracking identifyers via Optitrack,2014-01-31T00:06:45Z,2014-04-01T21:23:56Z,ghost`  
 
 ##### JSON:  
 `{"closed_at": "2014-03-26T17:19:11Z", "created_at": "2014-03-21T16:55:09Z", "issue": "95", "closed_by": "ghost", "title": "Cut more Wolfbot PCBs"}`
    
 #### 3. New Libraries Encountered [UC3]
 
   Few, if any, new libraries were found in the repositories we had originally planned to work with, due to which after generation of the scraped output, we had to populate the [`libraries.csv`](https://github.ncsu.edu/adhaval/csc510-project/blob/master/backend/mock_data/libraries.csv) file with other libraries in each language (`Python`, `Java`, `C++`, `C`). Two attributes have been extracted to serve the purpose of our final use case:
    
   1. Langauge
   2. Library

##### CSV:  
`Python,theano
Python,pytorch
Python,kafka`

##### JSON:  
`{"Language": "Python", "Library": "theano"}  
{"Language": "Python", "Library": "pytorch"}`


#### Limitations and Possible Future Enhancements 

   1. The timeframe of current commits spanned a year in our repositories and necessitated a reassessment of our original sprint period, which would vary subject to an organisation's standards, depending on how the project is paced or at users' discretion.
   2. Currently, for the libraries use case, we have created dummy files in each laguage from where we are pulling the data. In the upcoming milestone, the data would be populated from real time repositories and actual code files. 
   
   We would be overcoming these limitations in the upcoming milestones when working with larger repositories with multiple contributors and a variety of libraries. We would customise our code based on the comapany's sprint periods and their language usage. For the libraries use case, in this milestone, we have considered 4 languages (`Python`, `Java`, `C++`, `C`). This would be further improvised based on the repositories set we choose to analyse in the further milestones.

-----

### Portal Implementation
 
Currently, we have implemented the three use cases mentioned above and are able to obtain a visualization for them using Tableau. The related code can be found here :

[Backend Code](https://github.ncsu.edu/adhaval/csc510-project/tree/master/backend)  
[Frontend Code](https://github.ncsu.edu/adhaval/csc510-project/tree/master/WebPage)


#### Details

##### Scripts
The scripts needed to get the data from GitHub repositories have been written in Python. For the “libraries” use-case, we have used a Python library called Pydriller.
Visualization : The visualization has been performed on Tableau Desktop. Once the necessary metrics were finalized and set, the visualizations were published on Tableau Public. 

##### Webpage 
The webpage for the portal was created using HTML. The list of repositories is listed first. Based on the ones that are of the user’s interest, the user can select the repositories and visualize them. This further embeds the Tableau visualization performed for the selected repositories. 

For this milestone, we were able to scrape relevant data from GitHub repositories, store the same in CSV/JSON files and use it to form a visualization on Tableau. This visualization was then exported and further embedded in an HTML page where the user can see the metrics needed. 

As of now, the data is static and  is extracted from some GitHub repositories we have taken as demo GitHub repositories. In the next stage of the project, we intend to add a continuous ingest of data. The data will also be stored in a database and will be pulled on a weekly basis. The data we look forward to using in the next milestone would be from repositories of the same company which the  user would be interested in seeing the stats of.

Visualisations from our portal have been depicted below:

![alt text](https://github.ncsu.edu/adhaval/csc510-project/blob/master/images/ms2_viz1.png)

![alt text](https://github.ncsu.edu/adhaval/csc510-project/blob/master/images/ms2_viz2.png)

![alt text](https://github.ncsu.edu/adhaval/csc510-project/blob/master/images/ms2_viz3.png)

-----

### Task Tracking
Link to [WORKSHEET.md](https://github.ncsu.edu/adhaval/csc510-project/blob/master/WORKSHEET.md)

-----

### Screencast
The screencast for the implementation phase 1 can be found [here](https://drive.google.com/open?id=11YUSBKubf2NmozqIPmkunWUTJMNPEDzo). 
