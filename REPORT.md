Screencast Link - [Here](https://drive.google.com/open?id=12W_ObjR67FYFHSkMZnkuZAk0swaaqpbx)

## PROJECT REPORT

### Problem
The information hosted by GitHub for projects is currently specific to that project only and from a manager's perspective not useful to to make people and process related decisions. The kind of insights that can be accessed through GitHub are pulse, contributors, commits, code frequency, network and forks. These are on a high level that does not delve into the details of any project, and although these insights are helpful to summarise a team’s work, they do not contribute towards any decision making on a larger scale for the management of an organization. Through our project we addressed the problem managers usually face while decision making in teams. This project attempts to visualize product, process and project metrics for the managers. Managers, who are pivotal to decision making, are usually not presented with a reliable source of information to help with decision making. Our portal addresses this issue by directly mining data from GitHub. Our app is best suited to very large teams where managers cannot keep track of each team member and need some high level insights into the team's performance to be able to gauge it. In situations where teams work together remotely and managers do not have the resources or the capacity to personally monitor each team member's performance, a portal that summarises all project activity on GitHub would prove to be a practical approach to save employees' time and resources.

### Features
There are three primary features of our project, namely:
##### 1. Commits  
   Each team member's commits in a respository are tracked by us. Both the number of commits as well as the volume of commits are estimated. The volume of commits determines the amount of change each commit incorporated in terms of lines of code. This makes it easier to weed out commits that may have been redundant or unnecessary like file name changes, while giving more importance to changes that reflect actual work.  
![alt text](/images/commits.png)

##### 2. Issues  
   Adding to our first use case, this feature allows project managers to visualise which developers solved which issues and the amount of time they took to solve it. These issues are issues which are tagged as "bugs". The granuality of time tracking is in days so that more complex problems are also reflected in proportion to the time it took to solve them. One such visualisation is depicted below:  

![alt text](/images/issues.png)

##### 3. Libraries
   There are various libraries that projects make use of, some are standard and other may have come into use quite recently. To find out about such libraries, our project provides another functoinality that lets you visualise all the new libraries that files in the chosen repository or repositories have made use of.  
<img width="1280" alt="screen shot 2019-04-26 at 12 48 36 pm" src="https://media.github.ncsu.edu/user/10688/files/71447780-6822-11e9-97ee-3c0463d4b9a1">

Besides these, there are a couple of other fetaures that our project offers:  

##### 4. Multiple Repositories View  
   A functionality that GitHub does not currently offer is the capability to visualise activity (insights) over multiple repositories. This can be incredibly useful for project managers who handle multiple projects at a time and need a single platform to assess projects either relatively or standalone. They get to decide which projects they wish to access information about.  
   
##### 5. Enterprise level solution  
   This application can be extended and deployed to any enterprise (Organization/Company) that uses GitHub repositories as a version control system and a project management system to keep all the projects in one place. Currently, we have used repositories from IBM. In order to extend our application, we can have data stored from various other organizations and have to authenticate the users and visualize relevant data.
   

### Reflection
#### What worked for our team :
1. We followed an agile development process which progressed in three week sprints. Tasks were assigned each week and the extent of their accomplishment by the end of each week laid foundation for the assignment of tasks in the following weeks. This process was incredibly helpful for teams like ours in which team members had neither worked with each other or with softwares like Tableau, Heroku or Flask before this project. The kind of incremental work done throughout the milestones allowed us to scale up our application and we successfully deployed a web app by the end of the semester.  

2. The use of GitHub ReST API and libraries like PyDriller helped us write our use-case scripts in a very efficient manner which would have otherwise been extremely tedious to do if we had to write the entire HTTP GET and POST calls by ourselves.

#### What could be done better :

1. In retrospect, we noticed that as we progressed with the project, we had clearly separated the work among the members and the integration part of the components took us quite sometime towards the last couple of milestones. If we had to do something differently, we would prefer having an integrated and deployed basic application right from the beginning which we could build and add features to.

2. We could also have chosen another Visualization tool other than Tableau since we had a lot of time and effort spent in order to figure out how to make the Free version work like the Tableau Server paid version. Instead, if we would have chosen a better visualization tool/API (eg. Google Charts API) it would have made our life easy.

### Limitations and Future Work
  1. Our project currently works on one organisation's repositories. However, it is flexible enough to scale up to work with larger organisations that designate work to specialised sub-organisations. Scaling up the web app would invlove larger, cloud based databases and high capacity servers that could handle more traffic than the current version of the web app. This can be implemented in the future.

  2. Tableau has various products that we can host our visualisations on. We have hosted ours on a free trial version that has a limited time validity. For a permanent platform, especially to scale this up for firms, we would need access to the paid versions of Tableau's softwares which also offer more flexibility, bandwidth and speed than the free versions.  

  3. The scope of this project is restricted to organisations that work in software development. It would be much more helpful if catered to organisations that do not primarily work with software but need insights on the software instead.  

  4. An extension to the second limitation is the speed of execution of our web app, which is quite low due low bandwidth of the servers we are currently using. This is easily fixed by purchasing higher capacity servers to replace the one we are currently working with.  
  
  5. There is a standard set of languages for which this project supports the third use case of finding new libraries used. These are - Python, Java, C and C++. However, this functionality can be extended to other languages as and when needed.
