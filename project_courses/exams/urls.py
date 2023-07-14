from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamViewSet, QuestionViewSet, UserExamViewSet

router = DefaultRouter()
router.register('exams', ExamViewSet)
router.register('questions', QuestionViewSet)
router.register('user_exams', UserExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
