from django.urls import path
from . import views

urlpatterns = [
	path('', views.site_dash, name = 'site_dash-dash'),
	
]