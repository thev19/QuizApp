from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('get-all-questions/', views.get_all_questions, name='get_all_questions'),
    path('submit-test/', views.submit_test, name='submit_test'),
    path('results/', views.quiz_results, name='quiz_results'),
    path('restart-quiz', views.restart_quiz, name='restart_quiz')
]