from django.urls import path

from .views import CreateUserAPIView, EditUserView, LogoutUserView, authenticate_user

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('edit/', EditUserView.as_view()),
    path('login/', authenticate_user),
    path('logout/', LogoutUserView.as_view()),

]
