from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User

def register( request):
    if request.method=='POST':
        username=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get('password')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Userprofile.objects.create(
            user=user,
            phone=phone
        )
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user) 
        return redirect("home")
    return render(request,"register.html")

@login_required
def home(request):
    return render(request, "home.html")


def login(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=authenticate(request,username=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("invalid password or username")
    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect("home")
