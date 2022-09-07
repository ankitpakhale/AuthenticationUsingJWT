import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializer import *
from .models import *
# Create your views here.

class HelloView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        now = datetime.datetime.now()
        timeHTML = f"It is now {now}."
        content = {'message': 'Hello User!', 'time': timeHTML}
        return Response(content)

class Get_data(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = Student_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        print('---------GET--',serializer)
        return Response(serializer.data)

class Post_data(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = Student_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print('---------POST--',serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Student_data(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = Student_serializer
    def get(self, request):
        data = Student_model.objects.all()
        serializer = self.serializer_class(data, many=True)
        
        print(len('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyNTIyMjY0LCJpYXQiOjE2NjI1MjE5NjQsImp0aSI6ImM4OTkxMGVmMDViNzQwM2ViY2M2NDdkZWVhMWJjZTE5IiwidXNlcl9pZCI6MX0.GEq4rV1HaY61_ECuprtMp_CdxG7bv4BiFv5pvnMxEUE'))
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_data(APIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Student_update_serializer
    def get(self, request, id):
        data = Student_model.objects.get(id=id)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, id):
        stu_object = Student_model.objects.get(id=id)
        serializer = self.serializer_class(stu_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Patch_data(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = Student_update_serializer
    def get(self, request, id):
        data = Student_model.objects.get(id=id)
        serializer = self.serializer_class(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        stu_object = Student_model.objects.get(id=id)
        stu_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
