from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Question, Choice, QuizSession
from django.views.decorators.csrf import csrf_exempt
import json
import random

def welcome_page(request):
    user_name = request.session.get('user_name')
    return render(request, 'quiz/welcome.html', {'user_name': user_name})

def start_quiz(request):
    if request.method == 'POST' and 'restart' in request.POST:
        request.session.pop('quiz_submitted', None)
        request.session.pop('quiz_session_id', None)

        quiz_session = QuizSession.objects.create()
        request.session['quiz_session_id'] = quiz_session.id
        request.session['quiz_submitted'] = False 

        return render(request, 'quiz/quiz.html', {
            'session_id': quiz_session.id,
            'user_name': request.session.get('user_name')  
        })

    if request.session.get('quiz_submitted', False):
        return redirect('welcome') 

    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            return render(request, 'quiz/welcome.html', {
                'error': 'Please provide your name.'
            })

        request.session['user_name'] = name

        quiz_session = QuizSession.objects.create()
        request.session['quiz_session_id'] = quiz_session.id
        request.session['quiz_submitted'] = False  

        return render(request, 'quiz/quiz.html', {
            'session_id': quiz_session.id,
            'user_name': name
        })

    return render(request, 'quiz/welcome.html')

def restart_quiz(request):
    request.session.pop('quiz_results', None)
    request.session.pop('quiz_submitted', None)
    return redirect('start_quiz')


@require_http_methods(["GET"])
def get_all_questions(request):

    questions = list(Question.objects.all())

    selected_questions = random.sample(questions, min(len(questions), 20))

    questions_data = []
    for question in selected_questions:
        choices = list(question.choices.all())
        questions_data.append({
            'id': question.id,
            'text': question.text,
            'choices': [
                {'id': choice.id, 'text': choice.text}
                for choice in choices
            ]
        })

    return JsonResponse({
        'questions': questions_data
    })



@csrf_exempt
@require_http_methods(["POST"])
def submit_test(request):
    data = json.loads(request.body)
    answers = data.get('answers', [])
    results = []

    for answer in answers:
        question_id = answer.get('questionId')
        selected_option_id = answer.get('selectedOptionId')
        question = Question.objects.get(id=question_id)

        # Find the correct option
        correct_option = question.choices.filter(is_correct=True).first()
        selected_choice = None
        if selected_option_id:
            selected_choice = Choice.objects.get(id=selected_option_id)
            is_correct = selected_choice.is_correct
        else:
            is_correct = False

        # Add result
        results.append({
            'questionId': question.id,
            'selectedOptionId': selected_choice.text if selected_choice else None ,
            'isCorrect': is_correct,
            'correctOptionId': correct_option.text if correct_option else None,
            'question': question.text,
        })

        request.session['quiz_results'] = results
        request.session['quiz_submitted'] = True  # Set the flag

    return JsonResponse({'results': results})

def quiz_results(request):
    # user_name = request.session.get('user_name', [])
    # return render(request, 'quiz/results.html', {'user_name': user_name})
    results = request.session.get('quiz_results', [])
    user_name = request.session.get('user_name', [])
    if not results:
        return redirect('start_quiz')
    

    total_questions = len(results)
    correct_answers = sum(1 for r in results if r['isCorrect'])
    incorrect_answers = sum(1 for r in results if not r['isCorrect'] and r['selectedOptionId'])
    not_attempted = sum(1 for r in results if not r['selectedOptionId'])

    return render(request, 'quiz/results.html', {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'not_attempted': not_attempted,
        'questions': results,
        'user_name': user_name
    })


