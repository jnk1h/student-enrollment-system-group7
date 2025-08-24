from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Instructor, Course, Student, Enrollment
from .serializers import DepartmentSerializer, InstructorSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer
from rest_framework.permissions import DjangoModelPermissions

# Create your viewsets here.
class DepartmentViewSet (viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [DjangoModelPermissions]

class InstructorViewSet (viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [DjangoModelPermissions]

class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions]


class StudentViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]

class EnrollmentViewSet (viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [DjangoModelPermissions]