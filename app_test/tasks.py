from celery import shared_task
from .models import userProfile

@shared_task
def send_email(user_id, subject, message):
    try:
        user = userProfile.objects.get(id=user_id)
        print(f"Sending email to {user.email} with subject '{subject}' and message '{message}'")
        return None
    except userProfile.DoesNotExist:
        raise ValueError(f"User profile with id {user_id} does not exist")
