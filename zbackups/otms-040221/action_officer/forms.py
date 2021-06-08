from django import forms
from requestor.models import *
from travelauth.models import *
from login.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Requestor
        fields = ('status',)

class UpdateFormTravel(forms.ModelForm):
    OPTIONS = (
        (0, "Endorsement from Usec. concerned"),
        (1, "Request for Travel Authority"),
        (2, "Invitation Letter from the host/country"),
        (3, "Certificate as to no pending task/Office-in-charge"),
        (4, "Certification as to no pending admin case"),
        (5, "Service Record"),
        (6, "Certificate of Availability of Funds"),
        (7, "Estimate Breakdown of expenses"),
        (8, "Certificate as to no unliquidated cash advance"),
        (9, "Certificate as to not due to retirement/resign"),
        (10, "Certificate of undertaking"),
    )
    with_issues = forms.CharField(label='Other Issues',
                    widget=forms.TextInput(attrs={'placeholder': 'Ex. No Attachment, Unliquidated', 'style': 'width:400px'}), required=False)

    unsigned_docs = forms.CharField(label='Unsigned Docs',
                    widget=forms.TextInput(attrs={'placeholder': 'Ex Format. No Attachment, No Pending Case Unsigned', 'style': 'width:400px'}), required=False)

    wrong_attachment = forms.CharField(label='Wrong Attachment',
                    widget=forms.TextInput(attrs={'placeholder': 'Ex. Format: Walang Helmet, Backride Ko', 'style': 'width:400px'}), required=False)

    lacking_documents = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS, required=False)

    class Meta:
        model = TravelRequest_tbl
        fields = ('status','ta_signed_upload','lacking_documents', 'with_issues', 'unsigned_docs', 'wrong_attachment' )

class DatabaseTravelUpdateForm(forms.ModelForm):
    class Meta:
        model = TravelRequest_tbl
        fields = ('gender','first_name','last_name', 'agency','position','programdates_from', 'programdates_to', 'request_category', 'program_title',
        'destination','sponsor','pre_travel_expense', 'dsa_day','clothing_allowance','remarks','rep_allowance','other_remarks',
        'ptr_submitted', 'echo_seminar','year','ptr_dnpt','acknowledgement','endorsement' )
        labels = {
            "gender": "Sex",
            "programdates_from": "Departure",
            "programdates_to": "Arrival",
            "request_category": "Type of Travel",
            "program_title": "Seminar Title/Purpose",
        }

class DatabaseTravelLocalUpdateForm(forms.ModelForm):
    class Meta:
        model = TravelRequest_tbl
        fields = ('first_name','last_name','position', 'agency','program_title','inviting_institute','venue','programdates_from','programdates_to','fee',
        'perday','other_expense', 'echo', 'training_report','received','released','remarks'  )
        labels = {
            "gender": "Sex",
            "programdates_from": "Departure",
            "programdates_to": "Arrival",
            "request_category": "Type of Travel",
            "program_title": "Seminar Title/Purpose",
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #          Row(
    #             Column('gender', css_class='form-group col-md-2 mb-0'),
    #             Column('first_name', css_class='form-group col-md-5 mb-0'),
    #             Column('last_name', css_class='form-group col-md-5 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #            Column('agency', css_class='form-group col-md-3 mb-0'),
    #            Column('position', css_class='form-group col-md-3 mb-0'),
    #            Column('programdates_from', css_class='form-group col-md-3 mb-0'),
    #            Column('programdates_to', css_class='form-group col-md-3 mb-0'),
    #            css_class='form-row'
    #        ),
    #          Row(
    #             Column('request_category', css_class='form-group col-md-2 mb-0'),
    #             Column('program_title', css_class='form-group col-md-5 mb-0'),
    #             Column('destination', css_class='form-group col-md-5 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #            Column('sponsor', css_class='form-group col-md-3 mb-0'),
    #            Column('pre_travel_expense', css_class='form-group col-md-3 mb-0'),
    #            Column('dsa_day', css_class='form-group col-md-3 mb-0'),
    #             Column('clothing_allowance', css_class='form-group col-md-3 mb-0'),
    #            css_class='form-row'
    #        ),
    #        Row(
    #           Column('remarks', css_class='form-group col-md-3 mb-0'),
    #           Column('rep_allowance', css_class='form-group col-md-3 mb-0'),
    #           Column('other_remarks', css_class='form-group col-md-3 mb-0'),
    #           Column('ptr_submitted', css_class='form-group col-md-3 mb-0'),
    #           css_class='form-row',
    #         ),
    #          Row(
    #             Column('echo_seminar', css_class='form-group col-md-3 mb-0'),
    #             Column('year', css_class='form-group col-md-3 mb-0'),
    #             Column('ptr_dnpt', css_class='form-group col-md-3 mb-0'),
    #             Column('acknowledgement', css_class='form-group col-md-3 mb-0'),
    #             css_class='form-row',
    #           ),
    #          Row(
    #             Column('endorsement', css_class='form-group col-md-3 mb-0'),
    #             css_class='form-row',
    #           )
    #         ,)
            # ),
            # 'address_1',
            # 'address_2',
            # Row(
            #     Column('city', css_class='form-group col-md-6 mb-0'),
            #     Column('state', css_class='form-group col-md-4 mb-0'),
            #     Column('zip_code', css_class='form-group col-md-2 mb-0'),
            #     css_class='form-row'
            # ),
            # 'check_me_out',
            # Submit('submit', 'Sign in')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username',
                  'password']

        label = {
            'password': 'Password'
        }
    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(UserForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        # self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})


    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']

class ScholarshipUpdateForm(forms.ModelForm):

    class Meta:
        model = Requestor
        fields = ('gender','category','prog_title','scho_donor','location','start_date','end_date','other_expense','service_obligation','echo','training_report','remarks')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('middle_initial','official_designation','office_or_agency','sector','mobile','role')


    def __init__(self,  *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Roles.objects.filter(Q(role = 'Requestor') | Q(role = 'Action Officer'))
