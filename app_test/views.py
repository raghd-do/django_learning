from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import userProfile
from .tasks import  send_email
import logging
logger = logging.getLogger(__name__)

# APIView CRUD example
class create_user(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        if not all([first_name, last_name, email]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        user = userProfile.objects.create(first_name=first_name, last_name=last_name, email=email)
        self.send_welcome_email(user.id)
        return Response({"message": "User created", "user_id": user.id}, status=status.HTTP_201_CREATED)
    
    def send_welcome_email(self, user_id):
        try:
            user = userProfile.objects.get(id=user_id)
            subject = "Welcome to our platform!"
            message = f"Hi {user.first_name}, welcome to our platform. We're glad to have you here!"
            print(f"Scheduling welcome email for user_id {user.id}")
            send_email.delay(user.id, subject, message)
        except userProfile.DoesNotExist:
            logger.error(f"User with id {user_id} does not exist. Cannot send welcome email.")
    
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