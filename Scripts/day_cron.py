'''
pip install APScheduler

pip install pipenv

Action item for this project:

This cron job will run from daily from monday to friday at 5:46 am utc time

Runs from Monday to Friday at 5:46 (am) until 2022-12-30 00:00:00
'''
from datetime import datetime
# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

def cronjob():
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    f = open("demofile.txt", "a")
    f.write("Inserted a new line and the time is: %s" % datetime.now() +'\n')
    f.close()

sched = BlockingScheduler()

# sched.add_job(cronjob, "interval", seconds=5 )
# Runs from Monday to Friday at 5:46 (am) until 2022-12-30 00:00:00
sched.add_job(cronjob, 'cron', day_of_week='mon-fri', hour=5, minute=46, end_date='2022-12-30')

sched.start()
