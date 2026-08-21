from django.forms import widgets
from django import forms
# pyrefly: ignore [missing-import]
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','gender','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Email...'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Phone...'})
        }