from django import forms
from django import forms
from django.db.models import fields
from .models import Semester, askQuestion, lecture, Course

class lectureForm(forms.ModelForm):
    class Meta:
        model = lecture
        # fields = ('leectureName', 'name', 'position', 'pdf')
        fields = ('__all__')

class courseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')

class questionForm(forms.ModelForm):
    class Meta:
        model = askQuestion
        fields = ['comment_box',]
        labels = {'comment_box': 'ask question'}