from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        user = userProfile.objects.create(first_name=first_name, last_name=last_name, email=email)
        return Response({"message": "User created", "user_id": user.id}, status=status.HTTP_201_CREATED)
    
class read_user(APIView):
    def get(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            return Response({"id": user.id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email})
        except userProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class update_user(APIView):
    def put(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            user.first_name = request.data.get('first_name', user.first_name)
            user.last_name = request.data.get('last_name', user.last_name)
            user.email = request.data.get('email', user.email)
            user.save()
            return Response({"message": "User updated"}, status=status.HTTP_200_OK)
        except userProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class delete_user(APIView):
    def delete(self, request, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
        except userProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

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
        return Response(users_data, status=status.HTTP_200_OK)

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