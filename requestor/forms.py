from django import forms
from .models import (Requestor,
                     Category,
                     SectorForScholarship,
                     Nomination_Form,
                     Eligibility_Status,
                     Scholarship_Requirements,
                     TermsCondition)
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from bootstrap_datepicker_plus import DatePickerInput
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

# class NewRequestForm(forms.ModelForm):
#     '''This class displays the Scholarship Application Form'''
#
#     # reference = forms.CharField(max_length=4000)
#     ## Dropdown Category
#     filing_date = forms.DateField(widget=forms.SelectDateWidget())
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     sector_for_scholarship = forms.ModelChoiceField(queryset=SectorForScholarship.objects.all())
#     ## Dropdown Scholarship Nomination
#     prog_title = forms.CharField(max_length=50)
#     location = forms.CharField(max_length=4000)
#     start_date = forms.DateField(widget=forms.SelectDateWidget())
#     end_date = forms.DateField(widget=forms.SelectDateWidget())
#     attachments = forms.FileField()
#
#
#     class Meta:
#         model = Requestor
#         fields = ['filing_date', 'category','sector_for_scholarship', 'prog_title',
#                   'location', 'start_date', 'end_date', 'attachments']

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())



class NewRequestForm(forms.ModelForm):
    '''This class displays the Scholarship Application Form'''

    # reference = forms.CharField(max_length=4000)
    ## Dropdown Category
    # filing_date = forms.DateField(widget=forms.SelectDateWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    sector_for_scholarship = forms.ModelChoiceField(queryset=SectorForScholarship.objects.all(), label='Sector')
    ## Dropdown Scholarship Nomination
    prog_title = forms.CharField(max_length=50, label="Program Title")
    location = forms.CharField(max_length=4000)
    # start_date = forms.DateField()
    # end_date = forms.DateField()
    # attachments = forms.FileField()

    class Meta:
            model = Requestor
            fields = ['category','sector_for_scholarship', 'prog_title',
                      'location', 'start_date', 'end_date']
            widgets = {
                'start_date':DatePickerInput(),
                'end_date':DatePickerInput()
            }


    def __init__(self, *args, **kwargs):
        super(NewRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('category', css_class='form-group col-md-6 mb-0'),
                Column('sector_for_scholarship', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'prog_title',
            'location',
            Row(
                Column('start_date', css_class='form-group col-md-6 mb-0'),
                Column('end_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),)
        self.helper.form_tag = False

        ## dropdown
        self.fields['sector_for_scholarship'].queryset = SectorForScholarship.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                print(category_id)
                self.fields['sector_for_scholarship'].queryset = SectorForScholarship.objects.filter(category_id=category_id).order_by('shortterm')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sector_for_scholarship'].queryset = self.instance.category.sector_for_scholarship_set.order_by('shortterm')





class NominationForm(forms.ModelForm):
    name_title = forms.CharField(max_length=100, label="Title")
    last_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    middle_initial = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    salary_grade = forms.CharField(max_length=100)
    office = forms.CharField(max_length=100)
    e_mail = forms.EmailField(max_length=100)
    mobile_no = forms.CharField(max_length=100)
    office_no = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)

    class Meta:
            model = Requestor
            fields = ['last_name', 'first_name','middle_initial', 'position',
                      'nickname', 'position', 'salary_grade', 'office',
                      'e_mail','mobile_no', 'office_no', 'address','name_title']

    def __init__(self, *args, **kwargs):
        super(NominationForm, self).__init__(*args, **kwargs)
        self.fields['name_title'].required = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name_title', css_class='form-group col-md-3 mb-0'),
                Column('last_name', css_class='form-group col-md-3 mb-0'),
                Column('first_name', css_class='form-group col-md-3 mb-0'),
                Column('middle_initial', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'address',
            Row(
                Column('nickname', css_class='form-group col-md-3 mb-0'),
                Column('position', css_class='form-group col-md-3 mb-0'),
                Column('salary_grade', css_class='form-group col-md-3 mb-0'),
                Column('office', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('office_no', css_class='form-group col-md-4 mb-0'),
                Column('e_mail', css_class='form-group col-md-4 mb-0'),
                Column('mobile_no', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),)
        self.helper.form_tag = False



GENDER_CHOICES = (
    ('-----', '-----'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Others'),
    ('Prefer not to say', 'Prefer not to say')
)
CIVIL_STATUS_CHOICES = (
    ('-----', '-----'),
    ('single', 'Single'),
    ('married', 'Married'),
    ('legally separated', 'Legally Separated'),
    ('annulled', 'Annulled'),
    ('widowed', 'Widowed')
)

class GedsiForm(forms.ModelForm):

    label_duty = '''Actual Duties and Responsibilities'''
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    age = forms.IntegerField()
    civil_status = forms.ChoiceField(choices=CIVIL_STATUS_CHOICES, label="Civil Status")
    # disability = forms.CharField(max_length=100)
    # ethnicity = forms.CharField(max_length=100)
    duties = forms.CharField(max_length=200, widget=forms.Textarea, label=label_duty)

    class Meta:
            model = Nomination_Form
            fields = ['gender', 'age', 'civil_status', 'disability','ethnicity','duties']

    def __init__(self, *args, **kwargs):
        super(GedsiForm, self).__init__(*args, **kwargs)
        self.fields['disability'].required = False
        self.fields['ethnicity'].required = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                Column('civil_status', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ethnicity', css_class='form-group col-md-6 mb-0'),
                Column('disability', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'duties')
        self.helper.form_tag = False

# class PreSelectionForm(forms.ModelForm):
#     attachments = forms.FileField()
#     class Meta:
#         model = Requestor
#         fields = ['attachments']
#
#     def __init__(self, *args, **kwargs):
#         super(PreSelectionForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False

class ScholarshipRequirementsForm(forms.ModelForm):
    personal_data_sheet = forms.FileField(label="Personal Data Sheet (Required)")
    individual_performance_commitment_and_review = forms.FileField(label = "Individual Performance Commitment and Review (Required)")
    potential_assessment_form = forms.FileField(label="Potential Assessment Form (Required)")
    last_file = forms.FileField(label="Signed Nomination Form")

    class Meta:
        model = Requestor
        fields = ['personal_data_sheet', 'individual_performance_commitment_and_review',
                   'potential_assessment_form', 'last_file']

    def __init__(self, *args, **kwargs):
        super(ScholarshipRequirementsForm, self).__init__(*args, **kwargs)
        self.fields['last_file'].required = False
        self.helper = FormHelper()
        self.helper.form_tag = False

class EligibilityStatusForm(forms.ModelForm):
    label_pending = "Do you have pending scholarship program from other inviting institution?"
    label_re_enry = "Do you have pending Re-entry Action Plan (REAP) or Capstone Project?"

    label_title = "Please write the program/course title"
    label_reap = "Please write the REAP title or Capstone Project"

    PENDING_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    
    pending_scholarship = forms.ChoiceField(choices = PENDING_CHOICES, label=label_pending)
    scholarship_title = forms.CharField(max_length=100, label=label_title)
    pending_reentry_action_plan = forms.ChoiceField(choices = PENDING_CHOICES, label=label_pending)
    reap_title = forms.CharField(max_length=100, label=label_reap)

    class Meta:
        model = Requestor
        fields = ['pending_scholarship', 'scholarship_title', 'pending_reentry_action_plan',
                  'reap_title']

    def __init__(self, *args, **kwargs):
        super(EligibilityStatusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column('pending_scholarship', css_class='form-group col-md-6 mb-0'),
                Column('pending_reentry_action_plan', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('scholarship_title', css_class='form-group col-md-6 mb-0'),
                Column('reap_title', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ))
        self.helper.form_tag = False


class PreSelectionForm(forms.ModelForm):
    label_pending = "Certificate of No Pending Case"
    label_task = "Certificate of No Pending Task"


    PENDING_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )

    pending_task = forms.FileField(label=label_task)
    pending_case = forms.FileField(label=label_pending)
    service_record = forms.FileField(label="Service Record")
    attended_training = forms.FileField(label="List of Attended Training (For Foreign Scholarship Application)")

    class Meta:
        model = Requestor
        fields = ['pending_task', 'pending_case', 'service_record', 'attended_training']

    def __init__(self, *args, **kwargs):
        super(PreSelectionForm, self).__init__(*args, **kwargs)
        self.fields['service_record'].required = False
        self.helper = FormHelper()
        self.helper.form_tag = False


class TermsConditionForm(forms.ModelForm):
    label_certify = 'I certify that the above is true and correct to the best of my knowledge.'
    label_ack = """I acknowledge and accept the condition that without the
                   original copies of all the signed forms herewith uploaded,
                   no travel order/authority will be issued to me. """

    label_agree = 'I agree with the DOTr Data Privacy Policy'

    checkbox_certify = forms.BooleanField(label = label_certify)
    checkbox_ack = forms.BooleanField(label = label_ack)
    checkbox_agree = forms.BooleanField(label = label_agree)


    class Meta:
        model = Requestor
        fields = ['checkbox_certify', 'checkbox_ack', 'checkbox_agree']

    def __init__(self, *args, **kwargs):
        super(TermsConditionForm, self).__init__(*args, **kwargs)

        self.fields['checkbox_agree'].label = mark_safe(_("I have read and agree with the "
                                                      "<a href ='https://drive.google.com/file/d/1HEzzosPzH27nSpMPKoUMKshvLOauWq9X/view'>DOTr Data Privacy Policy</a>"))
        self.helper = FormHelper()
        self.helper.form_tag = False
