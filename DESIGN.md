# Problem Statement
Project managers who handle multiple projects hosted on GitHub have to rely on manual methods for extracting the information that needs to be derived from GitHub for any project. GitHub contains an enormous amount of information but is restricted in the kind of insights they generate because they are provided for only one repository at a time. Currently, the kind of insights that can be accessed through GitHub are pulse, contributors, commits, code frequency, network and forks. These are on a high level that does not delve into the details of any project, and although these insights are helpful to summarise a team’s work, they do not contribute towards any decision making on a larger scale for the management of an organization.

The information that GitHub hosts can potentially guide future work and often lays the foundation for future development. However, it is not yet being fully leveraged by GitHub. It does boast of being the world’s leading software development platform, but fails to address the primary goal of any project manager working in the field of software development - informed decision making - despite having the means and access to be able to provide that. Information like team contribution, project status, the kind of bugs resolved and issues fixed with each new release of a software are merely a few of many such insights that can be mined from data hosted by GitHub, but are not being utilised to their full potential. 

# Solution Description
Through this project, we want to address the need of having a central dashboard where a project manager can track activities of multiple projects. While tracking various projects it is necessary to keep track of product, process and project metrics and manually keeping such a track is a tedious task. Thus, an analytics board that understands the performance indicators that a manager wants to track and provides him/her a simplified visual representation should highly cut down on the time needed by the manager to maintain these records separately and processing them. GitHub repositories have a lot of data spanned over projects which needs to be extracted to gain knowledge and processed to useful insights to managers. These insights help the manager to dedicate time and resources to certain projects based on the progress that has been made.

Understanding the team’s effort and contribution, the kinds of issues fixed and the new libraries used for particular functionalities help the manager make decisions to direct the team efforts towards maximizing results and productivity. We will be mining GitHub repositories to provide a visual representation communicates the status of projects coherently. We plan to use Tableau to provide graphs and pie charts to track the metrics. As a summary, the manager will be able to view the statistics like how much increase in code volume was there over a duration of time(eg. 6 weeks), the number of commits made, issues solved, bugs identified and releases, if there have been any. On the dashboard, the metrics about new libraries introduced in different repositories, issues fixed in each repository and the developers responsible and a time-based graph on the quality of code in each repository will be made accessible for managers. Each metric can be explored in detail by clicking on the metric's view on the dashboard and further understanding the information that the dashboard provides.

# Use Cases

### Use case 1: Manager wants to know which developer fixed the maximum number of bugs in the last 6 weeks

1. Preconditions: 
    Issues with bugs are assigned to the developers

2. Main Flow: 
After the issues are assigned to developers and bugs are identified and the developers fix the bugs. A report about these is collected over the span of 6 weeks which is updated on the portal for manager to see who can analyse which developer fixed these bugs based on the time taken for the bugs and the criticality of it to make an informative decision. 

3. Sub Flow: 
    1. The developers identify the bugs in the issue and understand what fixes to be done.
    2. After the bugs are fixed a status report is made by the developers over the span of 6 weeks.
    3. This report are updated and will be seen on the portal which the manager can then see.
    4. The manager can then see from the portal of the number of bugs fixed by whom over the span of 6 weeks and can then take an informative decision on it.

     

### Use Case 2: The new libraries used over the last 6 weeks in a particular project - for every programming language
 
1.	Preconditions:
    Some projects must be developed in the past 6 weeks.
 
2.	Main Flow:
    1.  User wants to check which libraries are used in past 6 weeks.[S1]
    2.  He generates a bar graph showing libraries used in different languages in past 6 weeks.[S2]
 
3.	Sub Flow:
    1. User goes to homepage and selects the tab “Libraries Used” on Left side Menu.
    2. A bar graph is generated with different libraries used in past 6 weeks.
 
4.	Alternate Flows:
    1. No project is developed in past 6 weeks.


### Use Case 3: Quantify the software quality based on bugs and issues resolved since the most recent software release

1. Preconditions: 
    Information about the recent software release.

2. Main flow: Analysed graph can be seen on the portal showing the software quality based on the bugs and issues resolved and after the most recent release dates.

3. Sub Flow: 
    1. Software quality measured based on issues and bugs resolved. 
    2. Its quality decided based on the level and time taken  to resolve the issues.
    3. A graph is made against the most recent software release
    4. Section about the improvements in the software quality will be available in the portal
    5. On clicking on that you get to see the graph which shows  the software quality based on bugs and issues resolved since the most recent software release
    6. After analysis we can suggest on improvements that needs to be done to improve the software quality.

# Design Sketches

## StoryBoard
The first interaction of the manager with the analytics portal would be to set up the portal according to the repositories that need to be analysed. Once that is set up, the manager is able to see the statistics corresponding to those repositories.
![alt text](/images/Analyticsportal.PNG)


After the setup is done, the manager can frequently make use of the analytics portal to understand and monitor the work being done in various projects.
![alt text](/images/story2.PNG)

A raw design of the use cases, which are the visualizations the manager views is as follows :

![alt text](/images/mockUp.PNG)

![alt text](/images/usecase1.PNG)

<img src="/images/lang.png" width="500" />

![alt text](/images/Softwarequality.PNG)


# Architecture Description
The dashboard's primary purpose is to provide insights to the managers about project metrics provided for various project repositories that they wish to monitor. The manager would first select the repositories to be monitored and a timeline over which the repositories need to be monitored(eg. 3/6 weeks) as per the need. Once this has been selected, the dashboard will start displaying those metrics over that selected timeframe. This means the manager can start tracking project progress over the timeframe that has been selected. The dashboard is what is seen by the manager. To get the required display of metrics, a lot of processing of data goes on in the background. To understand how this processing goes on, we need to understand the architecture of the system.

For the analytics dashboard, the main architecture being used is Pipe and filter. This is because, the data is extracted and filtered at each stage before the user is able to view it. Various building blocks(components) make up the system. The components of the architecture diagram are as follows :

GitHub repositories : These are the project repositories being monitored for managers. A manager might need to monitor from as few as 1-2 to any number of repositories.

Python scripts : Data needs to be extracted from the GitHub repositories and mined such that relevant metrics are collected. Python scripts and ReST API are used to achieve this. Python scripts form a means through which the relevant data is extracted and formatted into JSON.

Database : The JSON data is stored in a database from where it can be retrieved as and when it is required by the analytics for visualization purposes.

Tableau desktop : This component is used to decide and display the metrics locally. The use case based graphs and parameters can be decided here and then hosted on the server further.

Tableau server : The visualized data is hosted on the Tableau server, which is a SaaS platform that is accessible from PC, laptop or mobile devices.

Analytics dashboard : Managers can view the desired statistics here and make informed, data-driven decisions about processes and projects.

![image](https://media.github.ncsu.edu/user/10688/files/da1daf80-307b-11e9-829d-b66b50a83ce2)

The flow can be understood from the architecture diagram as follows: 
1. The data required for analysis(eg. commits, issues closed, etc) is extracted by making use of the GitHub REST API. Python scripts are used to extract data which is then formatted in JSON.

2. The Python scripts act as listeners in order to extract any changes done to the repository. The changes done to the repositories are mined and then stored in the database, before they can be visualized on the dashboard.

3. After the data(metrics) are collected and formatted, they are stored in the database. This data is stored until the next load has to be uploaded to the server.

4. The collected data is then made available on the Tableau desktop locally and the visualization task is performed here. 

5. From here, the visualizations made are hosted on Tableau server.

6. The managers can view the complete metrics they require to see on the analytics dashboard.

7. After the sprint/6 weeks are over, the data needs to be refreshed and the latest data needs to be made available for the manager.
    There is a need to ask the previous layer for the latest data.
    
8. Tableau server further checks with the previous layer, Tableau desktop for data availability for the new visualizations.

9. The Tableau desktop then queries the database for availability of the latest data and that is made visible in the same order (steps 4,5,6) on the analytics dashboard.

There are certain constraints and guidelines that a manager should keep in mind while using the portal. The information obtained from the portal will be updated on a daily basis. There isn’t much meaningful work that can be captured under the span of a single day to understand the progress of a project that spans for months together. Besides that, a manager can only view the projects they have been assigned or requested special access for. They are also not permitted a company level view which only executives of a company have access to. This maintains the hierarchy of an organisation. The portal would abide by the CIA model of security that stands for Confidentiality, Integrity and Availability. The data will never be accessed by unauthorised persons, in accordance with the property of Confidentiality. The property of Integrity holds that the data cannot be altered or modified. And according to the property of Availability, the data will be available for the authorised parties to access when needed. 
