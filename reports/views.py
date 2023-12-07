from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from components.models import Post,PostComment,ArticleComment,BookReview
from forum.models import Question, Answer, AnswerComment
from .models import PostReport,PostCommentReport,ArticleCommentReport,BookReviewReport,QuestionReport,AnswerReport,AnswerCommentReport
# Create your views here.

def report_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id) 

    if AnswerReport.objects.filter(answer=answer).exists():
        report = get_object_or_404(AnswerReport, answer=answer)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = AnswerReport(answer=answer, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 

    if PostReport.objects.filter(post=post).exists():
        report = get_object_or_404(PostReport, post=post)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = PostReport(post=post, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_question(request, question_id):
    question = get_object_or_404(Question, id=question_id) 

    if QuestionReport.objects.filter(question=question).exists():
        report = get_object_or_404(QuestionReport, question=question)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = QuestionReport(question=question, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_post_comment(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, id=post_comment_id) 

    if PostCommentReport.objects.filter(post_comment=post_comment).exists():
        report = get_object_or_404(PostCommentReport, post_comment=post_comment)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = PostCommentReport(post_comment=post_comment, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_answer_comment(request, answer_comment_id):
    answer_comment = get_object_or_404(AnswerComment, id=answer_comment_id) 

    if AnswerCommentReport.objects.filter(answer_comment=answer_comment).exists():
        report = get_object_or_404(AnswerCommentReport, answer_comment=answer_comment)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = AnswerCommentReport(answer_comment=answer_comment, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_article_comment(request, article_comment_id):
    article_comment = get_object_or_404(ArticleComment, id=article_comment_id) 

    if ArticleCommentReport.objects.filter(article_comment=article_comment).exists():
        report = get_object_or_404(ArticleCommentReport, article_comment=article_comment)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = ArticleCommentReport(article_comment=article_comment, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)

def report_book_review(request, book_review_id):
    book_review = get_object_or_404(BookReview, id=book_review_id) 

    if BookReviewReport.objects.filter(book_review=book_review).exists():
        report = get_object_or_404(BookReviewReport, book_review=book_review)
        report.count +=1
        report.save()
        response = {'success': 'Your report has been sent successfully.'}
    else:
        try:
            user = request.user
        except:
            user=None
        report = BookReviewReport(book_review=book_review, user=user)
        report.save()
        response = {'success': 'Your report has been sent successfully.'}

    return JsonResponse(response)