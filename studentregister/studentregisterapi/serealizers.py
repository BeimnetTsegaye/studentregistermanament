from rest_framework import serializers
from .models import Homeroom, School, Student, StudentSubject, Subject, Status, Teacher

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_name', 'academic_year']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'department']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_type', 'subject_code', 'max_score']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['student', 'total_score', 'average', 'rank', 'status']
        read_only_fields = ['total_score', 'average', 'rank', 'status']

class HomeroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeroom
        fields = ['homeroom_name', 'grade', 'school', 'teacher']

    def create(self, validated_data):
         return Homeroom.objects.create(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['student_name', 'gender', 'homeroom', 'student_code', 'subjects','student_profile']

    def get_subjects(self, obj):
        request = self.context.get('request')
        if obj.student_profile and hasattr(obj.student_profile, 'url'):
            return request.build_absolute_uri(obj.student_profile.url)
        subjects = StudentSubject.objects.filter(student=obj)
        return StudentSubjectSerializer(subjects, many=True).data

class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = ['student', 'subject', 'score']