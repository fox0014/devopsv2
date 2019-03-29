# -*-coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse,JsonResponse



class Mymessage_Chekmail(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def process_request(self, request):
    # Mymessage_Chek1 request
        print('Mymessage_Chek1 request')

    def process_response(self, request, response):
        print('Mymessage_Chek1 return')
        return response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path == '/message/mail/' or request.path == '/message/mail':
            if(request.method == 'GET'):
                return(JsonResponse({'status': 400, 'msg': 'do not use GET'}))        
#        print('Mymessage_Chek1 before view')
        response = self.get_response(request)

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('Mymessage_Chek1 behind view')

        return response