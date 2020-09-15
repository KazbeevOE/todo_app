from django.urls import path

from .views import BoardCreateView, BoardListSerializer, BoardEditView, \
    TaskCreateView, TaskListView, TaskEditView

urlpatterns = [
    path('board/create/', BoardCreateView.as_view(), name='board_create'),
    path('board/list/', BoardListSerializer.as_view(), name='board_list'),
    path('board/<int:board_id>/edit/', BoardEditView.as_view(), name='board_edit'),
    path('board/<int:board_id>/task/create', TaskCreateView.as_view(), name='task_create'),
    path('board/<int:board_id>/task/list/', TaskListView.as_view(), name='task_list'),
    path('task/<int:task_id>/edit', TaskEditView.as_view(), name='task_edit')
]
