from rest_framework import permissions

from todo_list.models import Board


class EmployeeOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        board_id = request.resolver_match.kwargs.get('board_id')
        board = Board.objects.get(id=board_id)
        return board.organization in request.user.organizations.all()
