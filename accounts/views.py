from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, StudentForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from accounts.models import AddressBook, News
from django.contrib.auth.views import logout



def index(request):
  address_book = AddressBook.objects.all()
  context = {
    "students": address_book,
  }
  return render(request, "accounts/home.html",context)

def users(request):
  users = User.objects.all()
  context = {
    "users" : users,
  }
  return render(request, "accounts/users.html", context)


def news(request):
  news = News.objects.all()
  context = { "news" : news,}
  return render(request, 'accounts/news.html', context)


def search(request):
    q = request.GET.get("q")
    if q:
      qS = Student.objects.filter(Q(name__icontains = q) | Q(surname__icontains = q))
      print(qS)
      context = {
        "search" : qS,
      }
      return render(request, "accounts/search.html",context)

def register(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/account/login')
    else:
      form = RegistrationForm()
    args = {'form': form }
    return render(request, 'accounts/reg_form.html', args)


def login_redirect(request):
    if User.is_authenticated:
      return redirect('/account/login')
    else:
      logout(request)
      redirect('/account/home.html')

def create(request):

  form = StudentForm(request.POST or None)
  if form.is_valid():
    student = form.save()
    return redirect('/account')

  return render(request, 'accounts/new.html', {'form': form})


def update(request,id):
  edit = AddressBook.objects.get(id=id)
  form = StudentForm(request.POST or None, instance = edit)
  if form.is_valid():
    student = form.save()
    return redirect('/account/profile')

  return render(request, 'accounts/edit.html', {'form': form, 'edit': edit})

def delete(request,id):
  if request.user.is_staff:
    erase = AddressBook.objects.get(id=id)
    erase.delete()
    return redirect('/account/profile')
  else:
    context = {
      "msg": "You are not admin or staff"
    }
    return render(request, 'accounts/reminder.html', context)

def about(request):
  return render(request, 'accounts/about.html')

def profile(request):
  address_book = AddressBook.objects.all()
  if request.user:
    context = {
    "students": address_book,
  }
  return render(request, 'accounts/profile.html',context)

def news_detail(request,id):
  news = News.objects.get(id=id)
  context = {
     "news": news,
  }

  return render(request, 'accounts/news_detail.html', context)

def logout_views(request):
  logout(request)
  return redirect('/')

def confirm(request, id):
  confirm = AddressBook.objects.get(id=id)
  context = {
    "confirm": confirm
  }
  return render(request, 'accounts/confirm_delete.html',context)

def confirm_edit(request,id):
  confirm = AddressBook.objects.get(id=id)
  context = {
    "confirm": confirm
  }
  return render(request, 'accounts/confirm_update.html',context)

