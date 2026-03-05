from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def home ( request):
    return HttpResponse('hello i am ronit')

def register( request):
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

@csrf_exempt
def student_detail( request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        percentile = request.POST.get("percentile")
        category = request.POST.get("category")
        home_university = request.POST.get("home_university")
        preferred_branch_id = request.POST.get("preferred_branch")

        
        if not all([full_name,percentile, category, home_university, preferred_branch_id]):
            messages.error(request, "Please fill all fields")
            return redirect("home")

        try:
            preferred_branch = Branch.objects.get(id=preferred_branch_id)
        except Branch.DoesNotExist:
            messages.error(request, "Invalid branch selected")
            return redirect("home")

    
        student = Student.objects.create(
            full_name=full_name,
            percentile=float(percentile),
            category=category,
            home_university=home_university,
            preferred_branch=preferred_branch
        )
        return JsonResponse({
            "message": f"Student {student.full_name} saved successfully!",
            "student_id": student.id
        })
    branches = Branch.objects.all()

    return render(request, "/", {
        "branches": branches,
        "categories": Student.CATEGORY_CHOICES
    })
    #database work pending
def predict_college( request, student_id):
    student = Student.objects.get(id=student_id)
    colleges=Cutoff.objects.filter(
        category=student.category,
        year=2026,
        branch=student.preferred_branch,
        percentile__lte=student.percentile,
    ).select_related("college", "branch").order_by("-percentile")
    #return render(request, "predict.html", {"colleges": colleges})(url will be discussed later)
    data = []

    for c in colleges:
        data.append({
            "college": c.college.name,
            "branch": c.branch.name,
            "cutoff": c.percentile,
            "year": c.year
        })

    return JsonResponse({"results": data})


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
        
    