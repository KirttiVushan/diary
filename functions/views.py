from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
# Create your views here.
def signin(request):
	if request.method=='GET':
		return render(request, 'functions/signin.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('diary')

			except IntegrityError:
				return render(request, 'functions/signin.html', {'form':UserCreationForm(), 'error':'The username is already taken, try something different'})
		else:
			return render(request, 'functions/signin.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def diary(request):
	return render(request, 'functions/diary.html')