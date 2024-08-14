from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer, ClassesSerializer, ClassroomPeriodSerializer, CoursesSerializer, TeacherSerializer
from classes.models import Class
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from teacher.models import Teacher
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        country = request.query_params.get("country")    
        if country:
            students = students.filter(country=country)    
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomPeriodListView(APIView):
    def get(self, request):
        periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(periods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassroomPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        action = request.data.get("action")
        if action == "add_to_class":
            class_id = request.data.get("class_id")
            student_class = get_object_or_404(Class, id=class_id)
            student_class.students.add(student)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ClassDetailView(APIView):
    def get(self, request, id):
        cls = get_object_or_404(Class, id=id)
        serializer = ClassesSerializer(cls)
        return Response(serializer.data)
    
    def put(self, request, id):
        cls = get_object_or_404(Class, id=id)
        serializer = ClassesSerializer(cls, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        cls = get_object_or_404(Class, id=id)
        cls.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassroomPeriodDetailView(APIView):
    def get(self, request, id):
        period = get_object_or_404(ClassroomPeriod, id=id)
        serializer = ClassroomPeriodSerializer(period)
        return Response(serializer.data)
    
    def put(self, request, id):
        period = get_object_or_404(ClassroomPeriod, id=id)
        serializer = ClassroomPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        period = get_object_or_404(ClassroomPeriod, id=id)
        period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CoursesDetailView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Courses, id=id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = get_object_or_404(Courses, id=id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        course = get_object_or_404(Courses, id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            course = get_object_or_404(Courses, id=course_id)
            teacher.courses.add(course)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            student_class = get_object_or_404(Class, id=class_id)
            student_class.teacher = teacher
            student_class.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodCreateView(APIView):
    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        if not teacher_id or not course_id:
            return Response({"error": "teacher_id and course_id are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        teacher = get_object_or_404(Teacher, id=teacher_id)
        course = get_object_or_404(Courses, id=course_id)

        class_period = ClassroomPeriod.objects.create(teacher=teacher, course=course)
        serializer = ClassroomPeriodSerializer(class_period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TimetableView(APIView):
    def get(self, request):
        timetable_data = []

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            periods = ClassroomPeriod.objects.filter(day_of_week=day).values(
                "start_time", "end_time", "course__name", "teacher__name"
            )
            timetable_data.append({
                "day": day,
                "periods": list(periods)
            })
        
        return Response(timetable_data)
