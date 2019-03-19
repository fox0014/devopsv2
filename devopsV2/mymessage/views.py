from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,JsonResponse

# Create your views here.

def mymail(request,service=None):
    send_mail(
    'Subject here',
    "Here is the message.%s" % service,
    settings.DEFAULT_FROM_EMAIL,
    ['huangyf@ev-link.com.cn'],
    fail_silently=False,
    )
    return(JsonResponse({'status': 0, 'msg': 'success'}))

def index(request,service=None):
    if(request.method == 'POST' and service == 'mail' ):
        result=mymail(request,service)
        return(result)
    else:
        return(JsonResponse({'status': 400, 'msg': 'failed'}))