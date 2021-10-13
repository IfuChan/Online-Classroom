from django.db import models

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=200, null=False,blank=False)
    lname=models.CharField(max_length=200, null=False,blank=False)
    email=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=100,null=False,blank=False)
    userType=models.CharField(max_length=30)
    userimage=models.ImageField(upload_to='imagefile/',null=True,blank=True)

    def __str__(self):
        return self.email

class Courses(models.Model):
    coursename=models.CharField(max_length=200, null=False,blank=False)
    semester=models.CharField(max_length=100, null=False,blank=False)
    desc=models.CharField(max_length=300, null=False,blank=False)

    def __str__(self):
        return self.coursename


class Lectures(models.Model):
   lecturename=models.CharField(max_length=200, null=False,blank=False)

   def __str__(self):
       return self.lecturename
