from rest_framework.serializers import Serializer
from api.models import Registration,Carmodels,Cars,CarImages

class RegistrationSerializer(Serializer.ModelSerializer):
    model = Registration
    fields = ["useremail","username","datedadded","is_active"]

class CarmodelsSerializer(Serializer.ModelSerializer):
    model = Carmodels
    fields = ["modelname","dateadded"]

class CarsSerializer(Serializer.ModelSerializer):
    model = Cars
    fields = ["carmodel","seats","engines_cc","fueltype","dimension_length","dimension_width","dimension_height","transmision","capacity_weight","waranty_years","price","dateadded"]

class CarImagesSerializer(Serializer.ModelSerializer):
    model = CarImages
    fields = ["car_id","carimages","dateadded"]