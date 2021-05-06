from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if the user is deleted also delete the profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self): #how we want profile to be displayed
        return f'{self.user.username} Profile'

    def save(self): #overriding save method
        super().save()

        img = Image.open(self.image.path) #open the image of the current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
