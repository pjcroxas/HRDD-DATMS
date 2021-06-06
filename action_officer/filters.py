from travelauth.models import TravelRequest_tbl, request_category, travel_sector
import django_filters
# from django_filters.widgets import Date

from django import forms




class GedsiReport(django_filters.FilterSet):
    # programdates_from = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type':'date'}))
    # GENDER_CHOICES = (
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('No Value', 'No Value'),
    #     ('Other', 'Others'),
    #     ('Prefer not to say', 'Prefer not to say')
    # )
    # gender = django_filters.MultipleChoiceFilter(choices=GENDER_CHOICES, null_value='-----', widget=forms.CheckboxSelectMultiple, label='GENDER')
    # program_title = django_filters.CharFilter(lookup_expr='icontains', label='PROGRAM TITLE')
    programdates_from=django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="START DATE"
    )
    programdates_to =django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="END DATE"
    )
    # request_category = django_filters.ModelMultipleChoiceFilter(queryset=request_category.objects.all(), widget=forms.CheckboxSelectMultiple, label='CATEGORY')
    # sector = django_filters.ModelMultipleChoiceFilter(queryset=travel_sector.objects.all(), widget=forms.CheckboxSelectMultiple, label="SECTOR")
    # destination = django_filters.CharFilter(lookup_expr='icontains', label='DESTINATION')



    class Meta:
        model = TravelRequest_tbl
        fields = ['programdates_from', 'programdates_to']



class EthnicityReport(django_filters.FilterSet):
    programdates_from=django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="START DATE"
    )
    programdates_to =django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="END DATE"
    )

    class Meta:
        model = TravelRequest_tbl
        fields = ['programdates_from', 'programdates_to']


class DisabilityReport(django_filters.FilterSet):
    programdates_from=django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="START DATE"
    )
    programdates_to =django_filters.DateFilter(widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ),
        label="END DATE"
    )
    class Meta:
        model = TravelRequest_tbl
        fields = ['programdates_from', 'programdates_to']
