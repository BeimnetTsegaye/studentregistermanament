# from django.db import models
# int length=150
# class SchoolForm (models.Model){
# id=models.Integer(max_length=100),
# schoolname = models.CharField(max_length=length, ${blank=True, null=True}),
# stud_name=models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE),
# }
# def __str__(self):
#     return self.schoolname

# class StudentForm(models.Model){
#     id=models.Integer(max_length=100)
#     ,
#     stud_name = models.CharField(max_length=length, ${blank=True, null=True}),
#     section=models.varChar(max_length=length, blank=True),
#     gender=models.CharField( max_length=50),
#     homeroom_name=models.ForeignKey("homeroom", verbose_name=_(""), on_delete=models.CASCADE)
#     def __str__(self):
#         return stud_name

#     def __unicode__(self):
#         return 
# }
# class homeroom(models.Model){
#     id=models.Integer(max_length=100)
#     ,
#     stud_name = models.CharField(max_length=length, ${blank=True, null=True}),
#     teach_name=models.ForeignKey("TeacherForm.Model", verbose_name=_(""), on_delete=models.CASCADE)
#     grade_section=models.CharField( max_length=50),
    
#     def __str__(self):
#         return f"{self.stud_name + self.teach_name}"

#     def __unicode__(self):
#         return 
# }
# class Teacherform(models.Model){
#     id=models.Integer(max_length=100)
#     ,
#     teach_name = models.CharField(max_length=length, ${blank=True, null=True}),
#     dept=models.varChar(max_length=length, blank=True),
    
#     def __str__(self):
#         return f"{self.teach_name + self.dept}"
#     def __unicode__(self):
#         return 
# }
# class StatusForm(models.Model){
#     id=models.Integer(max_length=100)
#     ,
#     stud_id =models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE)
#     rank=models.models.IntegerField(max_length=100),
#     avg=models.models.IntegerField(max_length=100),
#     total=models.models.IntegerField(max_length=100),
#     status=models.models.BooleanField(blank=True)
#     def __str__(self):
#         return f"{self.stud_id + self.status}"

#     def __unicode__(self):
#         return 
# }
# class SubjectForm(models.Model){
#     id=models.Integer(max_length=100)
#     ,
#     sub_type =models.models.ForeignKey("StudSubject", verbose_name=_(""), on_delete=models.CASCADE)
#     sub_value=models.models.IntegerField(max_length=length, blank=True),
#     sub_maxscore=models.models.IntegerField( max_length=50),
    
#     def __str__(self):
#         return sub_type

#     def __unicode__(self):
#         return 
# }
# class StudSubject(models.Model){
#     id=models.Integer(max_length=100),
#     stud_name =models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE),
#     section=models.varChar(max_length=length, blank=True),
#     score=models.IntegerField(_(""))    
#     def __str__(self):
#         return f"{self.stud_name + self.section}"

#     def __unicode__(self):
#         return 
# }
from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=150)
    academic_year = models.CharField(max_length=50)  # e.g., "2016 | Semester I"

    def __str__(self):
        return self.school_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)  # e.g., "Maths", "Chemistry"

    def __str__(self):
        return self.teacher_name

class Homeroom(models.Model):
    homeroom_name = models.CharField(max_length=100)  # e.g., "9A"
    grade = models.CharField(max_length=50)  # e.g., "Grade 9"
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Homeroom teacher

    def __str__(self):
        return f"{self.grade} - {self.homeroom_name}"

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    student_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    homeroom = models.ForeignKey(Homeroom, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=20, unique=True)  # e.g., "ABC001/16"

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
    subject_code = models.CharField(max_length=20, unique=True)  # e.g., "ABC001/16"
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
    total_score = models.IntegerField()  # Calculated from StudentSubject
    average = models.FloatField()        # total_score / number of subjects
    rank = models.IntegerField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.status}"