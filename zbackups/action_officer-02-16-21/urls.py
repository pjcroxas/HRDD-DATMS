from django.urls import path
from . import views

urlpatterns = [
	path('', views.sector, name = 'sector'),
	path('dashboard/<int:pk>', views.action_officer, name = 'action-dash'),
	path('new_sub/<int:pk>', views.new_sub, name = 'newsub'),
	path('followup', views.followup, name='followup'),
	path('followup_sch', views.followup_sch, name='followup_sch'),
	path('assigned/<int:pk>', views.assigned, name = 'assigned'),
	path('details/<int:pk>', views.requestdetails, name = 'requestdetails'),
	path('detailstravel/<int:pk>', views.requestdetailstravel, name = 'requestdetailstravel'),
	path('updatedetails/<int:pk>', views.updatedetails, name = 'updatedetails'),
	path('updatedetailstravel/<int:pk>', views.updatedetailstravel, name = 'updatedetailstravel'),
	path('new_sub/take/<int:tag>', views.take, name = 'take'),
	path('new_sub/taketravel/<int:tag>', views.taketravel, name = 'taketravel'),
	path('new_sub/take/<int:tag>/<str:cat>/<str:date>/<str:ln>/<str:fn>/<str:mi>/<str:pt>/<str:frm>/<str:to>/<str:ds>/<str:tid>/<str:last>/<str:email>', views.take, name = 'take'),
	path('officers', views.officersindex, name = 'officersindex'),
	path('officers/edit/<int:pk>', views.officers_edit, name = 'officers_edit'),
	path('officers/add/', views.officers_add, name = 'officers_add'),
	path('officers/block/<int:pk>', views.block, name='block'),
	path('officers/unblock/<int:pk>', views.unblock, name='unblock'),
	path('database/travel', views.dtravelforeign, name='dtravelforeign'),
	path('database/travel/<int:pk>',views.dtravelupdateforeign, name="dtravelupdateforeign"),
	path('database/travel-local/<int:pk>',views.dtravelupdatelocal, name="dtravelupdatelocal"),
	path('database/travel-local', views.dtravellocal, name='dtravellocal'),
	path('password/<int:pk>', views.change_password, name='change_password'),
	path('database/scholarship', views.dscholarship, name='dscholarship'),
	path('database/scholarship/<int:pk>', views.dupdatescholarship, name='dupdatescholarship'),
	path('new_sub/takescholar/<int:tag>', views.takescholar, name = 'takescholar'),

	# graphical reports
	path('graphical_reports', views.travel_request_stat, name='graphical_reports'),
	# GEDSI
	path('gender_reports', views.gedsi_search, name='_gedsi_search'),
	path('disability_reports', views.disability_search, name='_disability_search'),
	path('ethnicity_reports', views.ethnicity_search, name='_ethnicity_search'),





]
