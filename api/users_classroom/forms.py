from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.functional import empty
from users_classroom.models import UserProfile

class UserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')
        labels = {
        'password1':'Password',
        'password2':'Confirm Password',
        }
class UserProfileForm(forms.ModelForm):
    teacher = 'teacher'
    student = 'student'
    empty=None
    user_types = [
        (empty, None),
        (student, 'student'),
        (teacher, 'teacher'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfile
        fields = ('UploadPicture', 'user_type')