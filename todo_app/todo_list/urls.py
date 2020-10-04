from django.urls import path

from .views import BoardCreateView, BoardListView, BoardEditView, \
    TaskListView, TaskEditView

urlpatterns = [
    path('boards/create/', BoardCreateView.as_view(), name='board_create'),
    path('boards/list/', BoardListView.as_view(), name='board_list'),
    path('boards/<int:board_id>/edit/', BoardEditView.as_view(), name='board_edit'),
    path('boards/<int:board_id>/tasks/list/', TaskListView.as_view(), name='task_list'),
    path('boards/<int:board_id>/tasks/<int:task_id>/edit/', TaskEditView.as_view(), name='task_edit')
]
