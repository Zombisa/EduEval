# urls.py limpio
from django.contrib import admin
from django.urls import path, include
from edueval_backend.views import home, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/autenticacion/', include('apps.autenticacion.urls')),
    path('api/competencias-programa/', include('apps.competencias_programa.urls')),
    path('api/competencias-asignatura/', include('apps.competencias_asignatura.urls')),
    path('api/rubricas/', include('apps.rubricas.urls')),
    path('api/evaluaciones/', include('apps.evaluaciones.urls')),

    # Otros
    path('logout/', logout_view),
]
