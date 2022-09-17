from django.contrib import admin
from django.urls import path
from tutorials import views

admin.site.site_header = "UOH Admin"
admin.site.site_title = "UOH Admin Portal"
admin.site.index_title = "Welcome to UOH Online Voting System"

urlpatterns = [
    path('', views.index, name="home"),
    path('activities', views.activities, name='activities'),
    path('contactus', views.contactus, name='contactus'),
]
