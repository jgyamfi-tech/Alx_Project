from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Classroom, Student, Assessment, Performance
from .serializers import ClassroomSerializer, StudentSerializer, AssessmentSerializer, PerformanceSerializer
from .utils import calculate_performance

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

# Assessment Views
class AssessmentListCreateView(generics.ListCreateAPIView):
    """Teachers can add student scores and trigger performance update."""
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        assessment = serializer.save()
        student = assessment.student
        avg, status = calculate_performance(student)

        performance, created = Performance.objects.get_or_create(student=student)
        performance.average_score = avg
        performance.progress_status = status
        performance.save()

class AssessmentDetailView(generics.RetrieveAPIView):
    """Teachers can view a specific student’s assessment details."""
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Performance View
class PerformanceListView(generics.ListAPIView):
    """Get performance summary for all students."""
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]
