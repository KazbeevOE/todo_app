from django.urls import path

from .views import CreateUserAPIView

url_patterns = [
    path('create/', CreateUserAPIView.as_view()),
]
