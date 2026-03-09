from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


@login_required     
def student_detail(request):
    if request.method=='POST':
        percentile = request.POST.get("percentile")
        category = request.POST.get("category")
        home_university = request.POST.get("home_university")
        preferred_branch_id = request.POST.get("preferred_branch")
        
        
        if not all([percentile, category, home_university, preferred_branch_id]):
            messages.error(request, "Please fill all fields")
            return redirect("home")
        
        
        userprofile,created = Userprofile.objects.get_or_create(user=request.user)
        
        preferred_branch = Branch.objects.get(id=preferred_branch_id)
        
        
        
        student = Student.objects.create(
            user=userprofile,
            percentile=float(percentile),
            category=category,
            home_university=home_university,
            preferred_branch=preferred_branch
        )
        messages.success(request, "Student details saved successfully!")
        return redirect("register")
      
    branches = Branch.objects.all()

    return render(request,"student.html", {
        "branches": branches,
        "categories": Student.CATEGORY_CHOICES
    })