from django.shortcuts import render, redirect
from AuthenticationApp.models import *
from django.contrib.auth.decorators import login_required

@login_required
def emp_view(request):
    
    data = EmployeeModel.objects.all()
    
    return render(request, 'employee.html', {'data':data})

@login_required
def add_emp_view(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        
        EmployeeModel.objects.create(
            name = name,
            email = email,
            phone = phone,
            department = department,
            salary = int(salary),
        )
        return redirect('emp')
    
    return render(request, 'add-emp.html')

@login_required
def edit_emp_view(request, eid):
    
    data = EmployeeModel.objects.get(id = eid)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
    
        data.name = name
        data.email = email
        data.phone = phone
        data.department = department
        data.salary = salary
        
        data.save()

        return redirect('emp')
    
    return render(request, 'edit-emp.html',  {'data':data})

@login_required
def delete_emp_view(request, eid):
    
    EmployeeModel.objects.get(id = eid).delete()
    
    return redirect('emp')