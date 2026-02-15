from django.urls import path
from . import views

urlpatterns = [
    # APIView CRUD example
    path('api/create_user', views.create_user.as_view(), name='create_user'),
    path('api/read_user/<int:user_id>/', views.read_user.as_view(), name='read_user'),
    path('api/update_user/<int:user_id>/', views.update_user.as_view(), name='update_user'),
    path('api/delete_user/<int:user_id>/', views.delete_user.as_view(), name='delete_user'),
    path('api/all_users', views.all_users.as_view(), name='all_users'),
]