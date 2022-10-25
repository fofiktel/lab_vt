
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('second/',include('second_task.urls')),
    path('third/',include('third_task.urls')),
    path('fourth/',include('fourth_task.urls'))

]
