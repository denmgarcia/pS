from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User


def home(request):
    users = User.objects.all()
    for user in users:
      args = {
        'user': user,
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
