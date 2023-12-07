from django.shortcuts import render
from .models import Achievement
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

# Create your views here.

@login_required
def Achievements(request):
    user = request.user
    achievements = Achievement.objects.filter(user=user).order_by()

    context = {
        'achievements':achievements,
        'user':user,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'achievements.html', context)
    else:
        achievements_template_content = render_to_string('achievements.html', context)
        return render(request, 'BASE.html', {'achievements_template_content': achievements_template_content,})