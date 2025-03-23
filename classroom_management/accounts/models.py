from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    TEACHER = "Teacher"
    STUDENT = "Student"
    ADMIN = "Admin"

    ROLE_CHOICES = [
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
        (ADMIN, "Admin"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return self.username
