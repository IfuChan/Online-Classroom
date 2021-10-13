from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users_classroom.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Note

# Create your views here.
def index(request):
    return render (request, 'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not avaiable")
        else:
            return HttpResponse("Enter your correct password or username or both")

    else:
        return render(request, 'users_classroom/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_rec(request):  
    return render(request, 'users_classroom/audiorec.html')  

def register(request):
    
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users_classroom/registration.html', {'registered':registered,
                            'user_form':user_form, 'profile_form':profile_form})


@login_required
def note(request):
    if request.method == 'POST':
        title = request.POST['note-title']
        details = request.POST['note-text']

        note = Note.objects.create(title=title, details=details)
        note.save()
        return render (request, 'home.html')
    else:
        return render (request, 'home.html')

@login_required
def notes(request):  

    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'users_classroom/notes.html', context) 