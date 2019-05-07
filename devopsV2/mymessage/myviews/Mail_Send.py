from django.conf import settings
from django.core.mail import send_mail
from mymessage.models import message
import logging

logger = logging.getLogger(__name__)

def my_mail_send(*args,**kwargs):
 #   print(args,kwargs)
    requserid = args[1]['requserid']
    reqmsg_title = args[1]['reqmsg_title']
    reqmsg_body = args[1]['reqmsg_body']
    msobj = message(senduser_name=settings.DEFAULT_FROM_EMAIL,recvuser_name=requserid,ms_content=reqmsg_body,ms_title=reqmsg_title)
    logger.info(msobj.id)
    msobj.save()
    result=send_mail(
        reqmsg_title,
        reqmsg_body,
        settings.DEFAULT_FROM_EMAIL,
        [requserid],
        fail_silently=False,
    )
    logger.info(result)
    if result:
        logger.info(message.objects.all().filter(id=msobj.id).update(ms_code=1))
    return(result)