from celery import shared_task
from .models import userProfile

@shared_task
def add(x, y):
    return x + y

@shared_task
def multiply(x, y):
    return x * y

@shared_task
def create_user_profile(first_name, last_name, email):
    userProfile.objects.create(first_name=first_name, last_name=last_name, email=email)

@shared_task
def send_email(user_pk, subject, message):
    try:
        user = userProfile.objects.get(pk=user_pk)
        print(f"Sending email to {user.email} with subject '{subject}' and message '{message}'")
        return None
    except userProfile.DoesNotExist:
        raise ValueError(f"User profile with id {user_pk} does not exist")

@shared_task
def count_user_profiles():
    return userProfile.objects.count()

@shared_task
def rename_user_profile(profile_id, new_first_name, new_last_name):
    try:
        profile = userProfile.objects.get(id=profile_id)
        profile.first_name = new_first_name
        profile.last_name = new_last_name
        profile.save()
        return f"Profile {profile_id} renamed to {profile.first_name} {profile.last_name}"
    except userProfile.DoesNotExist:
        return f"Profile with id {profile_id} does not exist"
