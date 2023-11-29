from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

@login_required
def timeline(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('timeline')
    else:
        form = PostForm()
    
    posts = Post.objects.all().order_by('-created_at') # Order by creation time in descending order

    return render(request, 'timeline.html', {'form': form, 'posts': posts})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'menu/profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'menu/profile.html', {"profile":profile})
    else:
        messages.success(request, ("Please Log In Or Sign Up To View This Page"))
        return redirect('home')


def account_settings(request):
    return render(request, 'menu/account_settings.html')


# account settings
@login_required
def edit_posts(request):
    return render(request, 'menu/account/edit_posts.html')

@login_required
def edit_profile(request):
    return render(request, 'menu/account/edit_profile.html')

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        user_profile.delete()
        request.user.delete()  
        logout(request)  
        messages.success(request, "Your profile has been deleted.")
        return redirect('home')  
    else:
        return render(request, 'menu/account/delete_profile.html')


# nav menu

@login_required
def account_settings(request):
    return render(request, 'menu/account_settings.html')

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'menu/profile_list.html', {"profiles": profiles}) 

