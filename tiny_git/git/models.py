from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    git_repository = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #if the user is deleted also delete the project

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
