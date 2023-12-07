from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def shorten_time(value):
    time = timesince(value).split(", ")[0]
    if "week" in time:
        time = time.replace("week", "w")
    elif "day" in time:
        time = time.replace("day", "d")
    elif "month" in time:
        time = time.replace("month", "mo")
    elif "year" in time:
        time = time.replace("year", "y")
    return f"{time} ago"