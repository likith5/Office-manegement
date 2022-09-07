
from multiprocessing import context
from operator import methodcaller
from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.db.models import Q
from datetime import datetime

from .models import employee ,Role,Department

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'veiw_all_emp.html',context)




def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee removed")
        except:
            return HttpResponse("PLease Enter a valid emp id")
    emps = employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            'emps':emps
        }
        return render(request,'veiw_all_emp.html',context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')

    else:
        return HttpResponse("Error occurred")




def add_emp(request):
     if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = employee(first_name=first_name,last_name = last_name,salary=salary,bonus = bonus,phone=phone,dept_id=dept,role_id  = role,hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Emplyoee added succesfully')
     elif request.method == 'GET':
        return render(request,'add_emp.html')
     else:
        return HttpResponse('An error occured ')
