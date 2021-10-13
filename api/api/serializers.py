from rest_framework import serializers
from users_classroom.models import UserProfile
from django.contrib.auth.models import User, Group
from .models import User,Courses,Lectures

# class UserProfileSerializer(serializers.Serializer):
    
#     user = serializers.CharField()
#     user_type = serializers.CharField(max_length=10)

#     def create(self, validated_date):
#         return UserProfile.objects.create(validated_date)

#     def update(self, instance, validated_date):
#         instance.user = validated_date.get('user', instance.user)
#         instance.user_type = validated_date.get('user', instance.user_type)
#         instance.save()
#         return instance

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectures
        fields = '__all__'