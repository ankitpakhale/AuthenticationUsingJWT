from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .models import *
# Create your views here.

def demo(request):
    permission_classes = (IsAuthenticated,)
    if permission_classes:
        now = datetime.datetime.now()
        html = "<html><body><h2>It is now %s.</h2></body></html>" % now
        return HttpResponse(html)
    else:
        return HttpResponse("You are not allowed to enter because you don't have permission_classes")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        now = datetime.datetime.now()
        timeHTML = f"It is now {now}."
        content = {'message': 'Hello User!', 'time': timeHTML}
        return Response(content)

class Student_data(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        stu_data = Student_serializer(Student_model.objects.all(), many = True)
        print(stu_data)
        return Response(stu_data.data)
    
    # def post(self, request):
    #     pass
