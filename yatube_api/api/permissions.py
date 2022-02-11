from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Пермишн, который проверяет является ли юзер автором поста."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
