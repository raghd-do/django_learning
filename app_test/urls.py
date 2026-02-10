from django.urls import path
from . import views

urlpatterns = [
    # APIView CRUD example
    path('api/create_user', views.create_user, name='create_user'),
    path('api/read_user', views.read_user, name='read_user'),
    path('api/update_user', views.update_user, name='update_user'),
    path('api/delete_user', views.delete_user, name='delete_user'),
    path('api/all_users', views.all_users, name='all_users'),

    # APIView example
    path("api/add_task/<int:x>/<int:y>/", views.AddTask.as_view(), name="api_add_task"),
]