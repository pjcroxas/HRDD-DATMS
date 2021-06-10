from django.shortcuts import render, HttpResponseRedirect
from login.models import Author
from .models import TravelRequest_tbl, History_tbl,request_category, travel_sector, travel_office, Pending_training_report
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from requestor.models import Sector
from django.core.mail import send_mail
from OTMS.settings import EMAIL_HOST_USER
from django.shortcuts import redirect

# Create your views here.
def travelauth(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
	}

	if request.method == "POST":
		db = TravelRequest_tbl()
		db.request_category = request.POST.get('request_category')
		db.sub_category = request.POST.get('sub_category')
		db.support_category = request.POST.get('support_category')
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.requestor = request.user

		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/travelauth.html', query)


def dash(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
    }
	return render(request, 'travelauth/dash.html', query)

def local_dash(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
    }
	return render(request, 'travelauth/local_dash.html', query)


def tic(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'sec': travel_sector.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "International Commitment"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		db.ic_endorsement = request.FILES.get('endorsement')
		db.ic_icd = request.FILES.get('icd')
		db.ic_invitation = request.FILES.get('invitation')
		db.ic_no_pending_task = request.FILES.get('task')
		db.ic_no_admin_case = request.FILES.get('case')
		db.ic_service_record = request.FILES.get('service')
		db.ic_funds = request.FILES.get('funds')
		db.ic_expenses = request.FILES.get('expenses')
		db.ic_unliquidated = request.FILES.get('unliquidated')
		db.ic_retirement = request.FILES.get('retirement')
		db.ic_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "International Commitment"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6

		db.ic_endorsement = request.FILES.get('endorsement')
		db.ic_icd = request.FILES.get('icd')
		db.ic_invitation = request.FILES.get('invitation')
		db.ic_no_pending_task = request.FILES.get('task')
		db.ic_no_admin_case = request.FILES.get('case')
		db.ic_service_record = request.FILES.get('service')
		db.ic_funds = request.FILES.get('funds')
		db.ic_expenses = request.FILES.get('expenses')
		db.ic_unliquidated = request.FILES.get('unliquidated')
		db.ic_retirement = request.FILES.get('retirement')
		db.ic_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/t_ic.html', query)

def tmc(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'sec': travel_sector.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Meetings/Conferences/Special Missions"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		db.mc_endorsement = request.FILES.get('endorsement')
		db.mc_icd = request.FILES.get('icd')
		db.mc_invitation = request.FILES.get('invitation')
		db.mc_no_pending_task = request.FILES.get('task')
		db.mc_no_admin_case = request.FILES.get('case')
		db.mc_service_record = request.FILES.get('service')
		db.mc_funds = request.FILES.get('funds')
		db.mc_expenses = request.FILES.get('expenses')
		db.mc_unliquidated = request.FILES.get('unliquidated')
		db.mc_retirement = request.FILES.get('retirement')
		db.mc_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Meetings/Conferences/Special Missions"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6

		db.mc_endorsement = request.FILES.get('endorsement')
		db.mc_icd = request.FILES.get('icd')
		db.mc_invitation = request.FILES.get('invitation')
		db.mc_no_pending_task = request.FILES.get('task')
		db.mc_no_admin_case = request.FILES.get('case')
		db.mc_service_record = request.FILES.get('service')
		db.mc_funds = request.FILES.get('funds')
		db.mc_expenses = request.FILES.get('expenses')
		db.mc_unliquidated = request.FILES.get('unliquidated')
		db.mc_retirement = request.FILES.get('retirement')
		db.mc_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/t_mc.html', query)

def ltmc(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all()
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category = "Local"
		db.sub_category = request.POST.get('sub_category')
		db.support_category = "Meetings/Conferences/Special Missions"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		db.mc_endorsement = request.FILES['endorsement']
		db.mc_icd = request.FILES['icd']
		db.mc_invitation = request.FILES['invitation']
		db.mc_no_pending_task = request.FILES['task']
		db.mc_no_admin_case = request.FILES['case']
		db.mc_service_record = request.FILES['service']
		db.mc_funds = request.FILES['funds']
		db.mc_expenses = request.FILES['expenses']
		db.mc_unliquidated = request.FILES['unliquidated']
		db.mc_retirement = request.FILES['retirement']
		db.mc_undertaking = request.FILES['undertaking']
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category = "Local"
		db.sub_category = request.POST.get('sub_category')
		db.support_category = "Meetings/Conferences/Special Missions"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6

		db.mc_endorsement = request.FILES['endorsement']
		db.mc_icd = request.FILES['icd']
		db.mc_invitation = request.FILES['invitation']
		db.mc_no_pending_task = request.FILES['task']
		db.mc_no_admin_case = request.FILES['case']
		db.mc_service_record = request.FILES['service']
		db.mc_funds = request.FILES['funds']
		db.mc_expenses = request.FILES['expenses']
		db.mc_unliquidated = request.FILES['unliquidated']
		db.mc_retirement = request.FILES['retirement']
		db.mc_undertaking = request.FILES['undertaking']
		db.requestor = request.user

		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/ltmc.html', query)

def tts(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'sec': travel_sector.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Trainings/Scholarship/Seminars/Workshops"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		db.ts_endorsement = request.FILES.get('endorsement')
		db.ts_icd = request.FILES.get('icd')
		db.ts_invitation = request.FILES.get('invitation')
		db.ts_acceptance = request.FILES.get('acceptance')
		db.ts_minutes = request.FILES.get('minutes')
		db.ts_scholarship = request.FILES.get('scholarship')
		db.ts_no_pending_task = request.FILES.get('task')
		db.ts_no_admin_case = request.FILES.get('case')
		db.ts_service_record = request.FILES.get('service')
		db.ts_funds = request.FILES.get('funds')
		db.ts_expenses = request.FILES.get('expenses')
		db.ts_unliquidated = request.FILES.get('unliquidated')
		db.ts_retirement = request.FILES.get('retirement')
		db.ts_undertaking = request.FILES.get('undertaking')
		db.ts_report = request.FILES.get('report')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Trainings/Scholarship/Seminars/Workshops"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6
		db.ts_endorsement = request.FILES.get('endorsement')
		db.ts_icd = request.FILES.get('icd')
		db.ts_invitation = request.FILES.get('invitation')
		db.ts_acceptance = request.FILES.get('acceptance')
		db.ts_minutes = request.FILES.get('minutes')
		db.ts_scholarship = request.FILES.get('scholarship')
		db.ts_no_pending_task = request.FILES.get('task')
		db.ts_no_admin_case = request.FILES.get('case')
		db.ts_service_record = request.FILES.get('service')
		db.ts_funds = request.FILES.get('funds')
		db.ts_expenses = request.FILES.get('expenses')
		db.ts_unliquidated = request.FILES.get('unliquidated')
		db.ts_retirement = request.FILES.get('retirement')
		db.ts_undertaking = request.FILES.get('undertaking')
		db.ts_report = request.FILES.get('report')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/t_ts.html', query)

def ltts(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.destination = request.POST.get('destination')
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Training-Related Travel Request"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.name_title = request.POST.get('name_title')
		db.t_report = request.FILES.get('report')
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.nickname = request.POST.get('nname')
		db.salary_grade = request.POST.get('sg')
		db.email_address = request.POST.get('email')
		db.mobile_number = request.POST.get('mobile')
		db.age = request.POST.get('age')
		db.office_number = request.POST.get('office_number')
		db.address = request.POST.get('address')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		db.requestor = request.user
		db.save()		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.destination = request.POST.get('destination')
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "Training-Related Travel Request"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.name_title = request.POST.get('name_title')
		db.t_report = request.FILES.get('report')
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.nickname = request.POST.get('nname')
		db.salary_grade = request.POST.get('sg')
		db.email_address = request.POST.get('email')
		db.mobile_number = request.POST.get('mobile')
		db.age = request.POST.get('age')
		db.office_number = request.POST.get('office_number')
		db.address = request.POST.get('address')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/ltts.html', query)

def tfi(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'sec': travel_sector.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "FAT/Inspection"
		db.sector_ = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3
		
		db.fi_endorsement = request.FILES.get('endorsement')
		db.fi_icd = request.FILES.get('icd')
		db.fi_invitation = request.FILES.get('invitation')
		db.fi_agreement = request.FILES.get('agreement')
		db.fi_no_pending_task = request.FILES.get('task')
		db.fi_no_admin_case = request.FILES.get('case')
		db.fi_serivce_record = request.FILES.get('service')
		db.fi_funds = request.FILES.get('funds')
		db.fi_expenses = request.FILES.get('expenses')
		db.fi_unliquidated = request.FILES.get('unliquidated')
		db.fi_retirement = request.FILES.get('retirement')
		db.fi_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "FAT/Inspection"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6
		db.fi_endorsement = request.FILES.get('endorsement')
		db.fi_icd = request.FILES.get('icd')
		db.fi_invitation = request.FILES.get('invitation')
		db.fi_agreement = request.FILES.get('agreement')
		db.fi_no_pending_task = request.FILES.get('task')
		db.fi_no_admin_case = request.FILES.get('case')
		db.fi_serivce_record = request.FILES.get('service')
		db.fi_funds = request.FILES.get('funds')
		db.fi_expenses = request.FILES.get('expenses')
		db.fi_unliquidated = request.FILES.get('unliquidated')
		db.fi_retirement = request.FILES.get('retirement')
		db.fi_undertaking = request.FILES.get('undertaking')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/t_fi.html', query)

def ltfi(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all()
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "FAT/Inspection"
		db.travel_sector = request.POST.get('travel_sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Official"
		db.support_category = "FAT/Inspection"
		db.travel_sector = request.POST.get('travel_sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6

		
		
		db.requestor = request.user
		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/ltfi.html', query)

def tpt(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'sec': travel_sector.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Personal"
		db.support_category = "Personal Travel"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3


		db.pt_icd = request.FILES.get('icd')
		db.pt_no_pending_task = request.FILES.get('task')
		db.pt_no_admin_case = request.FILES.get('case')
		db.pt_service_record = request.FILES.get('service')
		db.pt_leave_application = request.FILES.get('leave')
		db.pt_clearance = request.FILES.get('clearance')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		db.requestor = request.user

		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Personal"
		db.support_category = "Personal Travel"
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6
		db.pt_icd = request.FILES.get('icd')
		db.pt_no_pending_task = request.FILES.get('task')
		db.pt_no_admin_case = request.FILES.get('case')
		db.pt_service_record = request.FILES.get('service')
		db.pt_leave_application = request.FILES.get('leave')
		db.pt_clearance = request.FILES.get('clearance')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user

		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/t_pt.html', query)

def ltpt(request):
	query = {
		'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'of': travel_office.objects.all(),
	}

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Personal"
		db.support_category = "Non-Training Related"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 3

		db.nt_invitation = request.FILES.get('invitation')
		db.nt_transportation = request.FILES.get('transportation')
		db.nt_allowance = request.FILES.get('allowance')
		db.nt_others = request.FILES.get('others')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')
		
		db.requestor = request.user

		if request.POST['wge']:
			db.nt_without_gov_expense = request.POST.get('wge')

		db.save()
		
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category_id = request.POST.get('rc')
		db.sub_category = "Personal"
		db.support_category = "Non-Training Related"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status_id = 6
		
		db.nt_invitation = request.FILES.get('invitation')
		db.nt_transportation = request.FILES.get('transportation')
		db.nt_allowance = request.FILES.get('allowance')
		db.nt_others = request.FILES.get('others')
		db.additional_requirement_1 = request.FILES.get('a1')
		db.additional_requirement_2 = request.FILES.get('a2')

		db.requestor = request.user

		if request.POST.get('wge'):
			db.nt_without_gov_expense = request.POST.get('wge')

		db.save()
		
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/ltpt.html', query)

def tf(request, tag=0):
	query = {}
	query['tag'] = tag
	query['fs'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	return render(request, 'travelauth/tf.html', query)

def main_dash(request):
	query = {}
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	return render(request, 'travelauth/main_dash.html', query)

def view(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	return render(request, 'travelauth/view.html', query)

def cancel(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST": 
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.status_id = 2
		upd.cancel_mess = request.POST.get('reason')
		upd.cancel_file = request.FILES.get('cancel_file')
		upd.save()
		return HttpResponseRedirect('/requestor/t_r')
	return render(request, 'travelauth/cancel.html', query)

def followup(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST":
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.followup = request.POST.get('followup')
		upd.save()
		return HttpResponseRedirect('/requestor/t_r')
	return render(request, 'travelauth/followup.html', query)

def edit(request, tag = 0):
	query = {}
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['tag'] = tag
	query['iden'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl.objects.get(travelreq_id = tag)
		db.sector_id = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.save()

	return render(request, 'travelauth/edit.html', query)

def edit_non_training(request, tag = 0):
	query = {}
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['tag'] = tag
	query['iden'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'draft' in request.POST:
		db = TravelRequest_tbl()
		db.request_category = "Local"
		db.sub_category = "Personal"
		db.support_category = "Non-Training Related"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status = 0

		
		db.requestor = request.user

		db.save()
		return HttpResponseRedirect('/')

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl()
		db.request_category = "Local"
		db.sub_category = "Personal"
		db.support_category = "Non-Training Related"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.status = 1

		

		db.requestor = request.user

		db.save()
		return HttpResponseRedirect('/')
	return render(request, 'travelauth/edit_non_training.html', query)

def history(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['hdata'] = History_tbl.objects.filter(travelreq_id = tag)

	return render(request, 'travelauth/history.html', query)

#meetings

def mceditendorsement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_endorsement = request.FILES.get('endorsement')
		upd.save()
		
		
	return render(request, 'travelauth/mceditendorsement.html', query)

def mcediticd(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_icd = request.FILES.get('icd')
		upd.save()

	return render(request, 'travelauth/mcediticd.html', query)

def mceditinvitation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_invitation = request.FILES.get('invitation')
		upd.save()

	return render(request, 'travelauth/mceditinvitation.html', query)

def mcedittask(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_no_pending_task = request.FILES.get('task')
		upd.save()

	return render(request, 'travelauth/mcedittask.html', query)

def mceditcase(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_no_admin_case = request.FILES.get('case')
		upd.save()

	return render(request, 'travelauth/mceditcase.html', query)

def mceditservice(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_service_record = request.FILES.get('service')
		upd.save()

	return render(request, 'travelauth/mceditservice.html', query)

def mceditfunds(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_funds = request.FILES.get('funds')
		upd.save()

	return render(request, 'travelauth/mceditfunds.html', query)

def mceditexpenses(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_expenses = request.FILES.get('expenses')
		upd.save()

	return render(request, 'travelauth/mceditexpenses.html', query)

def mceditunliquidated(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_unliquidated = request.FILES.get('unliquidated')
		upd.save()

	return render(request, 'travelauth/mceditunliquidated.html', query)

def mceditretirement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_retirement = request.FILES.get('retirement')
		upd.save()

	return render(request, 'travelauth/mceditretirement.html', query)

def mceditundertaking(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.mc_undertaking = request.FILES.get('undertaking')
		upd.save()

	return render(request, 'travelauth/mceditundertaking.html', query)

#IC
def iceditendorsement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_endorsement = request.FILES.get('endorsement')
		upd.save()
		
		
	return render(request, 'travelauth/iceditendorsement.html', query)

def icediticd(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_icd = request.FILES.get('icd')
		upd.save()

	return render(request, 'travelauth/icediticd.html', query)

def iceditinvitation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_invitation = request.FILES.get('invitation')
		upd.save()

	return render(request, 'travelauth/iceditinvitation.html', query)

def icedittask(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_no_pending_task = request.FILES.get('task')
		upd.save()

	return render(request, 'travelauth/icedittask.html', query)

def iceditcase(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_no_admin_case = request.FILES.get('case')
		upd.save()

	return render(request, 'travelauth/iceditcase.html', query)

def iceditservice(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_service_record = request.FILES.get('service')
		upd.save()

	return render(request, 'travelauth/iceditservice.html', query)

def iceditfunds(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_funds = request.FILES.get('funds')
		upd.save()

	return render(request, 'travelauth/iceditfunds.html', query)

def iceditexpenses(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_expenses = request.FILES.get('expenses')
		upd.save()

	return render(request, 'travelauth/iceditexpenses.html', query)

def iceditunliquidated(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_unliquidated = request.FILES.get('unliquidated')
		upd.save()

	return render(request, 'travelauth/iceditunliquidated.html', query)

def iceditretirement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_retirement = request.FILES.get('retirement')
		upd.save()

	return render(request, 'travelauth/iceditretirement.html', query)

def iceditundertaking(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ic_undertaking = request.FILES.get('undertaking')
		upd.save()

	return render(request, 'travelauth/iceditundertaking.html', query)

#trainings

def tseditendorsement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_endorsement = request.FILES.get('endorsement')
		upd.save()
		
		
	return render(request, 'travelauth/tseditendorsement.html', query)

def tsediticd(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_icd = request.FILES.get('icd')
		upd.save()

	return render(request, 'travelauth/tsediticd.html', query)

def tseditinvitation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_invitation = request.FILES.get('invitation')
		upd.save()

	return render(request, 'travelauth/tseditinvitation.html', query)

def tseditacceptance(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_acceptance = request.FILES.get('acceptance')
		upd.save()

	return render(request, 'travelauth/tseditacceptance.html', query)

def tseditminutes(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_minutes = request.FILES.get('minutes')
		upd.save()

	return render(request, 'travelauth/tseditminutes.html', query)

def tseditscholarship(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_scholarship = request.FILES.get('scholarship')
		upd.save()

	return render(request, 'travelauth/tseditscholarship.html', query)


def tsedittask(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_no_pending_task = request.FILES.get('task')
		upd.save()

	return render(request, 'travelauth/tsedittask.html', query)

def tseditcase(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_no_admin_case = request.FILES.get('case')
		upd.save()

	return render(request, 'travelauth/tseditcase.html', query)

def tseditservice(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_service_record = request.FILES.get('service')
		upd.save()

	return render(request, 'travelauth/tseditservice.html', query)

def tseditfunds(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_funds = request.FILES.get('funds')
		upd.save()

	return render(request, 'travelauth/tseditfunds.html', query)

def tseditexpenses(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_expenses = request.FILES.get('expenses')
		upd.save()

	return render(request, 'travelauth/tseditexpenses.html', query)

def tseditunliquidated(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_unliquidated = request.FILES.get('unliquidated')
		upd.save()

	return render(request, 'travelauth/tseditunliquidated.html', query)

def tseditretirement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_retirement = request.FILES.get('retirement')
		upd.save()

	return render(request, 'travelauth/tseditretirement.html', query)

def tseditundertaking(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.ts_undertaking = request.FILES.get('undertaking')
		upd.save()

	return render(request, 'travelauth/tseditundertaking.html', query)

#FAT

def fieditendorsement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_endorsement = request.FILES.get('endorsement')
		upd.save()
		
		
	return render(request, 'travelauth/fieditendorsement.html', query)

def fiediticd(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_icd = request.FILES.get('icd')
		upd.save()

	return render(request, 'travelauth/fiediticd.html', query)

def fieditinvitation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_invitation = request.FILES.get('invitation')
		upd.save()

	return render(request, 'travelauth/fieditinvitation.html', query)

def fieditagreement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_agreement = request.FILES.get('agreement')
		upd.save()

	return render(request, 'travelauth/fieditiagreement.html', query)


def fiedittask(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_no_pending_task = request.FILES.get('task')
		upd.save()

	return render(request, 'travelauth/fiedittask.html', query)

def fieditcase(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_no_admin_case = request.FILES.get('case')
		upd.save()

	return render(request, 'travelauth/fieditcase.html', query)

def fieditservice(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_service_record = request.FILES.get('service')
		upd.save()

	return render(request, 'travelauth/fieditservice.html', query)

def fieditfunds(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_funds = request.FILES.get('funds')
		upd.save()

	return render(request, 'travelauth/fieditfunds.html', query)

def fieditexpenses(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_expenses = request.FILES.get('expenses')
		upd.save()

	return render(request, 'travelauth/fieditexpenses.html', query)

def fieditunliquidated(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_unliquidated = request.FILES.get('unliquidated')
		upd.save()

	return render(request, 'travelauth/fieditunliquidated.html', query)

def fieditretirement(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_retirement = request.FILES.get('retirement')
		upd.save()

	return render(request, 'travelauth/fieditretirement.html', query)

def fieditundertaking(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.fi_undertaking = request.FILES.get('undertaking')
		upd.save()

	return render(request, 'travelauth/fieditundertaking.html', query)

#PT

def ptediticd(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_icd = request.FILES.get('icd')
		upd.save()

	return render(request, 'travelauth/ptediticd.html', query)

def ptedittask(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_no_pending_task = request.FILES.get('task')
		upd.save()

	return render(request, 'travelauth/ptedittask.html', query)

def pteditcase(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_no_admin_case = request.FILES.get('case')
		upd.save()

	return render(request, 'travelauth/pteditcase.html', query)

def pteditservice(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_service_record = request.FILES.get('service')
		upd.save()

	return render(request, 'travelauth/pteditservice.html', query)

def pteditleave(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_leave_application= request.FILES.get('leave')
		upd.save()

	return render(request, 'travelauth/pteditleave.html', query)

def pteditclearance(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.pt_clearance= request.FILES.get('clearance')
		upd.save()

	return render(request, 'travelauth/pteditclearance.html', query)

def a1edit(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_1 = request.FILES.get('a1')
		upd.save()

	return render(request, 'travelauth/a1edit.html', query)

def a2edit(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_2 = request.FILES.get('a2')
		upd.save()

	return render(request, 'travelauth/a2edit.html', query)

def edit_training(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl.objects.get(travelreq_id = tag)
		db.destination = request.POST.get('destination')
		db.sub_category = "Official"
		db.support_category = "Training-Related Travel Request"
		db.sector = request.POST.get('sector')
		db.program_title = request.POST.get('program_title')
		db.name_title = request.POST.get('name_title')
		db.t_report = request.FILES.get('report')
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.nickname = request.POST.get('nname')
		db.salary_grade = request.POST.get('sg')
		db.email_address = request.POST.get('email')
		db.mobile_number = request.POST.get('mobile')
		db.age = request.POST.get('age')
		db.office_number = request.POST.get('office_number')
		db.address = request.POST.get('address')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.t_pre_registration = request.FILES.get('preg')
		db.t_pds = request.FILES.get('pds')
		db.t_ipcr = request.FILES.get('ipcr')
		db.t_paf = request.FILES.get('paf')
		db.requestor = request.user
		db.save()
		
	return render(request, 'travelauth/edit_training.html', query)
	
def editreport(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.t_report= request.FILES.get('report')
		upd.save()

	return render(request, 'travelauth/editreport.html', query)

def editpds(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.t_pds= request.FILES.get('pds')
		upd.save()

	return render(request, 'travelauth/editpds.html', query)

def editpaf(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.t_paf= request.FILES.get('paf')
		upd.save()

	return render(request, 'travelauth/editpaf.html', query)

def editipcr(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.t_ipcr= request.FILES.get('ipcr')
		upd.save()

	return render(request, 'travelauth/editipcr.html', query)

def editpreregistration(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.t_pre_registration= request.FILES.get('preg')
		upd.save()

	return render(request, 'travelauth/editpreregistration.html', query)

def edit_ntraining(request, tag = 0):
	query = {
		'user': User.objects.filter(username = request.user),
        	'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'rc': request_category.objects.all(),
		'of': travel_office.objects.all(),
		'rdata': TravelRequest_tbl.objects.filter(travelreq_id = tag),
	}

	if request.method == "POST" and 'save' in request.POST:
		db = TravelRequest_tbl.objects.get(travelreq_id = tag)
		db.program_title = request.POST.get('program_title')
		db.last_name = request.POST.get('lname')
		db.first_name = request.POST.get('fname')
		db.middle_initial = request.POST.get('mname')
		db.suffix = request.POST.get('suff')
		db.position = request.POST.get('pos')
		db.office = request.POST.get('office')
		db.gender = request.POST.get('gender')
		db.civil_status = request.POST.get('civil_status')
		db.disability = request.POST.get('disability')
		db.ethnicity = request.POST.get('ethnicity')
		db.agency = request.POST.get('agency')
		db.destination = request.POST.get('destination')
		db.programdates_from = request.POST.get('from')
		db.programdates_to = request.POST.get('to')
		db.nt_invitation = request.FILES.get('invitation')
		db.nt_transportation = request.FILES.get('transportation')
		db.nt_allowance = request.FILES.get('allowance')
		db.nt_others = request.FILES.get('others')

		db.requestor = request.user

		db.save()
		
	return render(request, 'travelauth/edit_ntraining.html', query)

def nteinvitation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.nt_invitation= request.FILES.get('invitation')
		upd.save()

	return render(request, 'travelauth/nteinvitation.html', query)

def ntetransportation(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.nt_transportation= request.FILES.get('transportation')
		upd.save()

	return render(request, 'travelauth/ntetransportation.html', query)

def nteallowance(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.nt_allowance= request.FILES.get('allowance')
		upd.save()

	return render(request, 'travelauth/nteallowance.html', query)

def nteothers(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	
	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.nt_others= request.FILES.get('others')
		upd.save()

	return render(request, 'travelauth/nteothers.html', query)

def fup(request, tag = 0, assigned = "", ref = "", fn = "", mi = "", ln = "", pt = "", frm = "", to = "", dest = "", st = ""):
	query = {}
	query['tag'] = tag
	query['fn'] = fn
	query['mi'] = mi
	query['ln'] = ln
	query['pt'] = pt
	query['frm'] = frm
	query['to'] = to
	query['st'] = st
	query['dest'] = dest
	query['assigned'] = assigned
	query['ref'] = ref
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
	upd.followup = True
	upd.save()

	subject = 'Followup on Request'
	recepient = assigned
	greet = "Hi! \nThis email is to followup on a Travel Application assigned to "+assigned+".\n"
	tbl = "\nAPPLICATION DETAILS\n \nApplication Reference Number: "+ref+"\nApplicant Name: "+fn+" "+mi+". "+ln+" \nProgram Title: "+pt+" \nInclusive Dates: "+frm+" to "+to+" \nVenue:"+dest+"\nCurrent Status: "+st
	message = greet+tbl
	send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

	
	return redirect('/requestor/t_r')

def travel_report(request):
	query = {}
	query['user'] = User.objects.filter(username = request.user)
	query['pending'] = Pending_training_report.objects.all()
	query['designation'] =  Author.objects.filter(user = request.user)

	return render(request, 'travelauth/travel_report.html', query)

def edita1(request, tag = 0):

	query = {
		'tag': tag
	}
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_1 = request.FILES.get('a1')
		upd.save()

	return render(request, 'travelauth/edita1.html', query)

def edita2(request, tag = 0):

	query = {
		'tag': tag
	}
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_2 = request.FILES.get('a2')
		upd.save()

	return render(request, 'travelauth/edita2.html', query)

def ntedita1(request, tag = 0):

	query = {
		'tag': tag
	}
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_1 = request.FILES.get('a1')
		upd.save()

	return render(request, 'travelauth/ntedita1.html', query)

def ntedita2(request, tag = 0):

	query = {
		'tag': tag
	}
	query['rdata'] = TravelRequest_tbl.objects.filter(travelreq_id = tag)
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)

	if request.method == "POST" and 'edit' in request.POST:
		upd = TravelRequest_tbl.objects.get(travelreq_id = tag)
		upd.additional_requirement_2 = request.FILES.get('a2')
		upd.save()

	return render(request, 'travelauth/ntedita2.html', query)
























