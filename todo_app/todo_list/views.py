from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from .models import Board, Task
from .permissions import EmployeeOnly
from .serializers import BoardDetailSerializer, TaskDetailSerializer


class BoardCreateView(generics.CreateAPIView):
    serializer_class = BoardDetailSerializer
    permission_classes = (IsAdminUser,)


class BoardListView(generics.ListAPIView):
    serializer_class = BoardDetailSerializer
    permission_classes = (AllowAny,)
    queryset = Board.objects.all()


class BoardEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardDetailSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'


class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated, EmployeeOnly,)

    def get(self, request, *args, **kwargs):
        user_current_organization = request.data['organization']
        organization = Board.objects.filter(id=self.kwargs['board_id']).first().organization

        if user_current_organization == organization.name:
            return self.list(request, *args, **kwargs)

        else:
            res = {
                'error': 'You should authenticate as an organization employee'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        return Task.objects.filter(board=self.kwargs['board_id'])


class TaskEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated, EmployeeOnly,)

    def get_object(self):
        return Task.objects.get(id=self.kwargs['task_id'], board=self.kwargs['board_id'])
