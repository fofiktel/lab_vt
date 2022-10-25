from django.shortcuts import render
from.models import FacultyList, CourseList,GroupList,StudentList


def faculty(request):
    faculty_list = FacultyList.objects.all()
    context = {
        'faculty_list': faculty_list
    }
    return render(request, 'third_task/faculty.html', context)


def course(request, pk):
    course_list = FacultyList.objects.get(id=pk).courselist_set.all()
    context = {
        'course_list': course_list
    }

    return render(request, 'third_task/course.html', context)


def group(request, pk):
    group_list = CourseList.objects.get(id=pk).grouplist_set.all()

    context = {
        'group_list': group_list
    }
    return render(request,'third_task/group.html',context)


def students(request,pk):
    student_list = GroupList.objects.get(id=pk).studentlist_set.all()

    context = {
        'student_list': student_list
    }
    return render(request,'third_task/students.html',context)


def student(request, pk):

    student = StudentList.objects.get(id=pk)
    context = {
        'student': student
    }
    return render(request,'third_task/student.html',context)
# Create your views here.
