import re
from django import template
from django.utils.html import conditional_escape
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

def create_hashtag_link(tag):
    #url = 'tags/{}/'.format(tag)
    url = reverse("hashtags", args=(tag,))
    return '<a href="{}">#{}</a>'.format(url, tag)

@register.filter(name='hashtag_links' ,is_safe=True)
def hashtag_links(value):
  return mark_safe( re.sub(r"#(\w+)", lambda m: create_hashtag_link(m.group(1)), conditional_escape(value)))

def create_user_link(user):
    url = reverse("otherprofile", args=(user,))
    return '<a href="{}">@{}</a>'.format(url, user)

@register.filter(name='user_links' ,is_safe=True)
def user_links(value):
  return mark_safe( re.sub(r"@(\w+)", lambda m: create_user_link(m.group(1)), conditional_escape(value)))