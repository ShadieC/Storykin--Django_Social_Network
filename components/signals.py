from django.db.models.signals import post_save
from django.db.models import Count
from django.dispatch import receiver
from .models import Post,PostComment,Article,ArticleComment,ArticleReadingActivity,AffiliateActivity,Book,BookReview,PostReadingActivity,SocialFollow
from achievements.models import Achievement
from forum.models import Answer 
from donations.models import Donation

@receiver(post_save, sender=Post)
def create_storyteller_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        post_count = Post.objects.filter(author=user).count()
        aggregate = (post_count/20)*5

        if post_count >= 20:
            Achievement.objects.filter(user=user, name="Storyteller Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Storyteller Achievement").update( aggregate=aggregate)


@receiver(post_save, sender=Answer)
def create_community_contributor_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        answers_count = Answer.objects.filter(author=user).values('question').distinct().count()
        aggregate = (answers_count/20)*5

        if answers_count >= 20:
            Achievement.objects.filter(user=user, name="Community Contributor Achievement").update(defaults={'has_finished': True}, aggregate=5.00) 
        else:
            Achievement.objects.filter(user=user, name="Community Contributor Achievement").update(aggregate=aggregate)
          

@receiver(post_save, sender=PostComment)
def create_empathy_champion_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        posts_commented_count = PostComment.objects.filter(author=user).values('post').distinct().count()
        aggregate = (posts_commented_count/20)*5

        if posts_commented_count >= 20:
            Achievement.objects.filter(user=user, name="Empathy Champion Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Empathy Champion Achievement").update(aggregate=aggregate)


@receiver(post_save, sender=Post)
def create_inspirational_speaker_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        post_count = Post.objects.annotate(num_likes=Count('likes'), num_comments=Count('comment')).filter(author=user, num_likes__gte=1000, num_comments__gte=200).count()
        aggregate = (post_count/10)*5

        if post_count >= 10:
            Achievement.objects.filter(user=user, name="Inspirational Speaker Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Inspirational Speaker Achievement").update(aggregate=aggregate)
   

@receiver(post_save, sender=PostComment)
def create_mentor_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        posts_commented_count = PostComment.objects.annotate(num_likes=Count('likes'), num_comments=Count('replies')).filter(author=user, num_likes__gte=1000, num_comments__gte=200).values('post').distinct().count()        
        aggregate = (posts_commented_count/20)*5

        if posts_commented_count >= 20:
            Achievement.objects.filter(user=user, name="Mentor Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Mentor Achievement").update(aggregate=aggregate)


@receiver(post_save, sender=ArticleComment)
@receiver(post_save, sender=BookReview)
def create_reviewer_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        article_comment_count = ArticleComment.objects.filter(author=user).values('article').distinct().count()
        book_review_count = BookReview.objects.filter(author=user).values('book').distinct().count()
        aggregate = ((article_comment_count/10)*2.5) + ((book_review_count/10)*2.5)

        if article_comment_count >= 10 and book_review_count >= 10:
            Achievement.objects.filter(user=user, name="Reviewer Achievement").update(defaults={'has_finished': True}, aggregate=5.00) 
        else:
            Achievement.objects.filter(user=user, name="Reviewer Achievement").update(aggregate=aggregate)


@receiver(post_save, sender=ArticleReadingActivity)
@receiver(post_save, sender=PostReadingActivity)
def create_explorer_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        articles_read_count = ArticleReadingActivity.objects.filter(user=user).values('phase').distinct().count()
        posts_read_count = PostReadingActivity.objects.filter(user=user).values('phase').distinct().count()
        aggregate = ((articles_read_count/10)*2.5) + ((posts_read_count/10)*2.5)

        if articles_read_count >= 10 and posts_read_count >= 10:
            Achievement.objects.filter(user=user, name="Explorer Achievement").update(defaults={'has_finished': True}, aggregate=5.00)  
        else:
            Achievement.objects.filter(user=user, name="Explorer Achievement").update(aggregate=aggregate)
  

@receiver(post_save, sender=Article)
@receiver(post_save, sender=Book)
def create_expert_contributor_badge(sender, instance, created, **kwargs):
        user = instance.contributer
        article_count = Article.objects.annotate(num_likes=Count('likes'), num_comments=Count('articlecomment')).filter(contributer=user, num_likes__gte=1000, num_comments__gte=200).count()
        book_count = Book.objects.annotate(num_likes=Count('likes'), num_comments=Count('bookreview')).filter(contributer=user, num_likes__gte=1000, num_comments__gte=200).count()
        aggregate = ((article_count/4)*2.5) + ((book_count/4)*2.5)

        if article_count >= 4 and book_count >= 4:
            Achievement.objects.filter(user=user, name="Expert Contributor Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Expert Contributor Achievement").update(aggregate=aggregate)


@receiver(post_save, sender=BookReview)
@receiver(post_save, sender=AffiliateActivity)
def create_bookworm_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        user_read_books = user.books_read.all()
        user_reviewed_books = user.reviews.all().values_list('book', flat=True)
   
        user_read_and_reviewed_books_count = user_read_books.filter(id__in=user_reviewed_books).count()
        aggregate = ((user_read_and_reviewed_books_count/5)*5)

        if user_read_and_reviewed_books_count >= 5:
            Achievement.objects.filter(user=user, name="Bookworm Achievement").update(defaults={'has_finished': True}, aggregate=5.00)
        else:
            Achievement.objects.filter(user=user, name="Bookworm Achievement").update(aggregate=aggregate)


@receiver(post_save, sender=ArticleReadingActivity)
@receiver(post_save, sender=AffiliateActivity)
def create_active_learner_badge(sender, instance, created, **kwargs):
    if created:
        if instance.user:
            user = instance.user
        else:
            user = instance.author
        articles_read_count = ArticleReadingActivity.objects.filter(user=user).values('article').distinct().count()
        books_read_count = AffiliateActivity.objects.filter(author=user).values('book').distinct().count()
        aggregate = ((articles_read_count/4)*2.5) + ((books_read_count/4)*2.5)

        if articles_read_count == 10 and books_read_count == 10:
            Achievement.objects.filter(user=user, name="Active Learner Achievement").update(defaults={'has_finished': True}, aggregate=5.00) 
        else:
            Achievement.objects.filter(user=user, name="Active Learner Achievement").update(aggregate=aggregate)
 

@receiver(post_save, sender=SocialFollow)
@receiver(post_save, sender=Donation)
def create_top_supporter_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if user is not None:
            social_follow_count = SocialFollow.objects.filter(user=user).values('platform').distinct().count()
            donation_count = Donation.objects.filter(user=user).count()

            total = social_follow_count + donation_count
            aggregate = ((total/3)*5)

            if total >= 3:
                Achievement.objects.filter(user=user, name="Top Supporter Achievement").update(defaults={'has_finished': True}, aggregate=5.00) 
            else:
                Achievement.objects.filter(user=user, name="Top Supporter Achievement").update(aggregate=aggregate)
 
