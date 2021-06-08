from django.urls import path
from . import views

urlpatterns = [
        path('', views.base, name='base-base'),
	path('main_base', views.main_base, name = "base-main"),
]

