from django.db import models
from phases.models import Phase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class SocialFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    followed = models.BooleanField(default=False)

#========================================== Start Of Post Models =============================================================#
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='PostImages/',null=True , blank=True)
    admirers = models.ManyToManyField(User, related_name='post_admirers', blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

    def is_admired_by(self, user):
        return self.admirers.filter(id=user.id).exists()

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def comments_count(self):
        return PostComment.objects.filter(post=self).all().count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def likes_count(self):
        return self.likes.count()


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='postcomment_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.body)

    @property
    def children(self):
        return PostComment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def likes_count(self):
        return self.likes.count()

class PostReadingActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    phase = models.CharField(max_length=100)

    def update_phase(self):
        self.phase = self.post.phase
        self.save()
#============================================ End Of Post Models =============================================================#




#============================================ Start Of Article Models =========================================================#
class Article(models.Model):
    contributer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='ArticleImages/', null=True , blank=True)
    likes = models.ManyToManyField(User, related_name='article_likes', blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])

    def comments_count(self):
        return ArticleComment.objects.filter(article=self).all().count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def likes_count(self):
        return self.likes.count()

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='articlecomment_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.body)

    @property
    def children(self):
        return ArticleComment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def likes_count(self):
        return self.likes.count()

class ArticleReadingActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    phase = models.CharField(max_length=100)

    def update_phase(self):
        self.phase = self.article.phase
        self.save()
#============================================ End Of Article Models ==========================================================#


#============================================ Start Of Book Models ==========================================================#
class Book(models.Model):
    author = models.CharField(max_length=255)
    contributer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=False , blank=False)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, null=False , blank=False)
    image = models.ImageField(upload_to='BookImages/',null=False , blank=False)
    likes = models.ManyToManyField(User, related_name='book_likes', blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-added_at']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', args=[str(self.id)])

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def reviews_count(self):
        return BookReview.objects.filter(book=self).all().count()

    def likes_count(self):
        return self.likes.count()

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='book_review', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.body)

    @property
    def children(self):
        return BookReview.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def likes_count(self):
        return self.likes.count()


class AffiliateActivity(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_read')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)

    def update_link(self):
        self.phase = self.book.link
        self.save()
#==================================== End Of Book Models ==========================================================#