from rest_framework import serializers
from .models import Classroom, Student, Assessment, Performance
from accounts.models import CustomUser 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "user", "date_of_birth", "classroom"]

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "name", "teacher"]

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ["id", "student", "assessment_type", "score", "date"]


class PerformanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.username', read_only=True)

    class Meta:
        model = Performance
        fields = ["id", "student", "student_name", "average_score", "progress_status"]
