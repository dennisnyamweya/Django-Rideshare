from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=20)
    pickup = models.CharField(max_length=20)
    nid = models.IntegerField()
    gender = models.CharField(max_length=50,choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def _str_(self):
        return self.name