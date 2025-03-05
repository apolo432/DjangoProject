from rest_framework import serializers
from .models import Student, Test, TestResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'max_score']

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['id', 'student', 'test', 'score']