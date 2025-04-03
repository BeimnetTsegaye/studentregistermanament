from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=150)
    academic_year = models.CharField(max_length=50)  

    def __str__(self):
        return self.school_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=150)
    department = models.CharField(max_length=100) 

    def __str__(self):
        return self.teacher_name

class Homeroom(models.Model):
    homeroom_name = models.CharField(max_length=50) 
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.grade} - {self.homeroom_name}"

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    student_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    homeroom = models.ForeignKey(Homeroom, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=20, unique=True) 
    student_profile=models.FileField(upload_to="images/")
    def __str__(self):
        return self.student_name

class Subject(models.Model):
    SUBJECT_TYPES = [
        ('MATHS', 'Mathematics'),
        ('ENG', 'English'),
        ('BIO', 'Biology'),
        ('CHEM', 'Chemistry'),
        ('PHY', 'Physics'),
    ]
    
    subject_type = models.CharField(max_length=50, choices=SUBJECT_TYPES)
    subject_code = models.CharField(max_length=20, unique=True) 
    max_score = models.IntegerField(default=100)

    def __str__(self):
        return self.subject_type

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject}"

class Status(models.Model):
    STATUS_CHOICES = [('PASS', 'Pass'), ('FAIL', 'Fail')]
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_score = models.IntegerField() 
    average = models.FloatField()       
    rank = models.IntegerField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.status}"