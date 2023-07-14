from rest_framework import serializers
from .models import Exam, Question, UserExam
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class UserExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExam
        fields = '__all__'
