from rest_framework import permissions


class IsDoctor(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.user.type == 'doctor':
            return True
        return False


class IsOperator(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.user.type == 'operator':
            return True
        return False


class IsAdmin(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.user.type == 'admin':
            return True
        return False

