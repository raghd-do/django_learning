from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect_view, name='redirect_view'),
    path("users/", views.user_profile, name="user_profile"),
]