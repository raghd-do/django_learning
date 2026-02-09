from django.shortcuts import redirect
from django.http import JsonResponse
from .models import userProfile
from .tasks import add, multiply, create_user_profile, send_email, count_user_profiles, rename_user_profile


# Create your views here.
def index(request):
    if request.method == "GET":
        request.session['message'] = "You have been redirected!"
        return redirect('/redirect')
    elif request.method == "POST":
        request.session['message'] = "POST request received"
        return JsonResponse({"message": request.session.get("message")})
    
def redirect_view(request):
        return JsonResponse({"message": request.session.get("message", "No message set")})


def user_profile(request):
     return JsonResponse({"profiles": list(userProfile.objects.all().values())})

def add_user(request, first_name, last_name, email):
     user = userProfile.objects.create(first_name=first_name, last_name=last_name, email=email)
     sent_email = send_email.delay_on_commit(user_pk=user.id, subject="Welcome!", message=f"Hello {first_name}, your profile has been created.")
     return JsonResponse({"message": "User profile created", "sent_email": sent_email})

def add_task(request, x, y):
     add_result = add(x, y)
     return JsonResponse({"result": add_result})

def multiply_task(request, x, y):
     multiply_result = multiply(x, y)
     return JsonResponse({"result": multiply_result})