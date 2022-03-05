from django.urls import path

from .views import *
urlpatterns = [
    path('',loginview,name = "loginpage"),
    path('homepage/',homepageview,name = "homepage"),
    path('login/validate/',loginuser,name = "loginuser"),
    path('signup/',signupview,name = "signuppage"),
    path('signup/register/',registeruser,name = "registeruser"),
    path('logout/',logoutuser,name = "logoutuser"),

    #course urls
    path('course/<int:courseid>/',courseview),
    path('video/<int:videoid>/',videoview),

    path('about',about,name='aboutus'),
    

    
    ]