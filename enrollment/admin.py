from django.contrib import admin
from .models import Department, Instructor, Course, Student, Enrollment

# Register your models here.
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)