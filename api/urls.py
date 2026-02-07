from django.urls import path,include
from . import views

urlpatterns =[
    path('students/',views.viewStudent),
    path('students/<int:pk>/',views.viewStudentDetail),
    
]