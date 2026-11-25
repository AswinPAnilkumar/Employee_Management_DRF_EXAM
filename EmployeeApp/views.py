from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from EmployeeApp.serializers import UserSerializer,EmployeeSerializer
from EmployeeApp.models import Employee
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"User Successfully registered",
            "User Details":serializer_instance.data})
        else:
            return Response(data=serializer_instance.errors)

class UserView(APIView):
    def get(self,request):
        users = User.objects.filter(user=request.user)
        serializer_instance = UserSerializer(users,many=True)
        return Response(data=serializer_instance.data)

class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        employee = Employee.objects.all()
        serializer_instance = EmployeeSerializer(employee,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        serializer_instance = EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response({"Message":"Employee Successfully Added",
            "Employee Details":serializer_instance.data})
        else:
            return Response(data=serializer_instance.errors)

class EmployeeRetrieveUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,emp_id):
        employee_object = get_object_or_404(Employee,id=emp_id)
        serializer_instance = EmployeeSerializer(employee_object)
        return Response(data=serializer_instance.data)
    
    def put(self,request,emp_id):
        employee_object = get_object_or_404(Employee,id=emp_id)
        serializer_instance = EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"Employee Details Updated Successfully",
            "Employee Details" : serializer_instance.data})
        else:
            return Response(data=serializer_instance.errors)
    
    def delete(self,request,emp_id):
        employee_object = get_object_or_404(Employee,id=emp_id)
        employee_object.delete()
        return Response({"Message":"Employee Removed Successfully"})