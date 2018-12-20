from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50)
    user_phone = models.IntegerField()

    def __str__(self):
        return self.user_name