from django.shortcuts import render, redirect
from AuthenticationApp.models import *
from django.contrib.auth.decorators import login_required

@login_required
def std_view(request):
    
    data = StudentModel.objects.all()
    
    return render(request, 'students.html', {'data':data})

@login_required
def add_std_view(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        semester = request.POST.get('semester')
        course = request.POST.get('course')
        
        StudentModel.objects.create(
            name = name,
            email = email,
            roll_number = roll_number,
            semester = semester,
            course = course,
        )
        return redirect('std')
    
    return render(request, 'add-std.html')

@login_required
def edit_std_view(request, eid):
    
    data = StudentModel.objects.get(id = eid)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        semester = request.POST.get('semester')
        course = request.POST.get('course')
    
        data.name = name
        data.email = email
        data.roll_number = roll_number
        data.semester = semester
        data.course = course
        
        data.save()

        return redirect('std')
    
    return render(request, 'edit-std.html',  {'data':data})

@login_required
def delete_std_view(request, eid):
    
    StudentModel.objects.get(id = eid).delete()
    
    return redirect('std')