from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from accounts.models import Student


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        )

def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    user.first_name = self.clean_data['first_name']
    user.last_name = self.clean_data['last_name']
    user.email = self.clean_data['email']

    if commit:
        user.save()
    return user

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','midname','surname','address','phone')