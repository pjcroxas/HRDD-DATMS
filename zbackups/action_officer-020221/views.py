from django.shortcuts import render
from login.models import Author
from travelauth.models import TravelRequest_tbl
from django.contrib.auth.models import User
from django.db.models import Q
from requestor.models import *
from travelauth.models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from OTMS.settings import EMAIL_HOST_USER
from .filters import GedsiReport, EthnicityReport, DisabilityReport
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def sector(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
	}
	return render(request, 'action_officer/sector.html', query)


def action_officer(request, pk):

	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'tr': TravelRequest_tbl.objects.all(),
	}
	if pk == 1:
		query['total'] =  TravelRequest_tbl.objects.all().count()
		query['totalmar'] =  TravelRequest_tbl.objects.filter(Q(assigned = request.user)).count()
		query['newsubmissions'] =  TravelRequest_tbl.objects.filter(status__status__exact="New").count()
		query['urlpath'] = "travel"

		page = request.GET.get('page', 1)
		paginator = Paginator(TravelRequest_tbl.objects.all().order_by('-travelreq_id'), 10)

		try:
			query['requestors'] = paginator.page(page)
		except PageNotAnInteger:
			query['requestors'] = paginator.page(1)
		except EmptyPage:
			query['requestors'] = paginator.page(paginator.num_pages)

	else:
		query['total'] =  Requestor.objects.all().count()
		query['totalmar'] =  Requestor.objects.filter(Q(assigned = request.user)).count()
		query['newsubmissionsreq'] =  Requestor.objects.filter(status=4).count()
		query['requestors'] = Requestor.objects.all()
		query['urlpath'] = "scholarl"

		page = request.GET.get('page', 1)
		paginator = Paginator(Requestor.objects.all().order_by('-id'), 10)

		try:
			query['requestors'] = paginator.page(page)
		except PageNotAnInteger:
			query['requestors'] = paginator.page(1)
		except EmptyPage:
			query['requestors'] = paginator.page(paginator.num_pages)
	return render(request, 'action_officer/action_dash.html', query)

def requestdetails(request, pk):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'requestors': get_object_or_404(Requestor, pk=pk),
	}
	query['attachment']= Scholarship_Requirements.objects.filter(requestor=query['requestors']).first()
	return render(request, 'action_officer/reqdetail.html', query)

def requestdetailstravel(request, pk):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'travel': get_object_or_404(TravelRequest_tbl, pk=pk),
	}
	# query['attachment']= Scholarship_Requirements.objects.filter(requestor=query['requestors']).first()
	return render(request, 'action_officer/reqdetailtravel.html', query)

def requestdetails(request, pk):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'requestors': get_object_or_404(Requestor, pk=pk),
	}
	query['attachment']= Scholarship_Requirements.objects.filter(requestor=query['requestors']).first()
	return render(request, 'action_officer/reqdetail.html', query)

def new_sub(request, pk):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'tr': TravelRequest_tbl.objects.filter(status__status__exact="New").order_by('-travelreq_id'),
		'newsubmissions' : Requestor.objects.filter(status__status__exact="New")
	}
	if pk == 1: #travel if#
		query['urlpath'] = "travel"
		page = request.GET.get('page', 1)
		paginator = Paginator(TravelRequest_tbl.objects.filter(status__status__exact="New"), 10)

		try:
			query['requestor'] = paginator.page(page)
		except PageNotAnInteger:
			query['requestor'] = paginator.page(1)
		except EmptyPage:
			query['requestor'] = paginator.page(paginator.num_pages)

	else: # requestor if#
		query['requestor'] = Requestor.objects.filter(status__status__exact="New")
		query['urlpath'] = "Scholar"
	return render(request, 'action_officer/new_sub.html', query)

def take(request, tag=0, cat = "", date = "", ln="", fn="", mi= "", pt = "", frm = "", to = "", ds = "", tid = "", last = "", email=""):

	obj1 = get_object_or_404(TravelRequest_tbl, travelreq_id = tag)
	obj1.assigned = request.user
	obj1.status = Status.objects.get(status__exact="For Evaluation")
	obj1.save()
	args = {}
	args['last'] = last
	args['tag'] = tag
	args['cat'] = cat
	args['date'] = date
	args['ln'] = ln
	args['fn'] = fn
	args['mi'] = mi
	args['pt'] = pt
	args['frm'] = frm
	args['to'] = to
	args['ds'] = ds
	args['tid'] = tid
	args['email'] = email
	args['query'] = Requestor.objects.filter(id = tag).update(req_action = 1)
	args['user']= User.objects.filter(username = request.user),
	args['designation']= Author.objects.filter(user = request.user),
	args['pk'] = 1

	his = History_tbl()
	his.a_officer = request.user
	his.travelreq_id = tag
	his.status = "Submitted"
	his.save()

	subject = 'Application for Travel Request'

	recepient = email
	greet = "Hi, \nThis is to acknowledge receipt of your request for a Travel Authority (TA) and now being reviewed by our Action Officer in the Human Resource Development Division.\n \nPlease note that you still need to submit the HRDD the approved original documents \n     \nrelative to this request. Thus, approved TA shall be put on hold until you have submitted all the original documents.\n    \nTo view your application status, visit DOTMS.  \n    \n-HRD Training Team\n    \n"
	tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+date+"-"+tid+" \nApplication Date: "+date+"\nApplicant Name: "+fn+" "+mi+". "+ln+" \nCourse Title: "+pt+" \nInclusive Dates: "+frm+" to "+to+"\nVenue: "+ds+"\n"
	message = greet+tbl
	send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
	print(recepient)
	return render(request, 'action_officer/sample.html', args)

def taketravel(request, tag=""):
	pending = Status.objects.get(status__exact="For Evaluation")
	obj = get_object_or_404(TravelRequest_tbl, travelreq_id = tag)
	obj.assigned = request.user
	obj.status = pending
	obj.save()
	args = {}
	args['tag'] = tag
	args['user']= User.objects.filter(username = request.user),
	args['designation']= Author.objects.filter(user = request.user),
	args['pk'] = 1
	return render(request, 'action_officer/sample.html', args)

def updatedetails(request, pk):
	update = get_object_or_404(Requestor, pk=pk)
	if request.method == "POST":
		form = UpdateForm(request.POST, instance= update)
		if form.is_valid():
			form.save()
			return redirect('updatedetails', pk=update.pk)

	else:
		form = UpdateForm(instance=update)

	query = {
		'form':form,
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'requestors': get_object_or_404(Requestor, pk=pk),
	}
	query['attachment']= Scholarship_Requirements.objects.filter(requestor=query['requestors']).first()
	return render(request, 'action_officer/updatedetails.html', query)


def updatedetailstravel(request, pk):
	update = get_object_or_404(TravelRequest_tbl, pk=pk)
	approved = Status.objects.get(id=13)
	onhold = Status.objects.get(id=14)
	incomplete = Status.objects.get(id=9)
	dateprint = update.date_filed
	datefrom = update.programdates_from
	dateto = update.programdates_to
	print(dateprint)

	data = TravelRequest_tbl.objects.values_list('lacking_documents',flat=True).get(pk=pk)
	if request.method == "POST":
		form = UpdateFormTravel(request.POST, request.FILES, instance=update)
		if form.is_valid():
			recepient = update.requestor.email
			sform = form.save(commit=False)
			sform.with_issues = sform.with_issues.split(',')
			sform.unsigned_docs = sform.unsigned_docs.split(',')
			sform.wrong_attachment = sform.wrong_attachment.split(',')
			if sform.status ==  approved:
			   history = History_tbl(status = sform.status, a_officer = request.user.get_full_name() , travelreq_id = pk)
			   history.save()
			   print("aw")
			   subject = 'TA FOR DOWNLOAD'
			   greet = "Hi, \nWe are pleased to inform you that your request for Travel Authority is already APPROVED in the DOTMS . \n   \nTo check, visit DOTMS and click on DOWNLOAD TA.\n  \nThe hard copy is being mailed to your office today.\n \nSafe Travels.\n \n-HRD Travel Team"
			   tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+dateprint.strftime("%Y-%m-%d")+"-"+str(update.travelreq_id)+" \nApplication Date:"+dateprint.strftime("%Y-%m-%d %H:%M:%S")+"\nApplicant Name: "+update.first_name+" "+update.middle_initial+". "+update.last_name+" \nCourse Title: "+update.program_title+" \nInclusive Dates: "+datefrom+" to "+dateto+"\n Venue: "+update.destination+"\n"
			   message = greet+tbl
			   print(tbl)
			   send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


			if sform.status == onhold:
				 subject = 'PASSED EVALUATION BUT NO ORIGINAL DOCUMENTS'
				 greet = "Hi, "+update.first_name+' '+update.last_name+ " \nWe are pleased to inform you that the request for Travel Authority passed the evaluation and . \n   \nshall be moved to our next process. You will receive and update once the TA has been.\n  \nPlease be reminded to submit original copies of your approved endorsement and other\n \ndocuments relative to this request. Disregard if already submitted. \n \nThan you! \n \n-HRD Travel Team"
				 tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+dateprint.strftime("%Y-%m-%d")+"-"+str(update.travelreq_id)+" \nApplication Date:"+dateprint.strftime("%Y-%m-%d %H:%M:%S")+"\nApplicant Name: "+update.first_name+" "+update.middle_initial+". "+update.last_name+" \nCourse Title: "+update.program_title+" \nInclusive Dates: "+datefrom+" to "+dateto+"\n Venue: "+update.destination+"\n"
				 message = greet+tbl
				 send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
			if sform.status == incomplete:
				 subject = 'LACK DOCUMENTARY REQUIREMENT/ATTACHMENT'
				 greet = "Hi, "+update.first_name+' '+update.last_name+ " \nWe would like to remind you of the pending documents reflected in the DOTr Travel  \nManagement System (DOTMS) that you need to provide so we can proceed with the Travel Authority request process\n  \nKindly visit the DOTMS and attach the requirements within the day.\n \nPlease note that failure to comply within the timeline would mean delay in the process of the TA \n \nThan you! \n \n-HRD Travel Team"
				 tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+dateprint.strftime("%Y-%m-%d")+"-"+str(update.travelreq_id)+" \nApplication Date:"+dateprint.strftime("%Y-%m-%d %H:%M:%S")+"\nApplicant Name: "+update.first_name+" "+update.middle_initial+". "+update.last_name+" \nCourse Title: "+update.program_title+" \nInclusive Dates: "+datefrom+" to "+dateto+"\n Venue: "+update.destination+"\n"

				 message = greet+tbl
				 send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

			if sform.status != approved:
			   sform.ta_signed_upload = None
			   history = History_tbl(status = sform.status, a_officer = request.user.get_full_name() , travelreq_id = pk)
			   history.save()
			   print("anyare")

			if sform.status == onhold:
				 subject = 'PASSED EVALUATION BUT NO ORIGINAL DOCUMENTS'
				 greet = "Hi, "+update.first_name+' '+update.last_name+ " \nWe are pleased to inform you that the request for Travel Authority passed the evaluation and . \n   \nshall be moved to our next process. You will receive and update once the TA has been.\n  \nPlease be reminded to submit original copies of your approved endorsement and other\n \ndocuments relative to this request. Disregard if already submitted. \n \nThan you! \n \n-HRD Travel Team"
				 tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+dateprint.strftime("%Y-%m-%d")+"-"+str(update.travelreq_id)+" \nApplication Date:"+dateprint.strftime("%Y-%m-%d %H:%M:%S")+"\nApplicant Name: "+update.first_name+" "+update.middle_initial+". "+update.last_name+" \nCourse Title: "+update.program_title+" \nInclusive Dates: "+datefrom+" to "+dateto+"\n Venue: "+update.destination+"\n"
				 message = greet+tbl
				 send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


			if sform.status == Status.objects.get(id=18): #other issues
				 history = History_tbl(status = sform.status, a_officer = request.user.get_full_name() , travelreq_id = pk)
				 subject = 'OTHER ISSUES'
				 # greet = "Hi, "+update.first_name+' '+update.last_name+ " \nWe would like to inform you that upon evaluation of the requested travel (see request details below), there are discrepancies with the attached documents. \n Kindly settle the following document/s and attach within the day: --- "+(','.join(sform.with_issues))+" --- \n Please note that failure to comply within the timeline  would mean a delay in the processing of TA \n \n Thank you! \n HRDD Travel Team "
				 # tbl = "APPLICATION DETAILS\n \nApplication Reference Number: TR-"+dateprint.strftime("%Y-%m-%d")+"-"+str(update.travelreq_id)+" \nApplication Date:"+dateprint.strftime("%Y-%m-%d %H:%M:%S")+"\nApplicant Name: "+update.first_name+" "+update.middle_initial+". "+update.last_name+" \nCourse Title: "+update.program_title+" \nInclusive Dates: "+datefrom+" to "+dateto+"\n Venue: "+update.destination+"\n"
				 # message = greet+tbl
				 ctx = {
        				'with_issues': update,
    			}
				 html_message = render_to_string('action_officer/email_template/with_issues.html', ctx)
				 plain_message = strip_tags(html_message)
				 send_mail(subject, plain_message, EMAIL_HOST_USER, [recepient], html_message=html_message,  fail_silently = False)


			if sform.status == Status.objects.get(id=11): #unsigned_docs
				 history = History_tbl(status = sform.status, a_officer = request.user.get_full_name() , travelreq_id = pk)
				 subject = 'UNSIGNED DOCUMENTS'
				 ctx = {
        				'unsigned_docs': update,
    			}
				 html_message = render_to_string('action_officer/email_template/unsigned_docs.html', ctx)
				 plain_message = strip_tags(html_message)
				 send_mail(subject, plain_message, EMAIL_HOST_USER, [recepient], html_message=html_message,  fail_silently = False)
				 print(html_message)

			if sform.status == Status.objects.get(id=19): #wrong_attachment
				 history = History_tbl(status = sform.status, a_officer = request.user.get_full_name() , travelreq_id = pk)
				 subject = 'WRONG REQUIREMENT/ATTACHMENT'
				 ctx = {
        				'wrong_attachment': update,
    			}
				 html_message = render_to_string('action_officer/email_template/wrong_attachment.html', ctx)
				 plain_message = strip_tags(html_message)
				 send_mail(subject, plain_message, EMAIL_HOST_USER, [recepient], html_message=html_message,  fail_silently = False)
				 print(html_message)

			sform.save()
			return redirect('updatedetailstravel', pk=update.pk)

	else:
		if data is None:
			form = UpdateFormTravel(instance=update)
		else:
			form = UpdateFormTravel(instance=update, initial={'lacking_documents': list(data)})

	query = {
		'form':form,
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'travel': get_object_or_404(TravelRequest_tbl, pk=pk),

		'display_lack': data,

	}
	# query['attachment']= Scholarship_Requirements.objects.filter(requestor=query['requestors']).first()
	return render(request, 'action_officer/updatedetailstravel.html', query)


def assigned(request, pk):
	query = {
		'mar': Requestor.objects.filter(assigned = request.user),
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
	}
	if pk == 1:
		query['urlpath'] = "Travel"
		page = request.GET.get('page', 1)
		paginator = Paginator(TravelRequest_tbl.objects.filter(assigned = request.user).order_by('-travelreq_id'), 10)

		try:
			query['martr'] = paginator.page(page)
		except PageNotAnInteger:
			query['martr'] = paginator.page(1)
		except EmptyPage:
			query['martr'] = paginator.page(paginator.num_pages)
	return render(request, 'action_officer/assigned.html', query)



@login_required
def officersindex(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
	}
	query['officers'] = User.objects.all()
	query['officers2'] = Author.objects.all()
	return render(request, 'action_officer/officers/index.html', query)


def officers_edit(request, pk):
	user = get_object_or_404(User, pk=pk)
	user2 = Author.objects.get(user_id = pk)
	if request.method == "POST":
		user_form = EditUserForm(request.POST, instance = user)
		author_form = AuthorForm(request.POST, instance = user2)
		if user_form.is_valid() and author_form.is_valid():
			user_form.save()
			author_form.save()
			return HttpResponseRedirect(reverse('officersindex'))
		else:
			query = {
				'user': User.objects.filter(username = request.user),
				'designation': Author.objects.filter(user = request.user),
				'user_form':user_form,
				'author_form':author_form,

			}
			return render(request, 'action_officer/officers/edit.html', query)

	else:
		user_form = EditUserForm(instance = user)
		author_form = AuthorForm(instance = user2)
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_form':user_form,
		'author_form':author_form,
		'usercpk':user,
		}
	return render(request, 'action_officer/officers/edit.html', query)

@login_required
def change_password(request, pk):
    userc = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = SetPasswordForm(userc, request.POST)
        if form.is_valid():
            saveuser = form.save()
            update_session_auth_hash(request, request.user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password', pk= pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'action_officer/officers/change_password.html', {
        'form': form,
		'designation': Author.objects.filter(user = request.user),
		'user': User.objects.filter(username = request.user),
    })


def officers_add(request):
	if request.method == "POST":
		user_form = UserForm(request.POST)
		author_form = AuthorForm(request.POST)
		if user_form.is_valid() and author_form.is_valid():
			user = user_form.save()
			author = author_form.save(commit=False)
			author.user = user
			author.save()
			return HttpResponseRedirect(reverse('officersindex'))
		else:
			query = {
				'user': User.objects.filter(username = request.user),
				'designation': Author.objects.filter(user = request.user),
				'user_form':user_form,
				'author_form':author_form,
			}
			return render(request, 'action_officer/officers/add.html', query)

	else:
		user_form = UserForm()
		author_form = AuthorForm()
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_form':user_form,
		'author_form':author_form,
		}
	return render(request, 'action_officer/officers/add.html', query)


def block(request, pk):
	user = get_object_or_404(User, pk=pk)
	user.is_active = False
	user.save()
	return HttpResponseRedirect(reverse('officersindex'))

def unblock(request, pk):
	user = get_object_or_404(User, pk=pk)
	user.is_active = True
	user.save()
	return HttpResponseRedirect(reverse('officersindex'))



def dtravelforeign(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'travelforeign': TravelRequest_tbl.objects.filter(request_category__request_category="Foreign"),
	}
	return render(request, 'action_officer/Database/dtravelforeign.html', query	)

def dtravellocal(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'travelforeign': TravelRequest_tbl.objects.filter(request_category__request_category="Local"),
	}
	return render(request, 'action_officer/Database/dtravellocal.html', query)

def save_travel_form(request, form, template_name, travelid):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            if travelid == 1:
            	travelforeign = TravelRequest_tbl.objects.filter(request_category="Foreign")
            	data['html_book_list'] = render_to_string('action_officer/Database/travel_list.html', {
                	'travelforeign': travelforeign
            	})
            if travelid == 2:
                travelforeign = TravelRequest_tbl.objects.filter(request_category="Local")
                data['html_book_list'] = render_to_string('action_officer/Database/travel_list_local.html', {
                    'travelforeign': travelforeign
            	})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def dtravelupdateforeign(request, pk):
	user2 = TravelRequest_tbl.objects.get(travelreq_id = pk)
	if request.method == 'POST':
		form = DatabaseTravelUpdateForm(request.POST, instance=user2)
	else:
		form = DatabaseTravelUpdateForm(instance=user2)
	return save_travel_form(request, form, 'action_officer/Database/travelupdateform.html', 1)



def dtravelupdatelocal(request, pk):
	user2 = TravelRequest_tbl.objects.get(travelreq_id = pk)
	if request.method == 'POST':
		form = DatabaseTravelLocalUpdateForm(request.POST, instance=user2)
	else:
		form = DatabaseTravelLocalUpdateForm(instance=user2)
	return save_travel_form(request, form, 'action_officer/Database/travelupdatelocalform.html', 2)


def dscholarship(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'dscholarship': Requestor.objects.all(),
	}
	return render(request, 'action_officer/Database/scholarship.html', query)




def save_scholarship_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True


        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def dupdatescholarship(request, pk):
	user2 = Requestor.objects.get(id = pk)
	if request.method == 'POST':
		form = ScholarshipUpdateForm(request.POST, instance=user2)
	else:
		form = ScholarshipUpdateForm(instance=user2)
	return save_scholarship_form(request, form, 'action_officer/Database/scholarshipupdateform.html')



def travel_request_stat(request):
	total_request = TravelRequest_tbl.objects.all().count()
	total_users = User.objects.filter(is_superuser=0).count()
	travel_request_per_day = TravelRequest_tbl.objects \
        .values('date_filed__date') \
        .annotate(local=Count('date_filed', filter=Q(request_category_id=1)),
                  foreign=Count('date_filed', filter=Q(request_category_id=2)))


	travel_request_per_office = TravelRequest_tbl.objects.filter(agency='DOTr-CO').values('office')\
	                     .annotate(Count('travelreq_id')).order_by('office')

	travel_request_per_agency = TravelRequest_tbl.objects.values('agency')\
	                     .annotate(Count('travelreq_id')).order_by('agency')

	travel_request_per_type = TravelRequest_tbl.objects.values('sub_category')\
	                     .annotate(Count('travelreq_id')).order_by('sub_category')

	travel_request_per_nature = TravelRequest_tbl.objects.values('support_category')\
	                     .annotate(Count('travelreq_id')).order_by('support_category')


	# request_per_age = Requestor.objects.values('age')\
	#                      .annotate(Count('id')).order_by('age')
	#
	# request_per_sector = TravelRequest_tbl.objects.values("sector__sector").annotate(
    #     local_count=Count('sector', filter = Q(request_category=1)),
	# 	foreign_count=Count('sector', filter = Q(request_category=2))).order_by('sector')
	#
	# request_per_status = TravelRequest_tbl.objects.values("status__status").annotate(
    #     local_count=Count('status', filter = Q(request_category=1)),
	# 	foreign_count=Count('status', filter = Q(request_category=2))).order_by('status')

	# request_per_status = TravelRequest_tbl.objects.values("status__status").annotate(Count("status")).order_by("status__id")



	context = {
			'total_request':total_request,
			'total_users':total_users,


			'travel_request_per_day': travel_request_per_day,
			'travel_request_per_office': travel_request_per_office,
			'travel_request_per_agency':travel_request_per_agency,
			'travel_request_per_type':travel_request_per_type,
			'travel_request_per_nature':travel_request_per_nature,

			# 'request_per_age':request_per_age,
			# 'request_per_sector':request_per_sector,
			# 'request_per_status':request_per_status,
			'user': User.objects.filter(username = request.user),
			'designation': Author.objects.filter(user = request.user),
	}
	return render(request, 'action_officer/graphical_reports.html', context)

def disability_search(request):
	disability_list = TravelRequest_tbl.objects.all()
	dis_filter = DisabilityReport(request.GET, queryset=disability_list)
	# dis_count = dis_filter.count()

	context = {
		# 'dis_count':dis_count,
		'filter':dis_filter,
		'user': 	User.objects.filter(username = request.user),
		'designation': 		Author.objects.filter(user = request.user)

	}
	return render(request, 'action_officer/disability_list.html', context)


def ethnicity_search(request):
	eth_list = TravelRequest_tbl.objects.all()
	eth_filter = EthnicityReport(request.GET, queryset=eth_list)

	context = {

		'filter':	eth_filter,
		'user': 	User.objects.filter(username = request.user),
		'designation': 		Author.objects.filter(user = request.user)
	}

	return render(request, 'action_officer/ethnicity_list.html', context)


def gedsi_search(request):
    gedsi_list = TravelRequest_tbl.objects.all().order_by("-travelreq_id")
    gedsi_filter = GedsiReport(request.GET, queryset=gedsi_list)

    context = {

        'filter':	gedsi_filter,
		'user': 	User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
    }
    return render(request, 'action_officer/gedsi_list.html', context)
