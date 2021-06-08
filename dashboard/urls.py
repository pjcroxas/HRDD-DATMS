from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name = 'dash-dash'),
	path('dashboard1/', views.dashboard1, name = 'dash-dash1'),
]