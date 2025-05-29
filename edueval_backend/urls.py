from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from edueval_backend.views import home
from edueval_backend.views import logout_view, force_login_view

@login_required
def home(request):
    return HttpResponse(f"🎉 ¡Hola {request.user.username}! Estás autenticado.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    # Módulos del proyecto
    path('api/autenticacion/', include('apps.autenticacion.urls')),
    path('api/competencias-programa/', include('apps.competencias_programa.urls')),
    path('api/competencias-asignatura/', include('apps.competencias_asignatura.urls')),
    path('api/rubricas/', include('apps.rubricas.urls')),
    path('api/evaluaciones/', include('apps.evaluaciones.urls')),
    path('oidc/', include('mozilla_django_oidc.urls')),

]


urlpatterns += [
    path('logout/', logout_view),
    path('forzar-login/', force_login_view),
]
