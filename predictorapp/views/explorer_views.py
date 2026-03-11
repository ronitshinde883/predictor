from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..views import details_views,auth_views,predict_views


# def cutoff_explorer(request, college_id, branch_id, year, category):
#     college_id=request.GET.get("college")
#     branch_id=request.GET.get("branch")
#     year=request.GET.get("year")
#     category=request.GET.get("category")
    
#     cutoffs= Cutoff.objects.filter(
#         college_id=college_id,
#         branch_id=branch_id,
#         year=year,
#         category=category
#     )
#     data=[]
#     for c in cutoffs:
#         data.append({
#             "college":c.college.name,
#             "branch": c.branch.name,
#             "year": c.year,
#             "category": c.category,
#             "round": c.round,
#             "percentile": c.percentile,
#         })
#     return JsonResponse({"result":data})
@login_required
def allcollege(request):
    colleges=College.objects.all()
    return render(request,"colleges.html",{
        "colleges":colleges
    })