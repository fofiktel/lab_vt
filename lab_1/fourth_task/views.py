from django.shortcuts import render
from django.http import HttpResponseRedirect
from second_task.models import PersonalInformation


def choose_page(request):
    inf_list = PersonalInformation.objects.all()
    context = {
        'inf_list': inf_list
    }
    return render(request,'fourth_task/choose_page.html',context)


def delete_employee(request):
    if request.method == 'POST':
        PersonalInformation.objects.get(id=request.POST.get("employee")).delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/fourth/choose_page')


def update_form(request):
    if request.method == 'POST':
        inf = PersonalInformation.objects.get(id=request.POST.get("employee"))
        context = {
            'inf': inf
        }
        return render(request,'fourth_task/update_form.html',context)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/fourth/choose_page')


def update_information(request):
    if request.method == 'POST':
        person = PersonalInformation.objects.get(id=request.POST.get("employee"))
        person.employee_name = request.POST.get("name")
        person.job_title=request.POST.get("job_title")
        person.sex=request.POST.get("sex")
        person.department=request.POST.get("department")
        person.email=request.POST.get("email")
        person.phone_number=request.POST.get("phone")
        person.comment = request.POST.get('comment')
        person.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/fourth/choose_page')