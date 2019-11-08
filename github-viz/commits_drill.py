from pydriller import RepositoryMining
import mysql.connector
import datetime


class CommitsDrill:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Uw626LGjKb",
            passwd="8MlzS2lZJK",
            database="Uw626LGjKb"
        )
        self.time_format = '%Y-%m-%d %H:%M:%S'

    def commits(self, urls):
        url_no = 1
        for repo in urls:
            mycursor = self.mydb.cursor()
            count = 0
            url = "https://github.com/IBM/" + str(repo)
            mycursor.execute("truncate table commits")
            for commit in RepositoryMining(url).traverse_commits():
                #if "bug" in commit.msg:
                # datetime , commit.committer_date.strftime(self.time_format) (hash, project_name, author_name, modification_type, timezone, branch, commiter_date)
                query = "insert into commits values (%s, %s, %s, %s, %s, %s, %s)"
                values = (str(commit.hash), str(commit.project_name), str(commit.author.name),
                          int(len(commit.modifications)), int(commit.author_timezone),
                          str(commit.branches), commit.committer_date.strftime(self.time_format))
                mycursor.execute(query, values)
                self.mydb.commit()
                #    count += 1
            url_no += 1
        mycursor.execute("select * from commits")
        select = mycursor.fetchall()
        return None


#cd = CommitsDrill()
#x = cd.commits(['kui'])
#print(x)
