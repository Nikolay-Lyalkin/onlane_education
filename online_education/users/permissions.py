from rest_framework.permissions import BasePermission


class CanUserUpdate(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object():
            return True
