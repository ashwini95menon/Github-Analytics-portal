import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="github-viz.database.windows.net",
  user="ssmore@github-viz.database.windows.net",
  passwd="Github-viz",
  database="github-viz.database"
)

print(mydb)
mycursor = mydb.cursor()
time_format = '%Y-%m-%d %H:%M:%S'

mycursor.execute("insert into commits (hash, project_name, author_name, modification_type, timezone, branch, committer_date) values (%s, %s, %s, %s, %s, %s, %s)", ("jfsbiabfakfj", "whatsapp", "ameya", 20, 10002, "master", (datetime.datetime.now()).strftime(time_format)))
mydb.commit()
mycursor.execute("select * from commits")
ans = mycursor.fetchall()
print(ans)
