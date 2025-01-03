from django.db.models.signals import post_save   #import the post_save signal 
from django.contrib.auth.models import User     #import the User model 
from django.dispatch import receiver  #import the receiver decorator   
from .models import Profile #import the Profile model 

@receiver(post_save, sender=User) #create a receiver for the post_save signal 
def create_profile(sender, instance, created, **kwargs): #create a function that creates a profile for a user 
    if created: #check if the user is created 
        Profile.objects.create(user=instance) #create a profile for the user 
        
@receiver(post_save, sender=User) #create a receiver for the post_save signal
def save_profile(sender, instance, **kwargs): #create a function that saves the profile for a user 
    instance.profile.save() #save the profile for the user 