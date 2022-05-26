from distutils.command.upload import upload
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Registration(models.Model):
    useremail = models.CharField(max_length=300)
    username = models.EmailField(max_length=300)
    passwords = models.CharField(max_length=300)
    datedadded = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.username

class Carmodels(models.Model):
    modelname = models.CharField(max_length=300)
    dateadded = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Carmodels'

    def __str__(self):
        return self.modelname

class Cars(models.Model):
    carmodel = models.CharField(max_length=200)
    seats = models.IntegerField()
    engines_cc = models.IntegerField()
    fueltype = models.CharField(max_length=200)
    dimension_length = models.FloatField()
    dimension_width = models.FloatField()
    dimension_height = models.FloatField()
    transmision = models.CharField(max_length=200)
    capacity_weight = models.FloatField()
    waranty_years = models.IntegerField()
    price = models.IntegerField()
    dateadded = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return self.fueltype


class CarImages(models.Model):
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE)
    carimages = CloudinaryField('images')
    dateadded = models.CharField()

