from django.urls import path
from . import views

urlpatterns = [
    path('report_post/<int:post_id>/', views.report_post, name='report_post'),
    path('report_answer/<int:answer_id>/', views.report_answer, name='report_answer'),
    path('report_question/<int:question_id>/', views.report_question, name='report_question'),
    path('report_post_comment/<int:post_comment_id>/', views.report_post_comment, name='report_post_comment'),
    path('report_answer_comment/<int:answer_comment_id>/', views.report_answer_comment, name='report_answer_comment'),
    path('report_article_comment/<int:article_comment_id>/', views.report_article_comment, name='report_article_comment'),
    path('report_book_review/<int:book_review_id>/', views.report_book_review, name='report_book_review'),
]