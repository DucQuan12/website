from django.db import models
from django.contrib.auth.admin import User, Group
from django.utils import timezone

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    content = models.TextField(max_length=1000, blank=True, null=False)
    image = models.ImageField(upload_to='upload/', null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

