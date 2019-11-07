### Implementation
All the three use cases vary mainly in their data and visualisations, besides which the processes are streamlined to remain consistent with the rest of the application. We have deployed the webpages on Heroku and are now scheduling data fetches at an interval of one week. These are the refinements and implementations of our portal:

1. Through our web interface, the user chooses which repositories they wish to view and pick one or more of them to generate a view of these.
2. The webpage's backend delivers a list of repositories to another (Python) script to fetch information about them. Using GitHub's REST APIs, this generates the required information. 
3. The script in connector.py calls functions in bugs_driller.py, libraries_drill.py and issues_drill.py on a weekly basis to create files in scripts/data_gen/ for each of the repositories. These files are replaced every week to reduce the space complexity. 
4. From amongst these files, we only use the ones our user has requested for and deliver those to the Tableau visualisation. 
5. The visulisation depicts the metrics according to the usecase chosen.

#### Implementation 
Here, we describe each use-case first and then describe how we have implemented the specifics. 

#### Use Case 1: Manager wants to know the trend of bugs resolution in a project

The flow described below(in the usecase) has been implemented. We have used the **pydriller** library of Python to extract the information about repositories - bugs fixed by developers and bugs fixed in the repositories. All information about the repositories is stored and the relevant repositories are visualized based on the user's choice. The visualization is displayed in Tablaeu and the user can choose to perform various operations on the data visualized.

1. Preconditions: 
   Here by bugs, we refer to issues which are tagged as "bug"
   Information about bugs and developers is available on the issues tab of the respective GitHub repository. Manager needs to visualise this information.

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

The flow described below(in the usecase) has been implemented. We have used the **GitHub API** to extract the information about repositories - issues solved by developers and average time needed to resolve those issues.. All information about the repositories is stored and the relevant repositories are visualized based on the user's choice. The visualization is displayed in Tablaeu and the user can choose to perform various operations on the data visualized.

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
 
The flow described below(in the usecase) has been implemented. We have used the **pydriller** library of Python to extract the information about repositories - new libraries used, their names and frequency. We have ensured to not consider the libraries that have been commented out. All information about the repositories is stored and the relevant repositories are visualized based on the user's choice. The visualization is displayed in Tablaeu and the user can choose to perform various operations on the data visualized.

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

### Task Tracking :

We have followed agile methodology for the task assigning and tracking of the project. We have had several meetings, brainstorming sessions, code reviews and explanation demos by each of us during the course of the milestone.
Link to [WORKSHEET.md](https://github.ncsu.edu/adhaval/csc510-project/blob/master/WORKSHEET_M3.md)

### Screencast : 
The link to the screencast can be found [here](https://drive.google.com/file/d/1JPoU287oEsCbWcGfuydeBUXTlc6B5VHn/view?usp=sharing).

### Next Steps :
In the next milestone, we have to streamline our end-to-end functionality and make the portal fully functional along with all services implemented. 
