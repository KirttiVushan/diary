from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout , authenticate
from .forms import Content_field
from .models import Diary
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def home(request):
	return render(request, 'functions/home.html')


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

@login_required
def diary(request):
	diary=Diary.objects.filter(user=request.user).order_by('-dateaccessed')
	return render(request, 'functions/diary.html', {'diary':diary})


@login_required
def logout_user(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')


def login_user(request):
	if request.method=='GET':
		return render(request, 'functions/login_user.html', {'form':AuthenticationForm()})
	else:
		user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'functions/login_user.html', {'form':AuthenticationForm(), 'error': 'No username registered'})
		else:
			login(request, user)
			return redirect('diary')


@login_required
def new(request):
	if request.method=='GET':
		return render(request, 'functions/new.html', {'form':Content_field()})
	else:
		form= Content_field(request.POST)
		profile=form.save(commit=False)
		profile.user=request.user
		profile.save()
		return redirect('diary')

@login_required
def viewdiary(request, diary_pk):
	diarys=get_object_or_404(Diary, pk=diary_pk, user=request.user)
	if request.method=='GET':
		form=Content_field(instance=diarys)
		return render(request, 'functions/viewdiary.html', {'diarys':diarys , 'form':form})
	else:
		try:
			form=Content_field(request.POST ,instance=diarys)
			diarys.dateaccessed=timezone.now()
			form.save()
			return redirect('diary')
		except ValueError:
			return render(request, 'functions/viewdiary.html', {'diarys':diarys , 'form':form , 'error':'bad info'})


@login_required
def delete_diary(request, diary_pk):
	diary=get_object_or_404(Diary, pk=diary_pk, user=request.user)
	if request.method=='POST':
		diary.delete()
		return redirect('diary')




def about(request):
	return render (request, 'functions/about.html')