from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .myviews.Mail_Send import my_mail_send
from mytool.myviews.Thread_tool import MyThread

import json

# Create your views here.


def mymail(request,service=None):
#    prints = PrintThread()
    if request.body:
        reqbody = json.loads(request.body)
        reqcontent_type = request.content_type
        requserid = reqbody['userid']
        reqmsg_title = reqbody['msg_title']
        reqmsg_body = reqbody['msg_body']
        mails = MyThread(my_mail_send,requserid=requserid,reqmsg_title=reqmsg_title,reqmsg_body=reqmsg_body)
        mails.start()
    '''
    send_mail
    '''
    return(JsonResponse({'status': 0, 'msg': 'success'}))

def index(request,service=None):
    if(request.method == 'POST' and service == 'mail' ):
        result=mymail(request,service)
        return(result)
    else:
        return(JsonResponse({'status': 400, 'msg': 'failed'}))