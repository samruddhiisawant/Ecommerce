from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from customer.models import *
   
 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class ContactUsform(forms.ModelForm):
    class  Meta:
        model = Contact_us
        fields ="__all__"
        exclude=[]
        