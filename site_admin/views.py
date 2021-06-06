from django.shortcuts import render
from login.models import Author
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def site_dash(request):
	query = {
		'user': User.objects.filter(username = request.user),
		'designation': Author.objects.filter(user = request.user)
	}
	return render(request, 'site_admin/site_dash.html', query)
