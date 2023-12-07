from django.urls import path
from . import views

urlpatterns = [
    path('<str:forum_slug>/questions/', views.forum_questions, name='forum_questions'),
    path('<str:forum_slug>/answers/', views.forum_answers, name='forum_answers'),
    path('<str:forum_slug>/best-answers/', views.forum_best_answers, name='forum_best_answers'),
    path('<str:forum_slug>/most-followed/', views.forum_most_followed, name='forum_most_followed'),
    path('upvote_answer/<int:answer_id>/', views.upvote_answer, name='upvote_answer'),
    path('downvote_answer/<int:answer_id>/', views.downvote_answer, name='downvote_answer'),
    path('upvote_question/<int:question_id>/', views.upvote_question, name='upvote_question'),
    path('downvote_question/<int:question_id>/', views.downvote_question, name='downvote_question'),
    path('follow_question/<int:question_id>/', views.follow_question, name='follow_question'),

    path('<str:forum_slug>/questions/direct_load/', views.forum_questions_direct, name='forum_questions_direct'),
    path('<str:forum_slug>/answers/direct_load/', views.forum_answers_direct, name='forum_answers_direct'),
    path('<str:forum_slug>/best-answers/direct_load/', views.forum_best_answers_direct, name='forum_best_answers_direct'),
    path('<str:forum_slug>/most-followed/direct_load/', views.forum_most_followed_direct, name='forum_most_followed_direct'),
]