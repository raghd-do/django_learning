from rest_framework.views import APIView
from django.http import JsonResponse
from .models import userProfile
# from .tasks import add, multiply, create_user_profile, send_email, count_user_profiles, rename_user_profile
# import logging
# logger = logging.getLogger(__name__)

# APIView CRUD example
class create_user(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        if not all([first_name, last_name, email]):
            return JsonResponse({"error": "Missing required fields"}, status=400)
        user = userProfile.objects.create(first_name=first_name, last_name=last_name, email=email)
        return JsonResponse({"message": "User created", "user_id": user.id}, status=201)
    
class read_user(APIView):
    def get(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            return JsonResponse({"id": user.id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email})
        except userProfile.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

class update_user(APIView):
    def put(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            user.first_name = request.data.get('first_name', user.first_name)
            user.last_name = request.data.get('last_name', user.last_name)
            user.email = request.data.get('email', user.email)
            user.save()
            return JsonResponse({"message": "User updated"})
        except userProfile.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

class delete_user(APIView):
    def delete(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            user.delete()
            return JsonResponse({"message": "User deleted"})
        except userProfile.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

class all_users(APIView):
    def get(self, request):
        users = userProfile.objects.all()
        users_data = [
            {
               "id": user.id, 
               "first_name": user.first_name, 
               "last_name": user.last_name, 
               "email": user.email
            }
            for user in users
        ]
        return JsonResponse(users_data, safe=False)

# APIView celery example
# class AddTask(APIView):
#     def get(self, request, x, y):
#           add_result = int(request.GET.get("x", 0)) + int(request.GET.get("y", 0))
#           # age = self.calAge(1990)
#           return JsonResponse({"result": add_result})
#     def calAge(self, birth_year):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - birth_year

# def multiply_task(request, x, y):
#      multiply_result = multiply.delay(x, y)
#      return JsonResponse({"result": multiply_result})