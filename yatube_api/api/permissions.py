from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Пермишн, который проверяет является ли юзер автором поста.
    IsOwnerOrReadOnly: allows the owner of an object to edit or delete it,
    but allows read-only access to others"""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
