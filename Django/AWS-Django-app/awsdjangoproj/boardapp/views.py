from django.shortcuts import render, redirect
from boardapp.models import *
from django.db.models import Count
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse

def main_page(request):
    return render(request, 'main.html')

def user_register_page(request):
    return render(request, 'user_register.html')

def user_register_idcheck(request):
	if request.method == "POST":
		username = request.POST['username']
	else:
		username = ''

	idObject = User.objects.filter(username__exact=username)
	idCount = idObject.count()

	if idCount > 0:
		msg = "<font color='red'>이미 존재하는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=0 />"
	else:
		msg = "<font color='blue'>사용할 수 있는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=1 />"

	return HttpResponse(msg)

def user_register_result(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		last_name = request.POST['last_name']
		phone = request.POST['phone']
		email = request.POST['email']
		birth_year = int(request.POST['birth_year'])
		birth_month = int(request.POST['birth_month'])
		birth_day = int(request.POST['birth_day'])

	try:
		if username and User.objects.filter(username__exact=username).count() == 0:
			date_of_birth = datetime(birth_year, birth_month, birth_day)

			user = User.objects.create_user(
				username, password, last_name, email, phone, date_of_birth
			)

			redirection_page = '/boardapp/user_register_completed/'
		else:
			redirection_page = '/boardapp/error/'
	except:
		redirection_page = '/boardapp/error/'

	return redirect(redirection_page)

def user_register_completed(request):
	return render(request,  'user_register_completed_page.html')