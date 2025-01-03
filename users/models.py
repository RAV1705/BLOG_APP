from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #create a one-to-one relationship with the User model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #store the profile pictures in the profile_pics directory 

    def __str__(self): #define the string representation of the Profile model
        return f'{self.user.username} Profile' #return the username of the user and the word 'Profile'

    def save(self): #override the save method of the Profile model 
        super().save() #call the save method of the parent class

        img = Image.open(self.image.path) #open the image of the current instance

        if img.height > 300 or img.width > 300: #check if the height or width of the image is greater than 300 pixels
            output_size = (300, 300) #set the output size to 300x300 pixels
            img.thumbnail(output_size) #resize the image to the output size
            img.save(self.image.path) #save the resized image to the same path