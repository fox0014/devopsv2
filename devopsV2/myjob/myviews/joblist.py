from django.shortcuts import render
# Create your views here.
import logging
import time

log = logging.getLogger(__name__)

def my_job():
    log.info(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))