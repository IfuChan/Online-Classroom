from django.db import models
from django.contrib.auth.models import User
import os

from django.utils.functional import empty

# Create your models here.

def PicPath(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'ProfilePics/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfile(models.Model):
    
    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    UploadPicture = models.ImageField(upload_to=PicPath, verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    empty= None
    user_types = [
        (empty,None),
        (teacher, 'teacher'),
        (student, 'student'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=empty)

    def __str__(self):
        return self.user.username

class Note(models.Model):
    title = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title