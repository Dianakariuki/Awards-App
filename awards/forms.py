from .models import Projects,Rates,Comments,Profile,User 
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User 

class PostForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude=['user','design','usability','content']

class RateForm(forms.ModelForm):
    class Meta:
        model=Rates
        exclude=['user','project']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','pro_id']

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ["username","email","password1","password2"]