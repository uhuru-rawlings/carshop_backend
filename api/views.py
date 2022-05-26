from django.shortcuts import render
from api.models import Registration,Carmodels,Cars,CarImages
from api.serializers import RegistrationSerializer,CarmodelsSerializer,CarsSerializer,CarImagesSerializer
from django.contrib.auth.hashers import make_password,check_password
import jwt,datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def registration_view(request):
    details = request.data
    useremail = details['useremail']
    username = details['username']
    passwords = details['passwords']

    checkuser = Registration.objects.filter(useremail = useremail)
    if checkuser.exists():
        return Response({"error":"user with these details already exist"})
    else:
        new_user = Registration(useremail = useremail,username = username,passwords = make_password(passwords))
        new_user.save()
        return Response({"success":"user added successfully."})

@api_view(['POST'])
def resetpassword_view(request):
    details = request.data
    useremail = details['useremail']
    passwords = details['passwords']

    checkuser = Registration.objects.filter(useremail = useremail)
    if checkuser.exists():
        checkuser = Registration.objects.get(useremail = useremail)
        checkuser.passwords = make_password(passwords)
        checkuser.save()
        return Response({"success":"password reset successfully."})
    else:
        return Response({"error":"Wrong useremail provided."})

@api_view(['POST'])
def login_view(request):
    details = request.data
    useremail = details['useremail']
    passwords = details['passwords']

    checkuser = Registration.objects.filter(useremail = useremail)
    if checkuser.exists():
        checkuser = Registration.objects.get(useremail = useremail)
        if check_password(passwords, checkuser.passwords):
            payload = {
                'id': checkuser.id,
                'useremail':checkuser.useremail,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
            return Response({"token":token})
        else:
            return Response({"error":"wrong password, try again."})
    else:
        return Response({"error":"Wrong useremail provided."})

@api_view(['GET'])
def carmodels_view(request):
    models = Carmodels.objects.all()

    if models:
        serialize = CarmodelsSerializer(models, many = True)
        return Response(serialize.data)
    else:
        return Response([])

@api_view(['GET'])
def cars_view(request):
    cars = Cars.objects.all()

    if cars:
        serialize = CarsSerializer(cars, many = True)
        return Response(serialize.data)
    else:
        return Response([])

@api_view(['GET'])
def carsimages_view(request):
    carimages = CarImages.objects.all()

    if carimages:
        serialize = CarImagesSerializer(carimages, many = True)
        return Response(serialize.data)
    else:
        return Response([])