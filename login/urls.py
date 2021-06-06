from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views as user_views
from .forms import CustomAuthForm

urlpatterns = [
        path('', auth_views.LoginView.as_view(template_name='login/login.html', redirect_authenticated_user = True, authentication_form=CustomAuthForm), name = 'login-login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name = 'login-logout'),
        path('banner/', user_views.banner, name = 'login-banner'),
        path('reset/', user_views.reset, name = 'login-reset'),
        path('linkreset/<str:poll_id>', user_views.linkreset, name = 'login-linkreset'),

]
