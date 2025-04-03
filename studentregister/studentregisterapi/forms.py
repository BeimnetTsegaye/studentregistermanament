from django import forms
from studentregisterapi.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_profile']
