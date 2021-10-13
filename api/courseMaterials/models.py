from django.db import models
from django.template.defaultfilters import slugify, truncatechars
import os
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Semester(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Semester name', blank=False)
    semID = models.IntegerField(max_length=3,unique=True, verbose_name= 'Semester ID', blank=False)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        

def courseImage(instance, filename):
        upload_to = 'Images/'
        ext = filename.split('.')[-1]
        if instance.courseId:
         filename = 'Course_Pictures/{}.{}'.format(instance.courseId, ext)
         return os.path.join(upload_to, filename)
        

class Course(models.Model):
    courseId = models.CharField(max_length=30, unique=True, verbose_name='Course ID')
    name = models.CharField(max_length=50, verbose_name='Course Name')
    code = models.CharField(max_length=6, blank=False, unique= True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to=courseImage, blank=True, verbose_name='Course Image')
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.courseId)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_view', kwargs={'slug':self.semester.slug})

def chapterFles(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.leectureName:
        filename = 'ChapterFiles/{}/{}.{}'.format(instance.leectureName,instance.leectureName, ext)
        if os.path.exists(filename):
            new_name = str(instance.leectureName) + str('newCopy')
            filename =  'chapterFiles/{}/{}.{}'.format(instance.leectureName,new_name, ext)
        return os.path.join(upload_to, filename)

class lecture(models.Model):
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    leectureName = models.CharField(max_length=50,verbose_name='Lecture/File Name', blank=False, unique=True)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', related_name='lectures')
    name = models.CharField(max_length=20, verbose_name='Name')
    position = models.PositiveSmallIntegerField(verbose_name="Chapter Number:")
    pdf = models.FileField(upload_to=chapterFles, verbose_name="Upload PDF Files", blank=True)
    slug = models.SlugField(null=True, blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Faculty Name')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lecture_view', kwargs={'slug':self.subject.slug, 'semester':self.Semester.slug})
    
class askQuestion(models.Model):
    lecture_name = models.ForeignKey(lecture, on_delete=models.CASCADE, null=True, related_name='askquestions')
    question_name = models.CharField(max_length=60, blank=True)
    comment_box = models.TextField(max_length=300, blank= True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_question = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.question_name = slugify("question asked by:"+ str(self.user_name)+ "date:" +str(self.date_of_question))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_of_question']