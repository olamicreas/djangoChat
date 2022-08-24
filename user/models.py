from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics ')
    friend = models.ManyToManyField(User, related_name='my_friends', blank=True)

    def __str__(self):
        return self.user.username
    


class Friends(models.Model):
    users = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE, db_constraint=False)
    userss = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE, db_constraint=False)
   
    

    def __str__(self):
        return f' {self.users} added {self.userss}'


