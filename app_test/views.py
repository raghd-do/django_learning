from django.shortcuts import redirect
from django.http import JsonResponse
from .models import userProfile
from .tasks import add, multiply


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

def add_task(request, x, y):
     add_result = add(x, y)
     return JsonResponse({"result": add_result})

def multiply_task(request, x, y):
     multiply_result = multiply(x, y)
     return JsonResponse({"result": multiply_result})