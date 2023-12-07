from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Forum
from django.db.models import Max,Count
from django.template.loader import render_to_string
from notifications.utils import send_notification

def questions(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    # Get the best answers for each question
    questions = Question.objects.all()[:10]
    
    context = {
        'questions' : questions,
        'user': request.user,
    }

    return context

def forum_questions(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = questions(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/questions.html', context)
    else:
        questions_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'questions_content_template' : questions_content_template,
            'forum' : forum
        }
        forum_template_content = render_to_string('forum.html', contextio)
        return render(request, 'BASE.html', {'forum_template_content': forum_template_content})

def forum_questions_direct(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = questions(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'questions_content_template' : questions_content_template,
            'forum' : forum
        }
        return render(request, 'forum.html', contextio)
    else:
        raise Http404('Page not found')

   
def answers(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    # Get the all answers for each question
    answers = Answer.objects.all()
   
    context = {
        'answers' : answers,
        'user': request.user,
    }
    return context

def forum_answers(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = answers(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/answers.html', context)
    else:
        answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'answers_content_template' : answers_content_template,
            'forum' : forum
        }
        forum_template_content = render_to_string('forum.html', contextio)
        return render(request, 'BASE.html', {'forum_template_content': forum_template_content})

def forum_answers_direct(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = answers(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'answers_content_template' : answers_content_template,
            'forum' : forum
        }
        return render(request, 'forum.html', contextio)
    else:
        raise Http404('Page not found')


def best_answers(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    # Get the best answers for each question
    best_answers = Answer.objects.values('question').annotate(max_score=Max('upvotes')).order_by('-max_score')

    # Create a list of the best answers
    answers = []
    for answer in best_answers:
        best_answer = Answer.objects.filter(question=answer['question'], upvotes=answer['max_score']).first()
        answers.append(best_answer)
    
    context = {
        'answers' : answers,
        'user': request.user,
    }

    return context

def forum_best_answers(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = best_answers(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/answers.html', context)
    else:
        best_answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'best_answers_content_template' : best_answers_content_template,
            'forum' : forum
        }
        forum_template_content = render_to_string('forum.html', contextio)
        return render(request, 'BASE.html', {'forum_template_content': forum_template_content})

def forum_best_answers_direct(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = best_answers(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        best_answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'best_answers_content_template' : best_answers_content_template,
            'forum' : forum
        }
        return render(request, 'forum.html', contextio)
    else:
        raise Http404('Page not found')

def most_followed(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    # Get the best answers for each question
    questions = Question.objects.annotate(num_followers=Count('followers')).order_by('-num_followers')[:10]
    
    context = {
        'questions' : questions,
        'user': request.user,
    }
    return context
       
def forum_most_followed(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = most_followed(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/questions.html', context)
    else:
        most_followed_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'most_followed_content_template' : most_followed_content_template,
            'forum' : forum
        }
        forum_template_content = render_to_string('forum.html', contextio)
        return render(request, 'BASE.html', {'forum_template_content': forum_template_content})

def forum_most_followed_direct(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    context = most_followed(request, forum_slug)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        most_followed_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'most_followed_content_template' : most_followed_content_template,
            'forum' : forum
        }
        return render(request, 'forum.html', contextio)
    else:
        raise Http404('Page not found')

@login_required
def follow_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    user = request.user

    if not question.is_followed_by(user):
        question.followers.add(user)
        response = {'success': 'Question has been followed successfully.'}
    else:
        question.followers.remove(user)
        response = {'success': 'Question has been unfollowed successfully.'}

    return JsonResponse(response)


@login_required
def upvote_question(request, question_id):
    question = get_object_or_404(Question, id=question_id) 
    user = request.user

    if not question.is_upvoted_by(user):
        if question.is_downvoted_by(user):
            question.downvotes.remove(user)
        question.upvotes.add(user)
        send_notification(question.author, f'{request.user.username} upvoted your question : "{question.title}"', f'/questions/{question.id}/')
        response = {'success': 'Question upvoted successfully.'}
    else:
        question.upvotes.remove(user)
        response = {'success': 'Question un-upvoted successfully.'}

    return JsonResponse(response)

@login_required
def downvote_question(request, question_id):
    question = get_object_or_404(Question, id=question_id) 
    user = request.user

    if not question.is_downvoted_by(user):
        if question.is_upvoted_by(user):
            question.upvotes.remove(user)
        question.downvotes.add(user)
        response = {'success': 'Question downvoted successfully.'}
    else:
        question.downvotes.remove(user)
        response = {'success': 'Question un-downvoted successfully.'}

    return JsonResponse(response)

@login_required
def upvote_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id) 
    user = request.user

    if not answer.is_upvoted_by(user):
        if answer.is_downvoted_by(user):
            answer.downvotes.remove(user)

        answer.upvotes.add(user)
        send_notification(answer.author, f'{request.user.username} upvoted your answer : "{answer.content}"', f'/answers/{answer.id}/')
        response = {'success': 'Answer upvoted successfully.'}
    else:
        answer.upvotes.remove(user)
        response = {'success': 'Answer un-upvoted successfully.'}

    return JsonResponse(response)

@login_required
def downvote_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id) 
    user = request.user

    if not answer.is_downvoted_by(user):
        if answer.is_upvoted_by(user):
            answer.upvotes.remove(user)

        answer.downvotes.add(user)
        response = {'success': 'Answer downvoted successfully.'}
    else:
        answer.downvotes.remove(user)
        response = {'success': 'Answer un-downvoted successfully.'}

    return JsonResponse(response)


@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return JsonResponse({'success': True})

