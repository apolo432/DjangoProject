from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Max
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer


# Student endpoints
@api_view(['POST', 'GET'])
def student_list(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Test endpoints
@api_view(['POST', 'GET'])
def test_list(request):
    if request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def test_detail(request, pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TestSerializer(test)
    return Response(serializer.data)


# TestResult endpoints
@api_view(['POST'])
def submit_test_result(request):
    serializer = TestResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_results(request, student_id):
    results = TestResult.objects.filter(student_id=student_id)
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test_results(request, test_id):
    results = TestResult.objects.filter(test_id=test_id)
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test_average(request, test_id):
    avg = TestResult.objects.filter(test_id=test_id).aggregate(Avg('score'))
    return Response({'average_score': avg['score__avg']})


@api_view(['GET'])
def test_highest(request, test_id):
    highest = TestResult.objects.filter(test_id=test_id).aggregate(Max('score'))
    return Response({'highest_score': highest['score__max']})