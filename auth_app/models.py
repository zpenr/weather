from django.db import models

class Users(models.Model):
    ID = models.IntegerField(primary_key=True)
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)