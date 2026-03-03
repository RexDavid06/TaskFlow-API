from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
User=get_user_model()

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "User created successfully",
            "user": serializer.data
        })
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh), 
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({
            "error": "user not known",
        }, status=status.HTTP_401_UNAUTHORIZED)
    
