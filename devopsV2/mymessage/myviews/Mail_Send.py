from django.conf import settings
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

def my_mail_send(*args,**kwargs):
 #   print(args,kwargs)
    requserid = args[1]['requserid']
    reqmsg_title = args[1]['reqmsg_title']
    reqmsg_body = args[1]['reqmsg_body']
    result=send_mail(
        reqmsg_title,
        reqmsg_body,
        settings.DEFAULT_FROM_EMAIL,
        [requserid],
        fail_silently=False,
    )
    logger.info(result)
    return(result)