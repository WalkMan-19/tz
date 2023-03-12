from rest_framework import permissions

from core.models import User


class CheckStatusPermission(permissions.BasePermission):
    message = 'Просматривать записи могут только активные пользователи'

    def has_object_permission(self, request, view, obj):
        if request.user.status == User.Status.archived:
            return False
        return True
