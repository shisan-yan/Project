from django.db import models
from django.contrib.auth.forms import User
# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=40)
    mail = models.EmailField(max_length=200)

    def __str__(self):
        return self.name