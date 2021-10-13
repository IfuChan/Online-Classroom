from django.contrib import admin
from courseMaterials.models import Semester, Course, askQuestion, lecture


# Register your models here.

admin.site.register(Semester),
admin.site.register(Course),
admin.site.register(lecture),
admin.site.register(askQuestion),