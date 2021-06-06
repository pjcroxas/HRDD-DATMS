from django.shortcuts import render
from login.models import Author
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

# Create your views here.
def sa_dashboard(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
		'user_role' : Author.objects.filter(Q(user = request.user)&Q(role = 3)),
		'user_role_req' : Author.objects.filter(Q(user = request.user)&Q(role = 1)),
		'user_role_act' : Author.objects.filter(Q(user = request.user)&Q(role = 2)),
	}
	return render(request, 'super_ad/sa_dashboard.html', query)

def sa_log(request):
	query = {
		'logs': LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:10],
		'logCount': LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count(),
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
	}
	
	return render(request, 'super_ad/log.html', query)

def record_dash(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user),
	}
	return render(request, 'super_ad/record_dash.html', query)