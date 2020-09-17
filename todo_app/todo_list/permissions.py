from rest_framework import permissions


class EmployeeOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.board.organization in request.user.organizations
