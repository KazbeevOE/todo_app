from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Board, Task
from .permissions import EmployeeOnly
from .serializers import BoardDetailSerializer, BoardListSerializer, \
    TaskDetailSerializer, TaskListSerializer, TaskChangeSerializer


class BoardCreateView(generics.CreateAPIView):
    serializer_class = BoardDetailSerializer
    permission_classes = (IsAdminUser,)


class BoardListView(generics.ListAPIView):
    serializer_class = BoardListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()


class BoardEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardDetailSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated,)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, EmployeeOnly,)

    def get_queryset(self):
        return Task.objects.filter(board=self.kwargs['board_id'])


class TaskEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskChangeSerializer
    permission_classes = (IsAuthenticated, EmployeeOnly,)
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'
