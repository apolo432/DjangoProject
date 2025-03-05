from django.urls import path
from .views import (
    student_list,
    student_detail,
    test_list,
    test_detail,
    submit_test_result,
    student_results,
    test_results,
    test_average,
    test_highest
)

urlpatterns = [
    # Students
    path('students/', student_list),
    path('students/<int:pk>/', student_detail),

    # Tests
    path('tests/', test_list),
    path('tests/<int:pk>/', test_detail),

    # Results
    path('results/', submit_test_result),
    path('results/student/<int:student_id>/', student_results),
    path('results/test/<int:test_id>/', test_results),
    path('results/test/<int:test_id>/average/', test_average),
    path('results/test/<int:test_id>/highest/', test_highest),
]