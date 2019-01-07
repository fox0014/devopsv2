
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('<str:service>', views.index, name='index'),
]