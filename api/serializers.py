from rest_framework import serializers
from api.models import Registration,Carmodels,Cars,CarImages

class RegistrationSerializer(serializers.ModelSerializer):
    model = Registration
    fields = ["useremail","username","datedadded","is_active"]

class CarmodelsSerializer(serializers.ModelSerializer):
    model = Carmodels
    fields = ["modelname","dateadded"]

class CarsSerializer(serializers.ModelSerializer):
    model = Cars
    fields = ["carmodel","seats","engines_cc","fueltype","dimension_length","dimension_width","dimension_height","transmision","capacity_weight","waranty_years","price","dateadded"]

class CarImagesSerializer(serializers.ModelSerializer):
    model = CarImages
    fields = ["car_id","carimages","dateadded"]