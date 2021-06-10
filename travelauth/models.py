from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from requestor.models import *
from datetime import datetime  

# Create your models here.
class request_category(models.Model):
    catt_id = models.AutoField(primary_key=True)
    request_category = models.CharField(max_length=100, blank=True, null=True)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    shorterm = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.request_category)

class travel_sector(models.Model):
    sec_id = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sector)

class travel_office(models.Model):
    off_id = models.AutoField(primary_key=True)
    office = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.office)


class TravelRequest_tbl(models.Model):
    incrementor = models.IntegerField(default=0)
    travelreq_id = models.AutoField(primary_key=True)
    date_filed = models.DateTimeField(default=timezone.now)
    request_category = models.ForeignKey(request_category, on_delete=models.CASCADE, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    support_category = models.CharField(max_length=100, blank=True, null=True)
    sector = models.ForeignKey(travel_sector, on_delete=models.CASCADE, null=True)
    program_title = models.CharField(max_length=100, blank=True, null=True)
    name_title = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_initial = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    civil_status = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=100, blank=True, null=True)
    ethnicity = models.CharField(max_length=100, blank=True, null=True)
    agency = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    programdates_from = models.CharField(max_length=100, blank=True, null=True)
    programdates_to = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default = 0)
    cancel_mess = models.CharField(max_length=100, blank=True, null=True)
    ta_signed_upload = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    lacking_documents = models.CharField(max_length=100, blank=True, null=True)
    unsigned_docs = models.CharField(max_length=100, blank=True, null=True)
    wrong_attachment = models.CharField(max_length=100, blank=True, null=True)
    with_issues = models.CharField(max_length=100, blank=True, null=True)
    taketimestamp = models.DateTimeField(blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    office_number = models.CharField(max_length=100, blank=True, null=True)
    salary_grade = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    pptr = models.CharField(max_length=100, blank=True, null=True)

 
    
    ic_endorsement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_icd = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_invitation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_no_pending_task = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_no_admin_case = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_service_record = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_funds = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_expenses = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_unliquidated = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_retirement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ic_undertaking = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    mc_endorsement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_icd = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_invitation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_no_pending_task = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_no_admin_case = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_service_record = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_funds = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_expenses = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_unliquidated = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_retirement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    mc_undertaking = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    ts_endorsement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_icd = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_invitation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_acceptance = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_minutes = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_scholarship = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_no_pending_task = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_no_admin_case = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_service_record = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_funds = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_expenses = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_unliquidated = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_retirement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_undertaking = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    ts_report = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_endorsement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_icd = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_invitation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_agreement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_no_pending_task = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_no_admin_case = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_service_record = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_funds = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_expenses = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_unliquidated = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_retirement = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    fi_undertaking = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    pt_icd = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    pt_no_pending_task = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    pt_no_admin_case = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    pt_service_record = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    pt_leave_application = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    pt_clearance = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    t_pre_registration = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    t_pds = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    t_ipcr = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    t_paf = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    t_report = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    nt_invitation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    nt_transportation = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    nt_allowance = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    nt_others = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
<<<<<<< HEAD
=======
    nt_without_gov_expense = models.IntegerField(default=0, null = True)
>>>>>>> brian

    additional_requirement_1 = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    additional_requirement_2 = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    cancel_file = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')

    requestor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    assigned = models.ForeignKey(User, blank=True, null=True,
         on_delete=models.CASCADE, related_name='travelassigned')
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, null=True, default=4, blank=True)
    sponsor = models.CharField(max_length=100, blank=True, null=True)
    pre_travel_expense = models.CharField(max_length=100, blank=True, null=True)
    dsa_day = models.CharField(max_length=100, blank=True, null=True)
    clothing_allowance = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    rep_allowance = models.CharField(max_length=100, blank=True, null=True)
    other_remarks = models.CharField(max_length=100, blank=True, null=True)
    ptr_submitted = models.CharField(max_length=100, blank=True, null=True)
    echo_seminar = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    ptr_dnpt = models.CharField(max_length=100, blank=True, null=True)
    acknowledgement = models.CharField(max_length=100, blank=True, null=True)
    endorsement = models.CharField(max_length=100, blank=True, null=True)
    inviting_institute = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    fee = models.CharField(max_length=100, blank=True, null=True)
    perday = models.CharField(max_length=100, blank=True, null=True)
    other_expense = models.CharField(max_length=100, blank=True, null=True)
    echo = models.CharField(max_length=100, blank=True, null=True)
    training_report = models.CharField(max_length=100, blank=True, null=True)
    received = models.CharField(max_length=100, blank=True, null=True)
    released = models.CharField(max_length=100, blank=True, null=True)


    ## Follow up
    FOLLOWCHOICE = (
    (1, 'True'),
    (0, 'False'),
    )
    followup = models.BooleanField(verbose_name="Follow up to HRDD", choices = FOLLOWCHOICE, default="False")


    def __str__(self):
    	return str(self.program_title)

    def save(self):
        if self.incrementor == 0:
            if self.request_category.catt_id == 1:
                latest_incrementor = TravelRequest_tbl.objects.all().filter(request_category=1).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                ## Uncomment this for first request
                # self.incrementor = self.incrementor + 0
                super(TravelRequest_tbl, self).save()
            elif self.request_category.catt_id == 2:
                latest_incrementor = TravelRequest_tbl.objects.all().filter(request_category=2).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                ## Uncomment this for first request
                # self.incrementor = self.incrementor + 0
                super(TravelRequest_tbl, self).save()
            elif self.request_category.catt_id == 3:
                latest_incrementor = TravelRequest_tbl.objects.all().filter(request_category=2).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                ## Uncomment this for first request
                # self.incrementor = self.incrementor + 0
                super(TravelRequest_tbl, self).save()
            else:
                super(TravelRequest_tbl, self).save()
        else:
            super(TravelRequest_tbl, self).save()

class History_tbl(models.Model):
    history_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    a_officer = models.CharField(max_length=100, blank=True, null=True)
    travelreq_id = models.CharField(max_length=100, blank=True, null=True)
    eval_date =models.DateTimeField(default=timezone.now)
    scholar_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.status)+" by "+str(self.a_officer)+". For Evaluation. ("+str(self.eval_date)+")."

class Pending_remarks(models.Model):
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
    	return str(self.remarks)


class Pending_training_report(models.Model):
    report_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_initial = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    training_institution = models.CharField(max_length=100, blank=True, null=True)
    course_name = models.CharField(max_length=100, blank=True, null=True)
    duration_in_days = models.CharField(max_length=100, blank=True, null=True)
    programdates_from = models.DateField(default=datetime.now, blank=True)
    programdates_to = models.DateField(default=datetime.now, blank=True)
    program_fee = models.CharField(max_length=100, blank=True, null=True)
    post_report_submit_date = models.DateField(default=datetime.now, blank=True)
    echo_seminar_date = models.DateField(default=datetime.now, blank=True)
    remarks = models.ForeignKey(Pending_remarks, on_delete=models.CASCADE, null=True)

    def __str__(self):
    	return str(self.course_name)

