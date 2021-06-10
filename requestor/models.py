from django.db import models
from django.contrib.auth.models import User, Group
from .validators import validate_file_extension
from django.utils import timezone

# Create your models here.





class Category(models.Model):
    categories = models.CharField(max_length=100)
    shortterm = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.categories

    def natural_key(self):
        return (self.categories)

    def get_short(self):
        return self.shortterm



class SectorForScholarship(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True,  related_name="sector_for_scholarship_set")

class SectorForScholarship(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,  related_name="sector_for_scholarship_set")

    sectorforscholarship = models.CharField(max_length=100)
    shortterm = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.sectorforscholarship

    def natural_key(self):
        return (self.sectorforscholarship)





class SubCategory(models.Model):
    subcategories = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategories

    def natural_key(self):
        return (self.subcategories)





class SupportCategory(models.Model):
    ShortTerm = models.CharField(max_length=10, null=True)
    supportcategories = models.CharField(max_length=100)

    def __str__(self):
        return self.supportcategories

    def get_short(self):
        return self.ShortTerm

    def natural_key(self):
        return (self.supportcategories)





class Sector(models.Model):
    sector = models.CharField(max_length=100)

    def __str__(self):
        return self.sector

    def natural_key(self):
        return (self.sector)






class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

    def natural_key(self):

        return (self.status)

        return (self.status)




class Requestor(models.Model):
    '''Child table of Category, SubCategory,
    SupportCategory, Sector, SectorForScholarship,
    Status'''

    incrementor = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, default='')

    reference_scholarship = models.CharField(max_length=500, verbose_name=(
        'Reference'), default='Auto Assign', blank=True)
    ##### when i used date_filed in reference, the output is "nonetype" #####
    date_filed = models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_filed')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, verbose_name="Category")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                    null=True, verbose_name="Sub Category")
    supportcategory = models.ForeignKey(SupportCategory,
                                        on_delete=models.CASCADE, null=True, verbose_name="Support Category")
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE,
                               null=True, verbose_name="Sector")
    sector_for_scholarship = models.ForeignKey(SectorForScholarship,
                                               on_delete=models.CASCADE, null=True, verbose_name="Sector")



    location = models.CharField(max_length=50, blank=True, null=True)
    prog_title = models.CharField(max_length=50)
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, null=True, default=6, blank=True)
    attachments = models.FileField(
        upload_to='uploads/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    assigned = models.ForeignKey(User, blank=True, null=True,

                                 on_delete=models.CASCADE, related_name='assigned')
   # field for cancel function
    reason = models.CharField(max_length=100, blank=True, null=True)
    lacking_documents = models.CharField(max_length=250, blank=True, null=True)
    ta_signed_upload = models.FileField(
        max_length=100, blank=True, null=True, upload_to='uploads/')
    taketimestamp = models.DateTimeField(blank=True, null=True)

    sa_signed_upload = models.FileField(
        upload_to='sa_signed_upload/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)

    # filing_date = models.DateField(null=True) ## Temporary
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    req_action = models.CharField(max_length=50, default=0)
    gender = models.CharField(max_length=100, blank=True, null=True)
    scho_donor = models.CharField(max_length=100, blank=True, null=True)
    other_expense = models.CharField(max_length=100, blank=True, null=True)
    service_obligation = models.CharField(
        max_length=100, blank=True, null=True)


   # field for cancel function
    reason = models.CharField(max_length=100, blank=True, null=True)
    lacking_documents = models.CharField(max_length=250, blank=True, null=True)
    ta_signed_upload = models.FileField(max_length=100, blank=True, null = True, upload_to ='uploads/')
    taketimestamp = models.DateTimeField(blank=True, null=True)

    # filing_date = models.DateField(null=True) ## Temporary
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    req_action = models.CharField(max_length=50, default = 0)
    gender = models.CharField(max_length=100, blank=True, null=True)
    scho_donor = models.CharField(max_length=100, blank=True, null=True)
    other_expense = models.CharField(max_length=100, blank=True, null=True)
    service_obligation =  models.CharField(max_length=100, blank=True, null=True)

    echo = models.CharField(max_length=100, blank=True, null=True)
    training_report = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)





    # Nomination forms
    name_title = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    middle_initial = models.CharField(max_length=100, default='')
    nickname = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')
    salary_grade = models.CharField(max_length=100, default='')
    office = models.CharField(max_length=100, default='')
    e_mail = models.EmailField(max_length=100, default='')
    mobile_no = models.CharField(max_length=100, default='')
    office_no = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')


    # Gedsi

    ## Gedsi

    PENDING_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    CIVIL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('legally separated', 'Legally Separated'),
        ('annulled', 'Annulled'),
        ('widowed', 'Widowed')
    )

    gender = models.CharField(
        max_length=10, choices=PENDING_CHOICES, default='')
    age = models.IntegerField(null=True, blank=True)
    civil_status = models.CharField(
        max_length=20, choices=CIVIL_STATUS_CHOICES, default='')
    disability = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)
    duties = models.CharField(max_length=400, null=True, blank=True)

    # Eligibility Status

    gender = models.CharField(max_length=10, choices=PENDING_CHOICES, default='')
    age = models.IntegerField(null=True, blank=True)
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES, default='')
    disability = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)
    duties = models.CharField(max_length= 400, null=True, blank=True)

    ## Eligibility Status

    PENDING_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )

    pending_scholarship = models.CharField(
        max_length=10, choices=PENDING_CHOICES, null=True)
    scholarship_title = models.CharField(max_length=100, null=True)
    pending_reentry_action_plan = models.CharField(
        max_length=10, choices=PENDING_CHOICES, null=True, blank=True)

    pending_scholarship = models.CharField(max_length=10, choices=PENDING_CHOICES, null=True)
    scholarship_title = models.CharField(max_length=100, null=True)
    pending_reentry_action_plan = models.CharField(max_length=10, choices=PENDING_CHOICES, null=True, blank=True)

    reap_title = models.CharField(max_length=100, null=True, blank=True)

    last_file = models.FileField(
        upload_to='signed_nomination/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)


    # Preselection


    ## Preselection

    pending_task = models.FileField(
        upload_to='pending_tasks/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    service_record = models.FileField(
        upload_to='s_r/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)

    pending_case = models.FileField(
        upload_to='pending_case/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    attended_training = models.FileField(
        upload_to='a_t/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)


    # # Scholarship Requirements
    # personal_data_sheet = models.FileField(
    #     upload_to='pds/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    # individual_performance_commitment_and_review = models.FileField(
    #     upload_to='ipcr/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    # potential_assessment_form = models.FileField(


    ## Scholarship Requirements
    personal_data_sheet = models.FileField(
        upload_to='pds/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    individual_performance_commitment_and_review =  models.FileField(
        upload_to='ipcr/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    potential_assessment_form = models.FileField(
        upload_to='paf/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    justification = models.FileField(
        upload_to='justification/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)

    ## Terms & Conditions

    checkbox_certify = models.BooleanField(
        verbose_name="Certify", default="False")
    checkbox_ack = models.BooleanField(
        verbose_name="Acknowledgement", default='False')
    checkbox_agree = models.BooleanField(verbose_name="Agree", default='False')

    FOLLOWCHOICE = (
        (1, 'True'),
        (0, 'False'),
    )
    followup = models.BooleanField(
        verbose_name="Follow up to HRDD", choices=FOLLOWCHOICE, default="False")

    checkbox_certify = models.BooleanField(verbose_name="Certify", default="False")
    checkbox_ack = models.BooleanField(verbose_name="Acknowledgement", default='False')
    checkbox_agree = models.BooleanField(verbose_name="Agree", default='False')

    FOLLOWCHOICE = (
    (1, 'True'),
    (0, 'False'),
    )
    followup = models.BooleanField(verbose_name="Follow up to HRDD", choices = FOLLOWCHOICE, default="False")


    @property
    def filename(self):
        return os.path.basename(self.personal_data_sheet.name)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.personal_data_sheet.name)

    @property
    def filename(self):
        return os.path.basename(self.individual_performance_commitment_and_review.name)

    @property
    def extension(self):

        name, extension = os.path.splitext(
            self.individual_performance_commitment_and_review.name)

        name, extension = os.path.splitext(self.individual_performance_commitment_and_review.name)


    @property
    def filename(self):
        return os.path.basename(self.potential_assessment_form.name)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.potential_assessment_form.name)







    @property
    def filename(self):
        return os.path.basename(self.attachments.name)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.attachments.name)





    def __str__(self):
        return self.reference

    def __str__(self):
        return self.category

    def __str__(self):
        return self.prog_title

    def save(self):
        if self.incrementor == 0:
            if self.category.id == 1:

                latest_incrementor = Requestor.objects.all().filter(
                    category=1).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                # Uncomment this for first request
                #self.incrementor = self.incrementor + 0
                super(Requestor, self).save()
            elif self.category.id == 2:
                latest_incrementor = Requestor.objects.all().filter(
                    category=2).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                # Uncomment this for first request

                latest_incrementor = Requestor.objects.all().filter(category=1).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                ## Uncomment this for first request
                #self.incrementor = self.incrementor + 0
                super(Requestor, self).save()
            elif self.category.id == 2:
                latest_incrementor = Requestor.objects.all().filter(category=2).values('incrementor').last()
                latest_incrementor = latest_incrementor['incrementor']
                self.incrementor = latest_incrementor + 1
                ## Uncomment this for first request

                #self.incrementor = self.incrementor + 0
                super(Requestor, self).save()
            else:
                super(Requestor, self).save()
        else:
            super(Requestor, self).save()





class Nomination_Form(models.Model):
    nomination_id = models.AutoField(primary_key=True)
    # purpose = models.CharField(max_length=100)
    name_title = models.CharField(max_length=100, default='')
    requestor = models.OneToOneField(Requestor, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary_grade = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    office_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


    # Gedsi

    ## Gedsi

    PENDING_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    CIVIL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('legally separated', 'Legally Separated'),
        ('annulled', 'Annulled'),
        ('widowed', 'Widowed')
    )

    gender = models.CharField(
        max_length=10, choices=PENDING_CHOICES, default='')
    age = models.IntegerField(null=True, blank=True)
    civil_status = models.CharField(
        max_length=20, choices=CIVIL_STATUS_CHOICES, default='')
    disability = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)
    duties = models.CharField(max_length=400, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=PENDING_CHOICES, default='')
    age = models.IntegerField(null=True, blank=True)
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES, default='')
    disability = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)
    duties = models.CharField(max_length= 400, null=True, blank=True)


    def __str__(self):
        return str(self.requestor)


class Eligibility_Status(models.Model):

    requestor = requestor = models.OneToOneField(
        Requestor, on_delete=models.CASCADE)

    requestor = requestor = models.OneToOneField(Requestor, on_delete=models.CASCADE)

    eligibility_id = models.AutoField(primary_key=True)
    PENDING_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )

    pending_scholarship = models.CharField(
        max_length=10, choices=PENDING_CHOICES)
    scholarship_title = models.CharField(max_length=100)
    pending_reentry_action_plan = models.CharField(
        max_length=10, choices=PENDING_CHOICES)

    pending_scholarship = models.CharField(max_length=10, choices=PENDING_CHOICES)
    scholarship_title = models.CharField(max_length=100)
    pending_reentry_action_plan = models.CharField(max_length=10, choices=PENDING_CHOICES)

    reap_title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.requestor)


class Scholarship_Requirements(models.Model):
    requestor = models.OneToOneField(Requestor, on_delete=models.CASCADE)
    personal_data_sheet = models.FileField(
        upload_to='pds/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)

    individual_performance_commitment_and_review = models.FileField(
        upload_to='ipcr/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)
    potential_assessment_form = models.FileField(
        upload_to='paf/%Y/%m/%d/', validators=[validate_file_extension], null=True, blank=True)

    @property
    def filename(self):
        return os.path.basename(self.personal_data_sheet.name)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.personal_data_sheet.name)

    @property
    def filename(self):
        return os.path.basename(self.individual_performance_commitment_and_review.name)

    @property
    def extension(self):

        name, extension = os.path.splitext(
            self.individual_performance_commitment_and_review.name)

        name, extension = os.path.splitext(self.individual_performance_commitment_and_review.name)


    @property
    def filename(self):
        return os.path.basename(self.potential_assessment_form.name)

    @property
    def extension(self):
        name, extension = os.path.splitext(self.potential_assessment_form.name)

    def __str__(self):
        return str(self.requestor)


class TermsCondition(models.Model):
    label_certify = 'I certify that the above is true and correct to the best of my knowledge'
    label_ack = """I acknowledge and accept the condition that without the
                   original copies of all the signed forms herewith uploaded,
                   no travel order/authority will be issued to me. """

    label_agree = 'I agree with the DOTr Data Privacy Policy'

    requestor = models.OneToOneField(Requestor, on_delete=models.CASCADE)
    checkbox_certify = models.BooleanField(verbose_name=label_certify)
    checkbox_ack = models.BooleanField(verbose_name=label_ack, default='False')

    checkbox_agree = models.BooleanField(
        verbose_name=label_agree, default='False')

    checkbox_agree = models.BooleanField(verbose_name=label_agree, default='False')


    def __str__(self):
        return str(self.requestor)



class RequestorLog(models.Model):
    log_id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, verbose_name="Users")
    content_type = models.ForeignKey(Status, on_delete=models.CASCADE,
                                     null=True, verbose_name="content")




class RequestorLog(models.Model):
    log_id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
         null=True, verbose_name="Users")
    content_type = models.ForeignKey(Status, on_delete=models.CASCADE,
         null=True, verbose_name="content")


    change_msg = models.CharField(max_length=100)

    def __str__(self):
        return self.change_msg

    def __str__(self):
        return self.content_type

    def __str__(self):
        return self.change_msg
