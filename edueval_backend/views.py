from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
from urllib.parse import urlencode

def logout_view(request):
    logout(request)
    return redirect(f"{settings.KEYCLOAK_BASE_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/logout?redirect_uri=http://localhost:8000/")

def force_login_view(request):
    query = urlencode({
        'response_type': 'code',
        'scope': 'openid email',
        'client_id': settings.OIDC_RP_CLIENT_ID,
        'redirect_uri': 'http://localhost:8000/oidc/callback/',
        'prompt': 'login',
        'state': 'state123',
        'nonce': 'nonce123',
    })
    return redirect(f"{settings.OIDC_OP_AUTHORIZATION_ENDPOINT}?{query}")

def filter_users_by_claims(self, claims):
    return self.UserModel.objects.filter(username=claims.get('preferred_username'))


@login_required
def home(request):
    return HttpResponse(f"🎉 ¡Hola {request.user.username}! Estás autenticado.")