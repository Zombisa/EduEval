from functools import wraps
from django.http import JsonResponse
from rest_framework.permissions import BasePermission

def user_in_roles(user, roles):
    return user.is_authenticated and user.groups.filter(name__in=roles).exists()

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not user_in_roles(request.user, roles):
                return JsonResponse({"detail": "No autorizado"}, status=403)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

class IsCoordinador(BasePermission):
    def has_permission(self, request, view):
        return user_in_roles(request.user, ['coordinador'])

class IsDocente(BasePermission):
    def has_permission(self, request, view):
        return user_in_roles(request.user, ['profesor'])

class IsEvaluadorExterno(BasePermission):
    def has_permission(self, request, view):
        return user_in_roles(request.user, ['evaluador'])
