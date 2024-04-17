from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='users:login')
def all_posts(request):
    return render(request, 'posts/all_posts.html')