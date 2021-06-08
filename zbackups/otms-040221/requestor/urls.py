from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import request_site, request_detail, new_application, load_sectors, preview_page
from django.urls import path

urlpatterns = [

    path('requests', views.request_site, name='request_page'),
    path('redirect_scholarship', views.redirect_scholarship, name='request_redirect_scholarship'),
    path('t_r', views.t_r, name='request_page1'),
    url(r'^request_details/(?P<pk>\d+)/$', views.request_detail, name='request_details'),
    url(r'^preview_page/(?P<pk>\d+)/$', views.preview_page, name='preview_page'),
    url(r'^requests/(?P<pk>\d+)/new_application/$', views.new_application.as_view(), name='scholarship_app'),
    path('ajax/load-sectors/', views.load_sectors, name='ajax_load_sectors'),
    url('edit/(?P<pk>\d+)/$', views.editpost.as_view(), name='editpost'),
    url('cancel/(?P<pk>\d+)/$', views.cancel, name='cancelpost'),
    # url(r'^request/(?P<pk>\d+)/new_scholarship/$', views.scholarship_app, name='scholarship_application')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
