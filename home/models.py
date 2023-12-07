from django.db import models
from components.models import Post
from forum.models import Question, Answer
from django.contrib.auth.models import User
from components.models import Post
from django.db.models.signals import post_save, post_delete

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    pro_image = models.ImageField(upload_to='ProfileImages/',null=True , blank=True)
    bio = models.TextField(max_length=150,null=True , blank=True)
    followers = models.ManyToManyField(User, related_name='profile_following', blank=True)
    blocked = models.ManyToManyField(User, related_name='profile_blocked', blank=True)
    posts_blacklist = models.ManyToManyField(Post, related_name='profile_posts_blacklist', blank=True)
    answers_blacklist = models.ManyToManyField(Answer, related_name='profile_answers_blacklist', blank=True)
    questions_blacklist = models.ManyToManyField(Question, related_name='profile_questions_blacklist', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_followers_count(self):
        return self.followers.count()

    def is_followed_by(self, user):
        return self.followers.filter(id=user.id).exists()

    def has_blocked(self, user):
        return self.blocked.filter(id=user.id).exists()

    def has_post_blacklisted(self, post):
        return self.posts_blacklist.filter(id=post.id).exists()

    def has_answer_blacklisted(self, answer):
        return self.answers_blacklist.filter(id=answer.id).exists()

    def has_question_blacklisted(self, question):
        return self.questions_blacklist.filter(id=question.id).exists()

def create_profile(sender, instance, created, **kwargs):
    if created:
       profile = Profile.objects.create(user=instance)
       profile.save()

post_save.connect(create_profile, sender=User)


class ProfileFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Subscriber(models.Model):
   email = models.EmailField(unique=True)

   def __str__(self):
       return self.email

class HomePage(models.Model):
    identifier = models.CharField(max_length=100,default="malaica")
    header_part_1 = models.CharField(max_length=100)
    header_part_2 = models.CharField(max_length=100)
    hero_section_text = models.TextField(max_length=1000)
    about_us_part_1 = models.TextField(max_length=1000)
    about_us_part_2 = models.TextField(max_length=1000)
    about_me = models.TextField(max_length=1000)

class Testimonial(models.Model):
    description = models.TextField(max_length=1000)
    username = models.CharField(max_length=100)
    image = models.FileField(default='images/default.jpg', upload_to='Testimonials',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']




