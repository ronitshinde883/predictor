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
        user_id = request.POST.get("user_id")
        percentile = request.POST.get("percentile")
        category = request.POST.get("category")
        home_university = request.POST.get("home_university")
        preferred_branch_id = request.POST.get("preferred_branch")
        
        
        if not all([user_id, percentile, category, home_university, preferred_branch_id]):
            messages.error(request, "Please fill all fields")
            return redirect("home")
        
        try:
            user = Userprofile.objects.get(id=user_id)
        except Userprofile.DoesNotExist:
            messages.error(request, "User not found")
            return redirect("home")
        
        try:
            preferred_branch = Branch.objects.get(id=preferred_branch_id)
        except Branch.DoesNotExist:
            messages.error(request, "Invalid branch selected")
            return redirect("home")
        
        
        student = Student.objects.create(
            user=user,
            percentile=float(percentile),
            category=category,
            home_university=home_university,
            preferred_branch=preferred_branch
        )
        
        return JsonResponse({
            "message": f"Student {user.name} saved successfully!",
            "student_id": student.id
        })
        
    branches = Branch.objects.all()

    return render(request,"student.html", {
        "branches": branches,
        "categories": Student.CATEGORY_CHOICES
    })