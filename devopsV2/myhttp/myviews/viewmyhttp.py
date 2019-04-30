from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
import urllib.request
import logging
import json


log = logging.getLogger(__name__)

class MeataMyhttpsend(object):
    '''
    base http modle
    '''
    _headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
    
    def __init__(self,url):
        self.url = url

    def http_get(self):
        if self.url:      
            url = self.url
        else:
            url = "http://httpbin.org/get"
        req = urllib.request.Request(url,headers=self._headers)
        myresponse = urllib.request.urlopen(req).read()
        myresponse = myresponse.decode('utf-8')
#        print(myresponse)
#        print(myresponse.decode('utf-8'))
        try:  
            #json return beautiful
            myresponse = json.loads(myresponse)
            myresponse = json.dumps(myresponse,indent=4)
            myresponse = HttpResponse(myresponse,content_type='application/json')
#            myresponse = JsonResponse(myresponse, safe=False)
            return(myresponse)          
        except Exception as e:
            myresponse = myresponse
            logging.error(e)
        return(HttpResponse(myresponse.decode('utf-8')))
    
    def http_post(self,data):   
        data = {
           'first': 'true',
           'pn': 1,
           'kd': 'Python'
        }     
        url = self.url
        req = urllib.request.Request(url,headers=self.headers,data=data)          
        myresponse = urllib.request.urlopen(req).read()
        return(myresponse)    
