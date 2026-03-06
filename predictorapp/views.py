from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
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

        login(request, user)
        return redirect("home")
    return render(request,"register.html")

@login_required
def home(request):
    return render(request, "home.html")
@login_required
def predict_college( request, student_id):
    student = Student.objects.get(id=student_id)
    colleges=Cutoff.objects.filter(
        category=student.category,
        year=2026,
        branch=student.preferred_branch,
        percentile__lte=student.percentile,
    ).select_related("college", "branch").order_by("-percentile")
    return render(request, "predict.html", {"colleges": colleges})
    data = []

    for c in colleges:
        data.append({
            "college": c.college.name,
            "branch": c.branch.name,
            "cutoff": c.percentile,
            "year": c.year
        })

    return JsonResponse({"results": data})

@login_required
def cutoff_explorer(request, college_id, branch_id, year, category):
    college_id=request.GET.get("college")
    branch_id=request.GET.get("branch")
    year=request.GET.get("year")
    category=request.GET.get("category")
    
    cutoffs= Cutoff.objects.filter(
        college_id=college_id,
        branch_id=branch_id,
        year=year,
        category=category
    )
    data=[]
    for c in cutoffs:
        data.append({
            "college":c.college.name,
            "branch": c.branch.name,
            "year": c.year,
            "category": c.category,
            "round": c.round,
            "percentile": c.percentile,
        })
    return JsonResponse({"result":data})
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
@login_required 
def cutoff_explorer_page(request):
    colleges = College.objects.all()
    branches = Branch.objects.all()

    return render(request, "cutoff_explorer.html", {
        "colleges": colleges,
        "branches": branches,
        "categories": Cutoff.CATEGORY_CHOICES
    })

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Invalid username or password")

    return render(request, "login.html")