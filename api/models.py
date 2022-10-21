from django.db import models

# Create your models here.

class School(models.Model):
    school = models.CharField(max_length=50)
    def __str__(self):
        return self.school
    class Meta:
        ordering = ['id']

########################################################################################

class Teacher(models.Model):
    teacher = models.CharField(max_length=30)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="Teacher_Name", default="NULL")
    class_head = models.IntegerField()
    def __str__(self):
        return self.teacher

    class Meta:
        ordering = ['class_head']

##########################################################################################################################

class Student(models.Model):
    student = models.CharField(max_length=30)
    standard = models.IntegerField()
    roll = models.IntegerField()
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="class_teacher")
    school = models.ForeignKey(School, on_delete=models.CASCADE, max_length=30, related_name='School_Stu')
    def __str__(self):
        return self.student
    class Meta:
        ordering = ['roll']

#######################################################################################################################
