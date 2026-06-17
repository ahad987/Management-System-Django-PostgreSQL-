from django.shortcuts import render, redirect
from AuthenticationApp.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def singup_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:            
            user = AuthenticationModule.objects.create_user(
                username = username,
                email = email,
                password = password
            )            
            return redirect('singin')
    
    return render(request, 'signup.html')

def singin_view(request):
    
    if request.method == 'POST':
        
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        
        user = authenticate(username = user_name, password = pass_word)
        
        if user:
            login(request, user)
            
            return redirect('home')
    
    return render(request, 'signin.html')

@login_required
def home_view(request):
    
    return render(request, 'home.html')

@login_required
def signout_view(request):
    
    logout(request)
    
    return redirect('signin')