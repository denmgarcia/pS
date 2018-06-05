from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.db import models
from accounts.models import Student



def home(request):
  qs = request.GET.get("q")
  students = Student.objects.all()
  query = Student.objects.filter(name=qs)
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


def update(request):
  pass

def delete(request):
  pass

