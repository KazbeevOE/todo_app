from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('todo_list.urls')),
    path('users/', include('users.urls')),
]
