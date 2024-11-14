from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('<str:name>',views.greet,name ='greet'), this is what accepts a name as a route nd uses the name as a variable in the route.
    path('greet1',views.greet1,name ='greet1'),
    path('counter',views.counter,name ='counter'),



]