from celery import shared_task
from .models import userProfile
from django.utils import timezone

@shared_task
def send_email(user_id, subject, message):
    try:
        user = userProfile.objects.get(id=user_id)
        print(f"Sending email to {user.email} with subject '{subject}' and message '{message}'")
        return None
    except userProfile.DoesNotExist:
        raise ValueError(f"User profile with id {user_id} does not exist")
    
@shared_task
def daily_database_task():
    print("Running daily database task...")
    today = timezone.now().date()
    today_useers_count = userProfile.objects.filter(created_at__date=today).count()
    print(f"Number of user profiles created today: {today_useers_count}")
    return None
