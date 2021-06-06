from django.shortcuts import render
from login.models import Author
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def dashboard(request):
	query = {
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'user_role_sact' : Author.objects.filter(Q(user = request.user)&Q(role = 5)),
		'user_role_sa' : Author.objects.filter(Q(user = request.user)&Q(role = 4)),
	}
	return render(request, 'dashboard/dashboard.html', query)

def dashboard1(request):
	query = {
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
		'user_role_sact' : Author.objects.filter(Q(user = request.user)&Q(role = 5)),
		'user_role_sa' : Author.objects.filter(Q(user = request.user)&Q(role = 4)),
	}
	return render(request, 'dashboard/dashboard1.html', query)
