from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/update/<int:pk>/', views.update_student, name='update_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
