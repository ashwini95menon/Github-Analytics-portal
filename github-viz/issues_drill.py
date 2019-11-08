import requests
import mysql.connector
from datetime import datetime

username = "xxxxxx"
token = "xxxxxxxxxxxx"


class IssuesDrill:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Uw626LGjKb",
            passwd="8MlzS2lZJK",
            database="Uw626LGjKb"
        )
        self.time_format = '%Y-%m-%d %H:%M:%S'

    def list_all_issues(self, urls):
        session = requests.session()
        mycursor = self.mydb.cursor()
        mycursor.execute("truncate table issues")
        for repo in urls:
            url1 = "http://api.github.com/repos/IBM/" + repo + "/issues?state=closed"
            authentication = session.get(url1, auth=(username, token))
            for issue in authentication.json():
                num = int(issue['number'])
                title = str(issue['title'].encode('utf-8'))
                created_at = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime(self.time_format)
                closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime(self.time_format)
                closed_by = str(issue['user']['login'].encode('utf-8'))
                query = "insert into issues values (%s, %s, %s, %s, %s, %s)"
                values = (num, title, created_at, closed_at, closed_by, repo)
                mycursor.execute(query, values)
                self.mydb.commit()
        mycursor.execute("select * from issues")
        select = mycursor.fetchall()
        return None

#if __name__=="__main__":
#    list_all_issues()

#ids = IssuesDrill()
#ids.list_all_issues(["mi-prometheus", "kui"])
