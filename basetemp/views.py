from django.shortcuts import render
from login.models import Author
from travelauth.models import TravelRequest_tbl
from requestor.models import Requestor

# Create your views here.
def base(request):
	query = {}
	query['local_count'] = TravelRequest_tbl.objects.filter(request_category = "Local").count()
	query['foreign_count'] = TravelRequest_tbl.objects.filter(request_category = "Foreign").count()
	
	return render(request, 'basetemp/base.html', query)

def main_base(request):
	query = {}
	query['local_count'] = TravelRequest_tbl.objects.filter(request_category = "Local").count()
	query['foreign_count'] = TravelRequest_tbl.objects.filter(request_category = "Foreign").count()
	query['first_id'] = Requestor.objects.all().order_by('id')[:1]
	
	return render(request, 'basetemp/main_base.html', query)

