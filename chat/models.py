from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile



class Chat(models.Model):
    
    body = models.TextField()
    files = models.FileField(upload_to='uploads/', blank=True)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    date_posted = models.TimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} sent a message'

    class Meta:
        ordering = ['date_posted']





    
    

   
