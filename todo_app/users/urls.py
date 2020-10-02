from django.urls import path

from .views import RegisterUserView, EditUserView, AuthenticateUserView

urlpatterns = [
    path('create/', RegisterUserView.as_view()),
    path('edit/', EditUserView.as_view()),
    path('auth/', AuthenticateUserView.as_view()),
]
