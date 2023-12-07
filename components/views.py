from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from notifications.utils import send_notification
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import AffiliateActivity,Post,Article,ArticleComment,Book,BookReview,PostComment,SocialFollow,ArticleReadingActivity
from forum.models import Question, Answer, AnswerComment, Forum
from phases.models import Phase
from home.models import Profile
from home.utils import find_similar_posts,find_similar_answers

# Create your views here.
def follow_social_platform(request):
    if request.method == 'POST' and request.is_ajax():
        platform = request.POST.get('platform')
        user = request.user

        # Check if the user has already followed the platform
        social_follow, created = SocialFollow.objects.get_or_create(user=user, platform=platform)

        if created:
            social_follow.followed = True
            social_follow.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

def Post_Details(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = PostComment.objects.filter(post=post,parent__isnull=True).all().prefetch_related('replies')
    no_of_comments = comments.count()

    context = {
        'post': post,
        'comments': comments,
        'no_of_comments': no_of_comments,
        'user': request.user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'post.html', context)
    else:
        post_template_content = render_to_string('post.html', context)
        return render(request, 'BASE.html', {'post_template_content': post_template_content})

@login_required
def create_post(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        content = request.POST.get('content')
        title = request.POST.get('title')
        anonymous_checkbox = request.POST.get('anonymous')
        image = request.FILES.get('image')
        phase_slug = request.POST.get('phase')
        phase = get_object_or_404(Phase, slug=phase_slug)

        if anonymous_checkbox:
            anonymous=True
        else:
            anonymous=False
        

        new_post = Post(body=content , author = request.user , phase=phase, image=image, title=title, anonymous=anonymous)
        new_post.save()

        profile = Profile.objects.get(user=request.user)
        followers = profile.followers.all()
        
        for follower in followers:
            send_notification(follower, f'{request.user.username} created a new post "{new_post.title}"', f'/posts/{new_post.id}/')

        return JsonResponse({'success': True})


def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            parent_id = request.POST.get('parent')
            parent = get_object_or_404(PostComment, id=parent_id)
        except:
            parent=None

        new_comment = PostComment(body=content , author = request.user , post=post , parent=parent)
        new_comment.save()
        new_id = new_comment.id
        send_notification(post.author, f'{request.user.username} commented on your post: "{post.title}"', f'/posts/{post.id}/')
        
        admirers = post.admirers.all()
        
        for admirer in admirers:
            send_notification(admirer, f'{request.user.username} commented on a post you follow: "{post.title}"', f'/posts/{post.id}/')

        return JsonResponse({'success': True})

    elif request.method == 'GET':
        comments = PostComment.objects.filter(post=post,parent__isnull=True).all().prefetch_related('replies')

        return render(request, 'post.html', {'comments': comments,'post':post,'user': request.user,})

@login_required
def create_question(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        title = request.POST.get('title')
        anonymous_checkbox = request.POST.get('anonymous')
        if anonymous_checkbox:
            anonymous=True
        else:
            anonymous=False
        image = request.FILES.get('image')
        forum_slug = request.POST.get('question-forum')
        forum = get_object_or_404(Forum, slug=forum_slug)

        new_question = Question(title=title , author = request.user , forum=forum, image=image, anonymous=anonymous)
        new_question.save()

        profile = Profile.objects.get(user=request.user)
        followers = profile.followers.all()
        
        for follower in followers:
            send_notification(follower, f'{request.user.username} created a new question "{question.title}"', f'/question/{question.id}/')

        return JsonResponse({'success': True})

@login_required
def answer_question(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        content = request.POST.get('content')
        anonymous_checkbox = request.POST.get('anonymous')
        if anonymous_checkbox:
            anonymous=True
        else:
            anonymous=False
        image = request.FILES.get('image')
        question_id = request.POST.get('answer-question')
        question = get_object_or_404(Question, id=question_id)


        new_answer = Answer(content=content, question=question  , author = request.user , image=image, anonymous=anonymous)
        new_answer.save()

        send_notification(question.author, f'{request.user.username} answered your question "{question.title}"', f'/question/{question.id}/')

        followers = question.followers.all()
        
        for follower in followers:
            send_notification(follower, f'{request.user.username} answered your question "{question.title}"', f'/question/{question.id}/')

        return JsonResponse({'success': True})

def Question_Details(request,question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question).order_by('-created_at')
    context = {'user': request.user,'answers' : answers}
    answers_content_template = render_to_string('lists/answers.html', context)

    contextio = {
        'question': question,
        'answers_content_template': answers_content_template,
        'user': request.user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'question.html', contextio)
    else:
        question_template_content = render_to_string('question.html', contextio)
        return render(request, 'BASE.html', {'question_template_content': question_template_content,})


def Article_Details(request,article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = ArticleComment.objects.filter(article=article)
    no_of_comments = comments.count()

    if request.user.is_authenticated:
        activity = ArticleReadingActivity(user=request.user, article=article)
        activity.save()

    context = {
        'article': article,
        'comments': comments,
        'no_of_comments': no_of_comments,
        'user': request.user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'article.html', context)
    else:
        article_template_content = render_to_string('article.html', context)
        return render(request, 'BASE.html', {'article_template_content': article_template_content,})

def article_comments(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            parent_id = request.POST.get('parent')
            parent = get_object_or_404(ArticleComment, id=parent_id)
        except:
            parent=None

        new_comment = ArticleComment(body=content , author = request.user , article=article , parent=parent)
        new_comment.save()
        new_id = new_comment.id
        send_notification(article.author, f'{request.user.username} commented on your article "{article.title}"', f'/articles/{article.id}/')

        return JsonResponse({'success': True})

    elif request.method == 'GET':
        comments = ArticleComment.objects.filter(article=article,parent__isnull=True).all().prefetch_related('replies')

        return render(request, 'article.html', {'comments': comments,'article':article,'user': request.user,})

def Book_Details(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = BookReview.objects.filter(book=book,parent__isnull=True).all().prefetch_related('replies')
    no_of_comments = comments.count()

    context = {
        'book': book,
        'comments': comments,
        'no_of_comments': no_of_comments,
        'user': request.user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'book.html', context)
    else:
        book_template_content = render_to_string('book.html', context)
        return render(request, 'BASE.html', {'book_template_content': book_template_content})

def book_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            parent_id = request.POST.get('parent')
            parent = get_object_or_404(PostComment, id=parent_id)
        except:
            parent=None

        new_review = BookReview(body=content , author = request.user , book=book , parent=parent)
        new_review.save()
        new_id = new_review.id
        send_notification(book.contributer, f'{request.user.username} commented on your book "{book.title}"', f'/books/{book.id}/')

        return JsonResponse({'success': True})

    elif request.method == 'GET':
        comments = BookReview.objects.filter(book=book,parent__isnull=True).all().prefetch_related('replies')

        return render(request, 'book.html', {'comments': comments,'book':book,'user': request.user,})

def AffiliateActivity(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user.is_authenticated:
        AffiliateActivity.objects.update_or_create(user=user, book=book) 

    return redirect(book.link)

def Answer_Details(request,answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    comments = AnswerComment.objects.filter(answer=answer,parent__isnull=True).all().prefetch_related('replies')
    no_of_comments = comments.count()

    context = {
        'answer': answer,
        'comments': comments,
        'no_of_comments': no_of_comments,
        'user': request.user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'answer.html', context)
    else:
        post_template_content = render_to_string('answer.html', context)
        return render(request, 'BASE.html', {'post_template_content': post_template_content})

def answer_comments(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            parent_id = request.POST.get('parent')
            parent = get_object_or_404(AnswerComment, id=parent_id)
        except:
            parent=None

        new_comment = AnswerComment(body=content , author = request.user , answer=answer , parent=parent)
        new_comment.save()
        new_id = new_comment.id
        send_notification(answer.author, f'{request.user.username} commented on your answer "{answer.content}"', f'/answers/{answer.id}/')

        admirers = answer.admirers.all()
        
        for admirers in admirers:
            send_notification(admirer, f'{request.user.username} commented on a answer you follow: "{answer.content}"', f'/answers/{answer.id}/')

        return JsonResponse({'success': True})

    elif request.method == 'GET':
        comments = AnswerComment.objects.filter(answer=answer,parent__isnull=True).all().prefetch_related('replies')

        return render(request, 'answer.html', {'comments': comments,'answer':answer,})


#============================================ Article related liking ==========================================================#
@login_required 
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id) 
    user = request.user

    if not article.is_liked_by(user):
        article.likes.add(user)
        send_notification(article.author, f'{request.user.username} liked your article : "{article.title}"', f'/comments/{article.id}/')
        response = {'success': 'Article liked successfully.'}
    else:
        article.likes.remove(user)
        response = {'success': 'Article unliked successfully.'}

    return JsonResponse(response)

@login_required
def like_article_comment(request, article_comment_id):
    article_comment = get_object_or_404(ArticleComment, id=article_comment_id) 
    user = request.user

    if not article_comment.is_liked_by(user):
        article_comment.likes.add(user)
        send_notification(article_comment.author, f'{request.user.username} liked your article comment : "{article_comment.body}"', f'/comments/{article_comment.id}/')
        response = {'success': 'Comment liked successfully.'}
    else:
        article_comment.likes.remove(user)
        response = {'success': 'Comment unliked successfully.'}

    return JsonResponse(response)
#====================================================== End ================================================================#


#============================================ Post related liking ==========================================================#
@login_required 
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    user = request.user

    if not post.is_liked_by(user):
        post.likes.add(user)
        send_notification(post.author, f'{request.user.username} liked your post : "{post.title}"', f'/comments/{post.id}/')
        response = {'success': 'Post liked successfully.'}
    else:
        post.likes.remove(user)
        response = {'success': 'Post unliked successfully.'}

    return JsonResponse(response)


@login_required
def like_post_comment(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, id=post_comment_id) 
    user = request.user

    if not post_comment.is_liked_by(user):
        post_comment.likes.add(user)
        send_notification(post_comment.author, f'{request.user.username} liked your comment : "{post_comment.body}"', f'/comments/{post_comment.id}/')
        response = {'success': 'Comment liked successfully.'}
    else:
        post_comment.likes.remove(user)
        response = {'success': 'Comment unliked successfully.'}

    return JsonResponse(response)

@login_required
def like_answer_comment(request, answer_comment_id):
    answer_comment = get_object_or_404(AnswerComment, id=answer_comment_id) 
    user = request.user

    if not answer_comment.is_liked_by(user):
        answer_comment.likes.add(user)
        send_notification(answer_comment.author, f'{request.user.username} liked your comment : "{answer_comment.body}"', f'/comments/{answer_comment.id}/')
        response = {'success': 'Comment liked successfully.'}
    else:
        post_comment.likes.remove(user)
        response = {'success': 'Comment unliked successfully.'}

    return JsonResponse(response)


#====================================================== End ===================================================================#

#============================================ Book related liking =============================================================#
@login_required 
def like_book(request, book_id):
    book = get_object_or_404(Book, id=book_id) 
    user = request.user

    if not book.is_liked_by(user):
        book.likes.add(user)
        response = {'success': 'Book liked successfully.'}
    else:
        book.likes.remove(user)
        response = {'success': 'Book unliked successfully.'}

    return JsonResponse(response)


@login_required
def like_book_review(request, book_review_id):
    book_review = get_object_or_404(BookReview, id=book_review_id) 
    user = request.user

    if not book_review.is_liked_by(user):
        book_review.likes.add(user)
        send_notification(book_review.author, f'{request.user.username} liked your comment : "{book_review.body}"', f'/comments/{book_review.id}/')
        response = {'success': 'Book Review liked successfully.'}
    else:
        book_review.likes.remove(user)
        response = {'success': 'Book Review unliked successfully.'}

    return JsonResponse(response)
#====================================================== End ===================================================================#

@login_required
def DeletePost(request, post_id):
    user = request.user
    Post.objects.filter(id=post_id, author=user).delete()
    
    return JsonResponse({'success': 'Post has been deleted successfully.'})

@login_required
def delete_post_comment(request, post_comment_id):
    user = request.user
    PostComment.objects.filter(id=post_comment_id, author=user).delete() 
    
    return JsonResponse({'success': 'Comment has been deleted successfully.'})

@login_required
def delete_answer_comment(request, answer_comment_id):
    user = request.user
    AnswerComment.objects.filter(id=answer_comment_id, author=user).delete() 
    
    return JsonResponse({'success': 'Comment has been deleted successfully.'})

@login_required
def delete_article_comment(request, article_comment_id):
    user = request.user
    ArticleComment.objects.filter(id=article_comment_id, author=user).delete() 
    
    return JsonResponse({'success': 'Comment has been deleted successfully.'})

@login_required
def delete_book_review(request, book_review_id):
    user = request.user
    BookReview.objects.filter(id=book_review_id, author=user).delete() 
    
    return JsonResponse({'success': 'Comment has been deleted successfully.'})

@login_required
def DeleteAnswer(request, answer_id):
    user = request.user
    Answer.objects.filter(id=answer_id, author=user).delete()
    
    return JsonResponse({'success': 'Answer has been deleted successfully.'})

@login_required
def DeleteQuestion(request, question_id):
    user = request.user
    Question.objects.filter(id=question_id, author=user).delete()
    
    return JsonResponse({'success': 'Question has been deleted successfully.'})

@login_required 
def admire_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    user = request.user

    if not post.is_admired_by(user):
        post.admirers.add(user)
        response = {'success': 'Notifications for post have been turned on successfully.'}
    else:
        post.admirers.remove(user)
        response = {'success': 'Notifications for post have been turned off successfully.'}

    return JsonResponse(response)

@login_required 
def admire_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id) 
    user = request.user

    if not answer.is_admired_by(user):
        answer.admirers.add(user)
        response = {'success': 'Notifications for answer have been turned on successfully.'}
    else:
        answer.admirers.remove(user)
        response = {'success': 'Notifications for answer have been turned off successfully.'}

    return JsonResponse(response)

@login_required
def hide_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = find_similar_posts(request, post_id)
    profile = get_object_or_404(Profile, user=request.user)
    response = {}

    if not profile.has_post_blacklisted(post):
        profile.posts_blacklist.add(post)
        for similar_post in posts['similar_posts']:
            profile.posts_blacklist.add(similar_post)
        message = {'success': 'Post and similar posts have been hidden successfully.'}
        data = [{'id': post.id} for post in posts['similar_posts']]
        response["message"] = message
        response["data"] = data
    else:
        profile.posts_blacklist.remove(post)
        for similar_post in posts['similar_posts']:
            profile.posts_blacklist.remove(similar_post)
        message = {'success': 'Post and similar posts have been unhidden successfully.'}
        data = []
        response["message"] = message
        response["data"] = data
    
    return JsonResponse(response)

@login_required
def hide_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answers = find_similar_answers(request, answer_id)
    profile = get_object_or_404(Profile, user=request.user)
    response = {}

    if not profile.has_answer_blacklisted(answer):
        profile.answers_blacklist.add(answer)
        for similar_answer in answers['similar_answers']:
            profile.answers_blacklist.add(similar_answer)
        message = {'success': 'Answer and similar answers have been hidden successfully.'}
        data = [{'id': answer.id} for answer in answers['similar_answers']]
        response["message"] = message
        response["data"] = data
    else:
        profile.answers_blacklist.remove(answer)
        for similar_answer in answers['similar_answers']:
            profile.answers_blacklist.remove(similar_answer)
        message = {'success': 'Answer and similar answers have been unhidden successfully.'}
        data = []
        response["message"] = message
        response["data"] = data
    
    return JsonResponse(response)

@login_required
def hide_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    questions = find_similar_questions(request, question_id)
    profile = get_object_or_404(Profile, user=request.user)
    response = {}

    if not profile.has_question_blacklisted(question):
        profile.questions_blacklist.add(question)
        for similar_question in questions['similar_questions']:
            profile.questions_blacklist.add(similar_question)
        message = {'success': 'Question and similar questions have been hidden successfully.'}
        data = [{'id': question.id} for question in questions['similar_questions']]
        response["message"] = message
        response["data"] = data
    else:
        profile.questions_blacklist.remove(question)
        for similar_question in questions['similar_questions']:
            profile.questions_blacklist.remove(similar_question)
        message = {'success': 'Question and similar questions have been unhidden successfully.'}
        data = []
        response["message"] = message
        response["data"] = data
    
    return JsonResponse(response)

