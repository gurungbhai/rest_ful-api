from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # to return response
from django.shortcuts import get_object_or_404 #object does not exit
from rest_framework.views import APIView #normal view can return api data
from rest_framework.views import Response #to get stauts
from rest_framework.views import status 
from .models import employees 
from .serializers import employeesSerializer 

class employeeList(APIView):
    
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass