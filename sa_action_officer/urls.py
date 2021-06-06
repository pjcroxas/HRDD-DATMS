from django.urls import path
from . import views

urlpatterns = [
	path('', views.sa_action_officer, name = 'sa_action-dash'),
]
