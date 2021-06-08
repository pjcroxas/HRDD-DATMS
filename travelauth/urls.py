from django.urls import path
from . import views

urlpatterns = [
	path('', views.travelauth, name = 'travelauth-ta'),
	path('dash/', views.dash, name ='travelauth-dash'),
	path('edit_training/<int:tag>', views.edit_training, name = 'edit_training'),
	path('tic/', views.tic, name ='travelauth-ic'),
	path('tmc/', views.tmc, name ='travelauth-mc'),
	path('ltmc/', views.ltmc, name ='travelauth-lmc'),
	path('tts/', views.tts, name ='travelauth-ts'),
	path('ltts/', views.ltts, name ='travelauth-lts'),
	path('tfi/', views.tfi, name ='travelauth-fi'),
	path('ltfi/', views.ltfi, name ='travelauth-lfi'),
	path('tpt/', views.tpt, name ='travelauth-pt'),
	path('ltpt/', views.ltpt, name ='travelauth-lpt'),
	path('travel_files/<int:tag>', views.tf, name ='travelauth-tf'),
	path('main_dash/', views.main_dash, name ='travelauth-md'),
	path('local_dash/', views.local_dash, name ='travelauth-local_dash'),
	path('view/<int:tag>', views.view, name ='travelauth-v'),
	path('travel_report/', views.travel_report, name = 'travelauth-tr'),
	
	path('fup/<int:tag>/<str:assigned>/<str:ref>/<str:fn>/<str:mi>/<str:ln>/<str:pt>/<str:frm>/<str:to>/<str:dest>/<str:st>', views.fup, name = 'fup'), 
	
	path('nteinvitation/<int:tag>', views.nteinvitation, name ='travelauth-in'),
	path('ntetransportation/<int:tag>', views.ntetransportation, name ='travelauth-tr'),
	path('nteallowance/<int:tag>', views.nteallowance, name ='travelauth-al'),
	path('nteothers/<int:tag>', views.nteothers, name ='travelauth-ot'),	

	path('cancel/<int:tag>', views.cancel, name ='travelauth-c'),
	path('edit/<int:tag>', views.edit, name ='travelauth-e'),
	path('followup/<int:tag>', views.followup, name ='travelauth-followup'),
	path('history/<int:tag>', views.history, name ='travelauth-h'),
	path('edit_non_training/<int:tag>', views.edit_non_training, name ='travelauth-e'),
	path('edit_ntraining/<int:tag>', views.edit_ntraining, name ='travelauth-nt'),
	path('editpreregistration/<int:tag>', views.editpreregistration, name ='travelauth-preg'),
	path('editpds/<int:tag>', views.editpds, name ='travelauth-pds'),
	path('editipcr/<int:tag>', views.editipcr, name ='travelauth-ipcr'),
	path('editpaf/<int:tag>', views.editpaf, name ='travelauth-paf'),
	path('editreport/<int:tag>', views.editreport, name ='travelauth-report'),
	path('mceditendorsement/<int:tag>', views.mceditendorsement, name ='edit_endorsement_mc'),
	path('mcediticd/<int:tag>', views.mcediticd, name ='edit_icd_mc'),
	path('mceditinvitation/<int:tag>', views.mceditinvitation, name ='edit_invitation_mc'),
	path('mcedittask/<int:tag>', views.mcedittask, name ='edit_task_mc'),
	path('mceditcase/<int:tag>', views.mceditcase, name ='edit_case_mc'),
	path('mceditservice/<int:tag>', views.mceditservice, name ='edit_service_mc'),
	path('mceditfunds/<int:tag>', views.mceditfunds, name ='edit_funds_mc'),
	path('mceditexpenses/<int:tag>', views.mceditexpenses, name ='edit_expenses_mc'),
	path('mceditunliquidated/<int:tag>', views.mceditunliquidated, name ='edit_unliquidated_mc'),
	path('mceditretirement/<int:tag>', views.mceditretirement, name ='edit_retirement_mc'),
	path('mceditundertaking/<int:tag>', views.mceditundertaking, name ='edit_undertaking_mc'),
	path('iceditendorsement/<int:tag>', views.iceditendorsement, name ='edit_endorsement_ic'),
	path('icediticd/<int:tag>', views.icediticd, name ='edit_icd_ic'),
	path('iceditinvitation/<int:tag>', views.iceditinvitation, name ='edit_invitation_ic'),
	path('icedittask/<int:tag>', views.icedittask, name ='edit_task_ic'),
	path('iceditcase/<int:tag>', views.iceditcase, name ='edit_case_ic'),
	path('iceditservice/<int:tag>', views.iceditservice, name ='edit_service_ic'),
	path('iceditfunds/<int:tag>', views.iceditfunds, name ='edit_funds_ic'),
	path('iceditexpenses/<int:tag>', views.iceditexpenses, name ='edit_expenses_ic'),
	path('iceditunliquidated/<int:tag>', views.iceditunliquidated, name ='edit_unliquidated_ic'),
	path('iceditretirement/<int:tag>', views.iceditretirement, name ='edit_retirement_ic'),
	path('iceditundertaking/<int:tag>', views.iceditundertaking, name ='edit_undertaking_ic'),
	path('tseditendorsement/<int:tag>', views.tseditendorsement, name ='edit_endorsement_ts'),
	path('tsediticd/<int:tag>', views.tsediticd, name ='edit_icd_ts'),
	path('tseditinvitation/<int:tag>', views.tseditinvitation, name ='edit_invitation_ts'),
	path('tseditacceptance/<int:tag>', views.tseditacceptance, name ='edit_acceptance_ts'),
	path('tseditminutes/<int:tag>', views.tseditminutes, name ='edit_minutes_ts'),
	path('tseditscholarship/<int:tag>', views.tseditscholarship, name ='edit_scholarship_ts'),
	path('tsedittask/<int:tag>', views.tsedittask, name ='edit_task_ts'),
	path('tseditcase/<int:tag>', views.tseditcase, name ='edit_case_ts'),
	path('tseditservice/<int:tag>', views.tseditservice, name ='edit_service_ts'),
	path('tseditfunds/<int:tag>', views.tseditfunds, name ='edit_funds_ts'),
	path('tseditexpenses/<int:tag>', views.tseditexpenses, name ='edit_expenses_ts'),
	path('tseditunliquidated/<int:tag>', views.tseditunliquidated, name ='edit_unliquidated_ts'),
	path('tseditretirement/<int:tag>', views.tseditretirement, name ='edit_retirement_ts'),
	path('tseditundertaking/<int:tag>', views.tseditundertaking, name ='edit_undertaking_ts'),
	path('fieditendorsement/<int:tag>', views.fieditendorsement, name ='edit_endorsement_fi'),
	path('fiediticd/<int:tag>', views.fiediticd, name ='edit_icd_fi'),
	path('fieditinvitation/<int:tag>', views.fieditinvitation, name ='edit_invitation_fi'),
	path('fieditagreement/<int:tag>', views.fieditagreement, name ='edit_agreement_fi'),
	path('fiedittask/<int:tag>', views.fiedittask, name ='edit_task_fi'),
	path('fieditcase/<int:tag>', views.fieditcase, name ='edit_case_fi'),
	path('fieditservice/<int:tag>', views.fieditservice, name ='edit_service_fi'),
	path('fieditfunds/<int:tag>', views.fieditfunds, name ='edit_funds_fi'),
	path('fieditexpenses/<int:tag>', views.fieditexpenses, name ='edit_expenses_fi'),
	path('fieditunliquidated/<int:tag>', views.fieditunliquidated, name ='edit_unliquidated_fi'),
	path('fieditretirement/<int:tag>', views.fieditretirement, name ='edit_retirement_fi'),
	path('fieditundertaking/<int:tag>', views.fieditundertaking, name ='edit_undertaking_fi'),
	path('ptediticd/<int:tag>', views.ptediticd, name = 'edit_icd_pt'),
	path('ptedittask/<int:tag>', views.ptedittask, name = 'edit_task_pt'),
	path('pteditcase/<int:tag>', views.pteditcase, name = 'edit_case_pt'),
	path('pteditservice/<int:tag>', views.pteditservice, name = 'edit_service_pt'),
	path('pteditleave/<int:tag>', views.pteditleave, name = 'edit_leave_pt'),
	path('pteditclearance/<int:tag>', views.pteditclearance, name = 'edit_clearance_pt'),
	path('a1edit/<int:tag>', views.a1edit, name = 'edit_a1'),
	path('a2edit/<int:tag>', views.a2edit, name = 'edit_a2'),

]