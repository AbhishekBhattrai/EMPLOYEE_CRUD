from django.shortcuts import redirect, render

from application.models import Employee
from .forms import EmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'application/home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("employee_insert")   # redirect after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "application/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "application/register.html")




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