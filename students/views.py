from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student(request):
    students=[
        {'id':1,'name':'jonh','age':12}
    ]
    
    return HttpResponse(students)
