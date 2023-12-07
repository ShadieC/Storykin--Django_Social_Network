from django.db import models
from django.contrib.auth.models import User
from components.models import Post,PostComment,ArticleComment,BookReview
from forum.models import Question, Answer, AnswerComment

# Create your models here.

class PostCommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    post_comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class PostReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class ArticleCommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    article_comment = models.ForeignKey(ArticleComment, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class BookReviewReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    book_review = models.ForeignKey(BookReview, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class QuestionReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class AnswerReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)

class AnswerCommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    answer_comment = models.ForeignKey(AnswerComment, on_delete=models.CASCADE, related_name='report')
    count = models.IntegerField(default=0)