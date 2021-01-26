from rest_framework.permissions import  BasePermission

from rest_framework.permissions import BasePermission

class IsAuthorPermission(BasePermission):
    """
    Check if user is a doctor.
    """

    message = "The user is not a doctor."

    def has_permission(self, request, view):
        return request.user.is_author

