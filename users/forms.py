from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): #create a form that inherits from the UserCreationForm
    email = forms.EmailField() #add an email field to the form

    class Meta: #define the metadata of the form
        model = User #set the model of the form to the User model
        fields = ['username', 'email', 'password1', 'password2'] #set the fields of the form to the username, email, password1, and password2
 

class UserUpdateForm(forms.ModelForm): #create a form that inherits from the ModelForm
    email = forms.EmailField()  #add an email field to the form

    class Meta: #define the metadata of the form
        model = User #set the model of the form to the User model
        fields = ['username', 'email'] #set the fields of the form to the username and email


class ProfileUpdateForm(forms.ModelForm): #create a form that inherits from the ModelForm
    class Meta: #define the metadata of the form
        model = Profile #set the model of the form to the Profile model
        fields = ['image'] #set the fields of the form to the image