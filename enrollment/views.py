from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Instructor, Course, Student, Enrollment
from .serializers import DepartmentSerializer, InstructorSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer

# Create your viewsets here.
class DepartmentViewSet (viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class InstructorViewSet (viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet (viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer