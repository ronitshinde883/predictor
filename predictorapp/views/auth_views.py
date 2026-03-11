from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
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


def login_view(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user_obj=User.objects.get(email=email)
        user=authenticate(request,username=user_obj.username,password=password)
        
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            return HttpResponse("invalid password or username")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")
