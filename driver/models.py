from django.db import models
from django.utils.timezone import datetime
# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    car = models.CharField(max_length=20)
    pickup = models.CharField(max_length=20)
    nid = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)

class Car(models.Model):
    seats = models.CharField(max_length=20)
    plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)


class Location(models.Model):
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=datetime.now)