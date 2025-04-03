from django.urls import path

from studentregisterapi.views import HomeroomDetailAPIView, HomeroomListCreateAPIView, SchoolDetailAPIView, SchoolListCreateAPIView, StatusDetailAPIView, StatusListCreateAPIView, StudentDetailAPIView, StudentListCreateAPIView, StudentSubjectDetailAPIView, StudentSubjectListCreateAPIView, SubjectDetailAPIView, SubjectListCreateAPIView, TeacherDetailAPIView, TeacherListCreateAPIView, table_view

urlpatterns = [
    path('roster/', table_view, name='student-roster'),

    path('schools/', SchoolListCreateAPIView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', SchoolDetailAPIView.as_view(), name='school-detail'),
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),
    path('statuses/', StatusListCreateAPIView.as_view(), name='status-list-create'),
    path('statuses/<int:pk>/', StatusDetailAPIView.as_view(), name='status-detail'),
    path('homerooms/', HomeroomListCreateAPIView.as_view(), name='homeroom-list-create'),
    path('homerooms/<int:pk>/', HomeroomDetailAPIView.as_view(), name='homeroom-detail'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('student-subjects/', StudentSubjectListCreateAPIView.as_view(), name='student-subject-list-create'),
    path('student-subjects/<int:pk>/', StudentSubjectDetailAPIView.as_view(), name='student-subject-detail'),
]
