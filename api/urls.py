from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeesViewSet,basename='employee')

urlpatterns =[
    path('students/',views.viewStudent),
    path('students/<int:pk>/',views.viewStudentDetail),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeesDetails.as_view()),
    
    path('',include(router.urls))
]