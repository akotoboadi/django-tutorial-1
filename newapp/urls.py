from django.urls import path
from . import views

urlpatterns = [
    path('',views.greet1,name='greet1'),
    #path('<str:name>',views.greet,name ='greet'), this is what accepts a name as a route nd uses the name as a variable in the route.
    path('index',views.index,name ='index'),
    path('counter',views.counter,name ='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('post/<str:pk>',views.post,name='post'),
    path('profile',views.profile,name='profile'),



]