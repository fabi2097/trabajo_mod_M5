from django.shortcuts import render
from rest_framework import viewsets
from .models import Exam, Question, UserExam
from .serializers import ExamSerializer, QuestionSerializer, UserExamSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserExamViewSet(viewsets.ModelViewSet):
    queryset = UserExam.objects.all()
    serializer_class = UserExamSerializer
