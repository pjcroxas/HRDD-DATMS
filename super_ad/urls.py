from django.urls import path
from . import views

urlpatterns = [
	path('', views.sa_dashboard, name = 'sadash-dash'),
	path('sa_log/', views.sa_log, name = 'sadash-log'),
	path('record_dash/', views.record_dash, name = 'sarec-dash'),
]