from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser

class KeycloakOIDCAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return None  # Permite que otros autenticadores se encarguen

        token = token.split(" ")[1]

        # Verificamos que el middleware haya guardado los roles
        roles = getattr(request, 'keycloak_roles', None)
        if roles is None:
            raise AuthenticationFailed("Token no válido o no procesado")

        # Devuelve un usuario simulado con roles (puedes mejorar esto)
        user = AnonymousUser()
        user.roles = roles
        return (user, None)

    def authenticate_header(self, request):
        return 'Bearer'