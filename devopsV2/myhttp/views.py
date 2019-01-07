from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import urllib.request
import logging


log = logging.getLogger(__name__)

class Myconsule(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
    def getservice(self,services=None):
        catalog_service = "/v1/catalog/service/{services}".format(services=services)
        url = self.url + catalog_service
        req = urllib.request.Request(url,headers=self.headers)          
        myresponse = urllib.request.urlopen(req).read()
        return(myresponse)
    
def index(request,service=None):
    data = Myconsule('http://10.68.60.59:8500')
 #   clientservices=request.Get.get('service','')
    clientservices=request.path_info.split('/')[-1]
    redate = data.getservice(services=clientservices)
    print(redate.decode('utf-8'))
    return(HttpResponse(redate.decode('utf-8')))