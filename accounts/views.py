from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, StudentForm
from django.contrib.auth.models import User
from django.db import models
from accounts.models import Student
from . import forms


def home(request):
  qs = request.GET.get("q")
  query = Student.objects.filter(name=qs)
  students = Student.objects.all()
  
  args = {
  'query': query,
  'students': students
  }
  return render(request, 'accounts/home.html',args)



def register(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/account')
    else:
      form = RegistrationForm()
    args = {'form': form }
    return render(request, 'accounts/reg_form.html', args)


def login_redirect(request):
    return redirect('/account/login')

def create(request):

  form = StudentForm(request.POST or None)
  if form.is_valid():
    student = form.save()
    return redirect('/account')

  return render(request, 'accounts/new.html', {'form': form})


def update(request,id):
  edit = Student.objects.get(id=id)
  form = StudentForm(request.POST or None, instance = edit)
  if form.is_valid():
    student = form.save()
    return redirect('/account')

  return render(request, 'accounts/edit.html', {'form': form, 'edit': edit})

def delete(request,id):
  erase = Student.objects.get(id=id)
  erase.delete()
  return redirect('/account')

def about(request):
  return render(request, 'accounts/about.html')

def profile(request):
  return render(request, 'accounts/profile.html')


  

