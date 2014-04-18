from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


# Create your models here.
from django.db.models.fields import IntegerField


class UserProfile(AbstractBaseUser):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    birthday = models.DateField(default='22/8/1994')
    home = models.CharField(default='ha noi',max_length= 200)
    Score_of_the_last_test = IntegerField(default=10)
    Total_score = IntegerField(default=10)
    REQUIRED_FIELDS = ['birthday','home','Score of the last test','Total score']
    # Override the __str__() method to return out something meaningful!
    def __str__(self):
        return self.user.username




