from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post 
from .forms import PostForm

def all_post(request):
    all_posts = Post.objects.filter(active=True)
    context = {
        'all_posts' : all_posts
    }
    
    return render(request , 'all_posts.html' , context)
    


def post(request , id ):
    post = Post.objects.get(id=id)
   
    context = {
        'post' : post
    }
    return render(request , 'details.html', context)

def create_post(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    

    context = {
        'form' : form , 
    }

    return render(request , 'create.html' , context)


def edit_post(request , id):
    post = get_object_or_404(post , id = id)
    if(request.method == 'POST'):
        form = PostForm(request.POST , instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    

    context = {
        'form' : form , 
    }

    return render(request , 'edit.html' , context)
