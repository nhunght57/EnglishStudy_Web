from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
import datetime
from django.utils import timezone
from django.db.models.fields import IntegerField

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='profile')

    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    birthday = models.DateField(default=datetime.date(1994, 1, 1))
    home = models.CharField(default='Hanoi', max_length=200)
    score_of_the_last_test = IntegerField(default=0)
    total_score = IntegerField(default=0)
    REQUIRED_FIELDS = ['birthday', 'home', 'Score of the last tests', 'Total score']

    # Override the __str__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
