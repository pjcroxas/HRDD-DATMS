from django.shortcuts import render
from login.models import Author
from travelauth.models import TravelRequest_tbl
from django.contrib.auth.models import User
from django.db.models import Q
from requestor.models import *
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def sa_action_officer(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
	}
	return render(request, 'sa_action_officer/sa_ao.html', query)