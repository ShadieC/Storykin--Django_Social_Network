from django.db import models
from phases.models import Phase
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.dispatch import Signal
from django.urls import reverse

# Create your models here.
#action = Signal(providing_args=['author','verb','target'])

class Forum(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ForumImages/',blank=True,null=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    slug = models.SlugField(default='none')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

def create_forum(sender, instance, created, **kwargs):
    if created:
       forum = Forum.objects.create(phase=instance)
       forum.name = instance.name
       forum.save()

post_save.connect(create_forum, sender=Phase)

class Question(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='QuestionImages/',null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted_questions', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_questions', blank=True)
    followers = models.ManyToManyField(User, related_name='answer_followers', blank=True)
    anonymous = models.BooleanField(default=False)

    def aggregate_count(self):
        return self.upvotes.count() - self.downvotes.count()

    def is_upvoted_by(self, user):
        return self.upvotes.filter(id=user.id).exists()

    def is_downvoted_by(self, user):
        return self.downvotes.filter(id=user.id).exists()

    def is_followed_by(self, user):
        return self.followers.filter(id=user.id).exists()

    def answers_count(self):
        return Answer.objects.filter(question=self).all().count()

    def get_absolute_url(self):
        return reverse('question', args=[str(self.id)])


class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='AnswerImages/',null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted_answers', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_answers', blank=True)
    admirers = models.ManyToManyField(User, related_name='answer_admirers', blank=True)
    anonymous = models.BooleanField(default=False)

    def aggregate_count(self):
        return self.upvotes.count() - self.downvotes.count()

    def is_admired_by(self, user):
        return self.admirers.filter(id=user.id).exists()

    def comments_count(self):
        return AnswerComment.objects.filter(answer=self).all().count()

    def is_upvoted_by(self, user):
        return self.upvotes.filter(id=user.id).exists()

    def is_downvoted_by(self, user):
        return self.downvotes.filter(id=user.id).exists()

    def get_absolute_url(self):
        return reverse('answer', args=[str(self.id)])

class AnswerComment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE , related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='answer_comment_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.body)

    @property
    def children(self):
        return AnswerComment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()


