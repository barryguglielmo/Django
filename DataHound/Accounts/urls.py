from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^your_home/$', views.your_home, name = 'your_home'),
    url(r'^register/$', views.Register.as_view(), name = 'register'),
    url(r'^login/$', views.LoginView.as_view(), name = 'login'),
    url(r'^NewCsv/$', views.New_CSV, name = 'NewCsv'),
    url(r'^DataListView/$', views.DataListView.as_view(), name = 'DataListView'),
    url(r'^simple_graph/$', views.simple_graph, name = 'simple_graph'),
    url(r'^bodata.csv/$', views.bodata, name = 'bodata'),
    url(r'^logout_view/$', views.logout_view, name = 'logout_view'),


]
