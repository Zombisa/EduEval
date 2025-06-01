import jwt
from django.http import JsonResponse
from django.conf import settings

class KeycloakRoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization', None)

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                # Decodificamos el JWT sin verificar la firma por ahora
                payload = jwt.decode(token, options={"verify_signature": False})

                # Extraer roles asignados al cliente específico (edueval-backend)
                client_id = "edueval-backend"
                request.keycloak_roles = (
                    payload.get("resource_access", {})
                    .get(client_id, {})
                    .get("roles", [])
                )

                # Extraer también el username (opcional pero útil)
                request.keycloak_username = payload.get("preferred_username")

            except jwt.DecodeError:
                return JsonResponse({"error": "Token inválido"}, status=401)
        else:
            request.keycloak_roles = []
            request.keycloak_username = None

        return self.get_response(request)
