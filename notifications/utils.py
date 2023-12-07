from .models import Notification

def send_notification(user, message, url):
    notification = Notification(user=user, message=message, url=url)
    notification.save()