from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class Posts(models.Model):
    title =  models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title