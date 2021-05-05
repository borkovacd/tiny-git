from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if the user is deleted also delete the profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self): #how we want profile to be displayed
        return f'{self.user.username} Profile'

