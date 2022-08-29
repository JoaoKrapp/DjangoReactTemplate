from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import PersonSerializer, NoteSerializer
from .models import Person, Note

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
    testando = {
        "LMAO" : 123
    }
    return Response(testando)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)