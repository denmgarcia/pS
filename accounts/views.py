from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, StudentForm
from django.contrib.auth.models import User
from django.db.models import Q
from accounts.models import AddressBook, News
from django.contrib.auth.views import logout
from django.views import View


class IndexView(View):
    def get(self, request):
        address_book = AddressBook.objects.all()
        context = {"students": address_book, }
        return render(request, "accounts/home.html", context)


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        context = {"news": news, }
        return render(request, 'accounts/news.html', context)


class SearchView(View):
    def get(self, request):
        q = request.GET.get("q")
        if q:
            qS = AddressBook.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
            context = {"search": qS, }
            return render(request, "accounts/search.html", context)
        elif q == "":
            return render(request, "accounts/notfound.html")


class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'accounts/reg_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')


class LoginRedirect(View):
    def get(self, request):
        if User.is_authenticated:
            return redirect('/account/login')
        else:
            logout(request)
            redirect('/account/home.html')


class CreateView(View):
    form_class = StudentForm
    template_name = 'accounts/new.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/account')


class UpdateView(View):
    form_class = StudentForm
    template_name = 'accounts/edit.html'

    def post(self, request, id):
        edit = AddressBook.objects.get(id=id)
        form = StudentForm(request.POST or None, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    def get(self, request, id):
        edit = AddressBook.objects.get(id=id)
        form = self.form_class(instance=edit)
        return render(request, self.template_name, {'form': form, 'edit': edit})


class DeleteView(View):
    def get(self, request):
        if request.user.is_staff:
            erase = AddressBook.objects.get(id=id)
            erase.delete()
            return redirect('/account/profile')
        else:
            context = {
                "msg": "You are not admin or staff"
            }
            return render(request, 'accounts/reminder.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'accounts/about.html')


class ProfileView(View):
    def get(self, request):
        address_book = AddressBook.objects.all()
        if request.user:
            context = {
                "students": address_book}
            return render(request, 'accounts/profile.html', context)


class NewsDetailView(View):
    def get(self, request, id):
        news = News.objects.get(id=id)
        context = {
            "news": news
        }
        return render(request, 'accounts/news_detail.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class ConfirmView(View):
    def get(self, request, id):
        confirm = AddressBook.objects.get(id=id)
        context = {
            "confirm": confirm
        }
        return render(request, 'accounts/confirm_delete.html', context)


class ConfirmEdit(View):
    def get(self, request, id):
        confirm = AddressBook.objects.get(id=id)
        context = {
            "confirm": confirm,
        }
        return render(request, 'accounts/confirm_update.html', context)
