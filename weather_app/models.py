from django.db import models

class Locations(models.Model):
    Name = models.CharField(max_length=50)
    UserId = models.IntegerField()
    Latitude = models.DecimalField(max_digits=5, decimal_places=2)
    Longitude = models.DecimalField(max_digits=5, decimal_places=2)