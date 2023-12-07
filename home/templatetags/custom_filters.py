from django import template
from django.utils.timesince import timesince
from datetime import datetime

register = template.Library()

@register.filter
def shorten_time(value):
    time = timesince(value).split(", ")[0]
    int_value = time.split()[0]
    if "seconds" in time:
        time = "".join([int_value,"s"])
    elif "second" in time:
        time = "".join([int_value,"s"]) 
    elif "minutes" in time:
        time = "".join([int_value,"m"])      
    elif "minute" in time:
        time = "".join([int_value,"m"]) 
    elif "hours" in time:
        time = "".join([int_value,"h"])       
    elif "hour" in time:
        time = "".join([int_value,"h"])      
    elif "days" in time:
        time = "".join([int_value,"d"])       
    elif "day" in time:
        time = "".join([int_value,"d"])      
    elif "weeks" in time:
        time = "".join([int_value,"w"])       
    elif "week" in time:
        time = "".join([int_value,"w"])        
    else :
        current_year = datetime.now().year
        months = {'01': 'Jan','02': 'Feb','03': 'Mar','04': 'Apr','05': 'May','06': 'Jun','07': 'Jul','08': 'Aug','09': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'}
        month = value.strftime('%m')
        if value.year == current_year:
            return f"{value.strftime('%d')} {months[month]}"  # Shortened month and day if same year
        else:
            return f"{value.strftime('%d')} {months[month]},{value.strftime('%Y')}" # Shortened month, day, and year if different year
    return f"{time} ago"

@register.filter
def glorified_time(value):
    current_year = datetime.now().year
    months = {'01': 'Jan','02': 'Feb','03': 'Mar','04': 'Apr','05': 'May','06': 'Jun','07': 'Jul','08': 'Aug','09': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'}
    month = value.strftime('%m')

    return f"{value.strftime('%d')} {months[month]},{value.strftime('%Y')}" # Shortened month, day, and year if different year

@register.filter
def shorten_forum_time(value):
    time = timesince(value).split(", ")[0]
    int_value = time.split()[0]
    if "seconds" in time:
        time = "".join([int_value,"s"])
    elif "second" in time:
        time = "".join([int_value,"s"]) 
    elif "minutes" in time:
        time = "".join([int_value,"m"])      
    elif "minute" in time:
        time = "".join([int_value,"m"]) 
    elif "hours" in time:
        time = "".join([int_value,"h"])       
    elif "hour" in time:
        time = "".join([int_value,"h"])      
    elif "days" in time:
        time = "".join([int_value,"d"])       
    elif "day" in time:
        time = "".join([int_value,"d"])      
    elif "weeks" in time:
        time = "".join([int_value,"w"])       
    elif "week" in time:
        time = "".join([int_value,"w"])        
    else :
        current_year = datetime.now().year
        months = {'01': 'Jan','02': 'Feb','03': 'Mar','04': 'Apr','05': 'May','06': 'Jun','07': 'Jul','08': 'Aug','09': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'}
        month = value.strftime('%m')
        if value.year == current_year:
            return f"on {value.strftime('%d')} {months[month]}"  # Shortened month and day if same year
        else:
            return f"on {value.strftime('%d')} {months[month]},{value.strftime('%Y')}" # Shortened month, day, and year if different year
    return f"{time} ago"