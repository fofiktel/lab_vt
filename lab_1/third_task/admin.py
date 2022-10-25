from django.contrib import admin
from .models import StudentList,GroupList,CourseList,FacultyList

admin.site.register(FacultyList)
admin.site.register(CourseList)
admin.site.register(GroupList)
admin.site.register(StudentList)
# Register your models here.
