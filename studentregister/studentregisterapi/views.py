from rest_framework import generics
from studentregisterapi.forms import StudentForm
from .models import School, Teacher, Subject, Status, Homeroom, Student, StudentSubject
from django.shortcuts import get_object_or_404, redirect, render,redirect
from .serealizers import (
    SchoolSerializer,
    TeacherSerializer,
    SubjectSerializer,
    StatusSerializer,
    HomeroomSerializer,
    StudentSerializer,
    StudentSubjectSerializer
)

# School Views
class SchoolListCreateAPIView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

# Teacher Views
class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Subject Views
class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Status Views
class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# Homeroom Views
class HomeroomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Homeroom.objects.all()
    serializer_class = HomeroomSerializer

class HomeroomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homeroom.objects.all()
    serializer_class = HomeroomSerializer

# Student Views
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# StudentSubject Views
class StudentSubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer

class StudentSubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer

def table_view(request):
    # Fetch all students (you can add filtering, ordering, etc. as needed)
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'table.html', context)

def upload_profile_image(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = StudentForm()
    return render(request, 'upload.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')
