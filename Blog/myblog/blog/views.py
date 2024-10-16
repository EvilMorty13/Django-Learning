from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})