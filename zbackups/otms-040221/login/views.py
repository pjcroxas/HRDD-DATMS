from django.shortcuts import render
from .models import anntbl
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from OTMS.settings import EMAIL_HOST_USER
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


# Create your views here.
def login(request):
	return render(request, 'login/login.html')

def banner(request):
	query = {
		'first': anntbl.objects.filter(anid = 1),
		'res' :  anntbl.objects.filter(~Q(anid = 1))
	}
	return render(request, 'login/banner.html', query)

def reset(request):
	if request.method == 'POST':
		try:
			emailadd = request.POST.get('eadd')
			users = User.objects.get(email = emailadd)
			if request.POST.get('eadd'): 
				subject = 'Reset Password'
				recepient = request.POST.get('eadd')
				greet = '<p>Good day, click on the link for your password reset instructions 127.0.0.1:8000/linkreset/</p>'
				link = request.POST.get('eadd')
				message = greet+link
				send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
				messages.info(request, "Your Username and Temporary Password has been sent to your email address.Kindly check your email or contact the System Administrator at (02) 8888 local 88.")
			
				return render(request, 'login/reset.html')
			else:
				messages.info(request, 'Failed!')
				return render(request, 'login/reset.html')
		except ObjectDoesNotExist:
			messages.info(request, 'Email Not Found')
			return render(request, 'login/reset.html')

	return render(request, 'login/reset.html')

def linkreset(request,poll_id=""):
	allcontext = {
		'poll_id' : poll_id,
		'res' : User.objects.filter(username = poll_id),
	}

	if request.method == 'POST':
		p1 = request.POST.get('pword1')
		p2 = request.POST.get('pword2')
		if p1==p2:
			new_password = request.POST.get('pword1')
			
			try:
				user = User.objects.get(email=poll_id)
				user.set_password(new_password)
				user.save()
				messages.info(request, "Your password has been updated.For any queries, kindly contact the System Administrator at (02) 8888 local 88.")
			except ObjectDoesNotExist:
				messages.info(request, "Nope!")
			
		else:
			messages.info(request, 'Passwords do not match!')


	return render(request, 'login/linkreset.html', allcontext)
