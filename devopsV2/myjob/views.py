from django.shortcuts import render
# Create your views here.
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .myviews import joblist


#test apscheduler
def job_go():
    sched = BackgroundScheduler()
    sched.add_job(joblist.my_job, 'interval', seconds=36000)
    sched.start()