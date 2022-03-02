from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser


class IsSuperUser(BasePermission):
    safe_paths = ['/api/accounts/']

    def has_permission(self, request, view):
        return request.user.is_superuser or \
          bool(request.method == "POST" and
               request.path_info in self.safe_paths)


class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(obj == request.user or obj.user == request.user):
            return True
        return False