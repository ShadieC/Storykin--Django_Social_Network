from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate,login
from random import randint

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            log_user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if log_user is not None:
                login(request, log_user)
            return JsonResponse({'status': 'success'})
    else:
        user_form = UserRegistrationForm()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request,'account/register.html',{'user_form': user_form,'template': 'blank.html'})
    else:
        return render(request,'account/register.html',{'user_form': user_form,'template': 'base.html'})

def email_verification(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.POST.get('username')
        forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root','email', 'user', 'join', 'sql', 'static', 'python', 'delete','profile','donate','home','emotional-phases','life-phases','achievements','article','search','write-feedback','user-notifications','register','login','password-reset']
        if username.lower() in forbidden_users:
            return JsonResponse({'error': 'true'})

        if '@' in username or '+' in username or '-' in username:
            return JsonResponse({'error': 'true'})

        if User.objects.filter(username__iexact=username).exists():
            return JsonResponse({'error': 'true'})

        if  request.POST.get('password') != request.POST.get('password2'):
            return JsonResponse({'error': 'true'})

        email = request.POST.get('email')
        # Generate a six-digit verification code
        verification_code = str(randint(100000, 999999))
        # Send the verification code to the user's email
        send_mail(
            'Email Verification',
            f'Your storikyn.com verification code is {verification_code}, add this code to valid your registration',
            'shadyychimboza@gmail.com',
            [email],
            fail_silently=False,
        )
        return JsonResponse({'verification_code': verification_code,'error': 'false'})

