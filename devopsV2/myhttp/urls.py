
from django.urls import path
 
#from . import views
from .myviews import views
 
urlpatterns = [
    path('index2', views.index2, name='index2'),
    path('<str:service>', views.index, name='index'),
]