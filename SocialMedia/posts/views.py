from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import JsonResponse


# Create your views here.
@login_required(login_url='users:login')
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'posts': posts})

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'liked_counts': post.likes.count()})