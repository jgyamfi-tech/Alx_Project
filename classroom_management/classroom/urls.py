from django.urls import path
from .views import StudentListCreateView, StudentDetailView, AssessmentListCreateView, AssessmentDetailView

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student-list-create"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("assessments/", AssessmentListCreateView.as_view(), name="assessment-list-create"),
    path("assessments/<int:pk>/", AssessmentDetailView.as_view(), name="assessment-detail"),
]
