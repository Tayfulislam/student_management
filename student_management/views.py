
from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    return render(request, 'students/student_list.html')


from django.shortcuts import render, redirect
from .forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = StudentForm()
    return render(request, 'students/student_registerform.html', {'form': form})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

def update_student(request, pk):
    
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_update.html', {'form': form})


def delete_student(request, student_id): 
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.delete()
        return redirect('home') 
    
    return render(request, 'students/student_confirm_delete.html', {'student': student})