from django.urls import path
from core import views

urlpatterns = [
    path('create', views.CreateUserView.as_view())
]
