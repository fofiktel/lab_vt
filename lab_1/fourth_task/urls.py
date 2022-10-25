from django.urls import path
from . import views
app_name = 'fourth_task'

urlpatterns = [
   path('choose_page', views.choose_page, name='choose_page'),
   path('delete_employee', views.delete_employee, name='delete_employee'),
   path('update_employee',views.update_form,name='update_form'),
   path('update_inf',views.update_information,name='update_inf')
]