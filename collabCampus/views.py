from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def Home(request):
    return render(request,'home.html')

def login_user(request):
    # CHECK TO SEE IF LOGGING IN 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # AUTHENTICATE USER 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged in!")
            return redirect('home')
        else:
            messages.success(request,"ERROR LOGGING IN. PLEASE TRY AGAIN...")
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
              form.save()
              # AUTHENTICATE AND LOGIN
              username = form.cleaned_data['username']
              password = form.cleaned_data['password1']
              user = authenticate(username=username,password=password)
              login(request,user)
              messages.success(request,"successfully registered")
              return redirect('home')
    else:
         form = SignUpForm()  
         return render(request,'register.html',{
              'form': form
         })
    
    return render(request,'register.html',{
              'form': form
         })