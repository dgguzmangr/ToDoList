from authApp.models.persons import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['person_id', 'name', 'last_name']