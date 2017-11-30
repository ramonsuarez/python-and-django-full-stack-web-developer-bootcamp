from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneFiled(User)

    # Additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # Method to print out user
    def __str__(self):
        return self.user.username
    
