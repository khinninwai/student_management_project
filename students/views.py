from django.shortcuts import render, redirect, get_object_or_404
# pyrefly: ignore [missing-import]
from .models import Student
# pyrefly: ignore [missing-import]
from .forms import StudentForm


# Create your views here.

# READ (Student List)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# CREATE (Add Student)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'title': 'Create Student'})


# UPDATE (Email Student)
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'title': 'Edit Student'})


# DELETE (Delete Student)
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')