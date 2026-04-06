from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from ..models import Userprofile,Student,Cutoff,Branch,College,University
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views import View
from ..serializers.registerSerializer import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import default_token_generator



#will be updating to jwt based authentication later
class RegisterAPI(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(APIView):
    def post(self,request):
        email=request.data.get("email")
        password=request.data.get("password")
        
        try:
            user_obj=User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                "error":"Invalid Email Or Password"
            },status=status.HTTP_401_UNAUTHORIZED)
        user=authenticate(username=user_obj.username,password=password)
        
        if user:
            return Response({
                "message":"Login succesful"
            },status=status.HTTP_200_OK)
            
        return Response(
            {"error": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
        
class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        logout(request)
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )
        
class ForgotPasswordAPI(APIView):
    def post(self,request):
        email=request.data.get("email")
        if not email:
            return Response({"error":"Email is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                "error":"Email Not Found"
            },status=status.HTTP_404_NOT_FOUND)
        
        token=default_token_generator.make_token(user)
        reset_link=f"http://dummy-link/reset-password/{user.pk}/{token}/"#default django token 
        
        return Response({
            "message": "Password reset link generated",
            "reset_link": reset_link
        }, status=status.HTTP_200_OK)
        
class ResetPasswordAPI(APIView):
    def post(self,request,uid,token):
        password=request.data.get("password")
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response({"error":"inavlid user"},status=status.HTTP_404_NOT_FOUND)
        if default_token_generator.check_token(user,token):
            user.set_password(password)
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)       
        
        
        
        
        
        
        
        
    