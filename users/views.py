from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request): #create a view for the registration page
    if request.method == 'POST': #check if the request method is POST
        form = UserRegisterForm(request.POST) #create a form instance with the submitted data
        if form.is_valid(): #check if the form is valid
            form.save() #save the form
            username = form.cleaned_data.get('username') #get the username from the form
            messages.success(request, f'Your account has been created! You are now able to log in') #display a success message
            return redirect('login') #redirect the user to the login page
    else: #if the request method is not POST
        form = UserRegisterForm() #create a blank form instance
    return render(request, 'users/register.html', {'form': form}) #render the registration page with the form


@login_required #add the login_required decorator to the profile view
def profile(request): #create a view for the profile page
    if request.method == 'POST': #check if the request method is POST
        u_form = UserUpdateForm(request.POST, instance=request.user) #create a form instance with the submitted data and the current user instance
        p_form = ProfileUpdateForm(request.POST, #create a form instance with the submitted data, files, and the current profile instance 
                                   request.FILES,   #request.FILES is used to handle file uploads in the form 
                                   instance=request.user.profile)    
        if u_form.is_valid() and p_form.is_valid(): #check if both forms are valid 
            u_form.save() #save the user form
            p_form.save() #save the profile form
            messages.success(request, f'Your account has been updated!') #display a success message
            return redirect('profile') #redirect the user to the profile page

    else:
        u_form = UserUpdateForm(instance=request.user) #create a form instance with the current user instance
        p_form = ProfileUpdateForm(instance=request.user.profile)   #create a form instance with the current profile instance

    context = { #create a context dictionary with the user form and profile form 
        'u_form': u_form,  
        'p_form': p_form   
    }

    return render(request, 'users/profile.html', context) #render the profile page with the context dictionary