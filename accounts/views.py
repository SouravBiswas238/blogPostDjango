from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            'token':token.key,
            'email':user.email,
            'message': 'user registerd successfully'
        },status=status.HTTP_201_CREATED)