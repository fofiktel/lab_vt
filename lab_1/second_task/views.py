from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PersonalInformation

def data_form(request):
    return render(request, 'second_task/form.html')


def add_employee(request):
    if request.method == 'POST':
        inf = PersonalInformation(employee_name=request.POST.get("name"),job_title=request.POST.get("job_title"),
                                  sex=request.POST.get("sex"),department=request.POST.get("department"),
                                  email=request.POST.get("email"),phone_number=request.POST.get("phone"),
                                  comment=request.POST.get('comment'))
        inf.save()
    return HttpResponseRedirect("http://127.0.0.1:8000/fourth/choose_page")
