# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:53:05 2019

@author: ameya
"""

import commits_drill
import libraries_drill
import issues_drill
import schedule
import time

def job():
    print("I'm working...")
    commits_drill.commits()
    libraries_drill.libraries()
    issues_drill.list_all_issues()


schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
