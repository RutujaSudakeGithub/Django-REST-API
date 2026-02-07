# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404
from rest_framework import mixins,generics


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
    

# class based view
# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializers = EmployeeSerializer(employees,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializers=EmployeeSerializer(data=request.data)
        
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeesDetails(APIView):
#     def get_details(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         employee = self.get_details(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee = self.get_details(pk)
#         serializer = EmployeeSerializer(employee,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
#     def delete(self,request,pk):
#         employee = self.get_details(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class EmployeesDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

        
