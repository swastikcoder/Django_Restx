from django.shortcuts import render
from serializers import UserRegistratoiSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view('POST')
def register_user(request):
    serializer = UserRegistratoiSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
