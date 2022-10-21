from rest_framework import serializers
from .models import Student, School, Teacher

#############################################################################################

class StudentSerializer(serializers.ModelSerializer):
    class_teacher = serializers.StringRelatedField(read_only=True)
    school = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Student
        fields = ['student', 'standard', 'roll', 'class_teacher', 'school']
#############################################################################################


class TeacherSerializer(serializers.ModelSerializer):
    school_name = serializers.StringRelatedField(read_only=True)
    class_teacher = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['teacher', 'school_name', 'class_head', 'class_teacher']
######################################################################################################

class SchoolSerializer(serializers.ModelSerializer):
    School_Stu = serializers.StringRelatedField(many=True, read_only=True)
    Teacher_Name = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = School
        fields = ['school', 'School_Stu', 'Teacher_Name']
##########################################################################################################