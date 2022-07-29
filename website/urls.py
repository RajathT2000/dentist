from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('patients',views.patients,name="patients"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('news',views.news,name="news"),
    path('base',views.base,name="base")
]