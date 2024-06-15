from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Employee, Role, Department, Contact
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import Contact_form

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    form = Contact_form
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Contact(first_name = first_name, last_name = last_name, email = email, message = message)
        data.save()
        messages.success(request,'Contact Saved')
        return redirect('contact')
    return render(request, 'contact.html',{'form': form})

@login_required
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email is already exists')
            return redirect('register')
        else:
            user = User(email= email, password = password, first_name = first_name, last_name = last_name, username = username)
            user.set_password(password)
            user.save()
            messages.success(request, "Profile details updated.")
            return redirect('/')
    return render(request, 'register.html')

 
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('Login')
            return redirect('index') 
        else:
            messages.warning(request,'Invalid Credentials')
            print('Not Login')
            return redirect('login')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus = bonus, phone = phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        messages.success(request, "Employee Added sucessfully.")
        return redirect("/view_emp")
    elif request.method == 'GET':
         return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occured')

@login_required
def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        id = request.POST['id']

        emps = Employee.objects.all()

        if id:
            emps = emps.filter(id = id)
        else:
            messages.warning(request,'Employee with this id is not present')

        if first_name:
            emps = emps.filter(first_name__icontains = first_name)

        if last_name:
            emps = emps.filter(last_name__icontains = last_name)

        if salary:
            emps = emps.filter(salary = salary)

        context = {
            'emps' : emps
        }
        return render(request,'view_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')

    return render(request, 'filter_emp.html')


@login_required
def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            data = Employee.objects.get(id=emp_id)
            data.delete()
            messages.success(request, "Employee deleted sucessfully.")
            return redirect("/remove_emp")
        except:
            return HttpResponse("Enter a valid ID")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'remove_emp.html', context)

@login_required
def update_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'update_emp.html', context)

@login_required
def update_emp1(request,emp_id):
    emp = Employee.objects.get(id = emp_id)
    return render(request,'edit.html',{'emp': emp})

@login_required
def edit(request,emp_id=0):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    salary = int(request.POST['salary'])
    bonus = int(request.POST['bonus'])
    phone = int(request.POST['phone'])

    emp = Employee.objects.get(id=emp_id)
    emp.first_name = first_name
    emp.last_name = last_name
    emp.salary = salary
    emp.bonus = bonus
    emp.phone = phone

    emp.save()
    messages.success(request, "Profile details updated.")
    return redirect("/update_emp")

@login_required
def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'view_emp.html', context)


