from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, StudentForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from accounts.models import AddressBook, News
from django.contrib.auth.views import logout
from django.views import View


class IndexView(View):
  def get(self,request):
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

class NewsView(View):
  def get(self,request):
    news = News.objects.all()
    context = { "news" : news,}
    return render(request, 'accounts/news.html', context)

class SearchView(View):
  def get(self,request):
    q = request.GET.get("q")
    if q:
      qS = AddressBook.objects.filter(Q(first_name__icontains = q) | Q(last_name__icontains = q))
      context = {
        "search" : qS,
      }
      return render(request, "accounts/search.html",context)

class RegisterView(View):
  form_class = RegistrationForm
  template_name = 'accounts/reg_form.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class()
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/account/login')


def login_redirect(request):
    if User.is_authenticated:
      return redirect('/account/login')
    else:
      logout(request)
      redirect('/account/home.html')

class CreateView(View):
  form_class = StudentForm
  template_name = 'accounts/new.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class()
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    form =self.form_class(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('/account')


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

class ProfileView(View):
  def get(self,request):
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

