# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# def viewStudent(request):
#     students = Student.objects.all() # returns query set 
#     students_list = list(students.values()) #manual searilizable -> converting queryset in list because 
#     # jsonResponse accepts data in json format, function is not able to convert queyset into json, we converted it in 
#     #into list . Not recommend for crreating rest APIS
#     return  JsonResponse(students_list,safe=False)

@api_view(['GET','POST'])
def viewStudent(request):
    if request.method =="GET":
        # get all the data from student table
        students = Student.objects.all()
        serializers = StudentSerializer(students,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def viewStudentDetail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =='PUT':
        serializer = StudentSerializer(student,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)