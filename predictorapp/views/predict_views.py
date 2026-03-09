from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@login_required
def predict_college(request, student_id):

    student = Student.objects.get(id=student_id)
    colleges = Cutoff.objects.filter(
        category=student.category,
        year=2026,
        branch=student.preferred_branch,
        percentile__lte=student.percentile,
    ).select_related("college", "branch").order_by("-percentile")

    return render(request, "predict.html", {
        "student": student,
        "colleges": colleges
    })