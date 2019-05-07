from django.db import models
import uuid

# Create your models here.


class message(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    senduser_name  = models.CharField(max_length=200)
    recvuser_name  = models.CharField(max_length=200)
    ms_content = models.CharField(max_length=200)
    ms_title = models.CharField(max_length=200,default='ms_title')
    ms_code = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',auto_now=True)
    models.DateField()

    def __str__(self):
        return self.ms_content