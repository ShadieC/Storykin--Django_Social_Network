from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect,Http404
from components.models import Post,PostComment,Article,Book,ArticleComment,BookReview
from phases.models import Phase
from forum.models import Answer,Question,AnswerComment
from .models import HomePage,Testimonial,Profile,Subscriber
from forum.models import Forum
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django_social_share.templatetags import social_share
import braintree
from django.utils.text import slugify
# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id = 'tscvt5933c6cmkjr',
        public_key = 'x9qj2fs9cstmp6yg',
        private_key = 'b317fd77bbba9769d1f416aa0b036588'
    )
)

def Base(request):
    template = loader.get_template('BASE.html')
    context = {}
    
    return HttpResponse(template.render(context, request))

def Home(request):
    page_text = get_object_or_404(HomePage, identifier="ShadieX")
    testimonials = Testimonial.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')
    articles = Article.objects.all().order_by('-created_at')
    books = Book.objects.all().order_by('-title')

    context = {
        'page_text': page_text,
        'testimonials':testimonials,
        'posts':posts,
        'user': request.user,
        'articles': articles,
        'books':books,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            return render(request, 'home2.html', context)
        else:
            return render(request, 'home.html', context)
    else:
        if request.user.is_authenticated:
            home_template_content = render_to_string('home2.html', context)
        else:
            home_template_content = render_to_string('home.html', context)
        return render(request, 'BASE.html', {'home_template_content': home_template_content,})

def Donate(request):
    client_token = gateway.client_token.generate()

    context = {
        'client_token': client_token
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'donate.html', context)
    else:
        donate_template_content = render_to_string('donate.html', context)
        return render(request, 'BASE.html', {'donate_template_content': donate_template_content,})

def UserCounts(request, username):
    user = get_object_or_404(User, username=username)
    postscount = Post.objects.filter(author=user).count()
    questionscount = Question.objects.filter(author=user).count()
    answerscount = Question.objects.filter(author=user).count()
    likedcount = user.post_likes.all().count()

    counts = {
        'postscount' : postscount,
        'questionscount' : questionscount,
        'answerscount' : answerscount,
        'likedcount' : likedcount
    }

    return counts
    
def UserDetails(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=profile_user)
    request_user_profile = get_object_or_404(Profile, user=request.user)
    followers = profile.get_followers_count()
    following = profile_user.profile_following.all().count()
    phase_subscribed = profile_user.phase_subscribed.all().count()

    details = {
        'phase_subscribed' : phase_subscribed,
        'following' : following,
        'profile_user' : profile_user,
        'profile' : profile,
        'followers' : followers,
        'user' : request.user,
        'request_user_profile': request_user_profile,
    }

    return details

def UserProfile(request, username):
    details = UserDetails(request, username)
    posts = Post.objects.filter(author=details["profile_user"]).order_by('-created_at')
    counts = UserCounts(request, username)
    context = {
        'posts' : posts,
        'user': request.user,
    }
    context.update(details)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        posts_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'posts_content_template' : posts_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        return render(request, 'profile.html', contextio)
    else:
        posts_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'posts_content_template' : posts_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        profile_template_content = render_to_string('profile.html', contextio)
        return render(request, 'BASE.html', {'profile_template_content': profile_template_content,})

def user_posts_list(request, username):
    details = UserDetails(request, username)
    posts = Post.objects.filter(author=details["profile_user"]).order_by('-created_at')
    context = {        
        'user': request.user,
        'posts' : posts
    }
    return context

def user_posts(request, username):
    counts = UserCounts(request, username)
    context = user_posts_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/posts.html', context)
    else:
        details = UserDetails(request, username)
        posts_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'posts_content_template' : posts_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        profile_template_content = render_to_string('profile.html', contextio)
        return render(request, 'BASE.html', {'profile_template_content': profile_template_content})

def user_posts_direct(request, username):
    counts = UserCounts(request, username)
    context = user_posts_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        details = UserDetails(request, username)
        posts_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'posts_content_template' : posts_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        return render(request, 'profile.html', contextio)
    else:
        raise Http404('Page not found')


def user_questions_list(request, username):
    details = UserDetails(request, username)
    questions = Question.objects.filter(author=details["profile_user"]).order_by('-created_at')
    counts = UserCounts(request, username)
    context = {        
        'user': request.user,
        'questions' : questions
    }
    return context

def user_questions(request, username):
    counts = UserCounts(request, username)
    context = user_questions_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/questions.html', context)
    else:
        details = UserDetails(request, username)
        questions_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'questions_content_template' : questions_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        profile_template_content = render_to_string('profile.html', contextio)
        return render(request, 'BASE.html', {'profile_template_content': profile_template_content})

def user_questions_direct(request, username):
    counts = UserCounts(request, username)
    context = user_questions_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        details = UserDetails(request, username)
        questions_content_template = render_to_string('lists/questions.html', context)
        contextio = {
            'questions_content_template' : questions_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        return render(request, 'profile.html', contextio)
    else:
        raise Http404('Page not found')


def user_answers_list(request, username):
    details = UserDetails(request, username)
    answers = Question.objects.filter(author=details["profile_user"]).order_by('-created_at')
    context = {        
        'user': request.user,
        'answers' : answers
    }
    return context

def user_answers(request, username):
    counts = UserCounts(request, username)
    context = user_answers_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/answers.html', context)
    else:
        details = UserDetails(request, username)
        answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'answers_content_template' : answers_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        profile_template_content = render_to_string('profile.html', contextio)
        return render(request, 'BASE.html', {'profile_template_content': profile_template_content})

def user_answers_direct(request, username):
    counts = UserCounts(request, username)
    context = user_answers_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        details = UserDetails(request, username)
        answers_content_template = render_to_string('lists/answers.html', context)
        contextio = {
            'answers_content_template' : answers_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        return render(request, 'profile.html', contextio)
    else:
        raise Http404('Page not found')

def user_liked_posts_list(request, username):
    details = UserDetails(request, username)
    posts = details["profile_user"].post_likes.all
    context = {        
        'user': request.user,
        'posts' : posts
    }
    return context

def user_liked_posts(request, username):
    counts = UserCounts(request, username)
    context = user_liked_posts_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'lists/posts.html', context)
    else:
        details = UserDetails(request, username)
        liked_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'liked_content_template' : liked_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        profile_template_content = render_to_string('profile.html', contextio)
        return render(request, 'BASE.html', {'profile_template_content': profile_template_content})

def user_liked_posts_direct(request, username):
    counts = UserCounts(request, username)
    context = user_liked_posts_list(request, username)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        details = UserDetails(request, username)
        liked_content_template = render_to_string('lists/posts.html', context)
        contextio = {
            'liked_content_template' : liked_content_template,
        }
        contextio.update(counts)
        contextio.update(details)
        return render(request, 'profile.html', contextio)
    else:
        raise Http404('Page not found')


@login_required
def follow_profile(request, username):
    to_follow = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=to_follow)
    user = request.user

    if not profile.is_followed_by(user):
        profile.followers.add(user)
        response = {'success': 'User has been followed successfully.'}
    else:
        profile.followers.remove(user)
        response = {'success': 'User has been unfollowed successfully.'}

    return JsonResponse(response)

@login_required
def block_profile(request, username):
    my_profile = get_object_or_404(Profile, user=request.user)
    user = get_object_or_404(User, username=username)
    response = {}

    if not my_profile.has_blocked(user):
        my_profile.blocked.add(user)
        message = {'success': 'User has been blocked successfully.'}
        posts = Post.objects.filter(author=user)
        data = [{'id': post.id} for post in posts]
        response["message"] = message
        response["data"] = data
    else:
        my_profile.blocked.remove(user)
        message = {'success': 'User has been unblocked successfully.'}
        data = []
        response["message"] = message
        response["data"] = data

    return JsonResponse(response)

def Forum_Display(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    questions = Question.objects.all()[:10]
    questions_content_template = render_to_string('lists/questions.html', {'user': request.user,'questions':questions})
    
    context = {
        'questions_content_template' : questions_content_template,
        'forum' : forum
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'forum.html', context)
    else:
        forum_template_content = render_to_string('forum.html', context)
        return render(request, 'BASE.html', {'forum_template_content': forum_template_content})

def contact(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'shadyychimboza@gmail.com',  # Replace with your email address
            ['shadyychimboza@gmail.com'],  # Replace with your email address
            fail_silently=False,
        )
        response = {'status': 'successfull'}

    return JsonResponse(response)

def SearchView(request, tabname): 
    if tabname == 'posts' or tabname == 'reads' or tabname == 'questions' or tabname == 'answers' or tabname == 'profiles' or tabname == 'phases': 
        kerko = request.GET.get('q','')  
        phases = Phase.objects.filter(name__contains=kerko)
        profiles = Profile.objects.filter(user__username__contains=kerko)
        posts = Post.objects.filter(body__contains=kerko)
        articles = Article.objects.filter(body__contains=kerko)
        books = Book.objects.filter(title__contains=kerko)
        questions = Question.objects.filter(title__contains=kerko)
        answers = Answer.objects.filter(content__contains=kerko)

        search_posts_content_template = render_to_string('lists/posts.html', {'user': request.user,'posts': posts})
        search_questions_content_template = render_to_string('lists/questions.html', {'user': request.user,'questions': questions})
        search_answers_content_template = render_to_string('lists/answers.html', {'user': request.user,'answers': answers})
        search_reads_content_template = render_to_string('lists/reads.html', {'user': request.user,'articles': articles,'books': books,})
        search_profiles_content_template = render_to_string('lists/profiles.html', {'user': request.user,'profiles': profiles})
        search_phases_content_template = render_to_string('lists/phases.html', {'phases': phases})

        context = {
            'search_phases_content_template': search_phases_content_template,
            'search_profiles_content_template': search_profiles_content_template,
            'search_posts_content_template': search_posts_content_template,
            'search_questions_content_template': search_questions_content_template,
            'search_answers_content_template': search_answers_content_template,
            'search_reads_content_template': search_reads_content_template,
            'kerko': kerko,
        }
            
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return render(request, 'search.html', context)
        else:
            search_template_content = render_to_string('search.html', context)
            return render(request, 'BASE.html', {'search_template_content': search_template_content,})
    else:
        raise Http404('Search page not found')


def get_phase_options(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == "POST":
            category = request.POST.get('category')
            if category == 'emotional':
                phase_options = Phase.objects.filter(phase_type='Emotional Phase')
            else:
                phase_options = Phase.objects.filter(phase_type='Life Phase')

            data = [{'name': phase.name, 'slug': phase.slug} for phase in phase_options]

            return JsonResponse(data, safe=False)

        elif request.method == "GET":
            phase_options = Phase.objects.filter(phase_type='Emotional Phase')
            context = {
                'phase_options': phase_options, 
            }
            return render(request, 'phase-type-select.html', context)

def post_options(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    username = post.author.username
    post_author = get_object_or_404(User, username=username)
    post_author_profile = get_object_or_404(Profile, user=post_author)
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    context = {
        'post': post, 
        'user': user,
        'post_author_profile': post_author_profile,
        'post_author': post_author,
        'user_profile':user_profile,
    }
    return render(request, 'menu_options/post_options.html', context)

def question_options(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    username = question.author.username
    question_author = get_object_or_404(User, username=username)
    question_author_profile = get_object_or_404(Profile, user=question_author)
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    context = {
        'question': question, 
        'user': user,
        'question_author_profile': question_author_profile,
        'question_author': question_author,
        'user_profile':user_profile,
    }
    return render(request, 'menu_options/question_options.html', context)

def answer_options(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    username = answer.author.username
    answer_author = get_object_or_404(User, username=username)
    answer_author_profile = get_object_or_404(Profile, user=answer_author)
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    context = {
        'answer': answer, 
        'user': user,
        'answer_author_profile': answer_author_profile,
        'answer_author': answer_author,
        'user_profile':user_profile,
    }
    return render(request, 'menu_options/answer_options.html', context)

def post_comment_options(request, post_comment_id):
    comment = get_object_or_404(PostComment, id=post_comment_id)
    user = request.user
    delete_url = reverse('delete_post_comment', args=[str(comment.id)])
    report_url = reverse('report_post_comment', args=[str(comment.id)])

    context = {
        'comment': comment, 
        'user': user,
        'report_url': report_url,
        'delete_url': delete_url,
    }

    return render(request, 'menu_options/comment_options.html', context)

def answer_comment_options(request, answer_comment_id):
    comment = get_object_or_404(AnswerComment, id=answer_comment_id)
    user = request.user
    delete_url = reverse('delete_answer_comment', args=[str(comment.id)])
    report_url = reverse('report_answer_comment', args=[str(comment.id)])

    context = {
        'comment': comment, 
        'user': user,
        'report_url': report_url,
        'delete_url': delete_url,
    }

    return render(request, 'menu_options/comment_options.html', context)

def article_comment_options(request, article_comment_id):
    comment = get_object_or_404(ArticleComment, id=article_comment_id)
    delete_url = reverse('delete_article_comment', args=[str(comment.id)])
    report_url = reverse('report_article_comment', args=[str(comment.id)])

    user = request.user
    context = {
        'comment': comment, 
        'user': user,
        'report_url': report_url,
        'delete_url': delete_url,
    }

    return render(request, 'menu_options/comment_options.html', context)

def book_review_options(request, book_review_id):
    comment = get_object_or_404(BookReview, id=book_review_id)
    delete_url = reverse('delete_book_review', args=[str(comment.id)])
    report_url = reverse('report_book_review', args=[str(comment.id)])

    user = request.user
    context = {
        'comment': comment, 
        'user': user,
        'report_url': report_url,
        'delete_url': delete_url,
    }

    return render(request, 'menu_options/comment_options.html', context)

@login_required
def User_logout(request):
    logout(request)
    return redirect('home')

def Feedback(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'feedback.html')
    else:
        feedback_template_content = render_to_string('feedback.html')
        return render(request, 'BASE.html', {'feedback_template_content': feedback_template_content,})

@login_required
def edit_profile(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response = {}
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        pro_image = request.FILES.get('pro_image')
        user_username = request.POST.get('username')
        email = request.POST.get('email')

        user = request.user
        Profile.objects.filter(user=user).update(bio=bio)
        if pro_image :
            profile = get_object_or_404(Profile, user=user)
            profile.pro_image = pro_image
            profile.save()

        forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root','email', 'user', 'join', 'sql', 'static', 'python', 'delete']
        if user_username.lower() in forbidden_users:
            response['status'] = "error"
            response['error'] = "The username entered is prohibibited,choose another one"
            return JsonResponse(response)

        if '@' in user_username or '+' in user_username or '-' in user_username:
            response['status'] = "error"
            response['error'] = "This is an Invalid user, Do not user these chars: @ , - , +"
            return JsonResponse(response)

        if user_username == "":
            response['status'] = "error"
            response['error'] = "Username cannot be blank. Fill in something."
            return JsonResponse(response)

        if User.objects.filter(username__iexact=user_username).exists():
            if user.username != user_username:
                response['status'] = "error"
                response['error'] = "User with this username already exists."
                return JsonResponse(response)

        User.objects.filter(id=user.id).update(first_name = first_name, last_name = last_name, email = email, username=user_username)

        response = {'status': 'successfull'}

    return JsonResponse(response)

def newsletter_subscribe(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response = {}
        email = request.POST.get('email')

        new_subscriber = Subscriber(email = email)
        new_subscriber.save()

        response = {'success': 'You have subscribed to the newsletter successfully'}

    return JsonResponse(response)


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Check if the new passwords match
        if new_password1 != new_password2:
            return JsonResponse({'error': 'New passwords do not match'})

        # Use Django's built-in method to change the password
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user) # to update session with new password
            return JsonResponse({'success': 'Password changed successfully'})
        else:
            return JsonResponse({'error': 'Old password is incorrect'})

@login_required
def delete_account(request):
    # Delete the user account and logout
    request.user.delete()
    logout(request)
    return redirect('home')  # Redirect to homepage or any other page after deletion

@login_required
def open_settings(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    context = {
        'user' : user,
        'profile' : profile,
    }
    return render(request, 'settings.html', context)

def share_post(request, post_id):
    element = get_object_or_404(Post, id=post_id)
    link_url = element.get_absolute_url
    link_title = element.title
    link_text = "Check out this artcle: "+ element.title +" . Available on phases!"

    context = {
        'link_url' : link_url,
        'link_title' : link_title,
        'link_text' : link_text,
    }
    return render(request, 'share_to.html', context)

def share_article(request, article_id):
    element = get_object_or_404(Article, id=article_id)
    link_url = element.get_absolute_url
    link_title = element.title
    link_text = "Check out this artcle: "+ element.title +" . Available on phases!"

    context = {
        'link_url' : link_url,
        'link_title' : link_title,
        'link_text' : link_text,
    }
    return render(request, 'share_to.html', context)

def share_question(request, question_id):
    element = get_object_or_404(Question, id=question_id)
    link_url = element.get_absolute_url
    link_title = element.title
    link_text = "Check out this artcle: "+ element.title +" . Available on phases!"

    context = {
        'link_url' : link_url,
        'link_title' : link_title,
        'link_text' : link_text,
    }
    return render(request, 'share_to.html', context)

def share_answer(request, answer_id):
    element = get_object_or_404(Answer, id=answer_id)
    link_url = element.get_absolute_url
    link_title =  element.question.title
    link_text = "Check out this artcle: "+ element.question.title +" . Available on phases!"

    context = {
        'link_url' : link_url,
        'link_title' : link_title,
        'link_text' : link_text,
    }
    return render(request, 'share_to.html', context)

def share_website(request):
    link_url = reverse_lazy('home')
    link_title = "Check out this artcle:  . Available on phases!"
    link_text = "Check out this artcle:  . Available on phases!"

    context = {
        'link_url' : link_url,
        'link_title' : link_title,
        'link_text' : link_text,
    }
    return render(request, 'share_to.html', context)