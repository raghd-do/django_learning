from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect_view, name='redirect_view'),
    path("users/", views.user_profile, name="user_profile"),
    path("add_task/<int:x>/<int:y>/", views.add_task, name="add_task"),
    path("multiply_task/<int:x>/<int:y>/", views.multiply_task, name="multiply_task"),
    path("add_user/<str:first_name>/<str:last_name>/<str:email>/", views.add_user, name="add_user"),
]