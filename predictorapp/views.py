from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
# Create your views here.
def home(request):
    return HttpResponse('hello i am ronit')

def register(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get('password')
        
        Userprofile.object.create(
            name=name,
            email=email,
            phone=phone,
        )

# 
def student_detail(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        cet_percentile = request.POST.get("cet_percentile")
        category = request.POST.get("category")
        home_university = request.POST.get("home_university")
        preferred_branch_id = request.POST.get("preferred_branch")

        
        if not all([full_name, cet_percentile, category, home_university, preferred_branch_id]):
            messages.error(request, "Please fill all fields")
            return redirect("home")

        try:
            preferred_branch = Branch.objects.get(id=preferred_branch_id)
        except Branch.DoesNotExist:
            messages.error(request, "Invalid branch selected")
            return redirect("home")

    
        student = Student.objects.create(
            full_name=full_name,
            cet_percentile=float(cet_percentile),
            category=category,
            home_university=home_university,
            preferred_branch=preferred_branch
        )

        messages.success(request, f"Student {student.full_name} saved successfully!")
        return redirect("home")

    branches = Branch.objects.all()

    return render(request, "/", {
        "branches": branches,
        "categories": Student.CATEGORY_CHOICES
    })
    #database work pending
def predict_college(request,student_id):
    student = Student.objects.get(id=student_id)
    colleges=Cutoff.objects.filter(
        category=student.category,
        year=2026,
        branch=student.preferred_branch,
        percentile__lte=student.percentile,
    ).order_by("-Cutoff_percentile")
    #return render(request, "predict.html", {"colleges": colleges})(url will be discussed later)
    print(student.cet_percentile)