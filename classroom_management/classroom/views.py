from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Classroom, Student, Assessment
from .serializers import ClassroomSerializer, StudentSerializer, AssessmentSerializer

# Create your views here.

# Student CRUD Views
class StudentListCreateView(generics.ListCreateAPIView):
    """Teachers can view all students or add new students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Teachers can update or delete student records."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Assessment CRUD Views
class AssessmentListCreateView(generics.ListCreateAPIView):
    """Teachers can add student scores."""
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssessmentDetailView(generics.RetrieveAPIView):
    """Teachers can view a specific student’s assessment details."""
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]
