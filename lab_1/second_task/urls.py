from django.urls import path
from . import views
app_name = 'second_task'

urlpatterns = [
    path('form/',views.data_form,name='form'),
    path('add_employee',views.add_employee,name='add_employee')
]