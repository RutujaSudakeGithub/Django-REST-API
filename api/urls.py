from django.urls import path,include
from . import views

urlpatterns =[
    path('students/',views.viewStudent),
    path('students/<int:pk>/',views.viewStudentDetail),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeesDetails.as_view()),
    
]