from django import forms 
from app.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control my-2', 
        'placeholder': "Enter Username*"
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control my-2 ', 
        'placeholder': " Your Email*"
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control my-2 ', 
        'placeholder': " Enter Password*"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control my-2 ', 
        'placeholder': ""
    }))
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']



