from functools import partial
import re
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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

class Get_data(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        print('---------GET--',serializer)
        return Response(serializer.data)

class Post_data(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print('---------POST--',serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Student_data(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_data(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_update_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, *args, **kwargs):
        id = request.data['id']
        stu_object = Student_model.objects.get(id=id)
        serializer = self.serializer_class(stu_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Patch_data(APIView):
    '''
        Not Working properly
    '''
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_update_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        id = request.data['id']
        stu_object = Student_model.objects.get(id=id)
        serializer = self.serializer_class(stu_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Delete_data(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = Student_update_serializer
    def get(self, request, id):
        data = Student_model.objects.get(id=id)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        stu_object = Student_model.objects.get(id=id)
        stu_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
