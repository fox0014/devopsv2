
from django.urls import path
 
#from . import views
from .myviews import views
 
urlpatterns = [
    path('remotehttp', views.remotehttp, name='remotehttp'),
    path('<str:service>', views.index, name='index'),
]