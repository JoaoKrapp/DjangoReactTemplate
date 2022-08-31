import json
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import PersonSerializer, NoteSerializer, ImageSerializer
from .models import Person, Profile
from django.core.files import File

def error():
	res = {"code": 400, "message": "Bad Requset"}
	return Response(data=json.dumps(res), status=400)

# Creating custom token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		
		# Add custom claims
		token['username'] = user.username
		
		return token


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


# Create your views here.

class PersonView(generics.CreateAPIView):
	"""Generic api from rest framework
    """
	queryset = Person.objects.all()
	serializer_class = PersonSerializer


@api_view(['GET'])
def test(request):
	"""Base model that you can use as an example to create api's

    Args:
        request (request): Request methos, in @api_view will specify what methos is able to run this function, could be GET, POST, DELETE, PUT

    Returns:
        JSON: A look a like response from Javascript, basically a JSON file
    """
	testing = {
		"LMAO": 123
	}
	return Response(testing)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	""" TODO : This is a example of model to user, please dont use that in production!
	"""
	user = request.user
	
	notes = user.note_set.all()
	serializer = NoteSerializer(notes, many=True)
	return Response(serializer.data)
	
# Important api's here

@api_view(['POST'])
def sign_up(request):
	"""_summary_

	Args:
		request (_type_): _description_

	Returns:
		_type_: _description_
	"""

	# Get informations

	username = request.data['username']
	if not username:
		return error()

	password = request.data['password']
	if not password:
		return error()

	confirm_password = request.data['confirm_password']
	if not confirm_password:
		return error()

	# Verify information

	existing_username = User.objects.filter(username=username)

	# Already exist a user with that username

	if len(existing_username) != 0:
		return error()

	# Verify if the passwords are equal



	if confirm_password != password:
		print(confirm_password)
		print(password)
		return error()

	# Create new user

	print(existing_username)

	user = User.objects.create_user(username=username,password=password)
	user.save()
	
	res = {"code": 200, "message": "Success"}
	return Response(data=json.dumps(res), status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_avatar(request):
	
	print(request.FILES['file'])

	avatar = request.FILES['file']
	user = request.user

	new_profile = Profile.objects.create(user=user,avatar=avatar)
	new_profile.save()

	res = {"code": 200, "message": "Success"}
	return Response(data=json.dumps(res), status=200)
