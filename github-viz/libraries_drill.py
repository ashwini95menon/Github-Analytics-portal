import requests
import mysql.connector
from datetime import datetime

username = "xxxxxxx"
token = "xxxxxxxxxxxxxxxx"


class LibrariesDrill:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Uw626LGjKb",
            passwd="8MlzS2lZJK",
            database="Uw626LGjKb"
        )

    def list_all_libs(self, urls):
        session = requests.session()
        mycursor = self.mydb.cursor()
        for repo in urls:
            url1 = "http://api.github.com/repos/IBM/" + repo
            authentication = session.get(url1, auth=(username, token))
            for lib in authentication.json():
                query = "insert into libraries values (%s, %s)"
                values = (lib[0], lib[1])
                mycursor.execute(query, values)
                self.mydb.commit()
        mycursor.execute("select * from issues")
        select = mycursor.fetchall()
        return None
