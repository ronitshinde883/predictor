from django.contrib import admin
from django.urls import path
from .views import auth_views,details_views,predict_views,explorer_views,test_views
from .views.auth_views import RegisterAPI,LoginAPI,LogoutAPI,ResetPasswordAPI,ForgotPasswordAPI

urlpatterns = [

    #detail urls
    path("student/", details_views.student_detail, name="student_detail"),
    # predict urls
    path("predict/<int:student_id>/", predict_views.predict_college, name="predict_college"),
    path("percentile/", predict_views.predict_percentile, name="percentile"),
    path("colleges/<int:college_id>/",explorer_views.allcollege, name="college_detail"),
    path("colleges/",explorer_views.allcollege, name="colleges"),
    path('api/test/',test_views.test_api),
    
    
    
    #Auth urls
    
    path("api/register/", RegisterAPI.as_view(), name="api_register"),
    path("api/login/", LoginAPI.as_view(), name="api_login"),
    path("api/logout/", LogoutAPI.as_view(), name="api_logout"),
    path("api/forgot-password/", ForgotPasswordAPI.as_view(), name="api_forgot_password"),
    path("api/reset-password/<int:uid>/<str:token>/", ResetPasswordAPI.as_view(), name="api_reset_password")
    
]
