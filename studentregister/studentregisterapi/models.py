from django.db import models
int length=150
class SchoolForm (models.Model){
id=models.Integer(max_length=100),
schoolname = models.CharField(max_length=length, ${blank=True, null=True}),
stud_name=models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE),
}
def __str__(self):
    return self.schoolname

class StudentForm(models.Model){
    id=models.Integer(max_length=100)
    ,
    stud_name = models.CharField(max_length=length, ${blank=True, null=True}),
    section=models.varChar(max_length=length, blank=True),
    gender=models.CharField( max_length=50),
    homeroom_name=models.ForeignKey("homeroom", verbose_name=_(""), on_delete=models.CASCADE)
    def __str__(self):
        return stud_name

    def __unicode__(self):
        return 
}
class homeroom(models.Model){
    id=models.Integer(max_length=100)
    ,
    stud_name = models.CharField(max_length=length, ${blank=True, null=True}),
    teach_name=models.ForeignKey("TeacherForm.Model", verbose_name=_(""), on_delete=models.CASCADE)
    grade_section=models.CharField( max_length=50),
    
    def __str__(self):
        return f"{self.stud_name + self.teach_name}"

    def __unicode__(self):
        return 
}
class Teacherform(models.Model){
    id=models.Integer(max_length=100)
    ,
    teach_name = models.CharField(max_length=length, ${blank=True, null=True}),
    dept=models.varChar(max_length=length, blank=True),
    
    def __str__(self):
        return f"{self.teach_name + self.dept}"
    def __unicode__(self):
        return 
}
class StatusForm(models.Model){
    id=models.Integer(max_length=100)
    ,
    stud_id =models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE)
    rank=models.models.IntegerField(max_length=100),
    avg=models.models.IntegerField(max_length=100),
    total=models.models.IntegerField(max_length=100),
    status=models.models.BooleanField(blank=True)
    def __str__(self):
        return f"{self.stud_id + self.status}"

    def __unicode__(self):
        return 
}
class SubjectForm(models.Model){
    id=models.Integer(max_length=100)
    ,
    sub_type =models.models.ForeignKey("StudSubject", verbose_name=_(""), on_delete=models.CASCADE)
    sub_value=models.models.IntegerField(max_length=length, blank=True),
    sub_maxscore=models.models.IntegerField( max_length=50),
    
    def __str__(self):
        return sub_type

    def __unicode__(self):
        return 
}
class StudSubject(models.Model){
    id=models.Integer(max_length=100),
    stud_name =models.ForeignKey("StudentForm", verbose_name=_(""), on_delete=models.CASCADE),
    section=models.varChar(max_length=length, blank=True),
    score=models.IntegerField(_(""))    
    def __str__(self):
        return f"{self.stud_name + self.section}"

    def __unicode__(self):
        return 
}