from django.db import models


class FacultyList(models.Model):
    faculty_name = models.CharField(max_length=40,default='faculty')

    def __str__(self):
        return f'{self.faculty_name}'

class CourseList(models.Model):
    course_name = models.CharField(max_length=40,default='course')
    faculty = models.ForeignKey(FacultyList,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'course {self.course_name} faculty {self.faculty.faculty_name}'


class GroupList(models.Model):
    group_name = models.CharField(max_length=40,default='group')
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.group_name} course {self.course.course_name} faculty {self.course.faculty.faculty_name}'


class StudentList(models.Model):
    student_name = models.CharField(max_length=40,default='name')
    age = models.IntegerField(default=18)
    type_of_student = models.CharField(max_length=10,default="type")
    group = models.ForeignKey(GroupList,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.student_name} {self.group.group_name} course {self.group.course.course_name} faculty {self.group.course.faculty.faculty_name}'


# Create your models here.
