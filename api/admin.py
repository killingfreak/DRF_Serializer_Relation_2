from django.contrib import admin
from .models import Student, School, Teacher
# Register your models here.

@admin.register(School)
class School(admin.ModelAdmin):
    list_display = ["id", 'school']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [id, 'teacher', 'school_name', "class_head"]

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['roll', 'student', 'school', 'standard', 'class_teacher']
