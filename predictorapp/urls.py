from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_detail,name='home'),
    path("/register",views.register,name="register"),
    #path("pp/<int:student_id>/", views.predict_college, name="predict"),
]