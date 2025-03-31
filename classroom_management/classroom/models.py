from django.db import models
from django.conf import settings

# Create your models here.
class Classroom(models.Model):
    """Represents a classroom managed by a teacher."""
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="classrooms")

    def __str__(self):
        return self.name

class Student(models.Model):
    """Represents a student linked to a classroom."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    date_of_birth = models.DateField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.user.username

class Assessment(models.Model):
    """Records assessment scores for students."""
    EXERCISE = "Exercise"
    TEST = "Test"
    EXAM = "Exam"

    ASSESSMENT_CHOICES = [
        (EXERCISE, "Exercise"),
        (TEST, "Test"),
        (EXAM, "Exam"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="assessments")
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    score = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.assessment_type}: {self.score}"
