from django.db import models
#model was created for student and must be changed for teacher as well
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=55, null=False, blank=False)
    email=models.CharField(max_length=100, null=False, blank=False)
    password=models.CharField(max_length=35)

    def __str__(self):
        return self.name