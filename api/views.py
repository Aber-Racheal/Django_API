from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from .serializers import ClassroomPeriodSerializer
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status
    

class StudentListView(APIView):
    def get(self,request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ClassListView(APIView):
    def get(self,request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
class ClassroomPeriodListView(APIView):
    def get(self,request):
        Periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassroomPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
class CoursesListView(APIView):
    def get(self,request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
class TeacherListView(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
  
class ClassDetailView(APIView):
    def get(self,request,id):
        classes = Class.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    
    def put(self,request,id):
       classes = Class.objects.get(id=id)
       serializer = ClassesSerializer(classes, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classes = Class.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        
     
     
class ClassroomPeriodDetailView(APIView):
    def get(self,request,id):
        class_periods = ClassroomPeriod.objects.get(id=id)
        serializer = ClassroomPeriodSerializer(class_periods)
        return Response(serializer.data)
    
    def put(self,request,id):
       class_periods = ClassroomPeriod.objects.get(id=id)
       serializer = ClassroomPeriodSerializer(class_periods, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        class_periods = ClassroomPeriod.objects.get(id=id)
        class_periods.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
      
class CoursesDetailView(APIView):
    def get(self,request,id):
       courses = Courses.objects.get(id=id)
       serializer = CoursesSerializer(courses)
       return Response(serializer.data)
    
    def put(self,request,id):
       courses = Courses.objects.get(id=id)
       serializer = CoursesSerializer(courses, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        courses = Courses.objects.get(id=id)
        courses.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
      

class TeacherDetailView(APIView):
    def get(self,request,id):
        teachers = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)
    
    def put(self,request,id):
       teachers = Teacher.objects.get(id=id)
       serializer = TeacherSerializer(teachers, data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        teachers = Teacher.objects.get(id=id)
        teachers.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
      
