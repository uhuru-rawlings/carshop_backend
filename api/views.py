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