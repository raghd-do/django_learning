from django.shortcuts import redirect
from django.http import JsonResponse
from .models import userProfile


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