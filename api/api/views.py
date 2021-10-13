from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import GroupSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer, UserSerializer, LectureSerializer
from .models import User
from .models import Courses
from .models import Lectures

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]
# Create login for the api that will use the retrofit and wil change
# the response. the response has to be exists or invalid to check if login successful!

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/user-list/',
        'User Detail':'/user-detail/<int:id>',
        'Create':'/user-create/',
        'Update':'/user-update/<int:id>',
        'Delete':'/user-delete/<int:id>',
    }
    return Response(api_urls);

@api_view(['GET'])
def showAllUser(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showUser(request, pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Account Created')

@api_view(['POST'])
def updateUser(request, pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['GET'])
def deleteUser(request, pk):
    user=User.objects.get(id=pk)
    user.delete()
        
    return Response('User deleted Successfully')

@api_view(['POST'])
def loginUser(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
        return Response("failed")

    return Response("exist")

#used to login. match the responses with the android code responses!

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response('failed')

        return Response('exist')

@api_view(['POST'])
def createCourse(request):
    serializer=CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Course Created')

@api_view(['GET'])
def showAllCourse(request):
    courses=Courses.objects.all()
    serializer=CourseSerializer(courses,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createLecture(request):
    serializer=LectureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Lecture Created')

@api_view(['GET'])
def showAllLecture(request):
    lectures=Lectures.objects.all()
    serializer=LectureSerializer(lectures,many=True)
    return Response(serializer.data)