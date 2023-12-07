from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('email-verification/', views.email_verification, name='email_verification'),
    # login
    path('login/', auth_views.LoginView.as_view(extra_context={'template': 'base.html'}), name="login"),
    path('ax/login/', auth_views.LoginView.as_view(extra_context={'template': 'blank.html'}), name="ajax-login"),
    # reset password
    # restore password urls
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    path("password-reset/confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm",),
    path("password-reset/complete/",auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]
