from functools import wraps
from django.http import JsonResponse
from rest_framework.permissions import BasePermission

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_roles = getattr(request, 'keycloak_roles', [])
            if not any(role in user_roles for role in roles):
                return JsonResponse({"detail": "No autorizado"}, status=403)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

class IsCoordinador(BasePermission):
    def has_permission(self, request, view):
        return 'coordinador' in getattr(request, 'keycloak_roles', [])

class IsDocente(BasePermission):
    def has_permission(self, request, view):
        return 'profesor' in getattr(request, 'keycloak_roles', [])

class IsEvaluadorExterno(BasePermission):
    def has_permission(self, request, view):
        return 'evaluador' in getattr(request, 'keycloak_roles', [])
