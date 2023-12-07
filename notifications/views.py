from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Notification

# Create your views here.
@login_required
def notifications(request, username):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'notifications': notifications,
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'notifications.html', context)
    else:
        notifications_template_content = render_to_string('notifications.html', context)
        return render(request, 'BASE.html', {'notifications_template_content': notifications_template_content,})
