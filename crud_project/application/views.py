from django.shortcuts import redirect, render

from application.models import Employee
from .forms import EmployeeForm
# Create your views here.

def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request, 'application/employee_list.html', context)

def employee_form(request, id=0):
    if request.method=='GET':
        if id==0:
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request, 'application/employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('list/')    

def employee_delete(request, id):
    employee=Employee.objects.get(id=id).delete()
    return redirect('employee_list')