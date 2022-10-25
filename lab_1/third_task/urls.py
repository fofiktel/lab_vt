from django.urls import path
from . import views
app_name = 'third_task'

urlpatterns = [
    path('task', views.faculty, name='faculty'),
    path('course/<int:pk>',views.course,name='course'),
    path('group/<int:pk>',views.group,name='group'),
    path('students/<int:pk>',views.students,name='students'),
    path('student/<int:pk>',views.student,name='student')
]