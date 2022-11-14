'''
pip install APScheduler

pip install pipenv

Action item for this project:

creating a directory in my current folder whose name is equal to unix timestamp
means a folder name will be unix timestamp
which i am getting by calling time.time() function
'''

import os
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    # os.mkdir(str(int(time.time())))
    f = open("demofile2.txt", "a")
    f.write("Inserted a new line and the time is: %s" % datetime.now() +'\n')
    f.close()
    
# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=5)

scheduler.start()



'''

# Run.
$ python cronjob.py
# Cron job is running
# Tick! The time is: 2019-09-23 01:54:15.210989
'''