from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("student/", views.student_detail, name="student_detail"),
    path("register/",views.register,name="register"),
    path("predict/<int:student_id>/", views.predict_college, name="predict_college"),
    path(
        'cutoff/<int:college_id>/<int:branch_id>/<int:year>/<str:category>/',
        views.cutoff_explorer,
        name='cutoff_explorer'
    ),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name='logout')
]