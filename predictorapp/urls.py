from django.contrib import admin
from django.urls import path
from .views import auth_views,details_views,predict_views,explorer_views

urlpatterns = [
    #auth urls
    path("", auth_views.home, name="home"),
    path("register/", auth_views.register, name="register"),
    path("login/", auth_views.login_view, name="login"),
    path("logout/", auth_views.logout_view, name="logout"),
    #detail urls
    path("student/", details_views.student_detail, name="student_detail"),
    # predict urls
    path("predict/<int:student_id>/", predict_views.predict_college, name="predict_college"),
    #explorer urls
    # path("cutoff/<int:college_id>/<int:branch_id>/<int:year>/<str:category>/",explorer_views.cutoff_explorer,name="cutoff_explorer",
    # ),
    path("colleges/",explorer_views.allcollege, name="explore_colleges")
]