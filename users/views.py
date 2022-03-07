from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm
# Create your views here.

def loginUser(request):
    page = 'register'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username = username)
        except:
            messages.error(request, 'UserName does not exist')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
           messages.error(request, 'Username or Pass incorrect')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was successfully logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')
            
        else:
            messages.error(request, 'An error has occurred!')


    context = {'page': page, 'form': form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    profilesOBJ = Profile.objects.all()
    context = {'profiles':  profilesOBJ}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profileOBJ = Profile.objects.get(id = pk)
    topSkills = profileOBJ.skill_set.exclude(description__exact = "")
    otherSkills = profileOBJ.skill_set.filter(description = "")
    context = {'profile':  profileOBJ, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)