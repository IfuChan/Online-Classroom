from rest_framework import serializers
from .models import Student

#create another view for the user rather than the student!

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'