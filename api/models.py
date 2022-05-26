from django.db import models

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