
## Deployment 
In this milestone,  we have deployed our portal application on Heroku. This enables continuous integration. Whenever we make changes to our repository, the changes are reflected in Heroku. The steps to follow in order to deploy the application can be found in the README.md of the repository.

Link of the deployed application : Click [here](http://github-viz.herokuapp.com/)

## Data Ingest/Update
The data ingest takes place from GitHub repositories through Python scripts into a MySQL database. The MySQL database is updated with data from the repositories at a specified time every week. When the user asks for data from specified repositories, the database is queried and then, the resulting data is brought into the repository using Tableau MySQL connector. This required data is then used to create the appropriate visualizations and displayed to the user.

## Task Tracking
Link to [WORKSHEET.md](https://github.ncsu.edu/adhaval/csc510-project/blob/master/WORKSHEET_M4.md)

## Screencast
Link to [Screencast](https://drive.google.com/drive/folders/1DjYRy4VF0sMB2khZsR_7CBhubn4yjN4K?usp=sharing)
