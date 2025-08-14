from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, InstructorViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'instructor', InstructorViewSet)
router.register(r'course', CourseViewSet)
router.register(r'student', StudentViewSet)
router.register(r'enrollment', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]