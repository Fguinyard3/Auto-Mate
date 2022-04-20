from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response  
from .serializers import RegistrationSerializer, UserSerializer

from .models import FacebookUser
import requests
import json


class RegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                req = request.post(
                    'http://127.0.0.1:8000/api-auth/token', 
                    data = {
                        'username':new_user.email,
                        'password':request.data['password'],
                        'client_id':'Your Client ID',
                        'client_secret':'Your Client Secret',
                        'grant_type':'password'
                    })
            
            return Response(req.json(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = FacebookUser.objects.all()
    serializer_class = UserSerializer

class LoggedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
    


