from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University,PercentilePredictor
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..views import explorer_views,details_views,auth_views 

@login_required
def predict_college(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect("student_detail")

    colleges = Cutoff.objects.filter(
        category=student.category,
        year=2026,
        branch=student.preferred_branch,
        percentile__lte=student.percentile,
    ).select_related("college", "branch").order_by("-percentile")

    return render(request,"predict.html", {
        "student": student,
        "colleges": colleges
    })
    
def predict_percentile(request):
    if request.method=='POST':
        score=int(request.POST.get("score"))
        result=PercentilePredictor.objects.filter(score__lte=score).order_by("-score").first()
        
        return render(request,"score.html",{
            "percentile": result.percentile
        })
    return render(request,"score.html")