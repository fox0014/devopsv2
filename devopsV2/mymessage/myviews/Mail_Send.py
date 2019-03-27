from django.conf import settings
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

def my_mail_send(userid):
    result=send_mail(
        'Subject here',
        "Here is the message %s" % userid,
        settings.DEFAULT_FROM_EMAIL,
        [userid],
        fail_silently=False,
    )
    logger.info(result)
    return(result)