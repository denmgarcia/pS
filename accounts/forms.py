from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from accounts.models import AddressBook


class StudentForm(forms.ModelForm):
    class Meta:
        model = AddressBook
        fields = ('first_name','last_name','phone','address')


from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Username", "required":"autofocus"})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password","required":"autofocus"})) 


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Email", "required":"autofocus"}) )
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Username", "required":"autofocus"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "First Name", "required":"autofocus"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Last Name", "required":"autofocus"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password","required":"autofocus"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Confirm Password","required":"autofocus"}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')




def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    user.first_name = self.clean_data['first_name']
    user.last_name = self.clean_data['last_name']
    user.email = self.clean_data['email']

    if commit:
        user.save()
    return user