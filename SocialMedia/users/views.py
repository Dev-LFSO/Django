from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_user = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(Q(email=email_user))
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email_user, password=password)
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get("next"))
            return redirect('home')
        return render(request, 'users/register.html', {'error': 'User already exists'})
        
        
    return render(request, 'users/register.html')

def login_view(request):
    if request.user.is_authenticated:
        if request.GET.get('next'):
            return redirect(request.GET.get("next"))
        return redirect('home')
    if request.method == 'POST':
        try:
            user = User.objects.get(Q(email=request.POST.get('email')))
            password = request.POST.get('password')

            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                if request.user.is_authenticated:
                    if request.GET.get('next'):
                        return redirect(request.GET.get("next"))
                    return redirect('home')
            return render(request, 'users/login.html', {'error': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    if request.GET.get('next'):
        return redirect(request.GET.get("next"))
    return redirect('home')