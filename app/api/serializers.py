from dataclasses import field
import imp
from rest_framework import serializers
from . import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id', 'code', 'name')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = '__all__'