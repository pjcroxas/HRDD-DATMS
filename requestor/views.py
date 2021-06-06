from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import (Requestor,
                     Category,
                     SupportCategory,
                     SubCategory,
                     Sector,
                     RequestorLog,
                     SectorForScholarship,
                     Nomination_Form)
from login.models import Author
from django.contrib.auth.models import User
from travelauth.models import TravelRequest_tbl, History_tbl, Pending_training_report
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (NewRequestForm,
                    NominationForm,
                    EligibilityStatusForm,
                    ScholarshipRequirementsForm,
                    TermsConditionForm,
                    GedsiForm,
		                PreSelectionForm)
from django.core.mail import send_mail
from OTMS.settings import EMAIL_HOST_USER
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime 

def request_site(request):
    requestors = Requestor.objects.filter(user=request.user).exclude(status=25).order_by("-id")
    #requestors = Requestor.objects.all().order_by("-id")

    user = User.objects.filter(username = request.user)
    author = Author.objects.filter(user = request.user)
    reqtravel = TravelRequest_tbl.objects.filter(requestor = request.user).order_by('-travelreq_id')
    mark_number = 1


    page = request.GET.get('page', 1)
    paginator = Paginator(requestors, 5)

    try:
        scholarship_request = paginator.page(page)
    except PageNotAnInteger:
        scholarship_request = paginator.page(1)
    except EmptyPage:
        scholarship_request = paginator.page(paginator.num_pages)

    context = {
        'mark': mark_number,
        'scholarship_request':scholarship_request,
        'requestors':requestors,
        'user': user,
        'designation': author,
        'reqtravel' : reqtravel,
    }
    return render(request, 'request_page.html', context)

def history(request, tag = 0):
	query = {}
	query['tag'] = tag
	query['user'] = User.objects.filter(username = request.user)
	query['designation'] =  Author.objects.filter(user = request.user)
	query['rdata'] = Requestor.objects.filter(id = tag)
	query['hdata'] = History_tbl.objects.filter(scholar_id = tag)

	return render(request, 'history.html', query)

def t_r(request):
    reqtravel = TravelRequest_tbl.objects.filter(requestor = request.user).order_by('-travelreq_id')
    author = Author.objects.filter(user = request.user)
    user = User.objects.filter(username = request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(reqtravel, 5)

    try:
        reqtravelrequest = paginator.page(page)
    except PageNotAnInteger:
        reqtravelrequest = paginator.page(1)
    except EmptyPage:
        reqtravelrequest = paginator.page(paginator.num_pages)

    context = {
        'reqtravelrequest': reqtravelrequest,
        'user': user,
        'designation': author,
        'reqtravel' : reqtravel,
 
	}

    return render(request, 'request_page1.html', context)

def request_detail(request, pk):

    query = {
        'requestors' : get_object_or_404(Requestor, pk=pk),
        # 'nominees': get_object_or_404(Nomination_Form, pk=pk),
        'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user)
    }

    return render(request, 'req_detail.html', query)

def preview_page(request, pk):

    query = {
        'requestors' : get_object_or_404(Requestor, pk=pk),
        # 'nominees': get_object_or_404(Nomination_Form, pk=pk),
        'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user)
    }

    return render(request, 'nomination_form.html', query)

# def new_application(request, pk):
#     requestors = get_object_or_404(Requestor, pk=pk)
#     if request.method == 'POST':
#         requestor_form = NewRequestForm(request.POST)
#         nomination_form = NominationForm(request.POST)
#         eligibilitystatus_form = EligibilityStatusForm(request.POST)
#         requirements_form = ScholarshipRequirementsForm(request.POST, request.FILES)
#         termscondition_form = TermsConditionForm(request.POST)
#         gedsi_form = GedsiForm(request.POST)
#
        # if requestor_form.is_valid() or nomination_form.is_valid() or eligibilitystatus_form.is_valid()  or requirements_form.is_valid() or termscondition_form.is_valid() or gedsi_form.is_valid():
#             # Do the needful
            # new_app = requestor_form.save(commit=False)
            # nomination_app = nomination_form.save(commit=False)
            # eligibilitystatus_app = eligibilitystatus_form.save(commit=False)
            # requirements_app = requirements_form.save(commit=False)
            # termscondition_app = termscondition_form.save(commit=False)
            # gedsi_app = gedsi_form.save(commit=False)
            #
            # new_app.save()
            # nomination_app.requestor = new_app
            # eligibilitystatus_app.requestor = new_app
            # requirements_app.requestor = new_app
            # termscondition_app.requestor = new_app
            #
            # nomination_app.gender = gedsi_app.gender
            # nomination_app.age = gedsi_app.age
            # nomination_app.civil_status = gedsi_app.civil_status
            # nomination_app.disability = gedsi_app.disability
            # nomination_app.ethnicity = gedsi_app.ethnicity
            # nomination_app.duties = gedsi_app.duties
            #
            #
            # nomination_app.save()
            # eligibilitystatus_app.save()
            # requirements_app.save()
            # termscondition_app.save()
            # # gedsi_app.save()
            # new_log = RequestorLog(change_msg = "filed a new request")
            # new_log.save()
#             return HttpResponseRedirect(reverse('request_page'))
#     else:
#         requestor_form = NewRequestForm()
#         nomination_form = NominationForm()
#         eligibilitystatus_form = EligibilityStatusForm()
#         requirements_form = ScholarshipRequirementsForm()
#         termscondition_form = TermsConditionForm()
#         gedsi_form = GedsiForm()
#
#
    # return render(request,'scholarship_app.html', {
    #     'requestors': requestors,
    #     'requestor_form': requestor_form,
    #     'nomination_form': nomination_form,
    #     'eligibilitystatus_form': eligibilitystatus_form,
    #     'requirements_form':requirements_form,
    #     'termscondition_form' : termscondition_form,
    #     'gedsi_form':gedsi_form,
    #     'user': User.objects.filter(username = request.user),
    #     'designation': Author.objects.filter(user = request.user),
    # })

class new_application(View):
    def post(self, request, pk):
        requestors = get_object_or_404(Requestor, pk=pk)
        requestor_form = NewRequestForm(request.POST, request.FILES)
        nomination_form = NominationForm(request.POST)
        eligibilitystatus_form = EligibilityStatusForm(request.POST)
        requirements_form = ScholarshipRequirementsForm(request.POST, request.FILES)
        termscondition_form = TermsConditionForm(request.POST)
        gedsi_form = GedsiForm(request.POST)
        preselection_form = PreSelectionForm(request.POST, request.FILES)

        if requestor_form.is_valid() or nomination_form.is_valid() or eligibilitystatus_form.is_valid()  or requirements_form.is_valid() or termscondition_form.is_valid() or gedsi_form.is_valid() or preselection_form.is_valid():
            if "_draft" in request.POST:
                new_app = requestor_form.save(commit=False)
                nomination_app = nomination_form.save(commit=False)
                eligibilitystatus_app = eligibilitystatus_form.save(commit=False)
                requirements_app = requirements_form.save(commit=False)
                termscondition_app = termscondition_form.save(commit=False)
                gedsi_app = gedsi_form.save(commit=False)
                preselection_app = preselection_form.save(commit=False)

                nomination_app.requestor = new_app
                eligibilitystatus_app.requestor = new_app
                requirements_app.requestor = new_app
                termscondition_app.requestor = new_app

                ## Nomination Form
                new_app.name_title = nomination_app.name_title
                new_app.last_name = nomination_app.last_name
                new_app.first_name = nomination_app.first_name
                new_app.middle_initial = nomination_app.middle_initial
                new_app.nickname = nomination_app.nickname
                new_app.position = nomination_app.position
                new_app.salary_grade = nomination_app.salary_grade
                new_app.office = nomination_app.office
                new_app.e_mail = nomination_app.e_mail
                new_app.mobile_no = nomination_app.mobile_no
                new_app.office_no = nomination_app.office_no
                new_app.address = nomination_app.address

                ## GEDSI Form
                new_app.gender = gedsi_app.gender
                new_app.age = gedsi_app.age
                new_app.civil_status = gedsi_app.civil_status
                new_app.disability = gedsi_app.disability
                new_app.ethnicity = gedsi_app.ethnicity
                new_app.duties = gedsi_app.duties

                ## Eligibility forms
                new_app.pending_scholarship = eligibilitystatus_app.pending_scholarship
                new_app.scholarship_title = eligibilitystatus_app.scholarship_title
                new_app.pending_reentry_action_plan = eligibilitystatus_app.pending_reentry_action_plan
                new_app.reap_title = eligibilitystatus_app.reap_title

                ## Required Attachments
                new_app.personal_data_sheet = requirements_app.personal_data_sheet
                new_app.individual_performance_commitment_and_review = requirements_app.individual_performance_commitment_and_review
                new_app.potential_assessment_form = requirements_app.potential_assessment_form

                ## Preselection
                new_app.pending_task = preselection_app.pending_task
                new_app.pending_case = preselection_app.pending_case
                new_app.service_record = preselection_app.service_record
                new_app.attended_training = preselection_app.attended_training

                ## Terms and Condition
                new_app.checkbox_certify = termscondition_app.checkbox_certify
                new_app.checkbox_ack = termscondition_app.checkbox_ack
                new_app.checkbox_agree = termscondition_app.checkbox_agree
                new_app.status_id = 3 ## status = Draft
                new_app.user = request.user
                new_app.save()

                return redirect('request_page')

            elif "_save" in request.POST:
                new_app = requestor_form.save(commit=False)
                nomination_app = nomination_form.save(commit=False)
                eligibilitystatus_app = eligibilitystatus_form.save(commit=False)
                requirements_app = requirements_form.save(commit=False)
                termscondition_app = termscondition_form.save(commit=False)
                gedsi_app = gedsi_form.save(commit=False)
                preselection_app = preselection_form.save(commit=False)

                nomination_app.requestor = new_app
                eligibilitystatus_app.requestor = new_app
                requirements_app.requestor = new_app
                termscondition_app.requestor = new_app

                ## Nomination Form
                new_app.name_title = nomination_app.name_title
                new_app.last_name = nomination_app.last_name
                new_app.first_name = nomination_app.first_name
                new_app.middle_initial = nomination_app.middle_initial
                new_app.nickname = nomination_app.nickname
                new_app.position = nomination_app.position
                new_app.salary_grade = nomination_app.salary_grade
                new_app.office = nomination_app.office
                new_app.e_mail = nomination_app.e_mail
                new_app.mobile_no = nomination_app.mobile_no
                new_app.office_no = nomination_app.office_no
                new_app.address = nomination_app.address

                ## GEDSI Form
                new_app.gender = gedsi_app.gender
                new_app.age = gedsi_app.age
                new_app.civil_status = gedsi_app.civil_status
                new_app.disability = gedsi_app.disability
                new_app.ethnicity = gedsi_app.ethnicity
                new_app.duties = gedsi_app.duties

                ## Eligibility forms
                new_app.pending_scholarship = eligibilitystatus_app.pending_scholarship
                new_app.scholarship_title = eligibilitystatus_app.scholarship_title
                new_app.pending_reentry_action_plan = eligibilitystatus_app.pending_reentry_action_plan
                new_app.reap_title = eligibilitystatus_app.reap_title

                ## Required Attachments
                new_app.personal_data_sheet = requirements_app.personal_data_sheet
                new_app.individual_performance_commitment_and_review = requirements_app.individual_performance_commitment_and_review
                new_app.potential_assessment_form = requirements_app.potential_assessment_form

                ## Preselection
                new_app.pending_task = preselection_app.pending_task
                new_app.pending_case = preselection_app.pending_case
                new_app.service_record = preselection_app.service_record
                new_app.attended_training = preselection_app.attended_training

                ## Terms and Condition
                new_app.checkbox_certify = termscondition_app.checkbox_certify
                new_app.checkbox_ack = termscondition_app.checkbox_ack
                new_app.checkbox_agree = termscondition_app.checkbox_agree
                new_app.status_id =  6 ## status = New
                new_app.user = request.user

                new_app.save()
                new_log = RequestorLog(change_msg = "filed a new request")
                new_log.save()
                return redirect('request_page')

        return render(request,'scholarship_app.html', {
            'requestors': requestors,
            'requestor_form': requestor_form,
            'nomination_form': nomination_form,
            'eligibilitystatus_form': eligibilitystatus_form,
            'requirements_form':requirements_form,
            'preselection_form': preselection_form,
            'termscondition_form' : termscondition_form,
            'gedsi_form':gedsi_form,
            'user': User.objects.filter(username = request.user),
            'designation': Author.objects.filter(user = request.user),
        })

    def get(self, request, pk):
        requestors = get_object_or_404(Requestor, pk=pk)
        requestor_form = NewRequestForm()
        nomination_form = NominationForm()
        eligibilitystatus_form = EligibilityStatusForm()
        gedsi_form = GedsiForm()
        requirements_form = ScholarshipRequirementsForm()
        termscondition_form = TermsConditionForm()
        preselection_form = PreSelectionForm()

        context = context = {
        'requestors': requestors,
        'requestor_form': requestor_form,
        'nomination_form': nomination_form,
        'eligibilitystatus_form': eligibilitystatus_form,
        'requirements_form':requirements_form,
        'preselection_form': preselection_form,
        'gedsi_form': gedsi_form,
        'termscondition_form' : termscondition_form,
        'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
        }

        return render(request, 'scholarship_app.html',context)
class editpost(View):
    def post(self, request, pk):
        requestors= get_object_or_404(Requestor, pk=pk)
        requestor_form = NewRequestForm(request.POST or None, request.FILES or None, instance = requestors)
        nomination_form = NominationForm(request.POST or None, instance = requestors)
        eligibilitystatus_form = EligibilityStatusForm(request.POST or None, instance = requestors)
        gedsi_form = GedsiForm(request.POST or None, instance = requestors)
        requirements_form = ScholarshipRequirementsForm(request.POST or None, request.FILES or None, instance=requestors)

        context= {
            'requestors': requestors,
            'user': User.objects.filter(username = request.user),
            'designation': Author.objects.filter(user = request.user)
            }

        if requestor_form.is_valid() or nomination_form.is_valid() or eligibilitystatus_form.is_valid() or gedsi_form.is_valid() or requirements_form.is_valid():
            if "_update" in request.POST:
                new_app = requestor_form.save(commit= False)
                nomination_app = nomination_form.save(commit=False)
                eligibilitystatus_app = eligibilitystatus_form.save(commit=False)
                gedsi_app = gedsi_form.save(commit=False)
                requirements_app = requirements_form.save(commit=False)

                nomination_app.requestor = new_app
                eligibilitystatus_app.requestor = new_app
                gedsi_app.requestor = new_app
                requirements_app.requestor = new_app
                new_app.status_id = 3
                new_app.save()
                return redirect('request_page')

                context= {
                    'requestors': requestors,
                    'requestor_form': requestor_form,
                    'nomination_form': nomination_form,
                    'gedsi_form':gedsi_form,
                    'eligibilitystatus_form':eligibilitystatus_form,
                    'requirements_form':requirements_form,
                    'user': User.objects.filter(username = request.user),
                    'designation': Author.objects.filter(user = request.user),
                    }

                return render(request, 'update.html', context)

            elif "_submit" in request.POST:
                new_app = requestor_form.save(commit= False)
                nomination_app = nomination_form.save(commit=False)
                eligibilitystatus_app = eligibilitystatus_form.save(commit=False)
                gedsi_app = gedsi_form.save(commit=False)
                requirements_app = requirements_form.save(commit=False)

                nomination_app.requestor = new_app
                eligibilitystatus_app.requestor = new_app
                gedsi_app.requestor = new_app
                requirements_app.requestor = new_app
                new_app.status_id = 6
                new_app.save()
                return redirect('request_page')


        return render(request, 'update.html',
                {
                'requestors': requestors,
                'requestor_form': requestor_form,
                'nomination_form': nomination_form,
                'gedsi_form':gedsi_form,
                'eligibilitystatus_form':eligibilitystatus_form,
                'requirements_form':requirements_form,
                'user': User.objects.filter(username = request.user),
                'designation': Author.objects.filter(user = request.user),
                })

    def get(self, request, pk):
        requestors= get_object_or_404(Requestor, pk=pk)
        requestor_form = NewRequestForm(request.POST or None, request.FILES or None, instance = requestors)
        nomination_form = NominationForm(request.POST or None, instance = requestors)
        eligibilitystatus_form = EligibilityStatusForm(request.POST or None, instance = requestors)
        gedsi_form = GedsiForm(request.POST or None, instance = requestors)
        requirements_form = ScholarshipRequirementsForm(request.POST or None, request.FILES or None, instance=requestors)

        context = {
        'requestors': requestors,
        'requestor_form': requestor_form,
        'nomination_form': nomination_form,
        'eligibilitystatus_form': eligibilitystatus_form,
        'requirements_form':requirements_form,
        'gedsi_form': gedsi_form,
        'user': User.objects.filter(username = request.user),
        'designation': Author.objects.filter(user = request.user),
        }

        return render(request, 'update.html',context)

def cancel(request, pk):
    query = {}
    query['pk'] = pk
    query['user'] = User.objects.filter(username = request.user)
    query['designation'] =  Author.objects.filter(user = request.user)
    query['requestor_now'] = Requestor.objects.filter(id = pk)
    query['rdata'] = Requestor.objects.filter(pk=pk)

    if request.method == 'POST':
        new_status = 2
        reason = request.POST.get('reason')
        justification = request.FILES.get('justification')
        upd_requestor = Requestor.objects.filter(id = pk).update(status = new_status, reason = reason)
        return HttpResponseRedirect('/requestor/requests')
    return render(request, 'cancel.html', query)


def followup(request, pk):
    query = {}
    query['pk'] = pk
    query['user'] = User.objects.filter(username = request.user)
    query['designation'] =  Author.objects.filter(user = request.user)
    query['requestor_now'] = Requestor.objects.filter(id = pk)
    query['rdata'] = Requestor.objects.filter(pk=pk)

    if request.method == 'POST':
        upd = Requestor.objects.get(id = pk)
        upd.followup = request.POST.get('followup')
        upd.save()
        return HttpResponseRedirect('/requestor/requests')
    return render(request, 'followup.html', query)

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
	query['rdata'] = Requestor.objects.filter(id = tag)
	upd = Requestor.objects.get(id = tag)
	upd.followup = True
	upd.save()

	subject = 'Followup on Scholarship Request'
	recepient = assigned
	greet = "Hi! \nThis email is to followup on a Scholarship Application assigned to "+assigned+".\n"
	tbl = "\nAPPLICATION DETAILS\n \nApplication Reference Number: "+ref+"\nApplicant Name: "+fn+" "+mi+". "+ln+" \nProgram Title: "+pt+" \nInclusive Dates: "+frm+" to "+to+" \nLocation:"+dest+"\nCurrent Status: "+st
	message = greet+tbl
	send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

	return HttpResponseRedirect('/requestor/requests')




def redirect_scholarship(request):
    query = {}
    query['first_id'] = Requestor.objects.all().order_by('id')[:1]

    return render(request, 'redirect_scholarship.html', query)

def load_sectors(request):
    category_id = request.GET.get('scholar_category')
    # selectedCategory = Category.objects.filter(id=category_id)
    sectors = SectorForScholarship.objects.filter(category_id=category_id).order_by('shortterm')
    context = {'sectors': sectors}
    # sectors = SectorForScholarship.objects.all()
    return render(request, 'sector_dropdown_list_options.html', context)



def newrequest_form_valid(self, form):
    category = form.cleaned_data.get('category')
    sector_for_scholarship = form.cleaned_data.get('sector_for_scholarship')
    prog_title = form.cleaned_data.get('prog_title')

    form_name = form.cleaned_data.get('action')
    print(category)
    print(sector_for_scholarship)
    print(prog_title)
    return HttpResponseRedirect(self.get_success_url(form_name))

def nomination_form_valid(self, form):
    last_name = form.cleaned_data.get('last_name')
    first_name = form.cleaned_data.get('first_name')
    form_name = form.cleaned_data.get('action')
    print(last_name)
    print(first_name)
    return HttpResponseRedirect(self.get_success_url(form_name))
