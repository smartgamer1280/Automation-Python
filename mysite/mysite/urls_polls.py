from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('create-poll/',views.main,name="main"),
    path('home/',views.index,name='home'),
    path('socialmedia-handles/',views.social,name="social"),  
    path('contact-us/',views.contact,name="contact"),
    path('about-us/',views.about,name="about"),
    path('log-in/',views.Login,name="login")

    
    
    
]
