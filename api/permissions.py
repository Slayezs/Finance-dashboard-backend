from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.role == 'admin':
            return True

        if user.role == 'analyst':
            return request.method in ['GET','POST']

        if user.role == 'viewer':
            return request.method == 'GET'

        return False
    
class IsAdminUserCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'