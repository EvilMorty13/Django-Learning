from django.shortcuts import render,redirect
from .models import Post,Profile
from .forms import PostForm,ProfileUpdateForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,get_user
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
# Create your views here.


def home(request):
    us = request.user
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts,'us':us})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user
            post.save()  
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})


def register(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST) 
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('home') 
    else:
        form = UserCreationForm() 
    
    return render(request, 'blog/register.html', {'form': form}) 



def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'blog/profile.html', {'profile': profile})


@login_required
def profile_update(request, username):
    # Ensure the user can only update their own profile
    if request.user.username != username:
        return redirect('profile', username=request.user.username)

    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username)
    else:
        form = ProfileUpdateForm(instance=user.profile)

    return render(request, 'blog/profile_update.html', {'form': form, 'user': user})
