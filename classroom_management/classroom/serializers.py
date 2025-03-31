from rest_framework import serializers
from .models import Classroom, Student, Assessment
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
