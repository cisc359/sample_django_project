from django.db import models

# Create your models here.


class ZipCode(models.Model):
    zip = models.CharField(max_length=5, default='')
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    st_abbr = models.CharField(max_length=50)




class Weather(models.Model):

    temperature = models.FloatField
    humidity = models.FloatField
    windspeed = models.FloatField
    updated_time = models.DateTimeField

    # def __init__(self, updated_time, temperature, humidity, windspeed):
    #     self.updated_time = updated_time
    #     self.temperature = temperature
    #     self.humidity = humidity
    #     self.windspeed = windspeed